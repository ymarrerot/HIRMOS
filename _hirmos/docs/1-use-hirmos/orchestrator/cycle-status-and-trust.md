# Cycle Status and Trust

Use the expected runtime status path `/_hirmos/artifacts/context/<extension-id>/CYCLE_STATUS.md` to understand whether a cycle:
- completed governably
- paused pending direction
- ended provisionally because unresolved upstream gating still remained
- was superseded by a later run
- is stale by dependency because an upstream cycle later changed materially

Artifacts produced before finalization may still be useful, but the status artifact should make the trust boundary explicit.

A provisional cycle result means the command was allowed to run, but the outputs are exploratory/governed draft material rather than the current authoritative finalized state.

Templates and folder scaffolding do not count as generated outputs. Serious cycles should create or refine trust artifacts from the appropriate command-scoped templates when those templates exist.


A command may still be running while the cycle state has not yet been determined. Do not confuse an in-progress execution update with a paused cycle. A runnable command is only complete when it ends with a terminal run-state block such as `Run state: completed`, `Run state: paused`, `Run state: provisional`, or `Run state: failed`.
