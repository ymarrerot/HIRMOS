
# Delivery Unresolved Items

Status: delivery-level unresolved register.
Purpose: capture, classify, reconcile, dispose, carry, and revalidate delivery-level gated items, non-gating assumptions, technical-review items, blockers, and material uncertainty discovered while preparing or executing a durable delivery.

Canonical location:

```text
_hirmos/system/delivery/<delivery-id>/unresolved-items.md
```

## Authority Boundary

This file is subordinate to `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` and survives across all sessions that belong to the delivery.

Use this file for delivery-level uncertainty only. Do not store session-only blockers here unless they invalidate, amend, or materially challenge delivery authority.

Session-level unresolved items belong in `_hirmos/session/unresolved-items.md` after a `SESSION_SCOPE.md` exists. If a session-level item changes delivery truth, record or link the delivery impact here and amend `DELIVERY_SCOPE.md` when required.

## Current Checkpoint Feed

This section is the required source for the user-facing `Delivery Baseline — Review or Change` checkpoint.

### Gated delivery items

For each item:

- ID:
- Question / decision needed:
- Recommendation:
- Why this matters:
- Options / answer format:
- Downstream impact if unresolved:
- Status: OPEN | ANSWERED | DEFERRED | BLOCKED | NOT_APPLICABLE

### Non-gating delivery assumptions

For each item:

- ID:
- Assumption:
- Why non-gating:
- Risk:
- Revalidation point:
- Status: CARRIED | REVALIDATED | SUPERSEDED | BLOCKED

### Technical-review delivery items

For each item:

- ID:
- Decision / assumption:
- Why it matters:
- Inspectable artifact/path:
- Challenge/change path:
- Status: REVIEWABLE | ACCEPTED | CHANGED | BLOCKED

## Delivery Baseline Disposition

| Item ID | Classification | Decision / disposition | Reflected in delivery authority? | Evidence / pointer |
|---|---|---|---:|---|
| | gated / non-gating / technical-review | | YES / NO / NOT_APPLICABLE | |

## Phase / Session Inheritance

| Item ID | Affects phase/session | Required inheritance action | Session unresolved item needed? | Status |
|---|---|---|---:|---|
| | `PHASE-xx` / session / delivery-close | | YES / NO | PENDING |

## Delivery Close Review

At delivery close, HIRMOS must verify that every open delivery-level item is accepted, deferred with carry-forward, superseded, or explicitly blocking the delivery verdict.

## PROD-L8.26 Live-Only Close Reconciliation

At delivery close, this register should contain live delivery-level unresolved items only. Items resolved by accepted phase/session work must be marked `SUPERSEDED`, `ACCEPTED`, `REVALIDATED`, or moved into a compact resolved-history note; they must not remain current `OPEN`, `CARRIED`, `REVIEWABLE`, or `PENDING` if accepted artifacts contradict them.

Close must classify each item as one of:

- `RECONCILED` — resolved or adopted by accepted phase/session work;
- `CARRY_FORWARD` — still active and intentionally carried;
- `BLOCKING` — prevents delivery close;
- `SUPERSEDED` — no longer current due to accepted delivery/phase/session outcome;
- `NOT_APPLICABLE` — no longer relevant.

Do not preserve stale open delivery assumptions as active truth after a delivery is closed or accepted with limitations.
