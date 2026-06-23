# Command: hirmos status

Purpose: inspect active or last-known HIRMOS state without advancing governed work.

## Execution contract

Produces:

- read-only status summary

Terminal states:

- Status Reported
- No Active Session
- Status Blocked By Missing/Contradictory State

## Required reads

Before execution:

1. `_hirmos/core/protocol/COMMANDS.md`
2. `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md`
2. `_hirmos/session/SESSION_STATE.json`
3. `_hirmos/session/SESSION_EXECUTION.md` when present
4. `_hirmos/system/history/sessions/` only when no active session exists or the user asks for historical status

## Required behavior

`hirmos status` must report ledger integrity when a session is active: latest continuation pass, `SESSION_STATE.json.continuation_pass`, whether the ledger appears append-only, and the legal next governed command. It must not mutate the ledger.


### Command-state gate

`hirmos status` must apply `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` without mutating files. It must read `SESSION_STATE.json` and report whether the recorded command state is internally legal.

Status must report:

- current `status` and `lifecycle_stage`;
- legal next commands from `allowed_next_commands`;
- exactly one primary `recommended_next_command`;
- contradictions between `SESSION_STATE.json`, `SESSION_EXECUTION.md`, active-session artifacts, accepted-state latest-close metadata, archive state, or the post-close scaffold.

If command legality cannot be determined, status must return `Status Blocked By Missing/Contradictory State` and recommend exactly one governed recovery command.

### Status sequence

1. Verify bootstrap passed.
2. Inspect active session state and execution spine, if present.
3. If no active session exists, inspect last known history only when useful.
4. Report current status without mutating files.
5. Include next allowed action when it can be determined from recorded state.

## Status output should include

- active session id, if any;
- active command;
- interaction mode;
- active lifecycle boundary;
- continuation state;
- pending or blocked execution controls;
- active gated unresolved items;
- latest checkpoint;
- next allowed command/action;
- missing or contradictory state, if any.

## Prohibited behavior

`hirmos status` must not:

- create or modify session artifacts;
- mark controls satisfied;
- resolve unresolved items;
- advance lifecycle work;
- instantiate templates;
- update accepted system state;
- archive or close a session.


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

When Delivery Units, Phases, or implementation slices exist, read `_hirmos/core/protocol/VERTICAL_SLICE_AND_STATUS_UX.md`.

Status output must include:

- active Delivery Unit / Phase, if any;
- current Delivery Unit status;
- latest governed checkpoint;
- blocked controls or gated unresolved items;
- next allowed command/action;
- next recommended Delivery Unit when known.

`hirmos status` may read durable delivery pointers in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` and durable delivery artifacts under `_hirmos/system/delivery/<delivery-id>/`, but must not create or mutate them.

## Post-close status behavior

After normal close, `hirmos status` must report:

- no active governed session;
- latest archived session path when known;
- current-state latest-close metadata path;
- carry-forward items path;
- one primary next command/action when supported.

If `_hirmos/session/SESSION_STATE.json` claims an active session after close while the archive or close controls claim success, status must report an integrity conflict instead of trusting either surface silently.

## Claim reconciliation behavior

When this command surfaces a material readiness, progress, implementation, validation, runtime, integration, production-readiness, packaging, update-state, or close claim, it must apply `_hirmos/core/protocol/CLAIM_RECONCILIATION.md`.

Unsupported, unlogged, contradicted, or environment-blocked claims must be downgraded, routed back, or blocked before being shown as complete.

## Accepted current-state status

When reporting accepted current truth, `hirmos status` must read `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` first.

Status output must distinguish:

- current accepted truth from archived historical evidence;
- accepted MVP / delivery completion from production readiness;
- production readiness planning from production provider readiness and go-live approval;
- carry-forward items from accepted current truth.

If `CURRENT_SYSTEM_STATE.md` is missing, stale, or contradicted by current-state latest-close metadata / archive manifest, report `Status Blocked By Missing/Contradictory State`.

## Status invariant and canonical-value reporting

When status reports accepted current truth, it must report an integrity conflict if accepted-state invariant blocks are missing or if current-state posture/evidence fields contain noncanonical values.

Status must not silently normalize conflicting accepted-state files. It may recommend the specific repair owner: claim reconciliation, runtime integration readiness, accepted-state merge, role-workflow smoke checks, or package cleanup.


## Command-state reporting

`hirmos status` must report command legality from `SESSION_STATE.json` and must identify the exactly one recommended next governed command. It must report contradictions between `SESSION_STATE.json`, `SESSION_EXECUTION.md`, active-session artifacts, and post-close scaffold state without advancing lifecycle work.

## Durable Delivery Pointer Reporting

`hirmos status` must report active delivery information from `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` before consulting session-local artifacts.

Required status fields when applicable:

- Active delivery ID
- Delivery roadmap path
- Active delivery scope path
- Active phase path
- Active phase status
- Last accepted delivery
- Last accepted phase/session
- Next recommended delivery
- Next recommended delivery scope
- Next recommended phase
- Next governed command

If Current System State points to a missing or contradictory durable delivery artifact, status must report `Status Blocked By Delivery Pointer Conflict` and recommend repair through Update System State or delivery governance reconciliation.


When no active session exists but `CURRENT_SYSTEM_STATE.md` names a `Next recommended delivery`, status must report that delivery as the likely next `hirmos start` context unless carry-forward or blockers say otherwise.

## Durable Phase Adoption Status Reporting

When delivery governance is active, `hirmos status` must report:

- the Delivery Plan path;
- the single adopted active Phase path, if a session is active;
- whether Session Scope phase adoption is complete, partial, blocked, or not applicable;
- whether Current System State pointers agree with the adopted phase;
- whether the next governed command is blocked by phase-adoption defects.

Status must not imply implementation authorization when no durable phase has been adopted.


## Delivery Status Concordance Reporting

When Current System State reports active delivery pointers, `hirmos status` must report whether the durable Delivery Plan roadmap/register, active Delivery Scope, active Phase file, and Current System State pointers appear concordant.

Required status output fields when delivery governance is active:

- active delivery ID;
- Delivery roadmap path and status;
- Active delivery scope path and status;
- active phase path and status;
- last accepted phase;
- next recommended phase;
- next governed command;
- delivery status concordance: PASS | BLOCKED | NOT_ASSESSED.

If the Delivery Plan or Phase file is missing, stale, or contradictory to Current System State pointers, report `Status Blocked By Delivery Status Conflict` and recommend exactly one safe next command/action.

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

`hirmos status` must report whether the active phase can be accepted, what acceptance evidence is missing, and whether greenfield, brownfield, or mixed acceptance controls remain incomplete.


## CLI / Status UX Phase Lifecycle Reporting

`hirmos status` must provide a dedicated Phase Lifecycle Status Report when delivery governance is active or durable delivery pointers exist.

Required operator-visible fields:

- Active delivery ID
- Delivery Plan path
- Active Phase path
- Phase lifecycle status
- Phase type
- Phase Entry Gate status
- Phase adoption status
- Phase Progress Ledger status
- Carry-Forward Items status
- Phase Acceptance Evidence Gate status
- Missing evidence / blocked controls
- Current System State pointer concordance
- Exactly one recommended next command

Greenfield status group:

- MVP boundary status
- Architecture dependency status
- Prototype-vs-production expectation
- Scope expansion risk

Brownfield status group:

- Preservation baseline status
- Affected existing surfaces status
- Regression-sensitive behavior status
- Do-not-touch boundary status
- Migration/data safety status

Mixed phase status group:

- Greenfield status group reviewed
- Brownfield status group reviewed
- Mixed-mode simplified interpretation blocked

If the durable phase state is missing, contradictory, or unsupported for the current command state, status must report `Status Blocked By Phase Lifecycle Conflict` and recommend exactly one safe governed command.

## PROD-L4 delivery-route status reporting

`hirmos status` must make delivery routing visible without expanding the artifact surface.

When a session is active, status must report:

- selected Delivery Shape Decision;
- active capability route;
- whether `delivery-design`, `phase-contracting`, `session-scope`, and `implementation-readiness` are `REQUIRED`, `NOT_APPLICABLE`, `BLOCKED`, or satisfied;
- required authority artifacts and whether each exists, is non-placeholder, and is concordant;
- exactly one safe next governed command.

If the route is blocked by missing or contradictory delivery roadmap, delivery scope, phase, session scope, or Current System State pointers, status must report `Status Blocked By Delivery Route Conflict` and recommend reconciliation rather than implementation.


## PROD-L6 accepted-state status concordance

When no active session exists, `hirmos status` must report the latest close using accepted-state metadata first, then the history-only `ARCHIVE_MANIFEST.md` for concordance. It must distinguish accepted current truth from archived evidence.

For delivery-governed state, status must report:

- Delivery roadmap path;
- Active delivery scope path;
- Active phase path, if applicable;
- latest archive manifest path;
- whether accepted-state pointers and archive manifest concordance pass.

If accepted state still points to `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` as active delivery authority, report `Status Blocked By Delivery Pointer Conflict`.
