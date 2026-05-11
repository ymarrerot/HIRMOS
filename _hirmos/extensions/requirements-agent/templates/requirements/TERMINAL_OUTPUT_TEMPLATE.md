# Requirements Run Terminal Output

## Terminal State

- State: completed | paused | failed
- Extension: requirements-agent
- Entry point: requirements

## Summary

- ...

## Artifacts Produced or Updated

- _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md
- _hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md, when applicable

## Unresolved Items

### Gating / Decision Required
- ...

### Proceed With Caution
- ...

### Safe To Assume
- ...

## Validation Summary

- ...

## Evidence

- ...

## Hook / Runtime Control Evidence

- Hook subscriber matching: `<passed | paused | failed | not applicable>`
- Run execution controls: `<executed | pending | failed>`
- Validation trace: `<summary>`
- Decision absorption: `<summary | none>`

## Next Step

If completed:

```text
hirmos system-design
```

If paused or failed, state the exact blocker and required next action.
