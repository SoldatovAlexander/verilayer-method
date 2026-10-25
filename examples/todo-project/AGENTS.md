# Instructions for Codex / OpenCode / agents reading AGENTS.md

This folder is a **standalone example project**; it is not the root of the methodology repository. Always read \`VERILAYER_RULES.md\` and \`PROJECT_BRIEF.md\` before changing software or claiming a gate decision.

Follow VeriLayer Method v0.5: design ↔ verifiability on L0–L5; TRIZ analysis only for **material** contradictions; scoped VO + evidence; local S01–S12 Stop Gates; four independent states (VO, verification run, gate, action). Use Lite by default for small reversible work, and raise rigor with risk.

Never turn NOT_RUN or INFRA_BLOCKED into PASS or failed product code. Never call architectural review a system acceptance test. Continue safe unrelated work even if the requested release is blocked. Do not invent tool results, evidence, CI URLs, or approvals.

**Exercise:** To-Do List with reversible delete, local persistence and acceptance criteria; see \`PROJECT_BRIEF.md\`.

Before proposing release, run actual relevant tests and evaluate \`python tools/check_gate.py .verilayer/fixtures/<chosen-fixture>.json\` only as an *educational metadata check* (it neither authenticates evidence nor enforces tool permissions). Report PASS/BLOCKED and exact scope, not unsupported claims of completed real-world verification.
