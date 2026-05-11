# implementation-execution-cycle.spec

## Purpose

> Public-entrypoint relationship: this cycle remains a reusable implementation-execution subcycle. Regular users should normally run `hirmos implementation`, which may reuse this cycle only after implementation planning has been explicitly approved.


Govern the local implementation execution cycle for one selected phase, including prompt-scoped execution, mandatory evidence capture, built-in phase review, bounded follow-up repair, and truthful final terminal-state surfacing.

This Spec owns the behavioral truth for:
- phase-scoped execution
- prompt-by-prompt local execution discipline
- mandatory execution evidence artifacts
- stack-aware execution grounding
- built-in phase review
- bounded repair after failed phase review
- cycle trust artifacts and terminal-state rules
- final surfaced-output self-validation

Generic implementation discipline is centralized in `ENGINEERING_STANDARDS.md`. Retry-generation semantics are centralized in `retry-prompt.spec.md`. Retry-budget and escalation specifics remain centralized in `EXECUTION_RETRY_ESCALATION_POLICY.md`.

The entrypoint owns invocation and minimum runtime-facing output. This Spec owns the deeper behavioral requirements.

## Governing files to read first

Before this cycle begins, read at minimum:
- [_hirmos/extensions/implementation-agent/specs/ENGINEERING_STANDARDS.md](./ENGINEERING_STANDARDS.md)
- [_hirmos/extensions/implementation-agent/specs/retry-prompt.spec.md](./retry-prompt.spec.md)
- [_hirmos/extensions/implementation-agent/specs/EXECUTION_RETRY_ESCALATION_POLICY.md](./EXECUTION_RETRY_ESCALATION_POLICY.md)
- `_hirmos/project.json`
- the selected stack manifest and required stack surfaces
- the selected phase contract
- relevant system-level SoTs needed to execute the selected phase truthfully
- the in-scope approved implementation prompts for the selected phase

When present and relevant, also read execution-layer governance that materially constrains implementation behavior.

## Stack resolution rule

This cycle does not own stack resolution. It consumes the active stack resolved through:
1. `_hirmos/project.json`
2. `_hirmos/stacks/<selected-stack-id>/stack.yaml`
3. the stack surfaces declared by that manifest

At minimum, the execution cycle should consume stack surfaces that materially affect implementation behavior, especially:
- `overview`
- `engineering_standards`
- `commands`
- `execution_rules`

If the active stack cannot be resolved cleanly, the cycle must not pretend stack grounding exists.

## Readiness check before run

Before this cycle begins, verify that the required governing files and relevant project artifacts are present and readable in the current working state.

Read the governing files before starting the cycle.

If the required files are missing or unreadable, the cycle must not be treated as properly started.

## Minimum execution grounding contract

Implementation execution may only produce governably reviewable outputs when all of the following are true:
- the relevant phase contract and relevant system-level SoTs are present and readable
- approved implementation prompts for the selected phase are present and readable
- the active stack resolves cleanly through `_hirmos/project.json` and the selected stack package
- the implementation repository or implementation root is identifiable in the working state
- command and verification baselines can be grounded in repository-local commands or an explicitly stated governed fallback
- the locations for governed execution artifacts can be created or updated

If this grounding contract is not satisfied, the cycle must pause or fail rather than pretending execution closure.

## Output locations

### Prompt-level execution artifacts

For each executed prompt-level unit, preserve the execution record under:
- `_hirmos/artifacts/ops/runs/<prompt-id>/summary.md`
- `_hirmos/artifacts/ops/runs/<prompt-id>/evidence.md`
- `_hirmos/artifacts/ops/runs/<prompt-id>/patch.diff` whenever the codebase changed
- `_hirmos/artifacts/ops/reviews/<prompt-id>/...`
- `_hirmos/artifacts/ops/retries/<prompt-id>/...`

These outputs are mandatory.
Without complete prompt-level outputs, downstream review becomes weak or impossible.

The expected retry artifact shape is governed by `retry-prompt.spec.md`. Retry-budget and escalation thresholds are governed by `EXECUTION_RETRY_ESCALATION_POLICY.md`.

### Phase review artifacts

If phase review began, preserve it under a stable phase-specific review path such as:
- `_hirmos/artifacts/ops/reviews/<phase-id>-phase-review/REVIEW.md`
- `_hirmos/artifacts/ops/reviews/<phase-id>-phase-review/EVIDENCE.md`

This structured review artifact must be preserved even when the final cycle state becomes `paused` or `failed`. The surfaced review should follow `templates/implementation-execution-cycle/PHASE_REVIEW_TEMPLATE.md`.

### Cycle trust artifacts

After each run, update the command-scoped runtime trust artifacts under `_hirmos/artifacts/context/implementation-agent/implementation-execution-cycle/`.
Required artifacts are:
- `CYCLE_STATUS.md`
- `RUN_TRACE.md`
- `VALIDATION_TRACE.md`
- `DECISION_LOG.md` when decisions are made or requested

## Execution loop

### Prompt-level local loop

For each in-scope prompt-level execution unit:
- execute the bounded implementation task
- preserve required run/evidence artifacts
- review the result locally against the prompt, the relevant phase contract, and the actual produced evidence
- if local repair is still bounded and appropriate, generate retry work and continue the local loop
- if local repair is no longer appropriate, escalate truthfully rather than broadening scope silently

### Built-in phase review

After all in-scope prompt units for the selected phase have completed local execution and local validation, the cycle must automatically perform phase review before surfacing its final terminal result.

The phase review must verify the selected phase against:
- the actual implemented codebase
- the selected Phase SoT
- relevant system-level SoTs
- produced execution evidence
- verification commands and their actual results

### Bounded follow-up repair loop

If phase review finds fixable implementation or coverage gaps that can be resolved without Orchestrator involvement, the cycle must attempt bounded follow-up repair work.

After each bounded repair pass:
- update the relevant prompt/run/review artifacts as needed
- rerun the phase review

Do not surface final completion before this loop resolves to an honest completed result, paused result, or failed result.

## Pause vs fail rules

### Pause is allowed only when
- Orchestrator involvement is genuinely required
- an unresolved product truth, policy decision, or approval-bound tradeoff blocks truthful continuation
- a missing environment dependency prevents honest completion and cannot be resolved within approved scope
- bounded repair was exhausted without reaching an honest completed result

### Failure is allowed only when
- the cycle cannot be grounded at all
- a command-critical execution condition prevents a governable result and no truthful pause path makes sense
- minimum required artifacts for reviewability cannot be produced

## Terminal state surfacing

Allowed final surfaced states are:
- `completed`
- `paused`
- `failed`

A normal surfaced result of “ready for phase review handoff” is no longer sufficient as final completion for this entrypoint.

## Required terminal templates

The final surfaced output must follow exactly one of:
- `templates/implementation-execution-cycle/COMPLETED_TEMPLATE.md`
- `templates/implementation-execution-cycle/PAUSED_TEMPLATE.md`
- `templates/implementation-execution-cycle/FAILED_TEMPLATE.md`

Qualification rules:
- use completed only when the cycle has completed and the surfaced result can honestly disclose the review result, remaining material gaps, and next action
- use paused when Orchestrator involvement is required and a truthful pause remains governable
- use failed when a command-critical grounding, execution, validation, or review condition prevents a governable completed or paused result

## End condition

The Implementation Execution Cycle for the selected phase ends only when:
- all in-scope prompt-level execution units for that phase have passed the local execution/review/retry loop or were escalated truthfully
- required prompt-level outputs for review exist for each completed execution unit
- required cycle trust artifacts are updated for the current run state
- the phase review has been completed for non-paused completion states
- if phase review initially failed, the bounded repair loop was completed honestly
- the final response does not overstate remaining gaps or imply stricter acceptance than the review supports

## Mandatory self-validation

Before treating the cycle as complete, verify that:
- the cycle was grounded in readable governing/project files and the active stack resolved cleanly
- phase scope was preserved
- each completed execution unit produced the required summary, evidence, and patch artifacts when code changed
- local review used prompt + phase contract + evidence rather than guesswork
- retries remained bounded when used
- phase review was completed for non-paused completion states
- phase review was based on the actual codebase, selected phase contract, relevant system-level SoTs, execution evidence, and validation results
- bounded repair was attempted when appropriate after a failed review
- the final surfaced output uses the correct required template
- every required heading from the selected template is present
- artifact paths and command claims are truthful

If any of the above checks fail, refine the affected execution unit, continue bounded repair, pause, or fail rather than claiming governable completion.

## Non-goals

This cycle does NOT:
- plan phases
- generate implementation prompts from scratch
- execute all phases autonomously
- replace Orchestrator approval where approval-bound tradeoffs are involved
- claim release readiness by itself

## Output discipline

Return the cycle result, including:
- what in-scope implementation prompts were executed
- what execution/review/retry artifacts were produced
- whether phase review completed
- whether the actual codebase was reviewed
- whether bounded repair was attempted
- whether the final result is completed, paused, or failed
- any remaining issues requiring Orchestrator review
