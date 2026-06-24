# system-design

## Execution Contract

### Purpose

Produce system/application design from governed requirements and system-state evidence.

### Produces

- `_hirmos/session/DESIGN.md system/application design section`
- `_hirmos/session/DESIGN.md technical review when technical assumptions or risks exist`
- `_hirmos/session/unresolved-items.md updates`
- `_hirmos/session/SESSION_EXECUTION.md Design control updates`

### Terminal States

- COMPLETED — system/application design is recorded with reviewable assumptions.
- NEEDS_USER_DECISION — a design decision belongs to the user and blocks readiness.
- BLOCKED — governed requirements or system-state evidence are missing.
- ROUTE_BACK_REQUIRED — design requires additional current-state evidence.
- NOT_APPLICABLE — request does not require system/application design work.

## Activation triggers

- request requires architecture, workflow, data, integration, UI/API, permission, preservation, or technical design decisions
- governed requirements require implementation authorization inputs
- technical assumptions must be made reviewable

## Required inputs

- `_hirmos/session/DESIGN.md governed requirements section`
- `_hirmos/session/DESIGN.md`
- `_hirmos/session/unresolved-items.md`
- stack/project-type evidence when available

## Execution controls contributed

- Design control
- technical-review control
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

- Design from governed requirements, not raw requirement inputs alone.
- technical review.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in the focus-appropriate unresolved register selected by `SESSION_STATE.json.session_focus`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in the selected unresolved register, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## Runtime integration responsibilities

When material runtime services are involved, follow `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

Record or consume `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` as required by execution controls.

Do not claim fixture/mock/boundary/local/production integration levels beyond what the active artifacts and evidence support.
