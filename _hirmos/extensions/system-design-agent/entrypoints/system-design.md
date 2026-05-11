# system-design-agent:system-design

## Execution Contract

### Purpose

Run the HIRMOS **System Design** step for Orchestrated Spec-Driven Development.

This is the public System Design entrypoint. It composes the retained System Design subcycles without duplicating their detailed behavioral contracts:

```text
system-design-agent:system-design-cycle
system-design-agent:phase-design-cycle
```

Requirements are owned by `requirements-agent`. This entrypoint consumes completed Requirements artifacts and does not produce Requirements artifacts.

### Produces

This entrypoint produces or verifies the System Design outputs governed by `specs/system-design.spec.md`, including system-level SoTs, phase-level artifacts, unresolved-item governance artifacts, and run-scoped trust artifacts.

### Terminal States

Allowed final states:

- `completed`
- `paused`
- `failed`

State selection, completion validity, pause validity, and terminal-state composition are governed by `specs/system-design.spec.md`.

## Run-Critical Checklist

Before running, read and follow:

- `specs/system-design.spec.md`
- `specs/system-design-cycle.spec.md`
- `specs/phase-design-cycle.spec.md`
- all governing files referenced by those specs

This entrypoint must:

- require usable Requirements outputs before System Design proceeds;
- never regenerate Requirements;
- run or perform the narrowed `system-design-cycle` responsibilities;
- pause before phase design if unresolved gated items block honest phase design;
- run or perform `phase-design-cycle` for normal greenfield implementation readiness;
- validate the composed System Design result before surfacing a terminal state.

## Required Terminal Output Templates

- Completed runs must follow [_hirmos/extensions/system-design-agent/templates/system-design/COMPLETED_TEMPLATE.md](../templates/system-design/COMPLETED_TEMPLATE.md).
- Paused runs must follow [_hirmos/extensions/system-design-agent/templates/system-design/PAUSED_TEMPLATE.md](../templates/system-design/PAUSED_TEMPLATE.md).
- Failed runs may use the paused template structure with `failed` run state until a dedicated failed template is introduced.
- Do not improvise hybrid terminal outputs.

## Execution Sequence

Follow this sequence:

1. Verify required Requirements outputs, especially `_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`.
2. If Requirements outputs are missing or unusable, surface `paused` and direct the Orchestrator to run or repair `hirmos requirements`.
3. Run or perform the narrowed `system-design-agent:system-design-cycle` responsibilities.
4. Evaluate gated unresolved items that would block phase design.
5. If gated blockers remain, surface `paused`; do not run phase design yet.
6. If no gated blockers prevent phase design, run or perform `system-design-agent:phase-design-cycle`.
7. Run final System Design validation across Requirements inputs, system-level artifacts, phase artifacts, unresolved-item outcomes, hooks, and runtime trust artifacts.
8. Surface exactly one terminal state using the required template.

## Phase Design Requirement

For normal greenfield System Design, `phase-design-cycle` is required before this entrypoint may surface `completed`.

The only exception is a run scope that explicitly excludes implementation readiness. In that case, the surfaced output must record the limitation and must not claim implementation readiness.

## Output

Return the System Design terminal output.

The surfaced output must include the terminal state, artifacts produced or verified, Requirements artifacts consumed, subcycles performed or intentionally skipped with reason, unresolved-item summary, validation summary, and next-step guidance.

If completed, the next step is:

```text
hirmos implementation
```
