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

## Canonical interaction posture visibility

Use the canonical HIRMOS interaction posture from `_hirmos/core/authority/INTERACTION_POSTURE.md`: concise user-facing output, transparent artifact pointers for governed claims, and progressive disclosure when risk, validation failure, blocker state, route-back, or user request requires more detail.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in the focus-appropriate unresolved register, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.


## PROD-L8.13 Current-State-First Generated Artifact Cleanup

Generated artifacts and checkpoint text must explain routing from current system state, scope size, validation risk, continuity need, and artifact-authority requirements. Do not use greenfield/brownfield labels as the primary reason for delivery/session/phase selection. If a project-type label is useful, record it as supporting evidence metadata or phase-control routing metadata only.
