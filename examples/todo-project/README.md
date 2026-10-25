# VeriLayer Method v0.5 — Agent Starter Kit / Пример конфигураций

**Standalone demonstration, not a deployable agent framework.** This directory is meant to be copied into the **root of a new or disposable project**. The outer `verilayer-method` repository is a research/publication repository; its instructions do not automatically govern a separate software repository.

## What you get / Состав

| Agent/tool | Native file in this starter | Notes |
|---|---|---|
| OpenAI Codex | [`AGENTS.md`](AGENTS.md) | Project instructions |
| OpenCode | [`AGENTS.md`](AGENTS.md) | Reuses the same project instructions |
| Claude Code | [`CLAUDE.md`](CLAUDE.md) | Project memory/instructions |
| Cline | [`.clinerules/01-verilayer.md`](.clinerules/01-verilayer.md) | Project Cline Rule |
| Cursor | [`.cursor/rules/verilayer.mdc`](.cursor/rules/verilayer.mdc) | `alwaysApply` rule |
| GitHub Copilot | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | Repository-wide guidance |

All adapters point to [`VERILAYER_RULES.md`](VERILAYER_RULES.md) rather than copying different interpretations of the core. The [brief](PROJECT_BRIEF.md) defines an independent single-user To-Do exercise; [`.verilayer/TEMPLATES.md`](.verilayer/TEMPLATES.md) shows draft VO/CAR/Evidence/Gate records.

**Language:** Agent rules are written in English for portability; users may work with the agent in Russian. Output language is not prescribed by the protocol.

## Quick Start / Быстрый старт

Prerequisites: Git, one coding agent, Python 3.9+ to run the **optional** local demo checker. Python or a validator is not required to read/use the agent instructions.

**Option A: start a new empty test project (recommended).**

```bash
git clone https://github.com/SoldatovAlexander/verilayer-method.git
cp -R verilayer-method/examples/todo-project ./todo-verilayer-lab
cd todo-verilayer-lab
python -m unittest discover -s tests -v
python tools/check_gate.py .verilayer/fixtures/block-not-run.json
# exit code 2 is expected for BLOCKED
```

**Option B: adapt an existing software project.** Copy the core file, brief/templates, and only the native file for the agent you use. **Do not overwrite** existing `AGENTS.md`, `CLAUDE.md`, `.clinerules`, `.cursor/rules` or `.github/copilot-instructions.md` without merging rules and checking precedence. Reference the full published [methodology](../../METHODOLOGY.md).

Open the new `todo-verilayer-lab` folder as the **workspace/project root** in the agent tool, then start a fresh session so rules are loaded.

## Ready-to-use prompts / Стартовые запросы

**Prompt 1 — scope and verification:**

> Изучи PROJECT_BRIEF.md и VERILAYER_RULES.md. Предложи проработку To-Do List от L0 до L3. Для каждого важного утверждения опиши, каким свидетельством его можно проверить. Не пиши исполняемые тесты до появления соответствующего интерфейса/кода. Не объявляй готовность без выполненной проверки.

**Prompt 2 — material TRIZ contradiction:**

> Пользователь должен мгновенно удалять задачу, но иметь возможность исправить случайное удаление. Проведи CR-1…CR-7: точное противоречие, ИКР, доступные ресурсы, минимум два разных решения, компромиссы, новые VO, что решает владелец продукта. Не подменяй поиск решения доказательством его корректности.

**Prompt 3 — the gate / локальная остановка:**

> Проверь пример .verilayer/fixtures/block-not-run.json. Объясни отдельно VO state, verification run, Gate и agent action. Можно ли выпускать удаление задач? Можно ли независимо от этого исправить текст README? Запусти локальный валидатор как учебную демонстрацию, без реального выпуска и без выдуманных CI-доказательств.

For consistent cross-agent comparison, use **the same model class, task, repository state, budgets and approvals** where possible, then compare output with [`PROMPTS_AND_EXPECTATIONS.md`](PROMPTS_AND_EXPECTATIONS.md). Do not reveal hidden answers to a system being independently benchmarked.

## Gate metadata demo / Проверяемый учебный пример

```bash
python -m unittest discover -s tests -v
python tools/check_gate.py .verilayer/fixtures/pass-verified.json
python tools/check_gate.py .verilayer/fixtures/block-not-run.json
python tools/check_gate.py .verilayer/fixtures/block-stale-evidence.json
python tools/check_gate.py .verilayer/fixtures/pass-independent-work.json
```

Exit statuses: `0` = PASS, `2` = BLOCKED, `3` = invalid input/error. JSON `ci://EXAMPLE-ONLY/123` is an explicitly **synthetic placeholder**; the program does **not** authenticate CI, approvals, artifact hashes, reviewers or permission to execute commands. All four example fixtures are *fictional*; a successful demo is not evidence of a real code run.

The current Python checker is deliberately a **limited subset** of the formal proposal: it checks VO/evidence scope, version, declared run outcome and source-ref **presence** only. It does **not** implement all 12 Stop Gates, conditional passes, provenance verification, real waiver authorization, CI integration or tool authorization. A malicious agent can forge JSON. Real Critical gate enforcement requires independent trusted controls outside the coding agent.

## What to report when testing an agent

Record tool/version/model, initial workspace revision, risk profile, prompt, relevant rule-file loading, token/time budget, actual commands run, actual outputs, proposed VO/CAR, gate decision for **each requested action**, instances of False Proceed / False Stop, and cost. Separate (1) adherence to the protocol from (2) improvement in delivered software quality.

Found a rule that causes harm, unnecessary blocking, poor TRIZ decisions or missing evidence? [Open a reproducible counterexample](https://github.com/SoldatovAlexander/verilayer-method/issues/new/choose). See [experiment protocol](../../EXPERIMENT_PROTOCOL.md) for fair comparisons.

## License

**Instruction texts, templates and explanatory documentation:** [CC BY 4.0](../../LICENSE). **Python executable and test fixtures:** [Apache 2.0](../../LICENSE-CODE). Details: [licensing scope](../../LICENSE.md).

## Official adapter references (checked Oct 2026)

- [Cline rules / docs](https://docs.cline.bot/)
- [Cursor project rules](https://cursor.com/docs/rules)
- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [OpenCode rules](https://docs.opencode.ai/docs/rules/)
- [Claude Code CLAUDE.md](https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts)
- [GitHub Copilot repository instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
