# Decision Checkpoints

Serious cycles may pause when unresolved items materially affect downstream truth, delivery feasibility, or contract shape.

Allowed outcomes:
- use assumption
- ask customer
- defer and constrain

A paused cycle should ask the Orchestrator directly in chat and should update the cycle status artifact.


## Downstream continuation while upstream is unresolved

If a downstream cycle is run while an upstream cycle still has unresolved gating items, the framework may allow the command to continue, but the downstream result must be reported as `provisional`.

Before continuing, the extension should warn the Orchestrator that:
- the command will run;
- the state will be provisional;
- the reason for provisionality;
- the outputs are useful for exploration and steering but are not yet the current authoritative finalized state.
