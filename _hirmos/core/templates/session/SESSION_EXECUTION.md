# Session Execution

Status: active-session orchestration artifact.
Purpose: provide the linear execution-control spine for the current HIRMOS session.

`SESSION_EXECUTION.md` records command flow, lifecycle boundary state, execution controls, self-validation, fail-closed conditions, evidence logs, route-backs, and the next governed command. It must not own scope, acceptance criteria, unresolved-item detail, or accepted current-system truth.

Authoritative references:

- Machine state: `_hirmos/session/SESSION_STATE.json`
- Session contract: `_hirmos/session/SESSION_CONTRACT.md`
- Unresolved items register: `_hirmos/session/unresolved-items.md`
- Session close verification: `_hirmos/session/SESSION_CONTRACT.md` section 11
- Current system state: `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`
- Implementation units: `_hirmos/session/implementation-units/`


## Current Continuation Snapshot

This section is the required human-readable continuation surface. It must stay near the top of `SESSION_EXECUTION.md` so a new chat/model can resume safely without reading the full ledger first. Update this mirror whenever continuation state, lifecycle boundary, blockers, evidence status, or the next safe command changes.

| Field | Current value | Backing authority / evidence |
|---|---|---|
| Last updated | | |
| Session ID | | `SESSION_STATE.json` / Command Resolution |
| Current lifecycle stage | | `SESSION_STATE.json` / Lifecycle Progress |
| Current terminal state | | `SESSION_STATE.json` / Terminal State |
| Current status | | `SESSION_STATE.json` |
| Active contract | | `SESSION_CONTRACT.md` |
| Active delivery / phase / unit | | `SESSION_CONTRACT.md` / `DESIGN.md` / implementation units |
| Authoritative artifacts reviewed | | Artifact Instantiation Log / Material Artifact References |
| Completed since session start | | Command Timeline / Evidence Log |
| In progress | | Continuation Pass Register / implementation units |
| Blocked | | Fail-Closed Conditions / unresolved-items.md |
| Gated unresolved items | | `unresolved-items.md` |
| Non-gating unresolved items | | `unresolved-items.md` |
| Technical-review items | | `DESIGN.md` / `unresolved-items.md` |
| Evidence status | | `EVIDENCE.md` / Evidence Log |
| Next safe governed command | | `SESSION_STATE.json.recommended_next_command` |
| What the next model must not do | | Active Execution Controls / Preservation Rules |
| Resume instructions | | This snapshot + backing artifacts |

Fail-closed rule: if this snapshot is missing, placeholder-only, or contradicts `SESSION_STATE.json`, `unresolved-items.md`, or the append-only ledger, HIRMOS must update/reconcile it or stop at `Blocked / Fail-Closed` before surfacing continuation, readiness, completion, or close claims.

## Command Resolution

| Field | Value |
|---|---|
| Session ID | |
| Active command | |
| User request | |
| Interaction mode | |
| Active lifecycle stage | |
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

`SESSION_EXECUTION.md` is append-only for command history, continuation passes, evidence logs, route-backs, and lifecycle boundary records. HIRMOS must not replace or erase earlier pass records when a later `hirmos continue` corrects, extends, validates, or routes back the session.

Permitted edits to earlier sections are limited to:

- filling previously blank fields in the active current-state mirror;
- correcting clerical errors with a dated correction note;
- changing a control status only when the change is also logged in `Control Mutation Ledger`;
- appending evidence or review records that explicitly reference the affected earlier pass.

Forbidden edits:

- deleting prior continuation pass rows;
- replacing prior evidence with newer evidence;
- silently rewriting terminal state, next command, scope effect, or pass result;
- removing unresolved-item dispositions or unit-review outcomes;
- collapsing multiple continue passes into a single summary.

Fail-closed rule: if HIRMOS cannot preserve prior ledger history while applying a correction or amendment, it must stop at `Blocked / Fail-Closed` and recommend exactly one governed recovery command.


## Beyond Clear Specs Application

`SESSION_EXECUTION.md` applies the execution-control subset of `_hirmos/core/authority/BEYOND_CLEAR_SPECS.md` to the active session command spine. This does not activate broad doctrine everywhere; it applies the preserved pattern only where session execution needs it.

Required controls applied here:

- clear execution controls for each lifecycle boundary;
- strict local self-validation before surfacing readiness, implementation-completion, close-readiness, blocked, or close-success claims;
- append-only command, evidence, continuation-pass, route-back, and control-mutation records;
- fail-closed behavior when the ledger, machine state, unresolved-item register, Session Contract close verification, or evidence cannot support the claim.

HIRMOS must not claim a lifecycle boundary complete merely because the intended work was described clearly. It may claim the boundary only when this execution spine self-validates that the required controls were actually satisfied and recorded.

## Command Timeline

| Seq | Command / action | Lifecycle stage before | Lifecycle stage after | Result | Evidence |
|---:|---|---|---|---|---|

## Active Lifecycle Stage

- Current stage:
- Stage authority:
- Stage owner:
- Boundary claim allowed? YES | NO
- Boundary claim rationale:

## Active Execution Controls

Execution controls apply clear-specification discipline: clear specs, self-validation, and fail-closed behavior. If any required control is `UNSATISFIED` or `BLOCKED`, HIRMOS must not claim the lifecycle boundary complete.

| Control | Required evidence | Status | Notes / evidence path |
|---|---|---|---|
| Bootstrap control | Bootstrap completed for current agent/context | PENDING | |
| Command control | Relevant command spec read and terminal states understood | PENDING | |
| Working-copy control | Project root and `_hirmos/` installation verified | PENDING | |
| Current-system-state-first control | `CURRENT_SYSTEM_STATE.md` read before meaningful work or absence recorded | PENDING | |
| Session contract control | `SESSION_CONTRACT.md` exists, is non-placeholder, and defines scope/criteria | PENDING | |
| Unresolved-items control | `_hirmos/session/unresolved-items.md` directly reviewed and reconciled | PENDING | |
| Session Contract close verification control | `_hirmos/session/SESSION_CONTRACT.md` section 11 directly completed before implementation-completion, close-readiness, or close claims | PENDING | |
| Implementation-unit coverage control | Planned units collectively cover `SESSION_CONTRACT.md` or are not applicable | PENDING | |
| Implementation authorization control | Session contract authorizes implementation | PENDING | |
| Validation/evidence control | Claimed validation evidence is recorded | PENDING | |
| Continuation snapshot control | User-facing continuation/readiness output is backed by `Current Continuation Snapshot` and real artifacts | PENDING | |
| Close/reset control | Archive/state/reset invariants satisfied before close claim | PENDING | |

Allowed statuses:

```text
PENDING
SATISFIED
UNSATISFIED
BLOCKED
NOT_APPLICABLE
```


## Unresolved Register Direct Review Log

This log proves that HIRMOS reviewed `_hirmos/session/unresolved-items.md` directly. The `SESSION_CONTRACT.md` unresolved summary is not sufficient for these boundaries.

| Boundary | Register reviewed directly? | Blocking status | Gated count | Non-gating count | Technical-review count | Reviewer notes |
|---|---|---|---:|---:|---:|---|
| Bootstrap / command resolution | NO | NOT_REVIEWED | | | | |
| Implementation readiness | NO | NOT_REVIEWED | | | | |
| Implementation completion | NO | NOT_REVIEWED | | | | |
| Close readiness | NO | NOT_REVIEWED | | | | |

## Baseline Control Families

| Family | Controls included | Current status |
|---|---|---|
| Command and lifecycle | Bootstrap, command, working copy, lifecycle stage | PENDING |
| Contract and scope | Session contract, unresolved items, implementation authorization | PENDING |
| Implementation | Implementation units, evidence, validation | PENDING |
| Close and archive | Accepted-state update, archive, reset | PENDING |

## Control Mutation Ledger

Every material control-state change must be appended here. Do not overwrite earlier control outcomes without recording why the control changed.

| Seq | Control | Previous status | New status | Triggering command/pass | Reason | Evidence |
|---:|---|---|---|---|---|---|

## Control Self-Validation

Before each lifecycle boundary claim, answer:

| Question | Answer | Evidence | Gaps |
|---|---|---|---|
| Are all required controls for this boundary satisfied? | YES | | |
| Is any gated unresolved item blocking the boundary? | NO | | |
| Does the user-facing claim match artifact evidence? | YES | | |
| Is the next command governed and legal? | YES | | |

## Session Contract Section 11 Review Control

The root `_hirmos/session/SESSION_CONTRACT.md` section 11 artifact is the governed promised-vs-verified review surface. HIRMOS must not rely on chat summaries or `SESSION_CONTRACT.md` summaries alone for implementation-completion, close-readiness, or close claims.

## Ledger Integrity Self-Validation

Before surfacing any implementation-complete, close-ready, blocked, or close-success claim, answer these ledger integrity questions.

| Question | Answer | Evidence | Gaps / action |
|---|---|---|---|
| Were all previous continuation pass records preserved? | NOT_CHECKED | | |
| Was the current pass appended instead of replacing an earlier pass? | NOT_CHECKED | | |
| Were control changes recorded in the Control Mutation Ledger? | NOT_CHECKED | | |
| Were unresolved-item dispositions appended rather than deleted? | NOT_CHECKED | | |
| Were implementation-unit attempts/reviews appended rather than replaced? | NOT_CHECKED | | |
| Does `SESSION_STATE.json.continuation_pass` match the latest continuation pass number? | NOT_CHECKED | | |

Allowed answers: `YES`, `NO`, `NOT_APPLICABLE`, `NOT_CHECKED`. A `NO` answer blocks implementation-completion and close claims until reconciled.

## Fail-Closed Conditions

HIRMOS must fail closed and must not claim readiness, implementation completion, or close when any of these conditions is true:

- `SESSION_STATE.json` and `SESSION_EXECUTION.md` disagree on active status or lifecycle stage.
- `SESSION_CONTRACT.md` is missing, placeholder-only, or not reviewed when implementation or close is claimed.
- `_hirmos/session/unresolved-items.md` is missing or has unresolved gated items blocking the boundary.
- `_hirmos/session/SESSION_CONTRACT.md` section 11 is missing, placeholder-only, not directly reviewed, or has a fail-closed result of `FAIL` when implementation completion, close readiness, or close success is claimed.
- User-facing continuation/readiness output references artifacts that do not exist, are placeholders, or contradict the Current Continuation Snapshot.
- Implementation units are individually complete but the combined units do not cover the Session Contract.
- Validation evidence is claimed without recorded command output, inspection evidence, or explicit not-run rationale.
- Close is claimed while stale active-session artifacts remain after reset.
- If any prior continuation pass row is missing, collapsed, or overwritten without a correction note.

## Material Artifact References

| Artifact | Role | Required? | Current status |
|---|---|---:|---|
| `_hirmos/session/SESSION_STATE.json` | machine command state | yes | |
| `_hirmos/session/SESSION_CONTRACT.md` | session scope and acceptance authority | yes | |
| `_hirmos/session/unresolved-items.md` | governed unresolved-item register | yes | |
| `_hirmos/session/SESSION_CONTRACT.md` section 11 | governed promised-vs-verified contract review | yes | |
| `_hirmos/session/implementation-units/` | implementation unit contracts/reviews | conditional | |
| `_hirmos/session/bootstrap/` | startup/bootstrap evidence infrastructure | yes | |
| `_hirmos/session/EVIDENCE.md` | consolidated nontrivial evidence surface | conditional | |
| `_hirmos/session/stack-resolution.json` | machine-readable stack routing state | conditional | |

## Artifact Instantiation Log

Every created artifact must be recorded here.

| Target artifact | Source template | Lifecycle stage | Reason required | Non-placeholder check status |
|---|---|---|---|---|

## Lifecycle Progress

| Stage | Status | Evidence | Notes |
|---|---|---|---|
| Bootstrap | PENDING | | |
| Understand System State | PENDING | | |
| Design / Contracting | PENDING | | |
| Implementation Readiness | PENDING | | |
| Implementation | PENDING | | |
| Validation / Review | PENDING | | |
| Update System State / Close | PENDING | | |

## Continuation Boundary Log

Record each surfaced decision, readiness, completion, blocked, status, or close boundary that changes continuation state.

| Boundary ID | Boundary | Snapshot updated? | User-facing claim | Backing controls | Result |
|---|---|---|---|---|---|

## Continuation Pass Register

Every `hirmos continue` invocation must append one row and, when material, one detail block. Do not overwrite prior passes.

| Pass | Command | Pass type | Scope effect | Artifacts updated | Evidence | Result | Next governed command |
|---:|---|---|---|---|---|---|---|

Allowed pass types: `INITIAL_IMPLEMENTATION`, `CORRECTIVE`, `CONTRACT_AMENDMENT`, `VALIDATION_ONLY`, `ROUTE_BACK`.

Continuation pass append requirements:

- assign the next integer pass number from `SESSION_STATE.json.continuation_pass + 1`;
- record the exact user command or correction/amendment request;
- classify pass type and scope effect;
- identify affected Session Contract sections and implementation units;
- record artifacts changed and evidence produced;
- record whether prior pass records were preserved;
- update `SESSION_STATE.json.continuation_pass` to match the latest appended pass;
- surface exactly one legal next governed command.


### Continuation pass detail blocks

Use one block per pass when the row is not enough.

```text
### Continue Pass <n> — <type>
- User command:
- Reason:
- Scope effect: same-contract correction | contract amendment | validation only | route-back
- Session Contract impact:
- Implementation units affected:
- Unresolved items affected:
- Files/artifacts changed:
- Evidence:
- Result:
- Next governed command:
```

## Route-Back Records

Record when a later stage discovers a problem owned by an earlier stage.

| Seq | Discovered at stage | Problem | Owning stage/artifact | Downstream controls reset | Result |
|---:|---|---|---|---|---|

## Evidence Log

| Seq | Evidence type | Command / inspection / artifact | Result | Supports claim |
|---:|---|---|---|---|

## Readiness Gates

| Gate | Required before | Status | Evidence |
|---|---|---|---|
| `SESSION_CONTRACT.md` section 11 review | Implementation-completion, close-readiness, and close claims | PENDING | `_hirmos/session/SESSION_CONTRACT.md` section 11 |
| Unresolved Items Reconciliation | Every lifecycle boundary | PENDING | `_hirmos/session/unresolved-items.md` |
| Implementation Unit Coverage | Implementation start / close | PENDING | `_hirmos/session/implementation-units/` |
| Validation Evidence | Implementation complete / close | PENDING | evidence log / major artifacts / evidence |

## Exactly-one-next-command rule

Every surfaced command result must name exactly one primary governed next command. Prose such as `reply to proceed` is not a governed command.

## Terminal State

- Terminal state:
- Supported user-facing summary:
- Exactly one primary next governed command:
- Why this command is legal:

## Capability / Stage Activity Summary

| Capability / stage | Entrypoint | Activity summary | Produced artifacts | Unresolved-item producer outcome |
|---|---|---|---|---|

## System-State Capability Summary

| System-state capability | Evidence reviewed | Summary | Handoff / route-back |
|---|---|---|---|

## Design Capability Summary

| Design capability | Authority consumed | Output / decision | Handoff |
|---|---|---|---|

## Implementation Capability Summary

| Implementation capability | Unit / artifact | Output / evidence | Review result |
|---|---|---|---|

## Governed Continuation Summary

| Boundary / output | Governed basis | User-facing output | Next command |
|---|---|---|---|

- Current Continuation Snapshot status:
- Unresolved item status:

## Project Context / Stack Summary

| Project type | Active stack | Stack contexts active | Evidence |
|---|---|---|---|

## Runtime Integration / Production Readiness Summary

| Area | Authorized posture | Evidence | Limitation |
|---|---|---|---|

## Vertical Slice / Delivery Status Summary

| Slice / unit | Status | User-facing outcome | Next action |
|---|---|---|---|

## Command Output Summary

- User-facing summary:
- Exactly one primary next command/action:
- Next recommended phase:


## Close / Archive / Reset Invariant Controls

These controls are mandatory before normal close can be claimed. They apply even when older generated close/checklist artifacts are absent.

| Invariant | Required evidence | Status |
|---|---|---|
| Session Contract close verification completed | `_hirmos/session/SESSION_CONTRACT.md` section 11 final verdict supports close | PENDING |
| Unresolved register reconciled | `_hirmos/session/unresolved-items.md` directly reviewed; no blocking gated item remains | PENDING |
| Accepted state updated | `CURRENT_SYSTEM_STATE.md`, active-only `CARRY_FORWARD.md`, and `DECISION_LOG.md` updated or verified unchanged | PENDING |
| Archive complete | archive path contains all active session artifacts and `SESSION_EXECUTION.md` archive controls | PENDING |
| Archived session state normalized | archived `SESSION_STATE.json` is closed / archived / history_only | PENDING |
| Active session reset | active `_hirmos/session/` reset to idle scaffolding only | PENDING |
| Stale artifact scan clear | no runtime active-session artifacts remain after close reset | PENDING |

Fail-closed rule: if any invariant remains `PENDING`, `UNSATISFIED`, or `BLOCKED`, HIRMOS must not surface normal close success.

## Close / Archive / Accepted-State Integrity Summary

| Close control | Status | Evidence |
|---|---|---|
- Post-close status consistency:

## Claim Reconciliation Summary

| Claim | Evidence | Supported? | Downgrade / route-back if needed |
|---|---|---|---|
- claim reconciliation control:

## Archive Session State Normalization

- archive-session-state-normalized:
- active-session-state-reset:

## Current-State Execution Controls

| Current-state control | Status | Evidence |
|---|---|---|

## Invariant / Canonical Value Controls

| Invariant | Canonical value | Status | Evidence |
|---|---|---|---|

## Current-System-State-First Understanding Controls

| Understanding control | Status | Evidence |
|---|---|---|
- current-system-state-read-first:

## Requirements Baseline Controls

| Requirements control | Status | Evidence |
|---|---|---|
- requirements-baseline-instantiated:
- requirements-intake-classification-preserved:
- requirements-prototype-set-reconciled:
- requirements-flow-detail-sufficient:

## Close-Time Compliance Controls

| Close-time control | Status | Evidence |
|---|---|---|
- i23-claim-reconciliation-materialized:



## Production-Shaped Engineering Gate Execution

Required before implementation readiness and again before close for implementation-capable software sessions.

| Gate area | Required check | Readiness result | Close result | Evidence / limitation |
|---|---|---|---|---|
| Persistence / database | Durable data posture matches Design/Contract or limitation is authorized | PENDING | PENDING | |
| Auth / authorization | Protected resources have server-side isolation where material | PENDING | PENDING | |
| Background jobs / long-running work | Slow provider/file/AI work is not merely awaited in request path unless explicitly authorized | PENDING | PENDING | |
| Credits / usage / billing / quotas | Accounting is transactional/concurrency-safe/idempotent or explicitly limited | PENDING | PENDING | |
| Provider APIs / external services | Provider mode, env validation, and failure posture are truthful | PENDING | PENDING | |
| File/storage/handoff hygiene | Uploads/generated assets/secrets/runtime data are handled safely | PENDING | PENDING | |
| Critical-flow evidence | Test/smoke/runtime evidence exists or not-run rationale is accepted | PENDING | PENDING | |

Fail-closed rule: do not claim production-shaped implementation, implementation completion, or close success when code/evidence contradicts this gate. Downgrade the claim, route back, or preserve the limitation as carry-forward.

## Delivery Shape Decision Gate Execution

Required for every implementation-capable `hirmos start` before implementation readiness.

Literal decision question:

```text
What is the smallest sufficient governed delivery shape for this request?
Answer: SINGLE_SESSION_VERTICAL_SLICE / SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS / MULTI_SESSION_DELIVERY / MULTI_SESSION_DELIVERY_WITH_PHASE_FILES / UNCERTAIN.
Evidence:
Decision factors:
Smaller-shape safety analysis:
Larger-shape overhead analysis:
Required durable delivery artifacts, if any:
If UNCERTAIN, what must be inspected before deciding?
```

Gate result:

- Answer: SINGLE_SESSION_VERTICAL_SLICE | SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS | MULTI_SESSION_DELIVERY | MULTI_SESSION_DELIVERY_WITH_PHASE_FILES | UNCERTAIN | NOT_ASSESSED
- Evidence:
- Decision factors:
- Project-type factors considered:
- Production-shaped engineering factors considered:
- Validation/review factors considered:
- Continuity/accepted-state factors considered:
- Smaller-shape safety analysis:
- Larger-shape overhead analysis:
- Required Delivery Plan path:
- Active phase path, if any:
- Implementation-unit coverage path, if selected:
- Gate status: PASS | BLOCKED | NOT_ASSESSED

Fail-closed rule: `UNCERTAIN`, missing decision, unsafe smaller shape, or selected durable-delivery shape without required artifacts blocks implementation readiness.

## Delivery / Phase Capability Routing Log

Required when the selected delivery shape is `MULTI_SESSION_DELIVERY` or `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

| Capability | Expected durable/session output | Status | Evidence path | Notes |
| --- | --- | --- | --- | --- |
| delivery-design | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | PENDING | | |
| phase-contracting | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` when phase files are selected | PENDING | | |
| session-contract | `_hirmos/session/SESSION_CONTRACT.md` adopts the active phase | PENDING | | |
| implementation-readiness | `DESIGN.md` readiness basis and `SESSION_CONTRACT.md` authorize implementation | PENDING | | |

Fail closed if this log is missing, incomplete, or contradicted by artifacts while the selected delivery shape requires durable delivery artifacts.


## Current System State Delivery Pointer Concordance


## Durable Phase Adoption Gate

Required before implementation readiness whenever the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

| Check | Required result | Evidence artifact | Actual result |
|---|---|---|---|
| Exactly one durable phase adopted | SATISFIED | `SESSION_CONTRACT.md` Active Durable Phase Adoption | PENDING |
| Adopted phase path exists | SATISFIED | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | PENDING |
| Delivery Plan path exists | SATISFIED | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | PENDING |
| Current System State pointer matches adopted phase | SATISFIED | `CURRENT_SYSTEM_STATE.md` Active Development Context and Delivery Pointers | PENDING |
| Phase items mapped to Session Contract items | SATISFIED | `SESSION_CONTRACT.md` Adopted phase scope | PENDING |
| Partial adoption has explicit deferrals | SATISFIED / NOT_APPLICABLE | `SESSION_CONTRACT.md` Phase exclusions / deferrals | PENDING |

Fail-closed rule: implementation readiness is blocked if no durable phase is adopted, if more than one phase is treated as active for the same session, if the adopted phase path is missing, or if adopted phase scope is not mapped into authorized Session Contract items.


Record this before implementation readiness and again before close when delivery governance is active or potentially applicable.

| Check | Result | Evidence | Notes |
|---|---|---|---|
| Current System State delivery pointers read | SATISFIED / BLOCKED / NOT_APPLICABLE | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | |
| Delivery Plan pointer exists when required | SATISFIED / BLOCKED / NOT_APPLICABLE | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | |
| Active Phase pointer exists when required | SATISFIED / BLOCKED / NOT_APPLICABLE | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | |
| Session Contract adopts the same delivery/phase authority | SATISFIED / BLOCKED / NOT_APPLICABLE | `SESSION_CONTRACT.md` | |
| Next phase / next command concordance checked | SATISFIED / BLOCKED / NOT_APPLICABLE | `DELIVERY_PLAN.md`, `SESSION_STATE.json` | |

Fail-closed rule: delivery-governed implementation must not proceed while Current System State delivery pointers contradict the durable Delivery Plan, active Phase file, or Session Contract.


## Close-Time Delivery Status Execution Log

When delivery governance is active, record close-time delivery status actions here before close is claimed.

| Action | Target artifact | Result | Evidence |
|---|---|---|---|
| Delivery status transaction prepared | `SESSION_EXECUTION.md` close/update controls | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Adopted phase status update prepared | `PHASE-xx.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Parent Delivery Plan status update prepared | `DELIVERY_PLAN.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Current System State delivery pointers prepared | `CURRENT_SYSTEM_STATE.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |

Fail-closed rule: do not mark the close transaction complete if durable delivery status updates remain pending, blocked, stale, or contradictory.

## Phase Entry Gate Execution Log

Before implementation readiness, record the Phase Entry Gate result for any adopted durable phase.

Required log:

```text
Phase file inspected:
Delivery Plan inspected:
Current System State pointer inspected:
Phase Entry Gate status:
Greenfield entry controls result:
Brownfield entry controls result:
Mixed phase result:
Blocking items result:
Implementation readiness authorized: YES / NO
```

Fail-closed rule: do not proceed to implementation readiness if the Phase Entry Gate is missing, stale, ambiguous, or not `PASS`.

## Phase Progress / Carry-Forward Record

Required for delivery-governed sessions before continuation or close.

| Check | Status | Evidence / pointer | Notes |
|---|---|---|---|
| Adopted phase progress reviewed | PENDING / PASS / BLOCKED | | |
| Previous Phase Progress Ledger inspected | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Completed phase items recorded | PENDING / PASS / BLOCKED | | |
| Partial / blocked / deferred items classified | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Carry-forward obligations recorded | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Current System State pointer outcome determined | PENDING / PASS / BLOCKED | | |

Fail-closed rule: a delivery-governed close or continuation must not proceed when phase progress or carry-forward state is `PENDING` for adopted phase work.


## Phase Acceptance Enforcement Record

This record is required before a delivery-governed close may mark the adopted durable phase `ACCEPTED`.

| Acceptance control | Status | Evidence pointer | Notes |
|---|---|---|---|
| Phase Acceptance Evidence Gate inspected | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| All adopted Session Contract items reviewed | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Implementation Unit evidence complete | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Greenfield acceptance evidence complete when applicable | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Brownfield acceptance evidence complete when applicable | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |
| Delivery Plan / Phase / Current System State updates prepared | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |

Fail closed if phase acceptance evidence is incomplete, contradictory, or only stated in chat/archive without durable artifact updates.


## Phase Lifecycle Status Report Record

Record the status information that `hirmos status` must be able to surface without mutation.

| Status field | Value / evidence pointer | Status | Notes |
|---|---|---|---|
| Active delivery ID | | RECORDED / MISSING / NOT_APPLICABLE | |
| Delivery Plan path | | RECORDED / MISSING / NOT_APPLICABLE | |
| Active Phase path | | RECORDED / MISSING / NOT_APPLICABLE | |
| Phase lifecycle status | | RECORDED / MISSING / CONFLICT | |
| Phase type | | RECORDED / UNKNOWN / CONFLICT | |
| Phase Entry Gate status | | PASS / BLOCKED / UNCERTAIN / NOT_APPLICABLE | |
| Phase adoption status | | ADOPTED / BLOCKED / NOT_APPLICABLE | |
| Phase Progress Ledger status | | CURRENT / STALE / MISSING / NOT_APPLICABLE | |
| Carry-Forward Items status | | NONE / RECORDED / BLOCKED / NOT_APPLICABLE | |
| Phase Acceptance Evidence Gate status | | COMPLETE / INCOMPLETE / BLOCKED / NOT_APPLICABLE | |
| Missing evidence / blocked controls | | NONE / PRESENT / NOT_ASSESSED | |
| Current System State pointer concordance | | PASS / BLOCKED / NOT_ASSESSED | |
| Exactly one recommended next command | | RECORDED / MISSING / CONFLICT | |

Fail-closed rule: if status evidence is contradictory, report `Status Blocked By Phase Lifecycle Conflict`; do not imply implementation or phase acceptance authorization.


## Append-Only Ledger Integrity Check

Before surfacing any continuation, readiness, completion, blocked, or close output, verify that the Current Continuation Snapshot is current and that all earlier continuation pass rows and detail blocks remain present. New passes must be appended; earlier passes must not be replaced, summarized away, or deleted.

## Phase Progress / Carry-Forward Record

- Adopted phase progress reviewed:
- Carry-forward obligations recorded:
- Execution controls reset if needed:

## Phase Acceptance Enforcement Record

- Phase Acceptance Evidence Gate inspected:
- Phase acceptance evidence status:
- Phase lifecycle status:
