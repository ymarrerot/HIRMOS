# Spec: Requirements SoT

## Purpose

Define a complete, unambiguous, and implementation-ready specification of **what** the system must do.

This document is a **Source of Truth (SoT)**.

It must:
- eliminate ambiguity
- define scope boundaries
- serve as the contract for downstream system, architecture, and implementation planning

It must also:
- preserve staged delivery targets correctly when relevant
- ingest `REQUIREMENTS_INPUT_PACK.md` correctly when present
- ingest prototype-derived SoT artifacts correctly when present

## Output

- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)

## Stack-neutrality rule

`REQUIREMENTS_SOT.md` is normally stack-neutral.

Selected stack context does not normally define requirements truth. Stack-derived consequences should enter requirements planning only when a project-level stack decision creates a genuine requirement-level constraint that has already been accepted upstream.

## Core Principles

1. No ambiguity.
2. No implicit behavior.
3. No missing flows.
4. No mixing with architecture.
5. No implementation details.
6. Strong normalized requirements intake when present.
7. Structured prototype-derived intake when present.
8. Requirements-level preservation of staged delivery context when relevant.

## Required Inputs

Use all relevant requirements inputs provided by the Orchestrator, including:
- system idea / description
- requirement notes
- supporting documents
- constraints
- target users
- goals
- staged delivery targets or staged-delivery notes when relevant
- other structured project inputs

When present, also ingest:
- _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`)
- _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`)

Also check for prototype-derived SoT artifacts in `_hirmos/artifacts/sot/` when present.

Supported prototype-derived intake artifacts are:
- _hirmos/artifacts/sot/PROTOTYPE_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SOT.md`)
- _hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md`)
- `_hirmos/artifacts/sot/PROTOTYPE*_SOT.md` when multiple prototype-specific SoT files exist

## Requirements Input Pack Intake Rules

If _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`) exists, treat it as a first-class normalized upstream intake artifact.

It becomes the **primary normalized requirements-intake artifact** for requirements generation. Raw files under `_hirmos/inputs/requirements-agent/requirements/` remain supporting discovery material and MUST NOT automatically trigger regeneration or override of the existing pack.

This means:
- use it to strengthen completeness
- use it to preserve explicit assumptions and open questions
- use it to preserve delivery-target distinctions when relevant

But:
- do NOT treat it as Source of Truth
- do NOT blindly convert all candidate or inferred items into confirmed requirements
- do NOT collapse confirmed facts, assumptions, and research-backed notes into one undifferentiated layer
- do NOT let raw files under `_hirmos/inputs/requirements-agent/requirements/` implicitly override a curated existing `REQUIREMENTS_INPUT_PACK.md`
- do NOT silently promote research-backed defaults into source-confirmed requirements
- do NOT let material assumptions disappear if they still require confirmation

## Classification Preservation Rules

When ingesting `REQUIREMENTS_INPUT_PACK.md`, preserve the distinction between:
- source-confirmed requirements signals
- planning assumptions
- research-backed defaults
- declared delivery targets
- proposed delivery targets
- unresolved items that still require explicit confirmation or requirements-level handling

`REQUIREMENTS_SOT.md` may refine and normalize these inputs, but it must not silently collapse them into one undifferentiated truth layer.

## Unresolved-Item Severity Rules

When materially relevant unresolved items remain unresolved, classify them into:

- **Safe-to-assume** — Low-impact unresolved items that do not materially change scope boundaries, actor model, major workflow shape, key data model assumptions, delivery-target feasibility, or acceptance expectations.
- **Proceed-with-caution** — Items that influence planning quality or downstream detail, but do not make the current planning baseline structurally invalid if handled as explicit assumptions and preserved visibly.
- **Gating / decision-required** — Items that materially affect scope boundaries, actor model, workflow shape, data model shape, integration strategy, security/compliance posture, delivery-target feasibility, or acceptance expectations.

Use generic judgment criteria. Do not rely on domain-specific examples inside this framework rule.

Escalate unresolved items to **Gating / decision-required** when they materially change one or more of:
- actor or identity model
- core workflow shape
- data model shape
- result aggregation or export shape
- privacy, security, or compliance posture
- delivery-target feasibility
- live operational readiness

Feature-variation uncertainty should not automatically be treated as minor. If unresolved feature-shape variation would materially change authoring workflows, validation rules, schema assumptions, aggregation behavior, export structure, or live-session UX, classify it as **Gating / decision-required** rather than treating it as a harmless extension of the baseline.

For real-use delivery targets, readiness-critical unresolved items should generally be treated at least as Proceed-with-caution and often as Gating / decision-required.

## Prototype-Derived Intake Rules

### Case A — Single Prototype

If exactly one _hirmos/artifacts/sot/PROTOTYPE_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SOT.md`) exists, ingest it directly as a first-class prototype-derived input.

### Case B — Multiple Prototypes with Set

If multiple `_hirmos/artifacts/sot/PROTOTYPE*_SOT.md` files exist and _hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md`) exists:
- use _hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md`) as the primary normalized prototype-derived intake artifact
- also treat every individual `_hirmos/artifacts/sot/PROTOTYPE*_SOT.md` as a required first-class prototype input
- consult both layers

The set artifact is primary for:
- normalization
- shared signals
- conflicts
- variants
- consolidated requirement candidates

The individual prototype artifacts are required for:
- fine-grained details
- prototype-specific behavior
- traceability
- ambiguity handling
- conflict interpretation
- details compressed or omitted by normalization

### Case C — Multiple Prototypes without Set

If multiple `_hirmos/artifacts/sot/PROTOTYPE*_SOT.md` files exist and _hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md`) does not exist, this is an inconsistent state.

In that case:
- `REQUIREMENTS_SOT` generation MUST NOT proceed as if normalization were optional
- _hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md`) MUST be generated first as a prerequisite normalization step before continuing requirements generation

### Prototype Conversion Rule

Prototype-derived SoT must be converted into:
- requirements-level truth candidates
- system behaviors
- constraints
- assumptions when clearly justified
- open questions
- unresolved ambiguities when evidence is incomplete or contradictory

Prototype-derived SoT MUST NOT be treated as direct implementation truth.

## Cycle-Level Reconciliation Note

Visible `Assumptions` and `Open Questions` preserved in `REQUIREMENTS_SOT.md` remain part of the Requirements-level unresolved-item reconciliation feed. When this artifact is generated or refined during `requirements-agent:requirements`, each materially relevant unresolved item preserved here must also be contributed into this producer's own `## Producer contribution: ...` section inside the project-level canonical `/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md` artifact using the Requirements lifecycle binding at `/_hirmos/extensions/requirements-agent/specs/unresolved-item-contribution-contract.md`, which binds to the shared framework contract at `/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md`. Capturing them here does not by itself resolve them or remove the need for explicit severity classification plus documented handling before Requirements completion.

## Required Sections

The final `REQUIREMENTS_SOT.md` MUST include the following sections.

### 1. System Overview
- what the system is
- who it is for
- what problem it solves

### 2. Goals
- primary goals
- secondary goals, when relevant

### 3. Non-Goals
Explicitly define what the system will **not** do.

### 4. Actors
List all actors interacting with the system.

### 5. Core Capabilities
High-level list of what the system must support.
Each capability must be clear, atomic, and testable.

### 6. Functional Requirements
Use structured functional requirements such as:

#### FR-001: <Title>
- Description
- Actor(s)
- Preconditions
- Trigger
- Main Flow (step-by-step)
- Alternate Flows
- Edge Cases
- Expected Outcome

Rules:
- every flow must be explicit
- no “obvious behavior” allowed

### 7. User Flows
End-to-end flows across multiple requirements.

### 8. State Definitions
When applicable, define system states, allowed transitions, and invalid transitions.

### 9. Data Requirements
Define:
- required data
- optional data
- validation rules
- constraints

Do NOT define schema or database structure.

### 10. Constraints
Define:
- business constraints
- legal constraints
- system rules

### 11. Staged Delivery Targets (When Relevant)
If the project has multiple intended deliverables such as MVP, Delivery 2, Delivery 3, pilot, beta, or milestone-based rollout, preserve staged delivery as a planning-input layer.

Preserve the distinction between:
- **Declared Delivery Targets**
- **Proposed Delivery Targets (Planning Hypotheses)**

For each Delivery Target, capture:
- Name
- Included Scope
- Excluded Scope
- Notes

Additional rules:
- declared targets come from source-confirmed inputs
- proposed targets come from assistant recommendation or assistant-user collaborative reasoning
- proposed targets must remain clearly marked as proposed, not source-confirmed truth
- include this section only when staged delivery is provided, implied, or materially helpful for planning clarity
- keep this section concise and planning-oriented
- do NOT turn this section into phase planning or release planning
- do NOT define execution order or implementation sequencing here

#### Real-use delivery targets

When a declared delivery target is intended for real operational use rather than internal demonstration, planning must preserve any unresolved readiness-critical items clearly.

Readiness-critical items include, at minimum, unresolved assumptions or unknowns that materially affect:
- operational reliability
- scale/performance expectations
- degraded-mode behavior
- privacy/compliance posture
- acceptance feasibility

These items should remain visible as open questions, assumption-scoped direction, or gating items rather than being silently absorbed into settled truth.

### 12. Prototype-Derived Signals / Requirements Impact (When Relevant)
When prototype-derived SoT is used, preserve the material requirements impact of the prototypes, including:
- behaviors strongly indicated by the prototypes
- constraints implied by prototype behavior
- conflicts or variants that require requirements-level resolution
- unresolved ambiguity that affects downstream system planning

Rules:
- convert prototype-derived SoT into requirements-level meaning
- do NOT blindly restate prototype internals
- do NOT collapse normalized set-level signals and fine-grained prototype-specific details into one undifferentiated layer

### 13. Non-Functional Requirements
Include high-level requirements such as:
- performance expectations
- reliability
- availability
- scalability

### 14. Unresolved Items
This section must include both of the following subsections:

#### Assumptions
List requirement-shaping assumptions explicitly. Any materially relevant unsettled item such as poll types, export scope, segmentation scope, or identity model belongs here rather than only in narrative prose.

#### Open Questions
List unresolved requirement-shaping questions explicitly.

## Strict Rules

- MUST NOT include architecture
- MUST NOT include tech stack
- MUST NOT include implementation details
- MUST NOT reference code as implementation truth
- MUST NOT turn staged delivery targets into release planning or phase sequencing
- MUST NOT skip prototype-derived intake when relevant
- MUST NOT treat multiple-prototype-without-set as a normal state
- MUST NOT treat _hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md`) as lossless when multiple prototype-specific SoTs also exist

## Completion Criteria

The document is complete only if:
- all required sections are present
- all important flows are explicit
- ambiguity is minimized
- important edge cases are covered
- no architecture leakage remains
- requirements are testable
- system boundaries are clear
- non-goals are clearly defined
- staged delivery targets are captured when relevant
- prototype-derived intake is handled correctly when present
- if multiple prototypes exist, normalization is handled correctly and fine-grained prototype details are preserved appropriately
- unresolved items that still require explicit confirmation or requirements-level handling remain visible when relevant
- research-backed defaults are not silently flattened into confirmed requirements

## Anti-Patterns (Forbidden)

- “User can do X” without flow
- “System handles errors” without definition
- “As needed”, “if applicable”, “etc.”
- hidden assumptions
- vague terms such as fast, simple, or easy
- using _hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md`) alone as if it fully replaces all `_hirmos/artifacts/sot/PROTOTYPE*_SOT.md` detail in the multi-prototype case

## Validation Rule

If a developer could ask:

> What should happen here?

then `REQUIREMENTS_SOT.md` is incomplete.

If prototype-derived SoT exists and the requirements-agent cannot explain:
- how the normalized prototype set shaped the requirements
- how prototype-specific nuance was preserved where needed

then `REQUIREMENTS_SOT.md` is incomplete.

## Open Question Visibility

Material unresolved items captured in `REQUIREMENTS_SOT.md` must remain visible to the Requirements-level unresolved-item review. This includes both `Assumptions` and `Open Questions`. Capturing them here does not by itself resolve them, answer them, downgrade them, or remove the need for explicit severity classification plus documented handling before Requirements completion.

## Local Quality Bar

`REQUIREMENTS_SOT.md` is locally acceptable only when it is:
- complete enough to support downstream system planning
- explicit enough that important behavior is not left implicit
- structured enough that requirements can be reviewed and traced
- implementation-independent
- strong enough that downstream SoT generation does not depend on major requirement guessing

## Input Alignment Rules

`REQUIREMENTS_SOT.md` must remain aligned with its governing inputs.

This means it must:
- reflect the requirements inputs actually provided by the Orchestrator
- preserve material staged delivery context when relevant
- preserve prototype-derived requirements impact when relevant
- avoid inventing unsupported requirements
- surface ambiguity instead of silently overwriting conflicting evidence

## Failure / Repair Expectation

If local validation fails, `REQUIREMENTS_SOT.md` must be refined and revalidated before downstream system planning continues.

The cycle must not proceed on the basis of a weak or ambiguous requirements artifact.

## Local Validation Note

Within `requirements-agent:requirements`, `REQUIREMENTS_SOT.md` should be treated as one of the most load-bearing local gates. Downstream system planning should not proceed until both local quality and input alignment are strong enough to support the rest of the system-level SoT set.

## Prototype Auto-Discovery Alignment Note

When raw prototype inputs are present in `_hirmos/inputs/prototype-ingestion/prototypes/`, their discovery and preprocessing belong to the installed `prototype-ingestion` extension through its `requirements-agent:requirements` hook subscriptions, not to `requirements-agent:requirements-sot` directly.

`requirements-sot` must consume only the derived prototype SoT artifacts that result from that preprocessing, such as:
- _hirmos/artifacts/sot/PROTOTYPE_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SOT.md`)
- _hirmos/artifacts/sot/PROTOTYPE_01_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_01_SOT.md`)
- _hirmos/artifacts/sot/PROTOTYPE_02_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_02_SOT.md`)
- _hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md (`/_hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md`)

Raw prototype archives must not be used directly as requirements inputs.

## Decision Protocol for Gating Items

Before finalizing `REQUIREMENTS_SOT.md`, evaluate materially relevant unresolved items that still require explicit confirmation or requirements-level handling for severity. If any items remain Gating / decision-required, request Orchestrator direction before finalizing major artifacts.

Allowed outcomes:

- **Use assumption** — Proceed with an explicitly labeled Orchestrator-approved planning assumption. It remains assumption-scoped and must not be upgraded to source-confirmed truth.
- **Ask customer** — Pause and produce concise confirmation questions plus a short explanation of what planning remains unstable until answered.
- **Defer and constrain** — Proceed only if downstream planning is intentionally narrowed so the unresolved item does not silently expand into the design.

`REQUIREMENTS_SOT.md` may be finalized only after either no gating items remain unresolved or an Orchestrator decision has been recorded for each gating item.

## Cycle-context unresolved-item contribution obligation

When this producer is executed as part of `requirements-agent:requirements`, it must not leave its own linear workflow until every materially relevant unresolved item surfaced locally under:
- `### Assumptions`
- `### Open Questions`

has also been contributed into this producer's own `## Producer contribution: ...` section inside the project-level canonical `UNRESOLVED_ITEMS_INVENTORY.md` artifact.

Each contributed item must preserve:
- producer artifact path
- source subsection
- one contribution record per canonical unresolved item unless explicitly rejected with recorded reason

When contributing in cycle context, this producer may update only its own producer-scoped contribution section in the cycle-owned inventory structure.
It must not:
- reconcile items
- merge across producers
- classify final gating severity
- decide final handling outcomes
- update ledger outcomes on behalf of `requirements-agent:requirements`

If this producer surfaces materially relevant local unresolved items during `requirements-agent:requirements` context but does not update its producer-scoped inventory contribution truthfully before exit, local completion is invalid.

## Mandatory Self-Validation

Before finalizing, verify:
- the document is requirements-only
- ambiguity is minimized
- important flows are covered
- constraints are captured at the requirements level
- if _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`) exists, it is used correctly as normalized intake rather than treated as authoritative truth
- if _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`) exists, raw files under `_hirmos/inputs/requirements-agent/requirements/` do not automatically trigger regeneration or implicit override
- prototype-derived intake is handled correctly when present
- if staged delivery is relevant, declared and proposed targets are separated correctly
- if a declared delivery target is intended for real operational use, readiness-critical unresolved items remain visible and properly classified rather than implied away
- the result is strong enough to drive downstream architecture and implementation planning

If any issue is found, fix it before output.

## Acceptance Criteria

This entrypoint is acceptable for downstream use only when the final `REQUIREMENTS_SOT.md` preserves the original framework's local governance strength closely enough that `system-sot`, `architecture-sot`, and `phases-sot` can proceed without major requirements guessing.