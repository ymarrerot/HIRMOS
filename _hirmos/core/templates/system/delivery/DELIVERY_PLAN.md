# Delivery Plan

Status: DRAFT | ACTIVE | COMPLETE | SUPERSEDED | BLOCKED
Last updated from session:

## Purpose

This file is the durable project delivery roadmap/register. It indexes one or more durable deliveries and preserves completed, active, planned, deferred, cancelled, superseded, and blocked delivery history.

Canonical location:

```text
_hirmos/system/delivery/DELIVERY_PLAN.md
```

`DELIVERY_PLAN.md` is append/update-oriented. It must not be overwritten when new durable multi-session work appears later. New durable multi-session work adds a new delivery entry and creates a corresponding `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` while preserving prior delivery entries.

## Authority Boundary

`DELIVERY_PLAN.md` is the roadmap/register. It does not contain the full scoped authority for a delivery and does not authorize implementation by itself.

Authority flows through:

```text
CURRENT_SYSTEM_STATE.md
→ _hirmos/system/delivery/DELIVERY_PLAN.md
→ _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
→ _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md when phase files are used
→ _hirmos/session/SESSION_SCOPE.md
→ implementation-units / EVIDENCE / SESSION_EXECUTION.md
```

## Delivery Shape Source

Compatibility label: Delivery-Need Classification Source.

- Delivery shape: SINGLE_SESSION_VERTICAL_SLICE | SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS | MULTI_SESSION_DELIVERY | MULTI_SESSION_DELIVERY_WITH_PHASE_FILES
- Why durable delivery governance is / is not necessary:
- Why smaller shape was insufficient when delivery governance is active:
- Why phase files are / are not needed:

## Delivery Shape Decision Source

- Classification answer: YES | NO | UNCERTAIN
- Classification evidence:
- Greenfield triggers present:
- Brownfield triggers present:
- Universal triggers present:
- If adopted from prior work, source artifact/session:

## Delivery Index

| Delivery ID | Name | Status | Type | Scope file | Current/Final phase | Relationship |
|---|---|---|---|---|---|---|
| `<delivery-id>` | | planned / active / completed / partial / blocked / deferred / superseded / cancelled | MVP / release / hardening / migration / brownfield-change / other | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | none / `PHASE-xx` | initial / follows / supersedes / depends-on / blocks |

## Delivery Relationships

- Sequence constraints:
- Dependencies between deliveries:
- Supersedes / follows / blocks relationships:
- Shared constraints:

## Accepted-State Pointers

- Current system state: `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`
- Carry-forward: `_hirmos/system/accepted-state/CARRY_FORWARD.md`
- Decision log: `_hirmos/system/accepted-state/DECISION_LOG.md`

## Active Delivery

- Active delivery ID: none / `<delivery-id>`
- Active delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Current phase: none / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- Current/next session source:
- Current blockers:
- Carry-forward items:

## Delivery Navigation

This section makes delivery-to-delivery continuation explicit for future `hirmos start` runs. It is navigation metadata, not implementation authority.

- Last accepted delivery: none / `<delivery-id>`
- Active delivery: none / `<delivery-id>`
- Active delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Next recommended delivery: none / `<delivery-id>`
- Next recommended delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Selection rationale:
- User override / unrelated-task rule: if the user provides an unrelated task, `hirmos start` must run current-state understanding before adopting this recommendation.

## Delivery Coverage Matrix

| Delivery / accepted-state need | Delivery scope | Covered by phase(s) | Deferred? | Evidence / rationale |
|---|---|---|---:|---|
| | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | none / `PHASE-xx` | NO | |

## Delivery Status Update Log

| Date/session | Delivery | Change | Previous status | New status | Evidence |
|---|---|---|---|---|---|
| | | | | | |

## Completion / Close Rules

- A delivery is complete only when its `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` close verification passes.
- Accepted-state files must point to completed and active deliveries when durable delivery governance exists.
- New durable multi-session work must add or update a delivery entry rather than overwrite prior delivery history.
- When a delivery completes and a planned follow-up delivery is related by `follows`, `depends-on`, or an explicit sequence constraint, close must refresh Delivery Navigation and `CURRENT_SYSTEM_STATE.md` next-delivery pointers.
- The roadmap may recommend an active delivery or next phase, but implementation authority must be narrowed into `SESSION_SCOPE.md` before implementation.

## Close-Time Delivery Status Update Contract

This section must be updated during `hirmos close` whenever a session accepts, partially accepts, blocks, supersedes, defers, cancels, or advances a delivery in this roadmap/register.


## Delivery Decomposition

Compatibility section. Delivery decomposition is represented by Delivery Index entries, each delivery's DELIVERY_SCOPE.md Phase Plan, and conditional PHASE-xx.md files.


## Active Development Context

- Active delivery:
- Active delivery scope:
- Current phase:
- Next recommended delivery:
- Next recommended delivery scope:
- Next recommended phase:
- Current blockers:
