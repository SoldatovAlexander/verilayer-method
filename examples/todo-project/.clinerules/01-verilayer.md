# Cline project rule — VeriLayer v0.5

Start by reading \`VERILAYER_RULES.md\` and \`PROJECT_BRIEF.md\`. This is a practice configuration, not an enforced security control.

- Plan in L0–L5: requirements ↔ verification methods together. Introduce executable tests as code becomes testable.
- For every material conflict, run TRIZ CR-1…CR-7, compare two meaningfully distinct options and link the result to VO; do not treat TRIZ itself as evidence.
- Record a scoped, versioned VO for important unsatisfied claims. Evidence requires provenance and the correct source/test version.
- Keep separate VO, test-run, gate and action statuses. NOT_RUN/INFRA_BLOCKED never mean PASS.
- Apply S01–S12 as *action-specific* Stop Gates. A release may be BLOCKED while safe independent documentation continues.
- No unapproved destructive commands, hidden acceptance-criteria changes, fabricated CI results, or self-authorized waiver.
- Provide the standard handoff defined in \`VERILAYER_RULES.md\` after each task.

Before running commands or changing files, respect Cline's actual approval controls. Prompt instructions alone do not enforce approvals.
