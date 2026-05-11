# implementation-agent integration

`implementation-agent` is designed to be reused through its public default entrypoint and, when needed, through lower-level explicit entrypoints.

## Public integration path

Use the public HIRMOS Implementation command in regular workflows:

```text
hirmos implementation
```

This command backs the Implementation workflow step:

```text
Requirements → System Design → Implementation
```

It assumes approved System Design and selected phase scope already exist. The official `system-design-agent` is the common upstream provider in greenfield HIRMOS workflows, but the implementation extension consumes approved artifacts rather than depending on a specific upstream extension identity.

## Advanced integration patterns

### Use the full implementation-planning path

Call `implementation-planning-cycle` when you want governed planning from approved scope to execution-ready prompt artifacts.

### Use the full execution path for one phase

Call `implementation-execution-cycle` when planning is already approved and you want one selected phase executed with governed evidence, local review, bounded retry discipline, and phase review.

### Use lower-level planning surfaces directly

Examples:

- `prompt-planning`
- `agent-prompt`

## Integration rules that matter most

- The public Implementation command pauses after planning for explicit approval before execution.
- `implementation-agent` does not perform Requirements or System Design.
- `implementation-agent` owns implementation prompt artifacts under `_hirmos/artifacts/prompts/`.
- `implementation-agent` owns execution evidence under `_hirmos/artifacts/ops/`.
- `implementation-agent` consumes active stack context where the governing Spec allows it.
- Normalized presentation artifacts may still affect implementation consequences when `_hirmos/artifacts/sot/PRESENTATION_SOT.md` exists and the relevant Spec says so.

## Evidence-backed Review

When execution occurs, the public Implementation step must surface Evidence-backed Review: what changed, what evidence was reviewed, what validation ran, what passed or failed, what remains unresolved, and why the terminal state is truthful.
