<p align="left">
  <img src="assets/brand/hirmos-logo-primary-light-1200.png" alt="HIRMOS" width="360">
</p>

**HIRMOS is an orchestration framework for AI-assisted software development.**

HIRMOS helps AI coding tools work from the current state of a project, propose clear scope before implementation, pause when user decisions are needed, and preserve evidence so work can continue safely across sessions.

**Simple by default. Transparent by design. Rigorous underneath. Progressive in disclosure.**

## What using HIRMOS looks like

You install HIRMOS into a project, open that project in your AI coding tool, and ask the agent to start HIRMOS work:

```text
hirmos start "Add Google login"
```

The agent inspects the current project, proposes a scoped plan, pauses for your review, implements only after the right scope is accepted, and closes by recording what changed and what still needs attention.

Small work can stay as one governed session. Larger work can become a delivery with phases and multiple sessions. The process gets more structured only when the work needs it.

## Why HIRMOS exists

Serious software development needs governed execution: grounded context, accepted scope, visible assumptions, reviewable decisions, validation evidence, and continuity across sessions.

AI coding tools make that requirement more important, not less. They can move quickly from request to implementation, compress many decisions into one exchange, and change a system faster than a human can inspect the reasoning trail.

HIRMOS exists to make AI-assisted software work accountable, inspectable, and continuable. Without that governance, AI-assisted work can easily:

- start from stale or incomplete project context;
- treat notes, prototypes, tickets, or chat history as final authority;
- hide unresolved decisions inside prose;
- implement outside the agreed scope;
- claim completion without evidence;
- lose what changed between one session and the next.

HIRMOS keeps the interaction simple, but adds enough structure around the agent to preserve an accountable execution trail.

## How HIRMOS works

HIRMOS follows a current-state-first lifecycle:

```text
User Request
↓
Understand System State
→ Design
→ Implementation
→ Update System State
```

Current-state-first means the agent inspects the project before treating the new request as complete authority. The user request starts the work, but HIRMOS first checks relevant project state, then activates only the capabilities and artifacts needed for that request.

## How work is shaped

HIRMOS keeps small work light and adds durable structure only when the work needs it.

| Work shape | Typical route | What you see first |
|---|---|---|
| Small bounded work | one governed session | Session Baseline or Recommended Baseline |
| Requirements or design work | design-only governed session | reviewable requirements or design output |
| Single-session implementation | session scope, then implementation readiness | Session Baseline — Review or Change |
| Larger delivery | delivery plan, then phase/session work | Delivery Baseline — Review or Change |
| Implementation with units | implementation-unit planning, pause, then execution | Implementation Plan — Review or Change |

A governed session is one bounded unit of AI-assisted work with agreed scope, visible decisions, and close evidence. A delivery is a larger body of work that may need multiple governed sessions.

The lifecycle stays the same. The work shape only decides how much structure is needed.

## What HIRMOS gives the agent

A HIRMOS-installed project includes a framework folder at `_hirmos/`. That framework gives supported AI coding tools a shared way to:

- read the current project state before acting;
- separate rough input from decisions the user has accepted;
- propose scope before implementation;
- track unresolved decisions, assumptions, and blockers;
- pause when user input is needed;
- separate implementation planning from implementation execution when the work is complex;
- validate and record evidence before claiming completion;
- preserve accepted outcomes for the next session.

If you want to inspect the details, HIRMOS records them in files such as `SESSION_SCOPE.md`, `SESSION_LEDGER.md`, unresolved-item registers, implementation-unit files, and accepted-state indexes under `_hirmos/`.

## Install HIRMOS

Install the HIRMOS CLI from npm:

```bash
npm install -g hirmos
```

Then initialize HIRMOS inside your project:

```bash
cd /your/project/path
hirmos init
```

A normal install adds the framework folder at the project root:

```text
your-project/
├── your app files...
└── _hirmos/
```

The CLI installs the framework payload and AI-tool integration files. It does not execute the HIRMOS workflow itself.

To update an existing HIRMOS installation, use an idle HIRMOS boundary and update the terminal CLI first:

```bash
npm install -g hirmos@latest
cd /your/project/path
hirmos update
```

The update preserves project HIRMOS state and project-local configuration while replacing framework-owned files, reconciling recorded AI-tool integrations, validating the upgraded installation, and rolling back the framework/integration swap if the transaction fails. If a governed session is active, close it under the currently installed framework before updating. After a successful update, open a new AI-agent context so the upgraded bootstrap/integration surfaces are loaded.

For the complete CLI guide, including version checks, updates, `--integration`, `--source`, `--version`, and `--offline`, see [`_hirmos/docs/reference/cli-reference.md`](./_hirmos/docs/reference/cli-reference.md).

## Use HIRMOS inside your AI coding tool

After initialization, open the project in your AI coding tool. The integration file generated by `hirmos init` is the normal bootstrap path for that tool.

Then use HIRMOS workflow commands inside the agent conversation:

```text
hirmos start "Add Google login"
hirmos status
hirmos continue
hirmos close
```

These are framework workflow commands interpreted by the AI agent after the tool integration bootstraps HIRMOS. They are not terminal CLI commands.

If you are not using the CLI yet, installed HIRMOS manually, or your AI tool did not load the generated integration file, use this fallback bootstrap prompt:

```text
Read and follow _hirmos/AGENTS.md
```

## Decide what you want to do next

### I want to use HIRMOS on a project

Start here:

1. [_hirmos/docs/1-use-hirmos/getting-started/README.md](./_hirmos/docs/1-use-hirmos/getting-started/README.md)
2. [_hirmos/docs/1-use-hirmos/getting-started/quickstart.md](./_hirmos/docs/1-use-hirmos/getting-started/quickstart.md)
3. [_hirmos/docs/1-use-hirmos/getting-started/first-real-run.md](./_hirmos/docs/1-use-hirmos/getting-started/first-real-run.md)

### I want to understand larger delivery work

Read:

- [_hirmos/docs/1-use-hirmos/getting-started/multi-session-work.md](./_hirmos/docs/1-use-hirmos/getting-started/multi-session-work.md)
- [_hirmos/docs/1-use-hirmos/examples/delivery-baseline-and-phase-session.md](./_hirmos/docs/1-use-hirmos/examples/delivery-baseline-and-phase-session.md)

### I want to understand the methodology

Read:

- [_hirmos/docs/2-methodology/README.md](./_hirmos/docs/2-methodology/README.md)
- [_hirmos/docs/2-methodology/current-state-first.md](./_hirmos/docs/2-methodology/current-state-first.md)
- [_hirmos/docs/2-methodology/unresolved-items.md](./_hirmos/docs/2-methodology/unresolved-items.md)
- [_hirmos/docs/2-methodology/evidence-backed-review.md](./_hirmos/docs/2-methodology/evidence-backed-review.md)

### I want to inspect a HIRMOS run

Use the reference docs:

- [_hirmos/docs/reference/artifact-model.md](./_hirmos/docs/reference/artifact-model.md)
- [_hirmos/docs/reference/runtime-surfaces.md](./_hirmos/docs/reference/runtime-surfaces.md)
- [_hirmos/docs/reference/glossary.md](./_hirmos/docs/reference/glossary.md)

### I want to extend or contribute to HIRMOS

Start with:

- [_hirmos/docs/3-extend-contribute/README.md](./_hirmos/docs/3-extend-contribute/README.md)

## Supported AI tools

HIRMOS can generate integration files for these tool targets:

```text
agents
claude
cursor
copilot
codex
opencode
gemini
windsurf
kiro
```

The generic `agents` integration creates `AGENTS.md`. Some tools also use tool-specific files such as `CLAUDE.md`, Cursor rules, Copilot instructions, Gemini guidance, Windsurf rules, or Kiro steering files.

## What HIRMOS is not

HIRMOS is not an autonomous coding agent, a hidden prompt pack, or a CLI runtime engine. It is a framework that gives AI coding agents a governed way to work inside a project.

HIRMOS is probably not the right fit if you want one-shot code generation with no traceability, no reviewable decisions, and no durable project memory.

## Documentation map

- [_hirmos/docs/README.md](./_hirmos/docs/README.md) — docs entrypoint
- [_hirmos/docs/1-use-hirmos/](./_hirmos/docs/1-use-hirmos/) — how to use HIRMOS for software work
- [_hirmos/docs/2-methodology/](./_hirmos/docs/2-methodology/) — current-state-first methodology
- [_hirmos/docs/3-extend-contribute/](./_hirmos/docs/3-extend-contribute/) — how to extend or contribute
- [_hirmos/docs/reference/](./_hirmos/docs/reference/) — artifact, runtime, and glossary reference

## Design principles

HIRMOS is organized around four onboarding principles:

- **Simple by default** — start with a small command surface and clear next steps.
- **Transparent by design** — decisions, assumptions, artifacts, and evidence remain inspectable.
- **Rigorous underneath** — protocols, validators, regression fixtures, and session artifacts protect serious work.
- **Progressive in disclosure** — users start simple and inspect deeper only when needed.

A project may be greenfield, brownfield, or somewhere in between. HIRMOS starts by understanding the current system state, then activates the capabilities needed for the work.

## Contributing

For framework structure, validation, and extension guidance, read:

- [_hirmos/docs/3-extend-contribute/README.md](./_hirmos/docs/3-extend-contribute/README.md)

## License

See the project license for distribution terms.
