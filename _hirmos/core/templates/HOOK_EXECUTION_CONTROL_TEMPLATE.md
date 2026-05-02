# HOOK EXECUTION CONTROL TEMPLATE

- Owning entrypoint:
- Run scope:
- Resolution source:
- Validation note:

This artifact is maintained to satisfy `Hook execution control` for hook-aware runs.

Allowed `Status` values:
- `pending`
- `executed`
- `no-subscribers`
- `failed`

## Hook Point: <hook-point-id>
- Workflow location:
- Matched subscribers:
- Rejected matching subscribers:
- Execution order:
- Status:
- Inspected path:
- Discovered runtime packs:
- Accepted active runtime packs:
- Rejected runtime packs:
- Notes:

Evidence note:
- When a hook note reports on runtime-pack discovery, support the note with explicit discovery evidence rather than only free-form summary prose.

Subscriber-resolution note:
- If `Matched subscribers` is `none`, but an installed extension manifest declared an exact hook-target match for this hook point, record the rejected matching subscriber(s) and the explicit rejection reason(s).
