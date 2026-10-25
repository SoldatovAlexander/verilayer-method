# VeriLayer v0.5 — common agent protocol (example)

**Status:** educational agent instructions, not an enforceable security policy or proof of research effectiveness.
**Source of truth:** [published methodology](../../METHODOLOGY.md) — in the source repository follow the link to \`METHODOLOGY.md\`; after copying this starter to a new project use https://github.com/SoldatovAlexander/verilayer-method/blob/main/METHODOLOGY.md.

## Principles (P1–P8)
1. Work at the level of the claim: L0 needs/user value; L1 system; L2 components; L3 contracts/invariants; L4 executable implementation; L5 integrated acceptance. Review at L1 is not evidence of an L5 runtime claim.
2. For each nontrivial decision, develop **design and its method of verification together**. Do not require executable tests before relevant interfaces/code exist.
3. Open a versioned **Verification Obligation (VO)** when an important claim remains unverified. Record \`id, claim, source, artifact_id, version, origin_level, target_level, expected_evidence, verification_method, blocking_gate, dependencies, risk_profile, owner, reviewer, status, evidence_refs, residual_risk\`; optionally \`linked_car\`.
4. Identify material contradictions: if improving an important quality or satisfying one binding requirement conflicts with another, perform **TRIZ CR-1…CR-7**: detect, frame, idealize, identify resources, generate ≥2 genuinely distinct alternatives, compare harms/costs and new VOs, decide and revisit after evidence. Lightweight analysis is sufficient for Lite tasks. TRIZ suggestions are **not verification evidence**.
5. Keep **four independent state axes**:
   - VO: OPEN / PLANNED / SUPPORTED / VERIFIED / FAILED / WAIVED
   - Verification run: NOT_RUN / EXECUTED_PASS / EXECUTED_FAIL / INFRA_BLOCKED / INCONCLUSIVE
   - Gate: PASS / CONDITIONAL_PASS / BLOCKED / ESCALATED
   - Agent action: PROCEED / REVISE / INVESTIGATE / ESCALATE
6. **Scope-specific gates S01–S12:** apply to the requested action and only its real dependencies. S01 unclear goal; S02 contradictory requirements; S03 architecture constraint breach; S04 no oracle; S05 blocking VO; S06 evidence mismatch; S07 failed test; S08 not run/infrastructure issue; S09 improper criteria change; S10 irreversible risk/no authority; S11 stale traceability; S12 failed acceptance.
7. A failing or missing check blocks only the **dependent** merge/release/unsafe operation. Continue provably independent reading, documentation and reversible exploration.
8. For any claimed PASS report evidence **source, object version, scope and limits**. Never fabricate a run, CI URL or human approval. \`WAIVED\` is not \`VERIFIED\`; \`INFRA_BLOCKED\` is not a product failure.

## Standard work loop
**Context → Design ↔ Verifiability → Contradiction check/TRIZ if material → VO/Evidence → Gate decision → Allowed next action → Handoff.**

Before coding: restate goal and risk profile (Lite/Standard/Critical); inventory existing claims, requirements, versions, and dependent actions; specify checks that could disprove your design.
During coding: create executable tests when corresponding code exists; preserve the origin of test oracles; record failures as failures.
Before any high-impact external action: require independent authorization and tool-enforced permissions. The educational \`tools/check_gate.py\` only checks self-reported metadata consistency and **must not** be treated as authorization.

## Reply/handoff template
- **Level / scope / requested action:**
- **Assumptions and unresolved requirements:**
- **Design + corresponding verification method:**
- **Contradictions / CAR (if material):**
- **VO IDs / evidence refs, versions, actual run status:**
- **Gate result and why (S01–S12 as relevant):**
- **Allowed next action / allowed independent work:**
- **Open risk / owner / reviewer:**

## Stop and escalation
Do not silently edit acceptance criteria, change a blocking requirement, disable a failing test, invent evidence, or authorize irreversible operations. Ask the authorized owner when information or authority is missing. Explicitly report an inability to check something.
