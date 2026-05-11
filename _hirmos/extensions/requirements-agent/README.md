# requirements-agent

Official HIRMOS extension for the **Requirements** step in Orchestrated Spec-Driven Development.

## Public command

```text
hirmos requirements
```

## Purpose

Turn user-provided goals, context, notes, prototypes, user stories, files, attachments, bounded repository context, and constraints into requirements artifacts suitable for System Design.

## Produces

- `_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`
- `_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`
- project-level unresolved-item artifacts under `_hirmos/artifacts/context/requirements-agent/requirements/` when required

## Important governance rule

This extension contributes unresolved assumptions, open questions, and gated requirements decisions through the existing HIRMOS unresolved-item governance pattern.

It must not create a separate Requirements-only unresolved-decision bypass artifact.

## Next workflow step

When Requirements completes, proceed to:

```text
hirmos system-design
```

## Status

This extension is the official Requirements extension for the regular-user workflow.


## Input sources

Requirements input can come from the current prompt/session, optional command argument text, online attachments, files under `_hirmos/inputs/requirements-agent/requirements/`, explicit bounded local file references, or hook-derived artifacts from installed extensions.

The `_hirmos/inputs/requirements-agent/requirements/` folder is a project runtime surface. It is not shipped inside the extension package; the active Core/entrypoint path creates missing runtime folders during init or first run when needed.
