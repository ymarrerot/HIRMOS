# Example: Scope Authority Surfaces

HIRMOS uses the smallest authority surface that can safely govern the work.

## Single-session work

```text
_hirmos/session/
  SESSION_STATE.json
  SESSION_LEDGER.md
  SESSION_SCOPE.md
  unresolved-items.md        # only when material unresolved items exist
  implementation-units/      # only when IU mode applies
```

`SESSION_SCOPE.md` owns active session scope. `SESSION_LEDGER.md` records command/gate progress and pointers. IU files own IU authority when implementation units are required.

## Durable delivery work

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md
  <delivery-id>/
    DELIVERY_SCOPE.md
    unresolved-items.md
    phases/
      PHASE-xx.md            # created just in time
```

Delivery artifacts own durable delivery authority. Session artifacts consume that authority when a bounded phase/session begins.

## Accepted current state

```text
_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md
```

Current System State is a navigation and accepted-state pointer surface. It should not duplicate detailed delivery scope, phase progress, evidence, or session logs. Derived pointer indexes can be regenerated from source artifacts when needed.
