# requirements-agent:requirements-input-pack

## Execution Contract

### Purpose

Generate or refine _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`) as the normalized requirements-intake artifact for downstream system design.

### Produces

- _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`)

### Terminal States

- `completed` — allowed only when _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`) has been generated or refined and passes the local Spec-backed validation bar.

## Instructions

1. Read and follow `specs/requirements-input-pack.spec.md`.
2. Gather all relevant requirements-oriented inputs, including:
   - manually attached requirement-relevant inputs
   - files under `_hirmos/inputs/requirements-agent/requirements/` when present
   - assistant-user collaborative reasoning produced during the session
   - staged-delivery inputs when present
   - optional research findings when useful
3. Normalize the available inputs into a governed intake artifact by following `specs/requirements-input-pack.spec.md` directly.
4. Preserve provenance and planning classifications clearly. Do not blur or silently promote:
   - confirmed facts
   - assumptions
   - research-backed defaults
   - open questions
   - pending confirmation items
   - declared delivery targets
   - proposed delivery targets
5. If staged delivery is explicit, implied, or worth proposing for planning clarity, preserve:
   - delivery target signals
   - declared delivery targets
   - proposed delivery targets
6. Strengthen downstream planning without pretending this artifact is Source of Truth.
7. Perform the mandatory self-validation defined in the Spec and fix any issue before finalizing.

## Output

Return ONLY the final _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`) content.

No explanations outside the document.