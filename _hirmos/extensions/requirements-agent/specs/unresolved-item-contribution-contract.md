# Requirements Unresolved Item Contribution Binding

## Purpose

Bind the framework-wide unresolved-item contribution contract to the `requirements-agent:requirements` lifecycle.

The shared unresolved-item artifact schemas and traceability requirements are governed by:

```text
/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md
```

This file defines only the Requirements lifecycle binding. It must not redefine the shared schema.

## Lifecycle binding

Lifecycle:

```text
requirements-agent:requirements
```

Lifecycle spec that owns sequencing, completion gating, and fail-closed behavior:

```text
/_hirmos/extensions/requirements-agent/specs/requirements.spec.md
```

Canonical project-level unresolved-item artifact root:

```text
/_hirmos/artifacts/context/requirements-agent/requirements/
```

Covered artifacts:

```text
/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
```

## Requirements producers covered by this lifecycle

The Requirements lifecycle may collect unresolved items from these Requirements producers:

```text
/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
```

Additional requirements-stage hook contributions may be accepted only through declared hooks and must preserve producer/artifact-scoped attribution. Producer contributions must be refreshed inline before the producer or hook workflow exits.

## Requirements-specific gating posture

Requirements must pause when unresolved items materially affect one or more of:

- core scope boundaries;
- actor or identity model;
- workflow shape;
- requirements acceptance expectations;
- data requirements;
- security/privacy/compliance posture;
- delivery-target feasibility;
- downstream System Design validity.

If a safe assumption is made, it must be explicitly recorded and preserved for downstream review.

## Prohibited bypass artifacts

Do not create or use:

```text
Requirements-only unresolved-decision bypass artifact
```

Use the shared unresolved-item artifact names under the project-level canonical context.

## Ownership boundaries

- `requirements.spec.md` owns Requirements workflow, terminal-state composition, and completion gating.
- `requirements-input-pack.spec.md` and `requirements-sot.spec.md` own local unresolved-item surfacing inside their producer artifacts.
- `/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md` owns shared schemas and traceability requirements.
