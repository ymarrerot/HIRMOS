# Command: hirmos close

Purpose: run Update System State when ready, archive the session, and reset the active session area.

## Execution contract

Produces:

- update-state decision or blocked-close report
- archived session under `_hirmos/system/history/sessions/<session-id>/` when close succeeds
- reset active session area after successful close

Terminal states:

- Closed / Archived
- Close Blocked
- Abort Closed
- No Active Session

## Required reads

Before execution:

1. `_hirmos/core/protocol/COMMANDS.md`
2. `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md`
2. `_hirmos/core/authority/LIFECYCLE.md`
3. `_hirmos/core/authority/ARTIFACT_MODEL.md`
4. `_hirmos/core/authority/EXECUTION_CONTROL_GOVERNANCE.md`
5. `_hirmos/core/protocol/VALIDATION_AND_EVIDENCE.md`
6. `_hirmos/core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md`
7. `_hirmos/session/SESSION_EXECUTION.md`
7. Active session artifacts named by update-state controls


## Production-shaped engineering posture

When the command reaches Design, Implementation, or close/update-state for software work, HIRMOS must apply the production-shaped default from `_hirmos/core/authority/LIFECYCLE.md` and `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Do not treat prototype/demo/local-only shortcuts as neutral defaults. They must be explicitly authorized, evidenced, and preserved as limitations or carry-forward items.

## Required behavior


### Beyond Clear Specs execution-control subset

This command applies the execution-control subset of `_hirmos/core/authority/BEYOND_CLEAR_SPECS.md` through `SESSION_EXECUTION.md`: clear command/boundary controls, strict self-validation before surfaced claims, append-only evidence/control records, and fail-closed behavior when the active artifacts do not support the claim.


Before close may claim success, `SESSION_EXECUTION.md` must show ledger integrity self-validation: all continuation passes preserved, latest pass number concordant with `SESSION_STATE.json.continuation_pass`, control mutations recorded, and no corrective pass left unresolved.


### Command-state gate

Before normal close, `hirmos close` must apply `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` and verify:

- `_hirmos/session/SESSION_STATE.json` exists and is valid;
- `status` is `active`;
- `hirmos close` is legal for the current `lifecycle_stage` and `allowed_next_commands`;
- `SESSION_SCOPE.md`, `SESSION_EXECUTION.md`, `unresolved-items.md`, and `SESSION_SCOPE.md` close verification exist and are non-placeholder;
- `SESSION_SCOPE.md` close verification has a final coverage verdict compatible with close;
- no gated unresolved item remains open unless explicitly deferred/carried with user approval;
- implementation-unit reviews are complete when implementation occurred.

If any check fails, stop at `Close Blocked` and recommend exactly one governed recovery command. Do not archive as normal close and do not update accepted current state from incomplete work.

### Required state mutation

A normal close must:

- update active `SESSION_STATE.json` during close to reflect close execution;
- archive the session with an archived `SESSION_STATE.json` normalized to `status = closed` and `lifecycle_stage = closed`;
- reset active `_hirmos/session/SESSION_STATE.json` to idle after archive succeeds;
- reset `session_id` and `blocking_reason` to empty/null, reset `allowed_next_commands` to `["hirmos start", "hirmos status"]`, and reset `recommended_next_command` to `hirmos start`;
- leave no stale active-session artifacts outside the allowed idle scaffold.

### Close sequence

1. Verify bootstrap passed.
2. Verify active session exists.
3. Verify Update System State controls.
4. Verify no required controls are `PENDING` or `BLOCKED` unless using an explicit abort close path.
5. Verify accepted outcomes, rejected outcomes, evidence-only artifacts, and carry-forward unresolved items are distinguished.
6. Create or update the system-state update artifact required by the active path.
7. Preserve accepted outcomes, carry-forward unresolved items, evidence, and `SESSION_EXECUTION.md` in history.
8. Archive the active session under `_hirmos/system/history/sessions/<session-id>/`.
9. Reset active session area to clean idle state after successful close.
10. Do not perform Design or Implementation during close.


## Archive and reset artifact rules

`hirmos close` must preserve the complete active session artifact set under `_hirmos/system/history/sessions/<session-id>/` before resetting `_hirmos/session/`.

Normal close resets the active session area to minimal idle scaffolding only:

```text
_hirmos/session/.gitkeep
_hirmos/session/SESSION_STATE.json
_hirmos/session/bootstrap/.gitkeep
```

Abort close preserves available artifacts and blocked reasons in history but must not present aborted work as accepted system state.

## Required close controls

Record or verify these controls before normal close:

| Control | Blocking condition |
|---|---|
| Active session control | no active session or contradictory session state |
| Update System State control | no update-state decision or readiness record |
| Evidence control | claimed outcomes lack evidence |
| Unresolved carry-forward control | unresolved items not resolved or carried forward |
| Archive control | archive path unavailable or incomplete |
| Active-session reset control | session reset plan missing |

## Abort close

Abort close is allowed only when normal close cannot proceed and the user explicitly requests abort or the command specification permits it.

Abort close must preserve the session state, blocked reason, unresolved items, and available evidence in history. It must not present aborted work as accepted system state.

## Blocked close

Stop at `Close Blocked` when:

- required Update System State controls are `PENDING` or `BLOCKED`;
- session evidence is missing or contradictory;
- gated unresolved items remain unresolved;
- implementation was started but not reviewed;
- archive preservation cannot be completed;
- close would require new Design or Implementation work.

## Governed checkpoint rules

Before surfacing a checkpoint that asks for a decision, claims readiness/completion, fails closed, or changes continuation state, HIRMOS must:

1. read `_hirmos/core/protocol/GOVERNED_CHECKPOINTS.md`;
2. update `_hirmos/session/SESSION_EXECUTION.md` → `Current Continuation Snapshot` when required;
3. verify the Current Continuation Snapshot is backed by existing non-placeholder session artifacts;
4. verify unresolved-item status from `_hirmos/session/unresolved-items.md` when decisions, assumptions, blockers, or continuation are involved;
5. record the surfaced boundary in `SESSION_EXECUTION.md` Continuation Boundary Log;
6. surface only claims supported by the Current Continuation Snapshot and active controls.


## Project-type and stack awareness

When reporting or closing a session, include project-type and stack status if those controls were active.

Do not claim Update System State readiness or close success if project-type or stack assumptions are stale, contradicted, or unresolved in a way that affects accepted outcomes.


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


## Command-state close transition

`hirmos close` is legal only when `SESSION_STATE.json.lifecycle_stage` is `implementation_complete`, `close_ready`, or an explicitly design-only terminal boundary. A normal close must reset active `SESSION_STATE.json` to `status: idle`, empty `session_id`, `lifecycle_stage: idle`, `allowed_next_commands: ["hirmos start", "hirmos status"]`, `recommended_next_command: hirmos start`, and no `blocking_reason`. The archived `SESSION_STATE.json` must be normalized to a closed/history state, not active.

## Accepted-state integrity gate

### Accepted-state and reset integrity gate

Before normal close success can be surfaced, HIRMOS must verify the complete close transaction described by `_hirmos/core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md`.

Required checks:

- `SESSION_SCOPE.md` and `SESSION_SCOPE.md` close verification classify promised work, verified work, gaps, deferred items, and final verdict.
- `unresolved-items.md` has no unresolved gated item blocking close, and all non-gating assumptions are accepted, resolved, or carried forward.
- implementation units in `implementation-units/` are reviewed when Implementation was active.
- `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` and active-only `CARRY_FORWARD.md` are updated only with accepted and carried outcomes.
- the archive contains `SESSION_EXECUTION.md` archive controls and the complete active session artifact set or recorded exceptions.
- archived `SESSION_STATE.json` is normalized to closed/history state, not active.
- active `_hirmos/session/SESSION_STATE.json` is reset to idle after normal close.
- active `_hirmos/session/` contains only allowed idle scaffolding: `SESSION_STATE.json`, `.gitkeep`, `bootstrap/.gitkeep`, and `implementation-units/.gitkeep`.
- `SESSION_EXECUTION.md`, `SESSION_SCOPE.md` close verification, the archive manifest, and accepted-state records do not contradict each other.

If any check fails, the terminal state is `Close Blocked`, not `Closed / Archived`.

## Claim reconciliation behavior

When this command surfaces a material readiness, progress, implementation, validation, runtime, integration, production-readiness, packaging, update-state, or close claim, it must apply `_hirmos/core/protocol/CLAIM_RECONCILIATION.md`.

Unsupported, unlogged, contradicted, or environment-blocked claims must be downgraded, routed back, or blocked before being shown as complete.

## Consolidated close-gate invariants

`hirmos close` validates durable framework invariants, not historical patch labels. A normal close may report `Closed / Archived` only when each applicable invariant group below is satisfied by the owning artifact.

### Archive and session-state integrity invariant

Required behavior:

1. Preserve the complete active session artifact set under `_hirmos/system/history/sessions/<session-id>/` before resetting `_hirmos/session/`.
2. Normalize the archived `SESSION_STATE.json` so a normally closed archive is terminal, not `active`.
3. Reset active `_hirmos/session/SESSION_STATE.json` to idle after archive succeeds.
4. Verify `SESSION_EXECUTION.md` archive controls, `ARCHIVE_MANIFEST.md / SESSION_EXECUTION.md close controls`, accepted-state records, and post-close status agree.

If archive/session-state integrity fails, the terminal state is `Close Blocked`.

### Durable current-system-state merge invariant

Required behavior:

1. Read existing `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`.
2. Classify material outcomes in `SESSION_SCOPE.md` close verification close-verification record as accepted, superseded, rejected / not applied, evidence-only, carry-forward, or blocked.
3. Merge accepted and superseded truth into `CURRENT_SYSTEM_STATE.md`.
4. Update `DECISION_LOG.md` for durable decisions.
5. Update `CARRY_FORWARD.md` for unresolved or future-session obligations.
6. Update `CURRENT_SYSTEM_STATE.md` accepted-state navigation and latest-close metadata in the same file.
7. Preserve accepted-state invariant blocks in `CURRENT_SYSTEM_STATE.md`, `CARRY_FORWARD.md`, and `DECISION_LOG.md`.

Do not claim close success if `CURRENT_SYSTEM_STATE.md` was not updated or explicitly verified as unchanged.

### Claim reconciliation and evidence materialization invariant

Normal close is itself a material close/archive/update-state claim. Therefore `_hirmos/session/EVIDENCE.md` must exist for every normal close when claim reconciliation is applicable, and the close claim must be reconciled before it is surfaced.

Required behavior:

1. Reconcile every material readiness, progress, implementation, validation, runtime, integration, production-readiness, packaging, update-state, and close claim through `_hirmos/core/protocol/CLAIM_RECONCILIATION.md`.
2. Materialize the owning evidence artifact required by the active scope before close; summaries in chat, carry-forward prose, or another artifact do not substitute for the owning artifact.
3. Downgrade, route back, or block unsupported, unlogged, contradicted, or environment-blocked claims before showing them as complete.
4. Treat missing required evidence artifacts as close blockers, not future cleanup.

### Local runtime and role-workflow evidence invariant

Required behavior:

1. Create or verify `EVIDENCE.md` when local setup, local runtime, database, service, environment, or secret-readiness claims are made.
2. Create or verify `EVIDENCE.md` when role/user/workflow readiness is claimed or role workflows are in scope, even if all workflow checks are `NOT_RUN`, `BLOCKED`, or `NOT_APPLICABLE`.
3. Keep build/test/lint evidence separate from local runtime readiness and role-workflow readiness.

### Canonical value invariant

Required behavior:

1. Use only canonical claim/evidence states from `_hirmos/core/protocol/CLAIM_RECONCILIATION.md` in structured evidence/status fields.
2. Use only canonical runtime posture values from `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` in structured runtime posture fields.
3. Do not use accepted-state decision classifications, prose observations, shorthand labels, or provider-specific phrases as structured evidence or runtime posture values.
4. Translate noncanonical shorthand before close; examples such as `LOCAL_REAL`, `observed`, `build pass`, or `ACCEPTED_AT_CLOSE` are not valid structured values.

### Package cleanliness invariant

When close surfaces or links a package/review package, the package claim must be reconciled and supported by packaging evidence.

Required behavior:

1. Exclude local secret files, generated runtime folders, source-control folders, dependency folders, and operating-system metadata unless they are intentionally packaged as explicitly labeled local evidence.
2. Treat a package link as a material package claim.
3. Block package-cleanliness claims when `.env`, `.DS_Store`, `__MACOSX`, `node_modules`, `.next`, `.git`, or generated runtime folders are present and not explicitly justified.

### Validator execution invariant

Run or record the result of:

```text
python3 _hirmos/tools/validate.py
```

when framework files changed, accepted-state invariants were touched, generated HIRMOS artifacts were updated, or close claims validation/compliance. A failing validator result blocks normal close until the owning artifact is repaired or the failure is explicitly classified as outside the active scope with rationale.

### Close result rule

If any applicable invariant group fails, the terminal state is `Close Blocked`. Do not claim normal close success, do not bury the failure in carry-forward only, and do not present failed validation as a successful close with caveats.

## Requirements and coverage invariant

Normal close must update requirement coverage when `_hirmos/session/REQUIREMENTS.md` exists or when requirements were material to the session.

Close must verify:

- `_hirmos/session/REQUIREMENTS.md` exists for material requirements work;
- every material in-scope requirement has a coverage status;
- every material requirement is mapped to delivered work, carry-forward, gated/unresolved state, blocked state, rejection, or explicit not-applicable rationale;
- `_hirmos/system/accepted-state/REQUIREMENTS.md` is created or updated when requirements remain relevant across sessions;
- `CURRENT_SYSTEM_STATE.md` references the accepted requirements and summarizes coverage posture without replacing the requirement catalog.

If requirements coverage is incomplete or contradictory, terminal state is `Close Blocked` unless the incomplete coverage is explicitly accepted as carry-forward, deferred, blocked, or out of scope.

## Durable Delivery Pointer Close Requirement


When close accepts, partially accepts, blocks, defers, cancels, supersedes, or advances a delivery, update delivery navigation in both `_hirmos/system/delivery/DELIVERY_PLAN.md` and `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`.

If the accepted delivery has a planned follow-up delivery in the Delivery Index, record:

- Last accepted delivery
- Next recommended delivery
- Next recommended delivery scope
- Next governed command: `hirmos start`

Close is blocked if delivery navigation is applicable but left stale, contradictory, or missing without an explicit not-applicable rationale.

When a session creates, updates, accepts, blocks, supersedes, or advances durable delivery artifacts, `hirmos close` must update or explicitly verify unchanged the Active Development Context and Delivery Pointers in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`.

Close is blocked if:

- accepted delivery work is not reflected in Current System State delivery pointers;
- Current System State points to a stale active phase after the phase was accepted, superseded, or replaced;
- a next phase or next governed command is known but not recorded;
- delivery governance was required and the Delivery Plan / Phase path pointers are missing.

## Durable Phase Adoption Close Requirement

When delivery governance is active, `hirmos close` must verify the adopted durable phase before archive/reset.

Close requires:

- one adopted phase in `SESSION_SCOPE.md`;
- direct review of the durable `PHASE-xx.md` in `SESSION_SCOPE.md` close verification;
- accepted, partial, blocked, or superseded phase result recorded in `SESSION_EXECUTION.md` close/update control pointers;
- Delivery Plan status and Current System State delivery pointers updated or explicitly verified unchanged.

Close is blocked if phase adoption is missing, multiple phases are claimed, phase result is not reconciled, or accepted-state pointers would become stale.


## Durable Delivery Status Close Requirement

When delivery governance was active, required, created, changed, accepted, blocked, superseded, or advanced, `hirmos close` must update durable delivery status before normal close success is surfaced.

Required behavior:

1. Read the adopted durable phase from `SESSION_SCOPE.md` Active Durable Phase Adoption.
2. Read the parent `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` and active `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`.
3. Reconcile `SESSION_SCOPE.md` close verification, implementation-unit reviews, unresolved-items dispositions, and evidence against the adopted phase exit criteria.
4. Complete `SESSION_EXECUTION.md` close/update control pointers Close-Time Delivery / Phase Status Transaction.
5. Update or explicitly verify unchanged the adopted `PHASE-xx.md` Close-Time Phase Status Update.
6. Update the parent `DELIVERY_PLAN.md` Delivery Decomposition row and Delivery Status Update Log.
7. Refresh `CURRENT_SYSTEM_STATE.md` Active Development Context and Delivery Pointers.
8. Record carry-forward delivery obligations in `CARRY_FORWARD.md` or the next phase scope.

Close is blocked if Delivery Plan status, Phase status, Session Scope adoption, SESSION_SCOPE.md close-verification verdict, implementation-unit review results, Current System State delivery pointers, and carry-forward obligations cannot be reconciled.

The archive manifest may record the transaction, but it does not substitute for updating the durable Delivery Plan roadmap, Delivery Scope, and Phase file.

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

`hirmos close` must block any delivery-governed close that marks the adopted durable phase `ACCEPTED` unless the Phase Acceptance Evidence Gate is PASS and durable Delivery Plan, Phase, and Current System State updates are applied or explicitly verified unchanged.


## Close-time stale checkpoint normalization

Before claiming close success, reconcile stale active-session checkpoint text against current resolved state. If older sections still say gated items are unresolved, implementation is blocked, or delivery adoption is pending after later passes resolved those controls, close must either update the stale active-session text before archive or record the discrepancy as a blocked close issue.

The archive must not preserve unresolved/blocking claims as active truth when `SESSION_STATE.json`, `SESSION_EXECUTION.md`, `unresolved-items.md`, `SESSION_SCOPE.md` close verification, and accepted-state records show they were resolved.


## Production-shaped engineering close gate

Before normal close, `hirmos close` must review the Production-Shaped Engineering Gate against final files and evidence.

Required close checks:

- “async/background job” claims are supported by an actual background/worker/queue/cron processing path, not only persisted status fields;
- metered-state/billing claims are supported by transactional, idempotent, concurrency-safe, or explicitly constrained code/evidence;
- provider-integration claims match the actual provider mode and environment posture;
- durable data claims match the actual local/production persistence posture;
- secrets, runtime uploads, generated outputs, local databases, caches, and OS metadata are excluded from handoff/release packages unless explicitly attached as evidence;
- critical-flow evidence exists in `EVIDENCE.md` or a not-run/not-applicable rationale is accepted.

If any check fails, close must downgrade the accepted claim, route back, or preserve the limitation as carry-forward. Do not accept production-shaped outcomes contradicted by implementation evidence.

## PROD-L8.9 focus-aware close reconciliation

`hirmos close` must reconcile the route actually used during the session before accepting, partially accepting, blocking, or failing the close.

Required behavior:

1. Read the active capability routing records in `SESSION_EXECUTION.md`.
2. Verify that the route matches the Delivery Shape Decision and `SESSION_SCOPE.md` authority chain.
3. For single-session routes, verify that no unnecessary durable delivery artifacts were created as close authority.
4. For delivery routes, verify `DELIVERY_PLAN.md`, `DELIVERY_SCOPE.md`, any adopted `PHASE-xx.md`, `SESSION_SCOPE.md`, and Current System State pointers are concordant.
5. Verify blocked or route-back capability outcomes have either been resolved or carried forward.
6. Block close success if the focus route claims and durable artifacts disagree.

Close may archive the routing evidence, but archive metadata does not replace updating durable delivery scope, delivery roadmap, phase status, unresolved items, and accepted-state pointers when those artifacts are active.


## PROD-L6 accepted-state/history/archive alignment

During normal close, `hirmos close` must create or update the archived `ARCHIVE_MANIFEST.md` under `_hirmos/system/history/sessions/<session-id>/` and verify that it agrees with `SESSION_EXECUTION.md` close controls, `SESSION_SCOPE.md` close verification, active-session reset, and accepted-state files.

For durable delivery work, the command must refresh Current System State delivery pointers using the PROD-L model:

```text
Delivery roadmap: _hirmos/system/delivery/DELIVERY_PLAN.md
Active delivery scope: _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
Active phase: _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

The archive manifest may record the transaction, but it does not substitute for updating the durable delivery roadmap/register, active delivery scope, phase file, and Current System State delivery pointers.


## PROD-L8.9 focus-aware close behavior

`hirmos close` must reconcile the active focus before claiming success. A delivery-baseline session close records delivery-baseline acceptance/amendment, blocked, deferred, or cancelled status; it must not claim implementation completion. A phase/session or implementation close must reconcile `SESSION_SCOPE.md` first, and when it adopts delivery authority, reconcile the adopted `DELIVERY_SCOPE.md`, active `PHASE-xx.md`, delivery unresolved register, session unresolved register, evidence, and accepted-state pointers.

If a session-level unresolved item invalidates a delivery-level decision or assumption, close must either update the delivery authority, add/update the delivery-level unresolved register, or block/partial-close truthfully.

## PROD-L8.9E/F Focus-Aware Close Guard

`hirmos close` must not claim implementation completion from a delivery-baseline session. Delivery-baseline close can only record delivery-baseline acceptance/amendment/blockage and the next governed phase/session command.


## PROD-L8.10 delivery-baseline close guard

A delivery-baseline runtime session must not be closed as implementation-complete work. If `session_focus = delivery_baseline`, close may only record delivery-baseline acceptance/blockage and runtime-session reset after authority reconciliation. The presence of `_hirmos/session/unresolved-items.md` during delivery-baseline focus is a concordance defect that must be corrected before normal close success.
