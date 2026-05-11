# Operator Playbook

The Orchestrator is the human authority in the framework.

Use this page after you start running real governed workflows and need practical guidance on:
- bootstrap
- choosing the right entrypoint
- interpreting completed vs paused vs provisional cycles
- recording decisions and rerunning work


If you are new to the broader framework model, it helps to review the [Conceptual diagram](../understanding/conceptual-diagram.md) and the [Workflow diagram](../understanding/workflow-diagram.md) first.


## Runtime identity labels

- `[Core]` identifies bootstrap, command dispatch, and core-level runtime reporting.
- Active extensions that declare `runtime.identity` are surfaced as a natural first-line identity label such as `[System Design Agent]`.
- The normal rendered shape is the identity label on its own line, a blank line, and then the producer-authored response body.
- Use identity labels at meaningful block boundaries or handoff points rather than on every sentence.


## Paused-cycle continuation

When a serious cycle pauses at a decision checkpoint, it should provide proposed Orchestrator directions in the same response. These proposals are advisory and help the Orchestrator continue the cycle quickly.


## Provisional downstream runs

A downstream cycle may still run when upstream gating items remain unresolved, but it should warn the Orchestrator before continuing and report the final state as `provisional`, not `completed`.

The warning should explain:
- the command will still run;
- why the result will be provisional;
- that the outputs are useful for exploration and steering but are not yet the current authoritative finalized state.

When the upstream dependency state later changes materially, the earlier downstream trust artifacts become stale by dependency and should be rerun before being treated as current.


## Go next

- **Interpret the trust state of serious runs:** open [Cycle status and trust](cycle-status-and-trust.md).
- **Handle pause points and steering decisions:** open [Decision checkpoints](decision-checkpoints.md).
- **Go back to the broader docs hub:** return to the [Documentation hub](../../README.md).

## Optional reading

- **Go back to framework guidance:** return to [Framework guidance](../../3-extend-contribute/framework/README.md).
