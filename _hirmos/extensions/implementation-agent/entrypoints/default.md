# implementation-agent Default Entrypoint

## Execution Contract

### Purpose

Route the active Implementation lifecycle boundary to installed implementation-agent capabilities required by `_hirmos/session/SESSION_EXECUTION.md` controls.

### Produces

- Capability activation decisions recorded in `_hirmos/session/SESSION_EXECUTION.md`.
- Capability-owned artifacts produced by selected capability entrypoints.

## Production-shaped Implementation obligation

Implementation must realize the accepted Design with production-shaped engineering defaults unless the Session Scope explicitly authorizes a weaker result.

Do not satisfy a contract by choosing a shortcut that changes the architecture shape of the system, such as using synchronous request-time work for long-running provider operations, using non-durable storage for durable business data, or using preflight-only checks for credit/usage mutations.

When a production-shaped implementation cannot be completed in scope, Implementation must record the blocker or limitation, route back when required, and avoid close/completion claims beyond the supported evidence.

- Route-back records when Implementation discovers invalid upstream authority.
- Unresolved-item contributions or blockers when implementation evidence exposes material uncertainty.

### Terminal States

- COMPLETED — selected capabilities completed and required controls are satisfied or explicitly not applicable.
- NEEDS_USER_DECISION — a selected capability discovered a gated user-owned unresolved item.
- BLOCKED — required capability inputs, artifacts, evidence, or provider resolution are missing or unsafe.
- ROUTE_BACK_REQUIRED — capability work invalidated an earlier lifecycle authority and must route back.
- NOT_APPLICABLE — no capability from this extension is required for the active lifecycle boundary.

## Required behavior

1. Apply the shared extension method in this entrypoint before routing implementation capabilities.
2. Read `_hirmos/core/protocol/CAPABILITY_ROUTING.md` when routing is material to the active command.
3. Select only capabilities required by the active lifecycle boundary and execution controls.
4. Read each selected capability entrypoint before running that capability.
5. Record capability decisions in `_hirmos/session/SESSION_EXECUTION.md`.
6. Do not claim capability completion until expected artifacts/evidence exist or are explicitly not applicable with rationale.
7. Do not allow implementation capabilities to silently rewrite Design authority, Session Scope, or accepted system state.

## Shared Extension Method

### Core Principle

Implementation is governed realization of accepted Design, not merely code editing. Implementation must execute only what the active Session Scope and approved Implementation Unit artifacts authorize.

### Required Inputs Before Implementation

Implementation requires a ready `_hirmos/session/SESSION_SCOPE.md`, resolved gated items in `_hirmos/session/unresolved-items.md`, current project evidence, and active execution controls in `_hirmos/session/SESSION_EXECUTION.md`.

### Implementation Unit Discipline

An Implementation Unit is an execution contract, not a generic task or prompt. The Session Scope Implementation Unit Plan must cover 100% of authorized implementation scope before execution begins. Each `IU-xx.md` must state scope, files/areas, acceptance checks, validation expectations, evidence requirements, and route-back triggers.

### Implementation Execution Discipline

Implementation execution performs only the work authorized by the target `IU-xx.md` artifact. Inspect current files before editing, modify only authorized areas, record actions/evidence in the unit, and route back when evidence invalidates Design, scope, or current-state assumptions.

### Validation and Evidence Discipline

Implementation is incomplete without evidence. Record validation commands, outcomes, not-run/not-applicable checks, limitations, and runtime posture. Do not convert a passing claim into completion unless the evidence supports the exact unit/session scope.

### Unit Review and Session Implementation Review

Unit review is local, specific, and evidence-based. Session implementation review aggregates unit results against the Session Scope, validation evidence, unresolved items, and scope coverage before Update System State readiness is claimed.

### Retry and Escalation Discipline

Retry must be evidence-based and bounded. Retry is valid only when the failed attempt produced enough evidence to define a safe next attempt; otherwise route back instead of retrying.

### Route-Back Rules

Implementation routes back when it discovers missing authority, contradictory current state, unsafe scope, unresolved gated decisions, invalid Design assumptions, or evidence that the active unit/session cannot be completed safely.

### Interaction-Mode Visibility

- `domain_expert`: surface user-owned decisions, blockers, concise status, completion/readiness, or artifact pointers.
- `technical_supervisor`: surface changed files, validation/evidence, assumptions, limitations, and review implications.
- `framework_diagnostics`: surface routing, controls, artifacts, unresolved-item contributions, route-backs, retries, and terminal-state basis.

### Completion Rule

Implementation may claim completion only when all authorized units are executed or validly not applicable, local reviews are recorded, validation/evidence gates are satisfied, gated unresolved items are closed or non-blocking, and session implementation review supports the claim.

### Unresolved-item producer discipline

Every capability in this extension is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. Each capability must record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve the protocol fields including current status, downstream impact, and revalidation point.

### Stack and project-context responsibilities

Implementation must follow active project type, stack context, package scripts, framework conventions, and current working-copy evidence; it must not assume generated or stale stack state.

### Runtime integration implementation discipline

Use `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` when runtime services affect execution or evidence. Do not claim fixture/mock/boundary/local/production integration levels beyond what commands, files, services, or user-environment verification support.

### Claim reconciliation discipline

Implementation must preserve final-file, command/log, validation, runtime, and user-environment verification evidence needed for `_hirmos/session/EVIDENCE.md`. Chat-only summaries are not accepted implementation evidence.

### Autonomous technical progress discipline

Attempt safe local technical progress before deferring it. Internal technical defaults may be chosen when reversible and evidence-backed; user-owned product, compliance, budget, external-production-provider, or destructive decisions remain gated.

### Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` when claiming local runtime behavior, role workflow readiness, or user-environment verification. Tests/build/lint alone do not prove runtime or role-workflow readiness.

### Runtime/evidence and smoke artifact responsibilities

Canonical runtime/evidence and smoke artifacts must be materialized before their claims are merged or surfaced as complete.

### Implementation close handoff responsibilities

Implementation close handoff must identify accepted outcomes, rejected/not-applied outcomes, validation evidence, unresolved carry-forward items, and Update System State readiness.

### Cross-run implementation lesson application

Apply accepted prior run lessons and carry-forward items only when they are present in accepted-state artifacts or active session artifacts, not from memory alone.