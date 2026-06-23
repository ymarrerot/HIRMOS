# Framework Command Reference

This page summarizes the HIRMOS framework workflow commands used inside an AI coding tool after HIRMOS has been installed and bootstrapped.

For terminal CLI usage, see the complete [CLI Reference](cli-reference.md).

## Framework workflow commands

After installation, open the project in a supported AI coding tool. The generated integration file is the normal bootstrap path for HIRMOS.

If the tool integration is not available or did not load, use this fallback bootstrap prompt:

```text
Read and follow _hirmos/AGENTS.md
```

Then use framework workflow commands in the AI-agent conversation.

These are not terminal CLI commands.

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

- verify session scope completion;
- reconcile unresolved items;
- preserve evidence in history;
- update durable current system state;
- reset active session state safely.

## Why workflow commands are not terminal CLI commands

HIRMOS workflow commands require AI-agent reasoning over the current project, source materials, artifacts, unresolved items, and implementation evidence. A thin shell command cannot perform that work honestly.

The terminal CLI installs HIRMOS. The AI coding tool runs HIRMOS workflow through the framework instructions.
