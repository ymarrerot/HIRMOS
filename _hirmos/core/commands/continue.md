# Command: hirmos continue

Purpose: continue an active governed HIRMOS session from its current lifecycle boundary.

## Execution contract

Produces:

- updated `_hirmos/session/SESSION_EXECUTION.md`
- updated active-session artifacts required by the current boundary
- checkpoint or terminal state output

Terminal states:

- Needs User Decision
- Ready for Implementation
- Implementation Complete
- Ready to Update System State
- Closed / Archived
- Blocked / Fail-Closed

## Required reads

Before execution:

1. `_hirmos/core/protocol/COMMANDS.md`
2. `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md`
2. `_hirmos/core/authority/EXECUTION_CONTROL_GOVERNANCE.md`
3. `_hirmos/session/SESSION_EXECUTION.md`
4. Any governing command, authority, protocol, capability, stack, template, or artifact file named by pending controls, including `_hirmos/core/protocol/GOVERNED_CHECKPOINTS.md` when a checkpoint will be surfaced.


## Production-shaped engineering posture

When the command reaches Design, Implementation, or close/update-state for software work, HIRMOS must apply the production-shaped default from `_hirmos/core/authority/LIFECYCLE.md` and `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Do not treat prototype/demo/local-only shortcuts as neutral defaults. They must be explicitly authorized, evidenced, and preserved as limitations or carry-forward items.

## Required behavior


### Beyond Clear Specs execution-control subset

This command applies the execution-control subset of `_hirmos/core/authority/BEYOND_CLEAR_SPECS.md` through `SESSION_EXECUTION.md`: clear command/boundary controls, strict self-validation before surfaced claims, append-only evidence/control records, and fail-closed behavior when the active artifacts do not support the claim.



### Command-state gate

Before advancing work, `hirmos continue` must apply `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` and verify:

- `_hirmos/session/SESSION_STATE.json` exists and is valid;
- `status` is `active`;
- `hirmos continue` is legal for the current `lifecycle_stage` and `allowed_next_commands`;
- required active-session artifacts exist: `SESSION_SCOPE.md`, `SESSION_EXECUTION.md`, `unresolved-items.md`, and `SESSION_SCOPE.md` close verification;
- no gated unresolved item blocks the requested boundary;
- if `lifecycle_stage = implementation_complete`, a bare `hirmos continue` is rejected unless `pending_correction = true` or the command includes a correction/contract-amendment request.

If the command is illegal, contradictory, or under-specified, stop at `Blocked / Fail-Closed` and recommend exactly one governed recovery command.

### Append-only ledger gate

Before making material changes, `hirmos continue` must inspect the existing `SESSION_EXECUTION.md` continuation pass register and preserve it. The command must append a new pass record; it must not replace prior passes with a fresh summary.

Required pre-pass checks:

- identify the latest recorded continuation pass number;
- compare it to `SESSION_STATE.json.continuation_pass`;
- classify the new pass as `INITIAL_IMPLEMENTATION`, `CORRECTIVE`, `CONTRACT_AMENDMENT`, `VALIDATION_ONLY`, or `ROUTE_BACK`;
- determine whether the user request changes scope or corrects existing scope;
- identify affected implementation-unit files and unresolved-item records before editing them.

If the latest recorded pass and `SESSION_STATE.json.continuation_pass` disagree, stop at `Blocked / Fail-Closed` until the ledger is reconciled.

### Required state mutation

Every accepted `hirmos continue` must:

- increment `SESSION_STATE.json.continuation_pass`;
- append a continuation pass record to `SESSION_EXECUTION.md` before surfacing results;
- append the control mutation and ledger integrity records required by `SESSION_EXECUTION.md`;
- update `lifecycle_stage`, `allowed_next_commands`, `recommended_next_command`, `pending_correction`, and `blocking_reason` as the pass outcome requires.

The command must not reset `continuation_pass` or rewrite prior continuation pass records. Do not replace an earlier continuation pass, evidence row, unit review, or unresolved-item disposition when adding a correction or amendment.

### Continue sequence

1. Verify bootstrap passed.
2. Verify `_hirmos/session/SESSION_EXECUTION.md` exists and declares an active session.
3. Read current lifecycle boundary, continuation state, terminal-state history, pending controls, blocked controls, and next allowed action.
4. If the previous state was `Needs User Decision`, locate and record the user response before proceeding.
5. Resolve required controls for the next allowed step.
6. Read only the adaptive files required by those controls.
7. Continue within the active lifecycle boundary or route to the next boundary only when controls allow it.
8. Route back if new evidence invalidates earlier stage authority.
9. Stop at the first governed checkpoint, readiness boundary, completion boundary, blocked state, or close/archive state.



## Cumulative continuation pass model

Every `hirmos continue` invocation must append a new continuation pass record to `SESSION_EXECUTION.md`. It must not overwrite prior pass history, evidence, unresolved-item dispositions, session-scope review results, or implementation-unit reviews.

Continuation pass types:

- Initial implementation pass
- Corrective pass inside the existing Session Scope
- Contract amendment pass when the user expands scope
- Validation-only pass
- Route-back pass

If the user requests work outside the current Session Scope, HIRMOS must amend `SESSION_SCOPE.md` before implementation. If the request is a correction inside existing scope, HIRMOS must record it as a corrective continuation pass. Bare `hirmos continue` after `implementation_complete` is illegal unless `SESSION_STATE.json.pending_correction` is true or `SESSION_EXECUTION.md` Current Continuation Snapshot explicitly recommended `hirmos continue`.

## Session artifact update rules

`hirmos continue` may instantiate or update artifacts required by the current lifecycle boundary and pending controls. It must not create all templates by default.

If a later boundary discovers that an earlier artifact is wrong or incomplete, `hirmos continue` must record a route-back in `SESSION_EXECUTION.md`, reset affected downstream controls, and return to the owning lifecycle stage. It must not silently rewrite earlier-stage authority from a later stage.

Any new or updated artifact must be recorded in the Artifact Instantiation Log or Lifecycle Progress Log as appropriate.

## Control handling

`hirmos continue` must not treat stale `SATISFIED` controls as automatically valid when new evidence, user changes, route-back records, or artifact changes affect them.

When new evidence invalidates an earlier boundary:

1. create a route-back record;
2. mark affected downstream controls `PENDING` or `BLOCKED`;
3. return to the owning lifecycle boundary;
4. do not silently rewrite earlier authority artifacts from a later stage.

## Required `SESSION_EXECUTION.md` updates

Before returning control to the user, update:

- Control status changes;
- User-decision disposition, when applicable;
- Route-back records, when applicable;
- Artifact changes;
- Lifecycle progress;
- Checkpoint record;
- Terminal state and next allowed action;
- Ledger integrity self-validation;
- Control mutation ledger entries when control statuses changed.

## Fail-closed conditions

Stop at `Blocked / Fail-Closed` when:

- `SESSION_EXECUTION.md` is missing or contradictory;
- pending controls have no governing file or evidence path;
- a required artifact is missing or placeholder-only;
- unresolved gated items remain without a user decision;
- Design authorization is missing before Implementation;
- evidence is claimed but not recorded;
- route-back is required but the owning stage cannot be identified.

## Governed checkpoint rules

Before surfacing a checkpoint that asks for a decision, claims readiness/completion, fails closed, or changes continuation state, HIRMOS must:

1. read `_hirmos/core/protocol/GOVERNED_CHECKPOINTS.md`;
2. update `_hirmos/session/SESSION_EXECUTION.md` → `Current Continuation Snapshot` when required;
3. verify the Current Continuation Snapshot is backed by existing non-placeholder session artifacts;
4. verify unresolved-item status from `_hirmos/session/unresolved-items.md` when decisions, assumptions, blockers, or continuation are involved;
5. record the surfaced boundary in `SESSION_EXECUTION.md` Continuation Boundary Log;
6. surface only claims supported by the Current Continuation Snapshot and active controls.


## Project-type and stack controls

When the active request involves software work, the command must ensure project-type and stack controls are represented in `SESSION_EXECUTION.md`.

Required behavior:

- classify project type from evidence, not User Request label alone;
- select stack from repository evidence first, then accepted state, request/config preference, prototype evidence, installed packages, or `generic` fallback;
- record material project-type decisions in `DESIGN.md` / `SESSION_SCOPE.md`, record machine-readable stack routing in `stack-resolution.json` when needed, and record command controls in `SESSION_EXECUTION.md`;
- activate stack contexts only when evidence shows multiple bounded stack areas;
- block or route back when project type, stack, or stack context uncertainty affects authority or evidence.


## Runtime integration controls

When the active request may involve material runtime services, read `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` and add runtime-integration controls to `SESSION_EXECUTION.md`.

Required behavior:

- instantiate or update `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` when material integration areas affect Design, Implementation, evidence, production readiness, or close;
- do not silently downgrade real integration requirements to fixtures, mocks, console fallbacks, or boundary-only work;
- do not surface low-level provider choices to Domain Expert users unless the protocol requires surfacing;
- do not claim implementation completion, production readiness, or close success beyond the integration posture supported by evidence.

## Vertical slice and status UX

When the active request uses a durable Delivery Plan, Phase, or implementation slice, read `_hirmos/core/protocol/VERTICAL_SLICE_AND_STATUS_UX.md` and `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md`.

Required behavior:

- identify the active Delivery Unit / Phase when one exists;
- keep `SESSION_EXECUTION.md` aligned with the active slice status;
- recommend exactly one primary next command/action unless blocked;
- do not imply the next Delivery Unit is authorized unless its governing contract and controls support it.

## Claim reconciliation behavior

When this command surfaces a material readiness, progress, implementation, validation, runtime, integration, production-readiness, packaging, update-state, or close claim, it must apply `_hirmos/core/protocol/CLAIM_RECONCILIATION.md`.

Unsupported, unlogged, contradicted, or environment-blocked claims must be downgraded, routed back, or blocked before being shown as complete.


## Current-system-state-first continuation rule

When `hirmos continue` advances into Design, Implementation, or a route-back that depends on current-state understanding, verify that `_hirmos/session/DESIGN.md` records current-system-state-first completion.

If `CURRENT_SYSTEM_STATE.md` exists but was not read by Understand System State, route back to Understand System State before advancing.

Firm rule: do not continue meaningful Design or Implementation while current-system-state-first controls are `PENDING` or `BLOCKED`.

## Durable Delivery Pointer Concordance

Before advancing implementation on a delivery-governed session, `hirmos continue` must verify that `SESSION_SCOPE.md` delivery authority agrees with Current System State active delivery pointers and the durable Delivery Plan / Phase file.

If the session scope, current-state pointer, Delivery Plan, and active Phase file disagree, `hirmos continue` must fail closed and route to delivery governance reconciliation before implementation proceeds.

## Durable Phase Adoption Continuation Check

Before executing delivery-governed implementation, `hirmos continue` must verify that the active Session Scope still adopts exactly one durable phase and that the adopted phase path still exists.

A continuation may amend the adopted phase only through a Contract Amendment in `SESSION_SCOPE.md`. The amendment must record whether it is a same-phase scope correction, a partial-adoption clarification, or a blocked attempt to switch phases.

Fail-closed rule: `hirmos continue` must not silently switch to a different phase, combine multiple phases into one session, or implement phase items not adopted into the Session Scope.


## Delivery Status Continuation Guard

Before a continuation pass advances or corrects delivery-governed work, `hirmos continue` must verify that the active Session Scope, Current System State delivery pointers, Delivery Plan, and adopted Phase status still agree.

If a prior close or continuation left the Delivery Plan or Phase status stale, `hirmos continue` must route back to delivery status reconciliation before authorizing more implementation work.

## Phase Entry Gate Enforcement

This command must respect the Phase Entry Gate for delivery-governed sessions.

- `hirmos start` must not reach implementation readiness when the adopted phase has no passing Phase Entry Gate.
- `hirmos continue` must re-check Phase Entry Gate concordance before continuing implementation if delivery governance is active.
- `hirmos status` must report whether the active phase is adoptable, blocked, or uncertain based on lifecycle status, phase type, and entry controls.
- `hirmos close` must fail closed if the session implemented a phase without recorded Phase Entry Gate authorization.

Required status terms: Phase Entry Gate, lifecycle status, phase type, entry criteria satisfied, greenfield entry controls, brownfield entry controls, pointer concordance.

## Phase Progress / Carry-Forward Enforcement

This command must respect phase progress and carry-forward enforcement for delivery-governed sessions.

- `hirmos start` must inspect prior Phase Progress Ledger rows before treating a multi-session phase as new work.
- `hirmos continue` must preserve append-only phase progress and must not drop partial, blocked, deferred, or open phase items.
- `hirmos status` must report whether phase progress is accepted, partial, blocked, deferred, or waiting on carry-forward obligations.
- `hirmos close` must fail closed when phase outcome is `PARTIAL`, `BLOCKED`, or `DEFERRED` and carry-forward obligations are missing.

Required status terms: Phase Progress Ledger, Carry-Forward Items, partial phase, blocked phase, deferred phase, resulting lifecycle status, Current System State active/next phase pointer.


## Phase Acceptance Enforcement

`hirmos continue` must preserve the Phase Acceptance Evidence Gate record. If the session is moving toward accepted phase status, it must append evidence and not overwrite previous evidence, unit reviews, or unresolved/carry-forward decisions.


## Continuation ledger integrity check

Before writing a new continuation pass, count the existing continuation passes and identify their detail headings in `_hirmos/session/SESSION_EXECUTION.md`. After writing the new pass, verify that every previous pass row and detail heading is still present and that the new pass was appended.

If the ledger was overwritten or an earlier detail block was removed, restore the missing history before surfacing the checkpoint. This is a command-state violation, not an acceptable cleanup.


## Production-shaped engineering continuation gate

When implementation is active for software work, `hirmos continue` must preserve the Production-Shaped Engineering Gate from `DESIGN.md`, `SESSION_SCOPE.md`, and `SESSION_EXECUTION.md`.

Required behavior:

- do not implement shortcuts that contradict the gate unless the Session Scope is amended first;
- record route-back when implementation evidence invalidates the production-shaped design or delivery shape;
- materialize `EVIDENCE.md` when command/runtime/provider/storage/database evidence becomes nontrivial;
- do not claim implementation completion when code evidence contradicts production-shaped claims.
