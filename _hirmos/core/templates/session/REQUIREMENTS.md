# Requirements

Status: conditional active-session requirements authority artifact.
Purpose: normalize material source inputs into requirement IDs, source traceability, requirement coverage, and requirement uncertainty when separate requirements authority is justified by `SESSION_SCOPE.md`.

`REQUIREMENTS.md` is subordinate to `SESSION_SCOPE.md`. It does not define session scope by itself. Only requirement IDs or sections explicitly adopted in `SESSION_SCOPE.md` are in scope for implementation and close verification.

## 1. Requirements Identity

| Field | Value |
|---|---|
| Session ID | `<session-id>` |
| Requirements version | `<v0>` |
| Requirements status | `DRAFT / READY_FOR_DESIGN / ACCEPTED / SUPERSEDED` |
| Source request | `<summary or path>` |
| Governing session scope | `_hirmos/session/SESSION_SCOPE.md` |
| Optional authority justification | `_hirmos/session/SESSION_SCOPE.md#optional-authority-artifact-justification-and-adoption` |

## 2. Responsibility Boundary

This artifact owns:

- normalized requirement IDs;
- requirement classification;
- source traceability;
- requirement coverage mapping;
- explicit requirement exclusions and uncertainty;
- requirement-level change/supersession history.

This artifact does not own:

- authorized session outcome or final scope;
- delivery shape decision;
- design decisions or stack choices;
- production-shaped engineering gate;
- implementation-unit planning;
- evidence details or implementation claims.

Those responsibilities belong to `SESSION_SCOPE.md`, `DESIGN.md`, `EVIDENCE.md`, and `implementation-units/` as applicable.

## 3. Source Inventory

Record every material source input considered.

| Source ID | Source/path | Type | Read status | Requirement relevance | Notes |
|---|---|---|---|---|---|
| SRC-001 | `<path or user request>` | `USER_REQUEST / FILE / CURRENT_STATE / OTHER` | `READ / BLOCKED / MISSING` | `IN_SCOPE / OUT_OF_SCOPE / UNCERTAIN` | `<notes>` |

## 4. Functional Requirements

| Requirement ID | Requirement | Source ID(s) | Acceptance signal | Adopted by SESSION_SCOPE? | Status |
|---|---|---|---|---|---|
| REQ-FUNC-001 | `<requirement>` | `SRC-001` | `<how to know it is satisfied>` | `YES / NO / PARTIAL` | `PROPOSED / ADOPTED / DEFERRED / REJECTED` |

## 5. Non-Functional Requirements

| Requirement ID | Requirement | Source ID(s) | Acceptance signal | Adopted by SESSION_SCOPE? | Status |
|---|---|---|---|---|---|
| REQ-NFR-001 | `<requirement>` | `SRC-001` | `<how to know it is satisfied>` | `YES / NO / PARTIAL` | `PROPOSED / ADOPTED / DEFERRED / REJECTED` |

## 6. Constraints and Exclusions

| ID | Type | Statement | Source ID(s) | Adopted by SESSION_SCOPE? | Notes |
|---|---|---|---|---|---|
| REQ-CON-001 | `CONSTRAINT / EXCLUSION` | `<statement>` | `SRC-001` | `YES / NO / PARTIAL` | `<notes>` |

## 7. Requirement Uncertainty and Gated Items

Material requirement uncertainty must also be represented in `_hirmos/session/unresolved-items.md`.

| Requirement ID / Source ID | Issue | Classification | Owner | Required decision or revalidation | Current handling |
|---|---|---|---|---|---|
| `<id>` | `<issue>` | `GATED / NON_GATING / TECHNICAL_REVIEW / BLOCKED` | `HUMAN / SYSTEM / TECHNICAL` | `<decision/revalidation>` | `<handling>` |

## 8. Requirement Coverage Mapping

| Requirement ID | Scope adoption | Implementation/evidence target | Mapping status | Notes |
|---|---|---|---|---|
| REQ-FUNC-001 | `ADOPTED / PARTIAL / NOT_ADOPTED` | `<SESSION_SCOPE section, IU path after acceptance, or evidence path>` | `MAPPED / PARTIAL / UNMAPPED / DEFERRED / BLOCKED` | `<notes>` |

Firm rule: before implementation authorization, every material in-scope requirement is mapped, deferred, blocked, or explicitly not applicable.

## 9. Coverage Status

| Requirement ID | Coverage status | Evidence / artifact reference | Remaining work | Close handling |
|---|---|---|---|---|
| REQ-FUNC-001 | `NOT_STARTED / PLANNED / IN_PROGRESS / IMPLEMENTED / PARTIAL / VERIFIED / DEFERRED / BLOCKED / NOT_APPLICABLE / REJECTED` | `<artifact path>` | `<remaining work>` | `<accepted / carry-forward / rejected>` |

Coverage status is not evidence status. Evidence status belongs in `EVIDENCE.md` claim reconciliation.

## 10. Source Traceability

Record source-to-requirement coverage.

| Source ID | Source section / area | Requirement IDs | Coverage notes |
|---|---|---|---|
| SRC-001 | `<section>` | `REQ-FUNC-001, REQ-NFR-001` | `<notes>` |

## 11. Change / Supersession Log

| Change | Requirement IDs affected | Reason | Result |
|---|---|---|---|
| `<change>` | `<ids>` | `<reason>` | `<accepted / superseded / rejected>` |

## 12. Input-to-Requirement Coverage Check

Every material source signal must be dispositioned before Design claims readiness.

| Source / Signal ID | Disposition | Requirement ID(s) / rationale | Notes |
|---|---|---|---|
| `SRC-001` | `MAPPED / OUT_OF_SCOPE / GATED / BLOCKED / DUPLICATE / SUPERSEDED / NOT_APPLICABLE` | `<REQ-ID or rationale>` | `<notes>` |

## 13. Requirements Self-Check

- [ ] `SESSION_SCOPE.md` justifies why separate requirements authority exists.
- [ ] All material input sources inspected, classified, or recorded as blocked.
- [ ] Requirements are normalized and source-mapped.
- [ ] Only requirements adopted by `SESSION_SCOPE.md` are treated as implementation obligations.
- [ ] Prototype/UI/reference signals are not silently promoted to confirmed requirements.
- [ ] Non-goals and exclusions are visible.
- [ ] Gated/unresolved requirements are represented in `unresolved-items.md` when material.
- [ ] Requirement coverage mapping exists or is explicitly deferred/blocked/not applicable.
- [ ] Evidence status, runtime posture, design decisions, and implementation claims are not mixed into requirement coverage fields.
- [ ] Accepted-state merge/carry-forward handling is recorded before close.
