# Project Context

Status: active-session context artifact.
Purpose: record evidence-backed project-type and stack-context classification used to route lifecycle work.

Project context guides routing. It is not requirements, Design, Implementation, or accepted-state authority by itself.

## User Request Signals

- User Request:
- Claimed project type, if any:
- Claimed stack/technology preference, if any:
- Source/prototype inputs affecting classification:

## Project-Type Classification

- Project type:
- Confidence: high | medium | low | unknown
- Classification evidence:
- Conflicts or uncertainty:
- Lifecycle routing effect:

Allowed project types:

```text
greenfield
brownfield_targeted_change
brownfield_large_change
prototype_or_poc_driven
mixed_or_stale_state
requirements_only
design_only
implementation_continuation
validation_or_review_only
close_or_update_only
status_or_inspection
unknown
```

## Stack Classification

- Active stack:
- Selection source:
- Confidence: high | medium | low | unknown
- Repository evidence:
- Accepted-state evidence:
- Request/config preference:
- Prototype/POC evidence:
- Decision: use | generic-fallback | blocked

## Stack Contexts

Default: not active.

Use this section only when evidence shows multiple bounded stack areas.

| Context ID | Root path | Stack ID | Evidence | Confidence | In-scope status | Notes |
|---|---|---|---|---|---|---|

Allowed in-scope statuses:

```text
IN_SCOPE
OUT_OF_SCOPE
IMPACTED_NOT_AUTHORIZED
UNKNOWN
```

## Delivery Routing Impact

State whether the project context requires:

- no delivery decomposition;
- Delivery Plan;
- Phase decomposition / Phase Contract;
- Delivery Unit Plan / Phase Contract;
- Preservation Contract;
- Regression Evidence Strategy;
- direct Session Contract.

## Route-Back Conditions

Record any project-type or stack uncertainty that requires route-back before Design, Implementation, or Update System State can proceed.

## Handoff

- Handoff to Understand System State:
- Handoff to Design:
- Handoff to Implementation:
- Handoff to Update System State:
