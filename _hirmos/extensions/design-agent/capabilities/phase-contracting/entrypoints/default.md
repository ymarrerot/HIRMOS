# phase-contracting

## Execution Contract

### Purpose

Produce phase plans, phase contracts, or delivery-unit contracts when delivery decomposition must govern future implementation sessions.

### Produces

- `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md phase decomposition when ordered phases are used`
- `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md for phase-sourced implementation`
- `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md when non-phase delivery units are used`
- `_hirmos/session/SESSION_EXECUTION.md delivery-unit/phase control updates`

### Terminal States

- COMPLETED — required phase or delivery-unit contracts are ready.
- NEEDS_USER_DECISION — phase/delivery boundary needs user input.
- BLOCKED — Delivery Plan or Design authority is missing.
- ROUTE_BACK_REQUIRED — phase planning exposes weak requirements/design/system-state evidence.
- NOT_APPLICABLE — delivery decomposition is not required.

## Activation triggers

- Delivery Plan requires phases
- Delivery Plan requires delivery units
- greenfield implementation needs phase contracts
- large or multi-session decomposition needs bounded delivery contracts

## Required inputs

- `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`
- `_hirmos/session/DESIGN.md`
- `_hirmos/session/unresolved-items.md`
- preservation/regression needs when applicable

## Execution controls contributed

- phase control
- Design control
- artifact-backed checkpoint control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/design-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific contract; do not execute from chat summaries or raw inputs alone.

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
