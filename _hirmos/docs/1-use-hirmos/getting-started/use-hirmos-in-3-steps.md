# Use HIRMOS in 3 Steps

Use this page when you want the regular-user path for running HIRMOS on a software project without first learning the full framework internals.

HIRMOS is an open modular framework for Orchestrated Spec-Driven Development. The short version is:

```text
Requirements → System Design → Implementation
```

This is the regular-user workflow for HIRMOS.

## Why this flow exists

Spec-Driven Development moves teams beyond vibe coding by making the spec drive the work.

But specs are not enough.

A spec can define what should be built, but it does not fully define how an AI agent is governed while the work is being done. HIRMOS adds the orchestration layer: durable artifacts, runtime controls, unresolved-decision handling, validation, and evidence-backed review.


## Why HIRMOS uses these three steps

HIRMOS implements [Orchestrated Spec-Driven Development](../../2-methodology/README.md): specs define what the AI agent should build, while orchestration governs how the agent does the work.

The three-step flow is the practical front door for that methodology.

## Step 1 — Requirements

Tell HIRMOS what you need to build.

This may include:

- a prompt or short command argument;
- project context;
- requirement notes;
- user stories;
- screenshots or online-service attachments;
- existing prototypes;
- files under `_hirmos/inputs/requirements-agent/requirements/`;
- explicit bounded local file or repository-context references;
- technical constraints;
- business or product constraints.

The Requirements step turns informal or partial inputs into structured requirements artifacts suitable for system design.

Use the commands below inside your AI tool after HIRMOS Core has loaded. They are HIRMOS workflow commands, not terminal shell commands.

Use real HIRMOS artifact names where they are clear. For example, a requirements-focused workflow should produce or update artifacts such as `REQUIREMENTS_SOT.md` and should contribute assumptions, open questions, and unresolved items into the existing unresolved-item governance path.

Run this step with:

```text
hirmos requirements
```

For short requirements, you may include the requirement directly after the command:

```text
hirmos requirements Build a menu management app for a small restaurant.
```

For longer or reusable requirements, use the current chat/session prompt, attach files when running in an online LLM environment, place local requirement files under `_hirmos/inputs/requirements-agent/requirements/`, or provide explicit bounded local file references. HIRMOS should not automatically ingest the whole repository without a bounded scope.

## Step 2 — System Design

HIRMOS turns requirements into structured, reviewable, testable system design artifacts before implementation.

System Design can include:

- system model;
- architecture and design decisions;
- staged delivery targets;
- implementation phases;
- assumptions and open questions;
- unresolved gated items requiring Orchestrator direction.

Useful HIRMOS artifacts in this area include names such as `SYSTEM_SOT.md`, `ARCHITECTURE_SOT.md`, and `PHASES_SOT.md`.

Run this step with:

```text
hirmos system-design
```

## Step 3 — Implementation

HIRMOS implements the system in bounded, reviewable units.

Implementation includes:

- implementation planning;
- an approval pause when planning needs review before execution;
- phase-by-phase execution;
- validation;
- repair or pause handling;
- evidence-backed review;
- completed, paused, or failed terminal status.

Run this step with:

```text
hirmos implementation
```

## Evidence-backed Review

Evidence-backed Review is part of Implementation, not a fourth top-level step.

It means HIRMOS should not merely claim that work is complete. It should explain:

- what changed;
- what artifacts were produced or updated;
- what checks ran;
- what passed or failed;
- what remains unresolved;
- whether the run completed, paused, or failed;
- what should happen next.

## How much do you need to learn first?

Start with the three-step flow.

You do not need to learn every internal control file, extension manifest, hook rule, or runtime folder before using HIRMOS. Those mechanics remain inspectable when you need them, but the beginner path should stay simple.

The operating principle is:

```text
Simple by default.
Transparent by design.
Rigorous underneath.
Progressive disclosure.
```

## Go next

- Continue to the [Quickstart](quickstart.md) for the practical first-run path.
- Read the [Overview](overview.md) for the beginner mental model.
- Use the [Documentation hub](../../README.md) when you want to choose a deeper lane.
