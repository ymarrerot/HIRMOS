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


## First continuation after start checkpoint

When `hirmos continue` is the first continuation after a `Recommended Baseline — Review or Change` checkpoint, it accepts the recommended baseline only when no gated unresolved item requires user input and every gated item is either resolved, explicitly adopted from a surfaced recommendation, or reclassified as non-gating with a documented assumption. Compatibility phrase: when no gated unresolved item blocks acceptance, `hirmos continue` accepts the recommended baseline unless the user requested changes before continuing. A baseline cannot be both `gated / pending user input / reflected in authority: NO` and silently accepted by bare `hirmos continue`.

Before implementation begins, `hirmos continue` must:

- verify that `SESSION_SCOPE.md` exists and records the accepted or amended session scope baseline;
- verify that `_hirmos/session/unresolved-items.md#Current Checkpoint Feed` has no unresolved gated item blocking Implementation;
- apply any user-requested baseline changes before proceeding;
- instantiate implementation-unit artifacts before material code changes begin when the accepted Session Scope requires implementation-unit mode; this satisfies the legacy rule to instantiate implementation-unit artifacts when the accepted Session Scope requires them;
- record the baseline acceptance, amendments, and created implementation-unit artifacts in `SESSION_EXECUTION.md`;
- stop or route back if the baseline is uncertain, contradicted, or missing required review items.

Full implementation-unit artifacts must be created in `_hirmos/session/implementation-units/` only after this acceptance/amendment boundary. Do not treat a pre-acceptance implementation-shape preview as implementation-unit authority.


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
- Scope amendment pass when the user expands scope
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
- do not imply the next Delivery Unit is authorized unless its governing authority and controls support it.

## Claim reconciliation behavior

When this command surfaces a material readiness, progress, implementation, validation, runtime, integration, production-readiness, packaging, update-state, or close claim, it must apply `_hirmos/core/protocol/CLAIM_RECONCILIATION.md`.

Unsupported, unlogged, contradicted, or environment-blocked claims must be downgraded, routed back, or blocked before being shown as complete.


## Current-system-state-first continuation rule

When `hirmos continue` advances into Design, Implementation, or a route-back that depends on current-state understanding, verify that `_hirmos/session/DESIGN.md` records current-system-state-first completion.

If `CURRENT_SYSTEM_STATE.md` exists but was not read by Understand System State, route back to Understand System State before advancing.

Firm rule: do not continue meaningful Design or Implementation while current-system-state-first controls are `PENDING` or `BLOCKED`.

## Durable Delivery Pointer Concordance


When continuation enters Design, Implementation, correction, or close preparation for delivery-governed work, verify that the active session still matches `CURRENT_SYSTEM_STATE.md` delivery navigation. If `Next recommended delivery` exists but the session is working on a different delivery, record the user/request override or route back to delivery governance reconciliation.

Before advancing implementation on a delivery-governed session, `hirmos continue` must verify that `SESSION_SCOPE.md` delivery authority agrees with Current System State active delivery pointers and the durable Delivery Plan / Phase file.

If the session scope, current-state pointer, Delivery Plan, and active Phase file disagree, `hirmos continue` must fail closed and route to delivery governance reconciliation before implementation proceeds.

## Durable Phase Adoption Continuation Check

Before executing delivery-governed implementation, `hirmos continue` must verify that the active Session Scope still adopts exactly one durable phase and that the adopted phase path still exists.

A continuation may amend the adopted phase only through a Scope Amendment in `SESSION_SCOPE.md`. The amendment must record whether it is a same-phase scope correction, a partial-adoption clarification, or a blocked attempt to switch phases.

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

## PROD-L8.9 focus-aware continuation behavior

`hirmos continue` must preserve the capability route and `session_focus` selected by `hirmos start` unless a governed active-authority amendment changes it.

Required behavior:

- Re-read `SESSION_STATE.json`, `SESSION_EXECUTION.md`, the active authority, focus-appropriate unresolved items, and any adopted delivery/phase artifacts before delivery-baseline acceptance, phase/session baseline preparation, implementation, or correction work.
- Re-run capability routing checks for required focus-route controls: `delivery-baseline`, `phase-baseline`, `session-scope`, and `implementation-readiness` when applicable.
- Block continuation if the active focus authority was removed, contradicted, made stale, or not accepted/amended before the command tries to advance past it.
- Block continuation if a session attempts to implement work from a different delivery or phase than the adopted authority chain.
- Record route preservation, route amendment, or route-back in `SESSION_EXECUTION.md`.

A continuation pass may add evidence or implementation-unit detail, but it must not expand delivery scope silently.


## PROD-L8.9 delivery-baseline continuation behavior

When `session_focus = delivery_baseline`, `hirmos continue` does not implement. It must treat the Delivery Baseline — Review or Change checkpoint as accepted unless the user requested amendments first, apply any amendments to `DELIVERY_SCOPE.md`, delivery-level `unresolved-items.md`, optional delivery `REQUIREMENTS.md`/`DESIGN.md`, and `DELIVERY_PLAN.md`, then set the next focus to `phase_session_baseline` when a phase/session should be prepared.

After delivery-baseline acceptance or amendment, `hirmos continue` may instantiate only the next needed `PHASE-xx.md` when phase files are selected. It must not instantiate future phase files by default. The instantiated phase must include a scalar Phase Entry Gate field: `Entry criteria status: SATISFIED` when the accepted/amended delivery baseline satisfies entry criteria. A table may add detail, but it must not replace this scalar field.

The same continuation pass must then create the bounded `SESSION_SCOPE.md` for that phase/session and pause with `Session Baseline — Review or Change`; implementation starts only on a later allowed continuation after the session baseline is accepted or amended. Before surfacing the checkpoint, refresh `SESSION_EXECUTION.md` so `phase-baseline` and `session-scope` rows are `COMPLETED` with evidence paths, not left `PENDING`; refresh Current System State Delivery Pointer Concordance so active phase and session scope rows are not `NOT_APPLICABLE`; and refresh `DELIVERY_PLAN.md` Active Development Context so `Current phase` points to the instantiated phase.

When `session_focus = session_baseline` or `phase_session_baseline`, `hirmos continue` treats the session baseline as accepted unless the user requested amendments first, then may instantiate implementation-unit artifacts only when needed by the accepted scope.

## PROD-L8.9E/F Baseline Acceptance Boundary

If the prior checkpoint was `Delivery Baseline — Review or Change`, `hirmos continue` accepts or amends delivery authority, then prepares the next phase/session baseline and pauses again. It must not implement directly from the delivery-baseline checkpoint. If the prior checkpoint was `Session Baseline — Review or Change`, `hirmos continue` accepts or amends the session baseline before implementation-unit artifacts are instantiated.


## PROD-L8.10 delivery-baseline continuation surface rule

When continuing from `session_focus = delivery_baseline`, session-level unresolved items remain `NOT_APPLICABLE` until `hirmos continue` advances into `phase_session_baseline` and creates a bounded `SESSION_SCOPE.md`. The command must not create `_hirmos/session/unresolved-items.md` as a placeholder while still in delivery-baseline acceptance. If a delivery decision becomes blocked or amended, update `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` and the delivery authority, not the session unresolved register.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.


## PROD-L8.13 Delivery Review Wording

When reporting delivery-baseline state, use status-aware delivery labels. Before baseline acceptance, use Candidate Delivery, Proposed Delivery, or Delivery Under Baseline Review. Use Active Delivery only after the baseline has been accepted/amended and the delivery is in a post-acceptance state. Explain routing from current-state-first evidence and governance need rather than from greenfield/brownfield labels alone.


## PROD-L8.14 navigation update rule

`hirmos continue` must preserve `CURRENT_SYSTEM_STATE.md` as the navigation authority while transitioning focus. When delivery baseline acceptance creates a phase/session baseline, active delivery, active phase, active session scope, and source artifact pointers must remain aligned. It must not create root accepted-state requirements/design/scope artifacts as a substitute for delivery/session source authorities.

## Current-State-First Source Reading Gate

Before Design, Implementation, continuation across delivery/phase/session boundaries, or close/update-state, `hirmos continue` must verify that Understand System State followed the canonical navigation path:

1. `CURRENT_SYSTEM_STATE.md` was read first.
2. Active governance pointers were followed: active delivery scope, active phase, active session scope, active unresolved registers, latest close/archive pointer, and active carry-forward records when present.
3. Source artifacts materially relevant to the requested continuation were read before material design or implementation.
4. Source-reading coverage was recorded in `SESSION_EXECUTION.md`, `BOOTSTRAP_REPORT.md`, or the active authority when material.

If this cannot be verified, route back to Understand System State before advancing.

## Runtime Freshness Gate

After every governed transition or implementation pass, `hirmos continue` must refresh the active snapshot and affected mirrors without rewriting append-only history:

- `SESSION_STATE.json` lifecycle and focus fields;
- `SESSION_EXECUTION.md` Current Continuation Snapshot, Machine Command State Concordance, Active Execution Controls, Focus-Aware Capability Routing Log, artifact instantiation log, and affected boundary records;
- `PHASE-xx.md` lifecycle/progress/acceptance fields when a phase is active;
- `SESSION_SCOPE.md` implementation-shape preview and close-verification status when implementation-unit records or evidence exist;
- `EVIDENCE.md` claim reconciliation when command/environment/runtime evidence changes;
- `CURRENT_SYSTEM_STATE.md` active navigation pointers when active delivery/phase/session pointers change.

Stale lower sections are not harmless if they contradict the current snapshot or machine state. HIRMOS must either reconcile them or mark them as historical rows with pass/date/context.

## Implementation-Unit Instantiation Timing

When implementation-unit mode is active, full implementation-unit artifacts must be instantiated immediately after the session baseline is accepted/amended and before material code changes begin. Retrospective implementation-unit creation after code changes is allowed only when the session explicitly declared a lightweight/no-IU mode, or when HIRMOS records a correction explaining the deviation and reconciles unit authority against actual changes before claiming completion.
