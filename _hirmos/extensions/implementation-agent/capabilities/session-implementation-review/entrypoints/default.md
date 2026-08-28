# session-implementation-review

## Execution Contract

### Purpose

Review all implementation units together against the Session Scope, delivery/phase criteria, validation evidence, and remaining blockers.

### Produces

- `_hirmos/session/SESSION_SCOPE.md` close verification updates
- `_hirmos/session/SESSION_SCOPE.md` final-verdict mirror updates
- `_hirmos/session/SESSION_LEDGER.md` implementation-completion gate

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

## Invocation timing

This capability should be invoked automatically when all active implementation units/work have reached their execution/review boundary and Implementation completion is being considered. It does not require a separate user request or a dedicated pre-close continuation when its required inputs are already available.

If required evidence is unavailable and only the user can provide or decide it, surface that specific evidence/decision checkpoint. Otherwise complete the aggregate review in the same continuation that finished implementation execution.

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
2. Confirm every completed unit contains a sealed contract, append-only execution evidence, and a Unit Review verdict.
3. Confirm the combined units satisfy 100% of `SESSION_SCOPE.md`, or record exact gaps/deferred items/blockers.
4. Complete `_hirmos/session/SESSION_SCOPE.md` close verification promised-vs-verified coverage.
5. Reconcile unresolved items by direct review of `_hirmos/session/unresolved-items.md`.
6. Decide whether implementation completion may be claimed or must fail closed.
7. Reconcile the Session Scope Automated Testing Posture and every applicable IU Automated Testing Posture against the final test suite, test-delta rationales, and validation results.
8. Confirm material testable behavior received the required automated-test layer, valid existing tests for unchanged behavior were not weakened to obtain PASS, and changed/removed behavior did not leave stale/orphan tests or fixtures without rationale.

Implementation completion cannot be claimed merely because all individual units passed or because IU files were cleaned up after execution; the combined implementation must satisfy the Session Scope or explicitly fail/partial/defer under the `SESSION_SCOPE.md` close verification review rules.




## Required behavior

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

# PROD-L8.22 Session Implementation Review Gate

This capability performs an aggregate evidence-backed review. It must not pass a session merely because implementation units individually claim completion.

Required review dimensions:

- automated-testing posture and behavioral test-integrity reconciliation;

- source session authority reviewed;
- IU set, sealed contract posture, execution records, and unit review records reviewed;
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


## PROD-L8.24 Generated Review Gate Validation
Session implementation review must instantiate the L8.22 review gate in generated artifacts, not only rely on template doctrine. Record actual final codebase reviewed, files inspected, scope coverage, cross-unit integration, runtime/provider evidence level, production evidence level, final result, why the result is honest, and what is not claimed. Missing generated review-gate fields must downgrade or block close acceptance.


## PROD-L8.25 Sealed IU Aggregate Review Guard

Aggregate implementation review must verify that completed IU files preserve sealed contract authority and separate it from append-only execution/review records. If a sealed contract section was edited after material implementation began without an explicit route-back/reopen/supersede record, the session cannot claim clean implementation acceptance. Downgrade, block, or route back instead of normalizing the artifact during review or close.

## PROD-L8.28 Active Close Concordance Review

Session implementation review must reconcile IU execution/review status before close. If any applicable IU remains `Execution status: NOT_STARTED`, `Review status: PENDING`, lacks Unit Result, lacks validation/evidence comparison, lacks required Automated Testing Posture, or lacks required Test / Fixture / Validator Change Rationale/test-integrity review for changed validation assets, the session must not claim implementation complete. The legal result is `PARTIAL`, `BLOCKED`, `ROUTE_BACK_REQUIRED`, or `GOVERNANCE_DEVIATION`, depending on evidence.

The aggregate review must explicitly compare generated IU status with SESSION_SCOPE close claims, phase/delivery close posture, and accepted-state evidence posture before archive.
