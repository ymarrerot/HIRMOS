# Cycles and Entrypoints

This page explains the practical relationship between high-level public entrypoints, internal cycles, and lower-level reusable entrypoints.

## Current posture

HIRMOS now prefers a simple regular-user front door:

```text
Requirements → System Design → Implementation
```

The corresponding default public commands are:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

These default public entrypoints may internally reuse narrower cycle or producer logic.

## Public entrypoints

A public entrypoint is a runnable surface exposed by an extension.

A manifest-declared public command is the regular-user command:

```text
hirmos <command>
```

A named public entrypoint is the power-user command:

```text
hirmos <command>:<entrypoint>
```

## Cycles

A cycle is a governed workflow unit. Some cycles remain useful as advanced or reusable surfaces, especially when they are coherent and do not duplicate a higher-level public entrypoint.

Examples of retained advanced/reusable cycles may include:

```text
hirmos system-design:phase-design-cycle
hirmos implementation:implementation-planning-cycle
hirmos implementation:implementation-execution-cycle
```

## What changed

Earlier HIRMOS surfaces sometimes exposed `*-cycle` entrypoints directly as the normal user-facing path. The regular-user workflow now favors default public extension commands and keeps narrower cycle entrypoints for power users only when they avoid duplicate lifecycle truth.

## When to use the default public command

Use the default public command when you want the normal governed path for a lifecycle step:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

## When to use a named cycle

Use a named cycle when you intentionally need:

- tighter control;
- targeted reruns;
- artifact-specific refinement;
- advanced/power-user operation;
- custom composition using known public surfaces.

## Drift rule

Do not preserve an old cycle entrypoint merely for historical reasons.

Keep it only when it can remain self-contained, reusable, and aligned with the default public entrypoint without duplicating behavioral truth.

## Need the deeper rules later?

Use this page for the practical distinction first. When you need the exact extension lifecycle or entrypoint rule, use:

- [Beyond Clear Specs](beyond-clear-specs.md)
- [Extension lifecycle and cycles](../../../core/authority/extensions/lifecycle-and-cycles.md)
- [Extension entrypoints](../../../core/authority/extensions/entrypoints.md)
- [Framework operating model](../../1-use-hirmos/understanding/framework-operating-model.md)
