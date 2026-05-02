# Public Entrypoints

This page explains how to design an extension's public runnable surface. In practice, public entrypoints are the operational surfaces people use to run governed work during specific SDLC stages or narrower supporting tasks.


Extensions may expose:
- one default public entrypoint via `entry`
- zero or more named public entrypoints via `entrypoints`

## SDLC anchor

A good practical question is: what piece of real work should an operator be able to run here? For example, a public entrypoint may represent a whole governed design cycle, a narrower planning step, an implementation support task, or a small utility surface used around those stages.

## Design guidance

Keep the public surface intentional.

Expose lower-level public entrypoints only when they are meaningfully reusable or when giving the operator finer control is genuinely helpful.

Keep implementation-only helpers private.

## Practical pattern

A good first pattern is:
- expose the highest-level coherent workflow first
- add lower-level public entrypoints only where reuse or operator control clearly benefits

## Public execution-facing contract

Runnable public entrypoints should be easy to scan during execution.
A reader should be able to quickly see:
- what the entrypoint is for
- what it produces
- how it can finish

## Need the deeper rules later?

Use this page for practical design guidance first. When you need the exact extension or Core contract details, use:
- [Beyond Clear Instructions](./beyond-clear-instructions.md) for entrypoints that should pair clear instructions with self-validation, and especially for ones that also need governed synthesis or stronger output-shape governance
- [Extension entrypoints](../../core/authority/extensions/entrypoints.md)
- [Entrypoint execution contract](../../core/authority/core/entrypoint-execution-contract.md)
- [Command protocol](../../core/command-protocol.md)
