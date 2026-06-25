# session-implementation-review

## Execution Contract

### Purpose

Review all implementation units together against the Session Scope, delivery/phase criteria, validation evidence, and remaining blockers.

### Produces

- `_hirmos/session/SESSION_SCOPE.md` close verification updates
- `_hirmos/session/SESSION_SCOPE.md` final-verdict mirror updates
- `_hirmos/session/SESSION_EXECUTION.md` implementation-completion gate

### Terminal States

- IMPLEMENTATION_COMPLETE — all required units and evidence satisfy the Session Scope.
- COMPLETE_WITH_LIMITATIONS — implementation is acceptable with explicit non-gating limitations.
- BLOCKED — one or more units, reviews, evidence records, or unresolved items are incomplete.
- FAILED — implementation does not satisfy the Session Scope.
- ROUTE_BACK_REQUIRED — review exposes design/scope/system-state inconsistency.
- NOT_APPLICABLE — implementation was not active for this session.

## Activation triggers

- all active implementation units are complete or intentionally not applicable
- implementation completion is being considered
- Update System State readiness depends on implementation result

## Required inputs

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/unresolved-items.md`
- `_hirmos/session/SESSION_SCOPE.md` close verification
- all applicable `_hirmos/session/implementation-units/IU-xx.md` artifacts
- validation/evidence appendices when applicable

## Execution controls contributed

- session implementation review control
- `SESSION_SCOPE.md` close verification review completion control
- Update System State readiness contribution

## Method

This capability inherits shared extension rules from `_hirmos/extensions/implementation-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

Session implementation review is the aggregate review above local unit review. It must:

1. Inspect every applicable IU artifact.
2. Confirm every completed unit contains execution evidence and a Unit Review verdict.
3. Confirm the combined units satisfy 100% of `SESSION_SCOPE.md`, or record exact gaps/deferred items/blockers.
4. Complete `_hirmos/session/SESSION_SCOPE.md` close verification promised-vs-verified coverage.
5. Reconcile unresolved items by direct review of `_hirmos/session/unresolved-items.md`.
6. Decide whether implementation completion may be claimed or must fail closed.

Implementation completion cannot be claimed merely because all individual units passed; the combined implementation must satisfy the Session Scope or explicitly fail/partial/defer under the `SESSION_SCOPE.md` close verification review rules.




## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.


# PROD-L8.22 Session Implementation Review Gate

This capability performs an aggregate evidence-backed review. It must not pass a session merely because implementation units individually claim completion.

Required review dimensions:

- source session authority reviewed;
- IU set and unit review records reviewed;
- actual final codebase reviewed: `YES` / `NO` / `NOT_APPLICABLE`;
- scope coverage result;
- cross-unit integration result;
- architecture/preservation alignment;
- validation evidence;
- runtime/provider evidence level;
- production evidence level;
- unresolved/carry-forward impact;
- final result: `PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, or `NOT_APPLICABLE`;
- why the result is honest;
- what is not claimed.

If evidence is insufficient for a broad claim, downgrade the claim instead of treating the review as passed.
