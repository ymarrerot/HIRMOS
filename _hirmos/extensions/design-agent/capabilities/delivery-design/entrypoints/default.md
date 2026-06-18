# delivery-design

## Execution Contract

### Purpose

Decide whether delivery decomposition is needed and produce a Delivery Plan when required.

### Produces

- `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`
- `_hirmos/session/DESIGN.md delivery design section`
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
- Design needs delivery decomposition before phase/session-contract work

## Required inputs

- `_hirmos/session/DESIGN.md`
- `_hirmos/session/support/system-state.md`
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
5. Apply the extension method and this capability-specific contract; do not execute from chat summaries or raw inputs alone.


## Capability-specific obligations

- Map Delivery Plan items to governed requirements.

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

Use `support/project-context.md` and `support/stack-resolution.json` when present or required by controls.

For large or multi-session work in any project type, require governed Delivery Units or Phases when one bounded session cannot safely govern the change.

When stack contexts are active, carry in-scope/out-of-scope contexts into the Session Contract and Implementation Readiness decision.


## durable delivery capability obligations

This capability must apply `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` before claiming completion.

Required behavior:

1. Read and record the Delivery-Need Classification answer from `SESSION_EXECUTION.md` and `SESSION_CONTRACT.md` when those artifacts exist.
2. When classification is `YES`, use only durable delivery authority under `_hirmos/system/delivery/<delivery-id>/`.
3. When classification is `YES`, require `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` and at least one `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` before implementation readiness.
4. When classification is `NO`, verify the active Session Contract contains affirmative single-session safety evidence.
5. When classification is `UNCERTAIN`, set this capability result to `BLOCKED` or `ROUTE_BACK_REQUIRED`; do not authorize Implementation.
6. Do not create or depend on session-local delivery authority artifacts.

Forbidden session-local delivery authorities:

```text
legacy session-local delivery plan, phase plan, delivery status, phase contract, or delivery-unit contract files
```
