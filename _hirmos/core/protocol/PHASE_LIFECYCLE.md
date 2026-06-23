# Phase Lifecycle Protocol

Status: core protocol.
Purpose: define canonical lifecycle status, phase type, and template requirements for multi-session delivery phases across project contexts.

## Current-State-First Principle

HIRMOS is designed for current-state-first development. A project may be greenfield, brownfield, or somewhere in between; HIRMOS starts by understanding the current system state, then activates the capabilities needed for the session.

Phase lifecycle enforcement must therefore be driven by the inspected current system state and durable delivery context, not by a hard-coded greenfield or brownfield assumption.

## Canonical Phase Lifecycle Statuses

Every durable phase file must use one canonical lifecycle status:

```text
NOT_STARTED
READY_FOR_ADOPTION
ACTIVE
BLOCKED
PARTIAL
READY_FOR_ACCEPTANCE
ACCEPTED
DEFERRED
SUPERSEDED
CANCELLED
```

Status meanings:

| Lifecycle status | Meaning | Implementation authorization |
|---|---|---|
| NOT_STARTED | Phase exists but entry criteria are not yet satisfied. | Not authorized. |
| READY_FOR_ADOPTION | Phase has enough current-state/design context to be adopted by a session. | Session may adopt. |
| ACTIVE | Phase is currently being implemented or reviewed. | Authorized only through session adoption. |
| BLOCKED | Phase cannot proceed due to gating unresolved items or missing state. | Not authorized until resolved. |
| PARTIAL | Some work completed, but exit criteria are not fully met. | Continue/carry-forward required. |
| READY_FOR_ACCEPTANCE | Evidence exists and phase awaits acceptance/review. | Close/acceptance path only. |
| ACCEPTED | Phase exit criteria accepted and durable state updated. | No further implementation unless amended/new phase. |
| DEFERRED | Phase or phase items intentionally deferred. | Not active unless reactivated. |
| SUPERSEDED | Replaced by later phase/design decision. | Not active. |
| CANCELLED | Cancelled and should not be implemented. | Not active. |

## Canonical Phase Types

Every durable phase must declare exactly one phase type:

```text
GREENFIELD
BROWNFIELD
MIXED
UNKNOWN
```

Rules:

- `UNKNOWN` blocks implementation readiness.
- `GREENFIELD` activates greenfield MVP boundary, scope, architecture sequencing, and product-maturity controls.
- `BROWNFIELD` activates brownfield preservation, regression, compatibility, and migration-safety controls.
- `MIXED` activates both greenfield-specific controls and brownfield-specific controls.

## Universal Phase Lifecycle Fields

Every `PHASE-xx.md` must include:

```text
Phase ID
Phase title
Phase type
Lifecycle status
Current-state basis
Delivery Plan pointer
Entry criteria
Exit criteria
Scope included
Scope excluded
Adoption constraints
Acceptance evidence requirements
Open items
Deferred items
Carry-forward items
Close-time status transaction
Last session/archive pointer
Next recommended action
```

## Type-Specific Control Groups

Greenfield phases must include:

```text
MVP boundary
Primary user/workflow slice
Prototype vs production intent
Architecture dependency status
Out-of-scope expansion guard
Validation level required
Production-readiness claim allowed
```

Brownfield phases must include:

```text
Preservation baseline
Affected existing surfaces
Regression-sensitive behavior
Do-not-touch boundaries
Compatibility constraints
Data/migration safety constraints
Rollback/recovery considerations
Regression evidence required
```

Mixed phases must include and satisfy both greenfield and brownfield control groups. They may segment controls by workstream, but phase acceptance must reconcile both sides.

## Template and Pointer Concordance

`DELIVERY_PLAN.md`, `PHASE-xx.md`, and `CURRENT_SYSTEM_STATE.md` must use the same lifecycle status vocabulary.

`CURRENT_SYSTEM_STATE.md` records pointers and lifecycle status only. It must not duplicate Delivery Plan or Phase content.

## Fail-Closed Rules

- A phase with `UNKNOWN` phase type cannot authorize implementation readiness.
- A phase with missing lifecycle status cannot be adopted.
- A phase with a non-canonical lifecycle status cannot be adopted.
- A greenfield phase missing its MVP/scope/architecture control group cannot be accepted.
- A brownfield phase missing its preservation/regression control group cannot be accepted.
- A mixed phase missing either control group cannot be accepted.
- Current System State delivery pointers must not use stale legacy status vocabulary that omits `READY_FOR_ADOPTION`, `PARTIAL`, `READY_FOR_ACCEPTANCE`, `DEFERRED`, or `CANCELLED`.

## Phase Entry Gate Enforcement

A durable phase cannot be adopted for implementation merely because it exists. HIRMOS must run a Phase Entry Gate before `SESSION_SCOPE.md` adopts a phase and before `SESSION_STATE.json` reaches `implementation_readiness`.

The Phase Entry Gate is current-state-first. It verifies that the phase is the correct next governed unit of work based on `CURRENT_SYSTEM_STATE.md`, the durable `DELIVERY_PLAN.md`, and the inspected `PHASE-xx.md` file. The gate applies to greenfield, brownfield, and mixed phases.

### Universal Phase Entry Gate Checks

Before a session may adopt a durable phase for implementation, HIRMOS must verify:

```text
Phase file exists
Delivery Plan pointer exists
Current System State pointer concordance is satisfied
Lifecycle status is READY_FOR_ADOPTION, ACTIVE, or PARTIAL
Phase type is GREENFIELD, BROWNFIELD, or MIXED
Entry criteria are explicit and satisfied
Exit criteria are explicit enough to review later
Open blocking items are absent or resolved
Adoption constraints are satisfied
Session adoption is the correct next phase according to the Delivery Plan and Current System State
```

`READY_FOR_ACCEPTANCE` may be adopted only for review/close-only work. It must not authorize new implementation.

### Greenfield Phase Entry Gate

For `GREENFIELD` phases, the entry gate must confirm:

```text
MVP boundary is explicit
Primary user/workflow slice is explicit
Architecture dependency status is resolved enough for this phase
Prototype vs production intent is explicit
Out-of-scope expansion guard is explicit
```

A greenfield phase must not be adopted if the phase is trying to implement the whole product at once without a bounded MVP slice.

### Brownfield Phase Entry Gate

For `BROWNFIELD` phases, the entry gate must confirm:

```text
Preservation baseline is explicit
Affected existing surfaces are identified
Regression-sensitive behavior is identified
Do-not-touch boundaries are explicit
Compatibility and data/migration safety constraints are considered when relevant
```

A brownfield phase must not be adopted if the current system has not been inspected enough to identify preservation and regression risk.

### Mixed Phase Entry Gate

For `MIXED` phases, both the greenfield and brownfield entry gates apply. The phase may segment controls by workstream, but implementation readiness is blocked until both control groups have enough current-state evidence.

### Fail-Closed Rules

- `UNKNOWN` phase type blocks phase adoption and implementation readiness.
- `NOT_STARTED`, `BLOCKED`, `ACCEPTED`, `DEFERRED`, `SUPERSEDED`, or `CANCELLED` lifecycle status blocks implementation adoption.
- Missing or unsatisfied entry criteria block implementation readiness.
- Missing greenfield MVP/scope/architecture entry controls block greenfield or mixed phase adoption.
- Missing brownfield preservation/regression entry controls block brownfield or mixed phase adoption.
- Pointer disagreement between Current System State, Delivery Plan, Phase file, and Session Scope blocks implementation readiness.

## Phase Progress / Carry-Forward Enforcement

A durable phase may span multiple sessions. HIRMOS must preserve phase progress across session boundaries instead of treating each session as a disconnected attempt to finish the whole phase.

This enforcement is current-state-first and applies to `GREENFIELD`, `BROWNFIELD`, and `MIXED` phases. Before any continuation or close claim, HIRMOS must compare the adopted phase, the session scope, implementation-unit reviews, unresolved items, and Current System State delivery pointers.

### Phase Progress Ledger

Every adopted `PHASE-xx.md` must maintain a Phase Progress Ledger that records session-by-session progress:

```text
Session/archive
Adopted phase scope
Completed items
Partial items
Blocked items
Deferred items
Carry-forward items
Evidence pointer
Resulting lifecycle status
```

The ledger is append-only for historical rows. Corrections must be recorded as a new row or explicit correction note, not by erasing prior progress.

### Carry-Forward Enforcement

If a phase is not accepted at close, HIRMOS must classify all remaining work as one of:

```text
OPEN
PARTIAL
BLOCKED
DEFERRED
SUPERSEDED
CANCELLED
```

Every `OPEN`, `PARTIAL`, `BLOCKED`, or `DEFERRED` item must have a carry-forward target:

```text
same PHASE-xx.md
next PHASE-xx.md
_hirmos/system/accepted-state/CARRY_FORWARD.md
future session scope
explicit cancellation/supersession rationale
```

### Universal Progress Rules

- `PARTIAL` close is valid only when incomplete work is recorded in the Phase Progress Ledger and Carry-Forward Items.
- `BLOCKED` close is valid only when blockers and required next actions are recorded.
- `DEFERRED` close is valid only when the target phase/session or accepted risk is recorded.
- A later session must inspect the previous Phase Progress Ledger before planning or continuing phase work.
- `CURRENT_SYSTEM_STATE.md` must point to the still-active phase or next phase after close.

### Greenfield Progress Rules

For `GREENFIELD` or `MIXED` phases, partial progress must preserve MVP boundary clarity. HIRMOS must not convert scaffolding/prototype progress into product-complete or production-ready truth unless the phase evidence supports that claim.

Required greenfield progress checks:

```text
MVP items completed / partial / not started
Prototype-vs-production posture preserved
Architecture gaps carried forward
Out-of-scope expansions recorded as deferred or rejected
```

### Brownfield Progress Rules

For `BROWNFIELD` or `MIXED` phases, partial progress must preserve existing-system safety. HIRMOS must not accept a phase when preservation, regression, compatibility, migration, or data-safety checks remain unresolved.

Required brownfield progress checks:

```text
Preservation baseline still valid
Affected surfaces updated or carried forward
Regression-sensitive behavior reviewed or carried forward
Do-not-touch boundary violations absent or explicitly escalated
Migration/data-safety gaps carried forward
```

### Fail-Closed Rules

- A delivery-governed close with phase lifecycle result `PARTIAL`, `BLOCKED`, or `DEFERRED` fails if carry-forward obligations are missing.
- A delivery-governed continuation fails if a previous partial phase has no Phase Progress Ledger.
- Phase progress cannot be inferred from chat summaries alone.
- A phase cannot advance to `ACCEPTED` while unresolved adopted work remains open, partial, blocked, or deferred without explicit exclusion/deferral.
- `CURRENT_SYSTEM_STATE.md`, `DELIVERY_PLAN.md`, and `PHASE-xx.md` must agree on the active/next phase after partial or blocked close.


## Phase Acceptance Enforcement

A phase may move to `ACCEPTED` only through a close-time Phase Acceptance Evidence Gate. Acceptance is not a narrative claim; it is a durable lifecycle transition supported by session evidence.

### Phase Acceptance Evidence Gate

Before `PHASE-xx.md` may record `Lifecycle status: ACCEPTED`, HIRMOS must verify:

- all phase exit criteria are satisfied or explicitly deferred/excluded with rationale;
- all adopted Session Scope items are reviewed;
- every implementation unit has execution evidence and unit review;
- `SESSION_SCOPE.md` close verification records phase coverage and acceptance verdict;
- `SESSION_EXECUTION.md` close/update control pointers records the accepted phase transaction;
- Delivery Plan and Phase file status are updated;
- `CURRENT_SYSTEM_STATE.md` delivery pointers are refreshed;
- unresolved, partial, blocked, or deferred work is reconciled before acceptance.

### Greenfield Acceptance Rules

Greenfield phases require MVP-slice evidence, architecture-to-implementation reconciliation, prototype-vs-production claim control, and explicit carry-forward for known gaps. `ACCEPTED` must not mean product-complete unless the phase objective says so.

### Brownfield Acceptance Rules

Brownfield phases require preservation evidence, affected-surface review, regression-sensitive behavior review, compatibility/data-safety review when applicable, and confirmation that do-not-touch boundaries were respected.

### Mixed Acceptance Rules

Mixed phases must satisfy both Greenfield Acceptance Rules and Brownfield Acceptance Rules before `ACCEPTED` is allowed.

### Fail-Closed Rules

HIRMOS must fail closed if a phase is marked or proposed as `ACCEPTED` without complete acceptance evidence, if adopted work remains unresolved without explicit exclusion/deferral, or if durable Delivery Plan / Phase / Current System State pointers are not updated consistently.


## CLI / Status UX Phase Lifecycle Reporting

`hirmos status` must expose phase lifecycle state in a clear operator-facing report whenever delivery governance is active or Current System State contains delivery pointers. This report is read-only and must never mutate durable delivery artifacts.

Required Phase Lifecycle Status Report fields:

- Active delivery ID
- Delivery Plan path
- Active Phase path
- Phase lifecycle status
- Phase type
- Phase Entry Gate status
- Phase adoption status
- Phase Progress Ledger status
- Carry-Forward Items status
- Phase Acceptance Evidence Gate status
- Missing evidence / blocked controls
- Current System State pointer concordance
- Exactly one recommended next command

Greenfield status UX must report MVP boundary status, architecture dependency status, prototype-vs-production expectation, and scope expansion risk.

Brownfield status UX must report preservation baseline status, affected existing surfaces status, regression-sensitive behavior status, do-not-touch boundary status, and migration/data safety status when applicable.

Mixed phase status UX must report both greenfield and brownfield status groups and must block simplified single-mode interpretation.

### Status Blockers

`hirmos status` must explicitly report `Status Blocked By Phase Lifecycle Conflict` when phase lifecycle status, phase type, Current System State pointers, Delivery Plan, active Phase file, or Session Scope adoption are missing or contradictory.

Status must not imply that a phase can be accepted unless the Phase Acceptance Evidence Gate is complete and close-time delivery status reconciliation is ready.

### Exactly-One-Next-Command Rule

The status report must end with exactly one recommended governed command. If lifecycle evidence is missing, the recommended command is normally `hirmos status` until the controlling artifact is repaired, or `hirmos continue` when the next safe action is to complete missing session evidence.
