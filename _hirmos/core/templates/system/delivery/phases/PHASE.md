# Phase Scope

Delivery ID:
Phase ID:
Phase name:
Lifecycle status: NOT_STARTED | READY_FOR_ADOPTION | ACTIVE | BLOCKED | PARTIAL | READY_FOR_ACCEPTANCE | ACCEPTED | DEFERRED | SUPERSEDED | CANCELLED
Phase type: GREENFIELD | BROWNFIELD | MIXED | UNKNOWN
Last updated from session:

## Authority

This phase file is compact phase authority for one adopted delivery slice. It owns phase boundary, entry/exit gates, progress/carry-forward pointers, acceptance posture, and session handoff. It must not duplicate session scope, IU contracts, code changes, detailed evidence, or delivery close posture.

Source Delivery Scope: `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
Delivery roadmap/register: `_hirmos/system/delivery/DELIVERY_PLAN.md`

## Phase Lifecycle State Model

Canonical statuses: NOT_STARTED, READY_FOR_ADOPTION, ACTIVE, BLOCKED, PARTIAL, READY_FOR_ACCEPTANCE, ACCEPTED, DEFERRED, SUPERSEDED, CANCELLED. `UNKNOWN` phase type blocks implementation readiness.

## Current-State Basis

- Current system state inspected: YES / NO
- Source accepted-state pointer:
- Parent delivery status source: derived from `_hirmos/system/delivery/DELIVERY_PLAN.md`, parent `DELIVERY_SCOPE.md` close posture, archives, and `CURRENT_SYSTEM_STATE.md`; do not maintain a writable parent status value here.
- Prior phase dependency status:
- Active carry-forward / unresolved obligations:

## Phase Objective

- Objective:
- User-visible value:
- Delivery scope IDs covered:
- Primary validation/evidence target:

## Universal Lifecycle Requirements

| Requirement | Status | Source / evidence pointer |
|---|---|---|
| Parent delivery baseline accepted/amended | PENDING / PASS / BLOCKED | |
| Phase entry criteria assessed | PENDING / PASS / BLOCKED | |
| Session adoption needed before implementation | YES / NO | |
| Exit criteria defined | PENDING / PASS / BLOCKED | |
| Evidence expectations defined | PENDING / PASS / BLOCKED | |

## Source Coverage

| Delivery Scope item / requirement / accepted-state need | Covered by this phase? | Evidence / rationale |
|---|---:|---|
| | YES / NO / PARTIAL | |

## Entry Criteria

Entry criteria status: PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE

- Required prior phases:
- Required accepted-state conditions:
- Required unresolved decisions:
- Required runtime/setup conditions:

## Binary Exit Criteria

| Binary Exit Criterion | Evidence required | Status |
|---|---|---|
| | | NOT_ASSESSED |

## Scope Included

Compact index only; implementation detail belongs in `SESSION_SCOPE.md` and IU files.

| Item | Source | Acceptance expectation |
|---|---|---|
| | `DELIVERY_SCOPE.md` / accepted state / user request | |

## Scope Excluded

| Item | Reason excluded | Carry-forward / deferral target |
|---|---|---|
| | | |

## Adoption Constraints

- Allowed adoption lifecycle statuses: READY_FOR_ADOPTION, ACTIVE, PARTIAL.
- Review-only adoption lifecycle status: READY_FOR_ACCEPTANCE.
- Implementation must not adopt NOT_STARTED, BLOCKED, ACCEPTED, DEFERRED, SUPERSEDED, CANCELLED, or UNKNOWN-type phases.
- Session adoption must map phase items to `SESSION_SCOPE.md` and implementation units.
- Phase adoption must preserve the governing `DELIVERY_SCOPE.md` boundaries.

## Greenfield Controls

Required when `Phase type` is `GREENFIELD` or `MIXED`.

- MVP boundary:
- Primary user/workflow slice:
- Prototype vs production intent:
- Architecture dependency status:
- Out-of-scope expansion guard:
- Validation level required:
- Production-readiness claim allowed: YES / NO / PARTIAL

## Brownfield Controls

Required when `Phase type` is `BROWNFIELD` or `MIXED`.

- Accepted-state preservation boundary:
- Regression-sensitive areas:
- Migration / compatibility obligations:
- Existing behavior that must not change:
- Rollback / recovery consideration:
- Validation level required:

## Mixed Phase Rule

A mixed phase must satisfy both Greenfield Controls and Brownfield Controls. If either side is incomplete, the phase cannot be implementation-ready.

## Phase Entry Gate

Entry gate status: PENDING / PASS / BLOCKED / UNCERTAIN
Entry criteria status: PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE
Entry criteria evidence:

### Greenfield Entry Gate Controls

- MVP/slice boundary is explicit.
- Required architecture decisions are recorded in `DELIVERY_SCOPE.md` or `SESSION_SCOPE.md`.
- Validation level is identified.

### Brownfield Entry Gate Controls

- Current accepted state was inspected.
- Preservation constraints are recorded.
- Regression evidence expectations are identified.

## Phase Progress Pointer Index

Pointer-only progress index. Do not maintain a narrative phase progress ledger here. Session chronology lives in `SESSION_LEDGER.md` and archives; detailed evidence lives in `EVIDENCE.md`; IU execution/review lives in IU files.

| Session/archive | Scope/result pointer | Evidence pointer | Remaining-work pointer | Status impact |
|---|---|---|---|---|
| | `_hirmos/system/history/sessions/<session-id>/SESSION_SCOPE.md` or archive manifest | | unresolved/carry-forward pointer | |

## Carry-Forward Enforcement

Carry-forward status: NONE / RECORDED / BLOCKED / NOT_APPLICABLE

- Carry-forward target:
- Revalidation point:
- Blocking unresolved items:

### Greenfield Progress Controls

- Scope expansion checked.
- MVP boundary preserved.

### Brownfield Progress Controls

- Preservation evidence checked.
- Regressions/blockers recorded.

## Phase Acceptance Evidence Gate

Acceptance gate status: PENDING / PASS / BLOCKED / PARTIAL
Phase acceptance evidence status: PENDING / COMPLETE / PARTIAL / BLOCKED / NOT_APPLICABLE

### Greenfield Acceptance Evidence

- Greenfield acceptance evidence: PENDING / COMPLETE / PARTIAL / BLOCKED / NOT_APPLICABLE
- User-visible slice evidence:
- Build/test/smoke evidence:
- Deferred scope:

### Brownfield Acceptance Evidence

- Brownfield acceptance evidence: PENDING / COMPLETE / PARTIAL / BLOCKED / NOT_APPLICABLE
- Preservation evidence:
- Regression evidence:
- Migration evidence when applicable:

### Mixed Acceptance Evidence

- Greenfield evidence result:
- Brownfield evidence result:
- Combined risk decision:

## Session Handoff

- Next recommended session:
- Next recommended phase:
- Required adopted scope:
- Required evidence to inspect:
- Known blockers:

## Close-Time Phase Status Update

During `hirmos close`, update changed status/pointer fields or explicitly verify unchanged. Do not duplicate session/IU/evidence detail.

## Phase Acceptance Review

The phase may be marked `ACCEPTED` only when the Phase Acceptance Evidence Gate is complete and the closed session records accepted outcome, evidence, unresolved/carry-forward disposition, and accepted-state update.

## Close Verification

- Parent `DELIVERY_SCOPE.md` status and phase table agree with this phase status.
- Parent `DELIVERY_PLAN.md` delivery index / active delivery pointer agrees with this delivery status.
- Binary Exit Criterion rows are resolved or carried forward.
- Phase Acceptance Review records the closed session before `ACCEPTED` status is used.

## Carry-Forward Items

Detailed carry-forward detail belongs in accepted-state or delivery unresolved registers; this phase records only phase-relevant target pointers.

- Carry-forward item:
- Target delivery/phase/session:
- Revalidation point:

## Phase Lifecycle Freshness Rule

When implementation starts or completes for this phase, HIRMOS must update lifecycle and pointer fields only. A phase must not remain `READY_FOR_ADOPTION` or say implementation has not started after implementation evidence or IU records exist for adopted phase scope.

| Freshness check | Status | Evidence / pointer |
|---|---|---|
| Phase lifecycle status matches active session state | MATCH / STALE / NOT_CHECKED | |
| Phase Progress Pointer Index reflects current session/archive pointer | MATCH / STALE / NOT_CHECKED | |
| Acceptance evidence gate reflects current evidence level | MATCH / STALE / NOT_CHECKED | |

## PROD-L8.19 Later Verification Update Record

Append current verification updates when later sessions resolve carry-forward, runtime limitation, or evidence gap. The original historical close verdict remains historical.

| Update date/session | Later evidence source | Original limitation / carry-forward | Current verification posture | Phase status impact | Notes |
|---|---|---|---|---|---|
| | | | ACCEPTED / PARTIAL / BLOCKED / HISTORICAL_ONLY | | |

## PROD-L8.21 Close-Time Phase Concordance Sweep

At close, active/current fields must not contradict the final phase status unless rows are explicitly labeled historical; stale not yet closed language must be historicalized or removed.

| Section / field | Current value | Expected close value | Status | Notes |
|---|---|---|---|---|
| Lifecycle status | | ACCEPTED / PARTIAL / BLOCKED / DEFERRED | PENDING | |
| Phase Progress Pointer Index | | current or historical-labeled | PENDING | |
| Binary Exit Criteria | | PASS / PARTIAL / BLOCKED / DEFERRED | PENDING | |
| Phase Acceptance Evidence Gate | | COMPLETE / PARTIAL / BLOCKED / NOT_APPLICABLE | PENDING | |
| Close-Time Phase Status Update | | closed/current or historical-labeled | PENDING | |

## PROD-L8.22 Phase Review Gate

Close-time phase acceptance requires evidence-backed review. Required generated values:

- Reviewed phase:
- Source authority reviewed:
- Session/IU evidence reviewed:
- Actual final codebase reviewed: YES / NO / NOT_APPLICABLE
- Files or areas inspected:
- Unit coverage reviewed: PASS / PARTIAL / BLOCKED / FAILED / NOT_APPLICABLE
- Cross-unit integration reviewed: PASS / PARTIAL / BLOCKED / FAILED / NOT_APPLICABLE
- Scope coverage result: PASS / PARTIAL / BLOCKED / FAILED
- Runtime evidence level: NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE
- Production evidence level: NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE
- Remaining gaps:
- Carry-forward items affecting phase acceptance:
- Final phase review result: PASS / PARTIAL / BLOCKED / FAILED
- Why this result is honest:
- What is not claimed:

## PROD-L8.23 Generated Phase Close Concordance

Generated phase files are stale if current lifecycle status is `ACCEPTED` while current exit/binary criteria remain `PENDING` or `NOT_ASSESSED` outside explicitly historical sections.

## PROD-L8.24 Generated Phase Review Gate Validation

A generated phase with `Lifecycle status: ACCEPTED`, `CLOSED`, or `PARTIAL` must instantiate the phase review gate with concrete values, not leave this template as unused guidance. Close must reconcile stale `PENDING`, `PLANNED`, `READY_FOR_ADOPTION`, `NOT_STARTED`, or `NOT_ASSESSED` sections that contradict the final phase status.

## PROD-L8.32L Derived Phase Progress Index Contract

`PHASE.md` owns phase authority, lifecycle status, entry/exit criteria, and acceptance posture. The Phase Progress Pointer Index is a derived navigation cache over session ledgers, IU files, evidence records, and archive manifests. Do not write a narrative phase progress ledger here.

If the phase progress pointer conflicts with archived session evidence, `SESSION_LEDGER.md`, or `ARCHIVE_MANIFEST.md`, mark the pointer `STALE` or `BLOCKED` and route to reconciliation before implementation-readiness, phase acceptance, or close claims.


## PROD-L8.32Q Parent Delivery Status Simplification

Phase files do not own or mirror current parent delivery lifecycle status. A phase file must point to its parent delivery scope and roadmap only. Parent delivery completion/active posture is derived from the roadmap/register, delivery close posture, accepted-state pointers, and archives.

Generated phase files must not contain `Parent delivery status: ACTIVE` after the parent delivery is complete elsewhere. Reopen every phase at delivery close only for phase-owned acceptance facts; do not rewrite phase files solely to synchronize parent delivery status.


## PROD-L8.32R Parent Delivery Posture Derivation

Generated phase files must not contain writable `Parent delivery status:` fields for any value. A phase may point to parent delivery sources, but parent delivery active/complete posture is derived by status/close from the roadmap/register, delivery scope authority, phase files, archives, and accepted-state pointers. Do not reopen phase files solely to synchronize parent delivery lifecycle labels.
