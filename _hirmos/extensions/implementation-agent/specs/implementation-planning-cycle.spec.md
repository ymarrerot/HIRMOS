# Spec: Implementation Planning Cycle

## Purpose

> Public-entrypoint relationship: this cycle remains a reusable implementation-planning subcycle. Regular users should normally run `hirmos implementation`, which may reuse this cycle and then pause for approval before execution.


Run the governed cycle that derives and validates the implementation prompt set from the planned phase contracts.

This cycle orchestrates the implementation-planning family inside `implementation-agent`. It does not replace the underlying local Specs that define prompt-planning and agent-prompt truth inside the same extension.

## Output location

- `_hirmos/artifacts/prompts/phase-<NN>-<slug>/PROMPT_PLAN.md`
- `_hirmos/artifacts/prompts/phase-<NN>-<slug>/P<phase>-<index>-<slug>.md`

## Required inputs

Use:
- relevant phase contracts under `_hirmos/artifacts/phases/`
- relevant system-level SoT artifacts
- active stack context resolved through `_hirmos/project.json` and the selected stack package manifest/surfaces
- current project context

At the current framework maturity level, this cycle may run across the full planned phase scope, but it remains implementation-owned rather than upstream-design-owned.

## Readiness check before run

Before this cycle begins, verify that the required governing files and relevant project artifacts are present and readable in the current working state.

Read the governing files before starting the cycle.

If the required files are missing or unreadable, the cycle must not be treated as properly started.

## Minimum implementation grounding contract

Implementation planning may only produce governably complete execution contracts when all of the following are true:

- the relevant phase contracts and governing SoTs are present and readable
- the active stack resolves cleanly through `_hirmos/project.json` and the selected stack package
- the stack package exposes readable `engineering_standards` and `commands` surfaces
- a real implementation repository or a minimal implementation starter is present in the working state
- the intended implementation root or codebase structure is identifiable
- a command baseline is available from repository-local scripts/commands or, when those are not available yet, from an explicitly accepted temporary baseline
- if no dedicated repository-wide test command exists yet, that gap is recorded explicitly in reporting and the prompt set must not pretend a stable test baseline already exists

Minimum implementation project context should include, at minimum, enough grounding to identify:

- the implementation root or starter layout
- the primary package/runtime toolchain
- the main verification path (tests, linting, typecheck, build, or equivalent relevant command families)

If this contract is not satisfied, the cycle must pause rather than pretending to generate dependable implementation execution contracts.

## Required governing files

Before running this cycle, read:
- [_hirmos/extensions/implementation-agent/specs/prompt-planning.spec.md](./prompt-planning.spec.md)
- [_hirmos/extensions/implementation-agent/specs/agent-prompt.spec.md](./agent-prompt.spec.md)
- [_hirmos/extensions/implementation-agent/specs/CYCLE_VALIDITY_SPINE.md](./CYCLE_VALIDITY_SPINE.md)
- [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md) when normalized presentation artifacts exist or may affect implementation consequences
- _hirmos/artifacts/sot/PRESENTATION_SOT.md (`/_hirmos/artifacts/sot/PRESENTATION_SOT.md`) when it exists and materially affects implementation consequences

## Governing Spec relationship

This cycle is the orchestrator-facing planning cycle for the implementation side.

For each implementation prompt artifact, the Assistant must use the relevant canonical local Specs:

- `specs/prompt-planning.spec.md` for decomposition, coverage strategy, sequencing, failure containment, and prompt-set planning quality
- `specs/agent-prompt.spec.md` for the local execution-contract shape, scope boundaries, required outputs, tests, observability, and acceptance criteria of each generated agent prompt

Relationship:
- `prompt-planning.spec.md` decides how the phase contract should be decomposed into bounded execution units
- `agent-prompt.spec.md` decides how each execution unit should be written as a reliable agent execution contract

The cycle orchestrates the loop. These Specs define the local planning and generation truth.

## Governing principle

Implementation Planning should remain horizontally planned across the intended scope. This is implementation-side planning, not upstream design-authority redefinition.

Planning the prompt set across all phases is allowed at the current framework maturity level, even though execution remains more bounded later.

When normalized presentation artifacts exist, apply [_hirmos/extensions/implementation-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md) and preserve the implementation-planning consequences needed for prompt planning and final agent prompts.

## Repeatable unit

Generate or refine one implementation prompt artifact.

For each prompt artifact, the cycle must:
- read and follow `specs/prompt-planning.spec.md` for the relevant decomposition and coverage logic
- read and follow `specs/agent-prompt.spec.md` for the local execution-contract requirements of the generated prompt
- validate the prompt artifact against:
  - the relevant phase contract
  - prompt quality expectations
  - prompt size/scope discipline
  - local coverage expectations

Repeat until each prompt artifact is locally acceptable.

## Canonical prompt artifact materialization

Implementation-planning-cycle owns the canonical prompt artifact layout under `_hirmos/artifacts/prompts/`.

Use this structure:

- one folder per phase using `phase-<NN>-<slug>/`
- `PROMPT_PLAN.md` for the approved phase-level prompt plan
- one Agent Prompt file per execution unit using `P<phase>-<index>-<slug>.md`

Examples:

- _hirmos/artifacts/prompts/phase-01-planning-baseline/PROMPT_PLAN.md (`/_hirmos/artifacts/prompts/phase-01-planning-baseline/PROMPT_PLAN.md`)
- _hirmos/artifacts/prompts/phase-01-planning-baseline/P1-001-bootstrap-phase-baseline.md (`/_hirmos/artifacts/prompts/phase-01-planning-baseline/P1-001-bootstrap-phase-baseline.md`)
- _hirmos/artifacts/prompts/phase-02-core-polling-platform/P2-003-build-live-poll-api.md (`/_hirmos/artifacts/prompts/phase-02-core-polling-platform/P2-003-build-live-poll-api.md`)

This layout is mandatory for implementation-planning outputs unless a future explicit framework change replaces it.

## Prompt-set review

After prompt artifacts are locally acceptable, run a full prompt-set review.

That review must check:
- full and correct implementation-scope coverage of the planned phases
- prompt sizing/scope quality
- prompt-set coherence
- consistency between prompt-planning strategy and the actual generated agent prompts

## Implementation-Planning Gating Review

Before finalizing implementation-planning-cycle outputs, check whether unresolved gating items materially affect prompt boundaries, prompt count, execution contract shape, or acceptance conditions. If yes, preserve that uncertainty explicitly and request Orchestrator direction when continuing would overstate execution readiness.

If continuing would overstate execution readiness, the cycle should pause and present the unresolved items as a structured decision request rather than presenting the run as governably complete.

## Readiness-sensitive implementation planning

When implementation planning supports a real-use delivery target, generated prompt sets should preserve any readiness-critical uncertainty that materially affects acceptance, observability, resilience, or execution expectations.

Implementation-planning must not make the execution layer appear more operationally ready than the upstream planning artifacts support.

## End condition

A completed run is not governably valid if required runtime trust artifacts are missing. Absence of `DECISION_LOG.md` is valid only when `CYCLE_STATUS.md` explicitly records `Decision log status: none required this run`.

If the cycle is reported as `completed`, the completed-state reporting must explicitly record:
- the terminal-state basis
- required runtime trust artifact completeness
- the unresolved-item or limitation basis
- any residual limitations that remain non-blocking

The Implementation Planning Cycle ends only when:
- the prompt set fully and correctly covers the implementation scope of the planned phases
- prompt sizing/scope quality is acceptable
- the prompt set is coherent enough for bounded execution
- each prompt artifact is strong enough to act as a reliable agent execution contract

## Required Runtime Trust Artifacts

After each run, update the command-scoped runtime trust artifacts under `_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/`. Required artifacts are:
- _hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/CYCLE_STATUS.md (`/_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/CYCLE_STATUS.md`)
- _hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/RUN_TRACE.md (`/_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/RUN_TRACE.md`)
- _hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/VALIDATION_TRACE.md (`/_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/VALIDATION_TRACE.md`)
- _hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/DECISION_LOG.md (`/_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/DECISION_LOG.md`) when decisions are made or requested

Use the corresponding templates under `_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/templates/` when generating or refining these artifacts. Templates and folder scaffolding do not count as generated runtime artifacts.

If no implementation-planning-cycle decisions were made or requested during the run, `DECISION_LOG.md` may be omitted only if `CYCLE_STATUS.md` explicitly states `Decision log status: none required this run`.

If unresolved gating items remain, record that generated prompt artifacts are planning outputs but not yet governably finalized execution-ready outcomes.

If the cycle completes without a dedicated repository-wide test command, the completed-state reporting must state that limitation explicitly and preserve that prompts may need to introduce or refine test execution steps until a stable repo-wide test baseline exists.

## Terminal Output Surfacing

The allowed surfaced terminal states for this entrypoint are:
- `completed`
- `paused`

Final surfaced output must use the required template for the truthful terminal state.

## Required Terminal Templates

Use:
- `templates/implementation-planning-cycle/COMPLETED_TEMPLATE.md` for `completed` runs
- `templates/implementation-planning-cycle/PAUSED_TEMPLATE.md` for `paused` runs

Completed-state reporting must surface inherited planning-relevant warnings when they materially affect downstream execution expectations.

## Final Surfaced Output Self-Validation

Before surfacing the final result, verify that:
- the correct required terminal template was selected for the truthful run state
- every required section from the selected template is present
- the grounding result is truthful, including missing repo-wide test-command disclosure when relevant
- surfaced artifact paths are real and relevant
- inherited upstream warnings or planning limitations are surfaced when they materially affect downstream expectations
- the final surfaced output includes a clear next action and working-copy link

If these checks fail, revise before return. Do not surface a partially compliant final output.

## Local Prompt Quality Bar

A prompt artifact is locally acceptable only when it:
- is clearly bounded to the relevant approved scope
- is aligned with the governing phase contract
- is sized appropriately for bounded execution and review
- defines required outputs, tests, observability, and acceptance criteria clearly enough for deterministic downstream execution
- does not depend on major unstated assumptions

## Input Alignment Rules

Implementation prompt artifacts must remain aligned with their governing inputs.

This means they must:
- preserve the phase contract accurately
- preserve delivery boundaries when relevant
- remain consistent with system-level and architecture constraints that materially affect implementation
- avoid silently introducing new implementation scope not supported by the governing phase artifacts

## Failure / Repair Expectation

If an individual prompt artifact fails:
- refine it before continuing

If full prompt-set review fails:
- refine the affected prompt artifacts and repeat the prompt-set review

## Non-goals

This cycle does NOT:
- execute implementation work
- define release control
- define autonomous execution stop/start behavior

## Downstream handoff note

A passing Implementation Planning Cycle means the prompt set is strong enough for bounded implementation execution to be selected and run under the current maturity model.

It does not by itself authorize full autonomous multi-phase execution.

## Local validation interface

When the Implementation Planning Cycle orchestrates local implementation planning work, use the local validation interface of the governing Specs, including where available:

- Required Inputs
- Local Prompt-Plan Quality Bar or local Agent-Prompt quality bar
- Input Alignment Rules
- Failure / Repair Expectation
- Validation and self-validation expectations on the prompt side

These semantic slots support consistent local gating without requiring the cycle to duplicate the underlying Spec logic.

## Mandatory self-validation

Before treating the cycle as complete, verify that:
- the cycle was properly grounded in readable governing/project files and the active stack resolved cleanly
- each prompt artifact passed local validation against the relevant phase contract, prompt sizing/scope discipline, execution-contract quality expectations, and stack-aware command/standards grounding
- the prompt set fully and correctly covers the implementation scope of the planned phases
- prompt sizing/scope quality is acceptable
- the prompt set is coherent enough for bounded execution
- each prompt artifact is strong enough to act as a reliable agent execution contract
- prompt artifacts were generated against `prompt-planning.spec.md` and `agent-prompt.spec.md` as canonical local Specs

If any of the above checks fail, refine the affected prompt artifacts or stop and report the grounding issue clearly.

## Compact validity checkpoint

Before finalizing the cycle response state, use `specs/CYCLE_VALIDITY_SPINE.md` as a compact validation checkpoint. Behavioral authority remains in this Spec.

## Output discipline

Return the cycle result, including:
- what prompt artifacts were created or refined
- whether local prompt validation passed
- whether full prompt-set review passed
- whether the prompt artifacts were generated against `prompt-planning.spec.md` and `agent-prompt.spec.md` as canonical local Specs
- any remaining issues requiring Orchestrator review