# system-state-agent Default Entrypoint

## Execution Contract

### Purpose

Route the active lifecycle boundary to the installed `system-state-agent` capabilities required by `SESSION_EXECUTION.md` controls.

### Produces

- Capability activation decisions recorded in `_hirmos/session/SESSION_EXECUTION.md`.
- Capability-owned artifacts produced by the selected capability entrypoints.
- Unresolved-item contributions when selected capabilities discover material uncertainty.

### Terminal States

- COMPLETED — selected capabilities completed and required controls are satisfied or explicitly not applicable.
- NEEDS_USER_DECISION — a selected capability discovered a gated user-owned unresolved item.
- BLOCKED — required capability inputs, artifacts, or provider resolution are missing or unsafe.
- ROUTE_BACK_REQUIRED — capability work invalidated an earlier lifecycle authority and must route back.
- NOT_APPLICABLE — no capability from this extension is required for the active lifecycle boundary.

## Required behavior


### Governance posture check

System-state updates are governed synchronization, not after-the-fact cleanup for unauthorized work. Do not convert ungoverned edits into accepted state without recording the governing session, source artifacts, evidence, and any deviation/correction status.


1. Apply the shared extension method in this entrypoint before routing system-state capabilities.
2. Read `_hirmos/core/protocol/CAPABILITY_ROUTING.md` when routing is material to the active command.
3. Select only capabilities required by the active lifecycle boundary and execution controls.
4. Read each selected capability entrypoint before running that capability.
5. Record capability decisions in `_hirmos/session/SESSION_EXECUTION.md`.
6. Do not claim capability completion until expected artifacts/evidence exist or are explicitly not applicable.

## Shared Extension Method

### Method invariants

1. User Request and source inputs are focus inputs, not authority.
2. Prototype and POC materials are evidence, not authority.
3. Understand System State must include general system understanding and request-focused system understanding.
4. Evidence must distinguish observed, inferred, assumed, unknown, blocked, and not applicable.
5. Material uncertainty must enter `_hirmos/session/unresolved-items.md`.
6. Update System State consumes reviewed outcomes; it does not create missing Design or Implementation results.
7. Capability completion must be recorded in `_hirmos/session/SESSION_EXECUTION.md`.

### Project type and stack responsibilities

System-state-agent identifies project type, stack evidence, package scripts, provider/runtime surfaces, local setup clues, and current working-copy boundaries as evidence for later Design and Implementation. It does not create governed requirements or implementation authority.

### Capability sequence for `hirmos start`

Typical sequence: `request-intake` → `source-material-ingestion` when source materials exist → `prototype-ingestion` when prototypes/POCs/screenshots/generated apps exist → `understand-system-state` → Design-stage capabilities when system-state controls are satisfied.

### Capability sequence for `hirmos close`

Typical sequence: read `SESSION_EXECUTION.md` and close controls → confirm reviewed outcomes/evidence → run `update-system-state` → archive session and reset active session state when normal close succeeds.

### Non-authority rule

This method does not authorize requirements, Design, Implementation, or accepted-state mutation. Those authorities are owned by lifecycle rules and stage-specific controls.

### Unresolved-item producer discipline

Every capability in this extension is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. Each capability must record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve the protocol fields including current status, downstream impact, and revalidation point.

### Runtime integration system-state signals

Understand System State should identify existing and requested database/auth/provider/storage/payment/deployment surfaces, environment patterns, local dependencies, production-readiness indicators, and prototype/demo/fallback behavior without turning those signals into Design authority.

### Close / archive integrity discipline

The update-system-state capability treats close as an accepted-state transaction and verifies accepted outcomes, rejected/not-applied outcomes, evidence-only artifacts, carry-forward items, archive preservation, active-session reset, and post-close status consistency before normal close success is claimed.

### Claim reconciliation during state update

Update System State reconciles accepted-state and close claims before applying accepted outcomes. It must not promote claims into accepted state unless final files, evidence, archive records, and session state support them.

### Autonomous technical discovery discipline

System-state-agent must identify safe technical progress opportunities before Design or Implementation asks routine setup questions. Inspect package scripts, env examples, database/auth/provider/storage/deployment evidence, migrations/seeds/tests/build/dev scripts, package scripts, and local service clues when safe.

### Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for local runtime, user-environment verification, or role workflow readiness claims. Tests/build/lint alone do not prove local runtime or role workflow readiness.

### Current-state method responsibilities

During Understand System State, read `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` first when it exists. During Update System State, merge accepted outcomes into `CURRENT_SYSTEM_STATE.md`, update current-state metadata, `CARRY_FORWARD.md`, and conditional `DECISION_LOG.md` when active, and keep MVP completion, runtime readiness, production readiness, provider readiness, compliance readiness, and go-live approval as separate tracks.

### Current-system-state-first understanding

Record the read status, contradictions, confidence, and Design handoff for `CURRENT_SYSTEM_STATE.md` in `_hirmos/session/DESIGN.md` and update current-system-state-first controls in `_hirmos/session/SESSION_EXECUTION.md`.

### Accepted-state invariant and canonical-value responsibilities

Preserve accepted-state artifact roles: `CURRENT_SYSTEM_STATE.md` is current truth; latest-close metadata is navigation; `CARRY_FORWARD.md` is continuation control; conditional `DECISION_LOG.md` is durable decision history when explicit governance is active. Preserve accepted-state invariant and canonical-value responsibilities when reading or updating accepted state.

### Update System State close-time responsibilities

Do not merge accepted outcomes or recommend close success until close-time evidence, claim reconciliation, accepted-state invariant blocks, canonical evidence/status/runtime values, and framework validation requirements are satisfied.

### Requirements source-input responsibilities

Source requirements, prototype-derived signals, UI notes, reference material, and accepted prior requirements must be inventoried and classified before Design relies on them. Source material ingestion and prototype ingestion extract signals; they do not create governed requirements by themselves.
