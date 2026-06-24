# delivery-design

## Execution Contract

### Purpose

Decide whether delivery decomposition is needed and produce a Delivery Plan roadmap/register and Delivery Scope when required.

### Produces

- `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- `_hirmos/session/SESSION_SCOPE.md delivery-route basis when available`
- `_hirmos/session/unresolved-items.md updates`
- `_hirmos/session/SESSION_EXECUTION.md delivery control updates`

### Terminal States

- COMPLETED — delivery plan is recorded or decomposition is explicitly not applicable.
- NEEDS_USER_DECISION — delivery target or staging decision requires user input.
- BLOCKED — Design or system-state inputs are missing.
- ROUTE_BACK_REQUIRED — delivery planning exposes missing system-state or requirements evidence.
- NOT_APPLICABLE — active request can be governed safely without delivery planning.

## Activation triggers

- greenfield project needs staged delivery
- large, multi-session, or prototype-to-product work cannot be safely governed as one session
- Design needs delivery decomposition before phase/session-scope work

## Required inputs

- `_hirmos/session/SESSION_EXECUTION.md`
- `_hirmos/session/SESSION_SCOPE.md when available`
- `_hirmos/session/unresolved-items.md`
- project-type and stack evidence

## Execution controls contributed

- Design control
- delivery-plan control
- unresolved-item control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/design-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.


## Capability-specific obligations

- Map delivery roadmap entries to one delivery scope and record delivery-route decisions.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in the focus-appropriate unresolved register selected by `SESSION_STATE.json.session_focus`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in the selected unresolved register, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## Project-type / stack requirements

Use the focus-appropriate `DESIGN.md`, `DELIVERY_SCOPE.md`, or `SESSION_SCOPE.md` for material project-type decisions and `stack-resolution.json` only when machine-readable stack routing is required by controls.

For any project type, require delivery-baseline governance when one bounded session cannot safely govern the change; do not equate delivery governance with a greenfield or brownfield label.

When stack contexts are active, carry in-scope/out-of-scope contexts into the active authority and Implementation Readiness decision when implementation is being authorized.


## durable delivery capability obligations

This capability must apply `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` before claiming completion.

Required behavior:

1. Read and record the Delivery Shape Decision from `SESSION_EXECUTION.md` and `SESSION_SCOPE.md` when those artifacts exist.
2. When the selected shape is `MULTI_SESSION_DELIVERY` or `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, use only durable delivery authority under `_hirmos/system/delivery/<delivery-id>/`.
3. When the selected shape is `MULTI_SESSION_DELIVERY`, require `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`; when the selected shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, require both the Delivery Plan and an adopted `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` before implementation readiness.
4. When the selected shape is a single-session shape, verify the active Session Scope contains affirmative bounded-scope safety evidence and implementation-unit coverage when required.
5. When the selected shape is `UNCERTAIN`, set this capability result to `BLOCKED` or `ROUTE_BACK_REQUIRED`; do not authorize Implementation.
6. Do not create or depend on session-local delivery authority artifacts.

Forbidden session-local delivery authorities:

```text
legacy session-local delivery plan, phase plan, delivery status, phase scope, or delivery-unit authority record files
```

## PROD-L8.9 focus-aware runtime route obligations

This capability participates in the command-selected focus route. Before claiming completion, it must ensure `SESSION_EXECUTION.md` records:

- selected Delivery Shape Decision;
- this capability decision and terminal state;
- required authority artifacts for the selected focus route;
- whether the focus route is satisfied, blocked, not applicable, or requires route-back;
- exactly one next governed command when the route cannot proceed.

The capability must not compensate for missing authority by creating legacy session-local delivery files or by duplicating full delivery authority inside `SESSION_SCOPE.md`.


Compatibility note: Map Delivery Plan items to governed requirements through the active `DELIVERY_SCOPE.md`; the Delivery Plan remains the roadmap/register.
