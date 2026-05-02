# INSTALLATION_MODEL.md

## Installation model

An extension should be installable by copying its directory into:

```text
_hirmos/extensions/
```

No central file edits should be required.

## Discovery model

The framework discovers installed extensions by scanning:

```text
_hirmos/extensions/*/extension.yaml
```

## Why this matters

Drop-in install and uninstall are critical for maintainability:

- add an extension by copying one folder;
- remove an extension by deleting one folder;
- avoid merge conflicts in shared registry files;
- keep ownership local to the extension itself.

## Optional future packaging

This framework can later support packaged extension bundles, registries, or signed extension archives, but the local folder contract should remain the base install model.
