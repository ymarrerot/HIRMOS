# Vertical Slice and Status UX Protocol

Status: core protocol.
Purpose: keep HIRMOS delivery momentum clear and simple while preserving lifecycle, execution-control, unresolved-item, evidence, and accepted-state governance.

This protocol governs how HIRMOS turns Delivery Plans, Delivery Plans, Phases, Session Contracts, Implementation Units, checkpoints, status, and close output into a clear user experience.

## Core rule

```text
HIRMOS may make the next slice obvious, but it must not make the next slice look authorized until the governing artifacts and execution controls support it.
```

Vertical-slice UX is a presentation and routing discipline. It does not replace Design authority, Implementation authorization, unresolved-item governance, evidence requirements, or Update System State.

## Vertical slice definition

A vertical slice is a bounded user-valuable or system-valuable delivery segment that can be designed, implemented, reviewed, and closed with clear evidence.

In HIRMOS, a vertical slice is represented by one of these governed sources:

- a Phase Contract;
- a Phase Contract;
- a Session Contract for small targeted work;
- an explicitly reviewed implementation-continuation scope.

A vertical slice is not a casual task list item.

## Delivery status model

Every Phase that appears in a Delivery Plan should have a status.

Allowed statuses:

```text
PROPOSED
READY_FOR_SESSION_SCOPE
ACTIVE_SESSION_SCOPE
IMPLEMENTING
IMPLEMENTATION_COMPLETE
UPDATE_STATE_READY
CLOSED_ACCEPTED
BLOCKED
NOT_SELECTED
SUPERSEDED
```

Status meanings:

- `PROPOSED`: the unit exists as a proposed delivery segment but is not ready to authorize a session.
- `READY_FOR_SESSION_SCOPE`: the unit has enough Design authority to source a Session Contract.
- `ACTIVE_SESSION_SCOPE`: the current session is governed by this unit or a bounded subset of it.
- `IMPLEMENTING`: Implementation has started for the active Session Contract scope.
- `IMPLEMENTATION_COMPLETE`: Implementation and required reviews are complete, but accepted state has not necessarily been updated.
- `UPDATE_STATE_READY`: reviewed outcomes are ready for Update System State.
- `CLOSED_ACCEPTED`: outcomes were accepted and archived through Update System State.
- `BLOCKED`: continuation is blocked by unresolved items, missing authority, missing evidence, invalid assumptions, or failed controls.
- `NOT_SELECTED`: the unit is not part of the active scope.
- `SUPERSEDED`: the unit was replaced by a later Design decision or route-back.

## User-visible momentum rule

HIRMOS should always try to make these clear:

1. what slice is active now;
2. what was completed in this step;
3. what is blocked, if anything;
4. what artifact backs the claim;
5. what the next recommended action is;
6. what the next recommended Phase is when the current unit closes.

This is required for all interaction modes, but the level of detail changes by mode.

## Domain Expert status UX

In `domain_expert` mode, status and checkpoint output should be concise.

Show:

- current user-facing stage;
- active Phase name when relevant;
- whether HIRMOS needs a decision;
- the recommended baseline or next step;
- material blockers;
- production-readiness implications when they affect a release or decision;
- inspection pointers only when useful.

Do not expose capability routing, all execution-control rows, or template mechanics unless they create a user decision or blocker.

## Technical Supervisor status UX

In `technical_supervisor` mode, status and checkpoint output should include:

- active Phase / Phase status;
- source artifacts;
- unresolved-item disposition;
- implementation authorization status;
- validation/evidence status;
- runtime integration posture summary when material;
- next command and next delivery recommendation.

## Framework Diagnostics status UX

In `framework_diagnostics` mode, status and checkpoint output should include full lifecycle boundary, control, capability, artifact, unresolved-item, evidence, route-back, and Phase status details.

## Next command recommendation rule

Every advancing command response should recommend exactly one primary next command or terminal next action unless the session is blocked.

Examples:

```text
Recommended next command: hirmos continue
Recommended next command: hirmos close
Recommended next action: answer the gated decision above
Recommended next action: run hirmos status after reviewing the blocker
```

Do not recommend multiple competing primary commands.

## Next phase recommendation rule

When a Phase is closed and accepted, HIRMOS should recommend the next phase when the Delivery Plan contains remaining units.

The recommendation must include:

- Phase ID/name;
- why it is recommended next;
- prerequisite blockers, if any;
- required command to start or continue it;
- whether it needs Design refresh before Implementation.

Do not imply the next phase is authorized unless its source contract is ready and current.

## Status command rule

`hirmos status` should produce a concise status report by default and support deeper inspection through interaction mode or explicit user request.

It must report:

- active session or no active session;
- active lifecycle boundary;
- active Phase / Phase, if any;
- current terminal/continuation state;
- pending or blocked controls;
- gated unresolved items;
- latest governed checkpoint;
- implementation/evidence status when active;
- runtime integration/production readiness status when material;
- next allowed action;
- next recommended Phase when known.

`hirmos status` remains read-only.

## Close output rule

After successful `hirmos close`, HIRMOS should surface:

- what was accepted into system state;
- where the session was archived;
- remaining carry-forward items;
- production-readiness or evidence limitations;
- next recommended Phase or next recommended command.

Close output must not introduce new Design or Implementation work. It may recommend the next slice based on existing Delivery Plan authority.

## Route-back and correction rule

If later evidence shows that a selected Phase, status, or next recommendation was wrong, HIRMOS must:

1. record a route-back in `SESSION_EXECUTION.md`;
2. mark affected Phase status as `BLOCKED` or `SUPERSEDED`;
3. update the governing Design artifact through the proper lifecycle path;
4. avoid continuing from stale status summaries.

## Prohibited behavior

HIRMOS must not:

- treat a Phase title as implementation authority;
- skip Session Contract because a slice sounds obvious;
- use status output to satisfy pending controls;
- claim a unit is complete without implementation/evidence review;
- claim a unit is closed without Update System State;
- recommend the next unit as authorized when unresolved items or stale Design block it;
- hide blockers to preserve momentum.

## Cross-run UX/operator-flow synthesis

When comparing implementation candidates or prototypes, HIRMOS must score UX/operator usability as a first-class delivery concern, not as decoration after data/API work.

For internal workflow applications, a vertical slice is incomplete if the user cannot understand and execute the workflow from the UI without inspecting raw database records or framework artifacts.

Cross-run UX lessons should be integrated into existing Phases / delivery slices by updating:

- `REQUIREMENTS_BASELINE.md` for UI/UX requirement coverage;
- `DELIVERY_PLAN.md` for user-journey sequencing;
- `SESSION_CONTRACT.md` for authorized UX work;
- `EVIDENCE.md` for operator journey checks;
- `EVIDENCE.md` claim reconciliation before claiming workflow readiness.

Minimum operator-flow questions for workflow-heavy apps:

```text
What needs my attention now?
What is blocked?
Who owns the next action?
What evidence supports the current recommendation?
What decision is required from the human?
What happens after this action?
```

Firm rule: strong backend/domain coverage does not justify a workflow-readiness claim when the operator cannot execute the intended workflow through the product surface.
