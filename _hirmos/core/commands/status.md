# Command: hirmos status
Status: compact command authority.
Purpose: provide the low-token command execution surface for `hirmos status`; status is read-only.

## Execution contract
Produces: status output only.
Terminal states: Status Reported / Status Blocked By Integrity Conflict.

## Required reads
1. This command file.
2. `_hirmos/core/protocol/COMMANDS.md`.
3. `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md`.
4. `SESSION_STATE.json`, current-state pointers, and active/delivery artifacts needed to explain status.

## Required behavior

Read this command file first, apply its gate checklist exactly, and read deeper protocols only when this command file names a gate requiring deeper detail, validation fails, or active artifacts contradict each other. Do not route through the removed runtime packet wrapper layer.

## PROD-L8.33E Status read-only bootstrap fast path

`hirmos status` may run a read-only preflight/status pass without creating `_hirmos/session/bootstrap/BOOTSTRAP_REPORT.md`. Bootstrap completion remains required before advancing commands: `hirmos start`, `hirmos continue`, and `hirmos close`.

If bootstrap is absent or incomplete, status must report that fact, report that advancing commands are blocked until bootstrap passes, and continue only as a read-only status/preflight report. Status must not create bootstrap artifacts, backfill accepted-state artifacts, repair carry-forward registers, update lifecycle state, or edit project/source files.

## PROD-L8.33E Status minimum read set

Idle or post-close status must start with this minimum read set:

1. `_hirmos/hirmos.config.json`
2. `_hirmos/session/SESSION_STATE.json`
3. `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`
4. `_hirmos/system/accepted-state/CARRY_FORWARD.md`
5. The latest archive manifest, if referenced by accepted-state pointers or discoverable under `_hirmos/system/history/sessions/`

Active-session status must add only the session artifacts needed to explain current authority:

1. `_hirmos/session/SESSION_LEDGER.md`
2. `_hirmos/session/SESSION_SCOPE.md`
3. `_hirmos/session/unresolved-items.md`, when present or when unresolved-item state is relevant
4. `_hirmos/session/implementation-units/*.md`, only when IU mode, IU plan status, or IU execution authorization is relevant

Delivery or phase status must add delivery/phase files only when accepted-state or session pointers indicate active delivery/phase context. Deeper protocol reads are escalation reads, not default status reads; use them only when the minimum reads reveal a contradiction, missing required field, active gate, or delivery/phase state that cannot be explained from the compact status surface.

## Runtime gate checklist
- Command-state gate and Command-state reporting: report status without mutating files.
- Status invariant and canonical-value reporting: do not invent state; read machine state and current artifacts.
- recommended_next_command must be legal and exactly one primary next action.
- Current-State Navigation Status Contract: report accepted current-state status, Active delivery scope path, Delivery roadmap path, and Next recommended delivery when present.
- Durable Delivery Pointer Reporting: if pointers conflict, surface Status Blocked By Delivery Pointer Conflict.
- PROD-L8.9 focus-aware status reporting: focus and route must match status.
- PROD-L8.9E/F Checkpoint Status Reporting: report prematurely instantiated surfaces.
- PROD-L8.10 delivery-baseline unresolved reporting: session-level unresolved register in this focus is a surface-minimality conflict.
- PROD-L8.11 Delivery-Baseline Optional Authority Location: report optional-authority conflicts.
- Durable Phase Adoption Status Reporting: Status must not imply implementation authorization when phase adoption is missing.
- Phase Entry Gate Enforcement: report Phase Entry Gate, lifecycle status, and phase type.
- Phase Progress / Carry-Forward Enforcement: report Phase Progress Pointer Index and Carry-Forward Items.
- Phase Acceptance Enforcement: report what acceptance evidence is missing.
- CLI / Status UX Phase Lifecycle Reporting: include Phase Lifecycle Status Report with Greenfield status group and Brownfield status group when applicable.
- Delivery Status Concordance Reporting: surface Status Blocked By Delivery Status Conflict.
- Status Blocked By Delivery Route Conflict and integrity conflict must be explicit.


## PROD-L8.33A Status Command Read-Only Gate

`hirmos status` is read-only. It reports current lifecycle stage, active gate, integrity conflicts, baseline authority state, IU execution authorization when IU mode applies, and exactly one recommended next command. It must not edit product/source files, advance lifecycle state, or backfill artifacts to make status appear clean.

Status output must explicitly report whether implementation is blocked by missing baseline acceptance, missing IU plan review, or missing `IU_EXECUTION_AUTHORIZED`.

## Post-close status behavior
There is no active session, so `hirmos continue` is not applicable. Post-close follow-up command clarity requires a concrete `hirmos start` recommendation when follow-up is needed.


## Artifact synchronization rule

Update canonical owning artifacts only. Do not maintain duplicate mutable narrative status in roadmap, phase, current-state, evidence, and ledger at the same time. Derived values such as recommended next command must be recomputed from gates, not independently authored. Stale or contradictory sections fail closed.


## PROD-L8.32K status boundary report

Status output must report the active command authority path, latest active gate validator result if present, and whether IU execution is authorized. If IU mode applies and `IU_EXECUTION_AUTHORIZED` is absent, status must say implementation execution is blocked even when IU files exist.

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

This file is the canonical compact command runtime authority for `hirmos status`. `_hirmos/core/runtime/` and `*.packet.md` command wrappers are removed. Do not route through a separate runtime packet; read this command file first, then read protocols only when this command file names a gate requiring deeper detail, validation fails, or active artifacts contradict each other.


## Validator-preserved command markers

- Status output must follow status invariant and canonical-value reporting.
- Surface Exactly one recommended next command.
## Ledger status reference markers

- status must report ledger integrity
- It must not mutate the ledger


## Artifact synchronization rule

Command execution must update the canonical owner of each fact and use pointers elsewhere. Do not duplicate mutable status across session, delivery, phase, current-state, evidence, and carry-forward artifacts. `SESSION_STATE.json` command fields are derived cache values and must be recomputed from ledger gates and command legality rules.

## PROD-L8.32L Just-in-Time Artifact Creation and Derived Pointer Indexes

Commands must not instantiate optional artifacts merely because a template exists. Create optional artifacts only when the current boundary makes the owning concern applicable. Treat Current System State, Delivery Plan, Phase, and ledger pointer rows as derived navigation caches over source artifacts; stale pointer rows fail closed.
