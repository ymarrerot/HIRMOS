# update-system-state

## Execution Contract

### Purpose

Synchronize reviewed accepted outcomes into durable system state, preserve session history, and prepare future sessions without performing Design or Implementation.

### Produces

- `_hirmos/session/SESSION_EXECUTION.md`
- `_hirmos/session/SESSION_EXECUTION.md`
- `_hirmos/system/accepted-state/*` updates when outcomes are accepted
- `_hirmos/system/history/sessions/<session-id>/` archive
- `_hirmos/session/SESSION_STATE.json` reset or updated terminal state
- `_hirmos/session/SESSION_EXECUTION.md` final state updates before archive

### Terminal States

- READY_TO_CLOSE — accepted outcomes, evidence, archive readiness, and carry-forward items are recorded.
- CLOSED — accepted state was updated or explicitly not updated, session archived, and active session reset.
- BLOCKED — required reviews, evidence, unresolved dispositions, or artifacts are missing.
- ABORT_CLOSE — user intentionally aborts or closes without accepting outcomes.
- NOT_APPLICABLE — command does not request update/close and no outcomes require durable state sync.

## Activation triggers

- `hirmos close` is invoked.
- Completed outcomes must become durable accepted state.
- Session history must be archived.
- A terminal abort or non-application decision must be recorded.

## Required inputs

- `_hirmos/session/SESSION_EXECUTION.md`
- `_hirmos/session/SESSION_EXECUTION.md` when close is requested
- `_hirmos/session/SESSION_EXECUTION.md` when accepted-state changes are proposed
- applicable Design/Implementation/review/evidence artifacts for the completed session
- `_hirmos/session/unresolved-items.md` when unresolved items exist

## Execution controls contributed

- update-system-state control
- close/archive control
- accepted-state mutation control
- unresolved-item carry-forward control
- evidence preservation control

## Method

1. Read `SESSION_EXECUTION.md` and confirm the session has a valid current state and no required controls in `PENDING` or `BLOCKED` unless the close is an abort close.
2. Confirm whether the session has reviewed outcomes eligible for accepted-state update.
3. Confirm applicable evidence: Design readiness, implementation-unit reviews, `EVIDENCE.md` when present, unresolved-item dispositions, `SESSION_SCOPE.md` close verification, and `SESSION_EXECUTION.md` close/update control pointers.
4. Separate outcomes into accepted outcomes, rejected/not-applied outcomes, evidence-only artifacts, and carry-forward items.
5. Create or update `_hirmos/session/SESSION_EXECUTION.md` with the update decision and evidence basis.
6. Create or update `_hirmos/session/SESSION_EXECUTION.md` with archive readiness and active-session reset requirements.
7. Apply accepted-state changes only when controls and evidence allow it.
8. Archive the full active session under `_hirmos/system/history/sessions/<session-id>/`.
9. Reset `_hirmos/session/` to clean session state after normal close, preserving only required scaffolding.
10. Record abort close separately without pretending outcomes were accepted.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.

## Canonical interaction posture visibility

Use the canonical HIRMOS interaction posture from `_hirmos/core/authority/INTERACTION_POSTURE.md`: concise user-facing output, transparent artifact pointers for governed claims, and progressive disclosure when risk, validation failure, blocker state, route-back, or user request requires more detail.

- By default, surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- Surface capability result, assumptions, artifacts/evidence, and review implications when requested or needed for responsible review.
- Surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis when validation failure, blocker state, route-back, or inspection need requires it.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## Runtime integration responsibilities

When material runtime services are involved, follow `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

Record or consume `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` as required by execution controls.

Do not claim fixture/mock/boundary/local/production integration levels beyond what the active artifacts and evidence support.

## Close integrity requirements

When this capability performs Update System State or close work, it must read `_hirmos/core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md` and satisfy the close integrity controls before surfacing close success.

Terminal state is `BLOCKED` when accepted-state records, archive records, active-session reset, and close output cannot be reconciled.
