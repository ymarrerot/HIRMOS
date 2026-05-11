# requirements-agent:requirements

## Execution Contract

### Purpose

Run the HIRMOS **Requirements** step for Orchestrated Spec-Driven Development.

This entrypoint turns user-provided goals, context, notes, prototypes, user stories, files, attachments, bounded repository context, and constraints into requirements artifacts suitable for System Design.

### Produces

- _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`)
- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)
- project-level unresolved-item artifacts under _hirmos/artifacts/context/requirements-agent/requirements/ when unresolved assumptions, open questions, or gating decisions are present

### Terminal States

- `completed` — allowed only when Requirements artifacts have been generated or refined, required validation passes, and no gating requirements decisions remain unresolved.
- `paused` — required when gated requirements decisions, missing required inputs, unresolved hook obligations, or validation blockers require Orchestrator/user input before System Design can safely proceed.
- `failed` — required when the Requirements step cannot safely complete and cannot identify a bounded pause/remediation path.

## Instructions

1. Read and follow `specs/requirements.spec.md`. Do not restate or bypass the deeper behavioral rules in that spec or its producer specs.
2. Invoke and honor declared Requirements hook points in order where applicable:
   - `requirements-agent.requirements.before-input-discovery`
   - `requirements-agent.requirements.before-requirements-normalization`
   - `requirements-agent.requirements.contribute-unresolved-items`
   - `requirements-agent.requirements.before-final-gating-review`
3. Ensure the Requirements runtime input folder exists or record that it is intentionally absent for this run:
   - `_hirmos/inputs/requirements-agent/requirements/`
   - Do not ship this folder inside the extension package. Runtime input folders are project runtime surfaces governed by Core command protocol; the active Core/entrypoint path must create missing runtime folders during init or first run when they are needed.
4. Gather all relevant requirement-shaping inputs, including:
   - the user prompt or collaborative reasoning from the current session
   - optional command argument tail after `hirmos requirements`
   - online-service attachments visible in the current LLM session, such as screenshots, PDFs, docs, exported notes, or prototype artifacts
   - files under `_hirmos/inputs/requirements-agent/requirements/` when present
   - explicit bounded local file paths or repository-context references surfaced by the user or Orchestrator
   - project context, notes, prototypes, user stories, screenshots, or local file references surfaced by the Orchestrator
   - existing prototype-derived or presentation-derived artifacts when available and relevant
5. If the user or Orchestrator references a required attachment, local file, folder, or repository context that is not readable, pause and state exactly what is missing or inaccessible.
6. Do not automatically scan or ingest the full repository by default. If the user asks to use repository context without a bounded scope, pause for scope or use a bounded discovery plan before treating repository content as Requirements input.
7. Run the requirements intake-pack responsibilities defined by `entrypoints/requirements-input-pack.md` and `specs/requirements-input-pack.spec.md`.
8. Run the requirements SoT responsibilities defined by `entrypoints/requirements-sot.md` and `specs/requirements-sot.spec.md`.
9. Contribute assumptions, open questions, and gated requirements decisions through the existing unresolved-item governance artifact pattern under the project-level canonical context.
10. Do **not** create any separate unresolved-decision bypass artifact.
11. Preserve clear separation between:
   - confirmed facts
   - assumptions
   - research-backed defaults
   - open questions
   - gating decisions
12. Validate hook subscriber matching, runtime trust artifacts, unresolved-item coverage, and decision absorption as defined by the Requirements spec.
13. Perform the mandatory self-validation defined by the Requirements spec.
14. Surface a governed terminal output using the Requirements terminal-output expectations.

## Output

Return the Requirements terminal output.

The surfaced output must include:

- terminal state: `completed`, `paused`, or `failed`
- artifacts produced or updated
- unresolved-item summary
- validation summary
- next step guidance

If completed, the next step is:

```text
hirmos system-design
```

If paused, state exactly what decision, input, or remediation is needed before System Design can safely proceed.
