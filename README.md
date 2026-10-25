# VeriLayer Method

**Abstraction-aligned verification, TRIZ contradiction resolution and evidence-governed decisions for AI-assisted software development.**

![Status](https://img.shields.io/badge/status-public--review-orange)
![Version](https://img.shields.io/badge/method-v0.5-blue)
![TRIZ](https://img.shields.io/badge/TRIZ-integrated-7e57c2)
![Evidence](https://img.shields.io/badge/evidence-experiments--pending-yellow)
[![Docs License](https://img.shields.io/badge/docs-CC%20BY%204.0-green)](LICENSE)
[![Code License](https://img.shields.io/badge/code-Apache%202.0-blue)](LICENSE-CODE)

## Project Description / Описание проекта

**EN:** VeriLayer Method (provisional working name) is a **public research draft** of a development approach for people and AI coding agents. Design and ways to verify it evolve together at each level of abstraction. When a significant engineering contradiction appears, a **TRIZ-based resolution loop** helps generate alternatives; evidence and local **Stop Gates** determine which agent actions can proceed. This is an **open, falsifiable hypothesis** — not a certified standard, deployed framework or proven improvement.

**RU:** VeriLayer Method — исследовательская методология разработки с участием человека и AI-агентов. На каждом уровне абстракции проектное решение уточняется **одновременно со способом проверки**. Существенные инженерные противоречия исследуются с помощью **ТРИЗ**, а проверочные обязательства (VO), свидетельства (Evidence) и **локальные Stop Gates** определяют, какие действия агент вправе продолжать. Эффективность подхода пока **не подтверждена экспериментально**. Название VeriLayer — рабочее, без завершённой юридической проверки товарного знака.

## Features / Основные элементы

- **L0–L5:** потребности → система → компоненты → контракты → код → интегрированная система; верификация соответствует уровню утверждения.
- **Design ↔ Verifiability:** проектирование и поиск способов проверки влияют друг на друга; исполняемые тесты создаются при появлении кода.
- **TRIZ / ТРИЗ:** формулировка существенного противоречия → ИКР → доступные ресурсы → альтернативы → оценка новых VO.
- **Verification Obligations (VO):** обязательства проверки с происхождением, версией объекта, уровнем, владельцем и границами применимости evidence.
- **12 Stop Gates (S01–S12):** локальное ограничение зависимого действия вместо остановки всего проекта.
- **Agent decisions:** `PROCEED`, `REVISE`, `INVESTIGATE`, `ESCALATE`; решение должно иметь доказательное основание.
- **Risk tailoring:** профили `Lite`, `Standard`, `Critical`, без одинаково тяжёлых процедур для всех задач.
- **Independent critique:** ищем `False Proceed`, `False Stop`, устаревшие evidence, неверные оракулы, предыдущие аналоги и отрицательные результаты.

## Architecture / Логика методологии

```text
                    Context / Requirements
                              │
                              ▼
            ┌─────────────────────────────────┐
            │ Design  ↔  Verifiability         │
            │            ↕                    │
            │ TRIZ contradiction resolution   │
            │ (only when conflict is material)│
            └────────────────┬────────────────┘
                             │
                     Verification Obligations
                             │
                    Evidence + scope + version
                             │
                   Local Stop Gate (S01–S12)
                             │
                ┌────────────┴───────────┐
                ▼                        ▼
          PROCEED / REVISE     INVESTIGATE / ESCALATE
                │                        │
                └──────────► Handoff ◄───┘
```

A gate blocks **only the dependent action**. Architectural review must not be presented as runtime test evidence. `NOT_RUN` is not `PASS` or a product failure.

## Agent Starter Kit / Конфигурации для агентов

**[Готовый пример To-Do List с инструкциями для Cline, Cursor, Codex, OpenCode, Claude Code и GitHub Copilot](examples/todo-project/README.md).**

В комплекте: общий протокол `VERILAYER_RULES.md`, нативные файлы правил каждого инструмента, brief, CAR/VO/Evidence/Gate шаблоны, четыре синтетических JSON-сценария и учебный Python checker с unit-тестами. Для быстрой проверки:

```bash
git clone https://github.com/SoldatovAlexander/verilayer-method.git
cp -R verilayer-method/examples/todo-project ./todo-verilayer-lab
cd todo-verilayer-lab
python -m unittest discover -s tests -v
```

**Важно:** Это обучающий starter kit, а не готовый агентный runtime и не сертифицированный policy enforcement. Проверка не аутентифицирует CI/evidence и не заменяет внешние разрешения для опасных операций. Примеры не доказывают экспериментальную эффективность методологии.

## Quick Start / С чего начать

VeriLayer v0.5 is **a documented methodology, not an installable CLI or running agent framework**. To explore or challenge it:

1. Read the [full method (RU)](METHODOLOGY.md): L0–L5, TRIZ, VO, evidence and Stop Gates.
2. Use the [evaluation protocol](EXPERIMENT_PROTOCOL.md) to define comparable baselines and negative outcomes **before** running tests.
3. Review the [critical review rules](REVIEW_GUIDE.md).
4. Submit a [counterexample, prior art or TRIZ critique](https://github.com/SoldatovAlexander/verilayer-method/issues/new/choose).
5. Follow the [public falsification thread — Issue #1](https://github.com/SoldatovAlexander/verilayer-method/issues/1).

**RU:** Не требуется ничего устанавливать. Начните с текста методологии, проверьте один конкретный тезис и откройте Issue с воспроизводимым контрпримером.

## Tests & Validation / Испытания

**Current status: NOT RUN.** Prepared author-written cases (`C01–C22`) and their evaluator-only key are not published as validated results. Their key is withheld to reduce contamination. No performance, safety or productivity benefits are claimed as measured.

We intend to compare:

| Arm | Process | Primary purpose |
|---|---|---|
| A | Ordinary agent workflow | Basic reference |
| B | Strong spec-driven workflow (Spec Kit / OpenSpec) | Serious competing practice |
| C | VeriLayer core without TRIZ | Ablation: effect of verification and gates |
| D | VeriLayer + TRIZ (v0.5) | Full proposed method |
| E (optional) | VeriLayer + conventional trade-off analysis | Control for extra deliberation |

Primary outcomes: **critical False Proceed**, **False Stop**, correctness of blocked scope and **total cost to accepted change**. A method that simply stops everything is not successful.

## Documentation / Документация

| Document | Purpose |
|---|---|
| [METHODOLOGY.md](METHODOLOGY.md) | Полная методология v0.5 и сквозной пример To-Do List |
| [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) | Гипотезы, исследовательские группы, метрики и защита от утечек |
| [REVIEW_GUIDE.md](REVIEW_GUIDE.md) | Правила научной и инженерной критики |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Как предложить исправление или воспроизводимый контрпример |
| [ANNOUNCEMENT_RU.md](ANNOUNCEMENT_RU.md) | Объявление для профессионального сообщества |
| [LICENSE.md](LICENSE.md) | Области действия двух лицензий и порядок атрибуции |

**Discuss / Обсудить:** [GitHub Issues](https://github.com/SoldatovAlexander/verilayer-method/issues) · [Open review #1](https://github.com/SoldatovAlexander/verilayer-method/issues/1).

## Relation to Existing Methods / Что не объявляется изобретением

NASA V&V and the V-model, GSN/assurance cases, risk-based verification, TDD/BDD/ATDD, GitHub Spec Kit/OpenSpec and Altshuller's TRIZ already establish important parts of this practice. The research question is whether their **specified combination and agent-action protocol** provides measurable improvement at acceptable cost. No global originality claim is made.

## License & Attribution / Лицензии

**Documentation, methodology and research:** [**Creative Commons Attribution 4.0 International — CC BY 4.0**](LICENSE). Redistribution, adaptation and commercial use are permitted with required attribution and notice of changes.

**Software code, future executable examples and automation:** [**Apache License 2.0**](LICENSE-CODE). Commercial use and modifications are permitted subject to its terms, notices and applicable patent provisions.

See [LICENSE.md](LICENSE.md) for the **exact scope by file type**, recommended attribution, mixed materials and third-party notices. © 2026 Alexander Soldatov and respective contributors.

**Trademark note:** VeriLayer is a *provisional working name*. Similar designations have been identified in trademark databases; no legal clearance or right to use a mark is represented here. Neither license grants trademark rights.

**Research note:** Open publication is an invitation to disprove the hypothesis, **not proof of effectiveness**.
