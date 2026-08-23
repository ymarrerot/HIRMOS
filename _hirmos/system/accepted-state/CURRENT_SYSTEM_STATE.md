# Current System State

> Accepted-State Artifact Invariants:
> - This file is part of durable accepted state.
> - Preserve this invariant block during Update System State.
> - Do not replace this file with a chat summary or session-local artifact.
> - Use canonical runtime posture values from `RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.
> - Use canonical evidence states from `EVIDENCE.md` claim reconciliation.
> - Keep accepted-state decision classifications separate from evidence status.

Status: durable accepted-state navigation authority.
Purpose: pointer-first accepted current truth, active governance pointers, latest-close metadata, compact accepted-state summaries, and source-artifact traceability for HIRMOS-governed work.

`CURRENT_SYSTEM_STATE.md` is pointer-complete, not content-complete. It must not duplicate delivery scope, phase scope, session scope, requirements, design, implementation, evidence detail, unresolved-item detail, archive content, or session logs. Detailed source authority remains in the source artifacts referenced here.

## 1. Current State Header

| Field | Value |
|---|---|
| System / project | |
| State version | 0 |
| Last updated by session | |
| Last accepted close archive | |
| Last update date | |
| Current-state evidence basis | source artifacts listed in Work History Ledger / Source Artifact Index |
| Project-type evidence, if relevant | current-state evidence metadata only; not primary routing authority |
| Active stack / stack contexts | |
| Current confidence | unknown |

## 2. Current Governance Context

This is the canonical pointer surface for current accepted-state navigation. It records active and recommended governance pointers only.

| Field | Value | Source / evidence |
|---|---|---|
| Delivery governance active | YES / NO / UNCERTAIN / NOT_APPLICABLE | |
| Active delivery ID | none / `<delivery-id>` | |
| Delivery roadmap | none / `_hirmos/system/delivery/DELIVERY_PLAN.md` | |
| Active delivery scope | none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | |
| Active phase | none / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | |
| Active phase lifecycle status | NOT_STARTED / READY_FOR_ADOPTION / ACTIVE / BLOCKED / PARTIAL / READY_FOR_ACCEPTANCE / ACCEPTED / DEFERRED / SUPERSEDED / CANCELLED / NOT_APPLICABLE | |
| Active phase type | GREENFIELD / BROWNFIELD / MIXED / UNKNOWN / NOT_APPLICABLE | evidence metadata only |
| Active session scope | none / `_hirmos/session/SESSION_SCOPE.md` | |
| Delivery unresolved register | none / `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` | |
| Session unresolved register | none / `_hirmos/session/unresolved-items.md` | |
| Last accepted delivery | none / `<delivery-id>` | |
| Last accepted phase | none / `<phase-id>` | |
| Last accepted session/archive | none / `<archive path>` | |
| Next recommended delivery | none / `<delivery-id>` | |
| Next recommended delivery scope | none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | |
| Next recommended phase | none / `<phase-id>` | |
| Next governed command | `hirmos start` / `hirmos status` / `hirmos continue` / `hirmos close` / none | |

Canonical literal pointer labels for validator/status checks:

```text
Delivery roadmap: none / `_hirmos/system/delivery/DELIVERY_PLAN.md`
Active delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
Active phase: none / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
Active session scope: none / `_hirmos/session/SESSION_SCOPE.md`
Next recommended delivery: none / `<delivery-id>`
Next recommended delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
Archive manifest concordance: unknown / PASS / PARTIAL / BLOCKED
```

Rejected pointer labels for validator/status checks:

```text
Active delivery: none | <delivery-id>
Delivery roadmap: none | _hirmos/system/delivery/DELIVERY_PLAN.md
Active delivery scope: none | _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
Active phase: none | _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

Pointer update rules:

 Phase Lifecycle Pointer Rule:

- Active phase lifecycle status must use the canonical phase lifecycle vocabulary.
- Active phase type must be GREENFIELD, BROWNFIELD, MIXED, UNKNOWN, or NOT_APPLICABLE.
- UNKNOWN phase type must not support implementation readiness.
- Current System State pointers must agree with the durable Delivery Plan row and adopted PHASE-xx.md file.
- If the selected delivery shape requires durable delivery artifacts, this section must point to the durable Delivery Plan and active Phase before the next implementation-capable session claims readiness.
- If a delivery or phase is accepted, superseded, blocked, deferred, cancelled, or replaced at close, update last/active/next pointers or explicitly record unchanged verification.
- If delivery governance is not active, record `NO` or `NOT_APPLICABLE`; do not leave stale delivery or phase pointers.
- `hirmos status` must read this section before reporting active/next delivery work.

Follow-up command guidance:

- When no active session exists, `hirmos continue` is not applicable.
- Optional follow-up work should use `hirmos start "<bounded follow-up objective>"` only when grounded in approved carry-forward or separately scoped new work.
- Do not push safe in-scope close-time checks to a new `hirmos start`; close-time carry-forward triage must first auto-resolve safe candidates or surface user-needed candidates before final close.

## 3. Accepted-State Navigation and Latest Close

This section is part of `CURRENT_SYSTEM_STATE.md` so accepted-state navigation, latest-close metadata, and current truth cannot drift across separate files.

### Accepted-State Files

| Artifact | Purpose | Required | Last updated by session |
|---|---|---:|---|
| `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | Accepted-state navigation authority, current governance pointers, concise current-state summary, Work History Ledger, Source Artifact Index, and latest-close metadata | yes | |
| `_hirmos/system/accepted-state/CARRY_FORWARD.md` | Active unresolved / future-session obligations only | yes | |
| `_hirmos/system/accepted-state/DECISION_LOG.md` | Conditional durable accepted/rejected/superseded decision support when explicit decision-log governance is active | conditional | |

No default root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md`, `DECISIONS.md`, or `ACCEPTED_CHANGES.md` is created.

### Latest Accepted Close

| Field | Value |
|---|---|
| Session ID | |
| Archive path | |
| Archive manifest | |
| Close date | |
| Current system state version | |
| Accepted outcomes summary | |
| Post-close state consistency | unknown |
| Archive manifest concordance | unknown / PASS / PARTIAL / BLOCKED |

### Future Session Starting Notes

Future sessions must read `CURRENT_SYSTEM_STATE.md` before treating archived session history, chat transcripts, summaries, or generated reports as current truth. They must follow the Current-State-First Navigation Spine to active and materially relevant source artifacts before design, implementation, continuation, or close.

### Current-State-First Navigation Spine

- Current Governance Context
- Accepted-State Navigation and Latest Close
- Work History Ledger
- Source Artifact Index
- Active carry-forward pointer / carry-forward summary
- Next governed command / next recommended work

## 4. Accepted State Summary

This section is a concise navigation summary only. It is not the complete requirements, design, scope, implementation, evidence, or decision authority.

| Summary area | Current accepted summary | Source artifact |
|---|---|---|
| Accepted product / system orientation | | |
| Accepted capabilities summary | | |
| Accepted boundaries summary | | |
| Important accepted constraints summary | | |
| Evidence and validation posture summary | | |
| Product State | | |
| Accepted product scope summary | | |
| Accepted roles / actors summary | | |
| Accepted workflows summary | | |
| Accepted MVP boundaries summary | | |
| Explicitly out of scope summary | | |

## 5. Work History Ledger

This chronological ledger records governed HIRMOS work outcomes and source authority paths. It is not a command log and must not duplicate full requirements, design, scope, implementation, evidence, or archive content.

| Date | Work ID | Type | Status | Authority | Source Artifacts | Accepted Output / Result |
|---|---|---|---|---|---|---|
| | | delivery baseline / phase-session baseline / single-session / implementation / correction / close | proposed / active / completed / deferred / blocked / cancelled / superseded / history-only | path or not applicable | paths | concise result and source pointer |

Ledger rules: add/update one row per governed work outcome at close; trace source artifact paths; do not log routine status commands; generated synthesis is not authority unless explicitly adopted.

## 6. Source Artifact Index

Use this index to make source requirements, design, scope, unresolved-item, evidence, delivery, phase, session, and archive artifacts discoverable without duplicating content.

| Class | ID / name | Status | Source path | Notes |
|---|---|---|---|---|
| Delivery Authorities | none | not yet created | none | no active delivery |
| Phase Authorities | none | not yet created | none | no active phase |
| Session Authorities | none | idle | none | no active session scope |
| Requirement Sources | none | not separately created | none | no separate requirements source yet |
| Design Sources | none | not separately created | none | no separate design source yet |
| Evidence Sources | none | not evaluated | none | no evidence source yet |
| Archive Sources | none | not yet created | none | no archive source yet |

## 7. Delivery State

### Active Development Context and Delivery Pointers

| Field | Value | Source |
|---|---|---|
| Delivery governance active | YES / NO / UNCERTAIN / NOT_APPLICABLE | |
| Delivery roadmap | none / `_hirmos/system/delivery/DELIVERY_PLAN.md` | |
| Active delivery scope | none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | |
| Active phase | none / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | |
| Active phase lifecycle status | NOT_STARTED / READY_FOR_ADOPTION / ACTIVE / BLOCKED / PARTIAL / READY_FOR_ACCEPTANCE / ACCEPTED / DEFERRED / SUPERSEDED / CANCELLED / NOT_APPLICABLE | |
| Active phase type | GREENFIELD / BROWNFIELD / MIXED / UNKNOWN / NOT_APPLICABLE | |
| Next recommended delivery | none / `<delivery-id>` | |
| Next recommended delivery scope | none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | |
| Next recommended phase | none / `<phase-id>` | |
| Pointer consistency result | unknown / PASS / PARTIAL / BLOCKED | |

## 8. Implementation State

| Area | Current accepted state | Source | Notes |
|---|---|---|---|
| Implemented capabilities | | | |
| Rejected / not-applied implementation outcomes | | | |
| Implementation unit source pointers | none | none | |

## 9. Technical / Architecture State

| Area | Current accepted state | Source |
|---|---|---|
| Stack | | |
| Architecture summary | | |
| Data model state | | |
| Auth / authorization state | | |
| Important accepted technical decisions | | |
| Superseded technical decisions | | |

## 10. Runtime Integration State

| Integration | Runtime posture | Evidence source | Limitations / next action |
|---|---|---|---|
| Database | DEMO_FIXTURE / INTEGRATION_BOUNDARY / LOCAL_REAL_INTEGRATION / PRODUCTION_PROVIDER_INTEGRATION / BLOCKED_PENDING_DECISION_OR_CREDENTIALS / NOT_APPLICABLE | | |
| Authentication | | | |
| Email | | | |
| SMS | | | |
| Storage | | | |
| Deployment / hosting | | | |
| Provider APIs / external services | | | |

## 11. Evidence State

Use canonical evidence states from `_hirmos/core/protocol/CLAIM_RECONCILIATION.md` only. Keep evidence detail in `_hirmos/session/EVIDENCE.md`, IU files, delivery close records, or archives; this section stores current accepted posture and pointers only.

| Evidence area | Current evidence state | Latest source | Limitations / not verified |
|---|---|---|---|
| Build | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | | |
| Tests | | | |
| Lint / typecheck | | | |
| Local technical setup | | | |
| Role workflow smoke checks | | | |
| User environment verification | | | |
| Production readiness verification | | | |

## 12. Production Readiness State

| Track | Current state | Evidence / decision | Blockers / next action |
|---|---|---|---|
| Production readiness planning | | | |
| Production provider readiness | | | |
| Production deployment readiness | | | |
| Compliance / legal / operational readiness | | | |
| Go-live approval | | | |

## 13. Unresolved / Carry-Forward State

Summarize active carry-forward posture only. Canonical active and resolved carry-forward lifecycle details live in `CARRY_FORWARD.md`.

| Item | Type | Owner | Future-session instruction | Source |
|---|---|---|---|---|
| none | none | none | none | none |

## 14. History / Traceability / Merge Notes

Record only the latest merge note for readability. Full detail remains in session archives and source artifacts.

| Field | Value |
|---|---|
| Last merge summary | |
| Sections updated | |
| Claims downgraded or rejected | |
| Carry-forward changes | |

## Canonical Runtime and Evidence Value Rules

Runtime posture fields must use only: `DEMO_FIXTURE`, `INTEGRATION_BOUNDARY`, `LOCAL_REAL_INTEGRATION`, `PRODUCTION_PROVIDER_INTEGRATION`, `BLOCKED_PENDING_DECISION_OR_CREDENTIALS`, `NOT_APPLICABLE`.

Evidence state fields must use only: `NOT_CLAIMED`, `NOT_RUN`, `CLAIMED_NOT_LOGGED`, `LOGGED_COMMAND_PASSED`, `LOGGED_COMMAND_FAILED`, `LOCAL_RUNTIME_VERIFIED`, `USER_ENVIRONMENT_VERIFIED`, `PRODUCTION_READINESS_VERIFIED`, `BLOCKED`, `NOT_APPLICABLE`.

Do not use shorthand values such as `observed`, `build pass`, `LOCAL_REAL`, `ACCEPTED_AT_CLOSE`, or `NOT_IMPLEMENTED` in posture/evidence/status fields. Put nuance in source/rationale/limitations fields.

## Cross-Run Lessons Applied

| Lesson source | Accepted lesson | Applied to | Requirement / DU reference | Evidence / decision reference |
|---|---|---|---|---|
| | | requirements / design / implementation / UX / test / package / carry-forward | | |

Rejected or deferred lessons belong in conditional `DECISION_LOG.md` when explicit governance is active, or in `CARRY_FORWARD.md` when they are active obligations.

### Close-Time Delivery Pointer Refresh Rule

When a session closes delivery-governed work, this pointer section must be refreshed from the accepted close transaction, not copied from stale pre-close state.

Required refresh inputs: `SESSION_LEDGER.md` close/update control pointers Close-Time Delivery / Phase Pointer Refresh; parent `DELIVERY_PLAN.md` roadmap/register Delivery Status Pointer Index and `DELIVERY_SCOPE.md` close verification; adopted `PHASE-xx.md` Close-Time Phase Status Update; session `ARCHIVE_MANIFEST.md`; `SESSION_SCOPE.md` close-verification verdict; Current System State delivery pointers refreshed or explicitly verified unchanged.

If no pointer value changed, record explicit unchanged verification. Missing or stale delivery pointers block normal close.

## Phase Progress Pointer Rule

When a multi-session phase closes as `PARTIAL`, `BLOCKED`, or `DEFERRED`, Current System State must point to the still-active phase, the next phase, or the explicit carry-forward target.

## Phase Acceptance Pointer Rule

When a phase becomes `ACCEPTED`, Current System State must update active delivery pointers so the accepted phase is the last accepted phase, the next recommended phase is explicit, and no stale active phase pointer implies more work remains unless an amendment/new phase opens.

## Phase Lifecycle Status Pointer Rule

`hirmos status` must read this accepted-state pointer section before reporting active delivery work and must surface a Phase Lifecycle Status Report with phase lifecycle status, phase type, Phase Entry Gate status, Phase Progress Pointer Index status, Carry-Forward Items status, Phase Acceptance Evidence Gate status, pointer concordance, blocked controls, and exactly one recommended next command.

Current System State must remain pointer-only: it may point to Delivery Plan, Phase, archive, and evidence locations, but must not duplicate detailed phase scope or acceptance evidence.

## Archive Manifest Concordance Rule

`CURRENT_SYSTEM_STATE.md` must agree with the latest session `ARCHIVE_MANIFEST.md` before future sessions treat the latest close as accepted current truth. The archive manifest is history-only evidence; it supports accepted-state concordance but does not replace this file.

Required concordance fields: latest accepted session id; latest archive path; accepted outcomes applied or explicitly rejected/not applied; active carry-forward items copied to `CARRY_FORWARD.md`; durable delivery pointers refreshed or explicitly verified unchanged; archived `SESSION_STATE.json` normalized to terminal history state; active `_hirmos/session/SESSION_STATE.json` reset to idle.

## Update Contract: Active Navigation vs Close Outcomes

Active navigation pointers may be refreshed during governed `hirmos start` / `hirmos continue` transitions when active delivery, phase, session, unresolved-register, or next-command pointers change. These pointer updates do not by themselves claim accepted completion.

Accepted-state outcome rows, latest accepted close metadata, final Work History Ledger outcomes, accepted-state summary changes, and archive concordance are updated during `hirmos close`.

## PROD-L8.19 Transition / Close Chronology Note

Active navigation pointers may change during governed transitions such as delivery acceptance, phase instantiation, session-baseline creation, and correction-session start. Accepted-state summaries, Work History Ledger outcome rows, latest-close metadata, and completed/accepted history are updated at close. Active/proposed rows recorded before close must be labeled ACTIVE / PROPOSED, not accepted.

## PROD-L8.21 Source Artifact Index Placeholder Rule

The Source Artifact Index must avoid blank placeholder rows. For each inactive optional source class, use explicit values such as `none`, `not separately created`, `not yet created`, `not evaluated`, or a concrete source path. Blank cells are not valid current-state navigation.

## PROD-L8.23 Generated Source Index Concordance

Generated Source Artifact Index rows must not be blank placeholders. Blank requirement/design/evidence source rows are stale navigation surfaces. Use concrete paths, `none`, `not separately created`, `not evaluated`, or `not yet created`.

## PROD-L8.24 Source Artifact Index Runtime Placeholder Guard

Generated `Source Artifact Index` rows must not include empty first cells, empty source-path cells, generic placeholder text, or template instruction rows such as `delivery / session / archive / generated synthesis`. Replace inactive classes with explicit `none`, `not separately created`, `not evaluated`, or concrete artifact paths.

## PROD-L8.26 Accepted-State Navigation Simplification and Evidence Posture

`CURRENT_SYSTEM_STATE.md` is pointer-complete, not evidence-complete. At delivery close, record compact accepted-state navigation and evidence posture without duplicating full delivery, phase, session, IU, or evidence content. Result may be `CLOSED_ACCEPTED`, `CLOSED_PARTIAL`, `BLOCKED`, `FAILED`, `DEFERRED`, or `SUPERSEDED`. Implementation acceptance, local runtime verification, and production verification must remain separate.

If critical-flow, provider, browser, image-generation, database, or production evidence is `NOT_RUN`, `BLOCKED`, or absent, this file must not claim broad `LOCAL_RUNTIME_VERIFIED`, `USER_ENVIRONMENT_VERIFIED`, or `PRODUCTION_READINESS_VERIFIED` for the whole delivery.

## PROD-L8.31 Generated-Run Pointer Concordance Gate

When a generated delivery/session reaches close or partial close, current system state must be refreshed before final output:

- Active development context refreshed: YES / NO / NOT_APPLICABLE
- Delivery pointer concordant with delivery plan/scope: YES / NO / NOT_APPLICABLE
- Active/next phase pointer concordant with durable phase files: YES / NO / NOT_APPLICABLE
- Evidence/carry-forward posture reflected without overclaim: YES / NO / NOT_APPLICABLE
- Generated-run mechanical gate result reflected: YES / NO / NOT_APPLICABLE

Stale or missing delivery/current-state pointers must be reported with other generated-run mechanical failures rather than masking them.
## PROD-L8.32L Derived Pointer Index Contract

Pointer tables in this artifact are navigation caches over canonical source artifacts. They may be generated or refreshed from filesystem paths, active session state, session ledger rows, delivery/phase directories, archive manifests, and carry-forward records. Do not hand-maintain pointer rows as independent truth; stale pointer rows block continuation until reconciled. If a source artifact is absent because its concern is not applicable, record `none` / `not created because not applicable`, not a placeholder path.

Literal rule: source artifacts win over derived pointer caches.


## PROD-L8.32Q Accepted-State Concordance Simplification

Accepted-state navigation must not require duplicated delivery status logs. Current delivery/phase posture is derived from delivery scope close posture, phase acceptance records, session archive manifests, evidence records, and roadmap/status pointer indexes. Stale pointer rows are defects; stale narrative status logs should not be created.


## PROD-L8.33G Carry-forward lifecycle summary rule

`CURRENT_SYSTEM_STATE.md` summarizes carry-forward posture but does not own carry-forward lifecycle truth. Active and resolved carry-forward records live in `_hirmos/system/accepted-state/CARRY_FORWARD.md`. A claim that a carry-forward item is resolved, user-verified, or production-verified must point to the matching resolved row in `CARRY_FORWARD.md`.
