# Framework Operating Model

## Purpose

Define the authoritative framework-wide operating model for HIRMOS.

Use this authority file when you need the canonical high-level model for how HIRMOS is structured, how responsibility is layered, how governance is preserved, and where the Orchestrator sits relative to the framework.

## Scope and usage rule

This file owns the framework-wide operating model.

Use it when:
- explaining the major layers of HIRMOS
- explaining how HIRMOS preserves authority boundaries, reviewability, and trust
- judging whether behavior belongs in the core, an extension, or the Orchestrator
- grounding review criteria that depend on framework structure or governance
- writing user-facing guidance that summarizes how HIRMOS works without re-owning doctrine

Secondary guidance may explain this model in lighter language, but should not silently replace it.

## The framework operating model

HIRMOS operates through four layers:
1. bootstrap
2. core protocol
3. extension workflows
4. runtime surfaces

The Orchestrator sits above those layers and remains the human authority deciding what to run, what to accept, and when to continue.

### Bootstrap

Bootstrap initializes the runtime into framework-aware operation.

This is where the framework teaches the runtime:
- what the core rules are
- what command model to use
- what the major governed surfaces are
- how to treat extensions as public command surfaces instead of random folders

In practice, bootstrap normally begins with `_hirmos/HIRMOS_CORE.md`.

### Core protocol

The core is intentionally small.

Its job is not to hold most workflow intelligence. Its job is to make extension behavior structured and reliable.

The core is responsible for things like:
- command interpretation
- extension discovery
- manifest validation
- public entrypoint resolution
- hook matching and ordering
- stack resolution
- enforcing the difference between public surface and private internals

### Extension workflows

Extensions carry most of the domain or workflow intelligence.

Examples:
- a design extension may normalize requirements and produce trusted source-of-truth artifacts
- an implementation extension may plan, execute, review, and retry bounded implementation work
- a supporting extension may enrich another extension through hooks

This is one of the most important design ideas in HIRMOS:
- the core stays small
- serious behavior lives in coherent extensions

### Runtime surfaces

The framework preserves work through governed project surfaces rather than leaving everything in chat.

Examples include:
- `_hirmos/inputs/`
- `_hirmos/artifacts/context/`
- `_hirmos/artifacts/outputs/`
- `_hirmos/artifacts/sot/`
- `_hirmos/artifacts/phases/`
- `_hirmos/artifacts/prompts/`
- `_hirmos/artifacts/ops/`

These surfaces make work:
- reviewable
- reusable
- inspectable
- less dependent on a single conversation

## The governance model inside the operating model {#governance-model}

HIRMOS governance lives inside the operating model rather than beside it.

### Bootstrap governance

Bootstrap teaches the runtime the framework's basic rules.

Examples:
- core bootstrap files
- command model expectations
- public-vs-private surface discipline

### Core governance

The core governs:
- command interpretation
- manifest rules
- entrypoint resolution
- hook matching and ordering
- stack resolution
- validation of the public command surface

### Extension-local governance {#extension-local-governance}

Serious extensions carry their own local contracts through:
- entrypoints
- extension-local specs
- templates
- validation traces
- paused, provisional, completed, or failed output expectations

This is where most workflow-specific quality bars live.

### Artifact-boundary governance {#artifact-boundary-governance}

The framework uses distinct surfaces for different kinds of project state.

For example:
- `_hirmos/artifacts/context/` is not the same as `_hirmos/artifacts/sot/`
- `_hirmos/artifacts/sot/` is not the same as `_hirmos/artifacts/prompts/`
- `_hirmos/artifacts/ops/` is not the same as `_hirmos/artifacts/context/`

These boundaries help prevent provisional materials from being mistaken for authoritative truth.

### Orchestrator governance

The Orchestrator remains the human authority.

The framework may propose, classify, warn, pause, or recommend.
But the Orchestrator still decides:
- what to run
- what to accept
- how to resolve important ambiguity
- when to continue downstream

## Why the operating model matters

Without these layers, AI-assisted work tends to collapse into one opaque stream of prompts and edits.

HIRMOS separates:
- framework mechanics
- workflow behavior
- project authority artifacts
- execution evidence

That separation is what lets the framework stay both modular and governable.

## What good governance should feel like {#good-governance}

Good governance should make AI-assisted work:
- more reviewable
- more explicit
- easier to inspect
- easier to rerun safely
- less dependent on hidden assumptions

It should not make the framework feel bureaucratic for its own sake.

## Common governance mistakes {#common-governance-mistakes}

HIRMOS is intentionally trying to avoid:
- putting too much behavioral truth in the core
- letting extensions silently rewrite authoritative artifacts they do not own
- treating chat output as enough without governed artifacts
- exposing every internal file as if it were a public contract
- allowing serious cycles to fake completion when they should pause

## The Orchestrator’s place in the model

### Orchestrator position

The Orchestrator sits above all four layers.

### Orchestrator responsibilities

The Orchestrator:
- chooses what to run
- reviews outputs
- records decisions
- accepts or rejects proposed directions
- decides when to continue, rerun, or stop

The framework helps structure the work. It does not replace human authority.

## Canonical authority lanes {#canonical-authority-lanes}

A project may install multiple system-design-focused extensions and multiple implementation-focused extensions, but canonical project lanes remain single-owner-at-a-time by use.

### Design authority in use

Multiple system-design-focused extensions may be installed, but only one can be **used as** the design authority at a time. The system-design extension currently being used as the design authority owns canonical writes to:

- `/_hirmos/artifacts/sot/`
- `/_hirmos/artifacts/phases/`

### Implementation authority in use

Multiple implementation-focused extensions may be installed, but only one can be **used as** the implementation authority for code-changing execution at a time. The implementation extension currently being used as the implementation authority owns canonical writes to:

- `/_hirmos/artifacts/prompts/`
- `/_hirmos/artifacts/ops/`
- project code changes

Alternative outputs from other installed extensions may still exist, but they should be treated as candidate artifacts until the project intentionally adopts them as the current canonical authority outputs.

## Related authority and guidance

Related authority files:
- `framework/source-of-truth-model.md`
- `framework/top-level-folder-definitions.md`

Related core-local authority lives under `_hirmos/core/authority/core/`.
