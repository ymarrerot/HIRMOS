# validation-review

## Execution Contract

### Purpose

Run or inspect stack/project validation evidence and decide whether evidence proves the active scope.

### Produces

- `_hirmos/session/EVIDENCE.md`
- validation logs or evidence references
- `_hirmos/session/SESSION_EXECUTION.md evidence claims`

### Terminal States

- COMPLETED — validation evidence is recorded with commands/checks, results, outputs, limitations, and scope coverage.
- BLOCKED — required validation command, environment, artifact, or evidence is unavailable.
- ROUTE_BACK_REQUIRED — validation failure reveals invalid scope/design or missing implementation.
- FAILED — validation ran and failed within current scope.
- NOT_APPLICABLE — no validation/review evidence is required for this request, with rationale.

## Activation triggers

- Implementation reached validation boundary
- review-only or validation-only request requires evidence
- close/update depends on validation evidence
- a unit or session review needs evidence consolidation

## Required inputs

- `_hirmos/session/SESSION_SCOPE.md`
- implementation evidence or review target
- stack/project validation commands when available

## Execution controls contributed

- validation/evidence control
- stack control when validation commands are stack-specific

## Method

This capability inherits shared extension rules from `_hirmos/extensions/implementation-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

Validation review must distinguish run evidence from claims.

It must:

- record each command/check, context, result, and output/log location;
- record not-run or not-applicable checks with risk and rationale;
- map evidence to Session Scope and implementation units;
- preserve limitations rather than converting them into success;
- block readiness/completion when evidence is missing for required scope.

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

## Stack context requirements

When stack contexts are active, Implementation must preserve stack context boundaries.

Each Implementation Unit should target one primary stack context unless a cross-stack unit is explicitly justified. Validation and evidence must be recorded by stack context when commands/checks differ.


## Runtime integration responsibilities

When material runtime services are involved, follow `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

Record or consume `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` as required by execution controls.

Do not claim fixture/mock/boundary/local/production integration levels beyond what the active artifacts and evidence support.

# PROD-L8.22 Validation Review Gate Discipline

Validation review must classify the exact evidence level proven. Build, lint, typecheck, and static tests support implementation acceptance only; they do not by themselves prove local runtime behavior, provider behavior, role workflow readiness, or production readiness.

Required output when material:

- evidence reviewed;
- command/log evidence reviewed;
- actual codebase reviewed: `YES` / `NO` / `NOT_APPLICABLE`;
- runtime evidence level;
- production evidence level;
- final validation result;
- claims supported;
- claims not supported.
