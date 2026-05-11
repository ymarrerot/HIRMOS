# Extension Validation

## Purpose

Define the framework-wide extension doctrine for extension-facing validation expectations.

Use this authority file when deciding:
- what a well-formed extension should make explicit
- how local self-validation relates to framework validation
- what should be visible in serious validation surfaces

For Core-local validation behavior, see:
- [Validation and ordering](../core/validation-and-ordering.md)
- [Extension manifest authority](../core/extension-manifest-authority.md)

## Role of validation from the extension side

Validation exists to make contract mistakes visible early.

From the extension side, validation should reinforce:
- explicit public surfaces
- coherent declarations
- clear boundaries between public and private files
- honest artifact and dependency expectations

Validation should help an extension stay governable rather than merely pass a checklist.

## Relationship to Core validation

The Core remains authoritative for framework validation behavior and enforcement.

From the extension side, the important doctrine is:
- make public surfaces explicit
- keep declarations coherent
- do not rely on accidental structure
- make serious local validation expectations visible when the extension owns them

## What serious extension validation should make explicit

When an extension owns a meaningful local quality bar or validation burden, that expectation should be visible in the extension's own stronger local surfaces.

Examples include:
- artifact quality expectations
- required local decision checks
- completion criteria that materially affect trust
- local consistency checks that the Core cannot own generically

Do not hide serious extension-local validation only inside ad hoc implementation details.

## Beyond Clear Specs, surfaced outputs, and self-validation

For the canonical Beyond Clear Specs pattern for trust-sensitive synthesis and surfaced outputs, see:
- [Beyond Clear Specs](./beyond-clear-specs.md#required-controls)

This doctrine is especially relevant when missing contributions, dropped branches, omitted sections, overstated completion claims, or vague summaries could mislead the Orchestrator, a reviewer, or an API consumer.

## Public versus private clarity

A healthy extension makes it obvious which files are:
- public runnable surfaces
- private support files
- declaration surfaces
- deeper local contract or method surfaces

Validation benefits from explicitness. Ambiguous structures create avoidable failures.

## Relationship to reviewability

Good validation supports reviewability.

If an extension claims an important artifact or public workflow, it should make the validation expectations legible enough for a reviewer to understand what "good enough" means.

## Review tests

When reviewing extension validation posture, ask:
- Are public surfaces explicit?
- Are declarations coherent and honest?
- Is serious local validation visible where the extension owns it?
- Does the extension avoid relying on accidental or ambiguous structure?
- Does the validation posture improve reviewability rather than hide it?
