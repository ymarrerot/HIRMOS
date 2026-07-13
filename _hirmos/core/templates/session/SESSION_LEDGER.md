# Session Ledger
Status: active-session ledger ledger.
Purpose: compact chronological gate/event ledger for the current HIRMOS session.
`SESSION_LEDGER.md` records only event order, gate status, authority source, evidence pointer, and next allowed transition. It must not own scope, requirements, design decisions, evidence details, unresolved-item details, accepted-state truth, or archive transaction details.

Authoritative references: machine state `_hirmos/session/SESSION_STATE.json`; bootstrap `bootstrap/BOOTSTRAP_REPORT.md`; scope `SESSION_SCOPE.md`; unresolved `unresolved-items.md`; evidence `EVIDENCE.md`; IU records `implementation-units/IU-*.md`; delivery artifacts; accepted-state `CURRENT_SYSTEM_STATE.md`; carry-forward `CARRY_FORWARD.md`; archive manifest.

## Current Continuation Snapshot
Compact resume surface. Update before readiness, completion, blocked, status, or close claims.
| Field | Current value | Backing authority / evidence |
|---|---|---|
| Last updated / Session ID / lifecycle / focus / status | | `SESSION_STATE.json` |
| Active authority / scope / delivery-phase-unit | | `SESSION_SCOPE.md` / delivery / IU pointers |
| Evidence status / artifacts reviewed | | `EVIDENCE.md` / Boundary Control Checklist |
| Next safe governed command | | `SESSION_STATE.json` |
| What the next model must not do | | Fail-Closed Conditions |

## Command Resolution
| Field | Value |
|---|---|
| Session ID / Active command / User request | |
| Canonical interaction posture | One HIRMOS posture: simple by default, transparent by design, rigorous underneath, progressive in disclosure. |
| Lifecycle before / after / continuation state | |
| Recommended next governed command | |

## Active / Pre-Close Machine Command State Concordance
`SESSION_STATE.json` is the machine command-state authority. This section is an explanatory mirror only. If this section disagrees with `SESSION_STATE.json`, HIRMOS must fail closed.
| Field | SESSION_STATE.json value | SESSION_LEDGER.md value | Concordance | Notes |
|---|---|---|---|---|
| status / lifecycle_stage / allowed_next_commands / recommended_next_command / continuation_pass / pending_correction | | | NOT_CHECKED | |
Allowed concordance values: `MATCH`, `MISMATCH`, `NOT_CHECKED`. A `MISMATCH` blocks readiness, implementation-completion, and close claims.

## Append-Only Ledger Covenant
Append-only for command history, continuation passes, route-backs, control-state changes, and boundary records. Preserve prior pass rows; do not collapse multiple continue passes into one summary. Every `hirmos continue` is a governed pass and must be classified before action. Corrections require a dated note and Control Mutation Ledger row. Forbidden edits: deleting prior continuation pass rows, silently rewriting terminal state, or collapsing multiple continue passes. Fail-closed rule: if HIRMOS cannot preserve prior ledger history while applying a correction or amendment, it must stop at `Blocked / Fail-Closed`.


## Derived Command-State Record

`SESSION_STATE.json.allowed_next_commands` and `SESSION_STATE.json.recommended_next_command` are derived cache fields, not independent writable authority. Recompute them from ledger gates, pending correction, lifecycle state, IU planning/execution authorization, and command packet legality before reporting next action. If derived command state conflicts with `SESSION_STATE.json`, fail closed and correct the cache before continuing.

| Derived value | Source gates | Derived result | Concordance with SESSION_STATE.json | Action |
|---|---|---|---|---|
| allowed_next_commands | SESSION_LEDGER.md + runtime command packet | | MATCH / STALE / BLOCKED | |
| recommended_next_command | SESSION_LEDGER.md + runtime command packet | | MATCH / STALE / BLOCKED | |


## Gate Marker Map
Compact validator-readable index for preserved gate markers. The detailed operational rules remain in owning artifacts, command files, protocols, IU files, and evidence records; this map preserves marker visibility without expanding user-facing checkpoint output.

| Gate / marker ID | Gate name | Required source | Status / evidence pointer |
|---|---|---|---|
| PROD-L8.19 | Command Legality and Correction Ledger Concordance | `SESSION_STATE.json`, command packets, IU files | see marker section / validation output |
| PROD-L8.21 | IU Set Authority Checkpoint | `implementation-units/IU-*.md`, `SESSION_SCOPE.md` | see marker section / validation output |
| PROD-L8.23 | Generated-Run IU Enforcement Checkpoint | IU files + active generated-artifact validation | see marker section / validation output |
| PROD-L8.24 | Pre-Execution Ledger Enforcement | pre-material-edit ledger row | see marker section / validation output |
| PROD-L8.30A | Bootstrap / IU Action-Gate Control | `BOOTSTRAP_REPORT.md`, IU files, validation output | see marker section / validation output |
| PROD-L8.31 | Generated-Run Mechanical Gate Record | generated-artifact validator | see marker table / validation output |
| PROD-L8.32K | Runtime Boundary Validation Record | command authority + active gate validator | see boundary record / validation output |
| PROD-L8.32L | Artifact Instantiation Boundary | source artifacts + derived pointer tooling | see boundary record / derived pointer output |

Rule: adding or changing a protected gate marker requires updating this map and its validator/static check. The map is an index, not a substitute for live gate rows or evidence.


## Archived Session State Concordance

Use this section only after archive/close. Archived ledgers may preserve pre-close machine state only when the section is explicitly labeled `Pre-Close` and points to `PRE_CLOSE_SESSION_STATE.json`. Post-close archive state must not be mixed with current-looking active/implementation-complete command rows.

| State surface | Expected archive value | Source pointer | Status | Notes |
|---|---|---|---|---|
| PRE_CLOSE_SESSION_STATE.json preserved | YES / NO / N/A | `_hirmos/system/history/sessions/<session-id>/PRE_CLOSE_SESSION_STATE.json` | PASS / BLOCKED / N/A | |
| Archived SESSION_STATE.json | archived / closed / superseded | `_hirmos/system/history/sessions/<session-id>/SESSION_STATE.json` | PASS / BLOCKED / N/A | |
| Active/pre-close concordance labeled historical | YES / NO / N/A | this ledger | PASS / BLOCKED / N/A | |

## Event Ledger
| Seq | Event | Status | Authority source | Evidence / pointer | Next allowed transition |
|---:|---|---|---|---|---|

## Boundary Control Checklist
Pointer-only checklist; details stay in owning artifacts.
| Control | Owning artifact | Required before | Status | Evidence / pointer |
|---|---|---|---|---|
| Bootstrap control | `bootstrap/BOOTSTRAP_REPORT.md` | command resolution | PENDING | complete discipline answers |
| General Run Preflight Control | `_hirmos/AGENTS.md` / config / command spec / integration registry when required | before command execution | PENDING | `PRECHECK_PASS`, `PRECHECK_WARNING`, or `PRECHECK_BLOCKER` |
| Command / working-copy / current-state / scope / unresolved / delivery / phase / IU / validation / close controls | owning artifact pointers | boundary-specific | PENDING / NOT_APPLICABLE | |
Allowed statuses: `PENDING`, `SATISFIED`, `UNSATISFIED`, `BLOCKED`, `NOT_APPLICABLE`.

## Active Execution Controls
| Boundary | Required controls | Control status | Notes / evidence path |
|---|---|---|---|
| command resolution | bootstrap, command, machine-state concordance | PENDING | |
| implementation readiness | current-state, session scope, unresolved, delivery/phase if active, implementation authorization | PENDING | |
| implementation completion | scope review, evidence pointer, unresolved review, unit review if active | PENDING | |
| close readiness / close success | scope close verification, evidence pointer, unresolved review, accepted-state/archive/reset plan | PENDING | |

## Baseline Control Families
Command/lifecycle, scope/unresolved, delivery/phase, implementation/evidence, and close/archive control families are tracked by Boundary Control Checklist and Active Execution Controls.

## Control Mutation Ledger
| Seq | Control | Previous status | New status | Triggering command/pass | Reason | Evidence pointer |
|---:|---|---|---|---|---|---|

## Readiness Gates
| Gate | Required before | Status | Evidence pointer |
|---|---|---|---|
| Session Scope review | implementation readiness / close | PENDING | `SESSION_SCOPE.md` |
| Unresolved Items Reconciliation | every lifecycle boundary | PENDING | focus-appropriate unresolved register |
| Implementation Unit Coverage | IU planning review / implementation execution / close | NOT_APPLICABLE | `implementation-units/` |
| Validation Evidence | completion / close | PENDING | `EVIDENCE.md` / unit reviews |

## Control Self-Validation
| Question | Answer | Evidence pointer | Gaps |
|---|---|---|---|
| Required controls satisfied / gated blockers absent / user-facing claim supported / next command legal? | NOT_CHECKED | | |

## Ledger Integrity Self-Validation
| Question | Answer | Evidence pointer | Gaps / action |
|---|---|---|---|
| Were all previous continuation pass records preserved? | NOT_CHECKED | | |
| Was the current pass appended and were control mutations recorded / unresolved dispositions referenced / IU reviews preserved / `SESSION_STATE.json.continuation_pass` concordant? | NOT_CHECKED | | |
Allowed answers: `YES`, `NO`, `NOT_APPLICABLE`, `NOT_CHECKED`. A `NO` answer blocks implementation-completion and close claims until reconciled.



## PROD-L8.32K Runtime Boundary Validation Record
This record proves the model used the compact runtime path and invoked validation before transition claims. It is pointer-only; validator output or command transcript detail belongs in evidence or command output.

| Boundary | Command file used | Active gate validator result | IU_EXECUTION_AUTHORIZED present? | Material project-file edits before authorization | Transition claim allowed? | Evidence pointer |
|---|---|---|---|---|---|---|
| start / continue / IU planning / IU execution / completion / close | `_hirmos/core/commands/<command>.md` | PASS / FAIL / BLOCKED / NOT_RUN | YES / NO / NOT_APPLICABLE | BLOCKED / NO / YES_INVALID | YES / NO | |

Fail-closed rule: `NOT_RUN`, `FAIL`, `BLOCKED`, or `YES_INVALID` blocks implementation-complete, close-readiness, close, archive, and accepted-state transition claims. Material project/source edits before accepted baseline authority are validation failures, not warning-level issues. In IU mode, material project/source edits before `IU_EXECUTION_AUTHORIZED` are validation failures, not warning-level issues.

## Start / Baseline Pre-Edit Gate
This gate prevents `hirmos start` from being collapsed into start + implementation. `hirmos start` may create/update HIRMOS governance artifacts and surface a baseline checkpoint only; it must not edit project/source files outside `_hirmos/`.

| Gate | Required before | Status | Authority source | Evidence pointer | Next allowed transition |
|---|---|---|---|---|---|
| BASELINE_UNDER_REVIEW | end of `hirmos start` | PASS / BLOCKED / NOT_APPLICABLE | `SESSION_SCOPE.md` or delivery baseline artifact | baseline checkpoint output | wait for `hirmos continue` |
| BASELINE_ACCEPTED_OR_AMENDED | material project/source edits | PENDING / PASS / BLOCKED / NOT_APPLICABLE | user continuation + `SESSION_SCOPE.md` status | Continuation Pass Register | implementation readiness or IU planning |
| PRE_MATERIAL_EDIT_GATE | immediately before first material edit | PENDING / PASS / BLOCKED / NOT_APPLICABLE | accepted baseline + command state + IU gate if applicable | Pre-Material-Edit Ledger Row | material edits may start only if all applicable gates pass |

Fail-closed rule: detailed user instructions are scope input, not implementation authorization. If baseline acceptance is missing, or if IU mode applies and `IU_EXECUTION_AUTHORIZED` is missing, material edits are blocked.

## IU Planning / IU Execution Boundary Record
This boundary prevents session-baseline acceptance from being confused with implementation authorization. In IU mode, baseline acceptance authorizes IU planning/materialization only. Material project-file edits require a later explicit IU execution authorization.

| Gate | Required before | Status | Authority source | Evidence pointer | Next allowed transition |
|---|---|---|---|---|---|
| IU_PLANNING_REQUIRED | after accepted session baseline when IU mode applies | PENDING / PASS / BLOCKED / NOT_APPLICABLE | `SESSION_SCOPE.md` compact IU pointers | planned IU count and expected paths | create full IU files, no project-file edits |
| IU_PLANNING_COMPLETE | before IU plan review checkpoint | PENDING / PASS / BLOCKED / NOT_APPLICABLE | `implementation-units/IU-*.md` | active generated-artifact validation result | pause for `IU Plan — Review or Change` |
| IU_EXECUTION_AUTHORIZED | before material project/source edits when IU mode applies | PENDING / PASS / BLOCKED / NOT_APPLICABLE | user accepted IU plan + sealed IU files | `hirmos continue "Accept IU plan and begin IU execution"` | implementation execution may start |

Fail-closed rule: `IU_PLANNING_COMPLETE` is not implementation authorization. `IU_EXECUTION_AUTHORIZED` must exist before the first material edit when IU mode applies.
## Fail-Closed Conditions
- `SESSION_STATE.json` and `SESSION_LEDGER.md` disagree on active status, lifecycle stage, continuation pass, or next governed command.
- Required owner artifacts are missing, placeholder-only, stale, or not reviewed when readiness/completion/close is claimed.
- The session attempts material project/source edits before accepted baseline authority is recorded.
- IU mode applies and the session attempts material project/source edits before `IU_EXECUTION_AUTHORIZED` is recorded after IU plan review.
- Gated unresolved items block the boundary; evidence is claimed without a pointer or not-run rationale; delivery/phase/current-state pointers contradict; IU coverage is incomplete; archive/accepted-state/reset evidence is missing; prior continuation rows are collapsed/overwritten.

## Command Timeline
| Seq | Command / action | Lifecycle stage before | Lifecycle stage after | Result | Evidence pointer |
|---:|---|---|---|---|---|

## Continuation Boundary Log
| Boundary ID | Boundary | Snapshot updated? | User-facing claim | Backing controls | Result |
|---|---|---|---|---|---|

## Continuation Pass Register
| Pass | Command | Pass type | Scope effect | SESSION_SCOPE.md impact | Artifacts updated | Evidence pointer | Result | Next governed command |
|---:|---|---|---|---|---|---|---|---|
Allowed pass types: `ACCEPTANCE_ONLY`, `INITIAL_IMPLEMENTATION`, `IU_EXECUTION_AUTHORIZATION`, `CORRECTIVE_PASS`, `SCOPE_AMENDMENT`, `VALIDATION_ONLY`, `ROUTE_BACK`, `CLOSE_PREPARATION`, `BLOCKED`.
Pass concordance rule: latest pass number in this register must match `SESSION_STATE.json.continuation_pass`; missing intermediate pass rows fail close/readiness claims.
Scope-effect rule: if the pass changes accepted authority, acceptance criteria, IU objectives, exclusions, validation requirements, unresolved disposition, or close-satisfaction criteria, record `SESSION_SCOPE.md impact` as `AUTHORITY_DELTA_APPENDED` and update `SESSION_SCOPE.md` before continuing. If not, record `NO_SCOPE_CHANGE` and explain the owner artifact updated.

### Continue Pass <n> — <type>
- User command / Reason / Scope effect / SESSION_SCOPE.md impact / IUs affected / unresolved pointer / files changed / evidence pointer / result / next governed command:

## PROD-L8.33A Continue/Status Gate Notes

- `hirmos continue` must classify and gate before it codes.
- Continue pass records are appended before implementation, validation-readiness, route-back, correction, or close-preparation action.
- If IUs are requested or required and no accepted IU plan exists, the pass result is IU planning / IU plan review, not material implementation.
- If IUs are not required, record the no-IU rationale before material project/source edits.
- `hirmos status` is read-only and must not mutate this ledger, product/source files, lifecycle state, or governance artifacts.

## Route-Back Records
Alias for corrections and earlier-stage route-backs.

## Route-Back / Correction Ledger
| Seq | Discovered at stage | Problem | Owning stage/artifact | Downstream controls reset | Result |
|---:|---|---|---|---|---|

## Artifact Instantiation Log
Pointer-only row for every created artifact.

## Artifact Reference and Instantiation Log
| Artifact | Role | Required? | Action | Non-placeholder / review status |
|---|---|---:|---|---|
| `SESSION_STATE.json` / `SESSION_LEDGER.md` / `SESSION_SCOPE.md` / bootstrap / unresolved / IU / evidence / delivery / archive artifacts | canonical session/delivery surfaces | yes/conditional/close | | |

## Unresolved Register Direct Review Log
Records counts/status only; item details stay in `unresolved-items.md`. `SESSION_SCOPE.md` unresolved summary is not sufficient.
| Boundary | Register reviewed directly? | Blocking status | Gated count | Non-gating count | Technical-review count | Evidence pointer |
|---|---|---|---:|---:|---:|---|
| Bootstrap / implementation readiness / implementation completion / close readiness | NO | NOT_REVIEWED | | | | |

## Capability / Stage Activity Summary
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

## Exactly-one-next-command rule
Every surfaced checkpoint, status, completion, blocked, or close output must provide exactly one primary next governed command/action.

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
| Capability | Expected durable/session output | Status | Evidence path | Notes |
|---|---|---|---|---|
| delivery-baseline / phase-baseline / session-scope / implementation-readiness | expected owner artifact | PENDING / COMPLETED / BLOCKED / NOT_APPLICABLE | | |
Post-continue freshness rule: in `phase_session_baseline`, `phase-baseline` and `session-scope` must be `COMPLETED` with evidence paths once artifacts exist.

## Current System State Delivery Pointer Concordance
| Check | Result | Evidence | Notes |
|---|---|---|---|
| Current System State delivery pointers read / Delivery roadmap pointer exists when required / Delivery scope pointer exists when required / Active Phase pointer exists when required / Session Scope adopts the same delivery/phase authority / Next phase / next command concordance checked | SATISFIED / BLOCKED / NOT_APPLICABLE | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` and delivery/session pointers | |
Fail-closed rule: delivery-governed implementation must not proceed while Current System State delivery pointers contradict durable delivery artifacts.

## Durable Phase Adoption Gate
| Check | Required result | Evidence artifact | Actual result |
|---|---|---|---|
| Exactly one durable phase adopted / Adopted phase path exists / Delivery roadmap path exists / Delivery Scope path exists / Current System State pointer matches adopted phase / Phase items mapped to Session Scope items / Partial adoption has explicit deferrals | SATISFIED / NOT_APPLICABLE | delivery + session scope artifacts | PENDING |

## Phase Entry Gate Execution Log
- Phase file inspected / Delivery Plan inspected / Delivery Scope inspected / Current System State pointer inspected:
- Phase Entry Gate status:
- Entry criteria status: PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE
- Implementation readiness authorized: YES / NO

## Phase Progress / Carry-Forward Record
| Check | Status | Evidence / pointer | Notes |
|---|---|---|---|
| Adopted phase progress reviewed / Carry-forward obligations recorded / Current System State pointer outcome determined | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |

## Phase Acceptance Enforcement Record
| Acceptance control | Status | Evidence pointer | Notes |
|---|---|---|---|
| Phase Acceptance Evidence Gate inspected / All adopted Session Scope items reviewed / Implementation Unit evidence complete / Delivery Plan-Phase-Current State updates prepared | PENDING / PASS / BLOCKED / NOT_APPLICABLE | | |

## Phase Lifecycle Status Report Record
| Status field | Value / evidence pointer | Status | Notes |
|---|---|---|---|
| Active delivery ID / Delivery Plan path / Active Phase path / Phase lifecycle status / Phase type / Phase Entry Gate status / Phase adoption status / Phase Acceptance Evidence Gate status / Exactly one recommended next command | | RECORDED / MISSING / CONFLICT / PASS / BLOCKED / UNCERTAIN / NOT_APPLICABLE | |

## Evidence Log
Pointer-only evidence log; detailed evidence belongs in `EVIDENCE.md` and implementation-unit reviews.

## Evidence Handoff
Pointers only. Evidence details belong in `EVIDENCE.md`, implementation-unit reviews, command output logs, screenshots/logs, or explicit not-run rationale.
| Seq | Evidence pointer | Evidence type | Result | Supports claim |
|---:|---|---|---|---|

## Close-Time Delivery Status Execution Log
| Action | Target artifact | Result | Evidence pointer |
|---|---|---|---|
| Delivery/phase/source pointer transaction prepared; status detail remains in owning close/session/archive artifacts; current-state pointers prepared | delivery/session artifacts | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
Fail-closed rule: do not mark complete if durable delivery status updates remain pending, blocked, stale, or contradictory.

## Close / Archive / Reset Invariant Controls
Required marker: archive-session-state-normalized. Pointer-only close controls. Detailed archive transaction belongs in `ARCHIVE_MANIFEST.md`; promised-vs-verified review belongs in `SESSION_SCOPE.md` close verification and `EVIDENCE.md`.
| Control | Status | Evidence pointer |
|---|---|---|
| Scope close verification complete / Archive manifest prepared / Accepted state updated / Active session reset prepared | PENDING | owner artifact pointer |

## Close / Archive / Accepted-State Integrity Summary
| Check | Status | Evidence pointer |
|---|---|---|
| Archive manifest agrees with active ledger / Accepted-state navigation agrees with delivery-session outcome / Post-close status consistency | PENDING | |

## Claim Reconciliation Summary
claim reconciliation control. Pointer-only claim/evidence comparison.
| Claim | Evidence pointer | Runtime evidence | Production evidence | Result |
|---|---|---|---|---|

## Current-State Execution Controls
| Control | Status | Evidence pointer |
|---|---|---|
| Current-state-first read / Accepted-state update required? | PENDING | accepted-state artifacts |

## Invariant / Canonical Value Controls
| Invariant | Expected value | Actual value | Result |
|---|---|---|---|

## Close-Time Carry-Forward Candidate Review
Carry-forward is last resort. Detail belongs in carry-forward/unresolved owner artifacts; this ledger records disposition and approval pointer.
| Candidate | Safe to resolve now? | User/action required? | Disposition | User approval for deferral | Evidence pointer |
|---|---|---|---|---|---|
Allowed dispositions: `AUTO_RESOLVED_NOW`, `USER_RESOLVED_NOW`, `APPROVED_CARRY_FORWARD`, `BLOCKING_UNRESOLVED`, `NO_LONGER_APPLIES`.

## Current-State Source Reading Record
Record source-reading coverage before Design, Implementation, continuation, or close claims.

## Runtime Freshness Reconciliation Record
After each transition or implementation pass, update only canonical source artifacts and derive command-state cache fields from the ledger and command packets. Do not duplicate mutable status in multiple narrative sections. Current-state and delivery pointers are refreshed only at governed transition/close boundaries or explicitly labeled ACTIVE / PROPOSED before close.

## Implementation-Unit Instantiation Timing Record
When IU mode is active, record whether full IU artifacts were created before material code changes; retrospective IU creation requires an explicit correction and reconciliation before completion claims.

## PROD-L8.19 Command Legality and Correction Ledger Concordance
### Idle Continue Legality Record
If `SESSION_STATE.json.status = idle`, `hirmos continue` fails closed, performs no project/artifact mutation, and recommends `hirmos start`.
### IU Pre-Execution Authority Record
In active IU mode, sealed contract sections of target `IU-xx.md` are execution authority; `SESSION_SCOPE.md` preview prose alone is insufficient.
### Material Correction Command Ledger
| Seq | user command/trigger | prior state | correction type | reason | files/artifacts changed | evidence pointer | result |
|---:|---|---|---|---|---|---|---|

## PROD-L8.21 IU Set Authority Checkpoint
Before material edits, IU-mode sessions must record set-level execution authority: IU mode; implementation shape; source phase/session authority; IU files created before material edits; non-placeholder review; scope coverage; uncovered items; sequencing/dependencies; authorization decision `IMPLEMENTATION_AUTHORIZED` / `BLOCKED` / `LIGHTWEIGHT_NO_IU`; first material edit allowed; timing evidence. IU Set Coverage Map: source scope item → source artifact → IU file(s) → coverage status → notes.

## PROD-L8.22 Session / Phase / Delivery Review Gate Ledger
Append one concise Review boundary row per session, phase, or delivery review gate: boundary, source authority, evidence reviewed, actual codebase reviewed (`YES`/`NO`/`NOT_APPLICABLE`), scope/integration result, runtime/production posture, final result (`PASS`/`PARTIAL`/`BLOCKED`/`FAILED`), and what is not claimed.

## PROD-L8.23 Generated-Run IU Enforcement Checkpoint
Generated IU-mode sessions must include a current `PROD-L8.21 IU Set Authority Checkpoint` before material edits with `Authorization decision: IMPLEMENTATION_AUTHORIZED` / `BLOCKED` / `LIGHTWEIGHT_NO_IU`, `IU files created before material edits: YES`, `Non-placeholder IU review: PASS`, `IU Set Coverage Map`, and timing evidence.

## PROD-L8.24 Pre-Execution Ledger Enforcement
Required active-ledger marker: **Pre-Material-Edit Ledger Row** with timestamp, session id, source authority, IU files verified, `IU Set Authority Checkpoint present: YES`, `Authorization decision: IMPLEMENTATION_AUTHORIZED`, `Material implementation started: NO`, `First material-edit command/event: NOT_STARTED`, `Retrospective checkpoint or IU expansion: NO`; `Retrospective sealed-contract mutation: NO`, and evidence paths. Add a **Material Edit Start Record** later than the pre-edit row.

## PROD-L8.25 Sealed IU Contract / Append-Only Record Boundary
When IU mode is active, record before material edits: target IU files, contract sections sealed, append-only sections available, first material edit not started, and `LLM Write Permission:` lines present.

## PROD-L8.26 Delivery Close Simplification Control
Record pointer-only controls: delivery close posture updated; delivery unresolved register reconciled live-only; current-state navigation updated/verified; Runtime evidence claim scope; production evidence claim scope; overclaims downgraded; archive/session-state normalization and timestamp chronology reviewed.

## PROD-L8.27 Pre-Archive Validation / Archive Immutability Control
Record before archive: pre-archive validation gate run on active artifacts; active validation result; active fixes applied before archive only; archive snapshot created after validation decision; Historical archive mutation after snapshot; failure class (`ACTIVE_FIXABLE` / `ARCHIVE_TRANSACTION_REPAIRABLE` / `ARCHIVE_HISTORICAL_IMMUTABLE`).

## PROD-L8.28 Generated IU Instantiation / Active Close Concordance Control
Record before archive when IU mode is active: full generated IU sealed contract sections and `LLM Write Permission:` lines before execution; append-only Execution Record; append-only Unit Review; no applicable IU remains `Execution status: NOT_STARTED` or `Review status: PENDING` while implementation completion is claimed.

## PROD-L8.30A Bootstrap / IU Action-Gate Control
Every session must write the full 16-answer bootstrap quiz in `bootstrap/BOOTSTRAP_REPORT.md`; prior bootstrap answers, chat memory, compressed summaries, and `see previous session` references are invalid substitutes. Record `Active generated-artifact validation result: PASS | FAIL | BLOCKED | NOT_RUN` before any `implementation_complete`, `Ready to close`, phase acceptance, or delivery acceptance claim. False clean-seal claim guard: if code preceded IU seal, do not claim clean pre-edit seal.

## PROD-L8.31 Generated-Run Mechanical Gate Record
Complete before implementation-complete, ready-to-close, phase/delivery acceptance, archive, or final close output.
| Gate | Value |
|---|---|
| Full bootstrap answers freshly written from durable sources | YES / NO |
| IU mode / IU planned | YES / NO / LIGHTWEIGHT_NO_IU |
| Planned IU count / actual full IU files | / |
| Planned IU count matches actual full IU files | YES / NO / NOT_APPLICABLE |
| Thin or placeholder IU files detected | YES / NO / NOT_APPLICABLE |
| Pre-material-edit IU authority exists | YES / NO / NOT_APPLICABLE |
| Active generated-artifact validation result | PASS / FAIL / BLOCKED / NOT_RUN |
| Carry-forward approvals verified for every `APPROVED_CARRY_FORWARD` | YES / NO / NOT_APPLICABLE |
| Current-state and delivery pointers refreshed | YES / NO / NOT_APPLICABLE |
| Mechanical gate decision: PASS / FAIL / BLOCKED | |
| If not PASS, lifecycle claim allowed | NO |
| Failure summary / route-back | |
Rule: no lifecycle completion, acceptance, archive, or clean close claim is allowed unless this record is PASS and supporting artifacts agree with it.

## Optional Conditional Notes
Use this only when a separate `REQUIREMENTS.md` authority exists: record pointer to the requirement authority and do not duplicate requirements here.

## Legacy Section Mapping / Preserved Static Markers
Static marker ownership is indexed in the Gate Marker Map above. Continuation pass append requirements: assign next pass number, preserve previous rows, update machine state, and surface exactly one legal next governed command.

## Beyond Clear Specs Application
This ledger applies the execution-control subset of `_hirmos/core/authority/BEYOND_CLEAR_SPECS.md`: clear execution controls for each lifecycle boundary, strict local self-validation before surfacing readiness, and fail-closed behavior when the ledger or owning artifacts do not support the claim.

## PROD-L8.10 Delivery-Baseline Session Surface Minimality Record
Session unresolved register: during `delivery_baseline`, `_hirmos/session/unresolved-items.md` is `NOT_APPLICABLE`; delivery unresolved details belong under `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`.

## PROD-L8.11 Delivery-Baseline Optional Authority Location
During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`; optional authority belongs in delivery artifacts or remains in `DELIVERY_SCOPE.md`.

## PROD-L8.13 Delivery Review Wording Record
Status-aware delivery review wording and current-state-first routing explanation must be recorded by pointer, not duplicated as broad narrative.

## Preserved IU Minimum Content Marker
Minimum IU content standard: independently reviewable, failure-contained, mapped to source scope, sequenced/dependency-aware when needed, covering adopted scope without hidden gaps, and carrying explicit `LLM Write Permission:` lines for sealed contract and append-only record sections.

## False Clean-Seal Claim Guard
If project files changed before IU contracts were sealed, record a governance deviation and do not make a false clean-seal claim.

## PROD-L8.32L Artifact Instantiation Boundary

Artifact creation is an event, not a default scaffold obligation. Record a row here only when an artifact is actually created, becomes applicable, or is intentionally absent because it is not applicable.

| Artifact / index | Owning concern | Applicability trigger | Created now? | Derived from | Source-of-truth status | Notes |
|---|---|---|---:|---|---|---|
| `_hirmos/session/EVIDENCE.md` | evidence detail | nontrivial evidence / claim reconciliation / close handoff | YES / NO / NOT_APPLICABLE | ledger/IU evidence pointers | source / derived / absent-valid | |
| `_hirmos/session/unresolved-items.md` | session unresolved details | unresolved items exist or boundary requires direct register review | YES / NO / NOT_APPLICABLE | producer contributions / checkpoint feed | source / absent-valid | |
| `_hirmos/session/REQUIREMENTS.md` | optional session requirements authority | separately justified after session scope is active | YES / NO / NOT_APPLICABLE | SESSION_SCOPE.md authority basis | source / absent-valid | |
| `_hirmos/session/DESIGN.md` | optional session design authority | separately justified after session scope is active | YES / NO / NOT_APPLICABLE | SESSION_SCOPE.md design decisions | source / absent-valid | |
| implementation-unit files | IU authority | IU planning after accepted session baseline | YES / NO / NOT_APPLICABLE | SESSION_SCOPE.md IU pointers | source / absent-valid | |

Absence is valid only when the row records `NOT_APPLICABLE` or when the active runtime boundary does not require the artifact. Do not create empty future synchronization obligations.


## PROD-L8.32Q Archive-State Semantics

In an active session, machine command-state concordance records the current active command state. In an archived session, pre-close active state must be explicitly labeled pre-close and tied to `PRE_CLOSE_SESSION_STATE.json`; post-close archived state must be recorded separately. A current-looking active/implementation-complete row inside an archived ledger is invalid unless explicitly marked historical/pre-close.
