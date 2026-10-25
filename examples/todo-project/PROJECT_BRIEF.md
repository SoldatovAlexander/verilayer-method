# To-Do List — test project brief (fictional exercise)

**Scope:** one user, local-only state, task creation/editing/completion/deletion; no external accounts, payments, personal identifiers or production access.

## L0 goals
- A user can add, edit, mark complete and delete a task.
- Previously saved tasks survive application restart under the defined storage-failure assumptions.
- Accidental delete must have a documented, testable mitigation; **exact undo window remains a product-owner decision**, not an agent assumption.

## L1–L3 candidate decisions (NOT accepted automatically)
- L1: local storage, atomic persistence or append-only journal.
- L2: separate task model, persistence service and UI.
- L3: explicit task IDs, edge cases and error states, recoverability contract.
- L4: implement and execute unit/component tests as code appears.
- L5: execute acceptance flows in the integrated application and record scope/version.

## Material TRIZ contradiction (CAR-DELETE-01)
**Improve:** deletion feels immediate. **Worsens:** protection against accidental irreversible loss. Desired ideal: removed instantly from active view, but reversible for an agreed interval. Compare at least (A) soft delete + Undo and (B) confirmation dialogue, and consider (C) append-only event log if risk warrants. Do not accept a solution until success criteria, residual risks and VO are documented.

## Example gate exercise
Before proposing a release of delete behavior, inspect \`.verilayer/fixtures/\` and run the demo checker. These fixtures contain **illustrative**, not real CI, evidence. In a real codebase, collect actual reproducible results and have external policy enforce forbidden actions.

## Exercise acceptance
Write down the exact agreed undo time window (or explicitly mark unresolved); implement it with boundary cases, persistence/restart behavior and recovery tests; verify only the claims that the executed tests actually cover. If no agreement on a blocking requirement exists, report S01/S02 and recommend INVESTIGATE or ESCALATE.
