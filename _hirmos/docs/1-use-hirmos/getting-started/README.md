# Getting Started

This is the lowest-cognitive-load path for using HIRMOS for the first time.

If you only remember one thing from this page, remember this:

```text
Install HIRMOS, let the AI tool bootstrap from _hirmos/AGENTS.md, then use hirmos start inside the agent conversation.
```

The generated integration file is the normal bootstrap path. Directly prompting the agent to read `_hirmos/AGENTS.md` is the fallback when you are not using the CLI yet, installed manually, or the AI tool did not load its generated integration file.

## What HIRMOS is

HIRMOS is an orchestration framework for AI-assisted software development.

It helps AI coding agents work from the current state of a project, organize work into governed sessions, preserve decisions and evidence, and scale from small changes to larger deliveries without losing context.

The HIRMOS lifecycle is:

```text
User Request
↓
Understand System State
→ Design
→ Implementation
→ Update System State
```

The lifecycle is ordered, but not waterfall. HIRMOS can route back when new facts, missing design authority, unresolved decisions, or failed evidence show that the current step is not ready.

## HIRMOS chooses the smallest honest work shape

You do not need to choose the artifact model yourself. HIRMOS should select the lightest safe route for the request:

| Request shape | Typical route | First pause |
|---|---|---|
| Small bounded work | single governed session | Session Baseline or Recommended Baseline |
| Requirements/design only | design session | Review or Change output |
| Single-session implementation | accepted session scope | Session Baseline — Review or Change |
| Larger MVP/release | Delivery Plan and Delivery Baseline | Delivery Baseline — Review or Change |
| Implementation with units | IU Planning before IU Execution | IU Plan — Review or Change |

When IU mode applies, accepting the session baseline creates the IU plan. It does not authorize material implementation. IU Execution begins only after the IU plan is accepted.

## What the install looks like

A normal install keeps your project files and adds one project-local framework folder:

```text
your-project/
├── package.json or other project files
├── app/ or src/ or services/
└── _hirmos/
```

You do not need to learn every folder before the first run. The important points are:

- your project remains your project;
- `_hirmos/` contains the installed framework;
- generated AI-tool integration files point the agent to `_hirmos/AGENTS.md`;
- active session artifacts are created only when governed work starts.

## Step 1 — Install HIRMOS

See [Installation](installation.md).

## Step 2 — Bootstrap the AI tool

Open the project in the AI coding tool selected during `hirmos init`. The generated integration file is the normal bootstrap path.

If the tool integration is not available or did not load, use this fallback bootstrap prompt:

```text
Read and follow _hirmos/AGENTS.md
```

The agent must complete full bootstrap before advancing commands (`hirmos start`, `hirmos continue`, `hirmos close`). `hirmos status` may use the framework's strictly read-only bootstrap fast path.

## Step 3 — Start with a request

Use a normal user request:

```text
hirmos start "Add Google login"
```

or, when the request is already clear from the conversation or uploaded files:

```text
hirmos start
```

`hirmos start` is not a terminal command. It is the framework command you give to the AI agent inside the integration tool.

## Step 4 — Review what HIRMOS reports

A good start should not jump straight to coding. HIRMOS should first explain what it understands, what current state it inspected, what work appears in scope, what is unresolved, and what the next safe command is.

Possible first pauses include:

- `Recommended Baseline — Review or Change` for lighter bounded work;
- `Session Baseline — Review or Change` for bounded session work;
- `Delivery Baseline — Review or Change` for larger durable work.

## Step 5 — Continue only when continuation is allowed

Use:

```text
hirmos continue
```

when the active checkpoint, unresolved items, and execution controls allow continuation.

For implementation sessions with IUs, expect two separate continuation boundaries:

```text
hirmos continue "Accept session baseline and create IU plan"
hirmos continue "Accept IU plan and begin IU execution"
```

## Step 6 — Inspect status or close

Use:

```text
hirmos status
hirmos close
```

`status` should be read-only. `close` should update system state and archive the session only when close readiness is satisfied.

## What you do not need to learn yet

For the first run, you do not need to study every extension, template, stack package, protocol, or validation-tool implementation. Bootstrap and the active command should tell the agent what to read when it becomes necessary.
