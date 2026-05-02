# Framework Operating Model

Use this page when you want the fast mental model for how HIRMOS behaves in practice. It is especially useful when you are trying to place HIRMOS in a familiar software delivery flow without dropping into deeper doctrine too early.


## Quick mental model

HIRMOS operates through four layers:
1. bootstrap
2. core protocol
3. extension workflows
4. runtime surfaces

The Orchestrator sits above those layers and remains the human authority deciding what to run, what to accept, and when to continue.

## How this maps to familiar SDLC work

- bootstrap prepares the framework before real project work begins
- extension workflows usually carry the heaviest SDLC work, such as requirements grounding, design, planning, implementation, or presentation-oriented support
- runtime surfaces preserve the artifacts and evidence produced during those stages
- the Orchestrator stays responsible for review, steering, and approval across the full flow

## Why this matters

The framework stays governable because it separates:
- framework mechanics
- workflow behavior
- project authority artifacts
- execution evidence

This keeps the core small while serious behavior lives in coherent extensions.



## Go next

- **See how work moves through the framework:** open the [Workflow diagram](./workflow-diagram.md).
- **Browse installed extensions in this project:** go to the [Installed extensions guide](../../extensions/README.md).
- **Go back to framework guidance:** return to [Framework guidance](./README.md).

## Optional reading

- **Need the canonical rule later?** See the [framework operating model authority](../../core/authority/framework/framework-operating-model.md).
