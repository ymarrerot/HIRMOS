
# Delivery Design

Status: optional delivery-level design authority.
Purpose: record delivery-wide technical design decisions only when separate design authority is justified by architecture, integration, migration, security, operational, or multi-session coordination needs.

Canonical location:

```text
_hirmos/system/delivery/<delivery-id>/DESIGN.md
```

This artifact is subordinate to `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`. It must not create independent delivery obligations absent from `DELIVERY_SCOPE.md`. `DELIVERY_SCOPE.md` must explicitly justify this file and adopt the design decision IDs or sections that govern the delivery.

## Responsibility Boundary

Owns:

- architecture decisions;
- data/persistence design;
- provider/integration boundaries;
- runtime/job-processing design;
- security/privacy/operational decisions;
- technical assumptions, alternatives, risks, and review points.

Does not own:

- requirement catalog;
- delivery authorization;
- phase/session implementation authority;
- implementation-unit planning;
- evidence details;
- delivery close verdict.

## Design Decision Register

| ID | Decision area | Decision | Rationale / evidence | Phase coverage | Review status |
|---|---|---|---|---|---|
| DD-01 | Architecture | | | `PHASE-xx` / not assigned | PENDING |

## Technical Review Points

| ID | Review point | Why it matters | Inspectable artifact/path | Challenge/change path |
|---|---|---|---|---|
| | | | | |

## Coverage Self-Check

- Every adopted delivery design decision is referenced by `DELIVERY_SCOPE.md`: YES / NO
- Every required design/engineering decision is assigned to the phase coverage plan: YES / NO
- Technical uncertainty is recorded in delivery `unresolved-items.md`: YES / NO / NOT_APPLICABLE
- Known gaps:
