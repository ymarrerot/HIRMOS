# Public Entrypoints

This page explains how to design an extension's public runnable surface. In practice, public entrypoints are the operational surfaces people use to run governed work during specific SDLC stages or narrower supporting tasks.

Extensions may expose:

- extension-local entry surfaces via `entry` and `entrypoints`;
- user-facing HIRMOS workflow commands via `hirmos_commands`.

## Manifest-declared public command

A manifest-declared public command is what runs when the user runs:

```text
hirmos <command>
```

For regular users, the declared public command should resolve to the highest-level coherent workflow the extension owns.

Examples from the official regular-user workflow:

```text
hirmos requirements      → requirements
hirmos system-design     → system-design
hirmos implementation    → implementation
```

## Named public entrypoints

Named entrypoints are explicit surfaces for narrower work after the command owner is resolved:

```text
hirmos <command>:<entrypoint>
```

Expose lower-level named entrypoints only when they are meaningfully reusable, useful for power users, or needed for governed sub-workflows.

Examples:

```text
hirmos requirements:requirements-sot
hirmos system-design:phase-design-cycle
hirmos implementation:implementation-planning-cycle
```

## SDLC anchor

A good practical question is: what piece of real work should an operator be able to run here?

A public entrypoint may represent:

- a whole governed Requirements step;
- a whole governed System Design step;
- a whole governed Implementation step;
- a narrower producer or planning step;
- a small utility surface used around those stages.

## Design guidance

Keep the public surface intentional.

Expose the highest-level coherent workflow first. Add lower-level public entrypoints only where reuse or operator control clearly benefits the workflow.

Keep implementation-only helpers private.

## Public execution-facing contract

Runnable public entrypoints should be easy to scan during execution. A reader should be able to quickly see:

- Purpose;
- Produces;
- Terminal States.

For serious workflow entrypoints, terminal states must support evidence-backed completed/paused/failed behavior.

## Avoid duplicate lifecycle truth

A friendly public command must not duplicate a large internal cycle spec. Prefer a thin public surface that references or reuses narrower producer/cycle logic where safe.

If keeping both a public default entrypoint and older cycle entrypoints creates drift risk, consolidate or deprecate the older cycle surface.

## Need the deeper rules later?

Use this page for practical design guidance first. When you need the exact extension or Core contract details, use:

- [Beyond Clear Specs](beyond-clear-specs.md)
- [Extension entrypoints](../../../core/authority/extensions/entrypoints.md)
- [Entrypoint execution contract](../../../core/authority/core/entrypoint-execution-contract.md)
- [Command protocol](../../../core/command-protocol.md)
