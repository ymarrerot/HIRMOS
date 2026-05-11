# Context, Inputs, and Outputs

This page explains how to think about the most common working surfaces while the framework is running.

The authoritative top-level folder definitions live in [_hirmos/core/authority/framework/top-level-folder-definitions.md](../../core/authority/framework/top-level-folder-definitions.md). This page explains the relationship between those surfaces rather than redefining them independently.

## Inputs
`_hirmos/inputs/<extension-id>/...`

Use inputs for raw runtime materials owned by an extension before normalization.

## Context
`_hirmos/artifacts/context/<extension-id>/...`

Use context for normalized, non-authoritative runtime artifacts that help an extension reason, plan, validate, or track trust state during a run.

## Outputs
`_hirmos/artifacts/outputs/<extension-id>/...`

Use outputs for extension-owned result artifacts and deliverables intended for human consumption, approval, handoff, or external/system consumption.

## How to choose among them

A simple rule of thumb:

- Raw intake belongs in `inputs`
- Normalized working state belongs in `context`
- Produced result surfaces belong in `outputs`

When the artifact becomes an authoritative framework artifact instead of an extension-owned working or result artifact, it may belong in a framework-governed surface such as `_hirmos/artifacts/sot/`, `_hirmos/artifacts/phases/`, `_hirmos/artifacts/prompts/`, or `_hirmos/artifacts/ops/` depending on its role.

For the final folder meaning, always defer to [_hirmos/core/authority/framework/top-level-folder-definitions.md](../../core/authority/framework/top-level-folder-definitions.md).