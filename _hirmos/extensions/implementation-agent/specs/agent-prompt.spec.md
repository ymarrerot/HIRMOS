# Spec: Agent Prompt

## Purpose

Define the reusable method for generating one COMPLETE approved execution prompt for an implementation execution consumer.

This is the bridge between:

- the Phase SoT (what must be built)
- the downstream execution contract (how a coding/execution consumer should behave)
- the actual implementation (code + artifacts)

This Spec assumes that prompt decomposition, sequencing, and coverage strategy have already been decided by `implementation-agent:prompt-planning`.

## Output Location

`_hirmos/artifacts/prompts/phase-<NN>-<slug>/P<phase>-<index>-<slug>.md`

## Execution Baseline Assumption

Generated Agent Prompts assume a downstream execution consumer that honors the prompt contract plus the active stack context resolved through `_hirmos/project.json` and the selected stack package surfaces. When a dedicated implementation-agent or other execution layer is installed, it may apply additional execution rules on top of this prompt contract.

## Core Principle

An Agent Prompt is NOT a task.

It is an EXECUTION CONTRACT.

It must:

- constrain behavior
- enforce phase boundaries
- define expected outputs
- guarantee verifiability

## Mandatory Alignment

Every Agent Prompt MUST align with:

- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)
- _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)
- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)
- _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- the relevant phase-specific SoT under `_hirmos/artifacts/phases/*`
- _hirmos/artifacts/sot/PRESENTATION_SOT.md (`/_hirmos/artifacts/sot/PRESENTATION_SOT.md`) when normalized presentation constraints materially affect implementation behavior, UI expectations, UX flow, asset usage, or template adaptation

## Governing files

Read before generation or refinement:
- [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md) when normalized presentation artifacts exist or may affect implementation shape
- _hirmos/artifacts/sot/PRESENTATION_SOT.md (`/_hirmos/artifacts/sot/PRESENTATION_SOT.md`) when it exists and materially affects implementation shape

## Required Inputs

`implementation-agent:agent-prompt` should be derived from the strongest available implementation-planning-cycle inputs, including:

- the relevant phase contract under `_hirmos/artifacts/phases/`
- the approved Prompt Plan when present
- the current target task description when one exists
- relevant _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)
- relevant _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)
- _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- [_hirmos/extensions/implementation-agent/specs/ENGINEERING_STANDARDS.md](./ENGINEERING_STANDARDS.md)
- [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md) when normalized presentation artifacts exist or may affect implementation shape
- active stack `engineering_standards`
- active stack `commands`
- active stack `architecture_guidance` when it materially affects implementation shape
- presentation-specific support context when it materially clarifies normalized presentation constraints without becoming a parallel design-truth surface

## Prompt Structure (STRICT)

An Agent Prompt MUST include all of the following:

### 1. Prompt Header

Format:

`PROMPT <ID> — <TITLE>`

Example:

`PROMPT P1-001 — Implement ingestion pipeline`

### 2. Context

Provide ONLY relevant context, including:

- current phase
- relevant components
- required behavior

Do NOT dump entire SoTs.

### 3. Objective

Define:

- exact task to perform
- expected outcome

Must be:

- specific
- measurable
- testable

### 4. Scope Definition (CRITICAL)

#### In Scope

Explicit list of:

- files
- components
- behaviors

#### Out of Scope

Explicit list of:

- forbidden changes
- unrelated areas
- future phase work

Must align with the approved prompt and phase contract.

### 5. Implementation Requirements

Define:

- components to build or modify
- interfaces and contracts
- data-flow expectations

Must align with _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) and preserve the implementation consequences of normalized presentation constraints when they materially affect implementation shape, according to [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md).

### 6. Constraints (STRICT)

Define:

- forbidden patterns
- forbidden shortcuts
- required standards

Must align with:

- [_hirmos/extensions/implementation-agent/specs/ENGINEERING_STANDARDS.md](./ENGINEERING_STANDARDS.md)
- active stack `engineering_standards` when present
- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)

### 7. Observability Requirements

Define REQUIRED:

- logs
- metrics
- traceability expectations

If not present, the prompt is incomplete.

### 8. Tests & Verification

Define:

- unit tests
- integration tests
- scenario tests

Must include:

- exact commands to run when relevant
- expected results

When a repository-local command baseline exists, it wins. Otherwise use the active stack `commands` surface or an explicitly accepted temporary command baseline

### 9. Deliverables

Define EXACT outputs, such as:

- files created or modified
- artifacts
- logs
- reports

### 10. Prompt-Level Task Summary Extensions (CRITICAL)

This section EXTENDS:

the downstream execution consumer's base task-summary output contract when one exists

Do NOT repeat base items.

ONLY add task-specific required outputs.

Purpose:

- enable automatic LLM review
- support deeper validation
- force structured outputs

Examples:

- data validation report
- API contract verification
- workflow execution trace
- performance metrics snapshot
- schema diff summary

Rules:

- must be structured
- must be deterministic
- must be verifiable

### 11. Acceptance Criteria (BINARY)

Define:

- success conditions
- failure conditions

Must be:

- measurable
- testable
- unambiguous

### 12. Execution Notes

Optional:

- hints
- clarifications
- edge-case reminders

## Prompt Decomposition Awareness (CRITICAL)

Before generating an Agent Prompt, determine whether this prompt belongs to a Prompt Plan.

### If YES (multi-prompt phase)

The Agent Prompt MUST:

- reference its Prompt ID (for example `P1-001`)
- clearly state its position in the sequence
- explicitly reference the Prompt Plan scope assigned to it
- respect dependencies
- limit scope strictly to its assigned portion
- NOT attempt to implement the full phase

### If NO (single-prompt phase)

Proceed normally.

### Decomposition Rules

The Agent Prompt MUST NOT:

- merge multiple prompt scopes
- implement future prompts
- assume missing components from future prompts

### Coverage Awareness

Each prompt MUST:

- explicitly state what part of the phase it covers
- explicitly state what it does not cover when later prompts are expected

### Failure Isolation

When a Prompt Plan exists, each Agent Prompt should preserve the failure-containment strategy of that plan.

This means the prompt should avoid hidden dependencies that make one prompt failure silently invalidate unrelated prompt execution. Where relevant, retry assumptions, fallback notes, or sequence-sensitive caveats should be made explicit rather than left implicit.

### Prompt ID Requirement

When the phase is decomposed into multiple prompts, the Agent Prompt MUST carry the approved Prompt ID exactly as assigned by the Prompt Plan.

Prompt IDs are part of bounded execution discipline and reviewability. Do not invent or silently renumber prompt IDs at the Agent Prompt layer.

## Review Chain Awareness (CRITICAL)

An Agent Prompt must be review-ready, not just execution-ready.

### Prompt Review Requirements

The prompt must support bounded downstream review by making all of the following easy to verify:

- what exact scope this prompt owns
- what governing artifacts constrain it
- what files/components/behaviors are in scope
- what tests and verification commands prove success
- what outputs and acceptance criteria are required

### Phase Review Awareness

When a Prompt Plan exists, the Agent Prompt should make its role in the larger phase implementation legible enough that a later phase-level review can confirm:

- prompt-plan alignment
- full coverage of the approved phase scope
- no duplicated or missing implementation responsibility

### Retry Compatibility

The prompt should be written so that a retry or regeneration can preserve the same bounded scope, deliverables, tests, and acceptance criteria without redefining the task.

## Phase Coverage Support

### Phase Coverage for this Prompt

Each Agent Prompt should identify the exact phase responsibilities it covers and, when relevant, the neighboring responsibilities that are intentionally left to other prompts.

This prevents local prompt success from being mistaken for full phase coverage.

## Strict Rules

The Agent Prompt MUST NOT:

- introduce new architecture
- violate phase boundaries
- skip tests
- skip observability

The Agent Prompt MUST:

- be self-contained
- be executable without clarification
- remain inside approved prompt-plan and phase boundaries
- avoid architecture drift
- define outputs clearly enough for automatic review and downstream verification

## Anti-Patterns (forbidden)

- vague task framing instead of an execution contract
- missing out-of-scope boundaries
- missing observability requirements
- missing tests or unverifiable verification steps
- missing prompt-level task summary extensions
- prompt-plan boundary violations
- future-prompt contamination
- architecture invention or drift

## Local Agent-Prompt Quality Bar

An Agent Prompt is locally acceptable only when it:

- acts as a real execution contract rather than a vague task description
- defines scope and out-of-scope boundaries explicitly
- preserves prompt-plan boundaries when relevant
- preserves phase boundaries and architecture constraints
- includes observability requirements
- includes tests and verification strong enough for review and execution
- defines deliverables and task-summary extensions clearly enough for downstream validation
- includes binary acceptance criteria

## Input Alignment Rules

An Agent Prompt must remain aligned with its governing inputs.

This means it must:

- preserve the relevant phase contract accurately
- remain consistent with the approved Prompt Plan when one exists
- remain consistent with relevant system and architecture constraints
- preserve final prompt consequences from normalized presentation artifacts when they affect UI behavior, UX flow, asset usage, or template adaptation, according to [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md)
- avoid inventing implementation scope not supported by governing artifacts

## Failure / Repair Expectation

If local validation fails, the Agent Prompt must be revised and revalidated before downstream execution is treated as acceptable.

## Completion Criteria

An Agent Prompt is complete only when:

- all strict sections are present
- scope and out-of-scope boundaries are explicit
- prompt-plan boundaries are respected when relevant
- observability, tests, deliverables, and task-summary extensions are defined clearly enough for execution and review
- acceptance criteria are binary and testable
- the prompt is executable without clarification

## Validation Rule

If a prompt allows:

- ambiguity
- interpretation drift
- missing outputs
- missing boundaries
- missing tests
- missing task-summary extensions

then it is INVALID.

## Mandatory Self-Validation

Before returning the result, verify all of the following:

- there is no ambiguity in scope or expected outcome
- all required sections are present
- prompt-plan boundaries are respected when relevant
- phase boundaries are respected
- architecture drift is blocked
- observability requirements are present
- tests and verification are present
- deliverables are explicit
- task-summary extensions are structured and verifiable
- acceptance criteria are binary and testable
- the prompt is executable without clarification

If any check fails, revise the Agent Prompt before returning it.

## Output Discipline

Return ONLY the final Agent Prompt.