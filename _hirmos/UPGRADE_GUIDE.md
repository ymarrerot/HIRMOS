# HIRMOS Upgrade Guide

This file is the concrete upgrade guidance surface for the framework.

For the authoritative framework-wide versioning doctrine, see:
- [Versioning contract](./core/authority/framework/versioning-contract.md)

## Upgrading to 1.3.2

This patch release keeps the framework package and the published `hirmos` npm CLI aligned after adding a non-blocking CLI update notice.

### What changed

- `hirmos init` now checks the npm registry for a newer published CLI version and prints a non-blocking update notice when one is available.
- The notice does not prevent initialization and is skipped when the check fails, times out, or is disabled.
- `hirmos init --offline` disables both remote framework download and the npm update check.
- Set `HIRMOS_CLI_UPDATE_CHECK=0` to disable only the npm update notice while still allowing normal remote framework download.

### Required actions

- Publish a matching GitHub Release `v1.3.2` with `hirmos-framework.zip` before publishing `hirmos@1.3.2` to npm.
- Existing users can update the CLI with:

```bash
npm install -g hirmos@latest
```

### Compatibility notes

- Existing `hirmos@1.3.1` installations continue to work, but they will not show the new update notice.
- The update check is best-effort and non-blocking; network failures do not fail `hirmos init`.

## Upgrading to 1.3.1

This patch release coordinates the framework package and the published `hirmos` npm CLI after adding remote GitHub release installation support.

### What changed

- `hirmos init` can now install `_hirmos/` automatically from GitHub Releases when the target project does not already contain `_hirmos/` and `--source` is not provided.
- `hirmos init --version <version>` can install a specific framework release, accepting both `1.3.1` and `v1.3.1` style values.
- `hirmos init --offline` disables remote download and fails clearly when `_hirmos/` is missing.
- Public onboarding now leads with `npm install -g hirmos` followed by `hirmos init`.
- The release packaging script now emits GitHub release helper notes and SHA-256 checksum output in `ops/dist/`.

### Required actions

- Before publishing `hirmos@1.3.1` to npm, create a matching GitHub Release `v1.3.1` with `hirmos-framework.zip` attached.
- Use `ops/scripts/package-hirmos-framework.sh` to regenerate `hirmos-framework.zip`, `hirmos-framework-github-release.md`, and `hirmos-framework-SHA256SUMS.txt`.
- Keep npm CLI versions and GitHub framework release tags aligned for public releases.

### Compatibility notes

- Existing `hirmos@1.3.0` installations can still run `hirmos init`; however, users should upgrade to `hirmos@1.3.1` to get the remote release install behavior.
- Local/offline installs with `hirmos init --source <path>` remain supported.

## Upgrading to 1.3.0

This release moves HIRMOS from a framework/manual-first experience toward a developer-product entry path while preserving the canonical Core bootstrap fallback.

The generated install archive is now `hirmos-framework.zip` instead of `hirmos-core-framework.zip`. The release package includes the free regular-user workflow extensions (`requirements-agent`, `system-design-agent`, and `implementation-agent`) and no longer treats them as separate add-on zips.

Repo-root `AGENTS.md` is no longer shipped in the private/public source roots. `AGENTS.md` is generated in target projects by `hirmos init` only when an integration selection requires it.

The product-facing CLI source now lives under `_hirmos/tools/cli/` instead of root-level `packages/cli/`. Agent/IDE/tool integration assets now live under `_hirmos/integrations/agent-tools/` instead of `_hirmos/agent-integrations/`. This preserves the target-project first impression as a single `_hirmos/` install surface.

Ops script names were also aligned with the release model: use `ops/scripts/package-hirmos-framework.sh` for the main framework package, `ops/scripts/package-other-extensions.sh` for optional/private extension packages, and `ops/scripts/update-public-repo.sh` to refresh `_public/`. `install-hirmos.sh` remains an internal/local install helper, not the public onboarding path.

### What changed

- `_hirmos/STACK_CONFIG.json`, the previous stack-only config file, is replaced by `_hirmos/project.json`.
- HIRMOS now includes agent/tool integration templates under `_hirmos/integrations/agent-tools/`, a TypeScript CLI source package under `_hirmos/tools/cli/` implementing `hirmos init`, and onboarding docs for the productized initialization path.
- The CLI generates thin bootstrap/context files and can install `_hirmos/` from a local source folder or local release package when `_hirmos/` is missing. It does not invoke agents, run HIRMOS workflow commands, or install tool-native command packs.
- Active stack selection now lives at `stack.active_stack` inside `_hirmos/project.json`.
- Extension manifests may declare user-facing workflow commands through `hirmos_commands`.
- The active workflow command grammar is:

```text
hirmos <command>[:entrypoint] [arguments]
```

Examples:

```text
hirmos requirements
hirmos system-design
hirmos implementation
hirmos system-design:phase-design-cycle
```

### Required actions

- Use `hirmos init` from a project root to generate selected agent/tool bootstrap files. Use `--source` for local/offline release packages when installing into a project that does not already contain `_hirmos/`.

- Update onboarding docs or local team instructions to distinguish the terminal CLI command `hirmos init` from HIRMOS workflow commands such as `hirmos requirements`, which are used inside the AI tool after Core bootstrap.
- Replace any local references to `_hirmos/STACK_CONFIG.json` with `_hirmos/project.json`.
- If you customize `hirmos init`, preserve existing user-owned integration files outside the HIRMOS managed block markers.
- Do not treat `_hirmos/integrations/agent-tools/` as Core runtime behavior. It is a HIRMOS productization/tool-discovery adapter surface that points agent tools to `_hirmos/HIRMOS_CORE.md`.
- Update custom extension manifests to declare `hirmos_commands` for any user-facing runnable workflows.
- Update local docs or scripts that still reference the pre-1.3.0 `cmd:` command surface, including forms such as `cmd: run extension <id>`.
- Update local ops references to use `package-hirmos-framework.sh`, `package-other-extensions.sh`, and `update-public-repo.sh`.

### Compatibility notes

- No compatibility alias is kept for the pre-1.3.0 `cmd:` command surface in active framework files.
- `_hirmos/VERSION` remains the only framework version source of truth. Do not duplicate the framework version in `_hirmos/project.json`.
- Official extension manifests remain compatible with Core 1.3.0 through `requires_core: ">=1.0.0 <2.0.0"`.

## Upgrading to 1.2.0

This release completes the public front-door simplification, methodology documentation, documentation information architecture, and project-level unresolved-item governance work.

### What changed

#### Public workflow
- The regular HIRMOS workflow is now documented as:

```text
Requirements → System Design → Implementation
```

- The three executable backing commands introduced in 1.2.0 were:

```text
cmd: run extension requirements-agent
cmd: run extension system-design-agent
cmd: run extension implementation-agent
```

These are historical 1.2.0 commands. The later DP-1 developer-productization migration changes the active command language to `hirmos <command>[:entrypoint] [arguments]`.

#### Requirements step
- `requirements-agent` is now the official Requirements extension.
- Requirements ownership moved out of the public System Design workflow.
- Requirements inputs may come from the current prompt/session, online attachments, the runtime input folder, bounded local file references, and hook-derived artifacts.

#### System Design and Implementation defaults
- `system-design-agent` now exposes `entrypoints/system-design.md` as its default public entrypoint.
- The System Design default entrypoint composes the narrowed `system-design-cycle` and `phase-design-cycle`.
- For normal greenfield completion, phase design is required before System Design may claim completion.
- `implementation-agent` now exposes `entrypoints/implementation.md` as its default public entrypoint.
- Implementation preserves the planning approval pause before execution.

#### Unresolved-item governance
- The canonical unresolved-item inventory moved to the project-level context namespace:

```text
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
```

- Related project-level unresolved-item artifacts are:

```text
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
```

- Producers that surface canonical unresolved items must refresh their own artifact-scoped inventory section inline before leaving the producer workflow.

#### Documentation
- Documentation now uses numbered progressive-disclosure lanes:

```text
_hirmos/docs/1-use-hirmos/
_hirmos/docs/2-methodology/
_hirmos/docs/3-extend-contribute/
_hirmos/docs/reference/
```

- Old first-level docs folders such as `getting-started/`, `extensions/`, `core/`, `framework/`, `examples/`, and `orchestrator/` were moved into these lanes.
- The root README was rewritten as the main GitHub landing page for HIRMOS.

#### Methodology and terminology
- Orchestrated Spec-Driven Development is documented as the methodology HIRMOS implements.
- The reliability pattern is now **Beyond Clear Specs**.
- Pillar 1 is now **Clear Specs**.

#### Initialization
- The canonical first-contact bootstrap remains:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

- The historical note above has been superseded by the post-1.2.0 DP-3B and DP-4 productization work, which adds a TypeScript `hirmos init` CLI source package under `_hirmos/tools/cli/` and updates public onboarding docs for the CLI initialization path.

### Required actions

- Use `hirmos init` from a project root to generate selected agent/tool bootstrap files. Use `--source` for local/offline release packages when installing into a project that does not already contain `_hirmos/`.
- Update local links or bookmarks that point to old docs paths.
- Update any custom extension or project docs that reference the old stage-scoped unresolved-item inventory paths.
- Update any custom docs that still use the old reliability-pattern terminology.
- Use `hirmos init` when the CLI is available to generate agent-native bootstrap files. Continue to use the explicit first-contact bootstrap instruction as the canonical fallback and authority-loading prompt.

### Compatibility notes
- Official extension manifests remain compatible with Core 1.2.0 through `requires_core: ">=1.0.0 <2.0.0"`.
- Historical outputs may still reference old docs paths, stage-scoped unresolved-item paths, or previous terminology. Treat those as historical artifacts unless a live framework file still points to them.

## Upgrading to 1.1.0

This release promotes the new assembled bootstrap as the primary runtime bootstrap path, simplifies the supporting Core authority graph, and standardizes the reliability-pattern surfaces as **Beyond Clear Specs**.

### What changed

#### Bootstrap and Core runtime
- `/_hirmos/core/bootstrap.md` is now the assembled runtime bootstrap path.
- `/_hirmos/core/bootstrap_supporting-notes.md` now carries synchronized maintenance notes for the assembled bootstrap.
- `/_hirmos/core/templates/BOOTSTRAP_REPORT_TEMPLATE.md` now defines the canonical bootstrap completion report shape.
- `/_hirmos/artifacts/context/core/bootstrap-report.md` is the canonical bootstrap report artifact path.
- `/_hirmos/core/authority/core/identity-display-execution-control.md` replaced the older fragmented terminal-output / runtime-identity / run-result doctrine surfaces.
- `/_hirmos/core/authority/core/hook-execution-control.md` is now the live Core authority surface for hook-aware execution.
- `/_hirmos/core/templates/IDENTITY_DISPLAY_EXECUTION_CONTROL_TEMPLATE.md` replaces `terminal-output-wrapper.md`.
- `/_hirmos/core/templates/HOOK_EXECUTION_CONTROL_TEMPLATE.md` replaces `HOOK_EXECUTION_MAP_TEMPLATE.md`.

#### Authority simplification
Removed and replaced:
- `framework/governance-model.md` -> `framework/framework-operating-model.md`
- `framework/framework-readme-role.md` -> `framework/framework-document-roles.md#framework-readme-role`
- `extensions/extension-readme-role.md` -> `extensions/extension-document-roles.md#extension-readme-role`
- `core/run-result-contract.md` -> `core/identity-display-execution-control.md#terminal-run-states`
- `core/runtime-identity-contract.md` -> `core/identity-display-execution-control.md#runtime-identity-declaration`
- `core/stack-package-authority.md` -> `core/stack-system.md#stack-package-contract`

#### Beyond Clear Specs standardization

Reliability-pattern references now use **Beyond Clear Specs**.

### Required actions

- Use `hirmos init` from a project root to generate selected agent/tool bootstrap files. Use `--source` for local/offline release packages when installing into a project that does not already contain `_hirmos/`.
- Update live references in local notes, custom docs, and extension materials that still point to removed or older reliability-pattern file surfaces.
- Update any bootstrap-related guidance to use the assembled bootstrap path and the bootstrap report artifact path.
- Update reliability-pattern references so they point to **Beyond Clear Specs**.

### Notes
- Historical generated outputs may still mention older names or older file paths. Those are historical artifacts unless a live framework file points to them.
- The assembled bootstrap remains the primary runtime reading path. The supporting decomposition exists underneath it for maintenance, not as the primary bootstrap path.

## Upgrading to 1.0.0

This is the initial stable versioning baseline for HIRMOS.

### What was added
- `_hirmos/VERSION`
- [_hirmos/CHANGELOG.md](./CHANGELOG.md)
- [_hirmos/UPGRADE_GUIDE.md](./UPGRADE_GUIDE.md)
- `version` in every installed extension manifest
- `requires_core` in every installed extension manifest
- extension-level `CHANGELOG.md`
- extension-level `UPGRADE_GUIDE.md`

### Required actions

- Use `hirmos init` from a project root to generate selected agent/tool bootstrap files. Use `--source` for local/offline release packages when installing into a project that does not already contain `_hirmos/`.
- None for a fresh install.

### Notes
- Compatibility is currently declared only through `requires_core` in each extension manifest.
- Extension manifests no longer use `spec_version` in the public Hirmos contract.
