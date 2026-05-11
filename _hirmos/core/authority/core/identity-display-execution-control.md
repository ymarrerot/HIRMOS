# Identity Display Execution Control

## Purpose

Define the authoritative Core-local doctrine for the `Identity display execution control`.

Use this file when you need the canonical rule for how HIRMOS declares runtime identity, validates surfaced results, renders final output, and constrains allowed terminal run states.

## Governing scope

This file governs the `Identity display execution control`.

Use it when you need the authoritative rule for:
- manifest-level `runtime.identity` declarations
- final surfaced-output validity
- required output wrapper shape
- terminal run states
- final reporting minimums
- paused or provisional surfaced-result contracts

## Identity display execution control rule

A runnable HIRMOS command must not surface a final chat-facing result as trustworthy unless it satisfies the identity display execution control.

This control exists to ensure that surfaced output:
- uses the right runtime identity
- follows the required wrapper shape
- uses an allowed terminal run state
- does not overclaim completion
- remains reviewable to the Orchestrator

## Required template source

When this control requires a governed surfaced-output shape, use:
- `/_hirmos/core/templates/IDENTITY_DISPLAY_EXECUTION_CONTROL_TEMPLATE.md`

## Surfaced-result validity

A surfaced result is valid only if:
- it uses an allowed runtime identity
- it uses the required wrapper structure when that structure is required
- its terminal state is allowed
- its content matches the true run state
- it does not hide material omissions or unresolved defects

Do not treat a chat-facing result as trustworthy just because it sounds polished.

## Wrapper ownership and rendering boundary

The Core owns the surfaced output contract.

Extensions may contribute the body content that appears inside a valid surfaced result, but they do not own the wrapper contract itself.

This preserves a clean boundary between:
- extension-local workflow behavior
- Core-owned runtime identity and surfaced-output validity

## Manifest-level runtime identity declaration {#runtime-identity-declaration}

Extensions declare runtime identity through their manifest-level `runtime.identity` contract.

That declaration is what tells the Core:
- what identity the extension is allowed to surface under
- which chat-facing wrapper identity should appear at runtime

The declaration must be explicit, coherent, and aligned with the public runnable surface. Do not rely on accidental naming or ad hoc phrasing in chat output.

## Terminal run states {#terminal-run-states}

A surfaced final result must use an allowed terminal run state.

The terminal run state must match the truth of the run.

Do not surface:
- completion when the run is actually paused
- confidence when the run is actually provisional
- success when the run should fail closed

## Final reporting minimum {#final-reporting-minimum}

Under uncertainty, apply the bootstrap Step 0 — Framework-wide uncertainty rule before surfacing readiness, completion, validation, or artifact-state claims.

A trustworthy final surfaced result must make the run state legible enough for the Orchestrator to understand what happened.

At minimum, final reporting should make clear:
- the terminal run state
- whether readiness or completion was truly granted
- what the next allowed state is, when that matters to safe continuation

## Paused cycle output contract {#paused-cycle-output-contract}

When a serious cycle pauses, the surfaced result must clearly communicate that the cycle is paused rather than completed.

The paused surfaced result should preserve the truth of why continuation is blocked and what kind of decision or resolution is still required.

## Provisional run contract {#provisional-run-contract}

When a run is provisional, the surfaced result must communicate that provisional status honestly.

Do not collapse provisional outputs into completed outputs just because an artifact exists.

## Final reporting expectations {#final-reporting-expectations}

Final reporting should protect trust.

It should:
- remain truthful to the actual run state
- preserve the required surfaced shape when applicable
- avoid overstating certainty or completion
- stay legible enough for operator review

## Invalid command surfaced result

When a `hirmos` input fails exact command matching, the surfaced result must clearly report invalid-command failure.

It must not present ordinary assistant help as though a valid Core command executed.

It must preserve the runtime identity/output contract for a fail-closed command result.

## Boundary note

This file owns the integrated rule for identity display, surfaced-result validity, runtime identity declaration, and terminal-state reporting.

Other files may summarize or point to this doctrine, but they should not re-own these rules.

## Related core files

- [Execution controls](./execution-controls.md)
- [Entrypoint execution contract](./entrypoint-execution-contract.md)
- [Hook execution control](./hook-execution-control.md)
- [Extension manifest authority](./extension-manifest-authority.md)


## Continuity failure surfaced result

If continuity of the active cumulative working copy becomes unclear or unverified, surfaced output must not imply trustworthy completion.

The runtime must surface the continuity failure honestly rather than continuing with ordinary completion-style output.

Do not present continuity-uncertain results as if the working state was still verified.
