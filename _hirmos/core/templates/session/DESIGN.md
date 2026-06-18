# Design

Status: active-session Design authority artifact.
Purpose: convert User Request, source inputs, prototype findings, system-state findings, and unresolved-item dispositions into governed requirements, system/application design, delivery structure, technical review inputs, and implementation authorization inputs.

Design can satisfy requirements/design/planning requests. Implementation is not required unless the active request needs governed realization of accepted Design.

## Design Source Matrix

| Input | Source artifact | Authority status | Used for | Notes |
|---|---|---|---|---|

Authority statuses:

```text
source_input
evidence
governed_requirement
design_authority
assumption
unknown
rejected
```

## Governed Requirements

State the governed requirements produced by Design. Separate them from raw requirement inputs.

For each material requirement, include:

- requirement ID;
- requirement statement;
- source evidence;
- system-state evidence;
- decision / assumption status;
- acceptance criteria;
- affected lifecycle responsibility;
- unresolved items affecting the requirement.

## System / Application Design

Describe the architecture, workflows, data model, integration approach, permissions, UX/API boundaries, stack implications, preservation requirements, and operational constraints relevant to the active request.

## Delivery Structure Decision

State whether the work needs:

- no delivery decomposition;
- Delivery Plan;
- Phase decomposition;
- Delivery Unit Plan;
- Preservation Contract;
- Regression Evidence Strategy.

Explain why.

## Delivery / Phase / Delivery-Unit Mapping

| Governed requirement or design item | Delivery plan item | Phase or Delivery Unit | Contract artifact | Notes |
|---|---|---|---|---|

## Technical Assumptions and Review Notes

List technical assumptions, tradeoffs, risks, alternatives considered, and review points. Reference `support/technical-review.md` when separate reviewer-facing detail exists.

## Unresolved Item Disposition

Summarize gated, non-gating, and technical-review items from `unresolved-items.md`. Do not claim implementation readiness while gated items remain unresolved.

## Implementation Authorization Inputs

State what must exist before Implementation can begin:

- Session Contract;
- delivery/phase/delivery-unit source, if applicable;
- Implementation Readiness;
- technical review path, if applicable;
- required evidence criteria;
- active execution controls satisfied.

## Not Authorized

List work that Design does not authorize.

## Route-Back Conditions

List conditions that require returning to Understand System State or regenerating Design.


## Runtime Integration and Production Readiness Design

Identify material runtime integration areas created or affected by this Design.

| Area | Material? | Current / planned posture | Production recommendation | Decision owner | Surface to Domain Expert now? |
|---|---:|---|---|---|---:|

Use `_hirmos/session/support/runtime-integration-readiness.md` when any material area exists.

Design must distinguish:

- safe local/demo progress;
- integration-boundary work;
- local real integration;
- production provider integration;
- blocked decisions, credentials, or accounts.

Do not authorize Implementation to claim more than the posture recorded here and in the Session Contract.
