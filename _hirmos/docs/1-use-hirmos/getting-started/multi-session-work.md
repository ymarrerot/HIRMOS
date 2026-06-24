# Multi-Session Work

HIRMOS can handle small single-session tasks and larger multi-session deliveries.

Multi-session delivery is not required for every request. It becomes useful when the work is too large, risky, or stateful to complete honestly in one governed session.

## When multi-session work is useful

Use multi-session delivery when the work includes:

- several phases or releases;
- major architecture and implementation tracks;
- dependencies between design, implementation, validation, and rollout;
- significant unresolved decisions that should not block all progress;
- brownfield preservation risk;
- work that must carry context across multiple AI conversations.

## What changes in a larger delivery

For larger work, HIRMOS may create durable delivery artifacts under:

```text
_hirmos/system/delivery/
```

A delivery can include:

- a top-level `_hirmos/system/delivery/DELIVERY_PLAN.md` that acts as the durable roadmap/register;
- one `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` per durable delivery or release;
- phase files such as `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` when phase-level contracts are useful;
- phase lifecycle state, entry gates, progress, carry-forward items, and acceptance evidence.

The active session still uses normal session artifacts. `SESSION_SCOPE.md` adopts and narrows delivery/phase authority instead of duplicating the entire delivery scope.

## Single-session work is still valid

Not every task needs a delivery plan or phases.

A small fix, narrow refactor, docs update, or bounded feature may only need:

```text
hirmos start
→ hirmos continue
→ hirmos close
```

A good HIRMOS run should not make small work feel heavy just because the framework can support larger delivery.

## How continuation should feel

Across sessions, HIRMOS should preserve:

- what was accepted;
- what was rejected or not applied;
- what remains unresolved;
- what phase or delivery state is active;
- what evidence was produced;
- what the next session should know before doing more work.

The user should not have to re-explain the entire project every time.

## What to inspect

For multi-session work, inspect:

- `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`
- `_hirmos/system/delivery/DELIVERY_PLAN.md` and `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- archived session records under `_hirmos/system/history/sessions/`
- active `unresolved-items.md` and session review artifacts when a session is open

## What to watch for

Be cautious if HIRMOS:

- creates delivery/phase artifacts for simple work without need;
- loses unresolved items between sessions;
- marks a phase accepted without evidence;
- closes a session without updating current state;
- reports progress but cannot point to accepted artifacts.


## PROD-L3 delivery roadmap/register model

For durable multi-session work, HIRMOS uses:

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md
  <delivery-id>/
    DELIVERY_SCOPE.md
    phases/
      PHASE-xx.md
```

`DELIVERY_PLAN.md` is the durable roadmap/register. It is updated, not overwritten, when later durable multi-session work adds another delivery. Each `DELIVERY_SCOPE.md` is the scoped authority for one delivery/release. Phase files are conditional and are used only when separate phase scopes improve continuity, evidence, or reviewability.

## Runtime behavior after PROD-L4

For multi-session work, HIRMOS does not just create delivery files. Runtime commands route through delivery capabilities:

```text
MULTI_SESSION_DELIVERY → delivery-design → session-scope → implementation-readiness
MULTI_SESSION_DELIVERY_WITH_PHASE_FILES → delivery-design → phase-contracting → session-scope → implementation-readiness
```

For bounded single-session work, HIRMOS should avoid delivery artifacts and record why delivery governance is not applicable.
