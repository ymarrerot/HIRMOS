# Spec: Architecture SoT

## Purpose

Define _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) as the target architecture and major technical structure for the system.

This artifact:
- translates `SYSTEM_SOT.md` into architecture
- defines structure, components, and interactions
- establishes system design direction
- is the primary stack-aware system-design artifact when an active stack is selected

## Required inputs

- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)
- _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)
- staged delivery context when relevant
- prototype-derived planning input when relevant
- active stack context when `_hirmos/project.json` resolves to a valid stack package

## Stack consumption rule

`ARCHITECTURE_SOT.md` is a justified stack consumer.

When an active stack is resolved through core, this Spec should consume the stack surfaces that materially affect architectural direction, especially:
- `architecture_guidance`
- `engineering_standards`
- other declared stack surfaces that materially constrain structure, boundaries, scaling direction, security posture, or implementation organization

Stack consumption must strengthen architectural realism without turning `ARCHITECTURE_SOT.md` into implementation instructions.

## Output

- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)

## Core principles

1. Deterministic structure
2. Explicit responsibilities
3. No ambiguity
4. No hidden behavior
5. Aligned with `SYSTEM_SOT.md`
6. Stack-aware when stack context materially affects architecture

## Architecture Planning-Honesty Rule

`ARCHITECTURE_SOT.md` may define a coherent target architecture for planning purposes, but it must not silently erase material uncertainty inherited from incomplete requirements, assumption-driven system decisions, or stack-driven constraints that remain unsettled.

When architecture direction depends on assumptions, research-backed defaults, or stack-derived guidance rather than source-confirmed truth, that should remain visible enough to avoid false precision.

## Required sections

`ARCHITECTURE_SOT.md` must include these sections:

### 1. Architecture Overview

Define:
- high-level structure
- architecture style (if applicable)
- system organization

### 2. Component Architecture

Define all major components.

For each component, make explicit:
- name
- responsibility
- inputs
- outputs
- dependencies

### 3. Interaction Model

Define:
- how components communicate
- data flow between components
- control flow

### 4. Data Flow

Define:
- how data moves through the system
- transformations
- lifecycle

### 5. State Management

Define:
- where state lives
- how state changes
- consistency rules

### 6. Persistence Model (Conceptual)

Define:
- what is stored
- why it is stored

Do **not** define schema.

### 7. External Integrations

Define:
- external systems
- how the system interacts with them

### 8. Error Handling Strategy

Define:
- how errors are handled
- system behavior on failure

### 9. Scalability Considerations

Define:
- how the system scales conceptually
- what stack-aware scaling or deployment implications materially affect the target architecture when relevant

### 10. Security Considerations

Define:
- access control
- data protection
- major security boundaries

### 11. Constraints

Define:
- technical/system constraints derived from `SYSTEM_SOT.md`
- stack-derived architectural constraints when relevant

### 12. Unresolved Items

This section must include both of the following subsections:

#### Assumptions
Only include architecture-shaping assumptions, including stack-influenced assumptions when they materially shape architecture, such as hosting baseline, persistence baseline, deployment/privacy constraints, or residency-sensitive hosting assumptions.

#### Open Questions
Only include unresolved items that still affect architecture direction.

Step-level extraction and reconciliation are governed by [`system-design.spec.md`](./system-design.spec.md). Capturing local unresolved items here does not by itself resolve them or remove the need for explicit severity classification plus documented handling before system-design completion.

## Requirement-derived uncertainty handling

If unresolved or pending-confirmation items materially affect architecture direction, preserve those in this artifact's `Unresolved Items` section as planning assumptions or clearly assumption-scoped design choices rather than presenting them as unquestioned certainty.

## Severity-aware architecture uncertainty

When architecture direction depends on unresolved gating items without a recorded Orchestrator decision, preserve the affected architecture direction as explicitly assumption-scoped rather than settled architecture truth. If an Orchestrator-approved assumption exists, preserve it visibly as assumption-scoped direction.

## Open Question Visibility

Material unresolved items captured in `ARCHITECTURE_SOT.md` must remain visible to the step-level unresolved-item review. This includes both `Assumptions` and `Open Questions`. Capturing them here does not by itself resolve them, answer them, downgrade them, or remove the need for explicit severity classification plus documented handling before system-design completion.

## Local architecture quality bar

`ARCHITECTURE_SOT.md` is locally acceptable only when it:
- expresses a coherent structural design for the system
- is strong enough to support downstream phase planning
- clearly separates major components and responsibilities
- reflects real constraints instead of generic architecture language
- makes component responsibilities explicit
- makes interactions and data flow explicit
- makes architecture boundaries coherent
- remains deterministic enough for downstream planning
- keeps assumption-driven or stack-driven architectural choices visibly scoped when confirmation is pending

## Input alignment rules

`ARCHITECTURE_SOT.md` must stay aligned to:
- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)
- _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)
- staged delivery context when it materially affects architecture scope or sequencing
- active stack context when stack-derived guidance materially affects architecture direction

It must not:
- introduce architectural behavior that contradicts or outruns the approved system definition
- convert stack guidance into implementation-level instructions
- ignore stack-derived constraints that materially affect structural design once the active stack is selected

## Failure / repair expectation

If the architecture is vague, contradictory, under-specified, materially ahead of the approved system definition, or unrealistically generic relative to the active stack context when one is selected:
- refine the architecture artifact before downstream planning continues
- do not compensate for weak architecture quality later in phase planning

## Strict rules

- MUST align with `SYSTEM_SOT.md`
- MUST NOT introduce new behavior not supported by upstream planning artifacts
- MUST NOT contradict `REQUIREMENTS_SOT.md`
- MUST NOT silently convert assumption-driven or stack-driven direction into settled architecture truth
- MUST NOT degrade into implementation tasking or tool-specific execution instructions

## Completion criteria

`ARCHITECTURE_SOT.md` is complete only when:
- all major components are defined
- interactions are explicit
- data flow is clear
- responsibilities are unambiguous
- major system connections are not missing
- the artifact remains consistent with `SYSTEM_SOT.md`
- stack-derived architectural implications are reflected coherently when an active stack is selected

## Anti-patterns

Avoid:
- vague components
- missing interactions
- implicit data flow
- architecture that introduces features not supported by the requirements or system definition
- stack-aware architecture claims that are too thin to shape real downstream planning
- implementation-command leakage

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

## Validation rule

If someone can reasonably ask, “How does this part work?” and `ARCHITECTURE_SOT.md` does not answer it clearly enough for downstream planning, the artifact is incomplete and must be refined before continuing.

## System-design-cycle note

When used inside `system-design-agent:system-design`, this artifact must pass its own local quality gate before downstream planning continues. Local artifact quality does not replace the final system-level coherence review.