# Example: system-design-agent paused cycle

This example shows the expected shape of a serious paused planning run.

## Command

```text
cmd: run extension system-design-agent:system-design-cycle
```

## Example terminal block

```text
Command: cmd: run extension system-design-agent:system-design-cycle
Run state: paused
Artifacts updated:
- _hirmos/artifacts/context/system-design-agent/REQUIREMENTS_INPUT_PACK.md
- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md
- _hirmos/artifacts/sot/SYSTEM_SOT.md
- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md
- _hirmos/artifacts/sot/PHASES_SOT.md
- _hirmos/artifacts/context/system-design-agent/system-design-cycle/CYCLE_STATUS.md
- _hirmos/artifacts/context/system-design-agent/system-design-cycle/DECISION_LOG.md
- _hirmos/artifacts/context/system-design-agent/system-design-cycle/VALIDATION_TRACE.md
- _hirmos/artifacts/context/system-design-agent/system-design-cycle/RUN_TRACE.md
- _hirmos/artifacts/context/system-design-agent/system-design-cycle/CYCLE_STATE_REPORT.md
Summary:
- Cycle state: paused pending Orchestrator direction
- Non-gating unresolved items:
  - Anonymous duplicate-prevention details
    - Classification: Proceed-with-caution
    - Handling answer: use bounded session-token duplicate prevention and rate limiting until stronger controls are explicitly required
    - Visible downstream: yes
- Gated unresolved items:
  - Identity and duplicate-prevention model
  - Event/session scope and concurrency model
  - Supported poll-type scope for MVP
  - Expected scale and latency targets
- Why they matter:
  - Identity and duplicate-prevention materially change participation rules and vote-validity behavior.
  - Event/session scope materially changes workflow shape and architecture direction.
  - Poll-type scope materially changes authoring, validation, aggregation, and export logic.
  - Scale and latency materially affect real-event readiness and degraded-mode planning.
- Allowed outcomes:
  - use assumption
  - ask customer
  - defer and constrain
- Proposed Orchestrator direction:
  - Identity / duplicate prevention
    - Suggested direction: ask customer
    - Rationale: this changes core product behavior and data handling.
  - Event/session scope / concurrency
    - Suggested direction: ask customer
    - Rationale: this changes workflow and system boundaries materially.
  - Poll types
    - Suggested direction: defer and constrain
    - Rationale: a bounded MVP scope keeps the planning set governable.
  - Scale / latency targets
    - Suggested direction: ask customer
    - Rationale: real-event readiness cannot be judged honestly without targets.
- Continuation options:
  - accept all proposed directions
  - modify one or more proposed directions
  - ask for customer-question drafting
- Advisory note:
  - Proposed directions are advisory only and were not applied as decisions.
Next action: review `_hirmos/artifacts/context/system-design-agent/system-design-cycle/CYCLE_STATE_REPORT.md`, record decisions for the gated unresolved items, and rerun system-design-agent:system-design-cycle.
```

In an installed `system-design-agent` package, use that extension's paused-run template as the authoritative field set for the terminal block shape.