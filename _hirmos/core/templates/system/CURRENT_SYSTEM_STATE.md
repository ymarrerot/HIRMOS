# Current System State

> Accepted-State Artifact Invariants:
> - This file is part of durable accepted state.
> - Preserve this invariant block during Update System State.
> - Do not replace this file with a chat summary or session-local artifact.
> - Use canonical runtime posture values from `RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.
> - Use canonical evidence states from `EVIDENCE.md` claim reconciliation.
> - Keep accepted-state decision classifications separate from evidence status.

Status: durable accepted-state record.
Purpose: canonical merged current truth of the software system for future HIRMOS sessions, including accepted-state navigation and latest-close metadata.

This file is updated only by governed Update System State / normal close. It is merged current truth and accepted-state navigation metadata, not a session log.

## 1. Current State Header

| Field | Value |
|---|---|
| System / project | |
| State version | 0 |
| Last updated by session | |
| Last accepted close archive | |
| Last update date | |
| Project type | |
| Active stack / stack contexts | |
| Current confidence | unknown |


## 2. Accepted-State Navigation and Latest Close

This section is part of `CURRENT_SYSTEM_STATE.md` so accepted-state navigation, latest-close metadata, and current truth cannot drift across separate files.

### Accepted-State Files

| Artifact | Purpose | Required | Last updated by session |
|---|---|---:|---|
| `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | Canonical merged current truth and accepted-state navigation | yes | |
| `_hirmos/system/accepted-state/CARRY_FORWARD.md` | Active unresolved / future-session obligations only | yes | |
| `_hirmos/system/accepted-state/DECISION_LOG.md` | Durable accepted/rejected/superseded decisions | yes | |
| `_hirmos/system/accepted-state/REQUIREMENTS.md` | Accepted requirements catalog and coverage map, when applicable | conditional | |

### Latest Accepted Close

- Session ID:
- Archive path:
- Archive manifest:
- Close date:
- Current system state version:
- Accepted outcomes summary:
- Post-close state consistency: unknown
- Archive manifest concordance: unknown

### Accepted-State Track Summary

| Track | Current summary | Source section / artifact |
|---|---|---|
| Product / MVP scope | | Current System State §3 |
| Delivery completion | | Current System State §4 |
| Local runtime readiness | | Current System State §8 |
| Runtime integration posture | | Current System State §7 |
| Production readiness planning | | Current System State §9 |
| Production provider readiness | | Current System State §9 |
| Compliance / go-live readiness | | Current System State §9 |

### Future Session Starting Notes

Future sessions must read `CURRENT_SYSTEM_STATE.md` before treating archived session history, chat transcripts, summaries, or generated reports as current truth.

## 3. Product State

### Accepted product scope

### Accepted roles / actors

### Accepted workflows

### Accepted MVP boundaries

### Explicitly out of scope

## 4. Delivery State

### Active Development Context and Delivery Pointers

This is the canonical pointer surface for durable delivery governance. It records only pointers and current delivery navigation. It must not duplicate the Delivery Plan, Delivery Scope, Phase contract, or session-local scope content.

| Field | Value | Source / evidence |
|---|---|---|
| Delivery governance active | YES / NO / UNCERTAIN / NOT_APPLICABLE | |
| Active delivery ID | none / `<delivery-id>` | |
| Delivery roadmap | none / `_hirmos/system/delivery/DELIVERY_PLAN.md` | |
| Active delivery scope | none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | |
| Active phase | none / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | |
| Active phase lifecycle status | NOT_STARTED / READY_FOR_ADOPTION / ACTIVE / BLOCKED / PARTIAL / READY_FOR_ACCEPTANCE / ACCEPTED / DEFERRED / SUPERSEDED / CANCELLED / NOT_APPLICABLE | |
| Active phase type | GREENFIELD / BROWNFIELD / MIXED / UNKNOWN / NOT_APPLICABLE | |
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

| Delivery Unit / Phase | Status | Accepted scope | Evidence / archive | Notes |
|---|---|---|---|---|

### Current active or next recommended delivery

- Delivery:
- Delivery scope:
- Rationale:
- Required next command/action:

## 5. Implementation State

| Capability / area | Current accepted implementation state | Evidence / archive | Limitations |
|---|---|---|---|

### Rejected / not-applied implementation outcomes

## 6. Technical / Architecture State

### Stack

### Architecture summary

### Data model state

### Auth / authorization state

### Important accepted technical decisions

Reference durable decisions in `DECISION_LOG.md`.

### Superseded technical decisions

## 7. Runtime Integration State

Use canonical posture values from `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` only.

| Area | Current posture | Evidence status | Production recommendation | Blockers / notes |
|---|---|---|---|---|
| Database | | | | |
| Authentication | | | | |
| Email | | | | |
| SMS | | | | |
| Storage | | | | |
| Deployment / hosting | | | | |

## 8. Evidence State

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

## 9. Production Readiness State

Keep these tracks separate. Do not collapse planning into readiness.

| Track | Current state | Evidence / decision | Blockers / next action |
|---|---|---|---|
| Production readiness planning | | | |
| Production provider readiness | | | |
| Production deployment readiness | | | |
| Compliance / legal / operational readiness | | | |
| Go-live approval | | | |

## 10. Unresolved / Carry-Forward State

Summarize active carry-forward items. Canonical active item details live in `CARRY_FORWARD.md`.

| Item | Type | Owner | Future-session instruction | Source |
|---|---|---|---|---|

## 11. History / Traceability

| Session / archive | Sections changed | Accepted outcomes | Rejected / carried outcomes |
|---|---|---|---|

## Merge Notes

Record only the latest merge note for current readability. Full history remains in session archives and `CURRENT_SYSTEM_STATE.md` History / Traceability.

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

## Requirements Reference

| Field | Value |
|---|---|
| Accepted requirements | `_hirmos/system/accepted-state/REQUIREMENTS.md` |
| Baseline version | `<version or unknown>` |
| Coverage posture | `<summary>` |
| Incomplete / deferred requirements | `<summary or link to CARRY_FORWARD.md>` |

`CURRENT_SYSTEM_STATE.md` summarizes accepted requirements coverage posture, but `REQUIREMENTS.md` remains the requirement catalog and coverage map.

## Cross-Run Lessons Applied

Use this section when accepted state incorporates lessons from multiple candidate implementations, prototypes, generated apps, external spec-tool outputs, UX drafts, or prior self-runs.

| Lesson source | Accepted lesson | Applied to | Requirement / DU reference | Evidence / decision reference |
|---|---|---|---|---|
| | | requirements / design / implementation / UX / test / package / carry-forward | | |

This section summarizes accepted lessons only. Rejected or deferred lessons belong in `DECISION_LOG.md` or `CARRY_FORWARD.md`.


### Close-Time Delivery Pointer Refresh Rule

When a session closes delivery-governed work, this pointer section must be refreshed from the accepted close transaction, not copied from stale pre-close state.

Required refresh inputs:

- `SESSION_EXECUTION.md` close/update control pointers Close-Time Delivery / Phase Status Transaction;
- parent `DELIVERY_PLAN.md` roadmap/register Delivery Status Update Log and `DELIVERY_SCOPE.md` close verification;
- adopted `PHASE-xx.md` Close-Time Phase Status Update Contract;
- session `ARCHIVE_MANIFEST.md` and `SESSION_SCOPE.md` close-verification verdict.
- Current System State delivery pointers refreshed or explicitly verified unchanged.

If no pointer value changed, record that the value was explicitly verified unchanged. Missing or stale delivery pointers block normal close.

## Phase Progress Pointer Rule

When a multi-session phase closes as `PARTIAL`, `BLOCKED`, or `DEFERRED`, Current System State must point to the still-active phase, the next phase, or the explicit carry-forward target. It must not imply that the Delivery Plan or project is complete when phase carry-forward obligations remain.


## Phase Acceptance Pointer Rule

When a phase becomes `ACCEPTED`, Current System State must update active delivery pointers so the accepted phase is recorded as the last accepted phase, the next recommended phase is explicit, and no stale active phase pointer implies more work remains in the accepted phase unless an amendment or new phase is opened.


## Phase Lifecycle Status Pointer Rule

`hirmos status` must read this accepted-state pointer section before reporting active delivery work and must surface a Phase Lifecycle Status Report with phase lifecycle status, phase type, Phase Entry Gate status, Phase Progress Ledger status, Carry-Forward Items status, Phase Acceptance Evidence Gate status, pointer concordance, blocked controls, and exactly one recommended next command.

Current System State must remain pointer-only: it may point to Delivery Plan, Phase, archive, and evidence locations, but must not duplicate the detailed phase contract or acceptance evidence.


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
