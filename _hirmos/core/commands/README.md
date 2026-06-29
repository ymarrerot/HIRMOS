# HIRMOS Command Runtime Surface

Status: compact command authority.
Purpose: provide the canonical low-token command execution surfaces for normal HIRMOS runtime use.

Command files are the first runtime authority files read by public commands: command file first, protocol references only as needed. They do not replace core protocols; they point to protocols only when a specific gate requires deeper detail.

Commands:

- `start.md`
- `continue.md`
- `status.md`
- `close.md`

Rule: command files are the default runtime path; protocols remain deeper reference authority.


## PROD-L8.32K Command-First Runtime Boundary

Normal command execution must read the relevant `_hirmos/core/commands/<command>.md` file first and record the command authority path used when making a lifecycle transition claim. Full protocols are escalation references only when a command gate, validation failure, or contradictory artifact state requires deeper detail.

Before any implementation, completion, close, or archive transition claim, HIRMOS must run or record an active gate validator result against the current active artifacts. Narrative compliance is not a validator substitute.

## PROD-L8.32L Just-in-Time Artifact Creation and Derived Pointer Indexes

Optional artifacts are not created to satisfy a template checklist. Create them only when the current governed boundary makes their owning concern applicable:

- `EVIDENCE.md` only when evidence volume, claim reconciliation, review-gate evidence, or close/archive evidence cannot be represented safely by ledger/IU evidence pointers.
- `_hirmos/session/unresolved-items.md` only when session-level unresolved items exist or unresolved-register review is required for the current boundary.
- session `REQUIREMENTS.md` / `DESIGN.md` only when separate session-level authority is explicitly justified after the flow reaches session or phase-session scope.
- delivery `DELIVERY_PLAN.md`, `DELIVERY_SCOPE.md`, delivery unresolved register, and `PHASE-xx.md` only when delivery governance is selected and the specific delivery/phase boundary is active.
- implementation-unit files only after session baseline acceptance and during IU planning; never during `hirmos start` pre-acceptance planning.

Pointer indexes in Current System State, Delivery Plan, Phase files, and ledger status surfaces are derived navigation caches. Prefer deriving them from filesystem paths, active session state, session ledger rows, archive manifests, and delivery/phase directories. If a derived pointer index conflicts with source artifacts, source artifacts win and the runtime must fail closed instead of preserving the stale pointer row.


## PROD-L8.32S Runtime Command Surface Unification

`_hirmos/core/commands/` is the single compact runtime command surface. The former `_hirmos/core/runtime/*.packet.md` layer is removed to avoid duplicate command authority. Do not recreate packet files or route command execution through a wrapper.
