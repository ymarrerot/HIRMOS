# implementation-agent:implementation-planning-cycle

## Execution Contract

> Public-entrypoint relationship: this entrypoint remains available as an advanced/reusable planning surface. The regular public Implementation command is `hirmos implementation`.


### Purpose

Run the full Implementation Planning Cycle for the intended implementation scope.

### Produces

- phase-scoped implementation prompt artifacts under `_hirmos/artifacts/prompts/phase-<NN>-<slug>/`
- cycle trust artifacts under `_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/`
- a governed cycle result surfaced as `completed` or `paused`

### Terminal States

- `completed` — allowed only when the intended implementation scope has been planned, required prompt artifacts and trust artifacts are in place, and the governing completed-state checks pass.
- `paused` — allowed when the cycle reaches a governed decision or grounding stop and reports that state using the required pause behavior.

## Run-Critical Checklist

- **Must read first:** `specs/implementation-planning-cycle.spec.md` and the required governing files it references.
- **Must verify grounding:** required cycle files, relevant phase contracts, relevant system-level SoT artifacts, the active stack context, and minimum implementation project context must be present and readable before planning proceeds.
- **Must follow governing pause behavior:** if unresolved gating items remain after prompt-set review and no governed downstream continuation rule applies, follow `specs/implementation-planning-cycle.spec.md`.
- **Must follow the required terminal templates:** completed runs must follow [_hirmos/extensions/implementation-agent/templates/implementation-planning-cycle/COMPLETED_TEMPLATE.md](../templates/implementation-planning-cycle/COMPLETED_TEMPLATE.md) and paused runs must follow [_hirmos/extensions/implementation-agent/templates/implementation-planning-cycle/PAUSED_TEMPLATE.md](../templates/implementation-planning-cycle/PAUSED_TEMPLATE.md).
- **Must not claim:** full cycle completion if unresolved gating items remain.

Trust-artifact obligations and completed/paused behavior are governed by `specs/implementation-planning-cycle.spec.md`.

## Allowed Final States

- `completed`
- `paused`

## Planning Logic

1. Read and follow `specs/implementation-planning-cycle.spec.md`.
2. Before starting the cycle:
   - verify that the required cycle files are present and readable in the current working state
   - verify that the relevant phase contracts, relevant system-level SoT artifacts, the active stack context, and minimum implementation project context are present and readable
   - read the required governing files before continuing
3. If the minimum implementation grounding contract is not satisfied:
   - pause the cycle
   - report the missing grounding items clearly
   - do not proceed as if dependable implementation execution contracts were produced
4. Materialize prompt artifacts using the canonical implementation-planning layout under `_hirmos/artifacts/prompts/phase-<NN>-<slug>/`, including:
   - `PROMPT_PLAN.md` for the phase-level prompt plan
   - one Agent Prompt file per prompt id using the pattern `P<phase>-<index>-<slug>.md`
5. Generate or refine the implementation prompt set across the intended planned scope.
6. For each implementation prompt artifact:
   - run `implementation-agent:prompt-planning`
   - run `implementation-agent:agent-prompt`
   - validate the result locally against the relevant phase contract, prompt sizing/scope discipline, execution-contract strength, and stack-aware command/standards grounding when relevant
   - refine until locally acceptable before continuing
7. After local prompt validation passes, run a full prompt-set review.
8. If prompt-set review fails:
   - refine the affected prompt artifacts
   - repeat the review until the cycle passes or a grounding failure must be reported
9. If unresolved gating items remain, follow the governing pause behavior in `specs/implementation-planning-cycle.spec.md`.

## Artifact Obligations

Required trust-artifact obligations are governed by `specs/implementation-planning-cycle.spec.md`.

Runtime trust artifacts live under `_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/`.

Templates and folder scaffolding do not count as generated runtime artifacts.

Compact final-state, artifact-completeness, and downstream-authority checks for this cycle are summarized in `specs/CYCLE_VALIDITY_SPINE.md`.

## Reporting Logic

### In-progress status blocks

- Make clear that the cycle is still running.
- Do not present interim progress as final completion.
- Do not end the command response without a terminal run-state block.

### Final response requirements

- Every runnable command response must end with exactly one terminal run-state block.
- Completed runs must follow [_hirmos/extensions/implementation-agent/templates/implementation-planning-cycle/COMPLETED_TEMPLATE.md](../templates/implementation-planning-cycle/COMPLETED_TEMPLATE.md).
- Paused runs must follow [_hirmos/extensions/implementation-agent/templates/implementation-planning-cycle/PAUSED_TEMPLATE.md](../templates/implementation-planning-cycle/PAUSED_TEMPLATE.md).
- Final surfaced output must include a link to download the updated full working copy as the minimum required Orchestrator-facing surfaced output.
- Governing completed and paused behavior remains in `specs/implementation-planning-cycle.spec.md`.


## Required Terminal Output Templates

- Final surfaced output must use exactly one required terminal template.
- Use [_hirmos/extensions/implementation-agent/templates/implementation-planning-cycle/COMPLETED_TEMPLATE.md](../templates/implementation-planning-cycle/COMPLETED_TEMPLATE.md) for `completed` runs.
- Use [_hirmos/extensions/implementation-agent/templates/implementation-planning-cycle/PAUSED_TEMPLATE.md](../templates/implementation-planning-cycle/PAUSED_TEMPLATE.md) for `paused` runs.
- Do not improvise mixed terminal outputs.
- Do not omit required sections from the selected template.

## Final Surfaced Output Self-Validation

Before the final response, verify that:
- the correct required terminal template was selected for the truthful run state
- every required section from the selected template is present
- the grounding result is truthful, including missing repo-wide test-command disclosure when relevant
- surfaced artifact paths are real and relevant
- inherited upstream warnings or planning limitations are surfaced when they materially affect downstream expectations
- the final Orchestrator-facing response includes a clear next action
- the final Orchestrator-facing response includes a link to download the updated full working copy

If the wrong template was selected or a required section is missing, revise before return. Do not return a partially compliant final output.

## Canonical Examples

Examples below are illustrative; governing behavior remains in the Spec.


### Paused run shape

Use [_hirmos/extensions/implementation-agent/templates/implementation-planning-cycle/PAUSED_TEMPLATE.md](../templates/implementation-planning-cycle/PAUSED_TEMPLATE.md) as the single authoritative source for paused output structure and required fields. Do not rely on duplicated inline paused examples in this entrypoint.

Examples below are illustrative; governing behavior remains in the Spec. The identity label is intentionally generic; the concrete value is resolved from the manifest by the core runtime.

### Example run: completed

Use [_hirmos/extensions/implementation-agent/templates/implementation-planning-cycle/COMPLETED_TEMPLATE.md](../templates/implementation-planning-cycle/COMPLETED_TEMPLATE.md) as the authoritative source for completed output structure and required fields. Do not rely on duplicated inline completed examples in this entrypoint.