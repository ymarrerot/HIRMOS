# Framework Structure

This page explains the main HIRMOS framework surfaces for contributors.

For normal project use, you usually do not need this page. For contribution work, it helps you understand where different responsibilities live inside the public framework payload.

## Public repository surface

The public HIRMOS repository is intentionally small. It contains the public framework payload, public documentation, repository metadata, and license.

```text
README.md
LICENSE
.github/
_hirmos/
```

Maintainer-only workspace assets are not part of the public repository surface. Public onboarding docs, contributor docs, and repository instructions should only reference paths present in the public repository.

## Framework payload structure

Inside `_hirmos/`, the main surfaces are:

```text
_hirmos/
  AGENTS.md
  README.md
  core/
  docs/
  extensions/
  integrations/
  session/
  system/
  tools/
  hirmos.config.json
```

| Surface | Responsibility |
|---|---|
| `AGENTS.md` | Bootstrap entrypoint for AI coding tools. |
| `core/` | Core protocols, requirements, templates, and runtime rules. |
| `docs/` | User-facing onboarding, methodology, contributor, and reference docs. |
| `extensions/` | Bundled capability providers such as system-state, design, and implementation agents. |
| `integrations/` | Framework-owned AI-tool integration registry and templates. |
| `session/` | Active session runtime artifact area. |
| `system/` | Durable accepted-state, delivery, and history surfaces. |
| `tools/` | Framework validation and support tools shipped inside the framework payload. |
| `hirmos.config.json` | Framework metadata and configuration, including the framework version. |
| `CHANGELOG.md` | Release history. |
| `UPGRADE_GUIDE.md` | Version-level operational notes. |

## Framework version metadata

HIRMOS tracks framework version metadata in:

```text
_hirmos/hirmos.config.json
```

Use `hirmos.config.json` as the public framework version source.

## Docs vs protocols

The public docs explain how to understand and use HIRMOS. Core protocols govern how HIRMOS behaves at runtime.

Use this rule:

```text
Docs onboard and orient.
Protocols govern execution.
Validators protect invariants.
```

Do not move hard runtime authority into public docs. Do not make docs so detailed that they become a second protocol system.

## Integration templates

AI-tool integration templates are framework payload. They live at:

```text
_hirmos/integrations/agent-tools/
```

The published CLI reads this framework-owned surface during `hirmos init` and `hirmos update` to generate or reconcile AI-tool integration files. The integration templates are not hidden CLI internals.

## Contribution checklist

When changing public framework content:

1. Keep public docs focused on public repository paths and installed `_hirmos/` paths.
2. Avoid references to local maintainer workspace assets.
3. Keep lifecycle authority in core protocols.
4. Update docs when public file paths or command surfaces change.
5. Run the framework validator when available:

```bash
python3 _hirmos/tools/validate.py
```
