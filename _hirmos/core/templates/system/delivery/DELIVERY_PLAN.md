# Delivery Plan

Status: DRAFT | ACTIVE | COMPLETE | SUPERSEDED | BLOCKED
Delivery ID:
Project type: GREENFIELD | BROWNFIELD | MIXED | UNKNOWN
Created from session:
Last updated from session:

## Authority

This is the durable multi-session delivery authority for the delivery ID above.

For durable multi-session delivery, a Delivery Plan is needed. Separate phase files are required only when the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

Canonical location:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
```

Phase contracts live under:

```text
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

Session-local delivery artifacts are not canonical delivery authority.

## Phase Lifecycle Vocabulary

All phase rows in this Delivery Plan must use the canonical phase lifecycle status vocabulary from `_hirmos/core/protocol/PHASE_LIFECYCLE.md`:

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

All phase rows must declare one canonical phase type:

```text
GREENFIELD
BROWNFIELD
MIXED
UNKNOWN
```

`UNKNOWN` phase type blocks implementation readiness until current-state understanding classifies the phase as `GREENFIELD`, `BROWNFIELD`, or `MIXED`.

## Delivery Shape Source

Compatibility label: Delivery-Need Classification Source.

- Delivery shape: SINGLE_SESSION_VERTICAL_SLICE | SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS | MULTI_SESSION_DELIVERY | MULTI_SESSION_DELIVERY_WITH_PHASE_FILES
- Why this shape is necessary:
- Why smaller shape was insufficient:
- Why phase files are / are not needed:

## Delivery Shape Decision Source

- Classification answer: YES | NO | UNCERTAIN
- Classification evidence:
- Greenfield triggers present:
- Brownfield triggers present:
- Universal triggers present:
- Why durable delivery governance is required:
- If adopted from prior work, source artifact/session:

## Delivery Objective

- User-visible outcome:
- Business/product/system objective:
- Non-goals:
- Success definition:

## Governing Inputs

| Source | Type | Relevance | Coverage status |
|---|---|---|---|
| | requirements / current-state / user request / design / archive | | NOT_ASSESSED |

## Delivery Decomposition

| Phase ID | Phase file | Phase title | Phase type | Lifecycle status | Objective | Depends on | Exit summary |
|---|---|---|---|---|---|---|---|
| PHASE-01 | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-01.md` | | GREENFIELD / BROWNFIELD / MIXED / UNKNOWN | NOT_STARTED | | | |

Lifecycle status compatibility:

- Implementation adoption may use only `READY_FOR_ADOPTION`, `ACTIVE`, or `PARTIAL`.
- Review/close-only work may use `READY_FOR_ACCEPTANCE`.
- `UNKNOWN`, `NOT_STARTED`, `BLOCKED`, `ACCEPTED`, `DEFERRED`, `SUPERSEDED`, or `CANCELLED` does not authorize implementation readiness.

## Cross-Phase Constraints

- Preservation constraints:
- Architecture constraints:
- Runtime/integration constraints:
- UX/operator constraints:
- Data/security/privacy constraints:
- Validation strategy:

## Delivery Coverage Matrix

| Requirement / accepted-state need | Covered by phase(s) | Deferred? | Evidence / rationale |
|---|---|---:|---|
| | | NO | |

## Active Development Context

- Current active phase:
- Current active phase lifecycle status:
- Current active phase type:
- Current/next session source:
- Current blockers:
- Carry-forward items:

## Delivery Status Update Log

| Date/session | Change | Phase affected | Previous lifecycle status | New lifecycle status | Evidence |
|---|---|---|---|---|---|
| | | | | | |

## Close / Acceptance Rules

A phase may be marked `ACCEPTED` only when a closed session verifies its Session Contract, implementation units, evidence, unresolved items, and current-state update responsibilities.

The Delivery Plan may recommend the next phase, but it does not authorize implementation by itself. Implementation authority flows through the active `SESSION_CONTRACT.md` and implementation units.

## Close-Time Delivery Status Update Contract

This section must be updated during `hirmos close` whenever a session accepts, partially accepts, blocks, supersedes, defers, cancels, or advances a phase in this Delivery Plan.

| Close session | Adopted phase | Phase type | Previous lifecycle status | New lifecycle status | Delivery status impact | Evidence / archive | Applied? |
|---|---|---|---|---|---|---|---:|
| | | GREENFIELD / BROWNFIELD / MIXED / UNKNOWN | | | | | yes / no / not_applicable |

Required close-time checks:

- The adopted phase row in `Delivery Decomposition` reflects the session outcome.
- The `Delivery Status Update Log` records the close session and archive evidence.
- The next recommended phase is updated or explicitly left unchanged with rationale.
- Carry-forward items are mapped to the next phase, `CARRY_FORWARD.md`, or a blocked delivery note.
- Current System State delivery pointers agree with this Delivery Plan.

Fail-closed rule: a governed delivery session must not claim normal close success if this Delivery Plan was required but its lifecycle status row, update log, next-phase recommendation, or carry-forward disposition is stale or missing.
