# retry-escalation

## Execution Contract

### Purpose

Define a bounded append-only retry, escalation, or route-back after a failed, partial, blocked, or route-back-required implementation unit review.

### Produces

- retry contract/evidence/review sections appended to the same `_hirmos/session/implementation-units/IU-xx.md` artifact without editing sealed contract sections
- `_hirmos/session/SESSION_LEDGER.md` retry/escalation control update
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

- `_hirmos/session/SESSION_SCOPE.md`
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
2. Preserve the original sealed Unit Scope / Authority.
3. Append a bounded retry section inside the same `IU-xx.md` without editing sealed contract sections.
4. State allowed retry scope and forbidden work.
5. State verification and escalation conditions.
6. Route back instead of retrying blindly if the failure exposes invalid scope, design, current-state assumptions, acceptance criteria, or contract authority.

Do not create standalone `implementation-units/IU-xx.md` artifacts, and do not modify sealed IU contract authority to make a retry pass.




## Required behavior

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## PROD-L8.25 Retry Mutation Guard

A retry may append evidence and review records within the same IU only when it remains inside the sealed contract. If the retry requires new scope, different source authority, changed acceptance criteria, or modified implementation requirements, record `ROUTE_BACK_REQUIRED` and create a new/reopened sealed contract version before further material edits.

## PROD-L8.28 Retry Boundary for Thin or Incomplete IUs

A thin, incomplete, unreviewed, or status-contradictory generated IU is not a normal retry target after implementation. If discovered before archive, route back to active IU planning/review and either complete the active artifact honestly or mark the session partial/blocked. If discovered after archive, apply PROD-L8.27 archive immutability and record the historical governance defect instead of expanding archived authority.
