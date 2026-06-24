# Multi-Session Work

HIRMOS can handle small single-session tasks and larger multi-session deliveries.

Multi-session delivery is not required for every request. It becomes useful when the work is too large, risky, or stateful to complete honestly in one governed session.

## When multi-session work is useful

Use multi-session delivery when the work includes:

- several phases or releases;
- major architecture and implementation tracks;
- dependencies between design, implementation, validation, and rollout;
- significant unresolved decisions that should not block all progress;
- existing-system preservation, regression, compatibility, or migration-safety risk;
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
DELIVERY_BASELINE / delivery_baseline → delivery-baseline
DELIVERY_PHASE_SESSION / phase_session_baseline → phase-baseline → session-scope → implementation-readiness
```

For bounded single-session work, HIRMOS should avoid delivery artifacts and record why delivery governance is not applicable.


## PROD-L8.9 delivery baseline focus

HIRMOS always runs inside a governed runtime session envelope, but `SESSION_SCOPE.md` is required only when the active work has a bounded phase/session work scope. Durable delivery-baseline work uses `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` as active authority and `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` for delivery-level unresolved items.

Before delivery-baseline acceptance, HIRMOS records a complete phase coverage plan inside `DELIVERY_SCOPE.md` and does not instantiate future `PHASE-xx.md` files by default. After acceptance, HIRMOS instantiates the next phase/session authority just in time.

## Delivery baseline workflow

When durable multi-session governance is justified, HIRMOS first prepares a delivery baseline rather than immediately creating a phase/session implementation scope.

```text
hirmos start
→ session_focus: delivery_baseline
→ _hirmos/system/delivery/DELIVERY_PLAN.md
→ _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
→ _hirmos/system/delivery/<delivery-id>/unresolved-items.md
→ optional _hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md
→ optional _hirmos/system/delivery/<delivery-id>/DESIGN.md
→ Delivery Baseline — Review or Change
```

Before the delivery baseline is accepted, HIRMOS should not create `SESSION_SCOPE.md`, session unresolved items, implementation-unit files, or future `PHASE-xx.md` files by default.

`DELIVERY_SCOPE.md` must still include a complete phase coverage plan. That plan is the lightweight promise that planned phases cover the complete delivery scope even when future phase files are created just in time.

After delivery-baseline acceptance:

```text
hirmos continue
→ activate or amend the delivery baseline
→ instantiate only the next needed PHASE-xx.md by default
→ create the next SESSION_SCOPE.md
→ Session Baseline — Review or Change
```

Only after the session baseline is accepted should HIRMOS create implementation-unit files and begin implementation.

## Delivery-level unresolved items

Delivery-level gated items, non-gating assumptions, and technical-review items live with the delivery:

```text
_hirmos/system/delivery/<delivery-id>/unresolved-items.md
```

Session-level unresolved items live in `_hirmos/session/unresolved-items.md` only after a bounded session scope exists. A session may resurface an accepted delivery assumption when implementation discovers a blocker or invalid assumption. In that case, the session unresolved item must point back to the delivery decision and state whether delivery authority must be amended.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.
