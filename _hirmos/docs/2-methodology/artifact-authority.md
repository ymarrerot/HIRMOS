# Artifact Authority

HIRMOS artifacts are useful only when each artifact has a clear ownership role.

The rule is:

```text
One fact should have one canonical owner.
Other artifacts should point to it or derive from it.
```

## Core authority surfaces

| Concern | Canonical authority |
|---|---|
| Active session scope | `_hirmos/session/SESSION_SCOPE.md` |
| Session command/gate progress | `_hirmos/session/SESSION_LEDGER.md` |
| Session unresolved items | `_hirmos/session/unresolved-items.md` |
| IU authority and review | `_hirmos/session/implementation-units/IU-xx.md` |
| Evidence detail | `_hirmos/session/EVIDENCE.md` when evidence volume requires it |
| Accepted current-state navigation | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` |
| Delivery roadmap/register | `_hirmos/system/delivery/DELIVERY_PLAN.md` |
| Delivery authority | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` |
| Phase authority | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` |

## Delivery authority

For durable multi-session delivery, a Delivery Plan is needed. Separate phase files are required only when the selected delivery shape needs ordered staged delivery.

Durable delivery authority lives under `_hirmos/system/delivery/<delivery-id>/`, not under `_hirmos/session/`. Active sessions consume accepted delivery/phase authority through `SESSION_SCOPE.md` and implementation units.

## Optional authority

Separate `REQUIREMENTS.md` or `DESIGN.md` files are optional. Create them only when separate authority materially improves clarity, reviewability, or safety.

| Level | Default authority | Optional authority when justified |
|---|---|---|
| Delivery | `system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | delivery `REQUIREMENTS.md` / `DESIGN.md` |
| Session | `session/SESSION_SCOPE.md` | session `REQUIREMENTS.md` / `DESIGN.md` |

## Avoid duplicated mutable status

Do not ask the model to maintain the same status in several artifacts.

Examples of values that should be derived or pointed to instead of duplicated:

- delivery completion posture;
- phase progress posture;
- next command recommendation;
- accepted close history;
- evidence summaries already owned by IU/evidence records.

A stale status row is worse than an absent row when it can mislead the next action.

## Just-in-time artifacts

Optional artifacts should be created when they are needed, not pre-created as empty placeholders. This keeps the runtime surface smaller and reduces synchronization failures.


## Source authority minimality

Use the narrowest source authority that can safely own the concern. Do not promote a detail to delivery, current-state, or reference authority when session or IU authority is sufficient.


## Source authority location matrix

| Concern | Preferred authority level |
|---|---|
| accepted-state navigation | `CURRENT_SYSTEM_STATE.md` |
| delivery scope | `DELIVERY_SCOPE.md` |
| phase scope | `PHASE-xx.md` |
| session scope | `SESSION_SCOPE.md` |
| unit execution | `IU-xx.md` |
| detailed evidence | `EVIDENCE.md` or IU evidence rows |

CURRENT_SYSTEM_STATE.md is the accepted-state navigation authority. It should point to source artifacts instead of duplicating their detailed content.
