# implementation-agent:agent-prompt

## Execution Contract

### Purpose

Generate one complete approved execution prompt for a downstream coding or execution consumer.

### Produces

- one final Agent Prompt in the canonical implementation-planning layout under `_hirmos/artifacts/prompts/phase-<NN>-<slug>/`

### Terminal States

- `completed` — allowed only when the final Agent Prompt has been generated or refined and passes the local Agent-Prompt quality bar.

## Instructions

1. Read and follow `specs/agent-prompt.spec.md`.
2. Use the strongest available governing inputs, including:
   - the relevant phase contract under `_hirmos/artifacts/phases/`
   - the approved Prompt Plan when present
   - relevant _hirmos/artifacts/sot/SYSTEM_SOT.md (`/_hirmos/artifacts/sot/SYSTEM_SOT.md`)
   - relevant _hirmos/artifacts/sot/ARCHITECTURE_SOT.md (`/_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`)
   - _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
   - the target task description when one exists
   - [_hirmos/extensions/implementation-agent/specs/ENGINEERING_STANDARDS.md](../specs/ENGINEERING_STANDARDS.md)
   - active stack `engineering_standards`
   - active stack `commands`
   - active stack `architecture_guidance` when materially relevant
3. Determine whether the current prompt belongs to a Prompt Plan.
4. If a Prompt Plan exists, identify the current prompt in the plan and extract its assigned scope, dependencies, and deliverables.
5. Construct the execution contract exactly as required by the Spec.
6. Enforce phase boundaries, prompt-plan boundaries, architecture constraints, observability requirements, tests, binary acceptance criteria, and review-chain readiness.
7. Validate the result against the local Agent-Prompt quality bar before returning it.

## Output

Return ONLY the final Agent Prompt.


## Independence Note

`implementation-agent` does not require any specific upstream extension to exist. This entrypoint produces an implementation-owned execution contract that downstream execution consumers may adopt and extend when installed. Executing the generated prompt is outside the governed role of this entrypoint itself.