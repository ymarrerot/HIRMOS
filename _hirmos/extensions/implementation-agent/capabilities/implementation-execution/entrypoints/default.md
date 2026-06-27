# implementation-execution

## Execution Contract

### Purpose

Execute one sealed implementation unit contract using its `IU-xx.md` artifact as the execution authority, while appending implementation evidence only to append-only execution sections.

### Produces

- append-only updates to `_hirmos/session/implementation-units/IU-xx.md` Execution Record section
- project/file changes authorized by the unit
- validation/evidence entries appended to the IU Execution Record and/or `_hirmos/session/EVIDENCE.md` when nontrivial evidence cannot fit cleanly in the IU artifact
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
- one sealed `_hirmos/session/implementation-units/IU-xx.md` with complete Unit Scope / Authority and Pre-Execution Checks
- stack/project context and required files

## Execution controls contributed

- implementation execution control
- unit evidence control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/implementation-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

Execution must:

1. Read the target `IU-xx.md` artifact directly.
2. Confirm the Unit Scope / Authority is non-placeholder and the contract status is `SEALED` before material edits.
3. Confirm the Session Scope still authorizes the unit.
4. Confirm `unresolved-items.md` has no gated blocker for the unit.
5. Inspect current project files before editing.
6. Modify only files/areas authorized by the sealed IU contract.
7. Append actions, files changed, validation, runtime posture, evidence, limitations, test/fixture/validator change rationale when applicable, and execution result to the `Execution Record` section only.
8. Record route-back or blocker conditions in `SESSION_EXECUTION.md` and `unresolved-items.md` when applicable.

Do not execute from prose, checkpoint summaries, or old split artifacts. The sealed IU Contract sections are the execution authority. The executor must not edit sealed contract sections after material implementation starts; if contract authority is wrong or incomplete, stop and route back instead of repairing the contract during execution.




## Required behavior


### Governance posture check

Implementation execution is not autonomous code editing followed by HIRMOS reporting. Before editing, confirm that the active IU contract is sealed execution authority and that the current command state permits implementation. If not, stop before mutation. During and after execution, append only to execution/evidence sections; do not update contract status, scope, acceptance criteria, or authority fields to make the record look compliant.


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

## PROD-L8.19 execution authority gate

Before editing project files, implementation execution must verify that the target `IU-xx.md` existed before material changes, contains non-placeholder Unit Scope / Authority, Files / Areas, Binary Acceptance Criteria, Verification Commands / Checks, and Evidence Requirements, and records `Contract status: SEALED`.

If the IU is missing, placeholder-only, unsealed, or was created/expanded retrospectively after implementation began, implementation execution must stop and route to correction/deviation handling. Do not execute from `SESSION_SCOPE.md` implementation-shape preview alone when IU mode is active.

## PROD-L8.21 execution authorization proof

Before material edits, implementation execution must verify `SESSION_EXECUTION.md` contains a current `PROD-L8.21 IU Set Authority Checkpoint` with `Authorization decision: IMPLEMENTATION_AUTHORIZED`, unless the session explicitly declared `LIGHTWEIGHT_NO_IU` before implementation began.

Do not treat thin IU stubs, unsealed IU contracts, retrospective IU files, or post-execution contract edits as execution authority.


## PROD-L8.23 Runtime Authority Enforcement
Before material edits, implementation execution must inspect generated `SESSION_EXECUTION.md` and generated IU files. If the IU Set Authority Checkpoint, authorization decision, coverage map, sealed contract status, or minimum IU contract is missing, execution must fail closed or route back to IU planning. It must not proceed on transcript claims or IU self-attestation alone.


## PROD-L8.24 Material Edit Start Gate
Before the first material project-file edit, confirm that `_hirmos/session/SESSION_EXECUTION.md` already contains the `Pre-Material-Edit Ledger Row`, `Authorization decision: IMPLEMENTATION_AUTHORIZED`, and `Retrospective checkpoint, IU expansion, or sealed-contract mutation: NO`. Then append a `Material Edit Start Record` that points back to the authorization row. If the authorization row is absent, appears only in an archive/close cleanup context, or was created to satisfy the validator after edits, fail closed and route back to IU planning/correction.


## PROD-L8.25 Sealed IU Contract Mutation Guard

After `Contract status: SEALED` and before the first material project-file edit, the executor must treat Unit Identity / Contract Metadata, Unit Scope / Authority, Pre-Execution Checks, Verification Commands / Checks, Evidence Requirements, Runtime Integration Posture, and Binary Acceptance Criteria as immutable contract authority. Execution may append only to Execution Record, applicable retry evidence, and external evidence surfaces. If implementation reality requires changing sealed contract authority, record `ROUTE_BACK_REQUIRED` and stop before further project-file mutation.
