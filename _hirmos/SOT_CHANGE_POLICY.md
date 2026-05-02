# SoT Change Policy

Source-of-Truth artifacts under `_hirmos/artifacts/sot/` are authority artifacts, not convenience notes.

## Rules

- Treat SoTs as the current approved design truth unless the owning design-side flow explicitly replaces them.
- Do not silently rewrite SoTs from implementation-side work, convenience cleanup, or inferred assumptions.
- When implementation work reveals stale, contradictory, or incomplete SoT authority, surface that drift explicitly in governed outputs instead of patching authority in place.
- Refresh SoT authority through the appropriate design-side entrypoint or through explicit Orchestrator instruction.
- Keep exploratory, provisional, or assumption-scoped downstream artifacts distinct from authoritative finalized SoT state.

## Practical effect

- `system-design-agent` owns normal SoT refresh and SoT-producing cycles.
- `implementation-agent` may consume SoTs, challenge them truthfully when drift is found, and record the issue, but it must not silently replace design authority.
- Optional extensions may add supporting evidence or derived context, but they should not overwrite SoT authority unless their governing contract explicitly says they own that SoT surface.
