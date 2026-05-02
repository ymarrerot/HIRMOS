# HIRMOS Documentation

This is the main user-facing documentation hub inside the framework install surface. Start with the lightest path that fits your goal, then go deeper only when you need more precision.

## First-time users

If you are new to HIRMOS, start with the [Getting started guide](./getting-started/README.md). That is the canonical low-cognitive-load onboarding path from first bootstrap to first meaningful run. Stay in that lane until it tells you to leave it.

## After getting started

Once you finish the [Getting started guide](./getting-started/README.md), choose **one** next move based on what you need right now. You do not need to read all of these lanes in parallel:

- [Discover available extensions at hirmos.dev](https://hirmos.dev) — use this when you are deciding what to install next
- [Browse extensions already installed in this project](../extensions/README.md) — use this when you want to work with what is already available locally
- [Understand the framework](./framework/README.md) — use this when you want the broader HIRMOS operating model
- [Operate serious runs safely](./orchestrator/operator-playbook.md) — use this when you are already running governed workflows

## Broader docs lanes

These lanes live side by side in the repo, but they are not parallel reading assignments. Pick the one that matches the question you have right now, then leave the others alone until you actually need them. This section is intentionally denser than the front door because it is for users who already finished getting started and now have a more specific question.

### I want the practical framework model first
Start here if you want the bigger picture before the operational detail.

- [Conceptual diagram](./framework/conceptual-diagram.md) — what the framework is
- [Workflow diagram](./framework/workflow-diagram.md) — how work moves through it
- [Framework operating model](./framework/framework-operating-model.md) — the operating model in practice
- [Framework operating model](./framework/framework-operating-model.md) — how authority and reviewability are preserved
- [Source-of-truth model](./framework/source-of-truth-model.md) — how the framework separates authority from working context
- [Context, inputs, and outputs](./framework/context-inputs-outputs.md) — where runtime materials live and why
- [Cycles and entrypoints](./extensions/cycles-and-entrypoints.md) — why cycles are the default command surface
- [Framework stacks](./framework/stacks.md) — how stack awareness works across the framework

### I want deeper framework mechanics
Use this lane only when a real usage question pushes you there. It is not part of the normal first-use path.

- [Core architecture](./core/architecture.md) — what the core owns and what it must not own
- [Core command protocol](./core/command-protocol.md) — how commands are interpreted
- [Loading and resolution](./core/loading-and-resolution.md) — how extension surfaces are resolved
- [Runtime surfaces](./framework/runtime-surfaces.md) — how governed runtime surfaces are meant to be used
- [Extension manifest](./core/extension-manifest.md) — extension manifest rules
- [Hook System v1](./core/hook-system-v1.md) — Hook System v1 overview
- [Core stacks](./core/stacks.md) — stack package and stack-resolution mechanics
- [Release packaging](./core/release-packaging.md) — packaging and release expectations

### I want to operate the framework safely
Use this lane when you are already running serious workflows and need trust guidance.

- [Operator playbook](./orchestrator/operator-playbook.md) — operator responsibilities and practical guidance
- [Decision checkpoints](./orchestrator/decision-checkpoints.md) — how to handle pause points and decisions
- [Cycle status and trust](./orchestrator/cycle-status-and-trust.md) — how to interpret completion states and trust surfaces
- [Optional paused-cycle example](./examples/system-design-agent-paused-cycle-example.md) — an example from one marketplace workflow extension, not a Core requirement

### I want to build or extend extensions
Use this lane only if you want to author reusable framework capabilities. It is not the normal next step after getting started. If you want to choose among extensions for real project work, use the [Installed extensions guide](../extensions/README.md) instead.

- [Extensions overview](./extensions/overview.md) — extension-authoring mental model
- [Creating your first extension](./extensions/creating-your-first-extension.md) — first runnable extension path
- [Public entrypoints](./extensions/public-entrypoints.md) — public entrypoint responsibilities
- [Spec-backed entrypoints](./extensions/spec-backed-entrypoints.md) — how serious entrypoints are governed
- [Hooks authoring](./extensions/hooks-authoring.md) — how to expose and consume hooks
- [Reusing existing extensions](./extensions/reusing-existing-extensions.md) — compose existing extension surfaces
- [Extending existing extensions](./extensions/extending-existing-extensions.md) — extend behavior without forking when possible
- [Stack consumption](./extensions/stack-consumption.md) — how extensions consume stack surfaces cleanly

### I want examples and reference material
Use these only when you already know what category of thing you are looking for. They are support material, not the main guided path.

- [Examples](./examples/) — concrete example structures and paused-run examples
- [Glossary](./framework/glossary.md) — key framework terms and where to go deeper

## Documentation structure

- `getting-started/` — the canonical first-time-user onboarding lane
- `framework/` — framework-wide user-facing mental models and guidance
- `core/` — user-facing guidance for understanding the core and its mechanics
- `orchestrator/` — human authority, checkpoints, and trust interpretation
- `extensions/` — extension design and authoring guidance
- `examples/` — concrete examples used for orientation and reuse

Use this docs hub when you intentionally want to leave the getting-started path and browse broader user-facing guidance. Use the [_hirmos install-surface guide](../README.md) when you want the broader map inside a project.

## Canonical rules when you need them

Use docs for onboarding and practical use. Use the authority lane only when you need authoritative rules.

- [Framework authority](../core/authority/framework/)
- [Core authority](../core/authority/core/)
- [Extension authority](../core/authority/extensions/)
- Extension specs inside each installed extension's local `specs/` folder
