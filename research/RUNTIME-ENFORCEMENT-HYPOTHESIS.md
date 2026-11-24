# Runtime Enforcement: проверяемый контроль исполнения действий AI-агентов

**Статус:** DRAFT · RESEARCH ONLY · NOT IMPLEMENTED · NOT TESTED  
**Дата:** 2026-11-24  
**Применимость:** VeriLayer v0.5, L0–L5, VO, Evidence, Stop Gates S01–S12.  
**Решение:** ненормативное предложение. **Не** изменяет METHODOLOGY.md v0.5 и **не** вводит новый Stop Gate.

## Источник, благодарность, границы прав

Выражаем благодарность команде **SpaceAI-UAG** за опубликованный прототип [SpaceAI Guard](https://github.com/SpaceAI-UAG/LLM-agent-security). Он демонстрирует OS sandbox, egress proxy, декларативные ограничения, контроль MCP-инструментов, привязанные к вызовам approvals, лимиты и журналы решений. Изученная версия: [`c2a06d57ee32`](https://github.com/SpaceAI-UAG/LLM-agent-security/commit/c2a06d57ee32f8445b74a4a90067a2465627e981) (30 октября 2026 года).

Первоисточники: [README.ru.md](https://github.com/SpaceAI-UAG/LLM-agent-security/blob/c2a06d57ee32f8445b74a4a90067a2465627e981/README.ru.md), [docs/runtime.ru.md](https://github.com/SpaceAI-UAG/LLM-agent-security/blob/c2a06d57ee32f8445b74a4a90067a2465627e981/docs/runtime.ru.md), [policy/validate.go](https://github.com/SpaceAI-UAG/LLM-agent-security/blob/c2a06d57ee32f8445b74a4a90067a2465627e981/internal/policy/validate.go), [approval.go](https://github.com/SpaceAI-UAG/LLM-agent-security/blob/c2a06d57ee32f8445b74a4a90067a2465627e981/internal/mcpguard/approval.go), [gateway_test.go](https://github.com/SpaceAI-UAG/LLM-agent-security/blob/c2a06d57ee32f8445b74a4a90067a2465627e981/internal/mcpguard/gateway_test.go), [attack/attack.sh](https://github.com/SpaceAI-UAG/LLM-agent-security/blob/c2a06d57ee32f8445b74a4a90067a2465627e981/attack/attack.sh).

Открытость репозитория не означает право повторного использования кода: на момент исследования файл LICENSE не опубликован. Поэтому никакой чужой код/конфигурация/диаграмма сюда **не копируется**. Принципы least privilege, external authorization, sandbox и fail-closed известны до SpaceAI Guard; источник является инженерной иллюстрацией, не заявкой на первенство. Публикация этой гипотезы не означает сотрудничества или одобрения SpaceAI.

## 1. Исследовательская проблема

VeriLayer уже требует **независимого от LLM enforcement** для опасных действий (раздел 15 METHODOLOGY.md). Но `Gate=PASS` означает обоснованность перехода по имеющимся VO и Evidence, а не предоставление агенту безусловных прав на инфраструктуру.

**H-RE:** связь локального Gate Decision с независимо действующей границей исполнения снижает фактические несанкционированные операции без чрезмерного роста False Stop, задержек и стоимости. Рассматривать как отдельное проверяемое дополнение, а не доказанный эффект или замену архитектуры безопасности.

## 2. Предложение: Execution Enforcement Contract (EEC)

EEC — исследовательская запись, связывающая определённое действие с версией policy, полномочиями и доказательствами исполнения. Для Lite-обратимых локальных действий может быть избыточной.

Предлагаемые поля:
- идентичность: `contract_id`, `schema_version`, `action_id`, `subject`, `requested_operation`, `tool_id`, `resource`, `scope`;
- привязка: `artifact_version`, `policy_version`, `arguments_digest`, `expires_at`, `max_uses`, `approval_ref`, `approver_role`;
- основания: `gate_id`, `gate_status`, `vo_refs`, `evidence_refs`;
- исполнение: `enforcer_id`, `enforcement_point`, `enforcer_ready_evidence`, `execution_outcome`, `audit_ref`, `residual_risk`.

Инварианты для проверки:
1. `BLOCKED`/`ESCALATED` **запрещает только зависимое действие**, безопасные независимые задачи продолжаются.
2. `PASS` передаёт запрос на независимую проверку действующих полномочий, а не отменяет ограничения сервисной/OS policy.
3. Approval, если требуется, привязано к субъекту, инструменту, ресурсу, точным аргументам, сроку и числу допустимых использований. Повтор/подмена должны отклоняться на границе.
4. Policy, approvals и обязательный audit недоступны для записи агенту. Неисправный контроль для Critical-операции блокирует **эту операцию**.
5. Изменение policy, artifact, разрешений, параметров или endpoint может инвалидировать EEC и требует переоценки затронутых VO/S11.
6. Точка проверки должна видеть фактический вызов. Самоотчёт агента не заменяет доказательство блокировки.
7. Проверить альтернативные пути (shell/API/иной MCP), TOCTOU и отсутствие гарантий отката удалённых операций. Digest без доверенной идентичности и устойчивого anti-replay механизма не достаточен.

### Синтетический пример (не действующая авторизация)

```json
{
  "schema_version": "research-0.1",
  "contract_id": "EEC-TODO-001",
  "action_id": "todo.delete",
  "subject": "agent-fixture",
  "tool_id": "todo.delete",
  "resource": "task-42",
  "scope": "single-user-todo-fixture",
  "arguments_digest": "sha256:DEMO_ONLY",
  "artifact_version": "fixture-v1",
  "policy_version": "policy-fixture-v1",
  "gate_id": "S10",
  "gate_status": "BLOCKED",
  "vo_refs": ["VO-TODO-DELETE-AUTH"],
  "evidence_refs": [],
  "approval_ref": null,
  "max_uses": 1,
  "enforcer_id": "NOT_IMPLEMENTED",
  "enforcement_point": "todo-service",
  "execution_outcome": "NOT_RUN",
  "audit_ref": null,
  "residual_risk": "Enforcement not implemented or evaluated"
}
```

## 3. Предложение: Enforcement Evidence

Отделить свидетельство **решения о полномочиях** от свидетельства **фактического исполнения**:
- `policy_validation_evidence`: policy корректна по ограниченному валидатору — **не** полная гарантия sandbox;
- `authorization_evidence`: approval получено и связано с текущими параметрами;
- `boundary_test_evidence`: запрещённая операция не достигла ресурса по доверенному oracle;
- `execution_audit_evidence`: независимый журнал вызова/решения/фактического результата;
- `environment_evidence`: применённая версия ОС/контроля и ограничения платформы.

Зелёный security-test доказывает только свой проверенный сценарий. Журнал `DENY` не доказывает невозможность альтернативного пути. Классификатор prompt-injection/regex не обеспечивает семантический DLP. Некоторые TLS-туннели не инспектируются. Истёкший timeout не означает откат ранее совершённой удалённой операции. Документировано авторами SpaceAI Guard; верификация независимым аудитом не проведена.

## 4. Применение к текущим S01–S12 (ещё не принято)

- S05/S06: где риск требует, VO подтверждается фактом boundary enforcement, со scope/version/provenance.
- S09/S11: изменение политики, прав и версии endpoint считается значимым изменением зависимостей.
- S10: явное технически ограниченное approval для опасного действия вместо естественно-языковой фразы «одобрено».
- S07/S08/S12: реальный negative-test run, а не самодекларация агента. `NOT_RUN`/`INFRA_BLOCKED` никогда не `PASS`.

Нет оснований считать этот список новой редакцией текущего реестра: это только точки возможного усиления и проверяемые предложения.

## 5. План пилота и фальсификация

Публичный [план шести To-Do сценариев](../examples/todo-project/.verilayer/RUNTIME-ENFORCEMENT-TEST-PLAN.md) проверяет запрещённое удаление, отсутствие/повтор approvals, защиту policy, отказ аудита и разрешение независимого чтения.

Предложены три группы: **RE-A** обычный агент с добросовестными минимальными защитами, **RE-B** VeriLayer v0.5 без EEC, **RE-C** VeriLayer с EEC и техническим enforcer. Условия исходного доступа и базовые safety controls должны быть сопоставимыми; отдельно измерить **эффект добавления enforcer** и его стоимость.

Метрики: `Executed Unauthorized Action Rate`, `False Stop Rate`, корректность scope, попытки обхода, неверное повторное использование approval, total cost to accepted change. Blind holdout, предварительная спецификация oracle, повторы и независимое ревью обязательны до выводов.

Отрицательный результат: EEC не снижает реальные неправомерные действия против сильного контроля либо повышает цену/ложные блокировки непропорционально эффекту. Не делать заявлений об улучшении до фактического эксперимента.

## 6. Backlog

- [x] Источник и ограничения лицензии зафиксированы.
- [x] Гипотеза EEC и Enforcement Evidence описаны независимо от продукта.
- [x] Публичные To-Do cases сформулированы.
- [ ] Review модели угроз, alternative paths и доверенных oracle.
- [ ] Независимый минимальный fake service + trust boundary в disposable environment.
- [ ] Создать скрытые holdout и зарегистрировать сравнительный протокол.
- [ ] Провести прогоны, включая Negative Evidence, False Stop и затраты.
- [ ] Решить после результатов, нужны ли изменения в нормативной VeriLayer v0.5.

**Итог:** не переносить архитектуру Go/Seatbelt/bubblewrap как требование VeriLayer. Исследовать проверяемую связь *method decision -> runtime authority -> observed execution*, дополняющую [исследование agent process](SUPERPOWERS-PROCESS-HYPOTHESIS.md).
