# understand-system-state

## Execution Contract

### Purpose

Produce general and User Request-focused system-state understanding before Design owns governed requirements, scope, or implementation authorization.

### Produces

- `_hirmos/session/DESIGN.md`
- `_hirmos/session/unresolved-items.md` updates
- `_hirmos/session/SESSION_EXECUTION.md` system-state control status

### Terminal States

- COMPLETED — general and focused system-state understanding is recorded with observed/inferred/assumed/unknown separation.
- NEEDS_USER_DECISION — state uncertainty creates a user-owned blocker before Design.
- BLOCKED — required system evidence is missing, contradictory, or unsafe to infer from.
- ROUTE_BACK_REQUIRED — later-stage discovery requires regenerating system-state understanding.

## Activation triggers

- Any governed software work is requested.
- Design, Implementation, or Update System State lacks sufficient current-state evidence.
- A later stage discovers new system truth that invalidates earlier state understanding.

## Required inputs

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/DESIGN.md` when source materials exist
- `_hirmos/session/DESIGN.md` when prototype/POC inputs exist
- repository/project evidence when a codebase exists
- `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` when it exists; if missing, record the absence explicitly
- supporting accepted-state records when they exist: `_hirmos/system/accepted-state/CARRY_FORWARD.md` and conditional `_hirmos/system/accepted-state/DECISION_LOG.md` when explicit governance is active; latest-close metadata lives inside `CURRENT_SYSTEM_STATE.md`
- session archives only when needed as history/evidence, not as current truth

## Execution controls contributed

- system-state control
- working-copy control
- source-evidence control when source material exists
- unresolved-item control when needed

## Method

1. Verify the active working-copy root and record it in `SESSION_EXECUTION.md`.
2. Read request intake and source/prototype ingestion outputs when present.
3. Perform general and focused system-state understanding. For general understanding, inspect broadly enough to avoid tunnel vision:
   - project/repository structure;
   - installed framework state;
   - application/runtime shape;
   - existing docs/specs;
   - `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` as the first accepted-state source when it exists;
   - supporting accepted-state records: `CURRENT_SYSTEM_STATE.md` latest-close metadata, `CARRY_FORWARD.md`, and conditional `DECISION_LOG.md` when active;
   - session archives only as history/evidence when needed, not as current truth;
   - project maturity and confidence.
4. Perform focused system understanding guided by the User Request and source-input focus map:
   - directly affected areas;
   - indirectly affected areas;
   - current behavior to preserve;
   - constraints and risks that Design must consider.
5. For every important claim, classify evidence as observed, inferred, assumed, unknown, blocked, or not applicable.
6. Classify project type and active stack from evidence, not preference alone.
7. Record preservation requirements discovered from existing system behavior, prototype behavior, or accepted-state history.
8. Record system-state unknowns, contradictions, or risks in `_hirmos/session/unresolved-items.md` when they affect safe Design, Implementation, or Update System State.
9. Produce a Handoff to Design that clearly states what Design may use as evidence and what it must not treat as authority.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## Project Context and Stack Classification

When this capability encounters project-type or stack evidence, record material findings in `DESIGN.md` / `SESSION_SCOPE.md`, `stack-resolution.json` for machine-readable stack routing, or `SESSION_EXECUTION.md` as required by active controls.

User Request labels and prototype technology signals are focus evidence, not final classification authority.


## Runtime integration responsibilities

When material runtime services are involved, follow `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

Record or consume `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` as required by execution controls.

Do not claim fixture/mock/boundary/local/production integration levels beyond what the active artifacts and evidence support.

## Current-System-State-First Requirement

Firm rule: HIRMOS must not begin meaningful Design or Implementation until Understand System State has read `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` when it exists, or has explicitly recorded that it is missing.

Required sequence for accepted-state understanding:

1. Check whether `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` exists.
2. If it exists, read it first as the primary accepted current-state source.
3. Read `_hirmos/system/accepted-state/CARRY_FORWARD.md` and conditional `_hirmos/system/accepted-state/DECISION_LOG.md` as supporting accepted-state records when present and active. Read latest-close metadata from `CURRENT_SYSTEM_STATE.md`.
4. Use session archives only as history/evidence or to resolve contradictions. Do not reconstruct current truth from archives when `CURRENT_SYSTEM_STATE.md` exists.
5. Record the read status, missing status, contradictions, and confidence in `_hirmos/session/DESIGN.md` and `_hirmos/session/SESSION_EXECUTION.md`.
6. Set terminal state `BLOCKED` when accepted-state contradictions make safe Design impossible without clarification.

Completion is invalid until the current-system-state-first control is `SATISFIED` or explicitly `NOT_APPLICABLE` with rationale.
