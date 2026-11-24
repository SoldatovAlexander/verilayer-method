# Superpowers: проверяемость агентного процесса — исследовательская гипотеза VeriLayer

**Статус:** DRAFT · RESEARCH ONLY · NOT IMPLEMENTED · NOT TESTED  
**Дата:** 2026-11-24  
**База сравнения:** VeriLayer Method v0.5, L0–L5, VO, Evidence, S01–S12 и ТРИЗ.  
**Решение:** ненормативное предложение. Основной текст METHODOLOGY.md и состав Stop Gates не меняются.

## Источник, благодарность и границы авторства

Выражаем благодарность **Jesse Vincent (GitHub: obra)** и участникам проекта [Superpowers](https://github.com/obra/superpowers), распространяемого под **MIT License**. Изучена ветка `main` на [коммите `22f0b463e7a5`](https://github.com/obra/superpowers/commit/22f0b463e7a5e579904dd6211a520321035526f7), 2026-11-03 (релиз v7.0.2).

Источники:
- [README / базовый workflow](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/README.md).
- [brainstorming](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md), [writing-plans](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md).
- [subagent-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) и [executing-plans](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md).
- [test-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/test-driven-development/SKILL.md), [verification-before-completion](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md).
- [writing-skills](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md), [diagnosing-superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md), [testing](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/docs/testing.md).

Superpowers — самостоятельная существующая методология агентного coding workflow, а не подтверждение оригинальности VeriLayer. TDD, независимое ревью, декомпозиция, worktrees, проверка перед завершением и skill testing известны независимо от обоих проектов. Ни копирование исходных skills, ни включение автора в состав участников VeriLayer, ни его одобрение не подразумеваются. Здесь изложены собственные гипотезы интеграции; при последующем копировании MIT-материалов отдельно выполнять условия уведомления об авторстве и лицензии.

## 1. Суть сопоставления

| Измерение | Superpowers: наблюдаемая практика | VeriLayer v0.5: уже существующий механизм | Что исследовать |
|---|---|---|---|
| Намерение | Диалог до разработки, playback и design approval | L0 и верификация пользовательской цели; S01 | Intent Confirmation Record / критерий достаточности L0 |
| Проектирование | Письменный дизайн, builder check | L1–L3, VO, ADR/CAR, S03/S04 | Не теряются ли предпосылки дизайна при передаче |
| Планирование | Конкретные задачи и review focus на неочевидных failure modes | VO с зависимостями и gate scope | Traceability задач ↔ claims ↔ tests ↔ decisions |
| Реализация | Red–green–refactor; отдельные task loop и ledger | L4 tests, run-status и Evidence | Точная запись факта RED и GREEN, oracle validity |
| Делегирование | Новый subagent на задачу, отдельное task review; или более дешёвый inline-режим | Agent protocol, независимая проверка Critical | Контроль передачи контекста, scope и стоимости |
| Завершение | Fresh verification перед claim, whole-branch review | S05–S08, S12, Evidence provenance | «Claim-to-command» сопоставление с результатом |
| Поведение agent rules | Skills проверяются на pressure-сценариях с baseline | Правила для разных harness, независимая критика | Behavioural VO для agent skills |
| Диагностика | Анализ transcript, отклонений, токенов и стоимости | False Proceed, False Stop, метрики cost | Процессная observability / lifecycle skills |

**Главное различие.** Superpowers описывает *как организовать цикл работы*, VeriLayer — *какое инженерное утверждение проверено на каком уровне и достаточно ли этого для конкретного действия*. Они пересекаются; Superpowers — сильный comparator, а не «библиотека дополнений, которой нет аналогов».

## 2. H-SP1 — подтверждение замысла как L0-obligation

Гипотеза: подтверждённый пользователем intent playback вместе с перечислением скрытых предпосылок снижает «дрейф замысла» по сравнению с обычным процессом, когда требования быстро превращаются в код.

Предложение: **Intent Confirmation Record (ICR)** — лаконичная запись, содержащая `intent_id`, `source`, `user_value`, `in_scope`, `out_of_scope`, `critical_assumptions`, `acceptance_examples`, `approved_version`, `unresolved_questions` и ссылку на L0-VO. ICR — **не новое обязательное требование для всех задач**. Для Lite-поправок с ясным ожидаемым результатом записи может быть достаточно в одном абзаце. Для Standard/Critical — ревью существенных предпосылок.

Не считать согласование дизайн-документа доказательством реализации. Если согласован только устный подход, нельзя выдавать ещё не показанный письменный документ за одобренный.

Связь с действующим S01/S02/S09: дополнять артефакты уточнения цели и изменениями критериев, но не создавать 13-й Stop Gate.

## 3. H-SP2 — handoff с фиксированным контекстом и независимым reviewer

Superpowers использует два исполнения: **subagent-driven** (новый implementer и review после каждой задачи) и **executing-plans** (inline-исполнение, один независимый общий review в конце). Разная стоимость и степень раннего контроля — не «хороший и плохой» сценарии.

Предложение: **Task Verification Handoff (TVH)** как потенциальное дополнение шаблонов:
- `task_id`, задача/потребитель, требуемый `scope`, ограничения, версии spec/plan/artifact;
- унаследованные L0–L3 claims и блокирующие VO;
- переданный контекст и **исключённые допущения**, которые нельзя молча домыслить;
- test oracle и запланированные `run_status`/evidence;
- независимые критерии ревью: соответствие спецификации, реальное поведение, нарушение инвариантов, неожиданные пути;
- решение reviewer с исходными ссылками, открытыми вопросами и допустимым следующим шагом.

Не считать отчёт implementer о собственном тесте независимым ревью; при отсутствии второго агента — честно фиксировать режим и его ограничения. Critical-задачи требуют сравнения экономического эффекта и качества двух стратегий.

## 4. H-SP3 — Behavioural Verification Obligations для agent skills

Наиболее перспективная идея: применять **TDD к самим правилам агентного поведения**. В Superpowers это baseline (без skill), pressure-сценарий, минимальная правка skill, повторная оценка и поиск новых обходов.

В VeriLayer предлагается использовать существующую категорию VO, но с `target=agent_rule` и отличным oracle:
- `BVO` — условное обозначение **внутри исследовательского набора**, не новый нормативный тип VO;
- `rule_id`, `skill_version`, `harness/model_version`, `trigger_context`, `expected_behavior`, `forbidden_behavior`, `baseline_trace`, `candidate_trace`, `independent_oracle`, `scope`, `run_status`, `evidence_refs`;
- строго отделять «skill загрузился», «агент выбрал правильный workflow» и «полученный продукт лучше»;
- оценивать устойчивость к переформулировке и конфликтующим указаниям, а не только совпадение ключевых слов;
- регистрировать **отрицательные случаи**: skill не активировался, активировался лишний раз, заставил неоправданно остановить работу, повысил стоимость без выгоды.

**Ограничение:** текстовые skills не являются security boundary. Отсылки агента к «обязательному workflow» не могут заменять реально исполняемый запрет. См. отдельную [гипотезу Runtime Enforcement](RUNTIME-ENFORCEMENT-HYPOTHESIS.md).

## 5. H-SP4 — evidence на каждый claim о завершении

Сопоставить `claim -> command -> actual fresh output -> artifact version -> scope`; несоответствие вызывает пересмотр исходного VO/Decision. В Superpowers правило «не утверждать, что тесты прошли, без свежего запуска» практически совпадает с текущими VeriLayer Evidence provenance и S06/S08.

Поэтому **не нужно дублировать правило** в METHODOLOGY.md. Предложение касается операционного чек-листа и автоматизируемого тестового oracle в пилоте. Различать:
1. RED: тест упал **по ожидаемой причине**, не из-за ошибки среды;
2. GREEN: соответствующий тест выполнен и прошёл;
3. regression: полный набор тестов не скрывает иных падений;
4. review: соответствие требованиям не сводится к зелёному CI;
5. claim: формулировка ограничена реально проверенным окружением.

## 6. H-SP5 — lifecycle и observability библиотеки skills

Skills приобретают **process debt**: дублирование правил разных harness, конфликт приоритетов, устаревшие примеры, безосновательные блокировки и дорогой контекст. Исследовать `Skill Lifecycle Record` (`owner`, `version`, `trigger`, `dependencies`, `supported_harnesses`, `behavioral_VO`, `baseline`, `last_eval`, `regressions`, `deprecation`, `cost`). Это предложенная модель управления, **не** подтверждение, что Superpowers использует именно такую схему.

Session diagnostics от Superpowers показывает полезный класс данных: следы фактической активации skills, повторной работы, конфликтов инструкций, стоимости и отклонений. Нельзя считать скопированные transcript надёжными без контроля полноты, конфиденциальности и независимости оценки.

## 7. Что НЕ переносить в VeriLayer как обязательное

- Жёсткий универсальный порядок и запрет начинать любое действие без длительного brainstorming: для Lite может повысить False Stop и стоимость.
- Обязательное создание subagent на каждую задачу: вариант inline с итоговым review должен оставаться честным экономическим конкурентом.
- Утверждение, что TDD или prompt-инструкции достаточны для безопасности и доказательства качества продукта.
- Прямое копирование skills в корневые AGENTS.md/CLAUDE.md: возможно противоречие между проектными правилами и исходным method protocol.
- Утверждение, что tests/ и описанные behaviour evals из другого проекта доказывают эффективность VeriLayer.

## 8. Проверка на однопользовательском To-Do List

Публичный [план эксперимента](../examples/todo-project/.verilayer/AGENT-PROCESS-CONFORMANCE-PLAN.md) содержит сценарии на intent, качество handoff, подмену evidence, ненужные остановки и TDD для agent skill.

Сопоставить сильные варианты:
- **SP-A:** обычный инженерно добросовестный агент с тестами и review;
- **SP-B:** Superpowers с корректно установленными skills, доступными инструментами и заявленными режимами работы;
- **SP-C:** VeriLayer v0.5 без новых гипотез;
- **SP-D:** VeriLayer v0.5 + ICR/TVH/BVO и диагностика, в допустимом для задачи risk profile.

Критерии: critical False Proceed, False Stop, traceability и correctness scope, воспроизводимость обоснования, качество принятого To-Do изменения, влияние intent drift, стоимость в токенах/времени/ревью и доля неверных утверждений о выполненных тестах. **Отдельно** оценивать rule-compliance и качество результата. Пререгистрация и независимые holdout обязательны до общих заявлений об улучшении.

Фальсификация: расширение не улучшает outcome относительно сильных SP-B/SP-C, создаёт необоснованные согласования, излишнюю стоимость, завышенные claims или не воспроизводится на независимо придуманных задачах.

## 9. Backlog

- [x] Указать первичный источник и автора, статус лицензии.
- [x] Зафиксировать сопоставление с VeriLayer v0.5 без изменения нормативных положений.
- [x] Описать гипотезы ICR, TVH, BVO, lifecycle и границы применимости.
- [x] Подготовить публичные exploratory-сценарии To-Do.
- [ ] Независимое экспертное ревью proposed oracles и форматов.
- [ ] Отдельный blind holdout и preregistration; заморозить бюджеты, модель и версии.
- [ ] Прототип optional-профиля инструкций/тестов, без вмешательства в основной starter kit.
- [ ] Прогоны SP-A–SP-D; отчёт о ложных остановках, rework и стоимости.
- [ ] Только после evidence принять/отклонить изменения нормативной редакции.

**Вывод:** полезнее всего не «встроить Superpowers в VeriLayer», а исследовать **проверяемость самого процесса работы агента**. Права и техническая возможность действий составляют отдельную гипотезу Runtime Enforcement.
