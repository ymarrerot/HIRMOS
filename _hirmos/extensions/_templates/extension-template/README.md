# extension-template

## Purpose

Starter material for building a new extension.

This template is intentionally small. It gives you the minimum runnable extension shape that matches the current HIRMOS authoring model, then lets you add docs, entrypoints, hooks, extension-local specs, and templates only when the extension actually needs them.

## Default public entrypoint

- `index.md`

## Named public entrypoints

- none by default

## Exposed hooks

- none by default

## Hook subscriptions

- none by default

## Artifacts read

- none by default

## Artifacts produced

- none by default

## Extension-local specs

- none by default

## Included starter files

- `README.md` — extension landing page
- `extension.yaml` — minimal runnable manifest
- `index.md` — default public entrypoint with the required execution contract

## What to customize first

1. Rename the folder to your real extension id.
2. Update `extension.yaml` with the real `id`, `summary`, and any additional fields you truly need.
3. Replace `index.md` with the real public entrypoint instructions and honest terminal states.
4. Rewrite this README so it explains the extension as an installed package rather than as a template.

## When to grow beyond this starter

Add more structure only when the extension truly needs it:
- add `entrypoints/` when you need named public entrypoints
- add `hooks/` only when the extension subscribes to exposed hooks
- add `specs/` only when the extension needs deeper extension-local method or contracts
- add `templates/` only when the extension owns reusable output or artifact structure
- add `docs/` when extension-local user guidance would materially help

## Related guidance

Use these when you need the deeper framework rules:
- `../../../docs/3-extend-contribute/extensions/creating-your-first-extension.md`
- `../../../docs/3-extend-contribute/extensions/public-entrypoints.md`
- `../../../docs/3-extend-contribute/extensions/spec-backed-entrypoints.md`
- `../../../core/authority/core/extension-manifest-authority.md`
- `../../../core/authority/core/entrypoint-execution-contract.md`
