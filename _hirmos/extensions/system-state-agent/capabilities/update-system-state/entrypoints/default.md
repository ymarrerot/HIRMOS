# update-system-state

## Execution Contract

### Purpose

Synchronize reviewed accepted outcomes into durable system state, preserve session history, and prepare future sessions without performing Design or Implementation.

### Produces

- `_hirmos/session/SESSION_LEDGER.md`
- `_hirmos/session/SESSION_LEDGER.md`
- `_hirmos/system/accepted-state/*` updates when outcomes are accepted
- `_hirmos/system/history/sessions/<session-id>/` archive
- `_hirmos/session/SESSION_STATE.json` reset or updated terminal state
- `_hirmos/session/SESSION_LEDGER.md` final state updates before archive

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

- `_hirmos/session/SESSION_LEDGER.md`
- `_hirmos/session/SESSION_LEDGER.md` when close is requested
- `_hirmos/session/SESSION_LEDGER.md` when accepted-state changes are proposed
- applicable Design/Implementation/review/evidence artifacts for the completed session
- `_hirmos/session/unresolved-items.md` when unresolved items exist

## Execution controls contributed

- update-system-state control
- close/archive control
- accepted-state mutation control
- unresolved-item carry-forward control
- evidence preservation control

## Method

1. Read `SESSION_LEDGER.md` and confirm the session has a valid current state and no required controls in `PENDING` or `BLOCKED` unless the close is an abort close.
2. Confirm whether the session has reviewed outcomes eligible for accepted-state update.
3. Confirm applicable evidence: Design readiness, implementation-unit reviews, `EVIDENCE.md` when present, unresolved-item dispositions, `SESSION_SCOPE.md` close verification, and `SESSION_LEDGER.md` close/update control pointers.
4. Separate outcomes into accepted outcomes, rejected/not-applied outcomes, evidence-only artifacts, and carry-forward items.
5. Create or update `_hirmos/session/SESSION_LEDGER.md` with the update decision and evidence basis.
6. Create or update `_hirmos/session/SESSION_LEDGER.md` with archive readiness and active-session reset requirements.
7. Apply accepted-state changes only when controls and evidence allow it.
8. Archive the full active session under `_hirmos/system/history/sessions/<session-id>/`.
9. Reset `_hirmos/session/` to clean session state after normal close, preserving only required scaffolding.
10. Record abort close separately without pretending outcomes were accepted.

## Required behavior

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## Runtime integration responsibilities

Apply the shared runtime-integration responsibilities in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Keep detailed evidence in the owning IU, `EVIDENCE.md`, or accepted-state/archive source; this entrypoint should point rather than duplicate.

## Close integrity requirements

When this capability performs Update System State or close work, it must read `_hirmos/core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md` and satisfy the close integrity controls before surfacing close success.

Terminal state is `BLOCKED` when accepted-state records, archive records, active-session reset, and close output cannot be reconciled.
