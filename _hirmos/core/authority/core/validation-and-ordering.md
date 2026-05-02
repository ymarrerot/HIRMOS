# Validation and Ordering v1

## Core validation checks

The framework should validate:
- one `extension.yaml` per extension folder;
- unique extension ids;
- `version` is present and readable as semantic version text;
- `requires_core` is present;
- valid `type`;
- `id` matches the folder name;
- existing `entry` file for runnable extensions;
- existing `entrypoints` paths;
- valid `requires` targets;
- valid `exposes_hooks` objects;
- valid `hooks` subscription objects.

## Hook validation checks

### Exposed hooks

Validate:
- required fields exist: `name`, `entrypoint`, `phase`, `summary`;
- names are unique within the owning extension;
- `entrypoint` names an actual public entrypoint of the owning runnable extension;
- optional `effects` and `required_context` fields are well-formed when present.

### Hook subscriptions

Validate:
- required fields exist: `target`, `file`;
- the referenced hook file exists;
- `priority`, when present, is numeric;
- `target` matches a declared exposed hook.

## Unknown targets and missing files

- Unknown hook targets are invalid for a trusted run plan.
- Missing hook files are invalid.
- These issues should fail validation clearly rather than disappearing silently.

## Ordering model

Matching hook subscriptions execute using this deterministic order:
1. ascending numeric `priority`;
2. declaration order inside the contributing extension manifest;
3. ascending contributing extension id across extensions.

## Priority model

The framework uses a WordPress-style priority model:
- lower numbers run earlier;
- higher numbers run later;
- default priority is `10`;
- common late priorities such as `99` and `9999` are allowed when intentional.

## Failure handling

If a hook cannot run:
- record the issue in traces;
- surface it in chat-facing reporting when material;
- pause the active run if trustworthy continuation depends on that hook;
- otherwise continue with warning.
