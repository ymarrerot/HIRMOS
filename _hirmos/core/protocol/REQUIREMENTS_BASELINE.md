# Requirements Baseline and Coverage Mapping

Status: core protocol.

## Purpose

`REQUIREMENTS_BASELINE.md` is the canonical normalized requirements-control artifact for a governed HIRMOS product/change.

It bridges raw user inputs and Design. It prevents requirement loss when a project has multiple source inputs such as uploaded requirements, notes, prototype material, UI design notes, research notes, prior accepted state, and conversation context.

It is intentionally compact and operational. It is not a heavyweight software requirements specification.

## Separation of authority

| Surface | Responsibility |
|---|---|
| Raw source inputs | Original user-provided material. Examples: `_hirmos/inputs/uploads/requirements.txt`, prototype files, UI notes, reference material, conversation context. |
| `DESIGN.md` source matrix / `DESIGN.md` source matrix | Source inventory and evidence extraction from raw material. Prototype-derived findings remain evidence, not accepted requirements. |
| `REQUIREMENTS_BASELINE.md` | Normalized accepted requirement universe, requirement IDs, source mapping, scope classification, unresolved/gated requirements, delivery-unit mapping, and coverage status. |
| `DESIGN.md` / `DELIVERY_PLAN.md` | Design decisions and delivery decomposition based on the accepted requirements baseline. |
| `EVIDENCE.md` claim reconciliation / evidence artifacts | Evidence for claims that requirements were implemented, verified, blocked, or deferred. |
| `CURRENT_SYSTEM_STATE.md` | Merged accepted current truth after close; it references the accepted requirements baseline but does not replace it. |

Firm rule: raw requirement notes are not governed requirements until normalized into `REQUIREMENTS_BASELINE.md` or explicitly classified as out of scope, gated, blocked, duplicate, superseded, or not applicable.

## Required artifact locations

Active session:

```text
_hirmos/session/REQUIREMENTS_BASELINE.md
```

Accepted state after close when product requirements remain relevant across sessions:

```text
_hirmos/system/accepted-state/REQUIREMENTS_BASELINE.md
```

The accepted-state requirements baseline is the durable requirement universe for future sessions. Future sessions may refine it, but must preserve traceability to source inputs and accepted decisions.

## Input normalization model

HIRMOS must support multiple requirement sources. Each source item must be classified before Design relies on it.

Canonical source classifications:

```text
RAW_REQUIREMENT_NOTE
PROTOTYPE_DERIVED_SIGNAL
UI_UX_DESIGN_NOTE
REFERENCE_MATERIAL
CONVERSATION_CONTEXT
ACCEPTED_STATE_REQUIREMENT
RESEARCH_BACKED_DEFAULT
MIXED_SOURCE
BLOCKED_UNREADABLE
NOT_APPLICABLE
```

Canonical requirement classes:

```text
FUNCTIONAL
WORKFLOW_STATE
DATA_DOMAIN
UI_UX
INTEGRATION
SECURITY_PRIVACY
AUDIT_EVIDENCE
RUNTIME_OPERATIONS
NON_FUNCTIONAL
ACCEPTANCE_CRITERION
NON_GOAL
CONSTRAINT
```

Canonical scope statuses:

```text
IN_SCOPE
OUT_OF_SCOPE
NON_GOAL
GATED
ASSUMPTION_BASED
DEFERRED
BLOCKED
DUPLICATE
SUPERSEDED
NOT_APPLICABLE
```

Canonical coverage statuses:

```text
NOT_STARTED
PLANNED
IN_PROGRESS
IMPLEMENTED
PARTIAL
VERIFIED
DEFERRED
BLOCKED
NOT_APPLICABLE
REJECTED
```

Coverage status is a requirement-coverage status, not evidence status. Evidence status must use canonical claim/evidence states from `EVIDENCE.md` claim reconciliation.

## Requirements baseline required sections

`REQUIREMENTS_BASELINE.md` must include:

1. Baseline Identity
2. Source Inputs and Classification
3. Product Goal
4. Scope Boundary
5. Requirement Catalog
6. Non-Goals and Exclusions
7. Gated / Unresolved Requirements
8. Requirement-to-Delivery Mapping
9. Coverage Status
10. Source Traceability
11. Change / Supersession Log
12. Baseline Self-Check

## Requirement ID rules

Each material requirement must have a stable ID.

Recommended prefixes:

```text
REQ-FUNC-###
REQ-WFLOW-###
REQ-DATA-###
REQ-UI-###
REQ-INT-###
REQ-SEC-###
REQ-AUDIT-###
REQ-NFR-###
REQ-ACCEPT-###
REQ-NONGOAL-###
```

IDs must be stable once accepted. If a requirement changes materially, mark the old requirement `SUPERSEDED` and create or reference the replacement ID.

## Source traceability rule

Every material requirement must include at least one source reference or an explicit rationale for why no source reference exists.

Acceptable source references include:

- uploaded file path and section heading;
- prototype ingestion artifact section;
- source materials artifact section;
- accepted prior requirements baseline ID;
- user-approved decision/Current Continuation Snapshot;
- conversation-derived request, when recorded in `SESSION_CONTRACT.md` parent authority.

Do not silently promote prototype behavior, UI design notes, research-backed defaults, or model assumptions into confirmed requirements.

## Design gating rule

Before Design produces a Delivery Plan for governed software work, every material source-derived requirement must be one of:

- represented in `REQUIREMENTS_BASELINE.md` with an ID;
- classified as a non-goal or out of scope;
- recorded as gated/unresolved;
- recorded as blocked/unreadable;
- recorded as duplicate/superseded/not applicable.

Design must not rely only on raw `requirements.txt`, prototype notes, UI notes, or chat memory when a requirements baseline is applicable.

## Delivery mapping rule

Before implementation authorization, each `IN_SCOPE`, `ASSUMPTION_BASED`, or `DEFERRED` requirement that affects delivery must be mapped to one or more Delivery Units, phases, or explicit carry-forward records.

A Delivery Plan may intentionally defer a requirement, but the deferral must be visible in the baseline coverage map.

## Close/update-state rule

During `hirmos close`, HIRMOS must update the session requirements baseline coverage and merge durable changes into `_hirmos/system/accepted-state/REQUIREMENTS_BASELINE.md` when requirements remain relevant across sessions.

Close may not claim complete requirements coverage while any material requirement remains `NOT_STARTED`, `PARTIAL`, `BLOCKED`, or `DEFERRED` unless that status is explicitly accepted as carry-forward or out of scope.

## Current-state relationship

`CURRENT_SYSTEM_STATE.md` must reference the accepted requirements baseline and summarize coverage posture, but it must not replace the requirement catalog.

`REQUIREMENTS_BASELINE.md` answers: what must be satisfied and where is it mapped?

`CURRENT_SYSTEM_STATE.md` answers: what is accepted current truth now?

## Normalized intake vs requirements baseline

HIRMOS may receive several requirements-oriented source layers at once: raw notes, uploaded requirements, UI notes, prototype evidence, generated-app behavior, prior accepted requirements, research-backed defaults, and conversation decisions. These layers must not be flattened directly into requirements.

Use this two-step model:

1. **Intake extraction** — `DESIGN.md` source matrix and `DESIGN.md` source matrix classify and extract evidence, assumptions, conflicts, delivery-target signals, and candidate requirement signals. These artifacts are governed intake artifacts, not requirements authority.
2. **Requirements baseline** — `REQUIREMENTS_BASELINE.md` converts accepted, assumption-based, gated, rejected, deferred, duplicate, superseded, and not-applicable requirement signals into a stable requirement catalog with source traceability and coverage mapping.

Firm rule: a source signal is not accepted requirement truth merely because it appears in a raw upload, prototype, screenshot, generated app, or research note. It becomes governed requirements authority only when represented in `REQUIREMENTS_BASELINE.md` with source traceability, class, scope status, and uncertainty handling.

## Intake classification preservation

When creating or refining `REQUIREMENTS_BASELINE.md`, preserve these distinctions from intake artifacts:

```text
CONFIRMED_SOURCE_SIGNAL
ASSUMPTION
RESEARCH_BACKED_DEFAULT
DECLARED_DELIVERY_TARGET
PROPOSED_DELIVERY_TARGET
OPEN_QUESTION
PENDING_CONFIRMATION
PROTOTYPE_OBSERVED_BEHAVIOR
PROTOTYPE_INTENDED_BEHAVIOR
PROTOTYPE_VARIANT
PROTOTYPE_CONFLICT
```

Do not silently collapse these classifications into one truth layer. If a requirement depends on an assumption, research-backed default, proposed delivery target, prototype variant, or unresolved question, mark the requirement `ASSUMPTION_BASED`, `GATED`, `DEFERRED`, or `BLOCKED` as appropriate.

## Requirements uncertainty severity

Requirements uncertainty must be classified without duplicating the unresolved-item system. Use this severity model inside `REQUIREMENTS_BASELINE.md`, and feed material items to `unresolved-items.md` using the normal unresolved-item protocol:

```text
SAFE_TO_ASSUME
PROCEED_WITH_CAUTION
GATING_DECISION_REQUIRED
NOT_APPLICABLE
```

Escalate to `GATING_DECISION_REQUIRED` when the unresolved item materially changes scope boundaries, actor/identity model, workflow shape, data model shape, integration strategy, security/privacy/compliance posture, delivery-target feasibility, or acceptance expectations.

## Requirement granularity rule

A requirements baseline must be explicit enough that Design and Implementation do not have to guess major behavior. For workflow-heavy or approval/state-machine-heavy systems, table-only catalog rows are not sufficient by themselves.

For each material workflow requirement, include or reference a detailed requirement record containing:

- actor(s);
- preconditions;
- trigger;
- main flow;
- alternate flows;
- edge cases or invalid transitions;
- expected outcome;
- source references;
- unresolved/gated items, if any.

If a developer could reasonably ask “what should happen here?” for a material flow, the requirements baseline is incomplete or must mark the point as gated/unresolved.

## Multiple-prototype intake rule

When prototype-like inputs exist, `DESIGN.md` source matrix must make clear whether there is one prototype or multiple prototype candidates.

If multiple prototypes exist, HIRMOS must preserve two layers of evidence before requirements normalization:

1. **Prototype-specific findings** — observed behavior, intended behavior, business logic, data contracts, integrations, assumptions, risks, and requirement candidates for each prototype.
2. **Prototype-set reconciliation** — shared signals, business-logic consolidation, data-contract consolidation, integration consolidation, workflow consolidation, conflict register, variant register, core-system candidates, and normalized requirement candidates.

Multiple prototypes without prototype-set reconciliation are an inconsistent intake state for requirements normalization. Design must not proceed as if normalization were optional. Either perform prototype-set reconciliation, or record `BLOCKED` / `GATING_DECISION_REQUIRED` with rationale.

Prototype-specific details must remain consultable. A prototype-set summary is not a lossless substitute for the individual prototype findings.

## Prototype conversion rule

Prototype-derived findings must be converted into requirements-level meaning before they influence Design.

Allowed conversions include:

- requirement candidates;
- system behaviors;
- workflow expectations;
- business rules;
- data expectations;
- integration expectations;
- constraints;
- assumptions;
- open questions;
- unresolved conflicts or variants.

Forbidden conversions include:

- treating prototype code as final architecture;
- copying prototype schema/file layout as system design truth;
- treating demo behavior as validated requirements;
- promoting prototype-specific behavior into global requirements without source classification;
- silently merging conflicting prototype behavior.

## Staged delivery target preservation

When delivery targets are explicit, implied, or proposed, preserve the distinction between:

```text
DECLARED_DELIVERY_TARGET
PROPOSED_DELIVERY_TARGET
```

Declared targets are source-confirmed. Proposed targets are HIRMOS recommendations or collaborative planning hypotheses. Proposed targets must not be recorded as source-confirmed requirements unless accepted by the user or another governed decision artifact.

## Salvage lineage applied

This protocol intentionally salvages the useful parts of earlier HIRMOS requirements/prototype work:

- requirements input pack classification: preserve confirmed facts, assumptions, open questions, goals, constraints, delivery signals, and source alignment;
- requirements source-of-truth discipline: normalize requirements without architecture or implementation details;
- prototype source-of-truth discipline: separate intended behavior, observed behavior, business logic, data contracts, integrations, missing production concerns, conflicts, and candidate requirements;
- prototype set reconciliation: preserve shared signals, variants, contradictions, and conflict registers across multiple prototypes.

It does not restore the old heavy extension structure. The current framework keeps these concepts in the existing lifecycle, artifacts, and close gate.

## Failure conditions

Fail closed or route back when:

- source inputs exist but are not inventoried or classified;
- raw requirements are used directly as Design authority while a baseline is missing;
- prototype findings are promoted into requirements without classification;
- Delivery Plan omits material in-scope requirements without mapping, deferral, or rationale;
- close claims complete requirements coverage without updating coverage status;
- accepted requirements baseline and current system state contradict each other;
- multiple prototype inputs exist but prototype-set reconciliation is missing, blocked, or not reflected in requirements normalization;
- confirmed facts, assumptions, research-backed defaults, proposed targets, prototype variants, or prototype conflicts are silently collapsed into accepted requirements;
- workflow-heavy requirements are represented only as vague catalog rows without flow details, edge cases, or unresolved-item classification.

## Cross-run coverage synthesis rule

When HIRMOS has access to multiple implementation candidates, self-runs, prototypes, generated apps, UX drafts, external spec-tool outputs, or comparable source packages, requirements coverage must be judged against the accepted `REQUIREMENTS_BASELINE.md`, not against the apparent completeness of any one candidate.

Cross-run sources are evidence inputs. They may reveal missed requirements, stronger UX patterns, better tests, cleaner specifications, or stronger package hygiene, but they do not become requirements authority until their lessons are normalized into the requirements baseline, delivery plan, technical review, or carry-forward state.

Before claiming total or near-total requirements coverage, HIRMOS must check:

- every material `IN_SCOPE` requirement has a stable ID;
- every material acceptance criterion is represented or explicitly classified;
- UI/UX requirements are not collapsed into generic CRUD coverage;
- integration and AI-governance requirements are represented separately from feature pages;
- non-goals are preserved so the implementation does not overbuild;
- each requirement has a delivery-unit mapping, a coverage status, and an evidence/carry-forward posture.

Firm rule: do not claim `100% requirements coverage`, `complete MVP coverage`, or equivalent unless `REQUIREMENTS_BASELINE.md` supports that claim and `EVIDENCE.md` claim reconciliation records the evidence status for the coverage claim.
