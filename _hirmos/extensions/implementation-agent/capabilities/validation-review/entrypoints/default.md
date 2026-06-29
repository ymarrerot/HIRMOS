# validation-review

## Execution Contract

### Purpose

Run or inspect stack/project validation evidence and decide whether evidence proves the active scope.

### Produces

- `_hirmos/session/EVIDENCE.md`
- validation logs or evidence references
- `_hirmos/session/SESSION_LEDGER.md evidence claims`

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

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## Stack context requirements

When stack contexts are active, Implementation must preserve stack context boundaries.

Each Implementation Unit should target one primary stack context unless a cross-stack unit is explicitly justified. Validation and evidence must be recorded by stack context when commands/checks differ.


## Runtime integration responsibilities

Apply the shared runtime-integration responsibilities in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Keep detailed evidence in the owning IU, `EVIDENCE.md`, or accepted-state/archive source; this entrypoint should point rather than duplicate.

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
