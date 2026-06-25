# implementation-unit-planning

## Execution Contract

### Purpose

Decompose the implementation scope authorized by `_hirmos/session/SESSION_SCOPE.md` into bounded implementation units, and create one self-contained unit artifact per unit under `_hirmos/session/implementation-units/`.

### Produces

- `_hirmos/session/SESSION_SCOPE.md` Implementation Unit Plan section updates
- `_hirmos/session/implementation-units/IU-xx.md` artifacts
- `_hirmos/session/SESSION_EXECUTION.md` implementation-unit planning control

### Terminal States

- COMPLETE — implementation units are explicit, bounded, and collectively cover the Session Scope or explicitly record uncovered scope.
- BLOCKED — required design/scope/current-state input is missing or contradictory.
- ROUTE_BACK_REQUIRED — planning exposes invalid design, missing scope authority, or impossible acceptance criteria.
- NOT_APPLICABLE — implementation is not active for this session.

## Activation triggers

- the Session Scope authorizes implementation
- implementation is non-trivial, multi-file, risky, or delegated to an implementation agent
- implementation-readiness requires unit decomposition

## Required inputs

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/unresolved-items.md`
- current system state and relevant design/delivery/phase/requirements artifacts
- stack/project evidence when implementation touches project files

## Execution controls contributed

- implementation-unit planning control
- Session Scope unit coverage control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/implementation-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

Planning must:

1. Read the Session Scope directly.
2. Read `unresolved-items.md` directly and fail closed if a gated item blocks implementation planning.
3. Create one self-contained `implementation-units/IU-xx.md` artifact per unit from `_hirmos/core/templates/session/implementation-units/IU.md`.
4. Fill each IU artifact's Unit Scope sections before execution begins.
5. Update the Session Scope Implementation Unit Plan table with the unit list and coverage mapping.
6. Literally answer in `SESSION_SCOPE.md`: `Do all planned implementation units collectively cover 100% of SESSION_SCOPE.md?`
7. Record the capability decision and evidence in `SESSION_EXECUTION.md`.

Do not create standalone `SESSION_SCOPE.md Implementation Unit Plan`, `implementation-units/IU-xx.md`, `implementation-units/IU-xx.md`, `implementation-units/IU-xx.md`, or `implementation-units/IU-xx.md` artifacts. Unit request, execution, review, and retry content live inside each `IU-xx.md` artifact.

## Required behavior


### Governance posture check

Implementation-unit planning creates execution authority before material work. It must not be used to reconstruct task files after implementation unless the session is explicitly recording a governance deviation/correction.


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

## PROD-L8.19 pre-execution authority requirement

This capability is the last allowed step before IU-governed material implementation begins. If the session requires IU mode, this capability must create the IU artifacts before any implementation-execution capability or project-file edit is performed.

Required control:

- record in `SESSION_EXECUTION.md` that IU artifacts were created before material edits;
- mark each IU with the `PROD-L8.19 Pre-Execution Authority Declaration`;
- fail closed if implementation has already occurred and IU files are being reconstructed after the fact;
- if reconstruction is necessary for audit, record it as a governance deviation/correction, not as normal IU planning.
