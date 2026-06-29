# implementation-readiness

## Execution Contract

### Purpose

Decide whether Design has produced enough governed authority for Implementation to begin.

### Produces

- `_hirmos/session/SESSION_LEDGER.md readiness gate updates`
- canonical interaction posture checkpoint basis when readiness or blockers must be surfaced

### Terminal States

- COMPLETED — Implementation Readiness is READY or NOT_APPLICABLE with rationale.
- NEEDS_USER_DECISION — readiness is blocked by user-owned gated decisions.
- BLOCKED — required artifacts or controls are missing.
- ROUTE_BACK_REQUIRED — readiness review reveals upstream Design or system-state gaps.
- NOT_APPLICABLE — Implementation is not part of the active request path.

## Activation triggers

- Design appears complete
- Implementation may be next
- Domain Expert mode should advance to implementation-readiness unless gated unresolved items block progress
- Technical Supervisor review checkpoint is needed

## Required inputs

- `_hirmos/session/unresolved-items.md`
- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md when required`
- `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md when required`
- `_hirmos/session/SESSION_LEDGER.md`

## Execution controls contributed

- implementation-authorization control
- snapshot-backed checkpoint control
- unresolved-item control
- Design control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/design-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

## Required behavior

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Capability-specific obligations

- Session Scope authorizes exactly what Implementation may do.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## Project-type / stack requirements

Use the focus-appropriate `DESIGN.md`, `DELIVERY_SCOPE.md`, or `SESSION_SCOPE.md` for material project-type decisions and `stack-resolution.json` only when machine-readable stack routing is required by controls.

For any project type, use the smallest sufficient governed delivery shape. Require delivery-baseline governance or Phase files only when one bounded session or one session with implementation units cannot safely govern the change.

When stack contexts are active, carry in-scope/out-of-scope contexts into the active authority and Implementation Readiness decision when implementation is being authorized.


## Runtime integration responsibilities

Apply the shared runtime-integration responsibilities in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Keep detailed evidence in the owning IU, `EVIDENCE.md`, or accepted-state/archive source; this entrypoint should point rather than duplicate.

## Delivery shape and durable delivery capability obligations

This capability must apply `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` before claiming completion.

Required behavior:

1. Read and record the Delivery Shape Decision from `SESSION_LEDGER.md` and `SESSION_SCOPE.md` when those artifacts exist.
2. When the selected shape is `SINGLE_SESSION_VERTICAL_SLICE`, verify affirmative bounded-scope safety evidence.
3. When the selected shape is `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS`, verify implementation-unit coverage for the Session Scope.
4. When the selected shape is `MULTI_SESSION_DELIVERY`, require `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` before implementation readiness.
5. When the selected shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, require both `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` and one adopted `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` before implementation readiness.
6. When the selected shape is `UNCERTAIN`, set this capability result to `BLOCKED` or `ROUTE_BACK_REQUIRED`; do not authorize Implementation.
7. Do not create or depend on session-local delivery authority artifacts.

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

### Delivery shape honesty and cost-aware routing

When this capability records or consumes a delivery shape, it must use the smallest sufficient governed shape for the real software work. It must not select durable delivery or phase files because the framework is being tested, inspected, or dogfooded. It must surface a compact tradeoff when the selected shape affects user interaction or token cost: technically possible simpler shape, why that shape is acceptable or insufficient, why the selected shape is necessary, and the risk if the work is compressed into a smaller shape. When multi-session delivery is selected, it must also apply phase-count honesty: choose the fewest phases that preserve honest validation, reviewability, continuity, and accepted-state integrity; apply merge pressure to every proposed phase after phase 2; and reject thin phases whose work can be safely merged.



## PROD-L8.32D Compact IU Planning Boundary

When scope mentions implementation units, keep `SESSION_SCOPE.md` to compact IU pointers only: planned IU ID, one-line objective, covered scope item IDs, and expected IU file path. Do not put full IU contracts, execution steps, per-IU binary acceptance detail, sealed status, evidence, or review content in session scope.
