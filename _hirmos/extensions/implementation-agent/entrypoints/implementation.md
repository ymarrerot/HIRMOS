# implementation-agent:implementation

## Execution Contract

### Purpose

Run the HIRMOS **Implementation** step for Orchestrated Spec-Driven Development.

This is the public Implementation entrypoint. It composes the retained implementation subcycles without duplicating their detailed behavioral contracts:

```text
implementation-agent:implementation-planning-cycle
implementation-agent:implementation-execution-cycle
```

The public step ensures planning exists, preserves the approval boundary after planning, and executes the selected/current phase only after explicit approval.

### Produces

This entrypoint produces or verifies the Implementation outputs governed by `specs/implementation.spec.md`, including planning artifacts, execution evidence, review/repair artifacts, run-scoped trust artifacts, terminal status, and Evidence-backed Review.

### Terminal States

Allowed final states:

- `completed`
- `paused`
- `failed`

State selection, completion validity, pause validity, failure validity, and Evidence-backed Review requirements are governed by `specs/implementation.spec.md`.

## Run-Critical Checklist

Before running, read and follow:

- `specs/implementation.spec.md`
- `specs/implementation-planning-cycle.spec.md`
- `specs/implementation-execution-cycle.spec.md`
- all governing files referenced by those specs

This entrypoint must:

- verify required System Design and selected/current phase artifacts;
- determine the selected/current phase;
- run or perform planning responsibilities when planning is missing or stale;
- pause after new or materially refreshed planning for explicit approval;
- avoid execution from unapproved planning;
- run or perform execution responsibilities only after approval;
- surface Evidence-backed Review when completion is claimed;
- validate the composed Implementation result before surfacing a terminal state.

## Required Terminal Output Templates

- Completed runs must follow [_hirmos/extensions/implementation-agent/templates/implementation/COMPLETED_TEMPLATE.md](../templates/implementation/COMPLETED_TEMPLATE.md).
- Paused runs must follow [_hirmos/extensions/implementation-agent/templates/implementation/PAUSED_TEMPLATE.md](../templates/implementation/PAUSED_TEMPLATE.md).
- Failed runs must follow [_hirmos/extensions/implementation-agent/templates/implementation/FAILED_TEMPLATE.md](../templates/implementation/FAILED_TEMPLATE.md).
- Do not improvise hybrid terminal outputs.

## Execution Sequence

Follow this sequence:

1. Verify required System Design and selected/current phase artifacts.
2. Determine the selected/current phase. If unclear, surface `paused` and request clarification.
3. Determine whether implementation planning artifacts exist and are current enough for the selected/current phase.
4. If planning artifacts are missing or stale, run or perform `implementation-agent:implementation-planning-cycle` responsibilities, then surface `paused` for approval.
5. If planning artifacts exist but are not explicitly approved for execution, surface `paused` and request approval.
6. If planning artifacts are present and approved, run or perform `implementation-agent:implementation-execution-cycle` responsibilities.
7. Surface Evidence-backed Review from actual artifacts, validation results, execution evidence, review findings, bounded repair attempts, unresolved items, and terminal state.
8. Surface exactly one terminal state using the required template.

## Approval Pause Rule

The public Implementation entrypoint must not proceed from planning to execution without explicit Orchestrator approval.

When planning is newly produced or materially refreshed, the normal final state is `paused` with a clear approval request.

## Output

Return the Implementation terminal output.

The surfaced output must include the terminal state, selected/current phase, planning approval status, subcycles performed or intentionally skipped with reason, artifacts produced or verified, Evidence-backed Review where applicable, validation summary, and next-step guidance.
