#!/usr/bin/env python3
"""Illustrative VeriLayer gate consistency checker; NOT a security boundary."""
import argparse
import json
import sys
from pathlib import Path


def decide(record):
    """Return a local, scoped decision from declared VO and evidence metadata."""
    action = record.get("action")
    required = record.get("required_vo_ids")
    obligations = record.get("verification_obligations")
    evidence = record.get("evidence")
    if not isinstance(action, dict) or not all(isinstance(action.get(k), str) and action[k] for k in ("id", "scope", "artifact_version")):
        raise ValueError("action requires nonempty id, scope, artifact_version")
    if not isinstance(required, list) or any(not isinstance(x, str) or not x for x in required):
        raise ValueError("required_vo_ids must be a list of nonempty strings")
    if len(required) != len(set(required)):
        raise ValueError("duplicate required VO ids")
    if not isinstance(obligations, list) or not isinstance(evidence, list):
        raise ValueError("verification_obligations and evidence must be lists")
    for entry in obligations + evidence:
        if not isinstance(entry, dict) or not isinstance(entry.get("id"), str):
            raise ValueError("obligations and evidence must have string IDs")
    vo_by_id = {v["id"]: v for v in obligations}
    ev_by_id = {e["id"]: e for e in evidence}
    if len(vo_by_id) != len(obligations) or len(ev_by_id) != len(evidence):
        raise ValueError("duplicate obligation/evidence IDs")
    blockers = []
    for vo_id in required:
        vo = vo_by_id.get(vo_id)
        if vo is None:
            blockers.append(f"{vo_id}: missing obligation (S05)")
            continue
        if vo.get("scope") != action["scope"] or vo.get("artifact_version") != action["artifact_version"]:
            blockers.append(f"{vo_id}: stale/different VO scope or version (S11)")
            continue
        if vo.get("status") != "VERIFIED":
            blockers.append(f"{vo_id}: status {vo.get('status', 'ABSENT')} is not VERIFIED (S05)")
            continue
        refs = vo.get("evidence_refs")
        if not isinstance(refs, list) or not refs:
            blockers.append(f"{vo_id}: VERIFIED lacks evidence references (S06)")
            continue
        for ev_id in refs:
            ev = ev_by_id.get(ev_id)
            if ev is None or ev.get("vo_id") != vo_id or ev.get("scope") != action["scope"] or ev.get("artifact_version") != action["artifact_version"]:
                blockers.append(f"{vo_id}: missing/mismatched evidence {ev_id} (S06/S11)")
                continue
            if ev.get("result") != "PASS" or ev.get("run_status") not in ("EXECUTED_PASS", "REVIEW_APPROVED"):
                blockers.append(f"{vo_id}: evidence {ev_id} was not a successful verification (S07/S08)")
            if not isinstance(ev.get("source_ref"), str) or not ev["source_ref"].strip():
                blockers.append(f"{vo_id}: evidence {ev_id} has no provenance source_ref (S06)")
    allowed = not blockers
    return {"gate": "PASS" if allowed else "BLOCKED", "agent_action": "PROCEED" if allowed else "INVESTIGATE", "action_id": action["id"], "scope": action["scope"], "blockers": blockers, "note": "Untrusted educational metadata check. Does not authenticate evidence or enforce tool permissions."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path, help="JSON gate request fixture")
    args = parser.parse_args()
    try:
        result = decide(json.loads(args.record.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 3
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["gate"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
