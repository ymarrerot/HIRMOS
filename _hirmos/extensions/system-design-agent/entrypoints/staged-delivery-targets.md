# system-design-agent:staged-delivery-targets

## Execution Contract

### Purpose

Generate or refine _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`) as the normalized staged-delivery planning-input artifact for downstream planning.

### Produces

- _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`)

### Terminal States

- `completed` — allowed only when _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`) has been generated or refined and passes the local Spec-backed validation bar.

## Instructions

1. Read and follow `specs/staged-delivery-targets.spec.md`.
2. Use _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`) as the primary normalized staged-delivery artifact when it already exists, unless the Orchestrator explicitly wants refinement.
3. Inspect available source materials for staged-delivery signals, including explicit deliverables, implied roadmap stages, milestone-based rollout language, MVP/pilot/beta references, and planning notes that materially affect roadmap honesty.
4. Use `specs/staged-delivery-targets.spec.md` as the required structure and governance baseline.
5. Preserve the distinction between declared delivery targets and proposed delivery targets.
6. Do not silently collapse multiple targets into one unless the inputs clearly justify doing so.
7. Do not present proposed targets as source-confirmed truth.
8. Keep the artifact planning-oriented. Do not turn it into release execution control, phase planning, or implementation sequencing.
9. If staged delivery is not actually relevant, do not invent targets. Surface that clearly instead of fabricating staged roadmap truth.
10. Validate the result against the local Spec-backed quality bar before finalizing.

## Output

Return only the final _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`) content.