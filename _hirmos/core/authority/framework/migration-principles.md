# Migration Principles

## Purpose

Define the authoritative framework-wide principles for migrating proven behavior from earlier HIRMOS or predecessor framework forms into the current architecture.

Use this document when deciding whether a capability should be preserved, reshaped, decomposed, or left behind during framework evolution.

## Scope and usage rule

This file owns the framework-wide migration principles.

Use it when:
- deciding how to carry forward proven operational behavior into the new framework
- reviewing whether a refactor preserved the framework's real strengths
- grounding framework-review findings about decomposition quality and migration discipline
- summarizing migration intent in user-facing guidance without silently re-owning the rule

## Guiding principle

The new framework should be the better architectural vehicle.
The earlier framework may still contain proven operational intelligence worth preserving.
Good migration keeps both truths in view at the same time.

## What must be preserved when it is still valid

Preserve the earlier framework's:
- discipline
- planning philosophy
- artifact-driven workflow
- role separation
- lifecycle and governance strength

Do not discard those strengths merely because the newer architecture is more modular.

## Coherent-family principle

Preserve coherent workflow families as coherent extensions unless there is a strong reason to split them.

A good decomposition keeps both:
- top-level coherent workflows
- lower-level reusable units inside those workflows

## Reuse principle

When a lower-level unit is genuinely reusable, preserve it as a reusable public or internal surface instead of burying it inside a larger migration.

## Manual and orchestrated paths

Preserve both:
- orchestrated high-level execution
- manual lower-level execution when tighter operator control is useful

## Public-entrypoint principle

Expose intentional public entrypoints.
Do not turn every internal file into a top-level runnable surface merely because it exists.

## Extension-spec-backed serious workflow principle

Serious workflow entrypoints should usually be backed by extension-local specs that preserve local method, validation, and quality expectations.

## Hooks-are-not-everything principle

Hooks are useful for augmentation.
They should not become the primary model for major workflow orchestration or coherent family composition.

## Related authority and guidance

Related authority files:
- [Framework operating model](./framework-operating-model.md)
- [Framework operating model](./framework-operating-model.md)
- [Cross-folder rules](../shared/cross-folder-rules.md)

Related user-facing guidance may summarize these principles without replacing them.
