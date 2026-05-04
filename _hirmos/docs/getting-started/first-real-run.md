# First Real Run

This optional example shows what a real governed run looks and feels like after a marketplace workflow extension has been installed. It uses `system-design-agent:system-design-cycle`, then continues into `system-design-agent:phase-design-cycle`, only as a concrete example; Core does not require this extension, and you may use another installed extension with equivalent governed entrypoints.

## What this guide is trying to show

A first real run should answer questions like these:
- What do I actually ask the LLM to do?
- What does a serious extension run look like on screen?
- What gets produced?
- What happens when the cycle pauses?
- What does the Orchestrator do next?

## Scenario

Imagine a team has already gathered early requirements and now wants a governed design workflow. The next practical step is to run the system design cycle so HIRMOS can normalize the design work, surface unresolved gated items, and produce the main design artifacts.

If your project only has the minimal built-in extensions, treat this page as a realistic example of what a serious run looks like after you install `system-design-agent`. You can discover and install that extension from the HIRMOS Marketplace.

## Step 1 — Bootstrap the framework

Tell your LLM:

> Read and follow the instructions on `_hirmos/HIRMOS_CORE.md`.

If you are the human operator, keep `_hirmos/HIRMOS_ORCHESTRATOR.md` available so you can make decisions when the cycle pauses.

## Step 2 — Confirm the extension is available

Ask for:

```text
cmd: list extensions
```

A compact example result could look like this:

```text
Available extensions
- hello-world
- pretty-output
- system-design-agent
```

At this point you know the design extension you need is installed and available in this project.

## Step 3 — Run the system design cycle

Ask for:

```text
cmd: run extension system-design-agent:system-design-cycle
```

A realistic compact run might look like this:

```text
[HIRMOS]
Command resolved: cmd: run extension system-design-agent:system-design-cycle
Extension: system-design-agent
Entrypoint: system-design-cycle

[System Design Agent]
Reading the required extension-local specs and current design inputs.
Normalizing requirements into design-ready working artifacts.
Generating system-level design artifacts.

Cycle paused pending Orchestrator direction.

Unresolved gated items
1. Authentication scope is unclear
   Why it matters: user roles and protected workflows cannot be finalized yet.
   Proposed direction: ask customer

2. Notification delivery requirements are incomplete
   Why it matters: workflow timing and cross-system responsibilities remain unsettled.
   Proposed direction: defer and constrain

Artifacts updated
- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md
- _hirmos/artifacts/sot/SYSTEM_SOT.md
- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md
- _hirmos/artifacts/context/system-design-agent/system-design-cycle/CYCLE_STATUS.md
- _hirmos/artifacts/context/system-design-agent/system-design-cycle/RUN_TRACE.md
- _hirmos/artifacts/context/system-design-agent/system-design-cycle/VALIDATION_TRACE.md
- _hirmos/artifacts/context/system-design-agent/system-design-cycle/CYCLE_STATE_REPORT.md

Run state: paused
```

## What the paused run produced

A practical first run like this usually leaves you with:

- `REQUIREMENTS_SOT.md` — normalized requirements and clarified problem framing
- `SYSTEM_SOT.md` — the system-level design definition
- `ARCHITECTURE_SOT.md` — the architecture view derived from system design
- `CYCLE_STATUS.md` — the current trust state of the run
- `RUN_TRACE.md` — what the cycle did during this run
- `VALIDATION_TRACE.md` — what validation it checked
- `CYCLE_STATE_REPORT.md` — the practical summary of the cycle state, including unresolved gated items

## Step 4 — Handle the paused cycle as the Orchestrator

A paused cycle is normal. It means the extension did useful work, but it needs operator direction before claiming authoritative completion.

For the example above, the Orchestrator can respond like this:

- **Authentication scope is unclear** → ask customer
  - Example direction: “Draft the exact questions we should send to confirm roles and protected actions.”

- **Notification delivery requirements are incomplete** → defer and constrain
  - Example direction: “Proceed assuming email notifications only for now, and explicitly constrain the design so SMS or push notifications remain out of scope until confirmed.”

After you decide, rerun the same cycle so those decisions are absorbed governably:

```text
cmd: run extension system-design-agent:system-design-cycle
```

That rerun may now complete or pause again if new gated items remain.

## Step 5 — Continue into phase design

Once system design is governably ready, the next common step is:

```text
cmd: run extension system-design-agent:phase-design-cycle
```

A compact example result could look like this:

```text
[HIRMOS]
Command resolved: cmd: run extension system-design-agent:phase-design-cycle
Extension: system-design-agent
Entrypoint: phase-design-cycle

[System Design Agent]
Reading system-level design artifacts and staged delivery targets.
Generating phase-ready delivery slices.

Artifacts updated
- _hirmos/artifacts/sot/PHASES_SOT.md
- _hirmos/artifacts/phases/phase_1_foundation_SOT.md
- _hirmos/artifacts/phases/phase_2_core_workflows_SOT.md
- _hirmos/artifacts/phases/phase_3_reporting_and_admin_SOT.md
- _hirmos/artifacts/context/system-design-agent/phase-design-cycle/CYCLE_STATUS.md
- _hirmos/artifacts/context/system-design-agent/phase-design-cycle/RUN_TRACE.md
- _hirmos/artifacts/context/system-design-agent/phase-design-cycle/VALIDATION_TRACE.md

Run state: completed
```

At this point the visitor can see that a real HIRMOS run does not just produce a single answer. It produces governed artifacts that move the project toward implementation in a reviewable way.

## What this real run should feel like

A real governed run should feel like this:
- the extension does substantive work
- the output is visible and reviewable
- pauses are understandable, not mysterious failures
- the Orchestrator stays responsible for the key decisions
- reruns absorb decisions instead of leaving them trapped in chat history

## Go next

- Continue to the [Documentation hub](../README.md) when you are ready to leave the getting-started lane and choose your next broader docs lane.
- Go back to the [Getting started guide](./README.md) if you want the full onboarding path at a glance.

## Optional reading

- [Operator playbook](../orchestrator/operator-playbook.md) if you want the human-side operating model for serious runs.
- [Optional paused-cycle example](../examples/system-design-agent-paused-cycle-example.md) if you installed the same example extension and want to compare this guide to a fuller paused-run example.
- The HIRMOS Marketplace if you want to install the optional workflow extension used in this example or choose another governed workflow extension.
