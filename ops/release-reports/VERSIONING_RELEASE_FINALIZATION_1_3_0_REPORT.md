# HIRMOS Versioning / Release Finalization Report — 1.3.0

## Status

Complete and validated.

## Release version

```text
1.3.0
```

## Release date

```text
2026-05-10
```

## Changes applied

- Updated `_hirmos/VERSION` from `1.2.0` to `1.3.0` in `_private` and `_public`.
- Updated `_hirmos/tools/cli/package.json` from `0.1.0` to `1.3.0` so the bundled product-facing CLI source aligns with the framework release.
- Converted `_hirmos/CHANGELOG.md` `[Unreleased]` entries into a dated `1.3.0` section.
- Reset `[Unreleased]` to `No unreleased changes yet.`
- Replaced the upgrade-guide placeholder `Upcoming command/config migration after 1.2.0` with `Upgrading to 1.3.0`.
- Preserved historical 1.2.0 notes as historical compatibility context.

## Release highlights

- Developer-productized initialization path through `hirmos init`.
- TypeScript CLI v1 source under `_hirmos/tools/cli/`.
- Agent/IDE/tool integration assets under `_hirmos/integrations/agent-tools/`.
- Active HIRMOS workflow command grammar: `hirmos <command>[:entrypoint] [arguments]`.
- `_hirmos/project.json` replaces `_hirmos/STACK_CONFIG.json`.
- Release package renamed to `hirmos-framework.zip`.
- Release package includes the free regular-user workflow extensions:
  - `requirements-agent`
  - `system-design-agent`
  - `implementation-agent`
- Release/source layout preserves one target-project root folder: `_hirmos/`.

## Validation run

```text
npm --prefix _private/_hirmos/tools/cli test
npm --prefix _public/_hirmos/tools/cli test
./ops/scripts/package-hirmos-framework.sh
./ops/scripts/package-other-extensions.sh
./ops/scripts/verify-packages.sh
./ops/scripts/verify-independence.sh
./ops/scripts/update-public-repo.sh
(cd _public && ./ops/scripts/verify-repo.sh)
npm --prefix _public/_hirmos/tools/cli test
```

## Validation result

```text
passed
```

## Package verification notes

- `ops/dist/hirmos-framework.zip` contains `_hirmos/VERSION` = `1.3.0`.
- `ops/dist/hirmos-framework.zip` contains `_hirmos/tools/cli/package.json` = `1.3.0`.
- `ops/dist/hirmos-framework.zip` includes `_hirmos/integrations/agent-tools/`.
- `ops/dist/hirmos-framework.zip` includes `_hirmos/tools/cli/`.
- `ops/dist/hirmos-framework.zip` includes the free regular-user workflow extensions.
- `ops/dist/hirmos-framework.zip` excludes root-level `packages/` and legacy `_hirmos/agent-integrations/`.
