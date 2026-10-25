# VeriLayer working record templates (human-facing examples)

These are **illustrative**, not a stable schema. Refer to sections 11–17 of public \`METHODOLOGY.md\` for definitive semantics. Do not fill unknown facts with fabricated results.

## Verification Obligation (VO)
\`\`\`yaml
id: VO-DELETE-01
claim: "Undo restores an accidentally deleted task within the approved interval"
source: PROJECT_BRIEF.md
artifact_id: TaskStore
version: "1.0"
origin_level: L0
target_level: L5
expected_evidence: "acceptance scenario + restart/failure check"
verification_method: "integration + E2E"
blocking_gate: release
dependencies: [task-delete]
risk_profile: Standard
owner: product-owner
reviewer: independent-reviewer
status: PLANNED
evidence_refs: []
residual_risk: "Undo window remains to be approved"
linked_car: CAR-DELETE-01
\`\`\`

## Contradiction Analysis Record (CAR)
\`\`\`yaml
car_id: CAR-DELETE-01
source: [user_needs_fast_delete, user_needs_undo]
level: L1
scope: task-delete
improves: deletion_latency
worsens: risk_of_irreversible_loss
ideal_result: "Task disappears instantly yet can be restored"
resources: [local_storage, ui_undo_action, action_log]
strategies:
  - soft_delete_and_undo
  - confirmation_before_delete
tradeoffs: "Undo adds retention requirements; dialog increases clicks"
harmful_effects: "Accidental disclosure in retained data needs review"
linked_vo: [VO-DELETE-01]
proposed_evidence: [unit_tests, acceptance_scenarios, restart_recovery]
owner: product-owner
status: OPEN
\`\`\`

## Evidence Record
\`\`\`yaml
id: EV-DELETE-01
vo_id: VO-DELETE-01
object_version: "1.0"
scope: task-delete
method: e2e
run_status: NOT_RUN  # do not call it PASS
source_ref: ""  # MUST be a real retrievable report, not a placeholder
reviewer: ""
result: INCONCLUSIVE
limitations: "No integration run performed yet"
\`\`\`

## Gate Decision
\`\`\`yaml
action_id: release_task_delete
scope: task-delete
requested_level: L5
gate: release
gate_status: BLOCKED
agent_action: INVESTIGATE
reasons: [S05, S08]
required_vo_ids: [VO-DELETE-01]
allowed_parallel_work: [edit_unrelated_readme]
authority: product-owner
\`\`\`

**Critical note:** \`tools/check_gate.py\` expects a simpler JSON **teaching fixture** rather than the full YAML record format above. It has intentionally no cryptographic trust, ACL checking, waiver handling or production authorization. JSON fixtures should never be used as proof that a live CI run occurred.
