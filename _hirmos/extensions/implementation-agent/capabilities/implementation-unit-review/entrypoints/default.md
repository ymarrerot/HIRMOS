# implementation-unit-review

## Execution Contract

### Purpose

Review one completed implementation unit against its sealed `IU-xx.md` contract authority, append-only execution record, validation, and evidence.

### Produces

- append-only updates to `_hirmos/session/implementation-units/IU-xx.md` Unit Review section
- retry or route-back decision appended inside the same IU artifact without editing sealed contract sections
- `_hirmos/session/SESSION_EXECUTION.md` unit-review control update

### Terminal States

- PASS — implementation satisfies 100% of the unit authority record.
- PASS_WITH_LIMITATIONS — implementation is acceptable with explicit limitations.
- FAIL — implementation does not satisfy the unit authority record.
- BLOCKED — review cannot complete due to missing evidence or blocker.
- ROUTE_BACK_REQUIRED — review exposes invalid design/scope/current-state assumptions.
- NOT_APPLICABLE — no unit review is required.

## Activation triggers

- an implementation unit execution record is complete or blocked
- unit completion is being considered

## Required inputs

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/unresolved-items.md`
- target `_hirmos/session/implementation-units/IU-xx.md` with sealed contract sections, Execution Record, and evidence sections

## Execution controls contributed

- implementation unit review control
- retry / route-back decision control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/implementation-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.


Unit review is local, specific, and evidence-based. A unit is not complete until local review is appended in the same `IU-xx.md` artifact. Unit review must not modify sealed contract sections; if review discovers invalid or incomplete contract authority, it must record route-back instead of repairing the contract.

The review must literally answer inside the IU artifact:

```text
Does the actual implementation satisfy 100% of this implementation unit authority record?
Answer: YES / NO / PARTIAL.
Evidence:
Gaps:
Deferred items:
```

The review must compare:

- Unit Scope requirements to actual result;
- in-scope / out-of-scope conformance;
- validation requirements to actual evidence;
- requested runtime posture to delivered posture;
- claims to concrete file/log/runtime evidence.

Retry decisions must be appended in the same `IU-xx.md` artifact under `## 6. Retries`. Do not create standalone retry-request artifacts. Retry within the sealed scope may proceed by append-only retry records; scope, authority, or acceptance-criteria changes require route-back and a new/reopened sealed contract version.




## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.

## Canonical interaction posture visibility

Use the canonical HIRMOS interaction posture from `_hirmos/core/authority/INTERACTION_POSTURE.md`: concise user-facing output, transparent artifact pointers for governed claims, and progressive disclosure when risk, validation failure, blocker state, route-back, or user request requires more detail.

- By default, surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- Surface capability result, assumptions, artifacts/evidence, and review implications when requested or needed for responsible review.
- Surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis when validation failure, blocker state, route-back, or inspection need requires it.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.



## PROD-L8.25 Sealed IU Review Guard

During review, compare the final implementation against the sealed contract as it existed before material edits. Do not improve contract wording, scope mapping, acceptance criteria, verification commands, or evidence requirements during review. If tests, fixtures, mocks, snapshots, validators, expected-output files, or regression fixtures changed, the review must check that the Execution Record includes a Test / Fixture / Validator Change Rationale and must judge whether realism/coverage was preserved or improved rather than weakened.

## PROD-L8.28 Active Close Unit Review Gate

Before a unit may contribute to phase/session close, review must append a concrete Unit Review result inside the IU. A generated IU with `Review status: PENDING`, missing Unit Result, missing Request-to-Result Review, or missing validation/evidence comparison cannot support implementation-complete, phase-accepted, or delivery-close claims.

If the sealed contract is thin, placeholder-only, missing required generated IU sections, or appears to have been expanded after implementation, review must record `ROUTE_BACK_REQUIRED` or a governance deviation. Do not repair sealed contract authority during review.
