# Delivery Scope

Authority status: DRAFT | PROPOSED | READY_FOR_BASELINE_REVIEW | BASELINED | SUPERSEDED | CANCELLED
Delivery ID:
Last updated from session:

## Purpose and Ownership

`DELIVERY_SCOPE.md` is the compact authority for one durable delivery/release. It owns stable delivery outcome authority, scope boundaries, phase coverage plan, delivery-level unresolved items pointer, production-shaped gate expectations, close-posture pointers, and source pointers. It must not duplicate phase details, session scope, IU contracts, evidence detail, or accepted-state summaries.

## 1. Delivery Identity

- Delivery ID:
- Delivery name:
- Delivery type: MVP / release / hardening / migration / existing-system-change / other
- Parent roadmap/register: `_hirmos/system/delivery/DELIVERY_PLAN.md`
- Delivery unresolved register: `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`
- Related deliveries:

## 2. Authorized Outcome

- User/business outcome:
- Primary user-visible workflow:
- Implementation acceptance level intended:
- Runtime evidence level intended:
- Production evidence level intended:
- Explicit non-goals:

## 3. Optional Authority Artifact Justification and Adoption

Optional delivery `REQUIREMENTS.md` and `DESIGN.md` are allowed only when independent authority is justified. Otherwise requirements and decisions remain compactly in this file.

| Optional artifact | Adopted? | Reason | Path |
|---|---:|---|---|
| REQUIREMENTS.md | YES / NO | | `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` |
| DESIGN.md | YES / NO | | `_hirmos/system/delivery/<delivery-id>/DESIGN.md` |

## 4. Scoped Requirements

Compact scope only. Do not expand into phase/session/IU implementation detail.

### Functional requirements

These rows define baseline scope identity and planned phase coverage only. They do not own current completion status. Requirement verification/completion posture is derived from accepted phase/session/IU/evidence records.

| ID | Requirement | Priority | Covered by phase(s) |
|---|---|---|---|
| FR-001 | | MUST / SHOULD / COULD | planned phase IDs |

### Non-functional requirements

These rows define baseline non-functional scope and evidence expectations only. They do not own current completion status.

| ID | Requirement | Evidence expectation | Covered by phase(s) |
|---|---|---|---|
| NFR-001 | | | planned phase IDs |

### Constraints

- Technical/runtime constraints:
- Provider/cost constraints:
- Data/security/privacy constraints:

### Explicit exclusions

- Exclusion:
- Rationale / later target:

## 5. Design and Engineering Decisions

Compact decision index only. Detailed design goes to optional `DESIGN.md` only if justified.

| Decision | Rationale | Source | Status |
|---|---|---|---|
| | | user / current state / existing code | PROPOSED / ACCEPTED / DEFERRED |

## 6. Delivery-Level Unresolved Items

Detailed unresolved items live in `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`.

- Delivery unresolved register path:
- Gated unresolved count:
- Non-gating unresolved count:
- Technical-review count:
- Blocking summary:

## 7. Production-Shaped Engineering Gate

- Deployment/production claim allowed: YES / NO / PARTIAL
- Local runtime evidence required:
- External provider evidence required:
- Data migration / persistence evidence required:
- Auth/security evidence required:
- Cost/credit evidence required:
- What is explicitly not claimed:

## 8. Phase Plan / Phase Coverage Plan

Before delivery-baseline acceptance, this table is the only phase coverage plan. Future `PHASE-xx.md` files are not instantiated until created just in time after acceptance. Keep rows thick enough to prove coverage, but do not duplicate phase files.

| Phase ID | Phase name | Lifecycle status | Phase type | Objective | Scope IDs covered | Exit evidence summary | Merge-pressure result | Future file path |
|---|---|---|---|---|---|---|---|---|
| PHASE-01 | | NOT_STARTED / READY_FOR_ADOPTION / ACTIVE / PARTIAL / READY_FOR_ACCEPTANCE / ACCEPTED / DEFERRED / CANCELLED | GREENFIELD / BROWNFIELD / MIXED / UNKNOWN | | FR/NFR IDs | | keep / merge candidate | none until instantiated / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-01.md` |

## 9. Delivery Coverage Self-Check

| Scope item ID | Covered by phase(s) | Deferred? | Gap / rationale |
|---|---|---:|---|
| | | NO | |

Coverage result: PASS / PARTIAL / BLOCKED / NOT_ASSESSED

## 10. Session Adoption Rules

- Delivery-baseline sessions use this file as active delivery authority.
- Phase/session implementation may begin only after accepted delivery baseline and an adopted phase/session authority.
- `SESSION_SCOPE.md` must adopt exactly the applicable phase/session slice before implementation.
- `SESSION_SCOPE.md` and IU files must not treat this delivery scope as direct implementation authority.

## 11. Evidence and Acceptance

Evidence detail belongs in `EVIDENCE.md`, IU records, session ledger/archive, or runtime command output. This section only defines expected evidence levels.

| Evidence class | Required level | Source pointer | Status |
|---|---|---|---|
| implementation | code/build/test/review | | NOT_ASSESSED |
| local runtime | smoke/E2E/manual | | NOT_ASSESSED |
| production | deploy/prod-like verification | | NOT_CLAIMED |

## 12. Delivery Close Verification

Close result: NOT_READY | ACCEPTED | PARTIAL | BLOCKED | DEFERRED | CANCELLED | SUPERSEDED

| Close check | Source artifact | Status | Notes |
|---|---|---|---|
| Scope coverage reconciled | this file + phases | PASS / PARTIAL / BLOCKED | |
| Session/IU evidence reviewed | session archive / IU / EVIDENCE.md | PASS / PARTIAL / BLOCKED | |
| Runtime evidence posture honest | EVIDENCE.md | PASS / PARTIAL / BLOCKED / NOT_CLAIMED | |
| Carry-forward disposition approved | CARRY_FORWARD.md / unresolved register | PASS / BLOCKED / N/A | |
| Current-state pointers refreshed | CURRENT_SYSTEM_STATE.md | PASS / BLOCKED | |

## PROD-L8.22 Delivery Review Gate Authority

Required generated values when close is attempted:

- Reviewed delivery:
- Source authority reviewed:
- Phase/session evidence reviewed:
- Actual final codebase reviewed: YES / NO / NOT_APPLICABLE
- Requirements/scope coverage posture: PASS / PARTIAL / BLOCKED / FAILED
- Scope coverage result: PASS / PARTIAL / BLOCKED / FAILED
- Runtime evidence level: NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE
- Production evidence level: NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE
- Final delivery review result: PASS / PARTIAL / BLOCKED / FAILED
- Why this result is honest:
- What is not claimed:

## PROD-L8.24 Delivery Scope Close Concordance

Generated delivery close records are invalid if current status and lower sections disagree. Reconcile stale `PENDING`, `PLANNED`, `NOT_STARTED`, `NOT_ASSESSED`, or downgrade result.

## PROD-L8.26 Delivery Close Concordance Simplification and Evidence Posture Hardening

Delivery close must not claim `LOCAL_E2E_VERIFIED` unless actual local end-to-end evidence exists and is pointed to by evidence artifacts.

### Compact Derived Delivery Close Posture

| Posture field | Value | Source pointer |
|---|---|---|
| Delivery result | DERIVED_NOT_READY / DERIVED_ACCEPTED / DERIVED_PARTIAL / DERIVED_BLOCKED / DERIVED_DEFERRED / DERIVED_CANCELLED / DERIVED_SUPERSEDED | source phase/session/archive/current-state pointer |
| Implementation coverage | PASS / PARTIAL / BLOCKED / FAILED | |
| Local runtime evidence | NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED | |
| Production evidence | NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED | |
| Delivery unresolved register | no open / open non-gating / gated blockers | `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` |
| Current-state navigation | refreshed / blocked | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` |

## PROD-L8.28 Active Close Concordance

At active close, delivery scope, delivery plan, active phase, session ledger, evidence, carry-forward, archive manifest, and current-state pointers must agree. Do not leave stale planned/pending sections as current truth.


## Delivery Authority / Close Posture Split

Delivery baseline authority is stable after acceptance except explicit user-approved amendment. Close/status posture is a compact result pointer updated at close; detailed phase/session/IU/evidence truth remains in owning artifacts. Do not maintain duplicate runtime status sections that can become stale.

## PROD-L8.32L Just-in-Time Delivery Artifact Rule

During delivery-baseline planning, do not instantiate future phase files, optional delivery `REQUIREMENTS.md`, optional delivery `DESIGN.md`, or delivery unresolved registers unless the accepted delivery boundary makes that artifact applicable now. The Phase Plan / Phase Coverage Plan may name expected future phase IDs and paths, but those paths are not authority until the files are created during the governed phase boundary.


## PROD-L8.32Q Delivery Completion Concordance Simplification

Delivery scope owns stable baseline authority, not duplicated runtime completion truth. Do not maintain a writable top-level `Status: ACTIVE` / `Status: COMPLETE` lifecycle mirror here. Use `Authority status` for baseline authority and derive delivery completion posture from phase files, session archives, evidence, and accepted-state/current roadmap pointers.

Requirement rows must not maintain close-time `PROPOSED` / `COMPLETE` status cells. They define scope identity and planned coverage only. Requirement completion and evidence posture are derived at status/close from accepted phase/session/IU/evidence records.

If delivery completion is claimed elsewhere while this file preserves stale mutable runtime status, close/status must fail closed or reconcile by removing the duplicate status field.
