# How HIRMOS implements Orchestrated SDD

Orchestrated Spec-Driven Development is the methodology.

HIRMOS is the open modular framework that implements it.

## The regular-user flow

The HIRMOS front door is:

```text
Requirements → System Design → Implementation
```

The regular-user commands are:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

These are HIRMOS workflow commands used inside the AI tool after Core bootstrap, not terminal shell commands.

## What HIRMOS adds around the lifecycle

HIRMOS adds the structures needed to make AI-assisted work orchestrated while it is happening:

- Core runtime governance;
- official lifecycle extensions;
- durable artifacts;
- project-level unresolved-decision handling;
- hook-based extension coordination;
- validation;
- fail-closed terminal behavior as an explicit HIRMOS design principle;
- evidence-backed completion.

These structures do not replace specs. They make the work around the specs visible, reviewable, and honest.

## Simple by default, transparent by design

Regular users can start with the three-step workflow.

Power users, contributors, and extension authors can inspect the framework mechanics that make the workflow reliable.

That is why HIRMOS uses progressive disclosure:

```text
Simple by default.
Transparent by design.
Rigorous underneath.
Progressive disclosure.
```

## Why HIRMOS keeps Core and extensions separate

HIRMOS Core owns framework-level bootstrap, command resolution, runtime controls, hook execution control, and surfaced-output discipline.

Extensions own workflow intelligence such as Requirements, System Design, Implementation, presentation inputs, prototype ingestion, and other specialized workflows.

This separation keeps the framework composable while preserving a central trust boundary.

## Why this matters

HIRMOS structures are not only compensations for today’s model limitations.

They are the orchestration layer serious AI-assisted development needs as work becomes faster, more complex, and more consequential.

Current agent failures make that need visible today. HIRMOS’ deeper value is that it gives teams a practical way to keep AI-assisted work traceable, reviewable, and evidence-backed over time.
