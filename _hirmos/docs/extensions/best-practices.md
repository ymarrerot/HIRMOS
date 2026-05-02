# Extension Authoring Best Practices

Use this page for practical design advice when you are writing or evolving an extension. The goal is to help you make good decisions quickly without turning this guide into a copied set of extension-local specs.

Need canonical doctrine for a specific surface? Use the targeted authority or extension-local spec references below only when you need exact rules:
- [Extension document roles](../../core/authority/extensions/extension-document-roles.md)
- [Extension README role](../../core/authority/extensions/extension-document-roles.md#extension-readme-role)
- [Extension entrypoints](../../core/authority/extensions/entrypoints.md)
- [Extension hooks](../../core/authority/extensions/hooks.md)
- [Extension manifests](../../core/authority/extensions/manifests.md)
- [Extension validation](../../core/authority/extensions/validation.md)
- [Extension naming conventions](../../core/authority/extensions/naming-conventions.md)
- [Extension stack consumption](../../core/authority/extensions/stacks.md)
- [Document design principles](../../core/authority/shared/document-design-principles.md)
- [Top-level folder definitions](../../core/authority/framework/top-level-folder-definitions.md)

## Beyond Clear Instructions

Use the practical guide to [Beyond Clear Instructions](./beyond-clear-instructions.md) whenever a runnable entrypoint should pair clear instructions with self-validation, and especially when the run also needs stronger synthesis or surfaced-output governance.


## Start with the smallest shape that works

Do not begin with a large extension structure unless the behavior actually needs it.

A simple entry file is usually enough when:
- the behavior is tiny
- the output is simple
- there is no meaningful artifact contract
- there is no strong local validation burden

A richer structure is usually helpful when:
- the entrypoint creates or refines an important artifact
- quality needs to be judged locally
- validation or repair logic matters
- the entrypoint will be reused by larger workflows or cycles

A good default is:
- small demo behavior → simple entry file
- serious workflow behavior → entrypoint + stronger local governance

## Keep the public surface small

Expose only the entrypoints the Orchestrator should actually run.

A healthy extension usually has:
- a small public command surface
- richer private supporting files behind it
- a clear difference between runnable entrypoints and internal support files

## Keep runnable surfaces easy to scan

A useful pattern is:
- **entrypoint** = runnable wrapper and minimal public execution-facing contract
- **deeper governance file** = local method, quality bar, validation, and artifact contract when needed

This keeps the runnable command easy to understand while preserving local discipline.

## Make the local quality bar visible when the work matters

If an artifact matters, say what “good enough” means locally.

A short concrete local quality bar is usually more helpful than a long general explanation.

## Preserve truth boundaries

Do not blur:
- confirmed facts
- assumptions
- proposals
- source-of-truth artifacts
- non-authoritative planning or working artifacts

If a distinction matters, make it visible.

## Be honest about uncertainty

When uncertainty materially affects downstream truth, contract shape, delivery feasibility, or operational readiness:
- surface it
- classify it
- pause when necessary

## Use runtime identity only when it helps orientation

If an extension benefits from a chat-facing runtime identity, declare `runtime.identity` in `extension.yaml`.

The Core owns runtime identity display behavior and formatting. Extension docs, templates, and entrypoints should not try to re-own that behavior.

## Design hooks at real seams

If your extension exposes hooks, expose them at real workflow seams where another extension may reasonably need to inspect, enrich, validate, or report.

Do not expose hooks just to seem flexible.

## Keep hook effects narrow

For Hook System v1, prefer bounded additive behavior.

Do not use hooks to bypass governance or hide major behavior changes.

## Keep starter templates separate from installed extensions

If you are creating a starter or scaffolding template for new framework objects, place it under `/_hirmos/extensions/_templates/...` rather than under `/_hirmos/extensions/`.

Keep local `templates/` folders inside extensions only for runtime or artifact-shaping templates that the installed extension actually uses.

## Use the framework's top-level folders instead of inventing new ones

As a practical rule, extensions should use the top-level folders HIRMOS already provides instead of inventing new ones.

For the authoritative folder meanings, use:
- [Top-level folder definitions](../../core/authority/framework/top-level-folder-definitions.md)


## Keep naming boring and clear

Good names are usually descriptive, not clever.

Prefer names that reveal:
- the extension family
- the artifact or workflow unit
- the command purpose
