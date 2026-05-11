# requirements-agent:requirements-sot

## Execution Contract

### Purpose

Generate or refine _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`) as the authoritative requirements baseline for the system.

### Produces

- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)

### Terminal States

- `completed` — allowed only when _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`) has been generated or refined and passes the local Spec-backed validation bar.

## Instructions

1. Read and follow `specs/requirements-sot.spec.md` exactly.
2. Gather and normalize all relevant requirements inputs provided by the Orchestrator.
3. When present, treat the following as first-class upstream intake artifacts:
   - _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`)
   - _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`)
4. Handle prototype-derived intake exactly as defined by the Spec:
   - direct single-prototype intake when one prototype SoT exists
   - normalized set-plus-individual intake when multiple prototype SoTs exist with a set artifact
   - inconsistent-state handling when multiple prototype SoTs exist without a set artifact
5. Generate or refine _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`) with explicit flows, clear boundaries, and no architecture or implementation leakage.
6. Perform the mandatory self-validation defined by the Spec.
7. If local validation fails, refine and revalidate before finalizing.

## Output

Return ONLY the final _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`) content.

No extra commentary.