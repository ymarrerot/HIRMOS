# Spec-Backed Entrypoints

Use this page to understand the practical relationship between a runnable entrypoint and the deeper governance that may sit behind it. The goal is to help authors choose the right amount of structure for real work without repeating doctrine inline.

Need the canonical rules? See:
- [Extension entrypoints](../../../core/authority/extensions/entrypoints.md)
- [Entrypoint execution contract](../../../core/authority/core/entrypoint-execution-contract.md)
- [Authority surface rules](../../../core/authority/shared/cross-folder-rules.md)

## When a simple entry file is enough

A simple entry file is usually enough when:
- the behavior is tiny
- there is no meaningful artifact contract
- there is no strong local quality bar
- the entrypoint is mostly illustrative

## When stronger local governance is helpful

A deeper governance surface is usually helpful when:
- the entrypoint produces an important artifact
- the entrypoint has non-trivial validation
- the entrypoint belongs to a coherent workflow family
- the entrypoint is reused by higher-level workflows

## Relationship between entrypoint and deeper governance

A public entrypoint is the runnable surface.
A deeper Spec or contract file carries the stronger local method when that extra structure is needed.

Also consider the [Beyond Clear Specs](beyond-clear-specs.md) when the entrypoint should pair clear specs with self-validation, especially if the run also produces a critical surfaced result.

## Why this matters

This keeps the public run surface concise without losing local rigor.
