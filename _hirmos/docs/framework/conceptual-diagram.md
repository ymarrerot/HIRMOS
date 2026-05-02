# Conceptual Diagram

This diagram is the fastest high-level mental model for HIRMOS.

It shows the main operating relationship between:
- the **Orchestrator**
- the **Core**
- installed **Extensions**
- governed **Runtime Surfaces**
- authoritative and non-authoritative project artifacts

```text
                           ┌──────────────────────────┐
                           │       Orchestrator       │
                           │                          │
                           │ Defines goals, chooses   │
                           │ entrypoints, reviews     │
                           │ outputs, records         │
                           │ decisions, owns final    │
                           │ direction                │
                           └────────────┬─────────────┘
                                        │
                                        │ bootstraps / commands
                                        ▼
                    ┌───────────────────────────────────────┐
                    │                 Core                  │
                    │                                       │
                    │ Bootstrap • command protocol •        │
                    │ manifest rules • loading/resolution • │
                    │ public-surface enforcement • tracing  │
                    └────────────┬──────────────────────────┘
                                 │ runs / resolves
                                 ▼
          ┌──────────────────────────────────────────────────────────┐
          │                    Installed Extensions                  │
          │                                                          │
          │  Agent extensions • workflow extensions • deliverable    │
          │  extensions • utility/hook extensions                    │
          └────────────┬───────────────────────────────┬─────────────┘
                       │ expose                         │ contribute
                       │ entrypoints                    │ hooks
                       ▼                                ▼
       ┌──────────────────────────────┐   ┌──────────────────────────┐
       │ Public Entrypoints           │   │ Specs / Internal Logic   │
       │                              │   │                          │
       │ - cycle entrypoints          │   │ Local method • quality   │
       │ - lower-level reusable       │   │ bar • validation •       │
       │   entrypoints                │   │ decision checkpoints     │
       └────────────┬─────────────────┘   └────────────┬─────────────┘
                    │ writes / reads                     │ governs
                    └────────────────────┬──────────────┘
                                         ▼
        ┌─────────────────────────────────────────────────────────────┐
        │                      Runtime Surfaces                       │
        │                                                             │
        │ _hirmos/inputs/<extension-id>/...   raw extension-owned input   │
        │ _hirmos/artifacts/context/<extension-id>/...  normalized working context   │
        │ _hirmos/artifacts/sot/                        authoritative source-of-truth  │
        │ _hirmos/artifacts/phases/                     generated phase contracts     │
        │ _hirmos/artifacts/prompts/                    generated execution prompts   │
        └─────────────────────────────────────────────────────────────┘
```

## What this diagram is trying to teach

### The Orchestrator is still central
The framework is not autonomous in the sense of replacing human authority.
The Orchestrator:
- chooses what to run
- reviews outputs
- resolves important decisions
- owns the final direction of the work

### The Core stays deliberately small
The Core is not where most workflow intelligence lives.
Its job is to:
- bootstrap the LLM into framework-aware operation
- interpret the public command surface
- resolve manifests and entrypoints
- preserve trust through explicit runtime behavior

### Extensions carry most of the intelligence
The real work happens in extensions.
Some extensions may behave like agents. Others may behave like workflow packs, deliverable generators, or utility/hook packs.

### Public entrypoints are the command surface
Extensions do not expose every internal file.
They expose an intentional public surface.
That is why the framework distinguishes:
- **public entrypoints**
- **private/internal files**

### Specs matter because they preserve local governance
For serious workflows, a Spec is the local contract behind the entrypoint.
A Spec can define:
- what the workflow is for
- what inputs it expects
- what outputs it produces
- what quality bar it must meet
- when it must pause for Orchestrator direction

### Runtime surfaces keep project state outside extension packages
This is one of the most important design decisions in HIRMOS.
Extensions remain clean installed packages. Runtime/project state lives in governed runtime surfaces outside extension package directories.

## How this differs from the original framework

The original framework expressed many of these ideas through built-in roles such as Assistant, Architect, and Agent. HIRMOS keeps the governance value of that model, but restructures the architecture around:
- a smaller Core
- coherent extensions
- explicit entrypoints
- namespaced runtime surfaces

That makes the new framework easier to extend, easier to package, and better suited for a community ecosystem.
