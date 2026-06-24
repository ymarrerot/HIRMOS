# Session Execution

Status: active-session execution ledger.
Purpose: provide the compact continuation handoff and append-only command/control ledger for the current HIRMOS session.

`SESSION_EXECUTION.md` records what happened, which boundary controls were checked, what changed during commands/continuation passes, and which governed command is safe next. It must not own scope, requirements, design decisions, evidence details, unresolved-item details, accepted-state truth, or archive transaction details.

Authoritative references:

- Machine state: `_hirmos/session/SESSION_STATE.json`
- Session scope authority: `_hirmos/session/SESSION_SCOPE.md`
- Unresolved-item details: `_hirmos/session/unresolved-items.md`
- Evidence details: `_hirmos/session/EVIDENCE.md` and implementation-unit records when present
- Delivery authority when active: `_hirmos/system/delivery/DELIVERY_PLAN.md`, `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`, and `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- Accepted state: `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`, `CARRY_FORWARD.md`, and `DECISION_LOG.md`
- Archive transaction: `_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md`

## Current Continuation Snapshot

This is the required human-readable resume surface. Keep it near the top and update it before surfacing readiness, completion, blocked, status, or close claims.

| Field | Current value | Backing authority / evidence |
|---|---|---|
| Last updated | | |
| Session ID | | `SESSION_STATE.json` |
| Current lifecycle stage | | `SESSION_STATE.json` |
| Session focus | | `SESSION_STATE.json.session_focus` |
| Active authority | | `SESSION_STATE.json.active_authority` |
| Current terminal state | | `SESSION_STATE.json` / Terminal State |
| Current status | | `SESSION_STATE.json` |
| Active scope | | `SESSION_SCOPE.md` when session scope exists; `DELIVERY_SCOPE.md` during delivery_baseline focus |
| Active delivery / phase / unit | | delivery artifacts / `SESSION_SCOPE.md` / implementation units |
| Authoritative artifacts reviewed | | Boundary Control Checklist / Artifact Reference Log |
| Completed since session start | | Command Timeline / Evidence Handoff |
| In progress | | Continuation Pass Register / implementation units |
| Blocked | | Fail-Closed Conditions / `unresolved-items.md` |
| Gated unresolved items | | `unresolved-items.md` pointer only |
| Non-gating unresolved items | | `unresolved-items.md` pointer only |
| Technical-review items | | `unresolved-items.md` pointer only |
| Evidence status | | `EVIDENCE.md` pointer only |
| Next safe governed command | | `SESSION_STATE.json.recommended_next_command` |
| What the next model must not do | | Boundary Control Checklist / Terminal State |
| Resume instructions | | This snapshot + backing artifacts |

Fail-closed rule: if this snapshot is missing, placeholder-only, or contradicts `SESSION_STATE.json`, `SESSION_SCOPE.md`, `unresolved-items.md`, or the append-only ledger, HIRMOS must reconcile it or stop at `Blocked / Fail-Closed` before surfacing continuation, readiness, completion, or close claims.

## Command Resolution

| Field | Value |
|---|---|
| Session ID | |
| Active command | |
| User request | |
| Interaction mode | |
| Active lifecycle stage before command | |
| Active lifecycle stage after command | |
| Continuation state | |
| Recommended next governed command | |

## Machine Command State Concordance

`SESSION_STATE.json` is the machine command-state authority. This section is an explanatory mirror only. If this section disagrees with `SESSION_STATE.json`, HIRMOS must fail closed.

| Field | SESSION_STATE.json value | SESSION_EXECUTION.md value | Concordance | Notes |
|---|---|---|---|---|
| status | | | NOT_CHECKED | |
| lifecycle_stage | | | NOT_CHECKED | |
| allowed_next_commands | | | NOT_CHECKED | |
| recommended_next_command | | | NOT_CHECKED | |
| continuation_pass | | | NOT_CHECKED | |
| pending_correction | | | NOT_CHECKED | |

Allowed concordance values: `MATCH`, `MISMATCH`, `NOT_CHECKED`. A `MISMATCH` blocks readiness, implementation-completion, and close claims.

## Append-Only Ledger Covenant

`SESSION_EXECUTION.md` is append-only for command history, continuation passes, route-backs, control-state changes, and boundary records. Earlier pass records must not be replaced when a later command corrects, extends, validates, or routes back the session.

Permitted edits to earlier sections are limited to:

- updating the Current Continuation Snapshot;
- filling previously blank command/control fields;
- correcting clerical errors with a dated correction note;
- changing a control status only when the change is also logged in Control Mutation Ledger.

Forbidden edits:

- deleting prior continuation pass rows;
- replacing prior evidence pointers with newer evidence pointers without a correction note;
- silently rewriting terminal state, next command, scope effect, or pass result;
- removing unresolved-item dispositions or unit-review outcomes;
- collapsing multiple continue passes into one summary.

Fail-closed rule: if HIRMOS cannot preserve prior ledger history while applying a correction or amendment, it must stop at `Blocked / Fail-Closed` and recommend exactly one governed recovery command.

## Boundary Control Checklist

This checklist records whether owning artifacts were reviewed at each lifecycle boundary. It stores review status and pointers only; detailed scope/evidence/unresolved/archive content stays in the owning artifact.

| Control | Owning artifact | Required before | Status | Evidence / pointer |
|---|---|---|---|---|
| Bootstrap control | `bootstrap/BOOTSTRAP_REPORT.md` | command resolution | PENDING | |
| Command control | command spec / `COMMAND_STATE_MACHINE.md` | every command | PENDING | |
| Working-copy control | project root / `_hirmos/` | meaningful mutation | PENDING | |
| Current-system-state-first control | `CURRENT_SYSTEM_STATE.md` | design / implementation | PENDING | |
| Session scope control | `SESSION_SCOPE.md` | session_baseline / implementation readiness / close | PENDING / NOT_APPLICABLE during delivery_baseline | |
| Unresolved-items control | `unresolved-items.md` | every boundary | PENDING | |
| Delivery baseline control | `DELIVERY_PLAN.md` / `DELIVERY_SCOPE.md` / delivery `unresolved-items.md` | delivery_baseline checkpoint | NOT_APPLICABLE | |
| Delivery/phase control | `DELIVERY_PLAN.md` / `DELIVERY_SCOPE.md` / `PHASE-xx.md` when instantiated | delivery-governed readiness / close | NOT_APPLICABLE | |
| Implementation-unit coverage control | `implementation-units/` | implementation-unit sessions | NOT_APPLICABLE | |
| Implementation authorization control | `SESSION_SCOPE.md` | implementation start | PENDING | |
| Validation/evidence control | `EVIDENCE.md` / unit reviews / command output | completion / close | PENDING | |
| Continuation snapshot control | Current Continuation Snapshot | user-facing checkpoints | PENDING | |
| Close/archive/reset control | `ARCHIVE_MANIFEST.md` / accepted-state files | close | NOT_APPLICABLE | |

Allowed statuses: `PENDING`, `SATISFIED`, `UNSATISFIED`, `BLOCKED`, `NOT_APPLICABLE`.

## Active Execution Controls

Execution controls apply clear-specification discipline to the command spine: required controls must be explicit, locally self-validated, and fail closed when missing or contradictory.

| Boundary | Required controls | Control status | Notes / evidence path |
|---|---|---|---|
| command resolution | bootstrap, command, machine-state concordance | PENDING | |
| implementation readiness | current-state, session scope, unresolved, delivery/phase if active, implementation authorization | PENDING | |
| implementation completion | scope review, evidence pointer, unresolved review, unit review if active | PENDING | |
| close readiness | scope close verification, evidence pointer, unresolved review, accepted-state plan | PENDING | |
| close success | archive manifest, accepted-state update, active-session reset | PENDING | |

## Baseline Control Families

| Family | Controls included | Current status |
|---|---|---|
| Command and lifecycle | bootstrap, command, working copy, lifecycle stage | PENDING |
| Scope and unresolved items | session scope, unresolved items, implementation authorization | PENDING |
| Delivery/phase routing | delivery roadmap, delivery scope, active phase when selected | NOT_APPLICABLE |
| Implementation and evidence | implementation units, evidence pointers, validation status | PENDING |
| Close and archive | accepted-state update, archive manifest, active reset | NOT_APPLICABLE |

## Control Mutation Ledger

Every material control-state change must be appended here. Do not overwrite earlier control outcomes without recording why the control changed.

| Seq | Control | Previous status | New status | Triggering command/pass | Reason | Evidence pointer |
|---:|---|---|---|---|---|---|

## Readiness Gates

| Gate | Required before | Status | Evidence pointer |
|---|---|---|---|
| Session Scope review | implementation readiness / close | PENDING | `SESSION_SCOPE.md` |
| Unresolved Items Reconciliation | every lifecycle boundary | PENDING | `unresolved-items.md` |
| Implementation Unit Coverage | implementation start / close | NOT_APPLICABLE | `implementation-units/` |
| Validation Evidence | completion / close | PENDING | `EVIDENCE.md` / unit reviews |

## Control Self-Validation

Before each lifecycle boundary claim, answer:

| Question | Answer | Evidence pointer | Gaps |
|---|---|---|---|
| Are all required controls for this boundary satisfied? | NOT_CHECKED | | |
| Is any gated unresolved item blocking the boundary? | NOT_CHECKED | | |
| Does the user-facing claim match artifact evidence? | NOT_CHECKED | | |
| Is the next command governed and legal? | NOT_CHECKED | | |

## Ledger Integrity Self-Validation

Before surfacing any implementation-complete, close-ready, blocked, or close-success claim, answer:

| Question | Answer | Evidence pointer | Gaps / action |
|---|---|---|---|
| Were all previous continuation pass records preserved? | NOT_CHECKED | | |
| Was the current pass appended instead of replacing an earlier pass? | NOT_CHECKED | | |
| Were control changes recorded in the Control Mutation Ledger? | NOT_CHECKED | | |
| Were unresolved-item dispositions referenced rather than duplicated? | NOT_CHECKED | | |
| Were implementation-unit attempts/reviews preserved in their owning files? | NOT_CHECKED | | |
| Does `SESSION_STATE.json.continuation_pass` match the latest continuation pass number? | NOT_CHECKED | | |

Allowed answers: `YES`, `NO`, `NOT_APPLICABLE`, `NOT_CHECKED`. A `NO` answer blocks implementation-completion and close claims until reconciled.

## Fail-Closed Conditions

HIRMOS must fail closed and must not claim readiness, implementation completion, or close when any of these conditions is true:

- `SESSION_STATE.json` and `SESSION_EXECUTION.md` disagree on active status, lifecycle stage, continuation pass, or next governed command.
- `SESSION_SCOPE.md` is missing, placeholder-only, stale, or not reviewed when implementation or close is claimed.
- `_hirmos/session/unresolved-items.md` is missing or has gated items blocking the boundary.
- Evidence is claimed without a pointer to `EVIDENCE.md`, unit review, command output, inspection note, or explicit not-run rationale.
- Delivery-governed work lacks the required `DELIVERY_PLAN.md`, `DELIVERY_SCOPE.md`, active `PHASE-xx.md`, or accepted-state pointer concordance.
- User-facing continuation/readiness output references artifacts that do not exist, are placeholders, or contradict this ledger.
- Implementation units are individually complete but the combined units do not cover `SESSION_SCOPE.md`.
- Close is claimed without archive manifest, accepted-state update/verification, and active-session reset evidence.
- Any prior continuation pass row is missing, collapsed, or overwritten without a correction note.

## Command Timeline

| Seq | Command / action | Lifecycle stage before | Lifecycle stage after | Result | Evidence pointer |
|---:|---|---|---|---|---|

## Continuation Boundary Log

Record each surfaced decision, readiness, completion, blocked, status, or close boundary that changes continuation state.

| Boundary ID | Boundary | Snapshot updated? | User-facing claim | Backing controls | Result |
|---|---|---|---|---|---|

## Continuation Pass Register

Every `hirmos continue` invocation must append one row and, when material, one detail block. Do not overwrite prior passes.

| Pass | Command | Pass type | Scope effect | Artifacts updated | Evidence pointer | Result | Next governed command |
|---:|---|---|---|---|---|---|---|

Allowed pass types: `INITIAL_IMPLEMENTATION`, `CORRECTIVE`, `SCOPE_AMENDMENT`, `VALIDATION_ONLY`, `ROUTE_BACK`.

Continuation pass append requirements:

- assign the next integer pass number from `SESSION_STATE.json.continuation_pass + 1`;
- record the user command or correction/amendment request;
- classify pass type and scope effect;
- identify affected `SESSION_SCOPE.md` sections and implementation units by pointer;
- record artifacts changed and evidence pointers produced;
- record whether prior pass records were preserved;
- update `SESSION_STATE.json.continuation_pass` to match the latest appended pass;
- surface exactly one legal next governed command.

### Continuation pass detail blocks

Use one block per pass when the row is not enough.

```text
### Continue Pass <n> — <type>
- User command:
- Reason:
- Scope effect: same-scope correction | scope amendment | validation only | route-back
- SESSION_SCOPE.md impact:
- Implementation units affected:
- Unresolved items pointer:
- Files/artifacts changed:
- Evidence pointer:
- Result:
- Next governed command:
```

## Route-Back Records

Alias for corrections and earlier-stage route-backs.

## Route-Back / Correction Ledger

Record when a later stage discovers a problem owned by an earlier stage.

| Seq | Discovered at stage | Problem | Owning stage/artifact | Downstream controls reset | Result |
|---:|---|---|---|---|---|

## Artifact Instantiation Log

Every created artifact must be recorded here by pointer.

## Artifact Reference and Instantiation Log

Record created, read, or updated artifacts without duplicating their content.

| Artifact | Role | Required? | Action | Non-placeholder / review status |
|---|---|---:|---|---|
| `_hirmos/session/SESSION_STATE.json` | machine command state | yes | | |
| `_hirmos/session/SESSION_SCOPE.md` | session scope authority | yes | | |
| `_hirmos/session/unresolved-items.md` | unresolved-item register | yes | | |
| `_hirmos/session/implementation-units/` | implementation unit records | conditional | | |
| `_hirmos/session/bootstrap/` | startup/bootstrap evidence | yes | | |
| `_hirmos/session/EVIDENCE.md` | detailed evidence surface | conditional | | |
| `_hirmos/session/stack-resolution.json` | machine-readable stack routing | conditional | | |
| `_hirmos/system/delivery/DELIVERY_PLAN.md` | delivery roadmap/register | conditional | | |
| `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | delivery authority | conditional | | |
| `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | phase authority | conditional | | |
| `_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md` | archive transaction | close | | |

## Unresolved Register Direct Review Log

This log proves direct review of `_hirmos/session/unresolved-items.md`. `SESSION_SCOPE.md` unresolved summary is not sufficient. It records counts/status only; item details stay in `unresolved-items.md`.

| Boundary | Register reviewed directly? | Blocking status | Gated count | Non-gating count | Technical-review count | Evidence pointer |
|---|---|---|---:|---:|---:|---|
| Bootstrap / command resolution | NO | NOT_REVIEWED | | | | |
| Implementation readiness | NO | NOT_REVIEWED | | | | |
| Implementation completion | NO | NOT_REVIEWED | | | | |
| Close readiness | NO | NOT_REVIEWED | | | | |

## Capability / Stage Activity Summary

Record capability routing outcomes as pointers, not full capability outputs.

| Capability / stage | Entrypoint | Activity summary | Produced artifacts | Unresolved-item producer outcome |
|---|---|---|---|---|

## System-State Capability Summary

| System-state capability | Evidence reviewed | Summary | Handoff / route-back |
|---|---|---|---|

## Design Capability Summary

| Design capability | Authority consumed | Output / decision pointer | Handoff |
|---|---|---|---|

## Implementation Capability Summary

| Implementation capability | Unit / artifact | Output / evidence pointer | Review result |
|---|---|---|---|

## Governed Continuation Summary

| Boundary / output | Governed basis | User-facing output | Next command |
|---|---|---|---|

- Current Continuation Snapshot status:
- Unresolved item status:

## Project Context / Stack Summary

| Project type | Active stack | Stack contexts active | Evidence pointer |
|---|---|---|---|

## Runtime Integration / Production Readiness Summary

Pointer-only summary. Detailed engineering gate decisions belong in `SESSION_SCOPE.md`; validation results belong in `EVIDENCE.md` or implementation-unit reviews.

| Area | Authorized posture pointer | Evidence pointer | Limitation pointer |
|---|---|---|---|

## Vertical Slice / Delivery Status Summary

| Slice / unit | Status | User-facing outcome | Next action |
|---|---|---|---|

## Command Output Summary

- User-facing summary:
- Exactly one primary next command/action:
- Next recommended delivery:
- Next recommended delivery scope:
- Next recommended phase:

## Delivery Shape Decision Gate Execution

Pointer-only execution record for the delivery-shape decision in `SESSION_SCOPE.md`.

- SESSION_SCOPE.md delivery-shape section reviewed:
- Selected route:
- Gate status: PASS | BLOCKED | NOT_ASSESSED
- Evidence pointer:

## Focus-Aware Capability Routing Log

Required when the selected delivery shape is `MULTI_SESSION_DELIVERY` or `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

| Capability | Expected durable/session output | Status | Evidence path | Notes |
|---|---|---|---|---|
| delivery-baseline | `_hirmos/system/delivery/DELIVERY_PLAN.md` and `<delivery-id>/DELIVERY_SCOPE.md` | PENDING | | |
| phase-baseline | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` when phase files are selected | PENDING | | |
| session-scope | `_hirmos/session/SESSION_SCOPE.md` adopts and narrows active delivery/phase authority | PENDING | | |
| implementation-readiness | `SESSION_SCOPE.md` authorizes implementation and required controls are satisfied | PENDING | | |

Fail closed if this log is missing, incomplete, or contradicted by artifacts while the selected delivery shape requires durable delivery artifacts.

## Current System State Delivery Pointer Concordance

Record this before implementation readiness and again before close when delivery governance is active or potentially applicable.

| Check | Result | Evidence | Notes |
|---|---|---|---|
| Current System State delivery pointers read | SATISFIED / BLOCKED / NOT_APPLICABLE | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | |
| Delivery roadmap pointer exists when required | SATISFIED / BLOCKED / NOT_APPLICABLE | `_hirmos/system/delivery/DELIVERY_PLAN.md` | |
| Delivery scope pointer exists when required | SATISFIED / BLOCKED / NOT_APPLICABLE | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | |
| Active Phase pointer exists when required | SATISFIED / BLOCKED / NOT_APPLICABLE | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | |
| Session Scope adopts the same delivery/phase authority | SATISFIED / BLOCKED / NOT_APPLICABLE | `SESSION_SCOPE.md` | |
| Next phase / next command concordance checked | SATISFIED / BLOCKED / NOT_APPLICABLE | `DELIVERY_PLAN.md`, `SESSION_STATE.json` | |

Fail-closed rule: delivery-governed implementation must not proceed while Current System State delivery pointers contradict the durable Delivery Plan roadmap, Delivery Scope, active Phase file, or Session Scope.

## Durable Phase Adoption Gate

Pointer-only execution record required before implementation readiness when the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

| Check | Required result | Evidence artifact | Actual result |
|---|---|---|---|
| Exactly one durable phase adopted | SATISFIED | `SESSION_SCOPE.md` Active Durable Phase Adoption | PENDING |
| Adopted phase path exists | SATISFIED | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | PENDING |
| Delivery roadmap path exists | SATISFIED | `_hirmos/system/delivery/DELIVERY_PLAN.md` | PENDING |
| Delivery Scope path exists | SATISFIED | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | PENDING |
| Current System State pointer matches adopted phase | SATISFIED | `CURRENT_SYSTEM_STATE.md` Active Development Context and Delivery Pointers | PENDING |
| Phase items mapped to Session Scope items | SATISFIED | `SESSION_SCOPE.md` Adopted phase scope | PENDING |
| Partial adoption has explicit deferrals | SATISFIED / NOT_APPLICABLE | `SESSION_SCOPE.md` Phase exclusions / deferrals | PENDING |

## Phase Entry Gate Execution Log

- Phase file inspected:
- Delivery Plan inspected:
- Delivery Scope inspected:
- Current System State pointer inspected:
- Phase Entry Gate status:
- Implementation readiness authorized: YES / NO

## Phase Progress / Carry-Forward Record

| Check | Status | Evidence / pointer | Notes |
|---|---|---|---|
| Adopted phase progress reviewed | PENDING / PASS / BLOCKED | | |
| Carry-forward obligations recorded | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Current System State pointer outcome determined | PENDING / PASS / BLOCKED | | |

## Phase Acceptance Enforcement Record

This record is required before a delivery-governed close may mark the adopted durable phase `ACCEPTED`. Detailed acceptance evidence belongs in the phase file, `SESSION_SCOPE.md` close verification, implementation-unit reviews, and `EVIDENCE.md`.

| Acceptance control | Status | Evidence pointer | Notes |
|---|---|---|---|
| Phase Acceptance Evidence Gate inspected | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| All adopted Session Scope items reviewed | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Implementation Unit evidence complete | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Delivery Plan / Phase / Current System State updates prepared | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |

## Phase Lifecycle Status Report Record

Record status information that `hirmos status` must be able to surface without mutation.

| Status field | Value / evidence pointer | Status | Notes |
|---|---|---|---|
| Active delivery ID | | RECORDED / MISSING / NOT_APPLICABLE | |
| Delivery Plan path | | RECORDED / MISSING / NOT_APPLICABLE | |
| Active Phase path | | RECORDED / MISSING / NOT_APPLICABLE | |
| Phase lifecycle status | | RECORDED / MISSING / CONFLICT | |
| Phase type | | RECORDED / UNKNOWN / CONFLICT | |
| Phase Entry Gate status | | PASS / BLOCKED / UNCERTAIN / NOT_APPLICABLE | |
| Phase adoption status | | ADOPTED / BLOCKED / NOT_APPLICABLE | |
| Phase Acceptance Evidence Gate status | | COMPLETE / INCOMPLETE / BLOCKED / NOT_APPLICABLE | |
| Exactly one recommended next command | | RECORDED / MISSING / CONFLICT | |

## Evidence Log

Pointer-only evidence log; detailed evidence belongs in `EVIDENCE.md` and implementation-unit reviews.

## Evidence Handoff

Pointers only. Evidence details belong in `EVIDENCE.md`, implementation-unit reviews, command output logs, screenshots/logs, or explicit not-run rationale.

| Seq | Evidence pointer | Evidence type | Result | Supports claim |
|---:|---|---|---|---|


## Close-Time Delivery Status Execution Log

Pointer-only delivery close transaction record. Detailed status updates belong in `DELIVERY_PLAN.md`, `DELIVERY_SCOPE.md`, `PHASE-xx.md`, accepted-state files, and `ARCHIVE_MANIFEST.md`.

| Action | Target artifact | Result | Evidence pointer |
|---|---|---|---|
| Delivery status transaction prepared | `SESSION_EXECUTION.md` close/update controls | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Adopted phase status update prepared | `PHASE-xx.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Parent Delivery Plan roadmap update and Delivery Scope status update prepared | `DELIVERY_PLAN.md` / `DELIVERY_SCOPE.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Current System State delivery pointers prepared | `CURRENT_SYSTEM_STATE.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |

Fail-closed rule: do not mark the close transaction complete if durable delivery status updates remain pending, blocked, stale, or contradictory.

## Close / Archive / Reset Invariant Controls

Pointer-only close controls. Detailed archive transaction belongs in `ARCHIVE_MANIFEST.md`; promised-vs-verified review belongs in `SESSION_SCOPE.md`; durable accepted truth belongs in accepted-state files.

| Invariant | Required evidence | Status |
|---|---|---|
| Session Scope close verification completed | `SESSION_SCOPE.md` close verification final verdict supports close | PENDING |
| Unresolved register reconciled | `unresolved-items.md` directly reviewed; no blocking gated item remains | PENDING |
| Accepted state updated or verified unchanged | `CURRENT_SYSTEM_STATE.md`, `CARRY_FORWARD.md`, `DECISION_LOG.md` | PENDING |
| Archive manifest created | `ARCHIVE_MANIFEST.md` exists and matches archived artifacts | PENDING |
| Archived session state normalized | archived `SESSION_STATE.json` is closed / archived / history_only | PENDING |
| Active session reset | active `_hirmos/session/` reset to idle scaffolding only | PENDING |
| Stale artifact scan clear | no runtime active-session artifacts remain after close reset | PENDING |

Fail-closed rule: if any invariant remains `PENDING`, `UNSATISFIED`, or `BLOCKED`, HIRMOS must not surface normal close success.

## Close / Archive / Accepted-State Integrity Summary

| Close control | Status | Evidence pointer |
|---|---|---|

- Post-close status consistency:

## Claim Reconciliation Summary

Pointer-only claim reconciliation. Material claim details belong in `EVIDENCE.md` or implementation-unit reviews.

| Claim | Evidence pointer | Supported? | Downgrade / route-back if needed |
|---|---|---|---|

- claim reconciliation control:

## Archive Session State Normalization

- archive-session-state-normalized:
- active-session-state-reset:

## Current-State Execution Controls

| Current-state control | Status | Evidence pointer |
|---|---|---|

## Invariant / Canonical Value Controls

| Invariant | Canonical value | Status | Evidence pointer |
|---|---|---|---|

## Conditional Requirements Controls

Use this only when a separate `REQUIREMENTS.md` authority exists. Otherwise record `NOT_APPLICABLE`.

| Requirements control | Status | Evidence pointer |
|---|---|---|
| requirements-authority-instantiated | NOT_APPLICABLE | |
| requirements-intake-classification-preserved | NOT_APPLICABLE | |
| requirements-flow-detail-sufficient | NOT_APPLICABLE | |

## Close-Time Compliance Controls

| Close-time control | Status | Evidence pointer |
|---|---|---|
| claim-reconciliation-materialized | PENDING | |

## Terminal State

- Terminal state:
- Supported user-facing summary:
- Exactly one primary next governed command:
- Why this command is legal:

## Exactly-one-next-command rule

Every surfaced command result must name exactly one primary governed next command. Prose such as `reply to proceed` is not a governed command.

## Append-Only Ledger Integrity Check

Before surfacing any continuation, readiness, completion, blocked, or close output, verify that the Current Continuation Snapshot is current and that all earlier continuation pass rows and detail blocks remain present. New passes must be appended; earlier passes must not be replaced, summarized away, or deleted.

## Beyond Clear Specs Application

`SESSION_EXECUTION.md` applies the execution-control subset of `_hirmos/core/authority/BEYOND_CLEAR_SPECS.md` to the active command spine only.

Required controls applied here:

- clear execution controls for each lifecycle boundary;
- strict local self-validation before surfacing readiness, implementation-completion, close-readiness, blocked, or close-success claims;
- append-only command, continuation-pass, route-back, and control-mutation records;
- fail-closed behavior when the ledger, machine state, unresolved-item register, Session Scope close verification, evidence pointers, or archive manifest cannot support the claim.

HIRMOS must not claim a lifecycle boundary complete merely because intended work was described clearly. It may claim the boundary only when this execution ledger self-validates that required controls were satisfied and recorded.
