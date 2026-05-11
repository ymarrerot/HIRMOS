# Spec: System SoT

## Purpose

Define _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`) as the authoritative system definition at a structural level.

This artifact:
- translates `REQUIREMENTS_SOT.md` into system definition
- defines system boundaries and responsibilities
- introduces system components at a conceptual level

This is **not** architecture.

## Output Location

_hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)

## Core Principles

1. No ambiguity.
2. No implementation details.
3. No tech stack.
4. No mixing with architecture.
5. Must map 1:1 to `REQUIREMENTS_SOT.md`.

## Stack-neutrality rule

`SYSTEM_SOT.md` is stack-neutral.

Even when an active stack is selected, this artifact must not absorb stack-specific architectural or implementation reasoning. If stack selection materially affects structural design, that influence belongs in `ARCHITECTURE_SOT.md`, not here.

## Planning-Honesty Rule

`SYSTEM_SOT.md` should present the system as a coherent planned system definition, but it must not silently erase material uncertainty inherited from incomplete source inputs.

When important system-shaping choices are still assumption-driven, research-backed, or pending confirmation rather than source-confirmed, preserve that design truth clearly enough for downstream design work, implementation preparation, and review.

## Required Inputs

Use the strongest available system-design inputs, including:
- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)
- staged delivery context when relevant
- prototype-derived requirements impact when relevant
- other project planning inputs that materially define what the system is

`REQUIREMENTS_SOT.md` is the required governing artifact.

## Required Sections

The final `SYSTEM_SOT.md` must include all sections below.

### 1. System Definition
- what the system is
- system type
- core purpose

### 2. System Boundaries
Define clearly:
- what is inside the system
- what is outside the system

### 3. Actors (Mapped)
From `REQUIREMENTS_SOT.md`:
- list all actors
- define their role relative to the system

### 4. System Responsibilities
Define what the system is responsible for:
- must directly map to core capabilities
- must be grouped logically

### 5. System Capabilities (Mapped)
Each capability must:
- map to `REQUIREMENTS_SOT.md`
- be expressed in system-level terms
- not describe UI or implementation

### 6. System Components (Conceptual)
Define logical components such as input handling, processing, state management, and output delivery.

Rules:
- conceptual only
- no implementation detail
- no tech stack

### 7. Data Domains
Define high-level data domains.

Do **not** define schema.

### 8. System States (If Applicable)
Define:
- global system states
- transitions
- constraints

### 9. External Interfaces
Define:
- interactions with external actors or systems
- what enters the system
- what leaves the system

No API details.

### 10. Constraints (System-Level)
Translate requirements constraints into system constraints.

### 11. Unresolved Items
This section must include both of the following subsections:

#### Assumptions
List explicit assumptions that materially affect system design, such as simultaneous-session expectations, degraded venue connectivity behavior, participant-flow privacy constraints, or other system-shaping operational assumptions.

#### Open Questions
List unresolved system-shaping questions explicitly.

Step-level extraction and reconciliation are governed by [`system-design.spec.md`](./system-design.spec.md). Capturing local unresolved items here does not by itself resolve them or remove the need for explicit severity classification plus documented handling before system-design completion.

## Pending Confirmation Propagation

If `REQUIREMENTS_SOT.md` contains Pending Confirmation Items that materially affect system behavior, workflow shape, actor model, or scope boundaries, `SYSTEM_SOT.md` should preserve that uncertainty in its `Unresolved Items` section rather than presenting the affected areas as fully settled.

This does not require repeating the full pending-confirmation section, but it does require avoiding false finality.

## Severity-Aware Uncertainty Propagation

If upstream Pending Confirmation Items were classified as Gating / decision-required and no Orchestrator decision has been recorded, `SYSTEM_SOT.md` must preserve the affected system shape as explicitly unsettled. It must not present that area as fully settled source-confirmed truth.

If an Orchestrator-approved assumption exists, preserve it as assumption-scoped system truth, not source-confirmed truth.

## Real-Use Readiness Propagation

If a declared delivery target is intended for real operational use, `SYSTEM_SOT.md` must preserve the system-level consequences of any readiness-critical unresolved items.

These may include unresolved expectations around:
- operational reliability
- scale/performance
- degraded-mode behavior
- privacy/compliance posture
- acceptance feasibility

The system definition must not present these areas as fully settled if the planning inputs do not support that conclusion.

If an Orchestrator-approved assumption exists, preserve it visibly as assumption-scoped system direction.

## Strict Rules

- MUST NOT include architecture
- MUST NOT include tech stack
- MUST NOT include APIs
- MUST NOT include database design
- MUST NOT present major assumption-driven system choices as fully settled truth when they still require confirmation

## Mapping Rule (Critical)

Every section must trace back to `REQUIREMENTS_SOT.md`.

If something exists here but not in requirements:
→ it is INVALID.

## Completion Criteria

`SYSTEM_SOT.md` is complete only if:
- all sections are present
- system boundaries are explicit
- all capabilities map to requirements
- no ambiguity exists
- no architecture leakage exists
- responsibilities are clear
- system components are logically defined

## Anti-Patterns (Forbidden)

- describing implementation
- introducing new features
- mixing UI with system logic
- vague responsibilities
- undefined system boundaries

## Validation Rule

If someone asks:

> “Where does this belong?”

then `SYSTEM_SOT.md` is incomplete.

## System Design Note

This Spec may be orchestrated by `system-design-agent:system-design`.

When used inside that cycle:
- this artifact must pass its own local quality gate before downstream planning continues
- local artifact quality does not replace final system-level coherence review across the full system-level SoT set

## Local Quality Bar

`SYSTEM_SOT.md` is locally acceptable only when it:
- clearly defines what the system is
- defines the system boundary clearly
- identifies the major actors and system responsibilities
- is strong enough to support downstream architecture and phase planning
- does not depend on major unstated assumptions

## Input Alignment Rules

`SYSTEM_SOT.md` must remain aligned with its governing inputs.

This means it must:
- reflect the requirements-level system definition accurately
- preserve material scope boundaries
- avoid inventing capabilities not supported by `REQUIREMENTS_SOT.md`
- avoid dropping important constraints that affect the system definition

## Failure / Repair Expectation

If local validation fails, `SYSTEM_SOT.md` must be refined and revalidated before downstream planning continues.

## Cycle-context unresolved-item contribution obligation

When this producer is executed as part of `system-design`, it must not leave its own linear workflow until every materially relevant unresolved item surfaced locally under:
- `### Assumptions`
- `### Open Questions`

has also been contributed into this producer's own `## Producer contribution: ...` section inside the project-level canonical `UNRESOLVED_ITEMS_INVENTORY.md` artifact.

Each contributed item must preserve:
- producer artifact path
- source subsection
- one contribution record per canonical unresolved item unless explicitly rejected with recorded reason

When contributing in cycle context, this producer may update only its own producer-scoped contribution section in the project-level canonical inventory structure.
It must not:
- reconcile items
- merge across producers
- classify final gating severity
- decide final handling outcomes
- update ledger outcomes on behalf of `system-design`

If this producer surfaces materially relevant local unresolved items during `system-design` context but does not update its producer-scoped inventory contribution truthfully before exit, local completion is invalid.

## Mandatory Self-Validation

Before finalizing, verify:
- all requirements are represented
- no new behavior is introduced
- no ambiguity remains
- no architecture leakage exists
- material assumption-driven system choices are not falsely presented as fully settled
- pending confirmation items are reflected appropriately when relevant
- system boundaries are explicit
- responsibilities are clear
- system components are conceptual rather than implementation-specific
- the artifact is strong enough to support downstream architecture and phase planning

- when running inside `system-design`, every canonical local unresolved item has a matching producer-scoped inventory contribution record or explicit rejection reason

If any issue is found:
→ fix it before output.

## Output Discipline

Return only final `SYSTEM_SOT.md` content.

No explanations.