# System State Update

Status: active-session Update System State artifact.
Lifecycle owner: Update System State.
Primary capability: `system-state-agent/update-system-state`.
Purpose: convert reviewed session outcomes into durable accepted system state or record why they were not accepted.

Update System State is truth synchronization and history. It is not Design or Implementation.

## Update Context

- Session ID:
- Source Session Execution:
- Session Contract, if any:
- Session Implementation Review, if any:
- Evidence Review:
- Close Checklist:

## Readiness Controls

| Control | Status | Evidence | Notes |
|---|---|---|---|

Required controls must not be `PENDING` or `BLOCKED` for normal close.

## Accepted Outcomes

List outcomes that become durable accepted system state.

| Outcome | Source artifact | Evidence | Accepted-state target | Notes |
|---|---|---|---|---|

## Rejected / Not Applied Outcomes

List outcomes that do not become accepted state and why.

| Outcome | Reason | Future handling |
|---|---|---|

## Evidence-Only Artifacts

List artifacts preserved for history but not accepted as current system state.

## Applied State Changes

Describe updates to `_hirmos/system/accepted-state/` or other accepted-state records.

## Carry-Forward Items

List unresolved items, assumptions, risks, or future-session notes carried forward.

| Item | Type | Owner | Future-session instruction |
|---|---|---|---|

## Archive Plan

- Archive path:
- Artifacts to archive:
- Active session reset required: yes / no
- Reset exceptions:

## Future Session Readiness

State what future sessions should treat as current system state and what they must re-check.

## Update Decision

- READY_TO_CLOSE | CLOSED | BLOCKED | ABORT_CLOSE | NOT_APPLICABLE
- Rationale:
- SESSION_EXECUTION.md final state updated: yes / no


## Runtime Integration Accepted State

Record accepted runtime integration posture for future sessions.

| Area | Accepted current posture | Production recommendation | Production-readiness blocker | Carry-forward action |
|---|---|---|---|---|

Do not record production readiness unless evidence supports production readiness for all material areas or limitations are explicitly recorded.

## Next Delivery Recommendation

After accepted outcomes are applied, record the next recommended Delivery Unit or explain why none is recommended.

- Next recommended unit:
- Reason:
- Governing Delivery Plan / contract:
- Required next command/action:
- Blockers or required Design refresh:

This recommendation is planning/status guidance. It does not authorize Implementation by itself.

## Close Transaction Integrity

| Transaction part | Status | Evidence | Notes |
|---|---|---|---|
| Readiness verification | PENDING | | |
| Accepted-state decision | PENDING | | |
| Accepted-state application | PENDING | | |
| Archive preservation | PENDING | | |
| Active-session reset | PENDING | | |
| Post-close verification | PENDING | | |

Normal close cannot be claimed until every required transaction part is complete or explicitly not applicable with rationale.

## Accepted-State Targets

| Target file | Change summary | Source artifact | Applied | Notes |
|---|---|---|---|---|
| `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | current truth, accepted-state navigation, latest-close metadata | | yes / no | |
| `_hirmos/system/accepted-state/CARRY_FORWARD.md` | | | yes / no | |

## Archive Manifest Link

- Archive manifest path:
- Archive completeness verified: yes / no
- Exceptions:

## Post-Close Status Expectation

After normal close, `hirmos status` should report idle active session, latest archive, current-state latest-close metadata, carry-forward path, and one primary next command/action when supported.

## Claim Reconciliation for Accepted Outcomes

Each accepted outcome must be supported by reconciled evidence.

| Accepted outcome | Claim family | Evidence status | Source artifact | Final-file support | Accepted? |
|---|---|---|---|---|---:|

Do not promote evidence-only, unverified, not-run, or contradicted claims into accepted system state.

## archive/session-state integrity Claim and Archive-State Application Gate

Before accepted-state update is applied:

- instantiate `support/claim-reconciliation.md` when any material claim supports accepted state;
- verify canonical evidence states only;
- verify accepted outcomes do not depend on noncanonical posture/evidence labels;
- verify close/archive state will not contradict accepted state;
- record any downgraded claims as carry-forward items instead of accepted truth.

Firm rule: accepted state must reflect proven or explicitly accepted outcomes only, not optimistic summaries.

## durable current-system-state Current-System-State Merge Plan

Normal close requires a current-state merge plan.

| Current-state section | Accepted / superseded change | Source artifact | Evidence / claim reconciliation | Applied? | Notes |
|---|---|---|---|---:|---|
| Current State Header | | | | yes / no | |
| Product State | | | | yes / no | |
| Delivery State, including active delivery pointers | | | | yes / no | |
| Implementation State | | | | yes / no | |
| Technical / Architecture State | | | | yes / no | |
| Runtime Integration State | | | | yes / no | |
| Evidence State | | | | yes / no | |
| Production Readiness State | | | | yes / no | |
| Unresolved / Carry-Forward State | | | | yes / no | |
| History / Traceability | | | | yes / no | |

#

## Delivery Pointer Accepted-State Update

Required when the session created, changed, accepted, blocked, superseded, or advanced durable delivery governance. If not applicable, record why.

| Pointer | Previous value | New value | Source artifact / evidence | Applied? |
|---|---|---|---|---:|
| Delivery governance active | | | `SESSION_CONTRACT.md`, `DELIVERY_PLAN.md`, `PHASE-xx.md` | yes / no / not_applicable |
| Active delivery ID | | | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | yes / no / not_applicable |
| Delivery plan | | | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | yes / no / not_applicable |
| Active phase | | | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | yes / no / not_applicable |
| Active phase status | | | phase/session evidence | yes / no / not_applicable |
| Last accepted phase | | | close/archive evidence | yes / no / not_applicable |
| Last accepted session/archive | | | `support/archive-manifest.md` | yes / no / not_applicable |
| Next recommended phase | | | `DELIVERY_PLAN.md` / `PHASE-xx.md` | yes / no / not_applicable |
| Next governed command | | | `SESSION_STATE.json` / close decision | yes / no / not_applicable |

Fail-closed rule: if delivery governance was active or required and these pointers are missing, stale, contradictory, or not explicitly verified unchanged, Update System State is blocked.

## Accepted-state support artifacts / records

| Supporting artifact | Required update | Applied? | Notes |
|---|---|---:|---|
| `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | canonical merged current truth, accepted-state navigation, latest close metadata | yes / no | |
| `_hirmos/system/accepted-state/CARRY_FORWARD.md` | future-session obligations | yes / no | |
| `_hirmos/system/accepted-state/DECISION_LOG.md` | durable decisions | yes / no | |

Firm rule: accepted outcomes must be merged into `CURRENT_SYSTEM_STATE.md` or explicitly rejected / not applied. Updating only latest-close metadata is not Update System State.

## Canonical Accepted-State Merge Enforcement

Before applying accepted-state changes, verify:

| Check | Result | Notes |
|---|---|---|
| Accepted-state invariant blocks preserved | yes / no / not_applicable | |
| `CURRENT_SYSTEM_STATE.md` updated with canonical posture values only | yes / no / not_applicable | |
| `CURRENT_SYSTEM_STATE.md` updated with canonical evidence states only | yes / no / not_applicable | |
| `CURRENT_SYSTEM_STATE.md` latest-close metadata updated with the current close/archive | yes / no / not_applicable | |
| Decision classifications kept separate from evidence status | yes / no / not_applicable | |
| Role workflow smoke status reconciled through `support/role-workflow-smoke.md` | yes / no / not_applicable | |

If any check fails, do not apply the current-state merge. Route back to the owning artifact and correct the values.

## Close-Time Compliance Application

Before applying accepted-state updates, verify that all required owning artifacts have been materialized and reconciled.

| Compliance item | Required because | Owning artifact | Result | Notes |
|---|---|---|---|---|
| Close claim reconciliation | normal close | `support/claim-reconciliation.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Implementation evidence | Implementation active | `support/session-implementation-review.md`, `support/evidence-review.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Local setup/runtime evidence | local setup/runtime claim | `support/local-runtime-evidence.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Role workflow smoke evidence | role/workflow claim | `support/role-workflow-smoke.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Runtime integration posture | integration posture claim | `support/runtime-integration-readiness.md` | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Framework validator | framework/invariant change | `python3 _hirmos/tools/validate.py` result | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Canonical structured-value scan | normal close | claim/runtime/current-state artifacts | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |
| Package cleanliness | package produced | package report / archive manifest | PENDING / SATISFIED / BLOCKED / NOT_APPLICABLE | |

Accepted-state merge is not allowed while any required close-time compliance item is `PENDING` or `BLOCKED`.

## Requirements Baseline Accepted-State Merge

When requirements were material to the session, Update System State must update `_hirmos/system/accepted-state/REQUIREMENTS_BASELINE.md` from `_hirmos/session/REQUIREMENTS_BASELINE.md`.

Record:

- requirements newly accepted;
- requirements implemented, partially implemented, verified, deferred, blocked, rejected, or not applicable;
- requirements moved to carry-forward;
- requirements superseded or changed;
- contradictions between requirements baseline and `CURRENT_SYSTEM_STATE.md`.

Do not claim complete requirements coverage unless the baseline coverage table supports that claim.

## Durable Phase Adoption Accepted-State Update

Required when delivery governance was active.

- Adopted Delivery Plan path:
- Adopted Phase path:
- Phase result from this session: ACCEPTED | PARTIAL | BLOCKED | SUPERSEDED | NOT_APPLICABLE
- Delivery Plan status update required? YES | NO | NOT_APPLICABLE
- Current System State pointer update required? YES | NO | NOT_APPLICABLE
- Next phase / session pointer:

Fail-closed rule: accepted-state update is incomplete if delivery governance was active and the adopted phase result is not reconciled into the Delivery Plan status and Current System State delivery pointers.


## Close-Time Delivery / Phase Status Transaction

Required when delivery governance was active, required, created, changed, accepted, blocked, superseded, or advanced in this session.

| Transaction item | Required target | Previous value | New value | Evidence | Applied? |
|---|---|---|---|---|---:|
| Adopted phase result | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` status and Phase Acceptance Review | | | `session-contract-review.md`, IU reviews, evidence | yes / no / not_applicable |
| Parent Delivery Plan phase row | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` Delivery Decomposition | | | phase status update | yes / no / not_applicable |
| Delivery Status Update Log | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` log entry | | | archive/session ID | yes / no / not_applicable |
| Next phase recommendation | Delivery Plan Active Development Context and Current System State pointers | | | Delivery Plan / Phase handoff | yes / no / not_applicable |
| Carry-forward delivery obligations | `CARRY_FORWARD.md` or next `PHASE-xx.md` | | | unresolved-items.md | yes / no / not_applicable |

Close-time delivery status verdict:

- DELIVERY_STATUS_UPDATE_APPLIED
- DELIVERY_STATUS_UNCHANGED_VERIFIED
- DELIVERY_STATUS_BLOCKED
- NOT_APPLICABLE

Fail-closed rule: if delivery governance was active or required and this transaction is missing, partially applied without rationale, or contradictory to the Delivery Plan, Phase file, Session Contract, or Current System State pointers, Update System State is blocked and normal close must not be claimed.

## Phase Progress / Carry-Forward Transaction

Required when delivery governance was active and the adopted phase is not fully accepted.

- Phase progress ledger updated: yes / no / not_applicable
- Resulting phase lifecycle status: ACCEPTED / PARTIAL / BLOCKED / DEFERRED / SUPERSEDED / CANCELLED / UNCHANGED_WITH_RATIONALE
- Carry-forward required: yes / no / not_applicable
- Carry-forward status: RECORDED / BLOCKED / NOT_APPLICABLE
- Carry-forward target:
- Current System State active/next phase pointer updated: yes / no / not_applicable

Fail-closed rule: if the resulting phase lifecycle status is `PARTIAL`, `BLOCKED`, or `DEFERRED`, `Carry-forward status` must be `RECORDED` before normal close.


## Phase Acceptance Transaction

- Phase acceptance status: ACCEPTED / NOT_ACCEPTED / BLOCKED / NOT_APPLICABLE
- Phase acceptance evidence status: COMPLETE / INCOMPLETE / BLOCKED / NOT_APPLICABLE
- Adopted phase path: _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
- Delivery Plan status update applied: yes / no / not_applicable
- Durable Phase status update applied: yes / no / not_applicable
- CURRENT_SYSTEM_STATE.md delivery pointers refreshed: yes / no / not_applicable
- Remaining adopted work: NONE / RECORDED_AS_CARRY_FORWARD / DEFERRED_WITH_RATIONALE / BLOCKED
- Greenfield acceptance evidence: COMPLETE / INCOMPLETE / NOT_APPLICABLE
- Brownfield acceptance evidence: COMPLETE / INCOMPLETE / NOT_APPLICABLE
