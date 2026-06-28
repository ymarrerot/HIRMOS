# implementation-unit-planning

## Execution Contract

### Purpose

Decompose the implementation scope authorized by `_hirmos/session/SESSION_SCOPE.md` into bounded implementation units, and create one sealed-contract unit artifact per unit under `_hirmos/session/implementation-units/`.

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
4. Fill each IU artifact's Unit Identity / Contract Metadata, Unit Scope / Authority, Pre-Execution Checks, Verification Commands / Checks, Evidence Requirements, and Binary Acceptance Criteria before execution begins.
5. Mark the contract sections with explicit `LLM Write Permission:` lines and seal the contract before material implementation begins.
6. Update the Session Scope Implementation Unit Plan table with the unit list and coverage mapping.
7. Literally answer in `SESSION_SCOPE.md`: `Do all planned implementation units collectively cover 100% of SESSION_SCOPE.md?`
8. Record the capability decision and evidence in `SESSION_EXECUTION.md`.

Do not create standalone `SESSION_SCOPE.md Implementation Unit Plan`, duplicate IU request files, duplicate IU execution files, duplicate IU review files, or duplicate IU retry files. Unit contract, execution, review, retry, and handoff content live inside each `IU-xx.md` artifact, but the IU Contract sections are sealed authority and later execution/review/retry sections are append-only records.

## Required behavior


### Governance posture check

Implementation-unit planning creates sealed execution authority before material work. It must not be used to reconstruct or improve IU contract authority after implementation unless the session explicitly records route-back, contract reopening/supersession, or a governance deviation/correction.


1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.

## Canonical interaction posture visibility

Use the canonical HIRMOS interaction posture from `_hirmos/core/authority/INTERACTION_POSTURE.md`: concise user-facing output, transparent artifact pointers for governed claims, and progressive disclosure when risk, validation failure, blocker state, route-back, or user request requires more detail.

- By default, surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- Surface capability result, assumptions, artifacts/evidence, and review implications when requested or needed for responsible review.
- Surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis when validation failure, blocker state, route-back, or inspection need requires it.

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

## PROD-L8.21 IU set authority planning

Before implementation execution, this capability must generate or verify the complete IU set and then record the `PROD-L8.21 IU Set Authority Checkpoint` in `SESSION_EXECUTION.md`.

The IU set must map adopted phase/session scope to IU files, prove minimum IU contract completeness, identify sequencing/dependencies, and return `IMPLEMENTATION_AUTHORIZED` only when the set is non-placeholder and complete.


## PROD-L8.23 Generated-Run Enforcement Duty
This capability must produce generated IU artifacts that can pass runtime validation, not only framework-template validation. Before implementation execution, it must update `SESSION_EXECUTION.md` with the IU authority checkpoint, authorization decision, non-placeholder IU review, and IU Set Coverage Map. Thin generated IU stubs are invalid when IU mode is active.


## PROD-L8.24 Pre-Execution Ledger Duty
After creating the IU set and before implementation execution, write the `Pre-Material-Edit Ledger Row` into `_hirmos/session/SESSION_EXECUTION.md`. This row must state that material implementation has not started, identify the IU files verified, record `Retrospective checkpoint or IU expansion: NO`, and authorize or block execution. Do not wait until close/archive to add or expand IU authority.

Compatibility note: implementation-unit planning creates execution authority before material work and must not reconstruct task files after implementation as if they were pre-existing authority.

## PROD-L8.21 IU set authority planning

Before implementation, planning must support the `PROD-L8.21 IU Set Authority Checkpoint` in `SESSION_EXECUTION.md`, including coverage map evidence and authorization decision `IMPLEMENTATION_AUTHORIZED` / `BLOCKED` / `LIGHTWEIGHT_NO_IU`.

## PROD-L8.23 Generated-Run Enforcement Duty

Thin generated IU stubs are not sufficient execution authority. Generated sessions must produce sealed, non-placeholder IU contracts before material edits and must not expand IU contract authority retrospectively.

## PROD-L8.28 Generated IU Instantiation Duty

Implementation-unit planning must instantiate the full IU sealed-section model, not a short status stub. Before authorizing implementation, each IU file must include non-placeholder contract content and `LLM Write Permission:` lines for every major section in `_hirmos/core/templates/session/implementation-units/IU.md`.

Required generated IU contract areas before execution:

- Unit Identity / Contract Metadata;
- Unit Scope / Authority;
- Objective, Context, In Scope, Out of Scope, Files / Areas, Preservation Rules;
- Implementation Requirements;
- Verification Commands / Checks;
- Evidence Requirements;
- Runtime Integration Posture;
- Binary Acceptance Criteria;
- Pre-Execution Checks;
- PROD-L8.21 Minimum IU Contract;
- Failure / route-back condition.

If any generated IU lacks these areas or contains placeholder-only content, return `BLOCKED` or `ROUTE_BACK_REQUIRED`; do not authorize implementation and do not rely on later close/archive cleanup to expand the IU.

## PROD-L8.31 Planned-IU Materialization Gate

When the accepted session scope says IUs are required or planned, this capability must materialize the full planned IU set before implementation execution.

Required output before implementation:

- planned IU count from `SESSION_SCOPE.md`;
- actual full IU files created under `_hirmos/session/implementation-units/`;
- count match result;
- non-placeholder full-template check for every IU;
- `SESSION_EXECUTION.md` `PROD-L8.31 Generated-Run Mechanical Gate Record` updated to show that planned IU count matches actual full IU files.

If planned IU count and actual full IU files do not match, authorization decision is `BLOCKED`, not `IMPLEMENTATION_AUTHORIZED`.
