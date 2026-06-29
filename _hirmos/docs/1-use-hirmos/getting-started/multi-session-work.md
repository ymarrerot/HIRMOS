# Multi-Session Work

Use durable delivery for multi-session work when a request is too large, risky, or long-running to finish honestly in one governed session.

HIRMOS still follows the same lifecycle:

```text
Understand System State → Design → Implementation → Update System State
```

Multi-session work changes the work shape. HIRMOS creates durable delivery authority before individual implementation sessions.

## When to use durable delivery

Use durable delivery for multi-session work when the request needs:

- multiple implementation phases;
- durable requirements/design decisions across sessions;
- staged acceptance;
- carry-forward items that must survive session close;
- visible release/delivery scope.

Do not use durable delivery just because the project is important. Small bounded work can remain a single-session governed route.

## Delivery route

A typical durable flow is:

```text
hirmos start "Build <larger outcome>"
→ Delivery Baseline — Review or Change
→ accept or change delivery baseline
→ next phase/session baseline
→ IU Planning when needed
→ IU Execution after IU plan acceptance
→ close/update system state
→ next session starts from current state
```

## Delivery authority

Durable delivery authority lives under:

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md
  <delivery-id>/
    DELIVERY_SCOPE.md
    unresolved-items.md
    phases/
      PHASE-xx.md
```

`DELIVERY_PLAN.md` is the roadmap/register and pointer surface. `DELIVERY_SCOPE.md` owns stable delivery authority. Phase files own the scope of a phase when a phase is instantiated.

These artifacts should not become duplicate mutable status reports. Completion posture should be derived from accepted phase/session artifacts, archive manifests, current-state pointers, and close evidence.

## Delivery Baseline — Review or Change

A Delivery Baseline should show:

- the delivery goal;
- the smallest honest delivery shape;
- phase or delivery-unit plan;
- gated decisions;
- non-gating assumptions;
- technical-review items;
- what will be created now and what will be created just in time later.

Before baseline acceptance, HIRMOS should not create future phase files by default. It should plan the phases and instantiate the next phase/session authority when that work becomes active.

## Phase/session execution

After delivery baseline acceptance, HIRMOS starts the next bounded phase/session. A phase/session baseline should adopt the accepted delivery authority and define the session scope.

When implementation units are needed, the flow is:

```text
Session Baseline accepted
→ IU Planning only
→ IU Plan — Review or Change
→ IU Plan accepted
→ IU Execution
```

Implementation must not begin from the delivery plan alone.

## Delivery-level unresolved items

Delivery-level gated items, non-gating assumptions, and technical-review items live with the delivery:

```text
_hirmos/system/delivery/<delivery-id>/unresolved-items.md
```

Session-level unresolved items live in `_hirmos/session/unresolved-items.md` only after a bounded session scope exists. A session may resurface an accepted delivery assumption when implementation discovers a blocker or invalid assumption. In that case, the session unresolved item should point back to the delivery decision and state whether delivery authority must be amended.

## Close and carry-forward

At close, HIRMOS should update current system state with accepted outcomes and pointers. It should preserve carry-forward items without pretending they are complete.

A stale status row is worse than no status row when it can mislead the next session. Prefer derived pointer indexes and source-artifact references over repeated mutable status fields.
