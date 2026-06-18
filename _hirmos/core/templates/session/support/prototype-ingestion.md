# Prototype Ingestion

Status: active-session source-input artifact.
Lifecycle owner: Understand System State.
Primary capability: `system-state-agent/prototype-ingestion`.
Purpose: extract prototype/POC evidence while separating observed behavior, intended behavior, implementation accident, and unknown intent.

A prototype is evidence, not authority. Prototype code, file layout, mock data, and generated architecture must not become Design authority by accident.

## Prototype Inventory

| ID | Prototype / POC material | Type | Location | Readable? | Notes |
|---|---|---|---|---|---|

Prototype types may include: screenshot flow, clickable prototype, generated app, exploratory code, mock data, architecture sketch, API sample, other.

## Observed Behavior

| Behavior / workflow / screen | Prototype ID | Evidence | Confidence | Notes |
|---|---|---|---|---|

## Intended Behavior Signals

| Intended behavior | Source | Prototype ID | Confidence | Notes |
|---|---|---|---|---|

## Unknown or Ambiguous Intent

| Unknown / ambiguity | Why it matters | Proposed handling | Unresolved item ID |
|---|---|---|---|

## Extracted Product / Domain Concepts

| Concept | Evidence | Type | Notes |
|---|---|---|---|

Types may include: role, workflow, screen, data concept, permission, integration, notification, report, rule, state, edge case.

## Implementation Details That Are Evidence Only

List prototype implementation details that must not become Design authority unless later accepted.

| Detail | Why it may be accidental | Safe handling |
|---|---|---|

## Conflicts

| Conflict | Involved sources | Why it matters | Proposed handling | Unresolved item ID |
|---|---|---|---|---|

## Preservation Expectations

List prototype behaviors that the user may expect to preserve if converting a prototype to product.


## Prototype-Specific Findings

When multiple prototypes exist, preserve prototype-specific details before set-level reconciliation.

| Prototype ID | Intended behavior | Observed behavior | Business logic / rules | Data contracts | Integrations | Assumptions | Production risks | Requirement candidates |
|---|---|---|---|---|---|---|---|---|

## Prototype Set Reconciliation

Complete this section when more than one prototype, generated app, screenshot flow, demo, or POC input is present.

### Shared Core Signals

| Signal | Prototype IDs | Signal type | Requirement impact | Notes |
|---|---|---|---|---|

Signal types may include: capability, workflow, actor, business rule, data expectation, integration, UI pattern, security assumption, operational constraint.

### Business Logic Consolidation

| Business logic area | Classification | Prototype IDs | Requirement impact | Notes |
|---|---|---|---|---|

Classifications:

```text
SHARED_CORE_RULE
SHARED_PATTERN_WITH_VARIANTS
CONFLICTING_LOGIC_REQUIRES_RESOLUTION
PROTOTYPE_SPECIFIC_RULE
```

### Data Contract Consolidation

| Data expectation | Prototype IDs | Shared / variant / conflict | Requirement candidate | Notes |
|---|---|---|---|---|

Do not define final schema here. Extract inputs, outputs, transformations, validations, and format expectations as requirements evidence.

### Integration Consolidation

| Integration area | Prototype IDs | Repeated system/service | Direction / sequence | Variant or conflict | Requirement candidate |
|---|---|---|---|---|---|

### Workflow Consolidation

| Workflow area | Prototype IDs | Classification | Requirement candidate | Notes |
|---|---|---|---|---|

Classifications:

```text
SHARED_CORE_WORKFLOW
WORKFLOW_VARIANT
CONFLICTING_WORKFLOW
PROTOTYPE_SPECIFIC_WORKFLOW
```

### Conflict Register

| Conflict ID | Prototypes involved | Conflict type | Description | Severity / impact | Must resolve before requirements baseline? | Unresolved item ID |
|---|---|---|---|---|---|---|

Conflict types may include: business rule, workflow, actor, integration, data expectation, UI behavior, scope, security/compliance, operational readiness.

### Variant Register

| Variant ID | Prototypes involved | Variant description | Could be configuration/option? | Requirement handling |
|---|---|---|---|---|

### Normalized Requirement Candidates

| Candidate ID | Candidate requirement | Source prototype signals | Classification | Requirements baseline handling |
|---|---|---|---|---|

Do not silently merge conflicts. Do not treat prototype-specific behavior as global truth. If multiple prototypes exist and this reconciliation is missing, requirements normalization must be `BLOCKED` or `GATING_DECISION_REQUIRED`.


## Handoff to Understand System State

List focus areas that system-state understanding must inspect because of the prototype.

## Handoff to Design

List prototype-derived evidence Design may use after reconciliation.

## Completion

- Terminal state: COMPLETED | NEEDS_USER_DECISION | BLOCKED | NOT_APPLICABLE
- SESSION_EXECUTION.md updated: yes / no
- Unresolved-item contribution completed: yes / no / not applicable
