# Critical review protocol / Правила независимой критики

**Goal:** attempt to refute the methodology with reproducible, independently checkable objections. Positive results are welcome only when the test design and limitations are explicit.

## What to challenge
- **Prior art:** a published mechanism or software system that already implements the claimed combination.
- **False Proceed:** an action incorrectly allowed despite an unmet blocking obligation.
- **False Stop:** a safe, independent action incorrectly blocked.
- **Evidence laundering:** a weak, obsolete, mock or not-executed result promoted to stronger proof.
- **TRIZ counterexample:** the contradiction method is inapplicable, counterproductive or worse than ordinary trade-off analysis.
- **Oracle/evaluation flaw:** wrong answer key, missing failure mode, contamination or invalid outcome measure.
- **Economic failure:** extra review, latency and rework exceed measurable benefits.

## Minimum issue format
1. **Claim or rule:** reference METHODOLOGY.md section, VO/Stop Gate ID.
2. **Situation / task and requested action.**
3. **Object version / level / dependency scope.**
4. **Actual behavior and evidence** (safe reproducer, logs, prompts, parameters if applicable).
5. **Expected outcome and reason.**
6. **Impact / risk / severity.**
7. **Prior art or alternative explanation**, if available.
8. **What evidence would settle the disagreement?**

## Adjudication
OPEN → NEEDS_EVIDENCE → ACCEPTED / REJECTED_WITH_REASON / DUPLICATE.

For accepted objections publish affected clauses, rationale, impact on earlier results, amended text, and version diff. Do not change the answer key *after looking at runs* without recording and separating the changes. Negative findings must be included in public summaries.

## Ethical boundaries
No real credentials, personal data, proprietary source, destructive production operations, or sensitive customer documents. Reproduce on mocks or synthetic datasets when necessary. Never interpret absent evidence as PASS.

## Important note
The 22 author-written scenarios are internal conformance materials; their evaluator key is *not* public. Public criticism should preferably include **new independently devised cases**, not memorize existing prompts.
