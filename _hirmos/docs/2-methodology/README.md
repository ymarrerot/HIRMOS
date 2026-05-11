# Orchestrated Spec-Driven Development

Orchestrated Spec-Driven Development is a methodology for AI-assisted software engineering that uses specs to define what the AI agent should build, while adding orchestration to govern how the work proceeds, pauses, validates, and proves completion.

It builds on Spec-Driven Development in the broad methodological sense: specs should guide planning, implementation, and validation. HIRMOS is not dependent on any specific SDD tool, vendor, command set, or implementation.

## The foundation: Spec-Driven Development

Spec-Driven Development is the practice of using written specifications to drive software work.

Instead of asking an AI agent to “just build it,” SDD first defines what should be built, what constraints matter, and what the implementation should satisfy.

That foundation matters. Clear Specs are much stronger than vague prompts. SDD is still an evolving practice, and different tools and teams implement it differently, so HIRMOS uses the term in its broad methodological sense rather than as a dependency on any single implementation.

## The gap: specs are necessary, but not enough

Specs are a strong starting point, but serious AI-assisted development also needs orchestration.

The simple distinction is:

```text
Specs define the intended work.
Orchestration governs how the work proceeds.
Evidence shows whether completion can be trusted.
```

This is not only about today's model limitations. Complex software work needs traceable decisions, durable artifacts, reviewable outputs, validation, and honest terminal states across sessions, files, people, and time.

AI-assisted development makes that need more urgent. Work moves faster, more decisions can be made implicitly, and an agent can still skip context, make silent assumptions, miss unresolved decisions, overclaim completion, or hide weak validation.

Some SDD implementations add governance mechanisms. Orchestrated SDD makes this orchestration explicit, systematic, and central to the workflow.

Many AI-assisted SDD workflows still need stronger answers to questions like:

```text
How should the AI agent proceed, pause, validate, and prove completion while doing the work?
```

Specs alone do not guarantee that the agent will pause when an important decision is unresolved.

Specs alone do not guarantee that assumptions, open questions, and tradeoffs will be tracked in a durable place.

Specs alone do not guarantee that inputs and outputs from multiple files, hooks, extensions, or artifacts will be reconciled correctly.

Specs alone do not guarantee that the agent will validate its own work before claiming completion.

HIRMOS adds fail-closed behavior as an explicit Orchestrated SDD design principle: when required evidence, decisions, or validation are missing, the workflow must pause or fail honestly instead of claiming success.

## A practical failure example

The spec says:

> “Before implementation, identify unresolved assumptions and open questions, and do not proceed if any item blocks safe implementation.”

The agent reads the spec, produces a good-looking system design, and says it is ready to implement.

But it never creates a durable unresolved-item inventory. It mentions two questions in prose, misses a third question from an attached design file, and does not clearly mark which items are blocking. When implementation starts, the agent silently chooses defaults.

Result: the system begins to take shape around unapproved assumptions, missing requirements, and unresolved decisions that were never surfaced clearly enough for the user to approve or reject.

This is not a failure of the spec. The spec was clear. It is a failure of orchestration: the workflow had no structure that forced the requirement to be satisfied, no artifact that preserved the inventory, and no validation that checked whether the inventory was complete before continuing.

## How Orchestrated SDD handles the same situation

In Orchestrated SDD, the agent cannot treat “identify unresolved items” as a loose request.

The workflow requires each source of unresolved items — requirements, system design, architecture, phases, presentation inputs, prototypes, or other extension outputs — to update its own section of a durable unresolved-item inventory while the work is happening.

The workflow reconciles those items before completion, uses required output templates when the run pauses, self-validates that the inventory was updated, and fails closed if a gated decision remains unresolved.

Result: implementation does not begin from hidden assumptions. It begins from requirements and design artifacts whose open decisions were captured, reviewed, resolved, or explicitly carried forward with visible risk.

That is the difference between a Clear Spec and an orchestrated workflow.

A Clear Spec says what should happen.

Orchestration makes the workflow prove that it happened — and leaves durable evidence behind.

## The reliability pattern: Beyond Clear Specs

The difference is not that Orchestrated SDD simply writes better specs.

The difference is that it applies a reliability pattern HIRMOS calls **Beyond Clear Specs**.

The pattern starts from a practical observation:

```text
Specs are necessary. Orchestration makes them trustworthy in practice.
```

Beyond Clear Specs introduces five pillars that work together:

1. Clear Specs
2. Durable artifacts
3. Required surfaced outputs
4. Self-validation
5. Fail-closed behavior

Clear Specs make the agent’s target explicit enough to guide work without relying on hidden assumptions.

Durable artifacts preserve important reasoning, inputs, decisions, and collected material before they are summarized or lost.

Required surfaced outputs force important results, decisions, and evidence to appear in a stable, reviewable shape.

Self-validation makes the workflow check whether it actually followed its own rules before claiming completion.

Fail-closed behavior is a HIRMOS design principle: when required evidence, decisions, or validation are missing, the workflow must pause or fail honestly rather than overclaiming success.

You can also think of the pattern in two practical groups:

- the governance backbone: durable artifacts, required surfaced outputs, and fail-closed behavior;
- the execution discipline: Clear Specs and self-validation.

Both groups remain important. The amount of scaffolding can scale with project risk and model capability, but the underlying discipline does not disappear.

Read the methodology deep dive on [Beyond Clear Specs](beyond-clear-specs.md) when you want to understand the five pillars in more detail.

## The lifecycle

Orchestrated SDD uses a practical lifecycle:

```text
Requirements → System Design → Implementation
```

Requirements turns goals, notes, files, prototypes, constraints, and user context into structured requirements artifacts.

System Design turns requirements into architecture, system decisions, phase design, and implementation-ready planning artifacts.

Implementation plans, pauses for approval when needed, executes bounded phases, validates results, and completes with Evidence-backed Review.

Read [Requirements → System Design → Implementation](requirements-system-design-implementation.md) for the lifecycle walkthrough.

## How HIRMOS implements Orchestrated SDD

HIRMOS is the open modular framework that implements Orchestrated Spec-Driven Development.

It provides Core runtime governance, official lifecycle extensions, durable artifacts, unresolved-decision handling, hooks, validation, and evidence-backed completion.

The regular-user flow is:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

These are HIRMOS workflow commands used inside the AI tool after Core bootstrap, not terminal shell commands.

Read [How HIRMOS implements Orchestrated SDD](hirmos-implementation.md) for the framework bridge.

## Go deeper

- [Specs are not enough](specs-are-not-enough.md)
- [Beyond Clear Specs](beyond-clear-specs.md)
- [Requirements → System Design → Implementation](requirements-system-design-implementation.md)
- [Unresolved decisions](unresolved-decisions.md)
- [Evidence-backed Review](evidence-backed-review.md)
- [How HIRMOS implements Orchestrated SDD](hirmos-implementation.md)
