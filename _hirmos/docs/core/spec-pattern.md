# Spec Pattern

A **Spec** is the canonical local method or contract backing a serious workflow entrypoint.

A Spec is stronger than a casual instruction file. It centralizes what the workflow unit is for, what it needs, what it produces, and how quality is judged locally.

## When to use a Spec

Use a Spec when an entrypoint needs more than a tiny one-off instruction file.

Typical signals:

- the entrypoint produces an important artifact
- the entrypoint has a real local quality bar
- the entrypoint requires validation or repair logic
- the entrypoint is reused by a higher-level workflow
- the entrypoint belongs to a coherent extension family

## How a Spec differs from other files

### Spec
Defines the local method/contract.

### README
Explains the extension to humans and LLMs at a package level.

### Prompt or entrypoint file
Acts as the executable wrapper or public runnable surface.

### Hook
Augments another extension's behavior.

## Recommended Spec contents

A good Spec usually defines:

- purpose
- required inputs
- output artifact(s)
- constraints and anti-patterns
- local quality bar
- validation rules
- completion criteria
- downstream handoff notes

## Decision checkpoints in Specs

Serious Specs may define decision checkpoints when unresolved items materially affect downstream authoritative truth, delivery feasibility, or contract shape. A decision checkpoint should state what triggers the checkpoint, what the Orchestrator must decide, what outcomes are allowed, and how assumption-scoped outcomes remain distinct from source-confirmed truth.

When a Spec defines a decision checkpoint, it should also define:

- the pause trigger
- the required paused output sections
- whether **Proposed Orchestrator direction** is required
- the required **Continuation options**
- whether the public runnable wrapper must use an active runtime identity in chat-facing pause/final blocks


The original framework already preserved uncertainty and allowed clarification when needed; this pattern makes that governance more explicit.

## Why Specs matter

Specs preserve local governance.

They let a coherent extension keep strong internal discipline without forcing that discipline into the global core.

Specs play a role similar to the original framework's strongest guide files: they centralize local method, constraints, quality bar, and validation.


For the authoritative role split among README files, docs, entrypoints, Specs, templates, hooks, manifests, and internal notes, see [_hirmos/core/authority/extensions/extension-document-roles.md](../../core/authority/extensions/extension-document-roles.md).