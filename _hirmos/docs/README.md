# HIRMOS Documentation

HIRMOS is an orchestration framework for AI-assisted software development.

This documentation is organized as an onboarding path. Start with the lane that matches what you want to do now; you do not need to read the whole framework before using it.

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

Use this lane when you need a definition, artifact map, runtime-surface explanation, or terminology lookup.

Start here:

- [Reference](reference/README.md)
- [Artifact Model](reference/artifact-model.md)
- [CLI Reference](reference/cli-reference.md)
- [Framework Command Reference](reference/framework-command-reference.md)
- [Integration Tools](reference/integration-tools.md)
- [Runtime Surfaces](reference/runtime-surfaces.md)
- [Glossary](reference/glossary.md)
- [Stacks](reference/stacks.md)
- [Interaction Modes](reference/interaction-modes.md)

## Decide what you want to do next

| I want to... | Go here |
|---|---|
| Install HIRMOS in a project | [Installation](1-use-hirmos/getting-started/installation.md) |
| Start using HIRMOS quickly | [Quickstart](1-use-hirmos/getting-started/quickstart.md) |
| Run my first real project session | [First Real Run](1-use-hirmos/getting-started/first-real-run.md) |
| Understand the command flow | [Commands](1-use-hirmos/getting-started/commands.md) |
| Understand the methodology | [Methodology Overview](2-methodology/README.md) |
| Understand current-state-first work | [Current-State-First Work](2-methodology/current-state-first.md) |
| Understand unresolved decisions and assumptions | [Unresolved Items](2-methodology/unresolved-items.md) |
| Extend or contribute to HIRMOS | [Extend & Contribute](3-extend-contribute/README.md) |
| Understand framework structure | [Framework Structure](3-extend-contribute/framework-structure.md) |
| Use the terminal CLI | [CLI Reference](reference/cli-reference.md) |
| Use HIRMOS workflow commands inside an AI tool | [Framework Command Reference](reference/framework-command-reference.md) |
| Understand AI-tool integrations | [Integration Tools](reference/integration-tools.md) |
| Look up artifact names or terminology | [Reference](reference/README.md) |

## If you only remember one thing

Use `hirmos init` to install the framework and generate the AI-tool integration file for your tool. That generated integration file is the normal bootstrap path. For complete CLI usage, including install, update, `--integration`, `--source`, `--version`, and `--offline`, see the [CLI Reference](reference/cli-reference.md).

If you are not using the CLI yet, installed HIRMOS manually, or your AI tool did not load the generated integration file, use this fallback bootstrap prompt:

```text
Read and follow _hirmos/AGENTS.md
```

Then use HIRMOS workflow commands inside the AI-agent conversation, not as terminal CLI commands:

```text
hirmos start "<your request>"
hirmos status
hirmos continue
hirmos close
```


## Scope authority model

Current HIRMOS releases use `SESSION_SCOPE.md` as active session authority. Durable multi-session work uses `_hirmos/system/delivery/DELIVERY_PLAN.md` as the delivery roadmap/register and `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` as the scoped authority for one delivery/release.

## Focus-aware delivery and session workflow

Current HIRMOS uses a focus-aware runtime model. Every command runs inside a governed session envelope, but HIRMOS creates only the artifacts required by the selected focus.

- Small work can stay minimal.
- Single-session implementation uses `SESSION_SCOPE.md` as the complete active authority.
- Durable delivery work first uses `DELIVERY_SCOPE.md` and delivery-level unresolved items, then creates phase/session authority after the delivery baseline is accepted.

See:

- [Command Guide](1-use-hirmos/getting-started/commands.md)
- [Multi-Session Work](1-use-hirmos/getting-started/multi-session-work.md)
- [Delivery Baseline and Phase/Session Flow](1-use-hirmos/examples/delivery-baseline-and-phase-session.md)
- [Runtime Surfaces](reference/runtime-surfaces.md)
