# Extension Entrypoints

## Purpose

Define the framework-wide extension doctrine for public entrypoints, higher-level cycles, lower-level runnable surfaces, and the relationship between an entrypoint and deeper local governance.

Use this authority file when deciding:
- what should be publicly runnable
- what should remain private
- when a higher-level cycle should be the governed default
- when a lower-level entrypoint is appropriate
- how a runnable surface should relate to deeper extension-local specs

For Core-local resolution and execution behavior, see:
- [Entrypoint execution contract](../core/entrypoint-execution-contract.md)
- [Command protocol](../../../core/command-protocol.md)

## Public runnable surface

An extension's public runnable surface is the set of entrypoints the Orchestrator is expected to run directly.

Public entrypoints should be:
- intentionally chosen
- easy to explain
- stable enough to rely on
- narrow enough to avoid leaking internal helpers as public contract

Do not expose internal support files merely because they exist.

## Default entrypoint versus named entrypoints

The default entrypoint should usually represent the best governed default path for the extension.

Named public entrypoints are appropriate when they offer:
- materially different public workflows
- useful operator control
- bounded reusable lower-level surfaces
- clearly separable artifact-producing runs

Do not multiply public entrypoints without a clear public reason.

## Higher-level cycles and lower-level entrypoints

A cycle is a high-level governed workflow entrypoint.

Prefer a cycle as the default public path when the work benefits from:
- coordinated multi-step execution
- trust artifact preservation
- integrated pause and completion handling
- the safest governed default for serious work

Lower-level entrypoints are appropriate when they intentionally expose:
- tighter operator control
- targeted reruns
- narrower artifact refinement
- bounded reusable workflow units

Cycles should be the governed default when that default materially improves correctness, trust, or usability.

## Public versus private boundary

A file should be public only when the Orchestrator or operator should reasonably run it directly.

A file should remain private when it is primarily:
- a helper
- a supporting artifact transform
- a local sub-step
- implementation support for a larger public workflow

A small public surface with stronger private support is healthier than a broad public surface with unclear boundaries.

## Relationship to extension-local specs

An entrypoint is the runnable public surface.

When the behavior is serious enough to need a stronger local quality bar, validation layer, scoring/reporting mechanics, or explicit completion contract, the deeper local method should live in extension-local specs rather than being overloaded into the public entrypoint file.

This keeps the public run surface concise while preserving rigor.

## Beyond Clear Instructions when applicable

For the canonical framework pattern about when clear instructions are not enough, and when governed synthesis structures, surfaced-output templates, strict self-validation, and fail-closed behavior should be added, see:
- [Beyond Clear Instructions](./beyond-clear-instructions.md#when-this-applies)

Use that doctrine when an entrypoint performs trust-sensitive synthesis, especially across multiple producers, multiple execution branches, or main-path plus hook contributions.

## Public execution-facing contract

A public entrypoint should expose enough execution-facing contract for a run to be understandable.

It should make clear, at the appropriate level:
- what the run is for
- what key inputs or parameters matter
- what major artifacts or outcomes it is responsible for
- what terminal states or decision points materially matter

It should not try to become the complete owner of all deeper local method when a stronger extension-local spec exists.

## Naming guidance for cycles and entrypoints

Higher-level governed workflows usually benefit from names that clearly signal their role, often including `-cycle` when that improves operator understanding.

Lower-level entrypoints should use narrower names that reveal their actual public purpose.

For broader extension naming doctrine, see:
- [Extension naming conventions](./naming-conventions.md)

## Review tests

When reviewing extension entrypoints, ask:
- Is the public surface intentionally small?
- Is the default public path the best governed default?
- Are lower-level public entrypoints exposed only when they offer real public value?
- Are private helper files kept private?
- Is deeper local method kept in extension-local specs when needed instead of being overloaded into entrypoint files?
