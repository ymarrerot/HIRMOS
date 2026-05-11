# implementation-agent:prompt-planning

## Execution Contract

### Purpose

Generate or refine one bounded prompt-planning artifact for the target implementation task or prompt scope.

### Produces

- one prompt-planning artifact, typically a `PROMPT_PLAN.md` or equivalent prompt-planning output required by the local Spec

### Terminal States

- `completed` — allowed only when the target prompt-planning artifact has been generated or refined and passes the local Spec-backed validation bar.

## Instructions

1. Read and follow `specs/prompt-planning.spec.md`.
2. Use the strongest available governing inputs, including:
   - the selected phase contract under `_hirmos/artifacts/phases/`
   - _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
   - relevant _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)
   - relevant _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)
   - staged delivery context when relevant
   - the current approved implementation scope
   - [_hirmos/extensions/implementation-agent/specs/ENGINEERING_STANDARDS.md](../specs/ENGINEERING_STANDARDS.md) when engineering discipline materially affects decomposition, verification, or failure containment
   - active stack `architecture_guidance` and `engineering_standards` when they materially affect decomposition or delivery boundaries
3. Detect whether the applicable phase contract or `PHASES_SOT.md` defines a Delivery Boundary.
4. Analyze the phase, assess complexity, choose the decomposition strategy, and produce a prompt plan that covers 100% of the relevant phase scope.
5. Define prompt sequence, dependencies, execution order, parallelism rules, failure containment, and validation strategy.
6. Validate the result against the local Prompt-Plan quality bar, delivery-boundary rules when relevant, and coverage/coherence expectations before returning it.

## Output

Return ONLY the final Prompt Plan.