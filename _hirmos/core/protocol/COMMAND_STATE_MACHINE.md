# Command State Machine

Status: core protocol.
Purpose: define the machine-readable command state, legal command transitions, mandatory start pause, cumulative continue behavior, and fail-closed command discipline for HIRMOS.

This protocol is the authoritative command-legality model. Command files describe command-specific work; this file defines whether a command may legally run at the current session state.

## Canonical lifecycle stages

`SESSION_STATE.json.lifecycle_stage` must use one of these canonical values:

```text
idle
bootstrap
system_state_understanding
session_scope
design
implementation_readiness
implementation
implementation_complete
correction_requested
close_ready
closed
blocked
```

Notes:

- `idle` means no active governed session is running.
- `implementation_readiness` is the mandatory pause boundary after `hirmos start` for implementation-capable sessions.
- `implementation_complete` may still accept a correction-specific `hirmos continue "..."` before close.
- `closed` is an archive/session-history state, not the active session state after close. The active session returns to `idle`.
- `blocked` requires a `blocking_reason` and exactly one governed recovery command.

## SESSION_STATE.json schema

`_hirmos/session/SESSION_STATE.json` is the machine command-state authority.

Required fields:

```json
{
  "schema_version": "session-state-v1",
  "status": "idle | active | blocked",
  "session_id": "",
  "lifecycle_stage": "idle",
  "continuation_pass": 0,
  "pending_correction": false,
  "allowed_next_commands": ["hirmos start"],
  "recommended_next_command": "hirmos start",
  "blocking_reason": null,
  "created_at": null,
  "updated_at": null
}
```

Rules:

- `status`, `session_id`, `lifecycle_stage`, `continuation_pass`, `pending_correction`, `allowed_next_commands`, `recommended_next_command`, `blocking_reason`, and timestamps are the full machine-state surface. Narrative continuation belongs in `SESSION_EXECUTION.md` Current Continuation Snapshot.
- `SESSION_EXECUTION.md` may explain state but must not override `SESSION_STATE.json`.
- If `SESSION_STATE.json` and `SESSION_EXECUTION.md` disagree, HIRMOS must fail closed.
- `allowed_next_commands` must contain only supported governed commands.
- `recommended_next_command` must be exactly one command and must be legal for the current state.

## Supported governed commands

```text
hirmos start
hirmos continue
hirmos status
hirmos close
```

Prose such as `reply to proceed`, `tell me when ready`, `we can continue`, or `should I proceed?` is not a governed command and must not be recommended as the primary next action.

## Command transition matrix

| Current status | Lifecycle stage | Legal next commands | Required primary recommendation |
|---|---|---|---|
| idle | idle | `hirmos start`, `hirmos status` | `hirmos start` unless the user asked for status |
| active | bootstrap | `hirmos continue`, `hirmos status` | `hirmos continue` |
| active | system_state_understanding | `hirmos continue`, `hirmos status` | `hirmos continue` unless blocked |
| active | session_scope | `hirmos continue`, `hirmos status` | `hirmos continue` unless blocked |
| active | design | `hirmos continue`, `hirmos status` | `hirmos continue` unless blocked |
| active | implementation_readiness | `hirmos continue`, `hirmos status` | `hirmos continue` |
| active | implementation | `hirmos continue`, `hirmos status` | `hirmos continue` unless complete or blocked |
| active | implementation_complete | `hirmos close`, `hirmos status`, correction-specific `hirmos continue "..."` | `hirmos close` unless user supplies a correction before close |
| active | correction_requested | `hirmos continue`, `hirmos status` | `hirmos continue` |
| active | close_ready | `hirmos close`, `hirmos status` | `hirmos close` |
| blocked | blocked | `hirmos status` and one explicit recovery command | explicit recovery command |

Illegal transitions fail closed. In particular:

- `hirmos start` is illegal when an active session exists.
- `hirmos continue` is illegal when session status is `idle`.
- bare `hirmos continue` is illegal after `implementation_complete` unless `pending_correction` is true or `SESSION_EXECUTION.md` Current Continuation Snapshot explicitly recommended `hirmos continue`.
- `hirmos close` is illegal before a design-only, implementation-complete, or close-ready terminal boundary is reached.

## Mandatory start pause rule

`hirmos start` must not go directly into implementation.

For implementation-capable sessions, `hirmos start` must stop at `implementation_readiness` after creating or updating:

- `_hirmos/session/SESSION_STATE.json`
- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/SESSION_EXECUTION.md`
- `_hirmos/session/unresolved-items.md`
- `_hirmos/session/SESSION_SCOPE.md` close verification initialized for later review
- implementation unit plan in `SESSION_SCOPE.md` when implementation is expected

The user-facing result must explain:

- what HIRMOS understood;
- what HIRMOS will do;
- what HIRMOS will not do;
- affected artifacts/areas;
- planned implementation units, when applicable;
- gated unresolved items;
- non-gating assumptions;
- required validation;
- exactly one next governed command: `hirmos continue`.

Design-only or analysis-only sessions may complete the requested design/analysis during `hirmos start`, but must still stop before implementation.

## Cumulative continue pass model

`hirmos continue` is append-only.

Every `hirmos continue` must create a new continuation pass record in `SESSION_EXECUTION.md`. It must not overwrite previous pass history, evidence, unresolved-item dispositions, or unit reviews.

Continuation pass types:

| Type | Meaning | Required behavior |
|---|---|---|
| Initial implementation pass | first implementation continuation after start/readiness | execute authorized implementation units |
| Corrective pass | user identifies a bug, gap, or issue inside current session scope before close | append correction pass, update affected IU/review/evidence |
| Scope amendment pass | user requests new work outside the existing Session Scope | amend `SESSION_SCOPE.md` before implementation |
| Validation-only pass | user asks to rerun or complete validation | append validation evidence and update review surfaces |
| Route-back pass | later evidence invalidates earlier authority | record route-back and reset affected controls |

Scope rules:

- Same-scope corrections do not rewrite the Authorized Scope; they append correction records.
- Scope expansions require a `Scope Amendment` section in `SESSION_SCOPE.md` before implementation.
- `unresolved-items.md` dispositions must be appended, not deleted.
- `SESSION_SCOPE.md` close verification must add review passes, not replace prior reviews.
- `implementation-units/IU-xx.md` must append attempts/retries/reviews.

## SESSION_EXECUTION append-only ledger requirements

`SESSION_EXECUTION.md` is the command ledger. It must be append-only for command history and continuation passes. The machine state in `SESSION_STATE.json` controls legality; the ledger records what happened and why.

Required ledger invariants:

- every advancing command appends to the command timeline;
- every `hirmos continue` appends a continuation pass record;
- control status changes are appended to a control mutation ledger;
- route-backs are recorded instead of silently rewriting earlier authority;
- corrections and scope amendments preserve earlier implementation/evidence records;
- prior pass records may be corrected only with an explicit correction note;
- `SESSION_STATE.json.continuation_pass` must match the latest continuation pass recorded in `SESSION_EXECUTION.md`;
- implementation-complete and close claims require ledger integrity self-validation.

If ledger integrity cannot be established, the command must fail closed.


## Beyond Clear Specs alignment for command execution

Command execution applies the execution-control subset of `_hirmos/core/authority/BEYOND_CLEAR_SPECS.md`. For command-state discipline, this means:

- command protocols provide clear executable specs;
- `SESSION_EXECUTION.md` provides strict local self-validation for lifecycle-boundary claims;
- command responses fail closed when machine state, ledger state, scope state, unresolved-item state, or evidence cannot support the requested transition;
- append-only continuation and control-mutation records protect against stale or overwritten session history.

This protocol does not require the full escalated Beyond Clear Specs pattern for every command or capability. It applies the minimum execution-control subset needed to keep command transitions honest, reviewable, and fail-closed.

## Exactly-one-next-command rule

Every command response must surface exactly one primary governed next command.

Allowed pattern:

```text
Next governed command: hirmos continue
```

If alternatives exist, they may be mentioned only after the primary command is clear.

Forbidden primary recommendations:

```text
reply to proceed
tell me when ready
continue if you want
hirmos continue or hirmos close
```

## Fail-closed command behavior

When a command cannot proceed, HIRMOS must:

1. state that the command is blocked;
2. identify the failed precondition;
3. identify the authoritative artifact or protocol that caused the block;
4. avoid changing files unless the command is a governed repair/status action;
5. recommend exactly one governed recovery command.

## Validator obligations

Validators must eventually enforce:

- `SESSION_STATE.json` schema validity;
- legal command transition matrix;
- recommended command legality;
- mandatory start pause;
- cumulative continue pass append-only markers;
- append-only ledger integrity phrases in `SESSION_EXECUTION.md`;
- concordance between `SESSION_STATE.json.continuation_pass` and latest ledger pass when active;
- active/idle session folder consistency;
- canonical artifact names;
- no deprecated command-state diagnostics.


## Delivery Shape Decision state gate

Before an implementation-capable session may enter `implementation_readiness`, HIRMOS must apply `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md`.

Required state effect:

- `SINGLE_SESSION_VERTICAL_SLICE` requires bounded-scope safety evidence;
- `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS` requires implementation-unit coverage for the Session Scope;
- `MULTI_SESSION_DELIVERY` requires a durable Delivery Plan before implementation readiness;
- `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES` requires a durable Delivery Plan and adopted phase file before implementation readiness;
- `UNCERTAIN` keeps the session blocked or in Design/system-state understanding;
- missing delivery-shape decision is a fail-closed condition.

The exactly-one-next-command rule must not recommend `hirmos continue` for implementation when the Delivery Shape Decision is missing, `UNCERTAIN`, or references missing durable delivery artifacts.

## Production-Shaped Engineering state gate

Before an implementation-capable session may enter `implementation_readiness`, HIRMOS must record the Production-Shaped Engineering Gate in `DESIGN.md`, `SESSION_SCOPE.md`, and `SESSION_EXECUTION.md`.

Before a session may enter `close_ready` or `closed`, HIRMOS must verify that implementation evidence supports the exact production-shaped claims being accepted. If evidence contradicts a claim, the claim must be downgraded, routed back, or preserved as a limitation/carry-forward item.

## Append-only continuation ledger integrity

`hirmos continue` is append-only. Before adding a continuation pass, the runner must preserve all earlier continuation register rows and all earlier pass detail blocks in `_hirmos/session/SESSION_EXECUTION.md`.

A continuation pass must not replace, summarize away, reorder, or delete earlier pass records. If a correction must amend an earlier claim, the correction is recorded in a new pass and may reference the earlier pass; the earlier pass remains visible.

Before surfacing a continuation checkpoint, the runner must verify that the expected previous pass count and detail blocks still exist. If an earlier pass was accidentally removed or changed, the runner must restore the ledger or fail closed before claiming progress.

## PROD-L8.19 Idle Continue Fail-Closed Rule

When `SESSION_STATE.json.status = idle`, `hirmos continue` is not a recovery shortcut and must not mutate project files, HIRMOS session artifacts; it must not modify project files, delivery artifacts, accepted-state artifacts, or archive artifacts except to report the illegal command if status reporting is explicitly requested.

Required behavior:

- fail closed with exactly one governed recovery command, normally `hirmos start`;
- if the user request is a correction/fix/analyze/report request, route it to a new governed `hirmos start` correction/session-intake flow before any project-file edits;
- do not perform a direct runtime fix while idle;
- do not create a retrospective correction session after code changes have already been made;
- do not treat chat transcript context as active session authority.

This rule reuses the existing command-state gate and does not create a new command or artifact surface.


## PROD-L8.20 Governance Posture Interpretation

Command legality is a precondition for action, not a post-action reporting check. If a command is illegal for the current state, the model must not perform useful edits and then describe them as a correction. It must stop before mutation, surface the invalid command state, and route to the existing governed command that can establish authority.

HIRMOS artifacts are active authority and live execution records. They are not compliance documents to be reconstructed after implementation.
