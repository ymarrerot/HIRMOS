# Example: system-design-agent paused System Design run

This example shows the expected shape of a serious paused System Design run using the current public default command.

## Command

```text
hirmos system-design
```

## Example terminal block

```text
Command: hirmos system-design
Resolved entrypoint: system-design
Run state: paused

Artifacts updated:
- _hirmos/artifacts/sot/SYSTEM_SOT.md
- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md
- _hirmos/artifacts/sot/PHASES_SOT.md
- _hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
- _hirmos/artifacts/context/system-design-agent/system-design/VALIDATION_TRACE.md
- _hirmos/artifacts/context/system-design-agent/system-design/RUN_TRACE.md

Summary:
- System Design state: paused pending Orchestrator direction
- Requirements source: _hirmos/artifacts/sot/REQUIREMENTS_SOT.md
- Gated unresolved items:
  - Event/session scope and concurrency model
  - Supported poll-type scope for MVP
  - Expected scale and latency targets
- Why they matter:
  - Event/session scope materially changes workflow and architecture boundaries.
  - Poll-type scope materially changes authoring, validation, aggregation, and export logic.
  - Scale and latency materially affect real-event readiness and degraded-mode planning.
- Allowed outcomes:
  - use assumption
  - ask customer
  - defer and constrain
- Proposed Orchestrator direction:
  - Event/session scope / concurrency
    - Suggested direction: ask customer
  - Poll types
    - Suggested direction: defer and constrain
  - Scale / latency targets
    - Suggested direction: ask customer
- Advisory note:
  - Proposed directions are advisory only and were not applied as decisions.
Next action: record decisions for the gated unresolved items and rerun `hirmos system-design`.
```

In an installed `system-design-agent` package, use that extension's System Design templates as the authoritative field set for the terminal block shape.
