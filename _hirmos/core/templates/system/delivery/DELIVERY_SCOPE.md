# Delivery Scope

Status: DRAFT | ACTIVE | COMPLETE | PARTIAL | SUPERSEDED | BLOCKED | DEFERRED | CANCELLED
Delivery ID:
Delivery name:
Delivery type: MVP | release | hardening | migration | brownfield-change | other
Parent delivery roadmap: `_hirmos/system/delivery/DELIVERY_PLAN.md`
Created from session:
Last updated from session:
Last session/archive pointer:

## 1. Delivery Identity

- Delivery ID:
- Delivery name:
- Delivery status:
- Parent delivery roadmap/register: `_hirmos/system/delivery/DELIVERY_PLAN.md`
- Delivery type:
- Relationship to other deliveries:

## 2. Authorized Outcome

- User-visible outcome:
- System-visible outcome:
- Business/product objective:
- Explicit non-goals:
- Success definition:

## 3. Scoped Requirements

| Requirement / accepted-state need | Source | Required for this delivery? | Acceptance expectation | Status |
|---|---|---:|---|---|
| | user request / accepted state / upload / prior delivery | YES / NO / PARTIAL | | NOT_ASSESSED |

### Functional requirements

- 

### Non-functional requirements

- 

### Constraints

- 

### Explicit exclusions

- 

## 4. Design and Engineering Decisions

| Decision area | Delivery decision | Rationale/evidence | Status |
|---|---|---|---|
| Architecture | | | PENDING |
| Stack | | | PENDING |
| Data / persistence | | | PENDING |
| Runtime / integration | | | PENDING |
| Security / privacy | | | PENDING |
| UX / operator workflow | | | PENDING |
| Preservation / regression | | | PENDING |

## 5. Production-Shaped Engineering Gate

| Gate | Required? | Planned approach | Evidence required at delivery close | Accepted limitation / deferment |
|---|---:|---|---|---|
| Persistence / database | YES / NO / UNKNOWN | | | |
| Auth / authorization | YES / NO / UNKNOWN | | | |
| Long-running / background work | YES / NO / UNKNOWN | | | |
| Usage / quotas / account limits | YES / NO / UNKNOWN | | | |
| Provider / API boundaries | YES / NO / UNKNOWN | | | |
| File / storage hygiene | YES / NO / UNKNOWN | | | |
| Secrets / environment hygiene | YES / NO / UNKNOWN | | | |
| Critical-flow tests / smoke evidence | YES / NO / UNKNOWN | | | |

## 6. Phase Plan

Use phases only when `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES` was selected or when separate phase files materially improve continuity, evidence, or reviewability.

| Phase | Phase file | Purpose | Scope | Entry condition | Exit condition | Status |
|---|---|---|---|---|---|---|
| PHASE-01 | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-01.md` | | | | | NOT_STARTED |

Lifecycle status vocabulary for phase rows:

```text
NOT_STARTED
READY_FOR_ADOPTION
ACTIVE
BLOCKED
PARTIAL
READY_FOR_ACCEPTANCE
ACCEPTED
DEFERRED
SUPERSEDED
CANCELLED
```

## 7. Session Adoption Rules

- Sessions must adopt from this Delivery Scope when they belong to this delivery.
- Sessions may not silently expand delivery scope.
- A session must narrow delivery scope into `_hirmos/session/SESSION_SCOPE.md` before implementation.
- New material requirements or design decisions must update this `DELIVERY_SCOPE.md` or be recorded in unresolved/carry-forward state.
- Phase-backed sessions must adopt both this `DELIVERY_SCOPE.md` and the selected `PHASE-xx.md`.

## 8. Evidence and Acceptance

| Evidence need | Source session/phase | Evidence location | Status |
|---|---|---|---|
| | | `_hirmos/session/EVIDENCE.md` / archive / implementation unit | PENDING |

Required delivery-level evidence:

- Session close verdicts for accepted phase/session work.
- Implementation evidence for delivery requirements.
- Current-state updates proving accepted outcomes.
- Carry-forward records for partial/deferred items.

## 9. Delivery Close Verification

| Verification item | Result | Evidence / notes |
|---|---|---|
| Requirements covered? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Design decisions implemented? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Production-shaped gate resolved? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Phase/session evidence complete? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Carry-forward created for remaining items? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |
| Accepted state updated? | PASS / PARTIAL / FAIL / NOT_APPLICABLE | |

Delivery verdict: accepted / partial / blocked / failed
