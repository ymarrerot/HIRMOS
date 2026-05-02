# Cycles and Entrypoints

This page explains the practical difference between high-level cycles and lower-level public entrypoints. In SDLC terms, cycles are usually the safer default when you want a governed workflow for a whole stage of work, while lower-level entrypoints are more useful for targeted reruns or narrower tasks.


## Why cycles matter

A cycle is a high-level governed workflow entrypoint.

Cycles are usually the safest default for real work because they often:
- load the right governing context
- orchestrate the right lower-level steps
- preserve the right trust artifacts
- pause honestly when important decisions are required

## SDLC anchor

A useful shortcut is to think of cycles as the workflow surfaces that usually own a larger SDLC step, such as requirements grounding, design, planning, implementation planning, or execution. Lower-level entrypoints are usually better when you only need to rerun one unit inside that stage.

## Naming pattern

High-level governed workflows usually use `-cycle` in the public entrypoint name.

Lower-level reusable workflows usually use narrower names without `-cycle`.

## When to use a cycle

Prefer a cycle when you want:
- the default governed path
- full trust surfaces
- integrated pause/completion handling
- less manual orchestration

## When to use a lower-level entrypoint

Use a lower-level entrypoint when you intentionally need:
- tighter control
- targeted reruns
- artifact-specific refinement
- custom composition using known public surfaces

## Need the deeper rules later?

Use this page for the practical distinction first. When you need the exact extension lifecycle or entrypoint rule, use:
- [Beyond Clear Instructions](./beyond-clear-instructions.md) when a cycle or entrypoint should pair clear instructions with self-validation, and when it also needs stronger synthesis or surfaced-output discipline
- [Extension lifecycle and cycles](../../core/authority/extensions/lifecycle-and-cycles.md)
- [Extension entrypoints](../../core/authority/extensions/entrypoints.md)
- [Framework operating model](../framework/framework-operating-model.md)
