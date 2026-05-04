# Overview

HIRMOS helps you turn intent into governed, reviewable AI-assisted engineering work without needing to learn the whole framework first. For a beginner, success means getting one useful command path working, seeing the generated artifacts, and understanding what to do next.

## The fastest useful way to think about the framework

If you are new to HIRMOS, keep this mental model in mind:

1. **Bootstrap the framework**
   - Ask your AI tool to read and follow `_hirmos/HIRMOS_CORE.md`.
2. **Start with a high-level entrypoint when one exists**
   - When a high-level cycle exists, start there instead of stitching together lower-level commands manually.
3. **Let the framework write reviewable artifacts**
   - Inputs, context, source-of-truth, phase contracts, prompts, and related artifacts exist so work stays reviewable.
4. **The Orchestrator stays responsible for key decisions**
   - The framework is structured, not autonomous. The Orchestrator chooses what to run, reviews what happened, and resolves important decisions.

## The most important beginner rule

Use the highest-level governed entrypoint that fits the job.

For example, prefer a high-level cycle exposed by an installed workflow extension over manually invoking lower-level entrypoints unless you intentionally need tighter control.

## What you can ignore for now

At the beginning, you do not need to understand:
- the full folder taxonomy
- the extension-local specs lanes
- deeper core mechanics
- extension authoring details

## Go next

- Continue to [Quickstart](./quickstart.md) if you are staying on the canonical getting-started path.
- Go back to the [Getting started guide](./README.md) if you want the full onboarding path at a glance.

## Optional reading

- [Release packaging](../core/release-packaging.md) if you plan to package or share the framework.
