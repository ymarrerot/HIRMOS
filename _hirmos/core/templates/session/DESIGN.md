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

## Current-State Basis

Record material current-system-state findings here when they affect Design or Implementation. Do not create a separate `DESIGN.md` current-state basis artifact for new sessions.

- `CURRENT_SYSTEM_STATE.md` read status: READ | MISSING | NOT_APPLICABLE | BLOCKED
- Accepted-state records reviewed:
- Repository/project evidence inspected:
- Current-state findings that affect scope/design:
- Current-state contradictions, risks, or blockers routed to `unresolved-items.md`:
- Delivery pointers / active delivery context reviewed:

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

## Delivery Shape Decision

This section is the Delivery Structure Decision for the current session and records the selected delivery shape.

State the smallest sufficient governed delivery shape:

```text
SINGLE_SESSION_VERTICAL_SLICE
SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS
MULTI_SESSION_DELIVERY
MULTI_SESSION_DELIVERY_WITH_PHASE_FILES
UNCERTAIN
```

Explain why this is the smallest shape that preserves engineering quality, implementation truth, reviewability, validation, continuity, and accepted-state integrity. Also explain why smaller and larger shapes were rejected.

## Delivery / Slice / Phase / Implementation-Unit Mapping

| Governed requirement or design item | Delivery shape item | Slice / phase / implementation unit | Contract artifact | Notes |
|---|---|---|---|---|

## Technical Assumptions and Review Notes

List technical assumptions, tradeoffs, risks, alternatives considered, and review points. Reference `DESIGN.md` technical review when separate reviewer-facing detail exists.

## Unresolved Item Disposition

Summarize gated, non-gating, and technical-review items from `unresolved-items.md`. Do not claim implementation readiness while gated items remain unresolved.

## Implementation Authorization Inputs

State what must exist before Implementation can begin:

- Session Scope;
- delivery/phase/delivery-unit source, if applicable;
- Implementation Readiness;
- technical review path, if applicable;
- required evidence criteria;
- active execution controls satisfied.

## Not Authorized

List work that Design does not authorize.

## Route-Back Conditions

List conditions that require returning to Understand System State or regenerating Design.



## Production-Shaped Engineering Gate — Design Decision

Required for implementation-capable software sessions before implementation authorization.

For each material area, record the production-shaped default, the session decision, whether weaker posture is explicitly authorized, and whether implementation is blocked.

| Area | Material? | Production-shaped default | Session decision | If weaker, why allowed? | Blocks implementation? | Evidence required |
|---|---:|---|---|---|---:|---|
| Persistence / database | | Durable persistence; local mirrors intended production where practical | | | | |
| Auth / authorization | | Server-side user/resource isolation for protected data/actions | | | | |
| Background jobs / long-running work | | Job/worker/queue/cron shape for slow provider/file/AI work | | | | |
| Usage / quotas / billing / quotas | | Transactional, idempotent, or concurrency-safe accounting | | | | |
| Provider APIs / external services | | Provider boundary, env validation, failure posture | | | | |
| File or object storage | | Validation, safe paths, retention/handoff hygiene | | | | |
| Secrets and environment configuration | | `.env.example`; no secrets/runtime data in handoff/release | | | | |
| Critical-flow tests / smoke evidence | | Test/smoke/runtime evidence plan for critical paths | | | | |

Implementation is not authorized while any material area is `BLOCKS implementation = YES`, unless the Session Scope explicitly changes scope to exclude that area.

If any item uses a prototype, fixture, demo-only, local-only, or non-production-shaped posture, the limitation must also appear in the Session Scope and unresolved/carry-forward controls as appropriate.

## Runtime Integration and Production Readiness Design

Identify material runtime integration areas created or affected by this Design.

| Area | Material? | Current / planned posture | Production recommendation | Decision owner | Surface to Domain Expert now? |
|---|---:|---|---|---|---:|

Design must distinguish:

- safe local/demo progress;
- integration-boundary work;
- local real integration;
- production provider integration;
- blocked decisions, credentials, or accounts.

Do not authorize Implementation to claim more than the posture recorded here and in the Session Scope.

- Material Integration Areas:
- Recommended Production Options:
- Current-Session Authorization:
- Production Readiness Checkpoint Basis:
- Update System State Carry-Forward:

## Technical Review and Implementation Readiness Basis

Use this section for reviewer-facing technical assumptions, production-shaped engineering posture, risk decisions, and implementation-readiness rationale. Do not create separate `DESIGN.md` technical review or `DESIGN.md` readiness basis artifacts for new sessions.

| Area | Decision / finding | Evidence | Status |
|---|---|---|---|
| Current-state basis sufficient | | | PENDING |
| Requirements/design scope sufficient | | | PENDING |
| Stack and runtime posture | | | PENDING |
| Production-shaped engineering risks | | | PENDING |
| Unresolved-item gate | | | PENDING |
| Implementation readiness | READY / BLOCKED / NEEDS_ROUTE_BACK / NOT_APPLICABLE | | PENDING |

Implementation may proceed only when `SESSION_SCOPE.md`, unresolved-item status, production-shaped engineering gate, and this readiness basis agree that implementation is authorized.

## Project-Type / Stack / Delivery Routing Context

Former project-context support-artifact content lives here under the strict-necessity model.

- Project-Type Classification:
- Stack Classification:
- Stack Contexts:
- Delivery Routing Impact:
