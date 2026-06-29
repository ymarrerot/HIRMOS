# delivery-design

## Execution Contract

### Purpose

Decide whether delivery decomposition is needed and produce a Delivery Plan roadmap/register and Delivery Scope when required.

### Produces

- `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- `_hirmos/session/SESSION_SCOPE.md delivery-route basis when available`
- `_hirmos/session/unresolved-items.md updates`
- `_hirmos/session/SESSION_LEDGER.md delivery control updates`

### Terminal States

- COMPLETED — delivery plan is recorded or decomposition is explicitly not applicable.
- NEEDS_USER_DECISION — delivery target or staging decision requires user input.
- BLOCKED — Design or system-state inputs are missing.
- ROUTE_BACK_REQUIRED — delivery planning exposes missing system-state or requirements evidence.
- NOT_APPLICABLE — active request can be governed safely without delivery planning.

## Activation triggers

- inspected current state and governance need show that staged delivery is required
- large, multi-session, or prototype-to-product work cannot be safely governed as one session
- Design needs delivery decomposition before phase/session-scope work

## Required inputs

- `_hirmos/session/SESSION_LEDGER.md`
- `_hirmos/session/SESSION_SCOPE.md when available`
- `_hirmos/session/unresolved-items.md`
- project-type and stack evidence

## Execution controls contributed

- Design control
- delivery-plan control
- unresolved-item control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/design-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

## Required behavior

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Capability-specific obligations

- Map delivery roadmap entries to one delivery scope and record delivery-route decisions.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## Project-type / stack requirements

Use the focus-appropriate `DESIGN.md`, `DELIVERY_SCOPE.md`, or `SESSION_SCOPE.md` for material project-type decisions and `stack-resolution.json` only when machine-readable stack routing is required by controls.

For any project type, require delivery-baseline governance when one bounded session cannot safely govern the change; do not equate delivery governance with a greenfield or brownfield label.

When stack contexts are active, carry in-scope/out-of-scope contexts into the active authority and Implementation Readiness decision when implementation is being authorized.


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


Compatibility note: Map Delivery Plan items to governed requirements through the active `DELIVERY_SCOPE.md`; the Delivery Plan remains the roadmap/register.


## PROD-L8.13 Current-State-First Generated Artifact Cleanup

Generated artifacts and checkpoint text must explain routing from current system state, scope size, validation risk, continuity need, and artifact-authority requirements. Do not use greenfield/brownfield labels as the primary reason for delivery/session/phase selection. If a project-type label is useful, record it as supporting evidence metadata or phase-control routing metadata only.


## PROD-L8.32D Compact IU Planning Boundary

When scope mentions implementation units, keep `SESSION_SCOPE.md` to compact IU pointers only: planned IU ID, one-line objective, covered scope item IDs, and expected IU file path. Do not put full IU contracts, execution steps, per-IU binary acceptance detail, sealed status, evidence, or review content in session scope.
