# 1 — Use HIRMOS for Software Work

This lane is for people who want to use HIRMOS on a real software project without learning every framework internal first.

HIRMOS works inside your AI coding tool. The terminal CLI installs the framework and tool-integration files. In normal use, the generated integration file bootstraps the AI tool into HIRMOS; direct prompting with `_hirmos/AGENTS.md` is the fallback when the CLI integration is unavailable or not loaded.

## Start here

1. [Quickstart](getting-started/quickstart.md) — the shortest safe path from installation to first use.
2. [Installation](getting-started/installation.md) — install HIRMOS and choose supported AI-tool integrations.
3. [Commands](getting-started/commands.md) — understand `hirmos start`, `hirmos status`, `hirmos continue`, and `hirmos close` as framework workflow commands, not terminal CLI commands.
4. [First Real Run](getting-started/first-real-run.md) — what to expect when HIRMOS handles real work.
5. [Working with Existing Projects](getting-started/working-with-existing-projects.md) — how HIRMOS should approach brownfield or mixed projects.
6. [Multi-Session Work](getting-started/multi-session-work.md) — how larger deliveries are carried across more than one session.
7. [Getting Started](getting-started/README.md) — the expanded first-use guide.

## Normal workflow

```text
Install HIRMOS
→ open your AI coding tool
→ let the generated tool integration bootstrap HIRMOS
If the tool integration is not available or did not load, use the fallback bootstrap prompt:

```text
Read and follow _hirmos/AGENTS.md
```
→ use hirmos start "<your request>" inside the AI conversation
→ review what HIRMOS understood, what is unresolved, and what it recommends next
→ continue, check status, or close when HIRMOS says that action is safe
```

## What HIRMOS should do for you

HIRMOS helps the AI agent:

- start from the current state of the project, not from a guessed ideal state;
- separate user requests, source inputs, accepted design, implementation evidence, and durable current state;
- track unresolved decisions, assumptions, blockers, and carry-forward work;
- break implementation into bounded, reviewable work;
- preserve evidence before claiming completion;
- update durable current system state when a session closes.

## What you do not need to learn first

For the first run, you do not need to study every protocol, template, extension, stack file, or validator. HIRMOS uses progressive disclosure: the active command should lead the agent to the files it needs for the current work.

## What to read next

- New installation: start with [Installation](getting-started/installation.md).
- First task: start with [Quickstart](getting-started/quickstart.md).
- Existing codebase: read [Working with Existing Projects](getting-started/working-with-existing-projects.md).
- Larger effort: read [Multi-Session Work](getting-started/multi-session-work.md).
