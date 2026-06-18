# Artifact Model Reference

HIRMOS uses a contract-centered artifact model.

## Active session artifacts

Active session artifacts use the active session spine below.

## Active session spine

```text
_hirmos/session/
  SESSION_STATE.json
  SESSION_CONTRACT.md
  SESSION_EXECUTION.md
  unresolved-items.md
  session-contract-review.md
  implementation-units/
  checkpoints/
  support/
```

- `SESSION_STATE.json`: machine-readable command/lifecycle state.
- `SESSION_CONTRACT.md`: active session scope, acceptance, coverage, and close verification authority.
- `SESSION_EXECUTION.md`: linear execution-control spine and evidence ledger.
- `unresolved-items.md`: governed register for gated items, non-gating assumptions, technical-review items, dispositions, and revalidation.
- `session-contract-review.md`: governed fast-access promised-vs-verified review and fail-closed verdict for implementation completion and close.
- `implementation-units/IU-xx.md`: self-contained unit contract, evidence, review, and retries.
- `checkpoints/`: user-facing lifecycle boundary receipts.
- `support/`: evidence appendices only; not a source of session scope or final contract review authority.

## Source inputs

Source inputs live under:

```text
_hirmos/inputs/
  uploads/
  prototypes/
  references/
```

Source inputs are evidence and focus signals. They are not requirements authority, design authority, implementation authorization, or accepted current state. HIRMOS may read files from `_hirmos/inputs/uploads/`, `_hirmos/inputs/prototypes/`, and `_hirmos/inputs/references/`, but Design must reconcile material source signals into governed artifacts before they become authorized work.

## Accepted system state

Durable current truth lives in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`.

## Delivery plans

Multi-session delivery plans live under:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

## Archive history

Closed sessions are archived under `_hirmos/system/history/sessions/<session-id>/`. Archive history is evidence, not current accepted state by itself.

## Archive history vs accepted state

Archive history preserves evidence. Accepted current system state must be merged into `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` through governed close/update-state controls.

## Durable delivery authority

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

For multi-session work in any project type, these durable artifacts are required. Session-local delivery files are not canonical delivery authority.
