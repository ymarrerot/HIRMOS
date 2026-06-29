# `_hirmos/`

This folder is the HIRMOS framework payload.

If you reached this page from the GitHub repository, start with the root README first:

- [HIRMOS repository README](../README.md)

The root README explains what HIRMOS is, what using it looks like, how to install it, and where to go next. This page is different: it is a map for people who intentionally opened the `_hirmos/` folder and want to understand what is inside the framework payload.

## What this folder is for

HIRMOS is installed into a software project as a single `_hirmos/` directory. AI coding tools use this directory to understand how to run HIRMOS workflow commands such as:

```text
hirmos start "Add Google login"
hirmos status
hirmos continue
hirmos close
```

Those workflow commands are interpreted by the AI agent inside the coding-tool conversation. They are not terminal commands.

The terminal CLI installs and updates the framework payload. The framework files inside `_hirmos/` guide the AI agent after installation.

## Quick map

| Path | Purpose |
|---|---|
| [`AGENTS.md`](./AGENTS.md) | Fallback bootstrap file for AI tools. If an integration file did not load, tell the agent: `Read and follow _hirmos/AGENTS.md`. |
| [`hirmos.config.json`](./hirmos.config.json) | Framework metadata and installed capability configuration. |
| [`core/commands/`](./core/commands/) | Compact runtime command authority for `hirmos start`, `status`, `continue`, and `close`. |
| [`core/templates/`](./core/templates/) | Canonical templates for generated session, delivery, state, evidence, and implementation-unit artifacts. |
| [`core/protocol/`](./core/protocol/) | Deeper reference protocols used when command files require escalation detail. |
| [`core/authority/`](./core/authority/) | Shared framework authority surfaces and control rules used across capabilities. |
| [`extensions/`](./extensions/) | HIRMOS capability entrypoints, such as design, implementation, and system-state capabilities. |
| [`integrations/`](./integrations/) | AI-tool integration registry and templates for Cursor, Claude, Copilot, Codex, Gemini, Windsurf, Kiro, OpenCode, and generic agent files. |
| [`tools/`](./tools/) | Validator and helper scripts used to check HIRMOS artifacts and framework invariants. |
| [`docs/`](./docs/) | User, methodology, contribution, and reference documentation. |
| [`system/`](./system/) | Seed accepted-state files used when HIRMOS initializes a project. |

## Where to read next

Choose the path that matches what you are doing.

### I am using HIRMOS in a project

Start here:

1. [Getting started](./docs/1-use-hirmos/getting-started/README.md)
2. [Quickstart](./docs/1-use-hirmos/getting-started/quickstart.md)
3. [First real run](./docs/1-use-hirmos/getting-started/first-real-run.md)

### I am trying to understand the workflow files

Read:

- [Runtime surfaces](./docs/reference/runtime-surfaces.md)
- [Artifact model](./docs/reference/artifact-model.md)
- [Glossary](./docs/reference/glossary.md)

### I am inspecting how HIRMOS controls AI-agent execution

Start with:

- [`core/commands/README.md`](./core/commands/README.md)
- [`core/commands/start.md`](./core/commands/start.md)
- [`core/commands/continue.md`](./core/commands/continue.md)
- [`core/commands/close.md`](./core/commands/close.md)

The command files are intentionally compact. They are the normal runtime surface. Larger protocol files exist for reference and escalation, not for routine first reads.

### I am extending or contributing to HIRMOS

Start here:

- [Extend and contribute](./docs/3-extend-contribute/README.md)

Then inspect:

- [`core/authority/`](./core/authority/)
- [`core/templates/`](./core/templates/)
- [`extensions/`](./extensions/)
- [`tools/validate.py`](./tools/validate.py)

## How this README differs from the root README

The root repository README is the main onboarding page for first-time visitors.

This `_hirmos/README.md` is a folder-level guide. It assumes you already opened the framework payload and want to understand its structure.

There is one packaging nuance:

- in the GitHub repository, `_hirmos/README.md` is this folder guide;
- in a release/install package, `_hirmos/README.md` is replaced with the root onboarding README so users can still read the main onboarding page inside their local project’s installed `_hirmos/` folder.

That packaging behavior is intentional. A GitHub browser and an installed-project user enter `_hirmos/` with different needs.

## Useful validation commands

From a HIRMOS workspace or installed project, the core validator can be run with:

```bash
python3 _hirmos/tools/validate.py
```

Framework development work also uses focused regression fixtures under `_hirmos/tools/` and package verification scripts under `ops/scripts/` in the source workspace.

## Design posture

HIRMOS keeps the user-facing path simple, but the framework payload is intentionally rigorous underneath.

At runtime, the agent should normally start from:

```text
_hirmos/AGENTS.md
_hirmos/core/commands/<command>.md
```

and should inspect deeper protocols, templates, tools, or historical artifacts only when the active command or validation result requires it.
