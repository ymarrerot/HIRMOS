# System Design Unresolved Item Contribution Binding

## Purpose

Bind the framework-wide unresolved-item contribution contract to the `system-design-agent:system-design` lifecycle.

The shared unresolved-item artifact schemas and traceability requirements are governed by:

```text
/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md
```

This file defines only the System Design lifecycle binding. It must not redefine the shared schema.

## Lifecycle binding

Lifecycle:

```text
system-design-agent:system-design
```

Lifecycle spec that owns sequencing, completion gating, and fail-closed behavior:

```text
/_hirmos/extensions/system-design-agent/specs/system-design.spec.md
```

Canonical project-level unresolved-item artifact root:

```text
/_hirmos/artifacts/context/project/
```

Covered artifacts:

```text
/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
```

## System Design producers covered by this lifecycle

The current System Design lifecycle may collect unresolved items from system-design-stage producers and declared hook contributions into the project-level canonical inventory. Producer contributions must be refreshed inline before the producer or hook workflow exits.

Requirements-stage producers belong to `requirements-agent`. System Design consumes the project-level canonical unresolved inventory and Requirements outputs as prior-stage inputs rather than re-owning Requirements unresolved decisions.

## System Design-specific gating posture

System Design must pause when unresolved items materially affect one or more of:

- architecture / deployment shape;
- system model correctness;
- component boundaries;
- integration contracts;
- phase roadmap validity;
- staged delivery targets;
- downstream implementation readiness;
- unresolved Requirements outputs that remain gating for safe design.

## Ownership boundaries

- `system-design.spec.md` owns System Design workflow, terminal-state composition, and completion gating for the current step.
- Producer specs own local unresolved-item surfacing inside their artifacts.
- `/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md` owns shared schemas and traceability requirements.
