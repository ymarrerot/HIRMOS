# Spec: Phases SoT

## Purpose

Define _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`) as the complete roadmap-aware phase strategy for how the system is built over time.

This artifact:
- translates _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`) and _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) into execution stages
- enforces strict scope boundaries
- enables deterministic downstream implementation planning
- must be strong enough to support downstream `phase-sot` contract generation
- uses staged delivery awareness to design a stronger roadmap-aware phase structure when relevant

## Output

- _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)

## Core Principles

1. Strict phase isolation
2. No scope overlap
3. No implicit work
4. Deterministic execution
5. Progressive system construction
6. Roadmap-aware phase design when staged delivery is relevant
7. Downstream phase-contract readiness

## Roadmap Classification Rule

`PHASES_SOT.md` must preserve the distinction between:
- declared delivery targets
- proposed delivery targets

It must also avoid pretending that assumption-heavy roadmap boundaries are fully settled when important confirmation items remain open.

## Roadmap Effects of Gating Items

If unresolved gating items materially affect phase boundaries, roadmap grouping, or delivery-target feasibility, `PHASES_SOT.md` must preserve that uncertainty explicitly. It must not make the roadmap look more settled than the planning inputs support. If the Orchestrator has approved a temporary assumption, preserve that assumption visibly rather than presenting the roadmap decision as source-confirmed.

## Stack influence rule

`PHASES_SOT.md` is primarily stack-indirect.

When the active stack materially affects architecture direction, that influence should normally arrive through the updated upstream `ARCHITECTURE_SOT.md` rather than through direct stack-specific roadmap reasoning inside this Spec.

## Required Inputs

`PHASES_SOT.md` should be derived from the strongest available upstream planning inputs, including:

- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)
- _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)
- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)
- _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`) when relevant
- pending confirmation items when they materially affect roadmap structure

## Input Alignment Rules

`PHASES_SOT.md` must stay aligned to:
- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)
- _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)
- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)
- declared and proposed delivery targets when relevant

It must not create phase structure that contradicts approved requirements, system scope, or architecture direction.

It must not invent unsupported responsibilities, sequencing logic, or roadmap boundaries.

## Local Phase-Roadmap Quality Bar

`PHASES_SOT.md` is locally acceptable only when:
- the roadmap is complete enough for downstream `phase-sot` contract generation
- phase boundaries are explicit and non-overlapping
- sequencing logic is coherent
- staged delivery is handled truthfully when relevant
- no major roadmap ambiguity remains hidden inside phase definitions
- the phase strategy is clear enough to derive the full downstream phase set

## Failure / Repair Expectation

If the roadmap is incomplete, overlapping, weakly sequenced, or materially misaligned with staged delivery or upstream SoTs:
- refine `PHASES_SOT.md` before downstream `phase-sot` generation proceeds
- do not rely on downstream phase artifacts to repair a weak roadmap definition

## Required Structure

The document must define all of the following sections.

### 1. Phase Model Overview

Define:
- total number of phases
- phase philosophy
- ordering logic
- why the system is partitioned this way

### 2. Global Phase Rules

Define rules that apply to all phases, including:
- no cross-phase implementation
- no scope leakage
- no skipping phases
- no implicit dependencies

### 3. Staged Delivery Targets (When Relevant)

If the project has multiple intended deliverables such as an MVP, pilot, internal beta, Delivery 2, Delivery 3, or other staged roadmap targets, `PHASES_SOT.md` must include a dedicated Staged Delivery Targets section.

That section must define each declared Delivery Target using this structure:
- Delivery Target Name
- Included Scope
- Excluded Scope
- Notes

You may include an Intended First Delivery hint when it is explicitly provided and materially useful for planning clarity.

#### Staged Delivery Target Rules

- all declared Delivery Targets must be preserved when relevant
- all declared Delivery Targets must be used to strengthen roadmap-aware phase design when relevant
- multiple Delivery Targets must not be collapsed without justification
- `PHASES_SOT.md` must remain phase-design-cycle focused and must not become release execution control
- the phase structure should support the full known staged-delivery roadmap cleanly, not only the earliest deliverable
- declared and proposed targets must remain distinct

If staged delivery is not relevant, omit the section rather than inventing one.

#### Readiness-critical roadmap honesty

If an early delivery target is intended for real use rather than internal demonstration, the phase structure must preserve readiness-critical unresolved items clearly enough to avoid false confidence in roadmap feasibility.

The roadmap should make visible where readiness-critical work must occur before the target can be treated as operationally usable.

Readiness-critical work may include validation or hardening related to:
- operational reliability
- scale/performance
- degraded-mode behavior
- privacy/compliance posture
- acceptance feasibility

### 4. Phase Definitions

Phase definitions must remain implementation-ready and non-overlapping.

#### `## PHASE X — <Name>`

##### Purpose
Short statement of what the phase achieves.

##### Scope
Concrete work included in the phase.

##### Out of Scope
Important exclusions that prevent scope drift.

##### Inputs
Artifacts or decisions required before the phase begins.

##### Outputs
Artifacts or implemented outcomes expected from the phase.

##### Tasks
Ordered or grouped work items that make the phase executable.

##### Constraints
Important limits, dependencies, or sequencing boundaries.

### 5. Unresolved Items
This section must include both of the following subsections:

#### Assumptions
Roadmap-shaping assumptions that materially affect sequencing, stabilization, or scope partitioning belong here.

#### Open Questions
Roadmap-shaping open questions that materially affect sequencing, stabilization, or scope partitioning belong here.

## Completion Criteria
Define strict checklist-style conditions required to mark the phase complete.

##### Cycle-context unresolved-item contribution obligation

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

## Validation Rules
Define how to verify correctness, completeness, and alignment with SoTs.

## Phase Design Rules

### 1. No Overlap
A responsibility must exist in only one phase.
If duplicated, the design is invalid.

### 2. No Hidden Dependencies
All dependencies must be explicit.

### 3. No Partial Responsibilities
Do not split responsibilities across phases unless explicitly defined and justified.

### 4. Progressive Complexity
Phases must build simple to complex.

## Upstream Open Question Handling

Phase planning should inherit only upstream open questions that have already passed through the step-level unresolved-item handling model with explicit severity classification and documented handling. Unreconciled upstream open questions should not be silently carried into finalized phase contracts, and downstream artifacts must preserve any assumption-based or constrained handling visibly where still material.

## Completion Criteria

`PHASES_SOT.md` is only complete when:
- the full roadmap is partitioned into explicit non-overlapping phases
- all major responsibilities are covered
- each phase has explicit scope, out-of-scope, inputs, outputs, tasks, constraints, completion criteria, and validation rules
- staged delivery is preserved and handled truthfully when relevant
- roadmap uncertainty that still depends on confirmation is surfaced honestly
- the document is strong enough to support downstream `phase-sot` generation without relying on those downstream artifacts to repair missing roadmap logic

## Anti-Patterns

Avoid all of the following:
- overlapping phase scope
- duplicated responsibilities across phases
- hidden dependencies
- implicit outputs
- phase decomposition optimized only for the earliest deliverable when broader staged delivery is known
- collapsing declared and proposed delivery targets together
- turning phase planning into release execution planning
- inventing unsupported roadmap structure

## Validation Rule

Before finalizing, verify that `PHASES_SOT.md`:
- reflects the established requirements, system, and architecture accurately
- defines a phase strategy clear enough to derive the full phase set
- avoids overlapping or ambiguous phase responsibilities
- is strong enough to support downstream `phase-sot` generation
- remains roadmap-aware when staged delivery targets are relevant
- preserves all declared delivery targets when relevant
- supports the full known staged-delivery roadmap coherently
- does not falsely present confirmation-dependent roadmap boundaries as fully settled

If any issue remains, refine the artifact before final output.

## Output Discipline

Return only final `PHASES_SOT.md` content.