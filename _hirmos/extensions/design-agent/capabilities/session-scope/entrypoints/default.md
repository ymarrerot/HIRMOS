# session-scope

## Execution Contract

### Purpose

Create the Session Scope that authorizes exactly what the active session may do.

### Produces

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/unresolved-items.md updates`
- `_hirmos/session/SESSION_LEDGER.md session-scope control updates`

### Terminal States

- COMPLETED — ready Session Scope exists and can authorize downstream work if readiness passes.
- NEEDS_USER_DECISION — scope boundary needs user decision.
- BLOCKED — required source authority artifacts or unresolved dispositions are missing.
- ROUTE_BACK_REQUIRED — scope creation exposes missing Design or system-state evidence.
- NOT_APPLICABLE — active request does not require session scope authority.

## Activation triggers

- Implementation may be needed
- active request needs bounded work authority
- delivery scope or durable phase must be adopted for the current session
- validation/review-only work needs explicit scope

## Required inputs

- `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md when applicable`
- `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md when applicable`
- `_hirmos/session/unresolved-items.md`

## Execution controls contributed

- session-scope control
- implementation-authorization control
- unresolved-item control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/design-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

## Required behavior

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Capability-specific obligations

- Create one compact active session authority that contains only the requirements, design decisions, exclusions, evidence expectations, and close checks needed for this session.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## Project-type / stack requirements

Use the focus-appropriate `DESIGN.md`, `DELIVERY_SCOPE.md`, or `SESSION_SCOPE.md` for material project-type decisions and `stack-resolution.json` only when machine-readable stack routing is required by controls.

For any project type, require delivery-baseline governance when one bounded session cannot safely govern the change; do not equate delivery governance with a greenfield or brownfield label.

When stack contexts are active, carry in-scope/out-of-scope contexts into the active authority and Implementation Readiness decision when implementation is being authorized.


## Automated testing scope responsibility

For implementation-capable software scope, apply the governed automated-testing and test-integrity rules in `_hirmos/core/protocol/VALIDATION_AND_EVIDENCE.md`. Populate the compact `SESSION_SCOPE.md` Automated Testing Posture before Implementation begins. The posture must preserve repository-native tooling, identify whether unit tests are required for material isolated deterministic logic, and name the stronger applicable layer when unit tests are not appropriate. Do not add per-IU test detail here when IU mode applies.

## Runtime integration responsibilities

Apply the shared runtime-integration responsibilities in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Keep detailed evidence in the owning IU, `EVIDENCE.md`, or accepted-state/archive source; this entrypoint should point rather than duplicate.

## durable delivery capability obligations

This capability must apply `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` before claiming completion.

Required behavior:

1. Read and record the Delivery Shape Decision from `SESSION_LEDGER.md` and `SESSION_SCOPE.md` when those artifacts exist.
2. When the selected shape is `MULTI_SESSION_DELIVERY` or `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, use only durable delivery authority under `_hirmos/system/delivery/<delivery-id>/`.
3. When the selected shape is `MULTI_SESSION_DELIVERY`, require `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`; when the selected shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, require both the Delivery Plan and an adopted `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` before implementation readiness.
4. When the selected shape is a single-session shape, verify the active Session Scope contains affirmative bounded-scope safety evidence and implementation-unit coverage when required.
5. When the selected shape is `UNCERTAIN`, set this capability result to `BLOCKED` or `ROUTE_BACK_REQUIRED`; do not authorize Implementation.
6. Do not create or depend on session-local delivery authority artifacts.

Forbidden session-local delivery authorities:

```text
legacy session-local delivery plan, phase plan, delivery status, phase scope, or delivery-unit authority record files
```

## PROD-L8.9 focus-aware runtime route obligations

This capability participates in the command-selected focus route. Before claiming completion, it must ensure `SESSION_LEDGER.md` records:

- selected Delivery Shape Decision;
- this capability decision and terminal state;
- required authority artifacts for the selected focus route;
- whether the focus route is satisfied, blocked, not applicable, or requires route-back;
- exactly one next governed command when the route cannot proceed.

The capability must not compensate for missing authority by creating legacy session-local delivery files or by duplicating full delivery authority inside `SESSION_SCOPE.md`.


Compatibility note: implementation unit planning, implementation unit review, session implementation review, and Update System State remain downstream responsibilities governed by `SESSION_SCOPE.md`.


## PROD-L8.13 Current-State-First Generated Artifact Cleanup

Generated artifacts and checkpoint text must explain routing from current system state, scope size, validation risk, continuity need, and artifact-authority requirements. Do not use greenfield/brownfield labels as the primary reason for delivery/session/phase selection. If a project-type label is useful, record it as supporting evidence metadata or phase-control routing metadata only.

### Delivery shape honesty and cost-aware routing

When this capability records or consumes a delivery shape, it must use the smallest sufficient governed shape for the real software work. It must not select durable delivery or phase files because the framework is being tested, inspected, or dogfooded. It must surface a compact tradeoff when the selected shape affects user interaction or token cost: technically possible simpler shape, why that shape is acceptable or insufficient, why the selected shape is necessary, and the risk if the work is compressed into a smaller shape. When multi-session delivery is selected, it must also apply phase-count honesty: choose the fewest phases that preserve honest validation, reviewability, continuity, and accepted-state integrity; apply merge pressure to every proposed phase after phase 2; and reject thin phases whose work can be safely merged.



## PROD-L8.32D Compact IU Planning Boundary

When scope mentions implementation units, keep `SESSION_SCOPE.md` to compact IU pointers only: planned IU ID, one-line objective, covered scope item IDs, and expected IU file path. Do not put full IU contracts, execution steps, per-IU binary acceptance detail, sealed status, evidence, or review content in session scope.
