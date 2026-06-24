# technical-review

## Execution Contract

### Purpose

Create reviewer-facing technical assumption, risk, decision, and inspection material without overloading Domain Expert output.

### Produces

- `_hirmos/session/DESIGN.md`
- `_hirmos/session/DESIGN.md technical assumptions summary`
- `_hirmos/session/unresolved-items.md technical-review items`
- `_hirmos/session/SESSION_EXECUTION.md technical-review control updates`

### Terminal States

- COMPLETED — technical review material is recorded or explicitly not applicable.
- NEEDS_USER_DECISION — technical risk creates a user-owned domain/risk/resource decision.
- BLOCKED — technical evidence is insufficient.
- ROUTE_BACK_REQUIRED — technical review exposes missing system-state or Design evidence.
- NOT_APPLICABLE — no material technical assumptions or review path is needed.

## Activation triggers

- technical assumptions or tradeoffs exist
- security/data/integration/performance/migration/preservation risk exists
- third-party review pointer is needed
- domain_expert output should progressively disclose technical detail

## Required inputs

- `_hirmos/session/DESIGN.md`
- `_hirmos/session/DESIGN.md`
- `_hirmos/session/unresolved-items.md`
- stack/project-type evidence when applicable

## Execution controls contributed

- technical-review control
- Design control
- snapshot-backed checkpoint control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/design-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.


## Capability-specific obligations

- Third-party review pointers.
- challenge/change path.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## Runtime integration responsibilities

When material runtime services are involved, follow `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

Record or consume `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` as required by execution controls.

Do not claim fixture/mock/boundary/local/production integration levels beyond what the active artifacts and evidence support.
