# Workflow Diagram

This diagram shows the regular-user workflow for HIRMOS.

It gives a simple SDLC anchor while preserving HIRMOS' governance model:

```text
Requirements → System Design → Implementation
```

It emphasizes:

- simple public lifecycle first;
- real HIRMOS artifact names where clear;
- unresolved decisions stay visible;
- implementation remains evidence-backed;
- deeper Core and extension mechanics remain available through progressive disclosure.

```text
                         HIRMOS Regular-User Workflow

┌─────────────────────────────────────────────────────────────────────┐
│ 0. Bootstrap                                                       │
│                                                                     │
│ - Orchestrator asks the AI tool to read and follow _hirmos/HIRMOS_CORE.md │
│ - The Core reads its governing files and becomes framework-aware   │
│ - Installed extensions become available through the command model  │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 1. Requirements                                                    │
│                                                                     │
│ - User provides goals, notes, context, stories, files, prototypes  │
│ - HIRMOS turns inputs into requirements artifacts                  │
│ - Clear artifact names such as REQUIREMENTS_SOT.md remain visible │
│ - Assumptions, open questions, and unresolved items are surfaced   │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 2. System Design                                                   │
│                                                                     │
│ - Requirements feed system and architecture design                 │
│ - HIRMOS produces artifacts such as SYSTEM_SOT.md,                 │
│   ARCHITECTURE_SOT.md, and PHASES_SOT.md                           │
│ - Gated decisions pause the workflow instead of being hidden       │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 3. Implementation                                                  │
│                                                                     │
│ - HIRMOS plans and executes bounded phases                         │
│ - Approval pauses occur where required                             │
│ - Validation and repair/pause handling protect trust               │
│ - Evidence-backed Review explains completion, pause, or failure    │
└─────────────────────────────────────────────────────────────────────┘
```

## How this relates to governed runtime mechanics

The regular-user workflow is intentionally simple. Underneath it, serious HIRMOS runs still depend on:

- extension entrypoints and specs;
- runtime artifacts;
- unresolved-item governance;
- hook execution control;
- run execution controls;
- validation traces;
- completed, paused, or failed terminal states.

The beginner path does not require learning every mechanic first. The mechanics remain inspectable when you need them.

## Command path

The practical command path uses one official extension command per workflow step:

```text
Requirements   → hirmos requirements
System Design  → hirmos system-design
Implementation → hirmos implementation
```

These command surfaces are the current practical path for the regular-user workflow.

## What this diagram is trying to teach

### Simple first

The top-level user flow should be easy to remember:

```text
Requirements → System Design → Implementation
```

### Transparent always

Simple does not mean black box. HIRMOS should still show the artifacts, unresolved decisions, checks, and terminal states that make the workflow trustworthy.

### Rigorous underneath

A HIRMOS run should not claim completion merely because it reached the end of a prompt. Completion should be supported by evidence and a valid terminal state.

## Go next

- **See the fast working model behind this flow:** open the [Framework operating model](framework-operating-model.md).
- **Use HIRMOS:** go to [Use HIRMOS in 3 Steps](../getting-started/use-hirmos-in-3-steps.md).
- **Operate serious runs safely:** go to the [Operator playbook](../orchestrator/operator-playbook.md).
- **Go back to framework guidance:** return to [Framework guidance](../../3-extend-contribute/framework/README.md).
