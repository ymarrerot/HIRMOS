# Getting Started

This is the canonical low-cognitive-load onboarding path for a first-time HIRMOS user.

If you only remember one thing from this page, remember this:

> `hirmos init` is the terminal command that generates agent-native bootstrap files. `_hirmos/HIRMOS_CORE.md` remains the HIRMOS bootstrap authority the AI tool must read before workflow work.

If you are not using the CLI yet, you can always initialize the AI session directly with: `Read and follow the instructions on _hirmos/HIRMOS_CORE.md`.

Follow this path in order. Treat this page as the canonical guide for the first-use journey, and avoid branching into the broader docs lanes until this page tells you to.

## What HIRMOS is

HIRMOS is an open modular framework for Orchestrated Spec-Driven Development.

The regular-user workflow is:

```text
Requirements → System Design → Implementation
```

This flow is designed to be simple by default, transparent by design, rigorous underneath, and progressively disclosed.

## What the drop-in install looks like inside your project

A normal drop-in install keeps your project root files and adds the `_hirmos/` framework folder beside them. Use a generated HIRMOS framework release package rather than copying the full GitHub repository checkout into your project. The GitHub landing-page `README.md`, root `LICENSE`, `.github/`, and `ops/` surfaces from the framework repository are **not** copied over to your project.

```text
your-project-folder/
├── README.md               # your project README
└── _hirmos/
    ├── HIRMOS_CORE.md          # bootstrap file the AI tool reads first
    ├── HIRMOS_ORCHESTRATOR.md  # human operator playbook
    ├── project.json
    ├── VERSION
    ├── CHANGELOG.md
    ├── UPGRADE_GUIDE.md
    ├── SOT_CHANGE_POLICY.md
    ├── README.md
    ├── core/
    │   └── authority/
    ├── docs/
    ├── extensions/
    │   └── _templates/
    ├── inputs/
    ├── artifacts/
    └── stacks/
```

You do not need to learn every folder now. The important thing is that your project keeps its own README, the AI tool ultimately reads `_hirmos/HIRMOS_CORE.md`, and the framework lives under `_hirmos/`. `hirmos init` can generate agent-native bootstrap files that point tools to that Core file, but it does not replace Core.

## Step 1 — Install and initialize

- [Install and Initialize HIRMOS](install-and-initialize.md) — install the `_hirmos/` payload, run `hirmos init` when available, and understand the fallback bootstrap prompt

## Step 2 — Get the basic mental model

- [Orchestrated Spec-Driven Development](../../2-methodology/README.md) — the methodology HIRMOS implements
- [Overview](overview.md) — what HIRMOS is trying to help you do and what you can ignore for now
- [Use HIRMOS in 3 Steps](use-hirmos-in-3-steps.md) — the Requirements → System Design → Implementation workflow

## Step 3 — Do the smallest successful run

- [Quickstart](quickstart.md) — the shortest practical path through bootstrap, inspection, and the three regular-user commands

## Step 4 — Make sure the project stack is right

- [Selecting a stack](selecting-a-stack.md) — confirm or change the active stack before doing more serious work

## Step 5 — See what a real governed run looks like

- [First real run](first-real-run.md) — an optional worked example using the Requirements → System Design → Implementation flow

## When to leave this lane

Once this path feels clear, go to:

- [Orchestrated Spec-Driven Development](../../2-methodology/README.md) if you want to understand why HIRMOS works this way
- [HIRMOS documentation hub](../../README.md) for the broader docs lanes
- [Operator playbook](../orchestrator/operator-playbook.md) for the human-side operating model during serious runs
- [Extend & Contribute to HIRMOS](../../3-extend-contribute/README.md) if you want to author extensions or contribute to the framework

## What this lane is not trying to teach yet

At this stage, you do not need to learn:

- the full folder taxonomy
- the extension-local specs lanes
- deeper core mechanics
- extension authoring details
