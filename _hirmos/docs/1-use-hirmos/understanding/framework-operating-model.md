# Framework Operating Model

Use this page when you want the fast mental model for how HIRMOS behaves in practice. It is especially useful when you are trying to place HIRMOS in a familiar software delivery flow without dropping into deeper doctrine too early.

## Quick mental model

HIRMOS operates through four layers:

1. bootstrap
2. core protocol
3. extension workflows
4. runtime surfaces

The Orchestrator sits above those layers and remains the human authority deciding what to run, what to accept, and when to continue.

## Public lifecycle model

The regular-user workflow is:

```text
Requirements → System Design → Implementation
```

This is the simple user-facing path. It does not remove the deeper mechanics underneath it.

### Requirements

The Requirements step turns user goals, notes, project context, user stories, files, prototypes, and constraints into requirements artifacts suitable for system design.

Use real HIRMOS artifact names where they are clear. For example, requirements work should produce or update `REQUIREMENTS_SOT.md` and contribute assumptions, open questions, and unresolved items to the existing unresolved-item governance path.

### System Design

The System Design step turns requirements into design artifacts such as system model, architecture, staged phases, and unresolved decision surfaces.

Typical HIRMOS artifacts in this area include `SYSTEM_SOT.md`, `ARCHITECTURE_SOT.md`, and `PHASES_SOT.md`.

### Implementation

The Implementation step executes work in bounded, reviewable units. It should include planning, approval pauses when required, validation, repair or pause handling, and Evidence-backed Review.

Evidence-backed Review means the run explains what happened, what checks ran, what passed or failed, what remains unresolved, and whether the run completed, paused, or failed.

## How this maps to familiar SDLC work

- bootstrap prepares the framework before real project work begins;
- extension workflows usually carry the heaviest SDLC work, such as requirements, system design, implementation, or presentation-oriented support;
- runtime surfaces preserve the artifacts and evidence produced during those stages;
- the Orchestrator stays responsible for review, steering, and approval across the full flow.

## Why this matters

The framework stays governable because it separates:

- framework mechanics;
- workflow behavior;
- project authority artifacts;
- execution evidence.

This keeps the Core small while serious behavior lives in coherent extensions.

## Command path

The regular-user workflow is backed by official extension commands:

```text
Requirements   → requirements-agent
System Design  → system-design-agent
Implementation → implementation-agent
```

Use the supported `hirmos <command>...` command examples in the quickstart. Other command forms are not part of the current public workflow.

## Go next

- **See how work moves through the framework:** open the [Workflow diagram](workflow-diagram.md).
- **Use HIRMOS:** go to [Use HIRMOS in 3 Steps](../getting-started/use-hirmos-in-3-steps.md).
- **Browse installed extensions in this project:** go to the [Installed extensions guide](../../../extensions/README.md).
- **Go back to framework guidance:** return to [Framework guidance](../../3-extend-contribute/framework/README.md).

## Optional reading

- **Need the canonical rule later?** See the [framework operating model authority](../../../core/authority/framework/framework-operating-model.md).
