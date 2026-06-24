# implementation-execution

## Execution Contract

### Purpose

Execute one approved implementation unit using its self-contained `IU-xx.md` artifact as the execution contract.

### Produces

- updated `_hirmos/session/implementation-units/IU-xx.md` Execution Record section
- project/file changes authorized by the unit
- validation/evidence entries in the same IU artifact and/or `_hirmos/session/EVIDENCE.md` when nontrivial evidence cannot fit cleanly in the IU artifact
- `_hirmos/session/SESSION_EXECUTION.md` execution-control updates

### Terminal States

- COMPLETED — unit execution finished and evidence was recorded.
- BLOCKED — execution cannot continue under current authority.
- FAILED — execution was attempted and failed within scope.
- ROUTE_BACK_REQUIRED — execution exposes invalid design/scope/current-state assumptions.
- NOT_APPLICABLE — no implementation execution is required.

## Activation triggers

- an approved implementation unit is ready to execute
- implementation stage is active

## Required inputs

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/unresolved-items.md`
- one approved `_hirmos/session/implementation-units/IU-xx.md` with a complete Unit Scope
- stack/project context and required files

## Execution controls contributed

- implementation execution control
- unit evidence control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/implementation-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

Execution must:

1. Read the target `IU-xx.md` artifact directly.
2. Confirm the Unit Scope is non-placeholder and approved for execution.
3. Confirm the Session Scope still authorizes the unit.
4. Confirm `unresolved-items.md` has no gated blocker for the unit.
5. Inspect current project files before editing.
6. Modify only files/areas authorized by the IU artifact; modify only files/areas authorized.
7. Record actions, files changed, validation, runtime posture, evidence, limitations, and execution result inside the same `IU-xx.md`.
8. Record route-back or blocker conditions in `SESSION_EXECUTION.md` and `unresolved-items.md` when applicable.

Do not execute from prose, checkpoint summaries, or old split artifacts. The IU artifact is the execution authority.




## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

