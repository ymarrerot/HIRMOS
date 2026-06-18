# retry-escalation

## Execution Contract

### Purpose

Define a bounded retry, escalation, or route-back after a failed, partial, blocked, or route-back-required implementation unit review.

### Produces

- retry contract/evidence/review sections appended to the same `_hirmos/session/implementation-units/IU-xx.md` artifact
- `_hirmos/session/SESSION_EXECUTION.md` retry/escalation control update
- unresolved-item updates when retry changes assumptions, blockers, or user decisions

### Terminal States

- RETRY_READY — retry is bounded, evidence-based, and authorized inside the existing unit/session scope.
- ESCALATE — retry is not enough; user or supervisor input is required.
- ROUTE_BACK_REQUIRED — failure invalidates design/scope/current-state assumptions.
- BLOCKED — retry cannot proceed.
- NOT_APPLICABLE — retry/escalation is not needed.

## Activation triggers

- a unit review records FAIL, BLOCKED, PARTIAL, or ROUTE_BACK_REQUIRED
- retry or escalation is being considered

## Required inputs

- `_hirmos/session/SESSION_CONTRACT.md`
- `_hirmos/session/unresolved-items.md`
- failed/partial/blocked `_hirmos/session/implementation-units/IU-xx.md`

## Execution controls contributed

- retry / escalation control
- route-back control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/implementation-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

Retry is not a second attempt at arbitrary implementation. It must route back instead of retrying when scope or design is invalid.

Retry must:

1. Use evidence from the failed attempt.
2. Preserve the original Unit Contract.
3. Append a bounded retry section inside the same `IU-xx.md`.
4. State allowed retry scope and forbidden work.
5. State verification and escalation conditions.
6. Route back instead of retrying blindly if the failure exposes invalid scope, design, or current-state assumptions.

Do not create standalone `implementation-units/IU-xx.md` artifacts.




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

