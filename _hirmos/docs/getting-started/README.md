# Getting Started

This is the canonical low-cognitive-load onboarding path for a first-time HIRMOS user.

If you only remember one thing from this page, remember this:

> To run HIRMOS, tell your LLM of choice: `Read and follow the instructions in HIRMOS_CORE.md`.

After that, follow this path in order. Treat this page as the canonical guide for the first-use journey, and avoid branching into the broader docs lanes until this page tells you to.

## What the drop-in install looks like inside your project

A normal drop-in install keeps your project README and adds the HIRMOS framework surfaces beside it. The GitHub landing-page `README.md` from the framework repository is **not** copied over to your project.

```text
your-project-folder/
├── HIRMOS_CORE.md          # bootstrap file the LLM reads first
├── HIRMOS_ORCHESTRATOR.md  # human operator playbook
├── README.md               # your project README
└── _hirmos/
    ├── STACK_CONFIG.json
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

You do not need to learn every folder now. The important thing is that your project keeps its own README, the LLM starts with `HIRMOS_CORE.md`, and the framework lives under `_hirmos/`.

## Step 1 — Get the basic mental model
- [Overview](./overview.md) — what HIRMOS is trying to help you do and what you can ignore for now

## Step 2 — Do the smallest successful run
- [Quickstart](./quickstart.md) — the shortest practical path through bootstrap, inspection, and a simple run

## Step 3 — Make sure the project stack is right
- [Selecting a stack](./selecting-a-stack.md) — confirm or change the active stack before doing more serious work

## Step 4 — See what a real governed run looks like
- [First real run](./first-real-run.md) — an optional worked example using one marketplace workflow extension after it has been installed

## When to leave this lane
Once this path feels clear, go to:
- [HIRMOS documentation hub](../README.md) for the broader docs lanes
- [Operator playbook](../orchestrator/operator-playbook.md) for the human-side operating model during serious runs

## What this lane is not trying to teach yet
At this stage, you do not need to learn:
- the full folder taxonomy
- the extension-local specs lanes
- deeper core mechanics
- extension authoring details
