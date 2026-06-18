# Command Reference

This page summarizes the command surfaces users see when working with HIRMOS.

There are two different command layers:

```text
Terminal CLI command:
  hirmos init

Framework workflow commands inside an AI coding tool:
  hirmos start
  hirmos status
  hirmos continue
  hirmos close
```

Do not confuse these layers.

## Terminal CLI command

### `hirmos init`

Run this in a project repository to install HIRMOS framework files and supported AI-tool integration files.

The terminal CLI installs the framework payload. It does not run the HIRMOS software-work lifecycle by itself.

## Framework workflow commands

After installation, open the project in a supported AI coding tool. The generated integration file is the normal bootstrap path for HIRMOS.

If the tool integration is not available or did not load, use this fallback bootstrap prompt:

```text
Read and follow _hirmos/AGENTS.md
```

Then use framework workflow commands in the AI-agent conversation.

### `hirmos start "<request>"`

Starts a governed HIRMOS work session for the user request.

Expected behavior:

- understand current system state;
- classify the work context from the project, not from user hints alone;
- identify source inputs;
- establish or update session artifacts;
- surface gated unresolved items and non-gating assumptions where relevant;
- pause before implementation when implementation is not yet authorized;
- recommend exactly one next command.

### `hirmos status`

Reports current session or delivery status.

Expected behavior:

- summarize active lifecycle state;
- report unresolved blockers and assumptions;
- report implementation-unit or phase progress where applicable;
- explain whether continue or close is legal;
- recommend exactly one next command.

### `hirmos continue`

Continues authorized work inside the current session.

Expected behavior:

- append cumulative execution history;
- execute or review the next authorized slice;
- preserve evidence;
- update unresolved items and session review state;
- avoid overwriting earlier execution context.

### `hirmos close`

Closes a session only when close conditions are satisfied.

Expected behavior:

- verify session contract completion;
- reconcile unresolved items;
- preserve evidence in history;
- update durable current system state;
- reset active session state safely.

## Why workflow commands are not terminal CLI commands

HIRMOS workflow commands require AI-agent reasoning over the current project, source materials, artifacts, unresolved items, and implementation evidence. A thin shell command cannot perform that work honestly.

The terminal CLI installs HIRMOS. The AI coding tool runs HIRMOS workflow through the framework instructions.

