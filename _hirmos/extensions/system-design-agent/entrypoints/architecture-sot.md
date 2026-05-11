# system-design-agent:architecture-sot

## Execution Contract

### Purpose

Generate or refine _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) as the target structural design for the system.

### Produces

- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)

### Terminal States

- `completed` — allowed only when _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) has been generated or refined and passes the local Spec-backed validation bar.

## Instructions

1. Read and follow `specs/architecture-sot.spec.md` exactly.
2. Use _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`), _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`), staged delivery context when relevant, prototype-derived planning inputs when relevant, and active stack context when core resolves a valid stack package.
3. Produce _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) using the required section structure and rules defined in the Spec.
4. Consume stack guidance only to the extent allowed by the Spec: strengthen architecture realism without turning the artifact into implementation instructions.
5. Do not outrun the approved system definition, contradict upstream planning artifacts, or silently convert assumption-driven architecture direction into fully settled truth.
6. Validate the artifact against the Spec before returning it.

## Output

Return only the final _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`) content.