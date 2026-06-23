# design-agent

Status: bundled extension.
Purpose: support the Design lifecycle stage with governed requirements, system/application design, durable delivery planning, phase contracts, Session Scopes, technical review, and implementation-readiness capabilities.

Read `entrypoints/default.md` before running any design-agent capability; it contains the shared Design method and routing contract.

## Capabilities

- `requirements-design`
- `system-design`
- `delivery-design`
- `phase-contracting`
- `session-scope`
- `technical-review`
- `implementation-readiness`

## Responsibility boundary

The extension supports Design. Core owns the lifecycle, commands, execution controls, artifact model, interaction modes, unresolved-item governance, and accepted-state safety.

Design outputs are authority for downstream Implementation only when they are recorded in active-session artifacts and required execution controls are satisfied.


## Durable delivery capability chain

When the selected delivery shape requires durable delivery, Design must route through:

```text
delivery-design → phase-contracting → session-scope → implementation-readiness
```

The durable Delivery Plan roadmap, Delivery Scope, and Phase files live under `_hirmos/system/delivery/<delivery-id>/`. The active session consumes them through `SESSION_SCOPE.md`; it does not create session-local delivery authority.
