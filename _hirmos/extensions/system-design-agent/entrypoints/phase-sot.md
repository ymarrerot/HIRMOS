# system-design-agent:phase-sot

## Execution Contract

### Purpose

Generate or refine one phase contract artifact aligned to the authoritative planning baseline.

### Produces

- one `_hirmos/artifacts/phases/phase_<NN>_<slug>_SOT.md` artifact for the target phase

### Terminal States

- `completed` — allowed only when the target phase artifact has been generated or refined and passes the local Spec-backed validation bar.

## Instructions

1. Read and follow `specs/phase-sot.spec.md`.
2. Use _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`), _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`), and _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) as the governing upstream planning contract.
3. Identify the target phase and map its responsibilities, dependencies, and unlocked outcomes.
4. Translate that phase into a deterministic, complete, enforceable, self-sufficient phase contract with explicit boundaries, workflows, observability, tests, and exit criteria.
5. Validate the result against the local quality bar and fix any issue before returning it.

## Output

Return only the final `phase_<N>_<slug>_SOT.md` content.