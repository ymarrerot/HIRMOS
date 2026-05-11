# Spec: Prompt Planning

## Purpose

Define the reusable method for decomposing one approved phase contract into a complete prompt plan.

This is the strategic layer between:

- the Phase SoT (contract)
- the downstream agent prompt set (execution contracts)

This Spec does not define the final agent-prompt execution contract structure. That is owned by `specs/agent-prompt.spec.md`.

## Output Location

Prompt-plan artifacts should be materialized by `implementation-agent:implementation-planning-cycle` at:

- `_hirmos/artifacts/prompts/phase-<NN>-<slug>/PROMPT_PLAN.md`

This Spec defines prompt-plan truth. The implementation-planning cycle owns the final folder and file naming convention.

## Core Principle

A phase MUST NOT be executed blindly.

It MUST be decomposed into execution units that are:

- logically isolated
- independently testable
- reviewable
- failure-contained

## Goal

Produce a prompt plan that:

- covers 100% of the relevant phase scope
- minimizes execution failure risk
- enables precise review and debugging
- makes sequencing and dependencies explicit
- preserves delivery-boundary constraints when relevant

## Governing files

Read before generation or refinement:
- [_hirmos/extensions/implementation-agent/specs/ENGINEERING_STANDARDS.md](./ENGINEERING_STANDARDS.md) when implementation-wide engineering discipline materially affects decomposition, verification, or failure containment
- [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md) when normalized presentation artifacts exist or may affect decomposition, sequencing, or deliverables
- _hirmos/artifacts/sot/PRESENTATION_SOT.md (`/_hirmos/artifacts/sot/PRESENTATION_SOT.md`) when it exists and materially affects decomposition or deliverables

## Required Inputs

`implementation-agent:prompt-planning` should be derived from the strongest available implementation-planning-cycle inputs, including:

- the current phase contract under `_hirmos/artifacts/phases/`
- relevant _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)
- relevant _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)
- _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- [_hirmos/extensions/implementation-agent/specs/ENGINEERING_STANDARDS.md](./ENGINEERING_STANDARDS.md) when engineering discipline materially affects decomposition, sequencing, reviewability, or delivery boundaries
- active stack `architecture_guidance` and `engineering_standards` surfaces when they materially affect decomposition, sequencing, or delivery boundaries
- [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md) when normalized presentation artifacts exist or may affect decomposition, sequencing, or deliverables
- staged delivery context when relevant
- _hirmos/artifacts/sot/PRESENTATION_SOT.md (`/_hirmos/artifacts/sot/PRESENTATION_SOT.md`) when normalized presentation constraints materially affect decomposition, shared UI foundation work, UX flow sequencing, asset usage, or template adaptation
- the current approved implementation scope

## Delivery Boundary Detection

Before decomposition, determine whether the applicable phase contract or `PHASES_SOT.md` defines a Delivery Boundary.

If a Delivery Boundary exists, extract at minimum:

- Current Delivery Target
- Included Scope
- Excluded Scope
- Delivery Packaging Constraint
- notes on future scope

## When Multiple Prompts Are Mandatory

Split the phase into multiple prompts if ANY of the following is true:

1. multiple independent workflows exist
2. multiple subsystems or components are introduced
3. the phase introduces both infrastructure and business logic
4. the required tests are large in number or diverse in type
5. observability requirements are complex
6. failure in one part should not block the entire phase
7. the implementation touches many unrelated files
8. the phase contains ingestion + processing + output as a pipeline
9. the phase introduces persistence + APIs + workflows together

## When a Single Prompt Is Allowed

A single prompt is allowed only when ALL are true:

- single responsibility
- limited scope
- small number of files
- simple workflows
- minimal observability surface
- minimal testing surface

## Decomposition Strategy

Choose intentionally among:

### 1. Vertical Slice (preferred)
Use end-to-end functionality per slice.

### 2. Layer-Based (secondary)
Split by system layer, such as infrastructure, domain logic, or interfaces.

### 3. Capability-Based
Assign one implementation capability per prompt.

## Prompt Plan Output (strict)

A prompt plan MUST include all of the following:

### 1. Phase Reference
- phase name
- phase number

### 2. Coverage Strategy
Explain:
- how the prompt set collectively covers the phase
- why the chosen decomposition strategy was selected

### 3. Prompt Sequence
For EACH prompt include:
- Prompt ID
- Prompt Title
- Purpose
- Scope
- Dependencies
- Key Deliverables
- Risk Level (optional but recommended)

Prompt ID format:
- `P<phase>-<index>`
- examples: `P1-001`, `P1-002`

### 4. Coverage Mapping (critical)
Map every relevant phase requirement or responsibility to one prompt.

If you cannot answer:

> Which prompt implements this requirement?

then the plan is INVALID.

### 5. Execution Order
Define the exact execution sequence.

### 6. Parallelism
State whether any prompts can run in parallel.
Default: sequential.

### 7. Failure Containment Strategy
Explain:
- how failures are isolated
- how retries are handled

### 8. Validation Strategy
Explain:
- how prompt-level review ensures local correctness
- how phase-level review ensures full coverage and coherence

## Delivery Boundary Constraints

When a Delivery Boundary exists, prompt planning MUST ensure:

- prompts stay inside the Current Delivery Target
- Included Scope required for the current delivery is fully covered by the prompt set
- Excluded Scope is not silently implemented
- the prompt set preserves the Delivery Packaging Constraint for the current delivery

Future scope may be acknowledged for sequencing or architectural context, but it must not contaminate current-delivery decomposition.

A prompt plan is INVALID if any of the following is true when Delivery Boundary exists:

- Included Scope is not fully covered by the prompt set
- Excluded Scope is included in current-delivery prompts without explicit governed approval
- current-delivery prompts depend on excluded future scope for functional completeness

## Additional Validation Rule for Delivery Boundary

When a Delivery Boundary exists, the prompt plan must be reviewed twice:

- once for normal phase-scope coverage and decomposition quality
- once for current-delivery containment against Included Scope, Excluded Scope, and the Delivery Packaging Constraint

A prompt plan that is internally coherent but violates the current delivery boundary is still invalid.

## Strict Rules

The prompt plan MUST:

- cover 100% of the relevant phase scope
- avoid overlapping responsibilities
- avoid coverage gaps
- ensure each prompt is independently reviewable
- preserve staged delivery boundaries when relevant
- remain aligned with governing system and architecture constraints
- preserve implementation-relevant consequences from normalized presentation artifacts when they exist, according to [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md)
- avoid inventing implementation scope not supported by governing artifacts

## Anti-Patterns (forbidden)

- a giant “do everything” prompt when decomposition is required
- unclear prompt boundaries
- overlapping scopes
- missing coverage mapping
- hidden-state dependencies between prompts
- current-delivery prompts contaminated by excluded future scope

## Local Prompt-Plan Quality Bar

A prompt plan is locally acceptable only when it:

- covers 100% of the relevant Phase SoT scope
- decomposes work into bounded, reviewable execution units
- defines sequencing and dependencies clearly enough for implementation planning
- provides meaningful failure containment
- preserves delivery boundaries when relevant
- avoids major unstated assumptions about prompt boundaries or execution order

## Input Alignment Rules

A prompt plan must remain aligned with its governing inputs.

This means it must:

- preserve the approved phase contract accurately
- remain consistent with relevant system and architecture constraints
- preserve prompt-planning consequences from normalized presentation artifacts when they affect prompt boundaries, sequencing, or deliverables, according to [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md)
- preserve staged delivery boundaries when relevant
- avoid inventing implementation scope not supported by governing artifacts

## Failure / Repair Expectation

If local validation fails, the prompt plan must be refined and revalidated before downstream agent-prompt generation is treated as acceptable.

## Implementation Planning Cycle Note

This Spec may be orchestrated by `implementation-agent:implementation-planning-cycle`.

When used inside that cycle:

- prompt-planning may run across the full planned phase scope at the current framework maturity level
- prompt quality includes sizing and scope discipline, not only coverage
- local prompt-plan validation does not replace full prompt-set coherence review

## Completion Criteria

A prompt plan is complete only when:

- the decomposition strategy is intentionally chosen and justified
- every relevant phase responsibility is mapped to prompt coverage
- sequencing, dependencies, and parallelism rules are explicit
- failure containment and validation strategy are explicit
- delivery-boundary compliance is preserved when relevant

## Validation Rule

If you cannot answer:

> Which prompt implements this requirement?

or if coverage, scope boundaries, or delivery-boundary compliance are unclear, the prompt plan is INVALID.

## Mandatory Self-Validation

Before returning the result, verify all of the following:

- every relevant phase responsibility is covered
- there are no overlaps between prompt scopes
- there are no obvious coverage gaps
- sequencing and dependencies are explicit
- decomposition is reviewable and failure-contained
- delivery-boundary rules are preserved when relevant
- no unsupported implementation scope was introduced

If any check fails, refine the prompt plan before returning it.

## Output Discipline

Return ONLY the final Prompt Plan.