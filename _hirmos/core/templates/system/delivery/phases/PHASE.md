# Phase Scope

Lifecycle status: NOT_STARTED | READY_FOR_ADOPTION | ACTIVE | BLOCKED | PARTIAL | READY_FOR_ACCEPTANCE | ACCEPTED | DEFERRED | SUPERSEDED | CANCELLED
Phase type: GREENFIELD | BROWNFIELD | MIXED | UNKNOWN
Delivery ID:
Phase ID:
Phase title:
Source Delivery Roadmap: `_hirmos/system/delivery/DELIVERY_PLAN.md`
Source Delivery Scope: `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
Created from session:
Last updated from session:
Last session/archive pointer:
Next recommended action:

## Authority

This is the durable phase scope for one bounded phase of a delivery governed by `DELIVERY_SCOPE.md`.

Canonical location:

```text
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

A phase may source a future `SESSION_SCOPE.md`, but it does not authorize implementation by itself. A session must still create or adopt a Session Scope and implementation units before implementation.

## Phase Lifecycle State Model

This phase must use the canonical lifecycle status and phase type vocabulary from `_hirmos/core/protocol/PHASE_LIFECYCLE.md`.

Implementation readiness is blocked when:

- `Phase type` is `UNKNOWN`.
- `Lifecycle status` is missing or non-canonical.
- `Lifecycle status` is incompatible with implementation adoption.
- Required type-specific control groups are missing for the declared phase type.

Implementation adoption is allowed only for:

```text
READY_FOR_ADOPTION
ACTIVE
PARTIAL
```

Review/close-only adoption may use:

```text
READY_FOR_ACCEPTANCE
```

## Current-State Basis

HIRMOS is current-state-first. Record the inspected current state that justifies this phase type and lifecycle status.

| Current-state source | Evidence read | Relevance | Classification impact |
|---|---|---|---|
| | | | GREENFIELD / BROWNFIELD / MIXED / UNKNOWN |

## Phase Objective

- User-visible outcome:
- Technical/system outcome:
- In scope:
- Out of scope:

## Universal Lifecycle Requirements

| Required field | Value / evidence | Status |
|---|---|---|
| Phase ID | | PENDING |
| Phase title | | PENDING |
| Phase type | GREENFIELD / BROWNFIELD / MIXED / UNKNOWN | PENDING |
| Lifecycle status | NOT_STARTED / READY_FOR_ADOPTION / ACTIVE / BLOCKED / PARTIAL / READY_FOR_ACCEPTANCE / ACCEPTED / DEFERRED / SUPERSEDED / CANCELLED | PENDING |
| Current-state basis | | PENDING |
| Delivery Roadmap pointer | `_hirmos/system/delivery/DELIVERY_PLAN.md` | PENDING |
| Delivery Scope pointer | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | PENDING |
| Entry criteria | | PENDING |
| Exit criteria | | PENDING |
| Scope included | | PENDING |
| Scope excluded | | PENDING |
| Adoption constraints | | PENDING |
| Acceptance evidence requirements | | PENDING |
| Open items | | PENDING |
| Deferred items | | PENDING |
| Carry-forward items | | PENDING |
| Close-time status transaction | | PENDING |
| Last session/archive pointer | | PENDING |
| Next recommended action | | PENDING |

## Source Coverage

| Delivery Scope item / requirement / accepted-state need | Covered by this phase? | Evidence / rationale |
|---|---:|---|
| | YES / NO / PARTIAL | |

## Entry Criteria

- Required prior phases:
- Required accepted-state conditions:
- Required unresolved decisions:
- Required runtime/setup conditions:

## Binary Exit Criteria

| Exit criterion | Evidence required | Status |
|---|---|---|
| | | NOT_ASSESSED |

## Scope Included

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

### Greenfield Entry Gate Controls

- MVP/slice boundary is explicit.
- Required architecture decisions are recorded in `DELIVERY_SCOPE.md` or `SESSION_SCOPE.md`.
- Validation level is identified.

### Brownfield Entry Gate Controls

- Current accepted state was inspected.
- Preservation constraints are recorded.
- Regression evidence expectations are identified.

## Phase Progress Ledger

| Session/archive | Work completed | Evidence | Remaining work | Status impact |
|---|---|---|---|---|
| | | | | |

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

### Greenfield Acceptance Evidence

- User-visible slice evidence:
- Build/test/smoke evidence:
- Deferred scope:

### Brownfield Acceptance Evidence

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

This section must be updated during `hirmos close` whenever a session accepts, partially accepts, blocks, supersedes, defers, cancels, or advances this phase.

## Phase Acceptance Review

The phase may be marked `ACCEPTED` only when the Phase Acceptance Evidence Gate is complete and the closed session records the accepted outcome, evidence, unresolved/carry-forward disposition, and accepted-state update.

## Close Verification

- The parent `DELIVERY_SCOPE.md` status and phase table agree with this phase status.
- The parent `DELIVERY_PLAN.md` delivery index / active delivery pointer agrees with this delivery status.
- Binary Exit Criterion rows are resolved or carried forward.
- Phase Acceptance Review records the closed session before `ACCEPTED` status is used.


## Carry-Forward Items

- Carry-forward item:
- Target delivery/phase/session:
- Revalidation point:
