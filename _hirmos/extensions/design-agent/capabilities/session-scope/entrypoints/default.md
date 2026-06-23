# session-scope

## Execution Contract

### Purpose

Create the Session Scope that authorizes exactly what the active session may do.

### Produces

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/unresolved-items.md updates`
- `_hirmos/session/SESSION_EXECUTION.md session-scope control updates`

### Terminal States

- COMPLETED — ready Session Scope exists and can authorize downstream work if readiness passes.
- NEEDS_USER_DECISION — scope boundary needs user decision.
- BLOCKED — required source contracts or unresolved dispositions are missing.
- ROUTE_BACK_REQUIRED — scope creation exposes missing Design or system-state evidence.
- NOT_APPLICABLE — active request does not require session scope authority.

## Activation triggers

- Implementation may be needed
- active request needs bounded work authority
- phase or delivery-unit contract must be adopted for current session
- validation/review-only work needs explicit scope

## Required inputs

- `_hirmos/session/DESIGN.md`
- `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md when applicable`
- `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md when applicable`
- `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md when applicable`
- `_hirmos/session/unresolved-items.md`
- `_hirmos/session/DESIGN.md technical review when applicable`

## Execution controls contributed

- session-scope control
- implementation-authorization control
- unresolved-item control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/design-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific contract; do not execute from chat summaries or raw inputs alone.


## Capability-specific obligations

- implementation unit planning, implementation unit review, session implementation review, and Update System State.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## Project-type / stack requirements

Use `DESIGN.md` / `SESSION_SCOPE.md` for material project-type decisions and `stack-resolution.json` only when machine-readable stack routing is required by controls.

For large or multi-session work in any project type, require governed Delivery Units or Phases when one bounded session cannot safely govern the change.

When stack contexts are active, carry in-scope/out-of-scope contexts into the Session Scope and Implementation Readiness decision.


## Runtime integration responsibilities

When material runtime services are involved, follow `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

Record or consume `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` as required by execution controls.

Do not claim fixture/mock/boundary/local/production integration levels beyond what the active artifacts and evidence support.


## durable delivery capability obligations

This capability must apply `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` before claiming completion.

Required behavior:

1. Read and record the Delivery Shape Decision from `SESSION_EXECUTION.md` and `SESSION_SCOPE.md` when those artifacts exist.
2. When the selected shape is `MULTI_SESSION_DELIVERY` or `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, use only durable delivery authority under `_hirmos/system/delivery/<delivery-id>/`.
3. When the selected shape is `MULTI_SESSION_DELIVERY`, require `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`; when the selected shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, require both the Delivery Plan and an adopted `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` before implementation readiness.
4. When the selected shape is a single-session shape, verify the active Session Scope contains affirmative bounded-scope safety evidence and implementation-unit coverage when required.
5. When the selected shape is `UNCERTAIN`, set this capability result to `BLOCKED` or `ROUTE_BACK_REQUIRED`; do not authorize Implementation.
6. Do not create or depend on session-local delivery authority artifacts.

Forbidden session-local delivery authorities:

```text
legacy session-local delivery plan, phase plan, delivery status, phase contract, or delivery-unit contract files
```
