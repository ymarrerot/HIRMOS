# Unresolved decisions

Unresolved decisions are one of the most common failure points in AI-assisted development.

They include assumptions, open questions, tradeoffs, missing constraints, and decisions that must be resolved before safe progress.

## Why unresolved decisions matter

Complex software work needs a traceable record of what was decided, what was deferred, and what still blocks progress.

That is true with or without AI. An assumption made during planning can become architecture. A tradeoff that was never surfaced can become implementation. By the time someone notices, reversing it may be expensive.

AI-assisted work makes this more urgent because decisions can be made quickly, implicitly, and confidently in a single response.

When unresolved decisions are not governed, the agent often chooses defaults silently.

Those defaults may become architecture, implementation, tests, documentation, and user-facing behavior before anyone realizes the decision was never approved.

## What Orchestrated SDD does differently

Orchestrated SDD treats unresolved decisions as first-class workflow material.

The workflow should:

- capture assumptions and open questions where they originate;
- preserve them in durable artifacts;
- reconcile them before completion;
- classify whether they are safe, risky, or gating;
- pause when a gated decision blocks trustworthy progress;
- record decisions after the user or Orchestrator resolves them.

The goal is simple: decisions that can materially affect what gets built should not stay hidden in prose.

## Project-level unresolved inventory

HIRMOS uses a project-level unresolved-item inventory as the canonical place to coordinate unresolved items across Requirements, System Design, presentation inputs, prototypes, and other extension outputs.

The project-level inventory lives under:

```text
_hirmos/artifacts/context/project/
```

The key artifact is:

```text
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
```

Each source of unresolved items updates its own artifact-scoped section inline while the work is happening.

That inline update rule matters. It prevents the common failure where an agent acknowledges open questions, promises to track them later, and then continues without preserving them.

## The simple rule

If an unresolved decision can materially affect what gets built, it must be preserved, classified, and either resolved or carried forward with visible risk.

That is how Orchestrated SDD prevents hidden assumptions from quietly becoming the system.
