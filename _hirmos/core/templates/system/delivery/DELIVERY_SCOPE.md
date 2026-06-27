
# Delivery Scope

Status: PROPOSED | READY_FOR_BASELINE_REVIEW | ACTIVE | ACCEPTED | PARTIAL | BLOCKED | SUPERSEDED | DEFERRED | CANCELLED
Delivery ID:
Delivery name:
Delivery type: MVP | release | hardening | migration | change | other
Parent delivery roadmap: `_hirmos/system/delivery/DELIVERY_PLAN.md`
Created from runtime session:
Last updated from runtime session:
Last session/archive pointer:

## 1. Delivery Identity

- Delivery ID:
- Delivery name:
- Delivery status:
- Parent delivery roadmap/register: `_hirmos/system/delivery/DELIVERY_PLAN.md`
- Delivery type:
- Relationship to other deliveries:
- Delivery baseline checkpoint status: NOT_STARTED | READY_FOR_BASELINE_REVIEW | ACCEPTED | AMENDED | BLOCKED

## 2. Authorized Outcome

- User-visible outcome:
- System-visible outcome:
- Business/product objective:
- Explicit non-goals:
- Success definition:

## 3. Optional Authority Artifact Justification and Adoption

`DELIVERY_SCOPE.md` is the complete delivery authority and acceptance root. Optional `REQUIREMENTS.md` and `DESIGN.md` may provide detailed delivery-wide authority only when this file explicitly justifies and adopts them. They must not create independent delivery obligations absent from this scope.

- Separate delivery `REQUIREMENTS.md` created? YES | NO
- Justification if yes:
- Adopted requirement IDs / sections: `REQ-*` / sections / NOT_APPLICABLE
- Separate delivery `DESIGN.md` created? YES | NO
- Justification if yes:
- Adopted design decision IDs / sections: `DD-*` / sections / NOT_APPLICABLE
- Why this does not duplicate delivery authority:
- Review pointer for user / technical reviewer:

## 4. Scoped Requirements

| Requirement / accepted-state need | Source | Required for this delivery? | Acceptance expectation | Phase coverage | Status |
|---|---|---:|---|---|---|
| | user request / accepted state / upload / prior delivery | YES / NO / PARTIAL | | `PHASE-xx` / not assigned | NOT_ASSESSED |

### Functional requirements

-

### Non-functional requirements

-

### Constraints

-

### Explicit exclusions

-

## 5. Design and Engineering Decisions

| Decision area | Delivery decision | Rationale/evidence | Phase coverage | Status |
|---|---|---|---|---|
| Architecture | | | `PHASE-xx` / not assigned | PENDING |
| Stack | | | `PHASE-xx` / not assigned | PENDING |
| Data / persistence | | | `PHASE-xx` / not assigned | PENDING |
| Runtime / integration | | | `PHASE-xx` / not assigned | PENDING |
| Security / privacy | | | `PHASE-xx` / not assigned | PENDING |
| UX / operator workflow | | | `PHASE-xx` / not assigned | PENDING |
| Preservation / regression | | | `PHASE-xx` / not assigned | PENDING |

## 6. Delivery-Level Unresolved Items

Canonical delivery unresolved register:

```text
_hirmos/system/delivery/<delivery-id>/unresolved-items.md
```

Delivery baseline approval must use this register for delivery-level gated items, non-gating assumptions, technical-review items, blockers, and material uncertainty.

- Gated delivery items open? YES | NO
- Phase-planning blockers open? YES | NO
- Non-gating delivery assumptions carried? YES | NO
- Technical-review delivery items present? YES | NO
- Checkpoint feed source: `_hirmos/system/delivery/<delivery-id>/unresolved-items.md#Current Checkpoint Feed`

## 7. Production-Shaped Engineering Gate

| Gate | Required? | Planned approach | Evidence required at delivery close | Phase coverage | Accepted limitation / deferment |
|---|---:|---|---|---|---|
| Persistence / database | YES / NO / UNKNOWN | | | `PHASE-xx` / delivery-level | |
| Auth / authorization | YES / NO / UNKNOWN | | | `PHASE-xx` / delivery-level | |
| Long-running / background work | YES / NO / UNKNOWN | | | `PHASE-xx` / delivery-level | |
| Usage / quotas / account limits | YES / NO / UNKNOWN | | | `PHASE-xx` / delivery-level | |
| Provider / API boundaries | YES / NO / UNKNOWN | | | `PHASE-xx` / delivery-level | |
| File / storage hygiene | YES / NO / UNKNOWN | | | `PHASE-xx` / delivery-level | |
| Secrets / environment hygiene | YES / NO / UNKNOWN | | | `PHASE-xx` / delivery-level | |
| Critical-flow tests / smoke evidence | YES / NO / UNKNOWN | | | `PHASE-xx` / delivery-level | |

## 8. Phase Plan / Phase Coverage Plan

Before delivery-baseline acceptance, this table must cover the complete delivery scope at planning level. It may name future phases without instantiating future `PHASE-xx.md` files. Do not reference a concrete phase file path until the file exists.

| Phase | Purpose | Delivery requirements covered | Design areas covered | Production gates covered | Entry condition | Exit condition | Status | Phase file |
|---|---|---|---|---|---|---|---|---|
| PHASE-01 | | `REQ-*` / scoped requirement rows | `DD-*` / decision areas | | | | planned | not instantiated |

Allowed status values before instantiation: `planned`, `blocked`, `deferred`, `not_applicable`.
Allowed status values after instantiation: `ready_for_adoption`, `active`, `blocked`, `partial`, `ready_for_acceptance`, `accepted`, `deferred`, `superseded`, `cancelled`.

## 9. Delivery Coverage Self-Check

Delivery baseline cannot be accepted until this self-check is complete, unless a surfaced gated delivery item explicitly blocks full phase coverage.

- All in-scope delivery requirements assigned to one or more phases: YES | NO
- All required design/engineering decisions assigned to one or more phases: YES | NO
- All production-shaped gates assigned to delivery-level or phase-level evidence: YES | NO
- No future concrete `PHASE-xx.md` paths referenced unless the files exist: YES | NO
- Known coverage gaps: none / list
- If any answer is NO, blocking delivery unresolved item ID:

## 10. Session Adoption Rules

- Sessions may adopt from this Delivery Scope only after the delivery baseline is accepted or amended.
- Sessions may not silently expand delivery scope.
- A phase/session must narrow delivery authority into `_hirmos/session/SESSION_SCOPE.md` before implementation.
- Session-level unresolved items may resurface delivery assumptions when implementation discovers blockers or invalid assumptions.
- If a session-level unresolved item invalidates delivery truth, update this Delivery Scope or the delivery unresolved register before claiming close or implementation readiness.

## 11. Evidence and Acceptance

| Evidence need | Source phase/session | Evidence location | Status |
|---|---|---|---|
| | | `_hirmos/session/EVIDENCE.md` / archive / implementation unit | PENDING |

Required delivery-level evidence:

- Session close verdicts for accepted phase/session work.
- Implementation evidence for delivery requirements.
- Current-state updates proving accepted outcomes.
- Carry-forward records for partial/deferred items.
- Delivery unresolved items accepted, deferred, superseded, or blocking.

## 12. Delivery Close Verification

| Verification item | Result | Evidence / notes |
|---|---|---|
| Requirements covered? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Design decisions implemented? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Production-shaped gate resolved? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Phase/session evidence complete? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Delivery unresolved items reconciled? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Carry-forward created for remaining items? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Accepted state updated? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |

Delivery verdict: accepted / partial / blocked / failed

## PROD-L8.22 Delivery Review Gate Authority

Delivery close requires an evidence-backed delivery review gate before claiming delivery acceptance. The delivery review gate aggregates accepted phase review gates, active/carry-forward records, runtime evidence, production posture, and final current-state pointers.

Required fields:

- Delivery reviewed:
- Phases reviewed:
- Accepted source artifacts reviewed:
- Cross-phase integration reviewed: PASS / PARTIAL / BLOCKED / FAILED / NOT_APPLICABLE
- End-to-end workflow evidence: PASS / PARTIAL / BLOCKED / FAILED / NOT_RUN / NOT_APPLICABLE
- Requirements/scope coverage posture: PASS / PARTIAL / BLOCKED / FAILED
- Runtime evidence level: NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE
- Production evidence level: NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE
- Carry-forward items affecting acceptance:
- Final delivery result: PASS / PARTIAL / BLOCKED / FAILED
- What is not claimed:
- Why this result is honest:

A delivery review must not claim full MVP/runtime/production acceptance when only implementation acceptance or static validation evidence exists. Stale delivery-plan sections must be reconciled or labeled historical before delivery close success is claimed.


## PROD-L8.24 Delivery Scope Close Concordance
At delivery close, this `DELIVERY_SCOPE.md` must not remain as a stale baseline-only authority when phases have moved to accepted/closed/partial states. Phase status rows, DAC rows, and delivery close verification must be reconciled, explicitly historicalized, or downgraded. Current rows that still say `planned`, `ready_for_adoption`, `PENDING`, or `NOT_STARTED` while final phase/delivery artifacts claim accepted/closed status are close-blocking concordance defects.

## PROD-L8.26 Delivery Close Concordance Simplification and Evidence Posture Hardening

`DELIVERY_SCOPE.md` remains the delivery authority, but delivery close must not turn this file into a duplicated evidence ledger. At delivery or phase close, update this file with a compact final posture and source pointers, then historicalize or reconcile stale planning rows.

### Compact Delivery Close Posture

| Posture dimension | Current close posture | Authoritative source / pointer | Limitation / next action |
|---|---|---|---|
| Delivery result | OPEN / CLOSED_ACCEPTED / CLOSED_PARTIAL / BLOCKED / FAILED / DEFERRED / SUPERSEDED | archive / phase / session pointer | |
| Implementation coverage | NOT_STARTED / PARTIAL / COMPLETE / NOT_APPLICABLE | phase/session close pointer | |
| Local runtime evidence | NOT_CLAIMED / NOT_RUN / PARTIAL / LOCAL_E2E_VERIFIED / BLOCKED / NOT_APPLICABLE | `EVIDENCE.md` / IU evidence / archive | |
| Production evidence | NOT_CLAIMED / NOT_RUN / STAGING_VERIFIED / PRODUCTION_VERIFIED / BLOCKED / NOT_APPLICABLE | `EVIDENCE.md` / carry-forward / archive | |
| Delivery unresolved register | LIVE_OPEN / RECONCILED / CARRY_FORWARD / BLOCKING / NOT_APPLICABLE | `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` | |
| Current-state navigation | UPDATED / VERIFIED_UNCHANGED / BLOCKED | `CURRENT_SYSTEM_STATE.md` | |

Simplification rule: detailed DAC, phase, session, IU, runtime, and production evidence remains in phase/session/evidence/archive artifacts. This file records the compact close posture and pointers only.

Hardening rule: a final delivery result must not claim `LOCAL_E2E_VERIFIED`, `PRODUCTION_VERIFIED`, or full delivery `PASS` when the supporting critical-flow, provider, browser, image-generation, database, or production evidence is `NOT_RUN`, `BLOCKED`, or absent. Use `CLOSED_PARTIAL`, `PARTIAL`, or a narrower implementation-accepted claim when runtime or production evidence is incomplete.

Close concordance rule: after delivery close, rows that still show `planned`, `ready_for_adoption`, `PENDING`, `NOT_STARTED`, or similar pre-close values must be either updated to current truth, explicitly marked `historical baseline snapshot`, or replaced by compact source pointers. Stale current rows are close-blocking concordance defects.
