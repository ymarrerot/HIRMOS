# Quickstart

Use this path when you want the shortest practical first run.

## 1. Install HIRMOS

Install HIRMOS into the project you want the AI agent to work on. A normal installation adds a project-local `_hirmos/` folder and tool-specific integration files.

If the CLI is not installed yet, install it from npm:

```bash
npm install -g hirmos
```

Then run the installer from the project root:

```bash
hirmos init
```

The terminal CLI installs HIRMOS. It does not run `hirmos start`, `hirmos continue`, `hirmos status`, or `hirmos close`.

For the complete CLI guide, including update checks and advanced install options, see [CLI Reference](../../reference/cli-reference.md).

## 2. Bootstrap the AI tool

In your AI coding tool, start a fresh agent context and say:

```text
Read and follow _hirmos/AGENTS.md
```

The generated integration file may do this automatically. The fallback prompt is useful when you want to be explicit.

## 3. Start the request

In the AI conversation, say something like:

```text
hirmos start "Add feature: login/sign up with Google"
```

Use a normal product or engineering request. You do not need to classify the project as greenfield, brownfield, or mixed. HIRMOS should inspect the current state and decide what capabilities are needed.

## 4. Expect current-state-first behavior

HIRMOS should not jump directly to implementation. It should begin with Understand System State, including the parts of the codebase, docs, source inputs, or existing artifacts that matter to the request.

A good first response should make clear:

- what HIRMOS inspected;
- what it understands about the request;
- what is in scope;
- what is unresolved;
- whether continuation is safe;
- exactly one recommended next command.

## 5. Answer only decisions that belong to you

If HIRMOS asks for input, it should distinguish:

- gated items that need your answer before affected work can proceed;
- non-gating assumptions it can carry safely for the current session;
- deferred or carry-forward items that should not be lost;
- technical-review items that another reviewer may inspect.

Do not feel obligated to answer every non-gating assumption before the first continuation.

## 6. Continue only through the next governed boundary

Use:

```text
hirmos continue
```

when HIRMOS says continuation is allowed.

If implementation units are required, HIRMOS should pause twice:

```text
Session Baseline accepted → IU Planning only
IU Plan accepted → IU Execution
```

This is intentional. It prevents implementation before the unit plan is visible and accepted.

## 7. Status or close

Use:

```text
hirmos status
hirmos close
```

`hirmos status` is read-only. `hirmos close` should update current system state and archive only when evidence supports the close claim.

## What a good quickstart feels like

```text
Tell HIRMOS what you want.
HIRMOS understands the current system.
HIRMOS designs the governed work.
HIRMOS asks only for decisions that matter.
HIRMOS implements only authorized work.
HIRMOS preserves accepted outcomes.
```
