# Overview

HIRMOS helps you turn intent into governed, reviewable AI-assisted engineering work without needing to learn the whole framework first.

HIRMOS is an open modular framework for Orchestrated Spec-Driven Development. It treats specs as essential, but not sufficient by themselves.

```text
SDD brings the spec-first inner loop.
HIRMOS brings the governed orchestration layer.
```

## The fastest useful way to think about the framework

If you are new to HIRMOS, keep this mental model in mind:

```text
Requirements → System Design → Implementation
```

1. **Requirements**
   - Tell HIRMOS what you need to build using prompts, notes, project context, user stories, files, prototypes, or constraints.
   - HIRMOS should turn that input into requirements artifacts such as `REQUIREMENTS_SOT.md`.
2. **System Design**
   - HIRMOS turns requirements into system design artifacts such as `SYSTEM_SOT.md`, `ARCHITECTURE_SOT.md`, and `PHASES_SOT.md`.
   - HIRMOS should surface unresolved decisions instead of silently guessing.
3. **Implementation**
   - HIRMOS implements in bounded, reviewable units.
   - Implementation should include validation and Evidence-backed Review before work is treated as complete.

## Why specs are not enough

Spec-Driven Development is a major improvement over vibe coding because the spec drives the work.

But a spec can define what should be built while still leaving open how an AI agent is governed while doing the work.

HIRMOS adds orchestration: runtime controls, durable artifacts, unresolved-decision handling, validation, and evidence-backed review.

## The most important beginner rule

Use the highest-level governed entrypoint that fits the job.

The regular-user workflow has one practical command per major step:

```text
Requirements   → requirements-agent
System Design  → system-design-agent
Implementation → implementation-agent
```

## What you can ignore for now

At the beginning, you do not need to understand:

- the full folder taxonomy
- the extension-local specs lanes
- deeper core mechanics
- extension authoring details
- hook execution internals
- runtime control templates

## Go next

- Continue to [Use HIRMOS in 3 Steps](use-hirmos-in-3-steps.md) for the regular-user workflow.
- Continue to [Quickstart](quickstart.md) for the practical first-run path.
- Go back to the [Getting started guide](README.md) if you want the full onboarding path at a glance.

## Optional reading

- [Release packaging](../../3-extend-contribute/core/release-packaging.md) if you plan to package or share the framework.
