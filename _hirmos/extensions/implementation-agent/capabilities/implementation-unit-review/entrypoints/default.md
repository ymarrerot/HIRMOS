# implementation-unit-review

## Execution Contract

### Purpose

Review one completed implementation unit against its own `IU-xx.md` Unit Contract, scope, validation, and evidence.

### Produces

- updated `_hirmos/session/implementation-units/IU-xx.md` Unit Review section
- retry or route-back decision inside the same IU artifact
- `_hirmos/session/SESSION_EXECUTION.md` unit-review control update

### Terminal States

- PASS — implementation satisfies 100% of the unit contract.
- PASS_WITH_LIMITATIONS — implementation is acceptable with explicit limitations.
- FAIL — implementation does not satisfy the unit contract.
- BLOCKED — review cannot complete due to missing evidence or blocker.
- ROUTE_BACK_REQUIRED — review exposes invalid design/scope/current-state assumptions.
- NOT_APPLICABLE — no unit review is required.

## Activation triggers

- an implementation unit execution record is complete or blocked
- unit completion is being considered

## Required inputs

- `_hirmos/session/SESSION_CONTRACT.md`
- `_hirmos/session/unresolved-items.md`
- target `_hirmos/session/implementation-units/IU-xx.md` with Execution Record and Evidence sections

## Execution controls contributed

- implementation unit review control
- retry / route-back decision control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/implementation-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.


Unit review is local, specific, and evidence-based. A unit is not complete until local review is recorded in the same `IU-xx.md` artifact.

The review must literally answer inside the IU artifact:

```text
Does the actual implementation satisfy 100% of this implementation unit contract?
Answer: YES / NO / PARTIAL.
Evidence:
Gaps:
Deferred items:
```

The review must compare:

- Unit Contract requirements to actual result;
- in-scope / out-of-scope conformance;
- validation requirements to actual evidence;
- requested runtime posture to delivered posture;
- claims to concrete file/log/runtime evidence.

Retry decisions must be recorded in the same `IU-xx.md` artifact under `## 6. Retries`. Do not create standalone retry-request artifacts.




## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific contract; do not execute from chat summaries or raw inputs alone.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

