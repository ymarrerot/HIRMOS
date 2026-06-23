# Scope Authority Surfaces Example

This example shows the smallest authority surface HIRMOS should create for common work shapes.

## Bounded single-session work

```text
_hirmos/session/
  SESSION_STATE.json
  SESSION_SCOPE.md
  SESSION_EXECUTION.md
  unresolved-items.md
  bootstrap/

  EVIDENCE.md                   # conditional
  implementation-units/         # conditional
  stack-resolution.json         # conditional
```

No delivery artifacts are required when the work can be governed safely in one session.

## Durable multi-session delivery

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md
  mvp/
    DELIVERY_SCOPE.md
    phases/
      PHASE-01.md
```

`DELIVERY_PLAN.md` is the durable roadmap/register. It is updated, not overwritten, when later durable multi-session work adds a delivery. `DELIVERY_SCOPE.md` is the scoped authority for one delivery/release. `SESSION_SCOPE.md` adopts and narrows this authority during an active session.

## Close/archive

Closed sessions are archived under:

```text
_hirmos/system/history/sessions/<session-id>/
  ARCHIVE_MANIFEST.md
```

The archive manifest records the close/archive transaction. It is not accepted current state by itself.
