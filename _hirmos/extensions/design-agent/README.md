# design-agent

Status: bundled extension.
Purpose: support the Design lifecycle stage with governed requirements, system/application design, delivery-baseline planning, phase/session baselines, Session Scopes, technical review, and implementation-readiness capabilities.

Read `entrypoints/default.md` before running any design-agent capability; it contains the shared Design method and routing authority.

## Capabilities

- `requirements-design`
- `system-design`
- `delivery-baseline`
- `phase-baseline`
- `delivery-design`
- `phase-contracting`
- `session-scope`
- `technical-review`
- `implementation-readiness`


## Responsibility boundary

The extension supports Design. Core owns the lifecycle, commands, execution controls, artifact model, interaction modes, unresolved-item governance, and accepted-state safety.

Design outputs are authority for downstream Implementation only when they are recorded in active-session artifacts and required execution controls are satisfied.


## Focus-aware durable delivery capability chain

When the selected route requires durable delivery, Design first routes through a delivery-baseline focus before phase/session authority exists:

```text
DELIVERY_BASELINE / delivery_baseline
  delivery-baseline
```

After the delivery baseline is accepted or amended, Design routes into the next phase/session baseline:

```text
DELIVERY_PHASE_SESSION / phase_session_baseline
  phase-baseline → session-scope → implementation-readiness
```

Legacy capability names remain installed only as subordinate implementation surfaces. Runtime command behavior must use the focus-aware route from `_hirmos/core/protocol/CAPABILITY_ROUTING.md`. The durable Delivery Plan roadmap, Delivery Scope, delivery unresolved register, optional delivery requirements/design, and just-in-time phase files live under `_hirmos/system/delivery/<delivery-id>/`. The active session consumes accepted delivery/phase authority through `SESSION_SCOPE.md`; it must not create session-local delivery authority.
