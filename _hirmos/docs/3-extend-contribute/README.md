# 3 — Extend & Contribute

Use this lane when you want to understand, extend, validate, or contribute to HIRMOS itself.

Most users do not need this lane for a normal project run. If you only want to use HIRMOS on a software project, start with [1 — Use HIRMOS](../1-use-hirmos/README.md).

## What this lane covers

This lane explains the public contributor surface of HIRMOS:

- the framework structure;
- the bundled extension and capability model;
- canonical entrypoint surfaces;
- validation and regression expectations;
- how contribution work should preserve the current framework shape.

It does not replace the private framework-maintainer playbook used for release, packaging, private/public propagation, and publishing workflow.

## Start here

| I want to... | Read |
|---|---|
| Understand the main framework folders | [Framework Structure](framework-structure.md) |
| Understand extensions, capabilities, and entrypoints | [Capabilities and Entrypoints](capabilities-and-entrypoints.md) |
| Validate a framework change | [Validation](validation.md) |
| Look up artifact names | [Artifact Model](../reference/artifact-model.md) |
| Look up installation/integration targets | [Integration Tools](../reference/integration-tools.md) |
| Look up terminology | [Glossary](../reference/glossary.md) |

## Contributor posture

HIRMOS is simple for users because the framework carries rigor underneath. Contribution work should preserve that balance:

```text
Simple by default.
Transparent by design.
Rigorous underneath.
Progressive in disclosure.
```

Good contributions usually make one of these things clearer:

- what the AI agent should do;
- what the user should see;
- what artifact owns a decision;
- what validation proves;
- what future sessions can rely on.

## Extension model

The baseline framework includes three bundled stage-aligned extensions:

- `system-state-agent`
- `design-agent`
- `implementation-agent`

Extensions bundle capabilities. They do not own the overall lifecycle.

Core owns:

- lifecycle authority;
- command routing;
- execution controls;
- unresolved-item governance;
- artifact model;
- validation and evidence rules;
- accepted-state update safety.

## Capability entrypoint contract

Runnable extension and capability entrypoints expose a minimal execution contract:

```text
Purpose
Produces
Terminal States
```

A capability may contribute execution controls and unresolved-item producer obligations, but it must not invent a separate lifecycle.

## Before changing framework internals

Before editing core protocols, templates, validators, extensions, or integration templates:

1. Read the relevant docs and protocol files.
2. Identify the canonical source of the behavior you are changing.
3. Update both private and public framework copies when required.
4. Run validation and regression checks.
5. Keep public onboarding docs simpler than internal protocol detail.

