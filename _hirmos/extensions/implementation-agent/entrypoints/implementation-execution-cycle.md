# implementation-agent:implementation-execution-cycle

## Execution Contract

> Public-entrypoint relationship: this entrypoint remains available as an advanced/reusable execution surface. It should be used only when implementation planning is already approved for the selected phase. The regular public Implementation command is `hirmos implementation`.


### Purpose

Run the governed local implementation execution cycle for one selected phase using already-approved implementation prompts, then automatically perform phase review before surfacing the final result.

### Produces

- prompt-level execution artifacts under `_hirmos/artifacts/ops/runs/`, `_hirmos/artifacts/ops/reviews/`, and `_hirmos/artifacts/ops/retries/`
- phase review artifacts under `_hirmos/artifacts/ops/reviews/<phase-id>-phase-review/`
- command-scoped trust artifacts under `_hirmos/artifacts/context/implementation-agent/implementation-execution-cycle/`
- a governed cycle result surfaced as `completed`, `paused`, or `failed`

### Terminal States

- `completed` — allowed only when all in-scope prompt-level execution units for the selected phase are locally acceptable, the phase review has completed, and the truthful final completion can be surfaced honestly.
- `paused` — allowed when the cycle reaches a governed stop that requires Orchestrator review or direction before truthful continuation.
- `failed` — allowed when a command-critical grounding, execution, or validation condition prevents a governable cycle result.

## Run-Critical Checklist

- **Must read first:** `specs/implementation-execution-cycle.spec.md`, `specs/ENGINEERING_STANDARDS.md`, `specs/retry-prompt.spec.md`, and the required governing files they reference.
- **Must verify grounding:** relevant phase contract, relevant system-level SoT artifacts, approved implementation prompts for the selected phase, active stack context, and identifiable implementation repository context must be present and readable before execution proceeds.
- **Must preserve mandatory execution evidence discipline:** each executed prompt-level unit must produce the required summary, evidence, and review artifacts needed for downstream review, and must produce `patch.diff` whenever the codebase changed.
- **Must preserve phase scope:** execution remains bounded to one selected phase and must not silently spill into later phases.
- **Must not claim:** final phase acceptance, multi-phase completion, or release readiness without the supporting phase review basis.

Trust-artifact obligations, engineering standards, terminal-state validity, phase review rules, and bounded repair-loop rules are governed by `specs/implementation-execution-cycle.spec.md` together with `specs/ENGINEERING_STANDARDS.md`. Retry-generation semantics are governed by `specs/retry-prompt.spec.md`. Retry-budget and escalation rules are governed by `specs/EXECUTION_RETRY_ESCALATION_POLICY.md`.

## Allowed Final States

- `completed`
- `paused`
- `failed`

## Execution Logic

1. Read and follow `specs/implementation-execution-cycle.spec.md`, `specs/ENGINEERING_STANDARDS.md`, `specs/retry-prompt.spec.md`, and `specs/EXECUTION_RETRY_ESCALATION_POLICY.md`.
2. Before starting the cycle:
   - verify that required governing files are present and readable in the current working state
   - verify that the selected phase contract, the relevant system-level SoT artifacts, the active stack context, the in-scope implementation prompts, and the implementation repository context are present and readable
   - read the required governing files before continuing, with `specs/ENGINEERING_STANDARDS.md` and the active stack package surfaces treated as first-class execution grounding
3. Determine the selected phase and load only the approved implementation prompts that belong to that phase.
4. For each in-scope implementation prompt:
   - execute the bounded implementation task
   - produce required run outputs and evidence
   - run local review against the governing prompt, relevant phase contract, and evidence
   - if local review fails and bounded repair is still appropriate, generate bounded retry work and continue the local loop
   - if the retry budget or escalation threshold is reached, pause instead of silently broadening scope
5. Continue until every in-scope prompt-level unit for the selected phase is locally acceptable or the cycle must pause/fail.
6. Automatically perform phase review against the actual implemented codebase, selected phase contract, relevant system-level SoTs, execution evidence, and validation command results.
7. If phase review finds bounded fixable gaps that do not require Orchestrator involvement, perform bounded follow-up repair work, then rerun phase review.
8. Repeat the review/repair loop until the cycle can honestly surface `completed`, `paused`, or `failed`.
9. Update command-scoped trust artifacts under `_hirmos/artifacts/context/implementation-agent/implementation-execution-cycle/`.
10. Surface the cycle result in a single governed terminal run-state block.

## Required Terminal Output Templates

Final surfaced output for this entrypoint must follow exactly one required template based on the truthful final state.
Do not improvise hybrid terminal outputs.

Use exactly one of:
- `templates/implementation-execution-cycle/COMPLETED_TEMPLATE.md`
- `templates/implementation-execution-cycle/PAUSED_TEMPLATE.md`
- `templates/implementation-execution-cycle/FAILED_TEMPLATE.md`

Template-selection rules:
- use the completed template only when the cycle has completed and the surfaced result can honestly disclose the review result, remaining material gaps, and next action
- use the paused template when Orchestrator involvement is required and a truthful pause remains governable
- use the failed template when a command-critical grounding, execution, validation, or review condition prevents a governable completed or paused result

## Artifact Obligations

Required cycle trust-artifact obligations are governed by `specs/implementation-execution-cycle.spec.md`.

Prompt-level execution outputs must preserve the governed execution record under `_hirmos/artifacts/ops/` because downstream review depends on those canonical implementation execution artifacts.

If phase review began, a structured phase review artifact must be preserved and must follow `templates/implementation-execution-cycle/PHASE_REVIEW_TEMPLATE.md`, even when the final cycle state becomes `paused` or `failed`.

## Reporting Logic

### In-progress status blocks

- Make clear that the cycle is still running.
- Do not present interim progress as final completion.
- Do not end the command response without a terminal run-state block.

### Final response requirements

- Every runnable command response must end with exactly one terminal run-state block.
- Final surfaced output must follow the selected required terminal template.
- Final surfaced output must clearly disclose the phase review result.
- Final surfaced output must clearly disclose whether the actual codebase was reviewed.
- Governing paused, completed, and failed behavior remains in `specs/implementation-execution-cycle.spec.md`.


## Final Surfaced Output Self-Validation

Before returning the final surfaced output, verify that:
- the correct terminal template was selected for the truthful final state
- every required heading from the selected template is present
- non-paused completion states include a completed phase review
- the surfaced output explicitly discloses whether the actual codebase was reviewed
- if phase review initially failed, the surfaced output truthfully discloses follow-up repair attempts and what remained unresolved
- the surfaced output does not overstate remaining gaps or imply stricter acceptance than the review supports
- artifact paths and command claims are truthful

If the wrong template was selected, a required section is missing, or phase review / repair-loop disclosure is incomplete, revise before return. Do not return a partially compliant final output.
