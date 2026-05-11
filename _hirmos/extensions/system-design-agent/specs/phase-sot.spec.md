# Spec: Phase SoT

## Purpose

Define the COMPLETE, ENFORCEABLE contract for a single development phase.

This Spec translates _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`) into an actionable phase-level implementation contract that is strong enough to support:

- execution planning
- prompt generation
- agent execution
- objective validation

A Phase SoT is the strictest contract in the design family for one phase.

## Output Location

`_hirmos/artifacts/phases/phase_<N>_<slug>_SOT.md`

## Core Principle

A Phase SoT is not general documentation.

It is a contract.

If the system does not match the Phase SoT, the phase has failed.

## Required Inputs

- _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`) (REQUIRED)
- _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`) (REQUIRED)
- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) (REQUIRED)
- target phase selection (REQUIRED)

## Input Alignment Rules

You must:

- locate the target phase in _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- preserve its intended scope, sequence position, dependencies, and unlocked outcomes
- map relevant system responsibilities from _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`) into this phase only
- map relevant architecture responsibilities from _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) into this phase only
- resolve ambiguity by tightening the contract, not by hand-waving or leaving implementation-critical gaps
- preserve strict phase boundaries and avoid future-phase leakage

You must not:

- contradict _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`), _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`), or _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)
- redefine the overall roadmap
- skip phase-specific details because they feel repetitive or obvious
- assume a phase is acceptable without explicit workflows, observability, tests, and exit criteria

## Operational readiness expectations

When a phase contributes directly to a real-use delivery target, the phase contract should preserve any readiness-critical expectations relevant to that phase clearly enough to be testable and enforceable.

These may include expectations around:
- reliability
- timing/performance
- degraded-mode behavior
- privacy/compliance controls
- acceptance evidence

If these expectations remain assumption-scoped or unresolved, the phase contract must keep that visible rather than presenting them as fully settled source-confirmed truth.

## Required Properties

Every Phase SoT must be:

- deterministic
- complete
- testable
- enforceable
- unambiguous
- self-sufficient enough to onboard a new LLM without hidden context

## Required Sections (STRICT — ALL MANDATORY)

### 1. Phase Definition

Must include:

- phase number
- phase name
- position in sequence
- short description

### 2. Phase Objective

Must answer:

- what problem this phase solves
- why this phase exists
- what becomes possible after completion

### 3. Business Outcome

Define the real-world outcome this phase creates.

### 4. Capabilities Delivered

List only capabilities introduced in this phase.

Rules:

- they must not already exist before this phase
- they must be testable
- they must map back to _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)

### 5. Scope (STRICT)

Define everything included in this phase.

It must be explicit, exhaustive, and unambiguous.

### 6. Out of Scope (CRITICAL)

Define everything excluded from this phase.

Purpose:

- prevent drift
- enforce phase boundaries

### 7. Required System Components

List all components that must exist by the end of this phase.

For each component include:

- name
- responsibility
- inputs
- outputs

This must align with _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`).

### 8. Required Data / Entities

Define all required data for this phase.

For each include:

- purpose
- key attributes
- lifecycle

### 9. Required Integrations

Define all integrations required in this phase.

Include:

- external systems
- internal adapters
- mocks if required by phase scope

For each include:

- direction (inbound/outbound)
- expectations such as reliability and timing

### 10. Required Workflows / Scenarios (CRITICAL)

Define real workflows step by step.

Each workflow must include:

- trigger
- numbered steps
- expected outputs
- failure paths
- edge cases

If a workflow is not defined, it is not implemented.

### 11. Architecture Additions

Define what new architecture is introduced in this phase.

Include:

- components
- layers
- boundaries
- interactions

Must align with _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`).

### 12. Observability Requirements (MANDATORY)

Define required:

- logs
- metrics
- alerts
- traceability / replay / debugging support

If the phase cannot be observed, it is not complete.

### 13. Required Tests & Verification Artifacts (NON-NEGOTIABLE)

You must define:

- unit tests
- integration tests
- scenario tests
- fixtures / test data
- verification commands
- evidence artifacts such as logs, outputs, and reports

If tests are missing, the phase is failed.

### 14. Dependencies

Define:

- previous phases
- required SoTs
- external prerequisites

### 15. Allowed Work

Provide an explicit list of what can be implemented in this phase.

### 16. Not Allowed Work (CRITICAL)

Provide an explicit list of what must not be implemented in this phase.

This enforces the phase boundary.

### 17. Exit Criteria (STRICT — BINARY)

Define completion conditions that are measurable and testable.

No interpretation should be required.

### 18. Verification Checklist (FINAL GATE)

Provide a post-implementation checklist covering:

- code validation
- workflow validation
- architecture validation
- test validation
- observability validation

If any item fails, the phase is not complete.

### 19. Next Phase Unlocked

Define what becomes possible only after this phase completes.

### 20. Phase Boundary Block (COPY-READY)

Must include:

- phase name
- allowed work
- not allowed work
- exit criteria

## Completion Criteria

A Phase SoT is complete only when:

- all mandatory sections exist
- scope and out-of-scope are explicit and non-overlapping
- workflows are concrete and implementation-relevant
- observability is explicit
- tests and verification artifacts are explicit
- allowed work and not allowed work are both enforceable
- exit criteria are binary and testable
- the phase can onboard a new LLM without hidden assumptions
- the result is strong enough to support downstream implementation planning and execution

## Anti-Patterns

Do not:

- omit sections because they seem implied
- leave workflows vague or under-specified
- omit failure paths or edge cases
- omit observability because it will be added later
- omit tests because implementation details are not written yet
- allow future-phase work to leak into the current phase
- define boundaries that cannot be objectively enforced
- contradict upstream SoTs

## Validation Rule

If any required section is incomplete, any workflow is vague, any tests are missing, scope is unclear, or the phase boundary is porous, the output is invalid and must be fixed before completion.

## Local Quality Bar

This Phase SoT passes its local quality bar only when it is:

- contract-grade rather than descriptive
- fully bounded
- operationally testable
- observability-complete
- strong enough to drive downstream execution without relying on hidden context

## Failure / Repair Expectation

If self-validation finds missing sections, vague definitions, missing workflows, missing tests, contradictions, or boundary leakage, revise the Phase SoT before returning it.

## Mandatory Self-Validation

Before returning the final Phase SoT, verify all of the following:

- no missing required sections
- no vague definitions
- no missing workflows
- no missing tests
- no missing observability requirements
- no contradictions with _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`), _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`), or _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)
- no future-phase leakage
- allowed work and not allowed work are explicit and enforceable
- exit criteria are binary and measurable

If any issue is found, fix it before output.

## Output Discipline

Return only final `phase_<N>_<slug>_SOT.md` content.
No extra commentary.