# system-design-agent:phases-sot

## Execution Contract

### Purpose

Generate or refine _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`) as the authoritative phased delivery breakdown for the current planning baseline.

### Produces

- _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)

### Terminal States

- `completed` — allowed only when _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`) has been generated or refined and passes the local Spec-backed validation bar.

## Instructions

1. Read and follow `specs/phases-sot.spec.md`.
2. Use _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`), _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`), _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`), staged delivery context when relevant, and pending confirmation items when they materially affect roadmap structure.
3. Design the full phase roadmap, not only the earliest delivery target.
4. Preserve the distinction between declared and proposed delivery targets when relevant.
5. Define a complete, non-overlapping phase structure strong enough to support downstream `phase-sot` contract generation.
6. Validate the output against the Spec's local quality bar and self-validation rules before finalizing.

## Output

Return only final _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`) content.