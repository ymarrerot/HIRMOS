# Example: Hello World

`hello-world` is the smallest runnable extension in the package.

## Bootstrap reminder

Before using the framework, bootstrap the core through `HIRMOS_CORE.md`.

## Structure

```text
_hirmos/extensions/hello-world/
├── README.md
├── CHANGELOG.md
├── UPGRADE_GUIDE.md
├── extension.yaml
└── index.md
```

## Manifest

```yaml
id: hello-world
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - runnable
summary: Prints a hello world message.
entry: index.md
```

## Entrypoint

`index.md` is the default public entrypoint.

## Note

This example is intentionally simple and does not need a Spec.
