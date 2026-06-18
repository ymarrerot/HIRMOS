# Glossary

## User Request

The entry trigger for HIRMOS work. It may include plain-language instructions, uploaded notes, tickets, screenshots, prototypes, or files. It guides focus but is not final authority.

## Understand System State

The lifecycle responsibility that establishes general and request-focused current system understanding before governed Design or Implementation.

## Design

The lifecycle responsibility that turns source inputs and system-state findings into governed requirements, design, delivery structure, Session Contract scope, decisions, and implementation readiness.

## Implementation

The lifecycle responsibility that realizes accepted Design through implementation units, project-file changes when authorized, validation, review, retry, and evidence. It is not limited to coding.

## Update System State

The lifecycle responsibility that records accepted outcomes, preserves history, carries forward unresolved items, and prepares future sessions. It is not implementation.

## Execution Control

A required control recorded in `SESSION_EXECUTION.md` that must be satisfied, blocked, pending, or not applicable before HIRMOS can claim progress or readiness.

## Gated Unresolved Item

An unresolved item that blocks the affected lifecycle boundary until resolved.

## Non-Gating Unresolved Item

An unresolved item that can be carried forward as an explicit assumption or constraint.

## Delivery Unit

A governed decomposition unit for delivery. A phase is the default Delivery Unit type when ordered staged delivery is natural.

## Session Contract

The Design-owned authority that defines what the current session may and may not do, and what Implementation is authorized to realize.


## Runtime integration posture

The internal HIRMOS classification for the actual level of a material runtime integration such as database, authentication, messaging, storage, deployment, or provider API.

Domain Expert users normally see a simplified recommendation and production-readiness decision, not the full internal taxonomy.

## Terminal CLI Command

A shell command run in a terminal. In current HIRMOS, the primary terminal CLI command is `hirmos init`, which installs framework and integration files into a project.

## Framework Workflow Command

A command phrase used inside an AI coding tool conversation, such as `hirmos start`, `hirmos status`, `hirmos continue`, or `hirmos close`. These commands are executed through the AI-tool integration and HIRMOS framework instructions, not by the terminal CLI.

## Integration Tool

An AI coding tool or agent environment that can read HIRMOS bootstrap instructions, such as Cursor, Claude, Copilot, Codex, OpenCode, Gemini, Windsurf, Kiro, or an AGENTS.md-compatible environment.

## Capability

A modular unit of HIRMOS behavior contributed by an extension. Capabilities produce governed artifacts, findings, evidence, controls, or implementation outputs under core lifecycle authority.

## Entrypoint

A framework file that describes how an extension or capability is activated and what it produces. Runnable entrypoints expose an execution contract with purpose, produced outputs, and terminal states.
