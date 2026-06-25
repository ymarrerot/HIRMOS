# Capabilities and Entrypoints

HIRMOS is modular. Core defines the lifecycle and governance model; extensions provide capabilities that can be activated when work needs them.

## Core owns lifecycle authority

Extensions and capabilities do not own HIRMOS lifecycle authority.

Core owns:

- command routing;
- lifecycle boundaries;
- session scope authority;
- unresolved-item governance;
- execution-control requirements;
- evidence and close rules;
- accepted-state update safety.

Extensions contribute specialized work capability under that core authority.

## Extension families

The baseline framework uses stage-aligned extension families for system-state, design, and implementation work. Use extension manifests for discovery instead of assuming hard-coded extension paths.

Each extension may expose capabilities through its own manifest and entrypoint files.

## Canonical entrypoint surfaces

Extension and capability entrypoints use canonical `entrypoints/default.md` surfaces.

Examples:

```text
_hirmos/extensions/<extension>/entrypoints/default.md
_hirmos/extensions/<extension>/capabilities/<capability>/entrypoints/default.md
```

These files are part of the framework payload and are read by AI coding tools through the HIRMOS bootstrap and routing model.

## Execution contract

Runnable entrypoints expose an execution contract. At minimum, contributors should expect these sections:

```text
Purpose
Produces
Terminal States
```

Capability entrypoints may also define:

- activation triggers;
- required inputs;
- execution controls contributed;
- required behavior;
- interaction-mode visibility;
- unresolved-item producer obligations.

## Producer discipline

Capabilities may produce artifacts, findings, evidence, draft decisions, implementation units, reviews, or recommendations.

They must not silently replace the authority of:

- `SESSION_SCOPE.md`;
- `SESSION_EXECUTION.md`;
- `unresolved-items.md`;
- `SESSION_SCOPE.md` close verification;
- `CURRENT_SYSTEM_STATE.md`.

A capability that finds an issue should contribute it to the appropriate governed artifact rather than hiding it in narrative text.

## Integration templates are framework payload

AI-tool integration templates are not owned by the terminal CLI.

```text
The published `hirmos init` CLI installs integration templates; it does not own them.
The canonical integration registry/templates live in the framework payload under `_hirmos/integrations/agent-tools/`.
```

This matters because HIRMOS must remain installable and inspectable as a framework payload, not as hidden CLI internals.



## Capability taxonomy and aliases

HIRMOS capability names are stable dispatch identifiers. Contributors should discuss capabilities through families before creating new capability IDs.

Canonical families:

- current-state understanding;
- delivery and phase shaping;
- session scope and design;
- implementation execution and review;
- accepted-state update.

The family names are documentation aliases only. They do not replace extension manifests or capability manifests. Before adding a capability, first determine whether an existing capability entrypoint can safely own the responsibility with a smaller update.


## Contribution checklist

When adding or changing an extension or capability:

1. Identify the core protocol it depends on.
2. Keep lifecycle authority in core.
3. Define what the capability produces.
4. Define terminal states clearly.
5. Update manifests and entrypoints consistently.
6. Add or update validation coverage when the structure changes.
7. Run private and public validators.
8. Run regression fixtures.
9. Confirm private/public parity.

## Delivery route capability expectations

Capabilities that participate in delivery routing must expose whether they are required, not applicable, blocked, satisfied, or route-back required for the active command boundary. Delivery-related capabilities must use the canonical route matrix from `CAPABILITY_ROUTING.md` and must not create alternate delivery authority surfaces.
