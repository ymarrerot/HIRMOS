# delivery-baseline

## Execution Contract

### Purpose

Prepare the Delivery Baseline — Review or Change checkpoint without instantiating session scope, phase files, or implementation units by default.

### Produces

- focus-specific authority artifacts defined by `_hirmos/core/protocol/CAPABILITY_ROUTING.md`
- `_hirmos/session/SESSION_EXECUTION.md` control updates

### Terminal States

- COMPLETED — required focus-specific authority is ready for the next checkpoint.
- NEEDS_USER_DECISION — the checkpoint has gated user-owned decisions.
- BLOCKED — required evidence or authority is missing.
- ROUTE_BACK_REQUIRED — current-state or delivery evidence invalidates the selected route.
- NOT_APPLICABLE — this focus is not active.

## Required behavior

1. Confirm `SESSION_STATE.json.session_focus` before producing artifacts.
2. Use the active authority and unresolved-item target required by `_hirmos/core/protocol/CAPABILITY_ROUTING.md`.
3. Do not create artifacts outside the selected focus.
4. Record capability status in `_hirmos/session/SESSION_EXECUTION.md`.

## Activation triggers

- Active `SESSION_STATE.json.session_focus` matches this capability focus.
- Command routing requires this focus before the next governed checkpoint.

## Required inputs

- `_hirmos/session/SESSION_STATE.json`
- `_hirmos/session/SESSION_EXECUTION.md`
- Current System State when available

## Execution controls contributed

- active-authority control
- focus-specific checkpoint control
- unresolved-item target control

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md`.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in the focus-appropriate unresolved register, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.
