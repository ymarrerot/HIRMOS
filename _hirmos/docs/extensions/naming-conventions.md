# Naming Conventions

Use this page when you want practical naming guidance for extension ids, entrypoints, hooks, and related surfaces. Good naming reduces friction for both operators and authors, especially as extensions begin to support more parts of the SDLC.

Need the canonical naming and reference rules? See:
- [Extension naming conventions](../../core/authority/extensions/naming-conventions.md)
- [Authority surface rules](../../core/authority/shared/cross-folder-rules.md)
- [Deep reference rules](../../core/authority/shared/deep-reference-rules.md)
- [Top-level folder definitions](../../core/authority/framework/top-level-folder-definitions.md)

## Extension ids

Use lowercase letters, numbers, and hyphens only.
Match the extension folder name.

## Entry files

Use `index.md` for the main entry file unless there is a strong reason not to.

## Hook files

Use hook-target-based names that help humans understand the subscription quickly, for example:

```text
hooks/system-design-cycle.before-requirements-normalization.md
hooks/hello-world.after-main-output.md
```

## Hook names

Prefer namespaced hook names that reveal ownership and the workflow seam.

## Extension docs

Use `README.md` inside each extension for local documentation.
