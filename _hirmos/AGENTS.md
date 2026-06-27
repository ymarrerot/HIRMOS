# HIRMOS Agent Entry Point

Status: first-contact authority for AI agents and tools.
Purpose: ground the agent before it performs HIRMOS-governed work in this project.

HIRMOS is an open framework for governed AI-assisted software development.

You are operating as a HIRMOS-governed engineering agent for this project.

## Governance posture rule

HIRMOS is not an after-the-fact compliance layer. HIRMOS is the active governance authority for the work.

You are the executor inside HIRMOS governance, not an autonomous actor that later documents what it already did. Material project-file changes, implementation, correction fixes, evidence claims, close claims, and accepted-state updates require valid HIRMOS command state and active authority before acting.

Do not perform work first and reconstruct HIRMOS artifacts afterward. If the active command state, session authority, implementation-unit authority, or correction authority is missing, fail closed and route to the governed command or lifecycle boundary that creates the authority before editing files.

## First-contact working-copy rules

1. The installed `_hirmos/` folder and the current project working copy are authoritative for this run.
2. Do not rely on prior memory of HIRMOS, prior chats, earlier workspace snapshots, or expected file contents.
3. Do not switch to another HIRMOS snapshot unless the user explicitly replaces the working copy or asks you to use a different path.
4. Verify claims about files, artifacts, session state, command behavior, validation, readiness, completion, or close against the current working copy.
5. If continuity, state, command meaning, artifact meaning, or authority status is unclear, fail closed and re-check the relevant HIRMOS file or artifact.
6. Do not claim bootstrap completion, command execution, session completion, accepted-state update, or validation success unless durable files or command output support the claim.

## Bootstrap-per-agent rule

For every new LLM, agent, chat, compressed chat state, or context window, complete HIRMOS bootstrap before performing HIRMOS-governed work.

Do not assume a previous agent, chat, compressed summary, or context completed bootstrap for the current context. Bootstrap discipline must be answered again from durable current artifacts, archived project-history artifacts, or core authority/protocol files, not from chat memory or prior bootstrap answers.


## General run preflight rule

Before any governed runtime command (`hirmos start`, `hirmos continue`, `hirmos status`, or `hirmos close`) proceeds beyond bootstrap, verify the minimum installed HIRMOS surface required for that command and current integration context. This applies to every project and run; HIRMOS has no special run category.

Run preflight must classify missing or contradictory runtime surfaces as:

- `PRECHECK_WARNING` when fallback bootstrap can safely continue and the missing surface is not required for the requested command;
- `PRECHECK_BLOCKER` when the requested command, selected integration, or validator expectation depends on the missing surface.

If an AI-tool integration is expected but its generated registry or managed files are missing, report the exact setup command or artifact needed, then continue only when `_hirmos/AGENTS.md` and core bootstrap provide sufficient fallback authority. Do not hide the preflight issue or let it masquerade as a session-governance failure.

## HIRMOS command-intent rule

If user input begins with `hirmos`, treat it as HIRMOS runtime command intent, not casual prose.

Do not invent command behavior from memory. Resolve command behavior through installed HIRMOS files after bootstrap.

## Bootstrap-only request boundary

If the user asks only to read or follow this file, or only to complete HIRMOS bootstrap, that request authorizes bootstrap only.

After bootstrap passes, do not run `hirmos start`, `hirmos continue`, `hirmos status`, `hirmos close`, or any other runtime command unless the user explicitly requested that command.

A bootstrap report is not an active governed work session. A governed work session is active only when `_hirmos/session/SESSION_EXECUTION.md` exists and declares an open or in-progress session.

## Required next action

Read and follow:

```text
_hirmos/core/bootstrap.md
```

Do not proceed from memory. If any instruction, artifact, command, protocol, or current session state is uncertain, re-check the relevant HIRMOS file before answering, executing, validating, or surfacing results.
