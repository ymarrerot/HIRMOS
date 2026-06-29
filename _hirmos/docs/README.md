# HIRMOS Documentation

HIRMOS is an orchestration framework for AI-assisted software development.

This documentation is organized as an onboarding path. Start with the lane that matches what you want to do now; you do not need to read the whole framework before using it.

## How HIRMOS routes work

HIRMOS always follows the lifecycle:

```text
Understand System State → Design → Implementation → Update System State
```

The work shape determines how much structure is needed:

- **Single-session route** — for bounded work that can be scoped, implemented, reviewed, and closed in one governed session.
- **Delivery route** — for larger work that needs a Delivery Plan and Delivery Baseline before phase/session implementation.
- **Phase/session route** — for implementing the next accepted slice of a durable delivery.
- **IU implementation route** — for implementation work that needs Implementation Unit planning before execution.

If you only remember one operational rule: **do not implement before the relevant scope is accepted, and do not execute IUs before the IU plan is accepted.**

## 1 — Use HIRMOS for software work

Use this lane when you want to install HIRMOS, start a real project run, or understand the basic workflow inside an AI coding tool.

Start here:

- [Use HIRMOS](1-use-hirmos/README.md)
- [Quickstart](1-use-hirmos/getting-started/quickstart.md)
- [Installation](1-use-hirmos/getting-started/installation.md)
- [Commands](1-use-hirmos/getting-started/commands.md)
- [First Real Run](1-use-hirmos/getting-started/first-real-run.md)

## 2 — Learn the methodology

Use this lane when you want to understand how HIRMOS organizes AI-assisted software work.

Start here:

- [Methodology Overview](2-methodology/README.md)
- [Current-State-First Work](2-methodology/current-state-first.md)
- [Unresolved Items](2-methodology/unresolved-items.md)
- [Evidence-Backed Review](2-methodology/evidence-backed-review.md)

## 3 — Extend or contribute

Use this lane when you want to understand the framework structure, extension model, capability entrypoints, validation, or contribution workflow.

Start here:

- [Extend & Contribute](3-extend-contribute/README.md)
- [Framework Structure](3-extend-contribute/framework-structure.md)
- [Capabilities and Entrypoints](3-extend-contribute/capabilities-and-entrypoints.md)
- [Validation](3-extend-contribute/validation.md)

## Reference

Use this lane when you need a deeper map of artifacts, commands, runtime surfaces, integrations, stacks, or terminology.

Start here:

- [Reference Overview](reference/README.md)
- [Artifact Model](reference/artifact-model.md)
- [Runtime Surfaces](reference/runtime-surfaces.md)
- [Framework Command Reference](reference/framework-command-reference.md)
- [Glossary](reference/glossary.md)

## What to read first

| Goal | Read |
|---|---|
| Install HIRMOS | [Installation](1-use-hirmos/getting-started/installation.md) |
| Run it for the first time | [Quickstart](1-use-hirmos/getting-started/quickstart.md) |
| See a realistic tutorial | [First Real Run](1-use-hirmos/getting-started/first-real-run.md) |
| Understand larger delivery work | [Multi-Session Work](1-use-hirmos/getting-started/multi-session-work.md) |
| Inspect artifacts | [Artifact Model](reference/artifact-model.md) |
| Contribute safely | [Validation](3-extend-contribute/validation.md) |

## Onboarding posture

HIRMOS docs follow four principles:

- **Simple by default** — start with commands and visible pauses.
- **Transparent by design** — show where decisions, assumptions, and evidence live.
- **Rigorous underneath** — keep validator, artifact, and lifecycle rules available in methodology/reference docs.
- **Progressive in disclosure** — link deeper details instead of front-loading them.
