
# Delivery Requirements

Status: optional delivery-level requirements authority.
Purpose: normalize and trace delivery-wide requirements only when separate requirements authority is justified by delivery complexity, auditability, shared multi-session adoption, or user request.

Canonical location:

```text
_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md
```

This artifact is subordinate to `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`. It must not create independent delivery obligations absent from `DELIVERY_SCOPE.md`. `DELIVERY_SCOPE.md` must explicitly justify this file and adopt the requirement IDs or sections that govern the delivery.

## Responsibility Boundary

Owns:

- delivery-wide requirement IDs;
- source traceability;
- requirement classification;
- coverage mapping;
- exclusions and requirement uncertainty that feed the delivery unresolved register.

Does not own:

- delivery authorization;
- design decisions;
- phase/session implementation authority;
- implementation-unit planning;
- evidence details;
- delivery close verdict.

## Requirements Catalog

| ID | Requirement | Source | Classification | Delivery scope status | Phase coverage | Acceptance expectation |
|---|---|---|---|---|---|
| REQ-01 | | | functional / non-functional / constraint | in-scope / excluded / deferred | `PHASE-xx` / not assigned | |

## Source Traceability

| Source | Requirement IDs derived | Notes |
|---|---|---|
| | | |

## Coverage Self-Check

- Every in-scope delivery requirement is adopted by `DELIVERY_SCOPE.md`: YES / NO
- Every in-scope delivery requirement is assigned to the phase coverage plan: YES / NO
- Requirement uncertainty is recorded in delivery `unresolved-items.md`: YES / NO / NOT_APPLICABLE
- Known gaps:
