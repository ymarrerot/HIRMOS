# Extension Hooks

## Purpose

Define the framework-wide extension doctrine for exposing hooks, subscribing to hooks, and designing hook seams that remain governed, visible, and bounded.

Use this authority file when deciding:
- whether an extension should expose a hook
- whether an extension should subscribe to a hook
- what makes a healthy hook seam
- what hook behavior must not try to do

For Core-local hook loading and execution behavior, see:
- [Hook execution control](../core/hook-execution-control.md)
- [Extension manifest authority](../core/extension-manifest-authority.md)

## Role of hooks

Hooks are bounded extension-coordination surfaces.

They exist so one extension can augment another extension's declared workflow seams without replacing the owning workflow or hiding authority.

Hooks should add governed extension points, not blur ownership.

## When to expose a hook

Expose a hook when another extension may reasonably need to:
- inspect inputs before a step runs
- add bounded preprocessing or enrichment
- generate derived supporting artifacts
- contribute validation or reporting
- attach optional behavior at a real workflow seam

Do not expose hooks merely to appear flexible.

A hook should correspond to a seam a human can explain clearly.

## When to subscribe to a hook

Subscribe to a hook when your extension is adding bounded behavior at a declared seam and does not need to replace the owning extension's workflow.

If the behavior would effectively replace or hijack the owning workflow, create a separate runnable extension instead of using a hook.

## Real seam quality

A healthy hook seam is one where a human can explain:
- what is happening at that point in the workflow
- why optional extension behavior may help there
- what the subscriber is allowed to contribute
- what the hook is not meant to override

Hooks should be placed at real workflow seams, not arbitrary internal lines.

## Bounded hook behavior

For Hook System v1, prefer bounded additive behavior.

Do not use hooks to:
- bypass governance
- hide major behavior changes
- silently replace the owning extension's local method
- move meaningful authority out of the owning workflow without a declared public surface

## Visibility and traceability

Material hook participation should remain visible in traces and reporting.

Hook behavior should enrich the run in a way that remains legible rather than creating mysterious magic.

## Hook naming from the extension side

Hook naming should reveal:
- the owning extension
- the workflow seam
- the timing of the seam

Names should stay boring, descriptive, and easy to reason about.

For broader naming doctrine, see:
- [Extension naming conventions](./naming-conventions.md)

## Relationship to manifests

The manifest is authoritative for declaring:
- hooks this extension exposes
- hook subscriptions this extension registers

This authority file governs the extension-side doctrine for when and why those declarations are healthy.

For manifest authoring doctrine, see:
- [Extension manifests](./manifests.md)

## Review tests

When reviewing hook usage, ask:
- Is the hook seam real and explainable?
- Is the hook being used for bounded augmentation rather than replacement?
- Would a separate runnable extension be healthier than this subscription?
- Is the effect visible enough in traces and reporting?
- Does the owning workflow retain clear authority?
