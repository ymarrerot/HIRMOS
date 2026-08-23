# Command: hirmos close
Status: compact command authority.
Purpose: provide the low-token command execution surface for `hirmos close`; use deeper protocols only when a listed gate requires detail.

## Execution contract
Produces: updated evidence/accepted-state artifacts, archive manifest, normalized archived `SESSION_STATE.json`, reset active session area, and post-close guidance.
Terminal states: Closed / Archived / Closed Partial / Close Blocked / Blocked / Fail-Closed.

## Required reads
1. This command file.
2. `_hirmos/core/protocol/COMMANDS.md`.
3. `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md`.
4. `_hirmos/core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md`.
5. Active `SESSION_STATE.json`, `SESSION_LEDGER.md`, `EVIDENCE.md`, carry-forward/unresolved records, and delivery/current-state artifacts as applicable.

## Required behavior

Read this command file first, apply its gate checklist exactly, and read deeper protocols only when this command file names a gate requiring deeper detail, validation fails, or active artifacts contradict each other. Do not route through the removed runtime packet wrapper layer.

## Runtime gate checklist
- Command-state gate and Command-state close transition: close is legal only from an active close-ready state.
- Required state mutation: normalize active/archived state, reset active session, and surface exactly one legal next command.
- Accepted-state integrity gate: accepted-state updates must match evidence and close result.
- Archive and session-state integrity invariant: write `ARCHIVE_MANIFEST.md`; Normalize the archived `SESSION_STATE.json`; archived `SESSION_STATE.json` normalized.
- PROD-L6 accepted-state/history/archive alignment: archive and accepted state must not diverge.
- PROD-L8.27 Pre-Archive Validation Gate and Archive Immutability: run the active-session validator before archive preservation; Historical governance/evidence failures must not be patched.
- PROD-L8.32K close validator invocation: close, archive, closed-partial, or accepted-state transition claims require an active gate validator result recorded before the claim; validator failures block archive/reset.
- PROD-L8.28 Generated IU Active Close Gate: Do not archive first and then expand historical IU files.
- PROD-L8.31 Generated-Run Close Gate: require explicit approval/deferral source and Delivery/current-state pointer reconciliation.
- Durable Delivery Pointer Close Requirement: Close is blocked if `Next recommended delivery` or Current System State delivery pointers conflict.
- Durable Delivery Status Close Requirement: update durable delivery status before normal close success; archive manifest may record the transaction.
- Durable current-system-state merge invariant: update accepted-state navigation and latest-close metadata.
- Durable Phase Adoption Close Requirement: require one adopted phase in `SESSION_SCOPE.md` for phase sessions.
- Phase Entry Gate Enforcement: inspect Phase Entry Gate, lifecycle status, and phase type.
- Phase Progress / Carry-Forward Enforcement: inspect Phase Progress Pointer Index and Carry-Forward Items.
- Phase Acceptance Enforcement: require Phase Acceptance Evidence Gate is PASS before phase acceptance claims.


## PROD-L8.33G Carry-Forward Attention block

Before claiming close success, `hirmos close` must display a Carry-Forward Attention block. If carry-forward is present, the block must list each item with global `CF-YYYYMMDD-NNN` ID, source session, source local ID, source ref, evidence gap, approval/deferral source, future-session instruction, and expected resolution evidence. If no active carry-forward remains after triage, the block must state that explicitly.

New active carry-forward rows must be written to `CARRY_FORWARD.md` using the global CF ID format and source pointers. Close must not use bare local IDs such as `CF-01` as accepted-state carry-forward IDs. Close must tell the user that later resolution uses the existing command flow: `hirmos start "Record verification that CF-YYYYMMDD-NNN is resolved"`, followed by `hirmos continue` and `hirmos close`.

Accepted-state maintenance close rule: when the active session type is accepted-state maintenance / carry-forward resolution, close must verify that every carry-forward removed from Active has a matching Resolved row in `CARRY_FORWARD.md`, that `CURRENT_SYSTEM_STATE.md` only summarizes the result, and that no historical archive was mutated.

## Carry-forward triage
Close-Time Carry-Forward Candidate Review: Carry-forward is a last-resort close disposition.
Allowed dispositions: AUTO_RESOLVED_NOW, USER_RESOLVED_NOW, APPROVED_CARRY_FORWARD, BLOCKING_UNRESOLVED, NO_LONGER_APPLIES.
`APPROVED_CARRY_FORWARD` requires an explicit approval/deferral source. Presence of `_hirmos/session/unresolved-items.md` during delivery-baseline focus is a concordance defect.

## Delivery and focus controls
- PROD-L8.9 focus-aware close reconciliation: focus route claims and durable artifacts disagree blocks close.
- PROD-L8.9E/F Focus-Aware Close Guard: must not claim implementation completion from a delivery-baseline session.
- PROD-L8.10 delivery-baseline close guard applies to minimal delivery-baseline surfaces.
- PROD-L8.11 Delivery-Baseline Optional Authority Location applies during delivery baseline close.
- PROD-L8.26 Delivery Close Concordance Simplification and Evidence Posture Hardening: use the simplified close ownership model.

## Post-close follow-up guidance
There is no active session, so `hirmos continue` is not applicable. Post-close follow-up guidance must recommend `hirmos start` for approved carry-forward or separately scoped work.
If any check fails, surface Close Blocked.


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


## PROD-L8.32Q Delivery Concordance Simplification

Use derived delivery concordance rather than asking the model to synchronize duplicated mutable delivery/phase status fields. Do not create `Delivery Status Update Log`. Do not treat `DELIVERY_SCOPE.md` requirement rows as current completion status. Parent delivery status in phase files is derived, not rewritten at every delivery close.


## PROD-L8.32S Runtime Command Surface Unification

This file is the canonical compact command runtime authority for `hirmos close`. `_hirmos/core/runtime/` and `*.packet.md` command wrappers are removed. Do not route through a separate runtime packet; read this command file first, then read protocols only when this command file names a gate requiring deeper detail, validation fails, or active artifacts contradict each other.


## Validator-preserved command markers

- Read CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md when close/update-state detail is needed.
- Check stale active-session artifacts before archive/reset.
- The presence of `_hirmos/session/unresolved-items.md` during delivery-baseline focus is a concordance defect.
## Ledger close reference markers

- ledger integrity self-validation
- latest pass number concordant with `SESSION_STATE.json.continuation_pass`
- Beyond Clear Specs execution-control subset
- clear command/boundary controls
- strict self-validation before surfaced claims
- fail-closed behavior when the active artifacts do not support the claim
- Work History Ledger
- Source Artifact Index


## Artifact synchronization rule

Command execution must update the canonical owner of each fact and use pointers elsewhere. Do not duplicate mutable status across session, delivery, phase, current-state, evidence, and carry-forward artifacts. `SESSION_STATE.json` command fields are derived cache values and must be recomputed from ledger gates and command legality rules.

## PROD-L8.32L Just-in-Time Artifact Creation and Derived Pointer Indexes

Commands must not instantiate optional artifacts merely because a template exists. Create optional artifacts only when the current boundary makes the owning concern applicable. Treat Current System State, Delivery Plan, Phase, and ledger pointer rows as derived navigation caches over source artifacts; stale pointer rows fail closed.
