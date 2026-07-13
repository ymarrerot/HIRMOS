# implementation-execution

## Execution Contract

### Purpose

Execute one sealed implementation unit contract using its `IU-xx.md` artifact as the execution authority, while appending implementation evidence only to append-only execution sections.

### Produces

- append-only updates to `_hirmos/session/implementation-units/IU-xx.md` Execution Record section
- project/file changes authorized by the unit
- validation/evidence entries appended to the IU Execution Record and/or `_hirmos/session/EVIDENCE.md` when nontrivial evidence cannot fit cleanly in the IU artifact
- `_hirmos/session/SESSION_LEDGER.md` execution-control updates

### Terminal States

- COMPLETED — unit execution finished and evidence was recorded.
- BLOCKED — execution cannot continue under current authority.
- FAILED — execution was attempted and failed within scope.
- ROUTE_BACK_REQUIRED — execution exposes invalid design/scope/current-state assumptions.
- NOT_APPLICABLE — no implementation execution is required.

## Activation triggers

- the IU plan has been explicitly accepted for execution
- `SESSION_LEDGER.md` records `IU_EXECUTION_AUTHORIZED`
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
8. Record route-back or blocker conditions in `SESSION_LEDGER.md` and `unresolved-items.md` when applicable.

Do not execute from prose, checkpoint summaries, or old split artifacts. The sealed IU Contract sections are the execution authority. The executor must not edit sealed contract sections after material implementation starts; if contract authority is wrong or incomplete, stop and route back instead of repairing the contract during execution.




## Required behavior

### Governance posture check

Implementation execution is not autonomous code editing followed by HIRMOS reporting. Before editing, confirm that the active IU contract is sealed execution authority and that the current command state permits implementation. If not, stop before mutation. During and after execution, append only to execution/evidence sections; do not update contract status, scope, acceptance criteria, or authority fields to make the record look compliant.

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## PROD-L8.19 execution authority gate

Before editing project files, implementation execution must verify that the target `IU-xx.md` existed before material changes, contains non-placeholder Unit Scope / Authority, Files / Areas, Binary Acceptance Criteria, Verification Commands / Checks, and Evidence Requirements, and records `Contract status: SEALED`.

If the IU is missing, placeholder-only, unsealed, or was created/expanded retrospectively after implementation began, implementation execution must stop and route to correction/deviation handling. Do not execute from `SESSION_SCOPE.md` implementation-shape preview alone when IU mode is active.

## PROD-L8.21 execution authorization proof

Before material edits, implementation execution must verify `SESSION_LEDGER.md` contains a current `PROD-L8.21 IU Set Authority Checkpoint`, `IU_PLANNING_COMPLETE`, and `IU_EXECUTION_AUTHORIZED`, unless the session explicitly declared `LIGHTWEIGHT_NO_IU` before implementation began. Legacy ledger rows may also include `Authorization decision: IMPLEMENTATION_AUTHORIZED`, but under L8.32I that phrase is not sufficient unless `IU_EXECUTION_AUTHORIZED` is also present.

Do not treat thin IU stubs, unsealed IU contracts, retrospective IU files, or post-execution contract edits as execution authority.


## PROD-L8.23 Runtime Authority Enforcement
Before material edits, implementation execution must inspect generated `SESSION_LEDGER.md` and generated IU files. If the IU Set Authority Checkpoint, authorization decision, coverage map, sealed contract status, or minimum IU contract is missing, execution must fail closed or route back to IU planning. It must not proceed on transcript claims or IU self-attestation alone.


## PROD-L8.24 Material Edit Start Gate
Before the first material project-file edit, confirm that `_hirmos/session/SESSION_LEDGER.md` already contains the `Pre-Material-Edit Ledger Row`, `IU_EXECUTION_AUTHORIZED`, and `Retrospective checkpoint, IU expansion, or sealed-contract mutation: NO`. Then append a `Material Edit Start Record` that points back to the authorization row. If the authorization row is absent, appears only in an archive/close cleanup context, or was created to satisfy the validator after edits, fail closed and route back to IU planning/correction.


## PROD-L8.25 Sealed IU Contract Mutation Guard

After `Contract status: SEALED` and before the first material project-file edit, the executor must treat Unit Identity / Contract Metadata, Unit Scope / Authority, Pre-Execution Checks, Verification Commands / Checks, Evidence Requirements, Runtime Integration Posture, and Binary Acceptance Criteria as immutable contract authority. Execution may append only to Execution Record, applicable retry evidence, and external evidence surfaces. If implementation reality requires changing sealed contract authority, record `ROUTE_BACK_REQUIRED` and stop before further project-file mutation.

## PROD-L8.28 Execution-Time Full-IU Guard

Before material edits, implementation execution must reject thin generated IU stubs. `Contract status: SEALED` is not sufficient unless the IU also contains the full non-placeholder sealed contract areas, `LLM Write Permission:` lines, verification/evidence requirements, binary acceptance criteria, and failure/route-back condition.

During execution, append concrete execution evidence to the Execution Record. Before claiming unit execution complete, the IU must show `Execution status: COMPLETED`, changed files/actions, validation/check outcomes, claim evidence, limitations, and execution result. If tests, fixtures, mocks, snapshots, validators, expected-output files, or regression fixtures changed, the Test / Fixture / Validator Change Rationale must be completed before review.

## PROD-L8.31 Mechanical Execution Block

Implementation execution must block when generated-run mechanical gates fail. Do not execute if:

- the current session lacks complete fresh bootstrap answers;
- IU mode is planned but planned IU count does not match actual full IU files;
- any target IU is thin, placeholder-only, unsealed, or retrospectively created;
- `SESSION_LEDGER.md` lacks a current generated-artifact validation PASS when completion/close readiness is being claimed.

Execution may resume only after artifact correction, route-back, or an explicit blocked/partial decision is recorded.


## PROD-L8.32D Execution Authority Boundary

## PROD-L8.32I Execution Authorization Boundary

Implementation execution must not start after `hirmos continue "Accept session baseline"` when IU mode applies. That continuation authorizes IU planning only. Execution may start only after the separate IU-plan review pause is accepted and `SESSION_LEDGER.md` records `IU_EXECUTION_AUTHORIZED`. If the ledger has `IU_PLANNING_COMPLETE` but not `IU_EXECUTION_AUTHORIZED`, block execution and surface `IU Plan — Review or Change`.


Implementation execution must not start from a `SESSION_SCOPE.md` IU table, preview, or planned-IU pointer list. Execution authority for IU mode requires full non-placeholder IU files under `_hirmos/session/implementation-units/` plus a `SESSION_LEDGER.md` gate PASS. If only `SESSION_SCOPE.md` contains IU-like detail, block execution and route to implementation-unit planning.


## PROD-L8.32K Runtime Boundary Execution Block

Implementation execution must not start from session baseline acceptance or IU planning completion. It may start only after `SESSION_LEDGER.md` records `IU_EXECUTION_AUTHORIZED` after IU plan review and the active gate validator result allows execution. If the validator is not run or fails, do not edit project files.

## PROD-L8.32Z baseline acceptance gate

Material project/source edits require accepted baseline authority recorded in `SESSION_SCOPE.md` and `SESSION_LEDGER.md`. When IU mode applies, accepted baseline authority authorizes IU planning only; implementation execution still requires full IU artifacts, IU plan review, and `IU_EXECUTION_AUTHORIZED`.
