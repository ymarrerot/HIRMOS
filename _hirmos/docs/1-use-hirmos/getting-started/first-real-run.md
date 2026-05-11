# First Real Run

This example shows what a real HIRMOS regular-user run looks like after the official workflow extensions are installed.

The practical flow is:

```text
Requirements → System Design → Implementation
```

with HIRMOS workflow-command backing:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

Use these workflow commands inside the AI tool after HIRMOS Core has loaded. They are not terminal shell commands.

## What this guide is trying to show

A first real run should answer questions like these:

- What do I actually ask the LLM to do?
- What does a serious HIRMOS run look like on screen?
- What gets produced?
- What happens when a step pauses?
- What does the Orchestrator do next?

## Scenario

Imagine a team wants to build a project from early notes, screenshots, user stories, and technical constraints. The team wants HIRMOS to turn those inputs into requirements, design the system, then implement one phase at a time with evidence.

## Step 1 — Initialize agent discovery and load Core

Install the HIRMOS CLI, then run this terminal command from the project root:

```bash
npm install -g hirmos
hirmos init
```

This creates or updates agent-native bootstrap files. It does not run the workflow.

Then tell your AI tool:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

If you are the human operator, keep `_hirmos/HIRMOS_ORCHESTRATOR.md` available so you can make decisions when a run pauses.

## Step 2 — Confirm the workflow extensions are available

Ask for:

```text
hirmos list extensions
```

A compact example result could include:

```text
Available extensions
- requirements-agent
- system-design-agent
- implementation-agent
- hello-world
- pretty-output
```

## Step 3 — Run Requirements

Ask for:

```text
hirmos requirements
```

A compact example result might look like this:

```text
[HIRMOS]
Command resolved: hirmos requirements
Extension: requirements-agent
Entrypoint: requirements

[Requirements Agent]
Normalizing project inputs into requirements artifacts.
Reviewing assumptions, open questions, and gated requirements decisions.

Run state: paused

Gated unresolved requirements
1. Authentication scope is unclear
   Why it matters: user roles and protected workflows cannot be finalized yet.
   Proposed direction: ask customer

2. Notification delivery requirements are incomplete
   Why it matters: workflow timing and cross-system responsibilities remain unsettled.
   Proposed direction: defer and constrain

Artifacts updated
- _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md
- _hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
```

A paused Requirements run is useful. It means HIRMOS found decisions that should not silently become implementation assumptions.

## Step 4 — Handle Requirements decisions

For the example above, the Orchestrator can respond like this:

- **Authentication scope is unclear** → ask customer
  - Example direction: “Draft the exact questions we should send to confirm roles and protected actions.”

- **Notification delivery requirements are incomplete** → defer and constrain
  - Example direction: “Proceed assuming email notifications only for now, and explicitly constrain SMS or push notifications as out of scope until confirmed.”

After decisions are provided, rerun:

```text
hirmos requirements
```

The step may complete or pause again if new gated items remain.

## Step 5 — Run System Design

After Requirements is complete enough for design, ask for:

```text
hirmos system-design
```

A compact completed result might include:

```text
[HIRMOS]
Command resolved: hirmos system-design
Extension: system-design-agent
Entrypoint: system-design

[System Design Agent]
Reading requirements artifacts.
Producing system, architecture, phase, and staged delivery artifacts.

Artifacts updated
- _hirmos/artifacts/sot/SYSTEM_SOT.md
- _hirmos/artifacts/sot/ARCHITECTURE_SOT.md
- _hirmos/artifacts/sot/PHASES_SOT.md
- _hirmos/artifacts/phases/phase_1_foundation_SOT.md
- _hirmos/artifacts/context/system-design-agent/system-design/VALIDATION_TRACE.md

Run state: completed
```

## Step 6 — Run Implementation

After System Design and phase scope are approved, ask for:

```text
hirmos implementation
```

A first run often produces or refreshes implementation planning and then pauses for approval:

```text
[HIRMOS]
Command resolved: hirmos implementation
Extension: implementation-agent
Entrypoint: implementation

[Implementation Agent]
Reviewing approved System Design and selected phase scope.
Producing implementation planning artifacts and execution-ready prompts.

Run state: paused

Approval required
Implementation planning is complete.
Review the generated implementation plan and prompts before phase execution.

Artifacts updated
- _hirmos/artifacts/prompts/phase-01-foundation/
- _hirmos/artifacts/context/implementation-agent/implementation/VALIDATION_TRACE.md
```

After approval, rerun or continue according to the surfaced instruction. The Implementation step then executes the selected/current phase, validates the result, and finishes with Evidence-backed Review.

## What Evidence-backed Review should feel like

Evidence-backed Review should answer:

- What changed?
- What checks ran?
- What passed or failed?
- What repair was attempted, if any?
- What remains unresolved?
- Is the step completed, paused, or failed?
- What should happen next?

## Go next

- Read [Quickstart](quickstart.md) for the concise command path.
- Read [Core commands](core-commands.md) for command syntax.
- Read [Operator playbook](../orchestrator/operator-playbook.md) for decision handling.
