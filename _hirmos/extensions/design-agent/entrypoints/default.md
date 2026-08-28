# design-agent Default Entrypoint

## Execution Contract

### Purpose

Route the active Design lifecycle boundary to the installed `design-agent` capabilities required by `_hirmos/session/SESSION_LEDGER.md` controls.

### Produces

- Design capability activation decisions in `_hirmos/session/SESSION_LEDGER.md`.
- Design-stage artifacts produced by selected capability entrypoints.

## Production-shaped Design obligation

For implementation-capable software work, Design must prefer production-shaped architecture by default. Do not treat demo/local shortcuts as equal options when a production-shaped local/default path is practical.

Design must identify material engineering areas affected by the request, including persistence, auth, provider APIs, file/object storage, background jobs, usage/quota/accounting, secrets/configuration, deployment assumptions, and validation evidence.

If Design authorizes a weaker prototype, fixture, local-only, or demo-only result, record the limitation explicitly in `DESIGN.md`, `SESSION_SCOPE.md`, and `unresolved-items.md` or carry-forward notes as appropriate.

- Unresolved-item contributions when Design discovers material uncertainty.
- Route-back records when Design lacks safe system-state evidence.

### Terminal States

- COMPLETED — selected Design capabilities completed and required controls are satisfied or explicitly not applicable.
- NEEDS_USER_DECISION — a selected Design capability discovered a gated user-owned unresolved item.
- BLOCKED — required Design inputs, artifacts, or provider resolution are missing or unsafe.
- ROUTE_BACK_REQUIRED — Design work requires returning to Understand System State or regenerating Design authority.
- NOT_APPLICABLE — no Design capability is required for the active lifecycle boundary.

## Required behavior

1. Apply the shared extension method in this entrypoint before routing Design capabilities.
2. Read `_hirmos/core/protocol/CAPABILITY_ROUTING.md` when routing is material to the active command.
3. Select only capabilities required by the active Design boundary and execution controls.
4. Read each selected capability entrypoint before running that capability.
5. Record each capability decision in `_hirmos/session/SESSION_LEDGER.md`.
6. Do not claim Design completion or Implementation readiness until expected artifacts/evidence exist and required controls are satisfied or explicitly not applicable.
7. Do not start Implementation from raw inputs, prototype findings, Delivery Plan alone, or incomplete Session Scope.

## Shared Extension Method

### Shared invariants

1. Requirement inputs are source material, not requirements authority.
2. Design owns governed requirements, system/application design, delivery-baseline authority, phase/session baseline authority, technical review, Session Scope when a bounded session scope exists, and implementation readiness.
3. Design may satisfy requirements/design/planning requests without activating Implementation.
4. Design may route back to Understand System State when evidence is missing, stale, contradictory, or too narrow.
5. Design may authorize Implementation only through a ready focus-specific authority chain: a ready Session Scope for single-session work, or an accepted delivery baseline plus ready phase/session scope for delivery-governed work.
6. The canonical interaction posture changes visibility, not Design authority.

### Source input surfaces

Design may inspect `_hirmos/inputs/`, especially `_hirmos/inputs/uploads/`, `_hirmos/inputs/prototypes/`, and `_hirmos/inputs/references/`. These files are raw source material only and must be reconciled through the focus-appropriate `REQUIREMENTS.md`, `DESIGN.md`, `DELIVERY_SCOPE.md`, `SESSION_SCOPE.md`, or unresolved-item register before they become governed authority.

### Operating sequence

1. Confirm Design is active in `_hirmos/session/SESSION_LEDGER.md`.
2. Use `_hirmos/core/protocol/CAPABILITY_ROUTING.md` to decide which design capabilities are `REQUIRED`, `OPTIONAL`, `SKIPPED`, `NOT_APPLICABLE`, or `BLOCKED`.
3. Produce governed requirements before system/application design relies on requirement authority.
4. Produce system/application design from governed requirements plus system-state evidence.
5. Decide the smallest sufficient governed delivery shape using `DELIVERY_GOVERNANCE.md`; do not equate broad greenfield, brownfield, app-like, or framework-evaluated work with automatic multi-session delivery.
6. Produce technical review material when assumptions, risks, or reviewer inspection paths exist.
7. If `session_focus = delivery_baseline`, produce delivery-baseline authority and stop at Delivery Baseline — Review or Change; do not create `SESSION_SCOPE.md`, phase files, or implementation units by default.
8. If `session_focus = phase_session_baseline`, instantiate only the next needed phase file, create/narrow `SESSION_SCOPE.md`, and stop at Session Baseline — Review or Change before implementation.
9. Produce Implementation Readiness only after the focus-specific baseline has been accepted or amended.
10. Record Design capability results, route-backs, unresolved-item producer outcomes, and readiness gates in `SESSION_LEDGER.md`.

### PROD-L8.9 focus-aware delivery routing

This section implements focus-aware Delivery Shape Capability Routing.

Use `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` and `_hirmos/core/protocol/CAPABILITY_ROUTING.md` to select the smallest sufficient governed delivery shape and active `session_focus`.

```text
SINGLE_SESSION_MINIMAL / minimal_session
  session-scope only when bounded output authority is needed

SINGLE_SESSION_VERTICAL_SLICE / session_baseline
  session-scope → implementation-readiness

SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS / session_baseline
  session-scope → implementation-readiness

DELIVERY_BASELINE / delivery_baseline
  delivery-baseline

DELIVERY_PHASE_SESSION / phase_session_baseline
  phase-baseline → session-scope → implementation-readiness
```

For durable delivery work, Design must first produce a delivery baseline under `_hirmos/system/delivery/<delivery-id>/` and stop at `Delivery Baseline — Review or Change`. It must not create `SESSION_SCOPE.md`, `PHASE-xx.md`, or implementation units before delivery-baseline acceptance by default. After acceptance or amendment, Design may instantiate the next needed phase file and create the bounded phase/session `SESSION_SCOPE.md`.

Design must explain why the selected shape is necessary for the real software work, why a technically possible simpler shape is acceptable or insufficient, and why larger alternatives would add unnecessary governance/token overhead. When multi-session delivery is selected, Design must also explain why the selected phase count is the smallest honest count, how 2-phase and 3-phase alternatives were considered, and why any phase after phase 2 cannot be merged. For a single-session shape, the Session Scope must record affirmative bounded-scope safety evidence.

### Design authority rules

- Governed requirements must preserve source evidence, requirement statement, decision/assumption status, acceptance criteria, unresolved effects, and downstream Design or Implementation effect.
- Raw inputs, prototypes, screenshots, notes, tickets, and prior documents remain evidence until reconciled by Design.
- The Session Scope is downstream implementation authority and must be used by implementation unit planning, implementation unit review, session implementation review, and Update System State readiness.
- Design must use project type, active stack, and stack contexts as routing/evidence inputs, not unchecked authority.

### Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

### Terminal outcomes

`COMPLETED`, `NEEDS_USER_DECISION`, `BLOCKED`, `ROUTE_BACK_REQUIRED`, and `NOT_APPLICABLE` use the meanings defined by the capability entrypoint and the active lifecycle boundary.

### Unresolved-item producer discipline

Every capability in this extension that can discover uncertainty is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. Each such capability must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. For `delivery_baseline`, the target is `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`; for session/phase/implementation focus, the target is `_hirmos/session/unresolved-items.md`. When items exist, preserve the protocol fields including current status, downstream impact, and revalidation point.

### Runtime integration and production-readiness design discipline

Design must identify material runtime integration areas, record integration posture, avoid claiming fixture/mock/boundary/local/production integration levels beyond evidence, and use `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` when integration posture affects scope or readiness.

### Claim reconciliation inputs

Design must preserve the authority and traceability needed for later claim reconciliation. It must not present readiness claims that cannot be reconciled against artifacts, final files, command/log evidence, or user-environment verification.

### Autonomous technical authorization discipline

Design should authorize safe local/default technical progress when this avoids unnecessary user decisions. It must distinguish internal technical defaults from user-owned product, budget, compliance, or production-provider decisions.

### Automated testing design discipline

For implementation-capable software work, apply `_hirmos/core/protocol/VALIDATION_AND_EVIDENCE.md` before Implementation readiness. Inspect the repository's existing test framework, scripts, test locations, fixture/mocking conventions, and coverage policy when present. Design should identify which material behaviors are suitable for isolated automated tests and which require component, integration, contract, or runtime evidence instead.

Do not introduce a second test framework without repository/project justification. For greenfield or currently untested codebases that will add material testable logic, plan the smallest appropriate test harness as part of implementation. Keep this posture compact in `SESSION_SCOPE.md`; use `DESIGN.md` for extra technical detail only when separate design authority is justified.

### Local setup and role-workflow smoke evidence

When local setup or role-workflow behavior affects readiness, Design must require the evidence artifacts governed by `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md`; tests/build/lint alone do not prove runtime or workflow readiness.

### Requirements design authority

Material requirements must be normalized into the focus-appropriate `REQUIREMENTS.md`: delivery-level requirements under `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` during delivery baseline, and session-level requirements under `_hirmos/session/REQUIREMENTS.md` only when a bounded session scope justifies separate requirements authority.

### Cross-run synthesis responsibilities

When prior runs, accepted state, or carry-forward items affect scope, Design must reconcile them into focus-appropriate governed requirements, design, Delivery Scope, Session Scope, or unresolved items instead of relying on chat memory.


A Durable Delivery Plan remains the durable roadmap/register for multi-session delivery shapes.

## PROD-L8.9 command-selected focus route

The design-agent default method must select capability routing from `SESSION_STATE.json.session_focus`, the Delivery Shape Decision, and the active authority, then record the result in `SESSION_LEDGER.md`.

Canonical focus routes:

```text
SINGLE_SESSION_MINIMAL / minimal_session
  session-scope only when bounded output authority is needed

SINGLE_SESSION_VERTICAL_SLICE / session_baseline
  session-scope → implementation-readiness

SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS / session_baseline
  session-scope → implementation-readiness

DELIVERY_BASELINE / delivery_baseline
  delivery-baseline

DELIVERY_PHASE_SESSION / phase_session_baseline
  phase-baseline → session-scope → implementation-readiness
```

The method must not activate delivery-baseline for safe single-session work, must not activate phase-baseline until the delivery baseline is accepted or amended, and must not allow implementation-readiness to pass until the selected focus-specific authority chain is satisfied.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.


## PROD-L8.13 Current-State-First Generated Artifact Cleanup

Generated artifacts and checkpoint text must explain routing from current system state, scope size, validation risk, continuity need, and artifact-authority requirements. Do not use greenfield/brownfield labels as the primary reason for delivery/session/phase selection. If a project-type label is useful, record it as supporting evidence metadata or phase-control routing metadata only.
