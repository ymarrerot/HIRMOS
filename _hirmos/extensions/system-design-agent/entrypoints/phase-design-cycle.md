# system-design-agent:phase-design-cycle

## Execution Contract

### Purpose

Run the full Phase Design Cycle for the current working state.

### Produces

- phase artifacts under `_hirmos/artifacts/phases/` aligned to the current planning baseline
- cycle trust artifacts under `_hirmos/artifacts/context/system-design-agent/phase-design-cycle/`
- a governed cycle result surfaced as `completed` or `paused`

### Terminal States

- `completed` — allowed only when the required phase set has been generated or refined, the governing completed-state checks pass, and no unresolved gating items block honest completion.
- `paused` — allowed when the cycle reaches a governed decision or grounding stop and reports that state using the required pause behavior.

## Run-Critical Checklist

- **Must read first:** `specs/phase-design-cycle.spec.md` and the required governing files it references.
- **Must verify grounding:** required cycle files, _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`), relevant system-level SoT artifacts, and staged-delivery context when relevant must be present and readable before planning proceeds.
- **Must validate final state:** validate the final run state against `specs/CYCLE_VALIDITY_SPINE.md` and `specs/phase-design-cycle.spec.md` before responding.
- **Must follow governing pause behavior:** if unresolved gating items remain after phase-set review, follow `specs/phase-design-cycle.spec.md`.
- **Must not claim:** full cycle completion if unresolved gating items remain.

## Allowed Final States

- `completed`
- `paused`

## Required Terminal Output Templates

- Completed runs must follow [_hirmos/extensions/system-design-agent/templates/phase-design-cycle/COMPLETED_TEMPLATE.md](../templates/phase-design-cycle/COMPLETED_TEMPLATE.md).
- Paused runs must follow [_hirmos/extensions/system-design-agent/templates/phase-design-cycle/PAUSED_TEMPLATE.md](../templates/phase-design-cycle/PAUSED_TEMPLATE.md).
- Do not improvise hybrid terminal outputs.
- The selected template is the source of truth for final surfaced output shape.

## Planning Logic

1. Read and follow `specs/phase-design-cycle.spec.md`.
2. Before starting the cycle:
   - verify that the required cycle files are present and readable in the current working state
   - verify that _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`), relevant system-level SoT artifacts, and staged delivery context when relevant are present and readable
   - read the required governing files before continuing
3. If the required files are missing or unreadable:
   - stop
   - report the issue clearly
   - do not proceed as if the cycle was properly grounded
4. Determine whether this execution is a governed rerun of the Phase Design Cycle.
5. If unresolved upstream gating still materially affects phase boundaries, roadmap grouping, downstream phase-contract shape, or delivery-target feasibility, do not continue as if the phase set can complete honestly. Follow the governing pause behavior in `specs/phase-design-cycle.spec.md`.
6. Generate or refine the full phase set defined by _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`), unless explicitly scoped otherwise.
7. For each generated phase artifact:
   - run `system-design-agent:phase-sot`
   - require the artifact to pass local validation against `specs/phase-sot.spec.md`
   - refine until locally acceptable before continuing
8. After local validation passes across the phase set, run a full phase-set review.
9. If phase-set review fails:
   - refine the affected phase artifacts
   - repeat the review until the cycle passes or a grounding failure must be reported
10. If this execution is a rerun, explicitly state:
   - why the rerun is happening
   - what changed since the prior pass
   - whether the new cycle result supersedes the previous phase-design-cycle result
11. If unresolved gating items remain and they materially affect the phase roadmap or downstream phase contracts, follow the governing pause behavior in `specs/phase-design-cycle.spec.md`.
12. Progress updates are allowed while the cycle is running, but they must clearly indicate that the cycle is still in progress and must not sound like final completion.

## Artifact Obligations

Required trust-artifact obligations are governed by `specs/phase-design-cycle.spec.md`.

Runtime trust artifacts live under `_hirmos/artifacts/context/system-design-agent/phase-design-cycle/`.

Templates and folder scaffolding do not count as generated runtime artifacts.

Compact final-state and artifact-completeness checks for this cycle are summarized in `specs/CYCLE_VALIDITY_SPINE.md`.

## Reporting Logic

### In-progress status blocks

- Make clear that the cycle is still running.
- Do not present interim progress as final completion.
- Do not end the command response without a terminal run-state block.

### Final response requirements

- Every runnable command response must end with exactly one terminal run-state block.
- Final responses must include a link to download the updated full working copy as the minimum required Orchestrator-facing surfaced output.
- Reruns should surface rerun reason, what changed, and supersession when relevant.
- Governing paused and completed behavior remains in `specs/phase-design-cycle.spec.md`.

## Final Surfaced Output Self-Validation

Before returning the final surfaced output, validate the surfaced body content against these criteria:

### Criterion 1 — Terminal-state compliance
- The surfaced output must reflect the true terminal state.
- If paused, it must be surfaced as paused.
- If completed, it must be surfaced as completed.

### Criterion 2 — Required template compliance
- If terminal state is `paused`, the surfaced output must include every required heading from [_hirmos/extensions/system-design-agent/templates/phase-design-cycle/PAUSED_TEMPLATE.md](../templates/phase-design-cycle/PAUSED_TEMPLATE.md).
- If terminal state is `completed`, the surfaced output must include every required heading from [_hirmos/extensions/system-design-agent/templates/phase-design-cycle/COMPLETED_TEMPLATE.md](../templates/phase-design-cycle/COMPLETED_TEMPLATE.md).
- No required heading may be omitted.
- Do not collapse required sections into improvised substitute headings.
- Do not rename required headings in a way that changes their role.

### Criterion 3 — Artifact/path truthfulness
- Every surfaced artifact path must be real and relevant to the run.
- Do not claim actions that were not performed.

### Criterion 4 — Unresolved-item fidelity
- Surfaced gated and non-gating limitations must remain faithful to the cycle artifacts and current phase-set review outcome.

### Criterion 5 — Honest completion posture
- Do not surface `completed` if unresolved gating items still materially affect phase boundaries, roadmap grouping, downstream phase-contract shape, or delivery-target feasibility.
- If `completed`, remaining limitations must be non-gating and surfaced explicitly.

### Criterion 6 — Next-step clarity
- The surfaced result must clearly tell the Orchestrator what to do next.
- If paused, the rerun condition must be explicit.

If any required template section is missing or the surfaced result overstates honest completion, revise before return. Do not return a partially compliant final output.

## Output-shape authority reminder

Use the entrypoint-specific templates below as the authoritative source for final surfaced output structure and required fields:
- [_hirmos/extensions/system-design-agent/templates/phase-design-cycle/COMPLETED_TEMPLATE.md](../templates/phase-design-cycle/COMPLETED_TEMPLATE.md)
- [_hirmos/extensions/system-design-agent/templates/phase-design-cycle/PAUSED_TEMPLATE.md](../templates/phase-design-cycle/PAUSED_TEMPLATE.md)


## Relationship to public System Design

For normal greenfield System Design, this cycle is required before `system-design-agent:system-design` may surface `completed`.

This cycle runs after the narrowed `system-design-agent:system-design-cycle` has produced system-level design artifacts and after all unresolved gated items that block phase design have been resolved.

If unresolved gated items still materially affect phase boundaries, roadmap grouping, downstream phase-contract shape, or delivery-target feasibility, this cycle must pause rather than present the phase set as governably complete.

If a public System Design run explicitly excludes implementation readiness, the public `system-design` entrypoint may skip this cycle only when it records the scope limitation and does not claim implementation readiness.
