# design-agent Default Entrypoint

## Execution Contract

### Purpose

Route the active Design lifecycle boundary to the installed `design-agent` capabilities required by `_hirmos/session/SESSION_EXECUTION.md` controls.

### Produces

- Design capability activation decisions in `_hirmos/session/SESSION_EXECUTION.md`.
- Design-stage artifacts produced by selected capability entrypoints.

## Production-shaped Design obligation

For implementation-capable software work, Design must prefer production-shaped architecture by default. Do not treat demo/local shortcuts as equal options when a production-shaped local/default path is practical.

Design must identify material engineering areas affected by the request, including persistence, auth, provider APIs, file/object storage, background jobs, credit/usage accounting, secrets/configuration, deployment assumptions, and validation evidence.

If Design authorizes a weaker prototype, fixture, local-only, or demo-only result, record the limitation explicitly in `DESIGN.md`, `SESSION_CONTRACT.md`, and `unresolved-items.md` or carry-forward notes as appropriate.

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
5. Record each capability decision in `_hirmos/session/SESSION_EXECUTION.md`.
6. Do not claim Design completion or Implementation readiness until expected artifacts/evidence exist and required controls are satisfied or explicitly not applicable.
7. Do not start Implementation from raw inputs, prototype findings, Delivery Plan alone, or incomplete Session Contract.

## Shared Extension Method

### Shared invariants

1. Requirement inputs are source material, not requirements authority.
2. Design owns governed requirements, system/application design, delivery structure, technical review, Session Contract, and implementation readiness.
3. Design may satisfy requirements/design/planning requests without activating Implementation.
4. Design may route back to Understand System State when evidence is missing, stale, contradictory, or too narrow.
5. Design may authorize Implementation only through a ready Session Contract and Implementation Readiness decision.
6. Interaction modes change visibility, not Design authority.

### Source input surfaces

Design may inspect `_hirmos/inputs/`, especially `_hirmos/inputs/uploads/`, `_hirmos/inputs/prototypes/`, and `_hirmos/inputs/references/`. These files are raw source material only and must be reconciled through `DESIGN.md` source matrix, `DESIGN.md` source matrix, `REQUIREMENTS_BASELINE.md`, `SESSION_CONTRACT.md`, or `unresolved-items.md` before they become governed authority.

### Operating sequence

1. Confirm Design is active in `_hirmos/session/SESSION_EXECUTION.md`.
2. Use `_hirmos/core/protocol/CAPABILITY_ROUTING.md` to decide which design capabilities are `REQUIRED`, `OPTIONAL`, `SKIPPED`, `NOT_APPLICABLE`, or `BLOCKED`.
3. Produce governed requirements before system/application design relies on requirement authority.
4. Produce system/application design from governed requirements plus system-state evidence.
5. Decide the smallest sufficient governed delivery shape using `DELIVERY_GOVERNANCE.md`; do not equate broad greenfield or brownfield work with automatic multi-session delivery.
6. Produce technical review material when assumptions, risks, or reviewer inspection paths exist.
7. Produce a Session Contract and Implementation Readiness before Implementation can begin.
8. Record Design capability results, route-backs, unresolved-item producer outcomes, and readiness gates in `SESSION_EXECUTION.md`.

### Durable Delivery / Phase Capability Rewire

This section now implements Delivery Shape Capability Routing.

Use `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` to select the smallest sufficient governed delivery shape.

```text
SINGLE_SESSION_VERTICAL_SLICE → session-contract → implementation-readiness
SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS → session-contract → implementation-readiness
MULTI_SESSION_DELIVERY → delivery-design → session-contract → implementation-readiness
MULTI_SESSION_DELIVERY_WITH_PHASE_FILES → delivery-design → phase-contracting → session-contract → implementation-readiness
```

Design must explain why the selected shape is safer than smaller alternatives and why larger alternatives would add unnecessary governance overhead. For a single-session shape, the Session Contract must record affirmative bounded-scope safety evidence.

### Design authority rules

- Governed requirements must preserve source evidence, requirement statement, decision/assumption status, acceptance criteria, unresolved effects, and downstream Design or Implementation effect.
- Raw inputs, prototypes, screenshots, notes, tickets, and prior documents remain evidence until reconciled by Design.
- The Session Contract is downstream implementation authority and must be used by implementation unit planning, implementation unit review, session implementation review, and Update System State readiness.
- Design must use project type, active stack, and stack contexts as routing/evidence inputs, not unchecked authority.

### Interaction-mode visibility

- `domain_expert`: surface user-owned decisions, recommended baseline, blockers, implementation-readiness summary, and concise artifact/reviewer pointers.
- `technical_supervisor`: surface artifact status, technical assumptions, readiness rationale, delivery/phase/session-contract mapping, and evidence implications.
- `framework_diagnostics`: surface routing, controls, artifact instantiation, unresolved-item contributions, route-backs, and validation/evidence details.

### Terminal outcomes

`COMPLETED`, `NEEDS_USER_DECISION`, `BLOCKED`, `ROUTE_BACK_REQUIRED`, and `NOT_APPLICABLE` use the meanings defined by the capability entrypoint and the active lifecycle boundary.

### Unresolved-item producer discipline

Every capability in this extension is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. Each capability must record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve the protocol fields including current status, downstream impact, and revalidation point.

### Runtime integration and production-readiness design discipline

Design must identify material runtime integration areas, record integration posture, avoid claiming fixture/mock/boundary/local/production integration levels beyond evidence, and use `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` when integration posture affects scope or readiness.

### Claim reconciliation inputs

Design must preserve the authority and traceability needed for later claim reconciliation. It must not present readiness claims that cannot be reconciled against artifacts, final files, command/log evidence, or user-environment verification.

### Autonomous technical authorization discipline

Design should authorize safe local/default technical progress when this avoids unnecessary user decisions. It must distinguish internal technical defaults from user-owned product, budget, compliance, or production-provider decisions.

### Local setup and role-workflow smoke evidence

When local setup or role-workflow behavior affects readiness, Design must require the evidence artifacts governed by `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md`; tests/build/lint alone do not prove runtime or workflow readiness.

### Requirements baseline design authority

Material requirements must be normalized into `_hirmos/session/REQUIREMENTS_BASELINE.md` before Design or Delivery Plan mapping relies on them.

### Cross-run synthesis responsibilities

When prior runs, accepted state, or carry-forward items affect scope, Design must reconcile them into governed requirements, Design, Session Contract, or unresolved items instead of relying on chat memory.


A Durable Delivery Plan remains the durable authority for multi-session delivery shapes.
When the selected delivery shape uses phase files, Design uses durable `PHASE-xx.md` contracts.
