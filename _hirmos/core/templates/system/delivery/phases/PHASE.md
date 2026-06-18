# Phase Contract

Lifecycle status: NOT_STARTED | READY_FOR_ADOPTION | ACTIVE | BLOCKED | PARTIAL | READY_FOR_ACCEPTANCE | ACCEPTED | DEFERRED | SUPERSEDED | CANCELLED
Phase type: GREENFIELD | BROWNFIELD | MIXED | UNKNOWN
Delivery ID:
Phase ID:
Phase title:
Source Delivery Plan: `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`
Created from session:
Last updated from session:
Last session/archive pointer:
Next recommended action:

## Authority

This is the durable phase contract for one bounded phase of a multi-session delivery.

Canonical location:

```text
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

This phase may source a future `SESSION_CONTRACT.md`, but it does not authorize implementation by itself. A session must still create or adopt a Session Contract and implementation units before implementation.

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
| Delivery Plan pointer | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | PENDING |
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

| Delivery Plan item / requirement / accepted-state need | Covered by this phase? | Evidence / rationale |
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
| | | |

## Scope Excluded

| Item | Reason excluded | Carry-forward / deferral target |
|---|---|---|
| | | |

## Adoption Constraints

- Allowed adoption lifecycle statuses: READY_FOR_ADOPTION, ACTIVE, PARTIAL.
- Review-only adoption lifecycle status: READY_FOR_ACCEPTANCE.
- Implementation must not adopt NOT_STARTED, BLOCKED, ACCEPTED, DEFERRED, SUPERSEDED, CANCELLED, or UNKNOWN-type phases.
- Session adoption must map phase items to `SESSION_CONTRACT.md` and implementation units.

## Greenfield Controls

Required when `Phase type` is `GREENFIELD` or `MIXED`.

- MVP boundary:
- Primary user/workflow slice:
- Prototype vs production intent:
- Architecture dependency status:
- Out-of-scope expansion guard:
- Validation level required:
- Production-readiness claim allowed: YES / NO / PARTIAL

Greenfield acceptance guard:

- Implemented slice must match the phase objective.
- Prototype/scaffold/demo status must not be represented as production-ready.
- Architecture/design claims must match actual implementation.
- Known gaps must be carried forward or explicitly deferred.

## Brownfield Controls

Required when `Phase type` is `BROWNFIELD` or `MIXED`.

- Preservation baseline:
- Affected existing surfaces:
- Regression-sensitive behavior:
- Do-not-touch boundaries:
- Compatibility constraints:
- Data/migration safety constraints:
- Rollback/recovery considerations:
- Regression evidence required:

Brownfield acceptance guard:

- Existing behavior preservation must have evidence or risk must be explicitly recorded.
- Regression-sensitive areas must be tested, reviewed, or explicitly carried as risk.
- Data/migration safety must be reviewed when relevant.
- Do-not-touch boundaries must be respected or deviations reviewed.

## Mixed Phase Rule

Required when `Phase type` is `MIXED`.

A mixed phase must satisfy both the Greenfield Controls and Brownfield Controls sections. It may segment controls by workstream, but acceptance must reconcile both sides before `ACCEPTED` is allowed.

## Open Items

| Item | Blocking? | Disposition | Owner/source |
|---|---:|---|---|
| | YES / NO | OPEN / DEFERRED / RESOLVED | |

## Deferred Items

| Item | Reason deferred | Target phase/session | Accepted risk? |
|---|---|---|---:|
| | | | YES / NO |

## Carry-Forward Items

| Item | Why it remains | Required next action | Target artifact |
|---|---|---|---|
| | | | `CARRY_FORWARD.md` / next phase / future session |

## Session Handoff

- Intended Session Contract scope:
- Required implementation unit boundaries:
- Required direct reads before implementation:
- Blockers that must stop `hirmos start` or `hirmos continue`:

## Phase Acceptance Review

- Session(s) that completed this phase:
- Evidence summary:
- Unresolved items resolved:
- Carry-forward to next phase:
- Type-specific controls satisfied: GREENFIELD / BROWNFIELD / BOTH_FOR_MIXED / NOT_APPLICABLE / NO
- Final phase verdict: ACCEPTED | PARTIAL | FAILED | BLOCKED | NOT_REVIEWED

## Close-Time Phase Status Update Contract

This section must be completed during `hirmos close` for the adopted durable phase.

| Close session | Phase type | Previous lifecycle status | New lifecycle status | Verdict basis | Evidence / archive | Applied? |
|---|---|---|---|---|---|---:|
| | GREENFIELD / BROWNFIELD / MIXED / UNKNOWN | | ACCEPTED / PARTIAL / BLOCKED / DEFERRED / SUPERSEDED / CANCELLED / UNCHANGED_WITH_RATIONALE | | | yes / no / not_applicable |

Required close-time checks:

- Phase Acceptance Review records the closed session, evidence summary, unresolved items, carry-forward obligations, and final phase verdict.
- Every Binary Exit Criterion is classified as satisfied, partial, failed, blocked, deferred, or not applicable.
- Partial or blocked results identify what remains for the next phase or future session.
- The parent `DELIVERY_PLAN.md` status row agrees with this phase status.
- `CURRENT_SYSTEM_STATE.md` delivery pointers agree with the resulting active/next phase state.

Fail-closed rule: if this phase was adopted by `SESSION_CONTRACT.md`, normal close is blocked until the Phase status update is recorded here or explicitly verified unchanged with rationale.

## Phase Entry Gate

This section must be completed before this phase can be adopted by an implementation-capable session.

| Entry gate check | Required result | Actual result | Evidence / pointer |
|---|---|---|---|
| Phase file exists | PASS | PENDING | |
| Delivery Plan pointer exists | PASS | PENDING | |
| Current System State pointer concordance | PASS | PENDING | |
| Lifecycle status supports adoption | READY_FOR_ADOPTION / ACTIVE / PARTIAL | PENDING | |
| Phase type supports implementation | GREENFIELD / BROWNFIELD / MIXED | PENDING | |
| Entry criteria explicit and satisfied | PASS | PENDING | |
| Exit criteria reviewable | PASS | PENDING | |
| Blocking open items absent/resolved | PASS | PENDING | |
| Adoption constraints satisfied | PASS | PENDING | |
| Correct next phase according to Delivery Plan and Current System State | PASS | PENDING | |

Entry gate status: PENDING / PASS / BLOCKED / UNCERTAIN

Fail-closed rule: implementation readiness is blocked unless `Entry gate status` is `PASS`.

### Greenfield Entry Gate Controls

Required when `Phase type` is `GREENFIELD` or `MIXED`.

| Greenfield entry control | Required result | Actual result | Evidence / pointer |
|---|---|---|---|
| MVP boundary is explicit | PASS | PENDING | |
| Primary user/workflow slice is explicit | PASS | PENDING | |
| Architecture dependency status is resolved enough for this phase | PASS | PENDING | |
| Prototype vs production intent is explicit | PASS | PENDING | |
| Out-of-scope expansion guard is explicit | PASS | PENDING | |

### Brownfield Entry Gate Controls

Required when `Phase type` is `BROWNFIELD` or `MIXED`.

| Brownfield entry control | Required result | Actual result | Evidence / pointer |
|---|---|---|---|
| Preservation baseline is explicit | PASS | PENDING | |
| Affected existing surfaces are identified | PASS | PENDING | |
| Regression-sensitive behavior is identified | PASS | PENDING | |
| Do-not-touch boundaries are explicit | PASS | PENDING | |
| Compatibility and data/migration safety constraints are considered when relevant | PASS | PENDING | |

## Phase Progress Ledger

Append one row per session that adopts or materially reviews this phase.

| Session/archive | Adopted scope | Completed items | Partial items | Blocked items | Deferred items | Evidence pointer | Resulting lifecycle status |
|---|---|---|---|---|---|---|---|
| | | | | | | | NOT_STARTED / READY_FOR_ADOPTION / ACTIVE / BLOCKED / PARTIAL / READY_FOR_ACCEPTANCE / ACCEPTED / DEFERRED / SUPERSEDED / CANCELLED |

Progress ledger rule: previous rows must not be erased. Corrections must be appended or explicitly marked as corrections.

## Carry-Forward Enforcement

Required when this phase is not fully accepted.

| Remaining item | Classification | Required next action | Carry-forward target | Blocking? | Owner/source |
|---|---|---|---|---:|---|
| | OPEN / PARTIAL / BLOCKED / DEFERRED / SUPERSEDED / CANCELLED | | same phase / next phase / CARRY_FORWARD.md / future session / cancellation rationale | YES / NO | |

Carry-forward status: NONE / RECORDED / BLOCKED / NOT_APPLICABLE

Fail-closed rule: if the resulting lifecycle status is `PARTIAL`, `BLOCKED`, or `DEFERRED`, `Carry-forward status` must be `RECORDED` or the close is blocked.

### Greenfield Progress Controls

Required when `Phase type` is `GREENFIELD` or `MIXED`.

| Control | Completed | Partial / remaining | Carry-forward target |
|---|---:|---|---|
| MVP boundary items | YES / NO / PARTIAL | | |
| Prototype-vs-production posture | YES / NO / PARTIAL | | |
| Architecture gaps | YES / NO / PARTIAL | | |
| Out-of-scope expansion guard | YES / NO / PARTIAL | | |

### Brownfield Progress Controls

Required when `Phase type` is `BROWNFIELD` or `MIXED`.

| Control | Completed | Partial / remaining | Carry-forward target |
|---|---:|---|---|
| Preservation baseline obligations | YES / NO / PARTIAL | | |
| Affected existing surfaces | YES / NO / PARTIAL | | |
| Regression-sensitive behavior | YES / NO / PARTIAL | | |
| Do-not-touch boundaries | YES / NO / PARTIAL | | |
| Migration/data-safety obligations | YES / NO / PARTIAL | | |


## Phase Acceptance Evidence Gate

- Acceptance gate status: PENDING / PASS / BLOCKED / NOT_APPLICABLE
- Phase acceptance evidence status: PENDING / COMPLETE / INCOMPLETE / BLOCKED / NOT_APPLICABLE
- All exit criteria satisfied or explicitly deferred/excluded: yes / no / not_applicable
- Session Contract Review acceptance verdict: ACCEPTED / PARTIAL / BLOCKED / FAILED / NOT_REVIEWED
- Implementation Unit evidence complete: yes / no / not_applicable
- Unresolved adopted work remaining: yes / no / not_applicable
- Delivery Plan status updated: yes / no / not_applicable
- Current System State pointers refreshed: yes / no / not_applicable

### Greenfield Acceptance Evidence

- Greenfield acceptance evidence: PENDING / COMPLETE / INCOMPLETE / BLOCKED / NOT_APPLICABLE
- MVP slice verified against phase objective: yes / no / not_applicable
- Architecture-to-implementation claims reconciled: yes / no / not_applicable
- Prototype-vs-production claims controlled: yes / no / not_applicable
- Known gaps carried forward or explicitly deferred: yes / no / not_applicable

### Brownfield Acceptance Evidence

- Brownfield acceptance evidence: PENDING / COMPLETE / INCOMPLETE / BLOCKED / NOT_APPLICABLE
- Preservation evidence complete: yes / no / not_applicable
- Affected surfaces reviewed: yes / no / not_applicable
- Regression-sensitive behavior reviewed: yes / no / not_applicable
- Compatibility/data-safety constraints reviewed: yes / no / not_applicable
- Do-not-touch boundaries respected: yes / no / not_applicable

### Mixed Acceptance Evidence

Mixed phase acceptance requires both Greenfield acceptance evidence and Brownfield acceptance evidence to be COMPLETE before final `ACCEPTED` lifecycle status is allowed.
