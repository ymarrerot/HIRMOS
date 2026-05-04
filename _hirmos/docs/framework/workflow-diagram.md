# Workflow Diagram

This diagram shows the preferred operational path for HIRMOS.

It also gives you a simple SDLC anchor: bootstrap happens before project work starts, cycles usually govern whole stages of work, and runtime artifacts preserve the outputs and decisions that later stages depend on.

It emphasizes:
- bootstrap first
- use high-level **Cycles** by default
- drop to lower-level entrypoints when tighter control is needed
- pause at decision checkpoints when required
- preserve trust state in runtime artifacts

```text
                        HIRMOS Operating Workflow

┌─────────────────────────────────────────────────────────────────────┐
│ 1. Bootstrap                                                       │
│                                                                     │
│ - Orchestrator asks the AI tool to read and follow _hirmos/HIRMOS_CORE.md             │
│ - The Core reads its governing files and becomes framework-aware   │
│ - Installed extensions become available through the command model  │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 2. Choose the right entrypoint                                     │
│                                                                     │
│ - Prefer a high-level cycle entrypoint when one exists             │
│ - Use lower-level entrypoints when tighter control is needed       │
│ - Public entrypoint names determine what the operator can run directly  │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 3. Resolve and run                                                 │
│                                                                     │
│ - Core resolves the extension manifest and public entrypoint       │
│ - Relevant hooks are loaded when declared                          │
│ - The entrypoint runs through its intended workflow logic     │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 4. Produce and update runtime artifacts                            │
│                                                                     │
│ - Raw inputs are consumed from _hirmos/inputs/<extension-id>/...       │
│ - Working context is normalized under _hirmos/artifacts/context/<extension-id>/  │
│ - Authoritative source-of-truth artifacts are written under _hirmos/artifacts/sot/           │
│ - Phase contracts and prompts are written to their own surfaces    │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 5. Validate locally                                                │
│                                                                     │
│ - The workflow validates against its governing Spec                │
│ - Local quality bar, anti-patterns, and completion checks apply    │
│ - Validation state may be recorded in context artifacts            │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 6. Decision checkpoint?                                            │
│                                                                     │
│ - If no major gating items remain, the cycle can complete          │
│ - If gating items remain, the cycle pauses                         │
│ - The Orchestrator is asked for direction directly in chat         │
│ - Trust state is recorded in cycle-status / decision artifacts     │
└─────────────────────────────────────────────────────────────────────┘
                     │                                   │
                     │ Complete                          │ Pause
                     ▼                                   │
┌─────────────────────────────────────────────────────────────────────┐
│ 7. Continue, rerun, or supersede                                   │
│                                                                     │
│ - Accept outputs and continue downstream                           │
│ - Rerun the same cycle after a decision or stronger inputs         │
│ - Use lower-level entrypoints for targeted refinement              │
│ - Supersede earlier outputs when the framework contract requires   │
└─────────────────────────────────────────────────────────────────────┘
                                                         │
                                                         ▼
                         back to a cycle or lower-level entrypoint
                         as appropriate
```

## How this relates to familiar SDLC stages

A useful mental model is:
- cycles often govern whole stages such as requirements grounding, design, planning, implementation planning, or execution
- lower-level entrypoints help when one stage needs a narrower rerun or targeted refinement
- runtime artifacts help the next stage inherit reviewed work instead of guesswork
- pauses happen when the workflow reaches a decision boundary that still needs human direction

## What this diagram is trying to teach

### Cycle-first is the default
The framework should normally be used through the highest-level governed entrypoint that fits the job.

For example, use a high-level cycle exposed by the installed workflow extension you selected. That is usually preferable to manually invoking lower-level entrypoints unless tighter control is needed.

### Lower-level entrypoints still matter
The framework intentionally preserves reusable lower-level workflows so the Orchestrator can:
- refine one artifact
- rerun one planning unit
- compose a custom flow
- debug a specific contract boundary

### Paused is a valid cycle outcome
A serious cycle does not need to force fake completion.
If unresolved gating items remain, a pause is a governed outcome, not a failure of the framework.

### Runtime artifacts are part of the trust model
The framework does not only “say” what happened in chat.
It should also preserve the state of work through runtime artifacts such as:
- cycle status
- decision logs
- validation traces
- generated SoTs, phase contracts, and prompts

## How this helps onboarding

A new user usually needs to understand two things quickly:
1. what the system **is**
2. how work **moves** through it

The conceptual diagram answers the first question.
This workflow diagram answers the second.


## Go next

- **See the fast working model behind this flow:** open the [Framework operating model](./framework-operating-model.md).
- **Operate serious runs safely:** go to the [Operator playbook](../orchestrator/operator-playbook.md).
- **Go back to framework guidance:** return to [Framework guidance](./README.md).

## Optional reading

- **Go back to the broader docs hub:** return to the [Documentation hub](../README.md).
