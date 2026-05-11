# requirements-agent Entry Points

## Public default entrypoint

```text
hirmos requirements
```

Resolves through `extension.yaml` to:

```text
entrypoints/requirements.md
```

## Entry points

| Entrypoint | Purpose |
|---|---|
| `requirements` | Public Requirements step. Produces/refines requirements artifacts and performs requirements-level unresolved-item handling. |
| `requirements-input-pack` | Producer for the normalized requirements intake pack. |
| `requirements-sot` | Producer for the canonical `REQUIREMENTS_SOT.md`. |

## Public vs producer entrypoints

Regular users should run the default command:

```text
hirmos requirements
```

Producer entrypoints exist for advanced/power-user workflows and for reuse by the public Requirements step.


## Optional prompt argument

The default Requirements command may include a short direct requirements prompt after the extension id:

```text
hirmos requirements Build a menu management app for a small restaurant.
```

Core passes that trailing text as the entrypoint argument tail. `requirements-agent:requirements` treats it as direct Requirements input for the active run.

For longer or reusable requirements, prefer the session prompt, online attachments, files under `_hirmos/inputs/requirements-agent/requirements/`, or explicit bounded local file references.
