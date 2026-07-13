# Command: hirmos continue
Status: compact command authority.
Purpose: provide the low-token command execution surface for `hirmos continue`; use deeper protocols only when a listed gate requires detail.

## Execution contract
Produces: updated `SESSION_LEDGER.md`, updated active-session artifacts required by the current boundary, and checkpoint or terminal output.
Terminal states: Needs User Decision / IU Plan Review / IU Execution Authorized / Implementation Complete / Ready to Update System State / Closed / Archived / Blocked / Fail-Closed.

## Required reads
1. This command file.
2. `_hirmos/core/protocol/COMMANDS.md`.
3. `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md`.
4. `_hirmos/session/SESSION_STATE.json` and `_hirmos/session/SESSION_LEDGER.md`.
5. Adaptive protocols and artifacts named by pending controls.

## Required behavior

Read this command file first, apply its gate checklist exactly, and read deeper protocols only when this command file names a gate requiring deeper detail, validation fails, or active artifacts contradict each other. Do not route through the removed runtime packet wrapper layer.

## Runtime gate checklist
- Governance posture check: HIRMOS is active governance; Do not patch first and reconstruct artifacts after the fact.
- Command-state gate: status is active, `hirmos continue` is legal, and required active-session artifacts exist.
- Required state mutation: increment `SESSION_STATE.json.continuation_pass`, update lifecycle status, allowed commands, recommended command, pending correction, and blocking reason.
- Cumulative continuation pass model: classify every `hirmos continue` invocation before action, append a new continuation pass record, and preserve prior pass history.
- Continue Pass Delta Recording Gate: before project-file edits, implementation continuation, corrective work, validation reruns, route-backs, or completion claims, record the pass classification in `SESSION_LEDGER.md` and update `SESSION_STATE.json.continuation_pass`.
- Append-only ledger gate: append a new continuation pass record before surfaced claims; if the pass changes accepted authority, append the corresponding `SESSION_SCOPE.md` scope amendment / authority delta before implementation continues.
- Runtime Freshness Gate: verify ledger and machine state agree before mutation.
- Current-State-First Source Reading Gate: when routing or accepted-state facts matter, inspect current-state pointers before downstream artifacts.
- Durable Delivery Pointer Concordance: reconcile `Next recommended delivery`; if inconsistent, route back to delivery governance reconciliation.
- Durable Phase Adoption Continuation Check: must not silently switch to a different phase.
- Phase Entry Gate Enforcement: inspect Phase Entry Gate, lifecycle status, and phase type.
- Phase Progress / Carry-Forward Enforcement: inspect Phase Progress Pointer Index and Carry-Forward Items.
- Phase Acceptance Enforcement: inspect Phase Acceptance Evidence Gate.
- Delivery Status Continuation Guard: route back to delivery status reconciliation when delivery status conflicts exist.

## Baseline and implementation boundary
- PROD-L8.32Z Baseline Acceptance Gate: baseline acceptance or amendment must be recorded before material project/source edits. If the user says `hirmos continue` from a baseline checkpoint, classify the pass first and update `SESSION_LEDGER.md`; if authority changes, append the `SESSION_SCOPE.md` authority delta before edits.
- Accepted baseline authority is necessary but not always sufficient for implementation. When IU mode is required or planned, baseline acceptance authorizes IU planning/materialization only and does not authorize material project/source edits.
- If IU mode is not required, implementation may begin only after accepted baseline authority is recorded, the ledger pre-edit gate is PASS, and the current command state allows implementation.
- If the user asks to accept baseline and implement in one message, split the work at the applicable boundary: create/validate IU plan first when IU mode applies, or record accepted baseline authority and pre-edit ledger gate before any material edits when IU mode does not apply.


## PROD-L8.33A Continue Command Integration Gate and IU Planning Enforcement

`hirmos continue` must classify and gate before it codes. The command is not automatically an implementation command. Before material project/source edits, implementation claims, validation reruns that affect readiness, route-backs, or close-preparation claims, HIRMOS must read the active session state, classify the continuation request, increment `SESSION_STATE.json.continuation_pass`, and append the continuation pass record to `SESSION_LEDGER.md`.

When the user requests implementation units and no accepted IU plan exists, `hirmos continue` must create or revise the IU plan, run active generated-artifact validation, surface `IU Plan — Review or Change`, and stop. If the user does not request implementation units, HIRMOS must still evaluate whether IUs are required by scope, risk, multi-file impact, validation complexity, or governance value. If IUs are required, baseline acceptance authorizes IU Planning only and does not authorize material project/source edits.

If implementation units are not required, record a concise no-IU rationale in the existing session governance artifacts before implementation begins. Never create IU files after material implementation to show compliance.

## IU Planning / IU Execution boundary
- PROD-L8.32I IU Planning Boundary Restoration: when the current pause is a session baseline and IU mode is required/planned, `hirmos continue "Accept session baseline"` authorizes IU planning only. It must create or verify full `implementation-units/IU-xx.md` files, update `SESSION_LEDGER.md` with `IU_PLANNING_COMPLETE`, run active generated-artifact validation, and pause for IU plan review. It must not edit project files or execute IUs in the same continuation.
- IU execution may begin only after a later explicit continuation such as `hirmos continue "Accept IU plan and begin IU execution"` records `IU_EXECUTION_AUTHORIZED` in `SESSION_LEDGER.md`.
- If the user asks to accept the session baseline and implement in one message, split the work: perform IU planning/materialization first, surface the IU-plan pause, and do not perform material project-file edits until IU execution is separately authorized.
- PROD-L8.9E/F Baseline Acceptance Boundary: must not implement directly from the delivery-baseline checkpoint.
- PROD-L8.10 delivery-baseline continuation surface rule: session-level unresolved items remain `NOT_APPLICABLE`.
- PROD-L8.11 Delivery-Baseline Optional Authority Location: Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.
- PROD-L8.19 idle-state command legality: bare `hirmos continue` is rejected when session state does not permit it.
- PROD-L8.19 IU pre-execution authority gate: implementation units must be sealed before material project-file edits.
- PROD-L8.32D IU Authority Boundary Continuation Rule: the scope IU table is not an implementation plan, not a sealed contract.
- PROD-L8.31 Generated-Run Mechanical Continuation Gate: planned IU count and actual full `IU-xx.md` files match; do not accept a narrative compliance statement as a gate result.
- Implementation-Unit Instantiation Timing: must fail closed before any project-file or artifact mutation when IU authority is missing.
- Material edit boundary: material project-file edits are prohibited until `IU_EXECUTION_AUTHORIZED` exists in `SESSION_LEDGER.md`; `IU_PLANNING_COMPLETE` alone is not execution authorization.
- PROD-L8.32K Runtime Boundary and Validator Invocation Fixture Hardening: before any lifecycle transition claim, record the command authority used and an active gate validator result. IU-mode material implementation, material project-file edits, implementation-complete claims, and close-readiness claims are blocked unless `IU_EXECUTION_AUTHORIZED` is present after IU plan review.
- L8.32K negative fixture rule: if baseline acceptance creates IU files but no `IU_EXECUTION_AUTHORIZED` gate exists, any project-file diff, Material Edit Start Record, or implementation-complete claim must fail validation.


## Scope and delivery safety
Do not expand delivery scope silently. If the user request changes authority, route back or amend scope before implementation. If unsafe, Fail-Closed.

For every `hirmos continue`, classify the pass as `ACCEPTANCE_ONLY`, `INITIAL_IMPLEMENTATION`, `SCOPE_AMENDMENT`, `CORRECTIVE_PASS`, `VALIDATION_ONLY`, `ROUTE_BACK`, `IU_EXECUTION_AUTHORIZATION`, `CLOSE_PREPARATION`, or `BLOCKED` before acting. Same-scope corrections require a ledger pass record and affected IU/evidence updates. New or changed acceptance criteria, IU objectives, scope promises, exclusions, validation requirements, or close-satisfaction criteria require both a ledger pass record and an append-only `SESSION_SCOPE.md` authority delta before project-file edits continue.


## Artifact synchronization rule

Update canonical owning artifacts only. Do not maintain duplicate mutable narrative status in roadmap, phase, current-state, evidence, and ledger at the same time. Derived values such as recommended next command must be recomputed from gates, not independently authored. Stale or contradictory sections fail closed.

## PROD-L8.32L Just-in-Time Artifact Creation and Derived Pointer Indexes

Optional artifacts are not created to satisfy a template checklist. Create them only when the current governed boundary makes their owning concern applicable:

- `EVIDENCE.md` only when evidence volume, claim reconciliation, review-gate evidence, or close/archive evidence cannot be represented safely by ledger/IU evidence pointers.
- `_hirmos/session/unresolved-items.md` only when session-level unresolved items exist or unresolved-register review is required for the current boundary.
- session `REQUIREMENTS.md` / `DESIGN.md` only when separate session-level authority is explicitly justified after the flow reaches session or phase-session scope.
- delivery `DELIVERY_PLAN.md`, `DELIVERY_SCOPE.md`, delivery unresolved register, and `PHASE-xx.md` only when delivery governance is selected and the specific delivery/phase boundary is active.
- implementation-unit files only after session baseline acceptance and during IU planning; never during `hirmos start` pre-acceptance planning.

Pointer indexes in Current System State, Delivery Plan, Phase files, and ledger status surfaces are derived navigation caches. Prefer deriving them from filesystem paths, active session state, session ledger rows, archive manifests, and delivery/phase directories. If a derived pointer index conflicts with source artifacts, source artifacts win and the runtime must fail closed instead of preserving the stale pointer row.


## PROD-L8.32S Runtime Command Surface Unification

This file is the canonical compact command runtime authority for `hirmos continue`. `_hirmos/core/runtime/` and `*.packet.md` command wrappers are removed. Do not route through a separate runtime packet; read this command file first, then read protocols only when this command file names a gate requiring deeper detail, validation fails, or active artifacts contradict each other.


## Validator-preserved command markers

- PROD-L8.9 focus-aware continuation behavior applies to every continuation.
- HIRMOS must not expand delivery scope silently.
## Ledger discipline reference markers

- identify the latest recorded continuation pass number
- compare it to `SESSION_STATE.json.continuation_pass`
- append the control mutation and ledger integrity records
- Do not replace an earlier continuation pass
- classify every `hirmos continue` invocation before action
- if the pass changes accepted authority, append the corresponding `SESSION_SCOPE.md` authority delta before implementation continues
- Beyond Clear Specs execution-control subset
- clear command/boundary controls
- strict self-validation before surfaced claims
- fail-closed behavior when the active artifacts do not support the claim
- accepts the recommended baseline unless the user requested changes before continuing
- instantiate implementation-unit artifacts when the accepted Session Scope requires them
- after session-baseline acceptance in IU mode, pause for IU plan review before implementation execution
- never interpret `hirmos continue "Accept session baseline"` as permission to edit project files when IU mode applies


## Artifact synchronization rule

Command execution must update the canonical owner of each fact and use pointers elsewhere. Do not duplicate mutable status across session, delivery, phase, current-state, evidence, and carry-forward artifacts. `SESSION_STATE.json` command fields are derived cache values and must be recomputed from ledger gates and command legality rules.

## PROD-L8.32L Just-in-Time Artifact Creation and Derived Pointer Indexes

Commands must not instantiate optional artifacts merely because a template exists. Create optional artifacts only when the current boundary makes the owning concern applicable. Treat Current System State, Delivery Plan, Phase, and ledger pointer rows as derived navigation caches over source artifacts; stale pointer rows fail closed.
