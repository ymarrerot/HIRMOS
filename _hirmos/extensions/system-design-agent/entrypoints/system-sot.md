# system-design-agent:system-sot

## Execution Contract

### Purpose

Generate or refine _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`) as the authoritative system definition derived from `REQUIREMENTS_SOT.md`.

### Produces

- _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)

### Terminal States

- `completed` — allowed only when _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`) has been generated or refined and passes the local Spec-backed validation bar.

## Instructions

1. Read and follow `specs/system-sot.spec.md`.
2. Gather and use the strongest available governing inputs for `SYSTEM_SOT.md`, including:
   - _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)
   - staged delivery context when relevant
   - prototype-derived requirements impact when relevant
   - other project planning inputs that materially define what the system is
3. Build the system definition strictly from those governing inputs.
4. Keep the result at the system-definition level:
   - no implementation details
   - no tech stack
   - no architecture
5. Validate the result against the Spec before finalizing.
6. If validation finds gaps, ambiguity, invented behavior, or architecture leakage, fix the artifact before returning it.

## Output

Return only final _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`) content.