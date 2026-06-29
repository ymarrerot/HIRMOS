# Command: hirmos start
Status: compact command authority.
Purpose: provide the low-token command execution surface for `hirmos start`; use deeper protocols only when a listed gate requires detail.

## Execution contract
Produces: `_hirmos/session/SESSION_LEDGER.md`, required session/delivery artifacts, and a governed checkpoint.
Terminal states: Needs User Decision / Session Baseline Review / IU Planning Required / Blocked / Fail-Closed / Request Not Governable.

## Required reads
1. This command file.
2. `_hirmos/core/protocol/COMMANDS.md` for public command discipline.
3. `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` for legality and state mutation.
4. `_hirmos/core/templates/session/SESSION_LEDGER.md` before writing the ledger.
5. Adaptive protocols only when the gate below references them.

## Required behavior

Read this command file first, apply its gate checklist exactly, and read deeper protocols only when this command file names a gate requiring deeper detail, validation fails, or active artifacts contradict each other. Do not route through the removed runtime packet wrapper layer.

## Runtime gate checklist
- General run preflight: record `PRECHECK_PASS`, `PRECHECK_WARNING`, or `PRECHECK_BLOCKER`; do not create special run-category semantics.
- Command-state gate: `SESSION_STATE.json` exists, `status` is `idle`, `hirmos start` is legal, and stale active-session artifacts are absent.
- Runtime timestamp source: derive timestamps from `SESSION_STATE.json.run_context`, not memory.
- Current-State-First Source Reading Contract: read `CURRENT_SYSTEM_STATE.md` first when present; if delivery pointers exist, apply Current System State Delivery Pointer Precheck and do not default to a single-session path when `Next recommended delivery` requires delivery-governed continuation.
- Delivery Shape Decision Gate: answer `smallest governed delivery shape`; include `Technically possible simpler shape:`, `Why selected shape is necessary for this real software work:`, `User interaction / token-cost impact:`, `If multi-session is selected, smallest honest phase count:`, `Phase-count options considered:`, `Phase merge pressure applied:`, and `Risk if compressed into fewer phases:`.
- Phase Entry Gate Enforcement: inspect Phase Entry Gate, lifecycle status, and phase type before implementation readiness.
- Durable Phase Adoption Pre-Implementation Gate: durable delivery implementation adopts exactly one durable phase file before implementation authorization.
- Phase Progress / Carry-Forward Enforcement: read Phase Progress Pointer Index and Carry-Forward Items before routing follow-up work.
- Phase Acceptance Enforcement: inspect Phase Acceptance Evidence Gate before implying acceptance.
- PROD-L8.32D Session Scope / IU Boundary: `SESSION_SCOPE.md` may contain only planned IU IDs, one-line objectives, covered scope item IDs, expected IU file paths, and planning status; it is not an IU contract.
- PROD-L8.31 Generated-Run Start Gate: verify the complete bootstrap quiz and, when IU mode is active, planned IU paths may be named only as expected future authority until the session baseline is accepted. Legacy generated-run gate phrase preserved: expected full `IU-xx.md` files exist before implementation; under L8.32I/S they must exist before IU execution authorization, not at start.
- PROD-L8.32I IU Planning / Execution Boundary: when IU mode is expected, `hirmos start` must make the next step explicitly `IU Planning`, not implementation or IU execution. Baseline acceptance authorizes IU planning/materialization only.
- PROD-L8.32K start boundary clarity: the start checkpoint must not imply that the next `hirmos continue` performs implementation when IU mode is expected; it must name IU Planning as the next governed boundary and require validation before any later transition claim.

## Delivery-baseline surface controls
- PROD-L8.9 focus-aware route runtime behavior: use `session_focus` routing.
- PROD-L8.9E/F Focus-Aware Checkpoint Output: a delivery-baseline pause must not create `_hirmos/session/SESSION_SCOPE.md`.
- PROD-L8.10 delivery-baseline surface rule: must not create `_hirmos/session/SESSION_SCOPE.md` or `_hirmos/session/unresolved-items.md`.
- PROD-L8.11 Delivery-Baseline Optional Authority Location: During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`.
- Root delivery registry rule: must not create a per-delivery `DELIVERY_PLAN.md` unless delivery governance explicitly requires it in the canonical delivery location.

## State mutation and terminal boundary
Required state mutation: set active session id, focus, lifecycle status, allowed commands, recommended command, blocking reason, and updated timestamp.
The final start state is the focus-appropriate governed checkpoint. Mandatory implementation-readiness pause: must not begin implementation during `hirmos start`. If IU mode is expected, the checkpoint must say the next continuation creates the IU plan/files and pauses for IU review; it must not say the next continuation begins implementation.
If preconditions fail, stop at Fail-Closed.

## Follow-up work after no active session exists
When no active session exists, do not recommend `hirmos continue`. Recommend a concrete start command, for example: `hirmos start "Run local E2E smokes for <delivery-id> and update evidence posture"`.


## Artifact synchronization rule

Update canonical owning artifacts only. Do not maintain duplicate mutable narrative status in roadmap, phase, current-state, evidence, and ledger at the same time. Derived values such as recommended next command must be recomputed from gates, not independently authored. Stale or contradictory sections fail closed.

## PROD-L8.32L Just-in-Time Artifact Creation and Derived Pointer Indexes

Optional artifacts are not created to satisfy a template checklist. Create them only when the current governed boundary makes their owning concern applicable:

- `EVIDENCE.md` only when evidence volume, claim reconciliation, review-gate evidence, or close/archive evidence cannot be represented safely by ledger/IU evidence pointers.
- `_hirmos/session/unresolved-items.md` only when session-level unresolved items exist or unresolved-register review is required for the current boundary.
- session `REQUIREMENTS.md` / `DESIGN.md` only when separate session-level authority is explicitly justified after the flow reaches session or phase-session scope.
- delivery `DELIVERY_PLAN.md`, `DELIVERY_SCOPE.md`, delivery unresolved register, and `PHASE-xx.md` only when delivery governance is selected and the specific delivery/phase boundary is active.
- implementation-unit files only after session baseline acceptance and during IU planning; never during `hirmos start` pre-acceptance planning.

Pointer indexes in Current System State, Delivery Plan, Phase files, and ledger status surfaces are derived navigation caches. Prefer deriving them from filesystem paths, active session state, session ledger rows, archive manifests, and delivery/phase directories. If a derived pointer index conflicts with source artifacts, source artifacts win and the runtime must fail closed instead of preserving the stale pointer row.


## PROD-L8.32S Runtime Command Surface Unification

This file is the canonical compact command runtime authority for `hirmos start`. `_hirmos/core/runtime/` and `*.packet.md` command wrappers are removed. Do not route through a separate runtime packet; read this command file first, then read protocols only when this command file names a gate requiring deeper detail, validation fails, or active artifacts contradict each other.


## Validator-preserved command markers

- A delivery-baseline pause must not create `_hirmos/session/SESSION_SCOPE.md`.
- Bootstrap requires complete discipline answers; durable answer source/answer basis missing blocks start.
- Current-state delivery pointers mean HIRMOS must not default to a single-session path.
## Start hardening reference markers

- before the session scope baseline has been accepted or amended
- Implementation-unit artifacts are created only after the session scope baseline is accepted or amended
- START_CHECKPOINT_OUTPUT.md
- SESSION_STATE.json` → `run_context


## Artifact synchronization rule

Command execution must update the canonical owner of each fact and use pointers elsewhere. Do not duplicate mutable status across session, delivery, phase, current-state, evidence, and carry-forward artifacts. `SESSION_STATE.json` command fields are derived cache values and must be recomputed from ledger gates and command legality rules.

## PROD-L8.32L Just-in-Time Artifact Creation and Derived Pointer Indexes

Commands must not instantiate optional artifacts merely because a template exists. Create optional artifacts only when the current boundary makes the owning concern applicable. Treat Current System State, Delivery Plan, Phase, and ledger pointer rows as derived navigation caches over source artifacts; stale pointer rows fail closed.
