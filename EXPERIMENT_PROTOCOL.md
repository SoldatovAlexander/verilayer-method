# Experiment protocol — preregistration draft v0.5

**Status:** Proposal for independent preregistration; **no experiments have been run or validated**.

## Research questions
- RQ1: Does VeriLayer reduce critical unsupported *False Proceed* actions?
- RQ2: Does it preserve safe throughput by avoiding *False Stop*?
- RQ3: Does adding TRIZ to the defined contradiction workflow improve engineering outcomes over ordinary trade-off analysis?
- RQ4: Are gains worth the total time, tokens, review and rework costs?

## Comparison arms
- **A: Ordinary agent** — good-faith engineering baseline with regular safety constraints, no VeriLayer instructions.
- **B: Strong spec-driven process** — correctly configured GitHub Spec Kit or OpenSpec, not an artificially weak comparator.
- **C: VeriLayer core** — L0–L5, VO, scoped evidence and S01–S12; *without* TRIZ contradiction resolution, as ablation.
- **D: VeriLayer + TRIZ** — the v0.5 proposed protocol (the **main proposal**).
- **E (optional): VeriLayer + ordinary trade-off analysis** — controls for more thinking/time rather than TRIZ specifically.

## Stages
0. Register hypotheses, allowed actions, interpretation and scoring rules **before** observing outputs.
1. Independent two-reviewer adjudication of existing 22 case answers and at least one new holdout suite.
2. Feasibility smoke test of 8 cases (4 blocks, 4 safe actions).
3. Isolated conformance runs with randomized order. Minimum repeats are *feasibility*, not a statistical power claim.
4. Comparative end-to-end development tasks: small To-Do app, contract API, state/failure handling, UX scenario and a non-deterministic component.
5. Blind evaluation and public release of negative and positive outcomes.

## Primary outcome and guardrails
Primary: **Critical False Proceed Rate**, with **False Stop Rate** and full **cost to accepted change** as prespecified guardrails. Evaluate scope correctness separately. Report severity-weighted results and confidence intervals, not just a single scoreboard.

Measure all generation/review/rework time, tokens and tool usage. Compare at matched budgets and with independent reviewers. A low FPR achieved solely by halting everything is *not* a success.

## Leakage / benchmark integrity
Freeze repository state and requirements per task. Do not disclose future fixes or the evaluator key. Isolate sessions and randomly assign arms. Vet hidden tasks, ambiguous acceptance criteria, wrong oracles and fixture failures. Keep raw traces and adjudication logs. Report baseline quality and deviations.

## What would falsify the thesis?
No material gain over active baseline B; excessive false stops or cost; benefits disappear on independently authored tasks; inability to reproduce gate decisions; or inability to enforce dangerous-operation decisions beyond free-text responses.

## TRIZ incremental test
The relevant comparison is **C versus D** and ideally **D versus E**, *with actual substantive engineering contradictions*. Primary: architectural validity, absence of invariant violations, independent reviewer outcomes, rework and total cost. Idea count is not sufficient evidence.

## Reproducibility artifacts
Task inputs, object/version hashes, model settings, tool outputs, decisions, timestamps, evaluator rubrics, review disagreements, and all accepted/rejected evidence. No claim of statistical superiority until power and sampling support it.
