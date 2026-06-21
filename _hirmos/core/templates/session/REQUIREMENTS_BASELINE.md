# REQUIREMENTS_BASELINE

## 1. Baseline Identity

| Field | Value |
|---|---|
| Session ID | `<session-id>` |
| Baseline version | `<v0>` |
| Baseline status | `DRAFT / READY_FOR_DESIGN / ACCEPTED / SUPERSEDED` |
| Created from | `<request / uploaded files / accepted state / prototype inputs>` |
| Last updated | `<timestamp or unknown>` |

## 2. Source Inputs and Classification

Record every material input source before Design relies on it.

| Source ID | Path / Source | Source classification | Inspected | Materiality | Notes |
|---|---|---|---|---|---|
| SRC-001 | `_hirmos/inputs/uploads/requirements.txt` | `RAW_REQUIREMENT_NOTE` | `YES / NO / BLOCKED` | `HIGH / MEDIUM / LOW` | `<notes>` |

Canonical source classifications:

```text
RAW_REQUIREMENT_NOTE
PROTOTYPE_DERIVED_SIGNAL
UI_UX_DESIGN_NOTE
REFERENCE_MATERIAL
CONVERSATION_CONTEXT
ACCEPTED_STATE_REQUIREMENT
RESEARCH_BACKED_DEFAULT
MIXED_SOURCE
BLOCKED_UNREADABLE
NOT_APPLICABLE
```

## 2A. Normalized Intake Classification Preservation

Use this section to preserve source classifications that must not be collapsed into accepted requirement truth.

| Signal ID | Signal | Classification | Source ID(s) | Requirement impact | Handling | Notes |
|---|---|---|---|---|---|---|
| SIG-001 | `<signal>` | `CONFIRMED_SOURCE_SIGNAL / ASSUMPTION / RESEARCH_BACKED_DEFAULT / DECLARED_DELIVERY_TARGET / PROPOSED_DELIVERY_TARGET / OPEN_QUESTION / PENDING_CONFIRMATION / PROTOTYPE_OBSERVED_BEHAVIOR / PROTOTYPE_INTENDED_BEHAVIOR / PROTOTYPE_VARIANT / PROTOTYPE_CONFLICT` | `SRC-###` | `<candidate requirement / constraint / non-goal / unresolved>` | `<accepted / assumption-based / gated / rejected / deferred / duplicate / superseded / not applicable>` | `<notes>` |

## 2B. Prototype-Set Reconciliation Status

Complete this section when prototype, POC, screenshot-flow, generated-app, demo-code, or multi-prototype inputs exist.

| Field | Value |
|---|---|
| Prototype inputs present | `YES / NO` |
| Prototype count | `<0 / 1 / many / unknown>` |
| Prototype-specific findings recorded | `YES / NO / NOT_APPLICABLE / BLOCKED` |
| Prototype-set reconciliation required | `YES / NO / BLOCKED` |
| Prototype-set reconciliation completed | `YES / NO / NOT_APPLICABLE / BLOCKED` |
| Blocking conflicts / variants | `<none / summary / unresolved item IDs>` |

If multiple prototypes exist, do not proceed to Design on prototype-derived requirements until shared signals, conflicts, variants, and normalized requirement candidates are recorded in `_hirmos/session/DESIGN.md` or explicitly blocked/gated.

## 3. Product Goal

Summarize the accepted product/change goal in concise terms.

## 4. Scope Boundary

### In Scope

- `<scope item>`

### Out of Scope / Non-Goals

- `<non-goal or exclusion>`

### Assumption-Based Scope

- `<assumption and source>`

## 5. Requirement Catalog

Every material requirement must have a stable ID, source reference, requirement class, scope status, and coverage status.

| Requirement ID | Requirement | Class | Scope status | Coverage status | Source references | Notes |
|---|---|---|---|---|---|---|
| REQ-FUNC-001 | `<requirement>` | `FUNCTIONAL` | `IN_SCOPE` | `PLANNED` | `SRC-001:<section>` | `<notes>` |

Canonical requirement classes:

```text
FUNCTIONAL
WORKFLOW_STATE
DATA_DOMAIN
UI_UX
INTEGRATION
SECURITY_PRIVACY
AUDIT_EVIDENCE
RUNTIME_OPERATIONS
NON_FUNCTIONAL
ACCEPTANCE_CRITERION
NON_GOAL
CONSTRAINT
```

Canonical scope statuses:

```text
IN_SCOPE
OUT_OF_SCOPE
NON_GOAL
GATED
ASSUMPTION_BASED
DEFERRED
BLOCKED
DUPLICATE
SUPERSEDED
NOT_APPLICABLE
```

Canonical coverage statuses:

```text
NOT_STARTED
PLANNED
IN_PROGRESS
IMPLEMENTED
PARTIAL
VERIFIED
DEFERRED
BLOCKED
NOT_APPLICABLE
REJECTED
```

## 5A. Detailed Requirement Records

Use detailed records for material workflow, approval, state-machine, integration, security, or acceptance requirements where a one-line catalog row is not enough.

### `<REQ-ID>: <Title>`

- Class: `<FUNCTIONAL / WORKFLOW_STATE / DATA_DOMAIN / UI_UX / INTEGRATION / SECURITY_PRIVACY / AUDIT_EVIDENCE / RUNTIME_OPERATIONS / NON_FUNCTIONAL / ACCEPTANCE_CRITERION / NON_GOAL / CONSTRAINT>`
- Scope status: `<IN_SCOPE / OUT_OF_SCOPE / NON_GOAL / GATED / ASSUMPTION_BASED / DEFERRED / BLOCKED / DUPLICATE / SUPERSEDED / NOT_APPLICABLE>`
- Coverage status: `<NOT_STARTED / PLANNED / IN_PROGRESS / IMPLEMENTED / PARTIAL / VERIFIED / DEFERRED / BLOCKED / NOT_APPLICABLE / REJECTED>`
- Source references: `<SRC-### / SIG-### / prototype finding / accepted prior requirement>`
- Actor(s): `<actors>`
- Preconditions: `<preconditions>`
- Trigger: `<trigger>`
- Main flow:
  1. `<step>`
- Alternate flows: `<alternate flows or NOT_APPLICABLE>`
- Edge cases / invalid transitions: `<edge cases or unresolved items>`
- Expected outcome: `<outcome>`
- Requirement uncertainty severity: `<SAFE_TO_ASSUME / PROCEED_WITH_CAUTION / GATING_DECISION_REQUIRED / NOT_APPLICABLE>`
- Unresolved item references: `<UNRESOLVED-### / none>`

Firm rule: if the requirement affects a material workflow and a developer could ask “what should happen here?”, add a detailed record or mark the missing behavior as gated/unresolved.

## 6. Non-Goals and Exclusions

| ID | Non-goal / exclusion | Source references | Rationale |
|---|---|---|---|
| REQ-NONGOAL-001 | `<non-goal>` | `<source>` | `<rationale>` |

## 7. Gated / Unresolved Requirements

| Requirement ID / Source ID | Issue | Owner | Required decision | Current handling |
|---|---|---|---|---|
| `<id>` | `<issue>` | `HUMAN / SYSTEM / TECHNICAL` | `<decision>` | `GATED / ASSUMPTION_BASED / BLOCKED / DEFERRED` |

Material unresolved requirements must also be represented in `_hirmos/session/unresolved-items.md`.

## 8. Requirement-to-Delivery Mapping

| Requirement ID | Delivery Unit / Phase / Carry-forward | Mapping status | Notes |
|---|---|---|---|
| REQ-FUNC-001 | `DU-001` | `MAPPED / PARTIAL / UNMAPPED / DEFERRED` | `<notes>` |

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
| SRC-001 | `<section>` | `REQ-FUNC-001, REQ-UI-001` | `<notes>` |

## 11. Change / Supersession Log

| Change | Requirement IDs affected | Reason | Result |
|---|---|---|---|
| `<change>` | `<ids>` | `<reason>` | `<accepted / superseded / rejected>` |

## 11A. Baseline Input-to-Requirement Coverage Check

Every material source signal must be dispositioned before Design claims readiness.

| Source / Signal ID | Disposition | Requirement ID(s) / rationale | Notes |
|---|---|---|---|
| `SRC-001` | `MAPPED / OUT_OF_SCOPE / GATED / BLOCKED / DUPLICATE / SUPERSEDED / NOT_APPLICABLE` | `<REQ-ID or rationale>` | `<notes>` |

## 12. Baseline Self-Check

- [ ] All material input sources inspected, classified, or recorded as blocked.
- [ ] Requirements are normalized and source-mapped.
- [ ] Prototype/UI/reference signals are not silently promoted to confirmed requirements.
- [ ] Non-goals and exclusions are visible.
- [ ] Gated/unresolved requirements are represented in `unresolved-items.md` when material.
- [ ] Delivery mapping exists or is explicitly deferred/blocked/not applicable.
- [ ] Coverage status uses canonical requirements coverage statuses.
- [ ] Evidence status, runtime posture, and implementation claims are not mixed into requirement coverage fields.
- [ ] Accepted-state merge/carry-forward handling is recorded before close.

## Cross-Run / Candidate Source Coverage Check

Use this section when the session compares multiple candidate implementations, prototypes, generated apps, prior self-runs, external spec-tool outputs, UX drafts, or other candidate sources.

| Candidate / source | Source type | Useful coverage lessons | Missing / weaker areas | Salvage destination | Requirement IDs affected |
|---|---|---|---|---|---|
| | HIRMOS run / external spec-tool run / prototype / external app-builder output / UX note / other | | | REQUIREMENTS_BASELINE / DELIVERY_PLAN / TECHNICAL_REVIEW / ROLE_WORKFLOW_SMOKE_CHECKS / CARRY_FORWARD | |

Coverage claim gate:

| Check | Value |
|---|---|
| All material requirement sources reconciled against this baseline? | yes / no / partial |
| UI/UX requirements checked separately from data/API coverage? | yes / no / not_applicable |
| Acceptance criteria checked separately from implementation breadth? | yes / no / not_applicable |
| Any candidate lessons promoted to new/updated requirements? | yes / no |
| Any candidate lessons rejected or marked not applicable? | yes / no |
| Coverage claim reconciled in EVIDENCE.md claim reconciliation? | yes / no / not_applicable |

Firm rule: candidate comparison output cannot substitute for updating this requirements baseline when the comparison reveals missing, partial, deferred, or newly clarified requirements.
