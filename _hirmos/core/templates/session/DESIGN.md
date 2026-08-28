# Design

Status: conditional active-session design authority artifact.
Purpose: record material technical decisions, architecture constraints, integration boundaries, alternatives, and technical-review points when separate design authority is justified by `SESSION_SCOPE.md`.

`DESIGN.md` is subordinate to `SESSION_SCOPE.md`. It does not define session scope by itself. Only design decisions or sections explicitly adopted in `SESSION_SCOPE.md` govern implementation and close verification.

## 1. Design Identity

| Field | Value |
|---|---|
| Session ID | `<session-id>` |
| Design version | `<v0>` |
| Design status | `DRAFT / READY_FOR_IMPLEMENTATION / ACCEPTED / SUPERSEDED` |
| Governing session scope | `_hirmos/session/SESSION_SCOPE.md` |
| Requirements authority, if any | `_hirmos/session/REQUIREMENTS.md` or `NOT_APPLICABLE` |
| Optional authority justification | `_hirmos/session/SESSION_SCOPE.md#optional-authority-artifact-justification-and-adoption` |

## 2. Responsibility Boundary

This artifact owns:

- architecture decisions;
- data and persistence decisions;
- provider and external-service boundaries;
- runtime/job-processing design;
- security, privacy, and operational decisions;
- technical assumptions, alternatives, risks, and technical-review points.

This artifact does not own:

- authorized session outcome or final scope;
- normalized requirement catalog;
- delivery shape authority except as design input;
- implementation-unit plans before baseline acceptance;
- evidence details or implementation claims;
- accepted-state truth.

Those responsibilities belong to `SESSION_SCOPE.md`, `REQUIREMENTS.md`, `implementation-units/`, `EVIDENCE.md`, and accepted-state artifacts as applicable.

## 3. Design Source Matrix

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

Record material current-system-state findings here when they affect Design or Implementation.

- `CURRENT_SYSTEM_STATE.md` read status: READ | MISSING | NOT_APPLICABLE | BLOCKED
- Accepted-state records reviewed:
- Repository/project evidence inspected:
- Current-state findings that affect scope/design:
- Current-state contradictions, risks, or blockers routed to `unresolved-items.md`:
- Delivery pointers / active delivery context reviewed:

## Governed Requirements

Summarize only the requirement IDs or scope sections that `SESSION_SCOPE.md` adopted and that materially affect design. Do not recreate the full requirement catalog here.

| Requirement / scope reference | Design implication | Notes |
|---|---|---|
| `<REQ-ID or SESSION_SCOPE section>` | `<implication>` | `<notes>` |

## System / Application Design Decisions

| Decision ID | Area | Decision | Rationale / evidence | Adopted by SESSION_SCOPE? | Review status |
|---|---|---|---|---|---|
| SD-001 | Architecture | `<decision>` | `<rationale>` | `YES / NO / PARTIAL` | `PENDING / REVIEWED / CHANGED` |


## Delivery Structure Decision

Delivery Shape Decision note: Design may record technical implications of the delivery shape selected in `SESSION_SCOPE.md`, but `SESSION_SCOPE.md` owns delivery shape authority. Do not create delivery or implementation-unit obligations here.

- Selected delivery shape from `SESSION_SCOPE.md`:
- Technical implications:
- Design risks created by this shape:

## Production-Shaped Engineering Decisions

Required for implementation-capable software sessions before implementation authorization. Decisions here provide technical detail for the Production-Shaped Engineering Gate in `SESSION_SCOPE.md`; they do not replace it.

| Area | Material? | Production-shaped default | Session decision | If weaker, why allowed? | Blocks implementation? | Evidence required |
|---|---:|---|---|---|---:|---|
| Persistence / database | | Durable persistence; local mirrors intended production where practical | | | | |
| Auth / authorization | | Server-side user/resource isolation for protected data/actions | | | | |
| Background jobs / long-running work | | Job/worker/queue/cron shape for slow provider/file/AI work | | | | |
| Usage / quotas / billing / quotas | | Transactional, idempotent, or concurrency-safe accounting | | | | |
| Provider APIs / external services | | Provider boundary, env validation, failure posture | | | | |
| File or object storage | | Validation, safe paths, retention/handoff hygiene | | | | |
| Secrets and environment configuration | | `.env.example`; no secrets/runtime data in handoff/release | | | | |
| Automated testing posture | | Repository-native unit/component/integration strategy for material software behavior; no universal HIRMOS coverage threshold | | | | |
| Critical-flow / runtime smoke evidence | | Runtime/smoke/user-flow evidence plan for critical paths; automated tests do not substitute for required runtime evidence | | | | |

Implementation is not authorized while any material area is `Blocks implementation = YES`, unless `SESSION_SCOPE.md` explicitly changes scope to exclude that area.

## Runtime Integration and Production Readiness Design

Identify material runtime integration areas created or affected by this design.

| Area | Material? | Current / planned posture | Production recommendation | Decision owner | Surface to Domain Expert now? |
|---|---:|---|---|---|---:|


- Material Integration Areas:
- Recommended Production Options:
- Current-Session Authorization:
- Production Readiness Checkpoint Basis:
- Update System State Carry-Forward:

Design must distinguish:

- safe local/demo progress;
- integration-boundary work;
- local real integration;
- production provider integration;
- blocked decisions, credentials, or accounts.

## Technical Assumptions and Review Notes

List technical assumptions, tradeoffs, risks, alternatives considered, and review points. Material items must also appear in `_hirmos/session/unresolved-items.md` as gated, non-gating, or technical-review items.

| Item ID | Assumption / decision / risk | Why it matters | Review path | Status |
|---|---|---|---|---|
| TD-001 | `<item>` | `<why>` | `<artifact/path or reviewer>` | `PENDING / REVIEWED / CARRIED` |

## Technical Review and Implementation Readiness Basis

Use this section for reviewer-facing technical readiness rationale. Do not create implementation-unit files or detailed implementation-unit plans here before baseline acceptance.

| Area | Decision / finding | Evidence | Status |
|---|---|---|---|
| Current-state basis sufficient | | | PENDING |
| Requirements/design scope sufficient | | | PENDING |
| Stack and runtime posture | | | PENDING |
| Production-shaped engineering risks | | | PENDING |
| Unresolved-item gate | | | PENDING |
| Implementation readiness | READY / BLOCKED / NEEDS_ROUTE_BACK / NOT_APPLICABLE | | PENDING |

Implementation may proceed only when `SESSION_SCOPE.md`, unresolved-item status, production-shaped engineering gate, and this readiness basis agree that implementation is authorized.


## Implementation Authorization Inputs

State what must exist before implementation can begin. `SESSION_SCOPE.md` owns authorization; this section records design-side readiness inputs only.

- Session Scope complete and non-placeholder:
- Adopted requirements/design decisions aligned:
- Unresolved-item gate clear or explicitly handled:
- Production-shaped engineering decisions aligned with `SESSION_SCOPE.md`:
- Implementation-unit artifacts deferred until baseline acceptance/amendment:

## Not Authorized

List work that this design does not authorize.

## Route-Back Conditions

List conditions that require returning to Understand System State, Requirements, Session Scope, or Design.


## Project-Type / Stack / Delivery Routing Context

Record technical routing context only when it affects design. `SESSION_SCOPE.md` owns delivery shape authority.

- Project-Type Classification:
- Stack Classification:
- Stack Contexts:
- Delivery Routing Impact:

## Design Self-Check

- [ ] `SESSION_SCOPE.md` justifies why separate design authority exists.
- [ ] This design records technical decisions only; it does not redefine session scope.
- [ ] Only decisions adopted by `SESSION_SCOPE.md` are treated as implementation obligations.
- [ ] Any separate `REQUIREMENTS.md` is referenced as requirement authority, not duplicated.
- [ ] No full implementation-unit artifacts or detailed implementation-unit plans are created here before baseline acceptance.
- [ ] Material technical assumptions and review points are mirrored in `unresolved-items.md`.
- [ ] The production-shaped engineering decisions agree with `SESSION_SCOPE.md`.
