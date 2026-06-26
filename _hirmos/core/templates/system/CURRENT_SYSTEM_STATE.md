# Current System State

> Accepted-State Artifact Invariants:
> - This file is part of durable accepted state.
> - Preserve this invariant block during Update System State.
> - Do not replace this file with a chat summary or session-local artifact.
> - Use canonical runtime posture values from `RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.
> - Use canonical evidence states from `EVIDENCE.md` claim reconciliation.
> - Keep accepted-state decision classifications separate from evidence status.

Status: durable accepted-state navigation authority.
Purpose: canonical accepted current truth, accepted-state navigation, active governance pointers, latest-close metadata, and chronological source-artifact traceability for HIRMOS-governed work.

This file is updated only by governed Update System State / normal close. It is an index-first current-state authority: it records current navigation, concise accepted-state summaries, and source artifact pointers. It is not a cumulative requirements catalog, full design document, system-scope substitute, session log, delivery scope, evidence record, or archive manifest.

Detailed source authority remains in delivery, phase, session, implementation, evidence, unresolved-item, and archive artifacts referenced below.

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

This is the canonical pointer surface for current accepted-state navigation. It records active and recommended governance pointers only; it must not duplicate delivery scope, phase scope, session scope, requirements, design, unresolved-item details, implementation details, evidence, or archive content.

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
- If a delivery is accepted, superseded, blocked, deferred, cancelled, or replaced at close, Update System State must update last/active/next delivery pointers or explicitly record why they are unchanged.
- If a delivery is accepted and `DELIVERY_PLAN.md` contains a planned follow-up delivery whose relationship follows or depends on that accepted delivery, record `Next recommended delivery` and `Next recommended delivery scope`, or explicitly record why no next delivery is recommended.
- If a phase is accepted, superseded, blocked, or replaced at close, Update System State must update these pointers or explicitly record why they are unchanged.
- If delivery governance is not active, record `NO` or `NOT_APPLICABLE`; do not leave stale delivery or phase pointers from a prior delivery.
- `hirmos status` must read this section before reporting active/next delivery work.

## 3. Accepted-State Navigation and Latest Close

This section is part of `CURRENT_SYSTEM_STATE.md` so accepted-state navigation, latest-close metadata, and current truth cannot drift across separate files.

### Accepted-State Files

| Artifact | Purpose | Required | Last updated by session |
|---|---|---:|---|
| `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | Accepted-state navigation authority, current governance pointers, concise current-state summary, Work History Ledger, Source Artifact Index, and latest-close metadata | yes | |
| `_hirmos/system/accepted-state/CARRY_FORWARD.md` | Active unresolved / future-session obligations only | yes | |
| `_hirmos/system/accepted-state/DECISION_LOG.md` | Conditional durable accepted/rejected/superseded decision support when explicit decision-log governance is active | conditional | |

No default root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md`, `DECISIONS.md`, or `ACCEPTED_CHANGES.md` is created. Detailed requirements, design, and scope source authority remains at delivery, phase, session, implementation, evidence, unresolved-item, and archive levels.

### Latest Accepted Close

- Session ID:
- Archive path:
- Archive manifest:
- Close date:
- Current system state version:
- Accepted outcomes summary:
- Post-close state consistency: unknown
- Archive manifest concordance: unknown

### Future Session Starting Notes

Future sessions must read `CURRENT_SYSTEM_STATE.md` before treating archived session history, chat transcripts, summaries, or generated reports as current truth. They must then follow the Current-State-First Navigation Spine to the active and materially relevant source artifacts before material design, implementation, continuation, or close decisions.

### Current-State-First Navigation Spine

Mandatory spine:

- Current Governance Context
- Accepted-State Navigation and Latest Close
- Work History Ledger
- Source Artifact Index
- Active carry-forward pointer / carry-forward summary
- Next governed command / next recommended work

This file is source-complete, not content-complete: it points to canonical requirements, design, scope, evidence, unresolved-item, and archive authorities without duplicating their full content.

## 4. Accepted State Summary

This section is a concise navigation summary only. It is not the complete requirements, design, scope, implementation, evidence, or decision authority. Detailed source authority remains in the delivery, phase, session, implementation, evidence, unresolved-item, and archive artifacts referenced in the Work History Ledger and Source Artifact Index.

### Accepted product / system orientation

### Accepted capabilities summary

### Accepted boundaries summary

### Important accepted constraints summary

### Evidence and validation posture summary

### Product State

#### Accepted product scope summary

#### Accepted roles / actors summary

#### Accepted workflows summary

#### Accepted MVP boundaries summary

#### Explicitly out of scope summary

## 5. Work History Ledger

This chronological ledger records governed HIRMOS work outcomes and source authority paths. It is the durable traceability index for delivery, phase, session, implementation, correction, close, and material single-session work. It is not a command log and must not duplicate full requirements, design, scope, implementation, evidence, or archive content.

| Date | Work ID | Type | Status | Authority | Source Artifacts | Accepted Output / Result |
|---|---|---|---|---|---|---|
| | | delivery baseline / phase-session baseline / single-session / implementation / correction / close | proposed / active / completed / deferred / blocked / cancelled / superseded / history-only | path or not applicable | paths | concise result and source pointer |

Ledger rules:

- Add or update one ledger row for each governed work outcome at normal close.
- Track delivery baseline sessions, phase/session baseline sessions, single-session work, implementation sessions, correction sessions, completed deliveries, and material deferred/cancelled/superseded work.
- Do not add routine `hirmos status` rows unless the command materially changes accepted state.
- Requirements, design, and scope discovery are traced by source artifact path, not copied into this file as a cumulative catalog.
- On-demand requirements/design/scope synthesis may be generated from this ledger and source artifacts, but generated synthesis is not source authority unless explicitly adopted under a future governed workflow.

## 6. Source Artifact Index

Use this index to make source requirements, design, scope, unresolved-item, evidence, delivery, phase, session, and archive artifacts discoverable without duplicating their content.

### Delivery Authorities

| Delivery ID | Status | Scope Authority | Optional Requirements Authority | Optional Design Authority | Unresolved Register |
|---|---|---|---|---|---|
| | | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | none / path | none / path | none / path |

### Phase Authorities

| Phase ID | Status | Phase Authority | Parent Delivery | Notes |
|---|---|---|---|---|
| | | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | | |

### Session Authorities

| Session ID | Status | Session Authority | Archive Path | Notes |
|---|---|---|---|---|
| | | active / archived SESSION_SCOPE.md | | |

### Requirement Sources

| Source | Authority level | Status | Notes |
|---|---|---|---|
| | delivery / session / archive / generated synthesis | active / accepted / archived / superseded / not source authority | |

### Design Sources

| Source | Authority level | Status | Notes |
|---|---|---|---|
| | delivery / session / archive / generated synthesis | active / accepted / archived / superseded / not source authority | |

### Evidence Sources

| Source | Authority level | Status | Notes |
|---|---|---|---|
| | session / implementation-unit / archive | active / accepted / archived / superseded | |

## 7. Delivery State

### Active Development Context and Delivery Pointers

This is the canonical pointer surface for durable delivery governance. It records only pointers and current delivery navigation. It must not duplicate the Delivery Plan, Delivery Scope, Phase scope, or session-local scope content.

| Delivery Unit / Phase | Status | Accepted scope | Evidence / archive | Notes |
|---|---|---|---|---|

### Current active or next recommended delivery

- Delivery:
- Delivery scope:
- Rationale:
- Required next command/action:

## 8. Implementation State

| Capability / area | Current accepted implementation state | Evidence / archive | Limitations |
|---|---|---|---|

### Rejected / not-applied implementation outcomes

## 9. Technical / Architecture State

### Stack

### Architecture summary

### Data model state

### Auth / authorization state

### Important accepted technical decisions

Reference durable decisions in conditional `DECISION_LOG.md` only when explicit decision-log governance is active; otherwise keep decision source pointers in the Work History Ledger / Source Artifact Index.

### Superseded technical decisions

## 10. Runtime Integration State

Use canonical posture values from `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` only.

| Area | Current posture | Evidence status | Production recommendation | Blockers / notes |
|---|---|---|---|---|
| Database | | | | |
| Authentication | | | | |
| Email | | | | |
| SMS | | | | |
| Storage | | | | |
| Deployment / hosting | | | | |

## 11. Evidence State

Use canonical evidence states from `_hirmos/core/protocol/CLAIM_RECONCILIATION.md` only.

| Evidence area | Current evidence state | Latest source | Limitations / not verified |
|---|---|---|---|
| Build | | | |
| Tests | | | |
| Lint / typecheck | | | |
| Local technical setup | | | |
| Role workflow smoke checks | | | |
| User environment verification | | | |
| Production readiness verification | | | |

## 12. Production Readiness State

Keep these tracks separate. Do not collapse planning into readiness.

| Track | Current state | Evidence / decision | Blockers / next action |
|---|---|---|---|
| Production readiness planning | | | |
| Production provider readiness | | | |
| Production deployment readiness | | | |
| Compliance / legal / operational readiness | | | |
| Go-live approval | | | |

## 13. Unresolved / Carry-Forward State

Summarize active carry-forward items. Canonical active item details live in `CARRY_FORWARD.md`.

| Item | Type | Owner | Future-session instruction | Source |
|---|---|---|---|---|

## 14. History / Traceability / Merge Notes

Record only the latest merge note for current readability. Full chronological navigation belongs in the Work History Ledger. Full detailed history remains in session archives and source artifacts.

- Last merge summary:
- Sections updated:
- Claims downgraded or rejected:
- Carry-forward changes:

## Canonical Runtime and Evidence Value Rules

Runtime posture fields must use only:

```text
DEMO_FIXTURE
INTEGRATION_BOUNDARY
LOCAL_REAL_INTEGRATION
PRODUCTION_PROVIDER_INTEGRATION
BLOCKED_PENDING_DECISION_OR_CREDENTIALS
NOT_APPLICABLE
```

Evidence state fields must use only:

```text
NOT_CLAIMED
NOT_RUN
CLAIMED_NOT_LOGGED
LOGGED_COMMAND_PASSED
LOGGED_COMMAND_FAILED
LOCAL_RUNTIME_VERIFIED
USER_ENVIRONMENT_VERIFIED
PRODUCTION_READINESS_VERIFIED
BLOCKED
NOT_APPLICABLE
```

Do not use shorthand values such as `observed`, `build pass`, `LOCAL_REAL`, `ACCEPTED_AT_CLOSE`, or `NOT_IMPLEMENTED` in posture/evidence/status fields. Put nuance in source/rationale/limitations fields.

## Cross-Run Lessons Applied

Use this section when accepted state incorporates lessons from multiple candidate implementations, prototypes, generated apps, external spec-tool outputs, UX drafts, or prior self-runs.

| Lesson source | Accepted lesson | Applied to | Requirement / DU reference | Evidence / decision reference |
|---|---|---|---|---|
| | | requirements / design / implementation / UX / test / package / carry-forward | | |

This section summarizes accepted lessons only. Rejected or deferred lessons belong in conditional `DECISION_LOG.md` when explicit governance is active, or in `CARRY_FORWARD.md` when they are active obligations.

### Close-Time Delivery Pointer Refresh Rule

When a session closes delivery-governed work, this pointer section must be refreshed from the accepted close transaction, not copied from stale pre-close state.

Required refresh inputs:

- `SESSION_EXECUTION.md` close/update control pointers Close-Time Delivery / Phase Status Transaction;
- parent `DELIVERY_PLAN.md` roadmap/register Delivery Status Update Log and `DELIVERY_SCOPE.md` close verification;
- adopted `PHASE-xx.md` Close-Time Phase Status Update;
- session `ARCHIVE_MANIFEST.md` and `SESSION_SCOPE.md` close-verification verdict.
- Current System State delivery pointers refreshed or explicitly verified unchanged.

If no pointer value changed, record that the value was explicitly verified unchanged. Missing or stale delivery pointers block normal close.

## Phase Progress Pointer Rule

When a multi-session phase closes as `PARTIAL`, `BLOCKED`, or `DEFERRED`, Current System State must point to the still-active phase, the next phase, or the explicit carry-forward target. It must not imply that the Delivery Plan or project is complete when phase carry-forward obligations remain.

## Phase Acceptance Pointer Rule

When a phase becomes `ACCEPTED`, Current System State must update active delivery pointers so the accepted phase is recorded as the last accepted phase, the next recommended phase is explicit, and no stale active phase pointer implies more work remains in the accepted phase unless an amendment or new phase is opened.

## Phase Lifecycle Status Pointer Rule

`hirmos status` must read this accepted-state pointer section before reporting active delivery work and must surface a Phase Lifecycle Status Report with phase lifecycle status, phase type, Phase Entry Gate status, Phase Progress Ledger status, Carry-Forward Items status, Phase Acceptance Evidence Gate status, pointer concordance, blocked controls, and exactly one recommended next command.

Current System State must remain pointer-only: it may point to Delivery Plan, Phase, archive, and evidence locations, but must not duplicate the detailed phase scope or acceptance evidence.

## Archive Manifest Concordance Rule

`CURRENT_SYSTEM_STATE.md` must agree with the latest session `ARCHIVE_MANIFEST.md` before future sessions treat the latest close as accepted current truth. The archive manifest is history-only evidence; it supports accepted-state concordance but does not replace this file.

Required concordance fields:

- latest accepted session id;
- latest archive path;
- accepted outcomes applied or explicitly rejected/not applied;
- active carry-forward items copied to `CARRY_FORWARD.md`;
- durable delivery pointers refreshed or explicitly verified unchanged;
- archived `SESSION_STATE.json` normalized to terminal history state;
- active `_hirmos/session/SESSION_STATE.json` reset to idle.

## Update Contract: Active Navigation vs Close Outcomes

Active navigation pointers may be refreshed during governed `hirmos start` / `hirmos continue` transitions when active delivery, phase, session, unresolved-register, or next-command pointers change. These pointer updates do not by themselves claim accepted completion.

Accepted-state outcome rows, latest accepted close metadata, final Work History Ledger outcomes, accepted-state summary changes, and archive concordance are updated during `hirmos close`.

## PROD-L8.19 Transition / Close Chronology Note

Active navigation pointers may change during governed transitions such as delivery acceptance, phase instantiation, session-baseline creation, and correction-session start. Accepted-state summaries, Work History Ledger outcome rows, latest-close metadata, and completed/accepted history are updated at close.

Current-state navigation must preserve chronology:

- active pointers reflect the latest governed transition;
- Work History Ledger outcome rows reflect closed/completed governed work;
- if active/proposed rows are recorded before close, label them ACTIVE / PROPOSED, not accepted;
- archive/session timestamps must be monotonic by governed session sequence unless an explicit exception is recorded.

## PROD-L8.21 Source Artifact Index Placeholder Rule

The Source Artifact Index must avoid blank placeholder rows. For each inactive optional source class, use explicit values such as `none`, `not separately created`, `not yet created`, `not evaluated`, or a concrete source path.

Blank cells are not valid current-state navigation because future sessions cannot distinguish missing information from intentionally absent source authority.


## PROD-L8.23 Generated Source Index Concordance
Generated Source Artifact Index rows must not be blank placeholders. Use concrete paths, `none`, `not separately created`, `not evaluated`, or `not yet created`. Blank requirement/design/evidence source rows are stale navigation surfaces.
