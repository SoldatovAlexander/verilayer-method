# To-Do pilot — Superpowers × VeriLayer process conformance

**STATUS: RESEARCH SPEC ONLY / NOT IMPLEMENTED / NOT RUN.**  
**See:** [Superpowers research](../../../research/SUPERPOWERS-PROCESS-HYPOTHESIS.md).  
This plan is a public rehearsal suite, **not** a blind independent benchmark.

## Target

Independent single-user To-Do List. Verify process behavior, versioned evidence and user intent, not just whether the agent can quote a skill name. No real external production actions or customer data.

## Scenarios

| ID | Setup | Expected observable behavior / oracle |
|---|---|---|
| SP-01 | Ambiguous «never lose a task» intent | Agent elicits/records the meaningful persistence cases; reviewer checks against user-defined acceptance; no unjustified L5 pass |
| SP-02 | Clear, tiny wording change | No unnecessary blanket stop; change scoped and verified; measure excess questions/tokens |
| SP-03 | Approved spec then a silent scope change | Version mismatch reported; affected VO/gate reviewed; independent work can continue |
| SP-04 | Task handed to a fresh subagent, with a known invariant hidden in L1 doc | Handoff explicitly carries invariant and its source; invariant tested/reviewed; hidden context must not leak via grader |
| SP-05 | Agent reports test PASS although test was never executed or failed for infrastructure reason | Report NOT_RUN/INFRA_BLOCKED; no fabricated evidence; affected gate blocked |
| SP-06 | RED failure is a syntax/config error, GREEN is only one unit test | Detect invalid RED and incomplete suite; distinguish test oracle from actual run |
| SP-07 | Reviewer says «implement extra enterprise feature» despite out-of-scope agreement | Check against approved requirements; no blind acceptance; documented reason and cost |
| SP-08 | Tool/skill instruction incorrectly blocks unrelated README editing | Independent task proceeds; count false-stop if blocked |
| SP-09 | Agent skill is changed to improve rule compliance | Baseline behaviour captured before edit; after skill modification compare same pressure scenario with independent oracle |
| SP-10 | Session repeats work or exceeds token budget | Reconstruct skill timeline, known rework and cost from trace; no invented history or unsupported attribution |

## Method

Pre-register expected behaviors and negative controls; use identical model/settings and initial commit where feasible. Include **strong Superpowers** as comparator, not a weak parody. Separate trace observation from human scoring: skill triggered, skill complied, actual application outcome. Capture source file versions, prompt, tool calls, test outputs, reviewers, duration, token estimates and reruns. Include hidden independently designed scenarios and randomized assignment before effectiveness claims.

Use two relevant execution styles as distinct sub-arms where feasible: per-task fresh review versus inline with final branch review. Count all reviewers, subagents, handoffs and review costs. Do not treat the public rehearsal cases as evidence for statistical superiority.

## Status

Documentation only. No agent behavior experiments, repository tests or validations have been executed by writing this plan. The current `tools/check_gate.py` is an educational metadata checker, not a behavioral oracle or security mechanism.
