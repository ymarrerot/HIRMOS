# Project Types Protocol

Status: core protocol.
Purpose: define evidence-backed project-type classification and routing effects for HIRMOS sessions.

Project type is a routing classification. It is not authority by itself.

## Core rule

```text
User Request guides focus; evidence determines classification.
Project type routes lifecycle work; it does not replace lifecycle authority.
```

HIRMOS must classify project type from the current working copy, accepted HIRMOS system state, User Request, source inputs, prototype/POC evidence, and repository evidence.

## Baseline project types

Allowed baseline values:

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

## Confidence

Project-type confidence must be recorded as:

```text
high
medium
low
unknown
```

Low or unknown confidence may continue only when the uncertainty does not affect Design authority, Implementation authorization, evidence requirements, or Update System State.

## Classification inputs

Use these inputs in priority order where applicable:

1. repository evidence and current working-copy structure;
2. accepted HIRMOS system state;
3. source inputs and prototype/POC evidence;
4. User Request focus signals;
5. prior active-session artifacts;
6. explicit configuration or operator instruction.

User labels such as "greenfield" or "small change" are focus signals, not final classification.

## Routing rules

### Greenfield

Greenfield work generally requires Design to produce delivery structure before Implementation when the request asks for product/software delivery.

Typical chain:

```text
Durable Delivery Plan
→ PHASE-xx.md
→ Session Contract
→ Implementation Units
```

Implementation must not begin from raw requirements alone.

### Brownfield targeted change

A targeted brownfield change may skip durable Delivery Plan governance only when focused system-state understanding proves the change can be safely governed by one Session Contract and the Delivery Shape Decision Gate records affirmative single-session safety evidence.

It still requires:

- focused affected-area understanding;
- preservation constraints;
- regression evidence expectations;
- Session Contract;
- Implementation authorization when project files will change.

### Large or multi-session delivery shape

Large or multi-session work requires governed delivery decomposition when it cannot be safely implemented as one bounded session. This applies to any project type: greenfield, brownfield, mixed, prototype-to-product, and other delivery paths.

Use the Delivery Unit model:

```text
Durable Delivery Plan
→ PHASE-xx.md
→ Session Contract
→ Implementation Units
```

Brownfield or mixed Delivery Units must also define preservation constraints and regression evidence strategy. Greenfield Delivery Units must define bounded MVP/scope/architecture controls.

A Phase is the default Delivery Unit type when ordered staged delivery is natural.

Other labels such as workstream, migration stage, risk-reduction pass, and implementation slice are Delivery Unit types only. They do not create separate governance rules.

### Prototype or POC driven

Prototype/POC-driven work must activate prototype ingestion when prototype evidence materially shapes the request.

A prototype is evidence, not authority. Design converts prototype findings into governed requirements, design, scope, and unresolved items.

### Requirements-only and design-only

These requests may be satisfied in Design and proceed to Update System State without Implementation.

### Implementation continuation

Implementation continuation must verify that existing Design authority, Session Contract, stack/project-type evidence, and execution controls remain valid before continuing Implementation.

### Validation or review only

Validation/review-only work may use Implementation-stage governance because it evaluates implemented work against Design. It may not change project files.

### Close or update only

Update System State may not create missing Design or Implementation outcomes. It must verify existing readiness and evidence.

## Failure and route-back conditions

Route back or block when:

- project type is uncertain and affects safety or scope;
- project type was misclassified;
- large or multi-session work lacks governed delivery decomposition;
- prototype/POC input was material but prototype ingestion was skipped;
- greenfield delivery lacks delivery/phase/session-contract authority before Implementation;
- brownfield work lacks preservation or regression evidence strategy;
- implementation continuation lacks valid upstream Design authority;
- Update System State relies on stale or invalid project-type assumptions.

## Interaction-mode visibility

- `domain_expert`: show concise project-type rationale and user-owned implications.
- `technical_supervisor`: show evidence, confidence, conflicts, and routing impact.
- `framework_diagnostics`: show full classification signals, controls, route-backs, and capability decisions.

Interaction modes change visibility, not classification rigor.


## Delivery shape fields

Project-type classification must include delivery shape, not only greenfield/brownfield labels.

Required fields:

```text
Project type: GREENFIELD / BROWNFIELD_TARGETED / BROWNFIELD_MULTISESSION / MIXED / UNKNOWN
Delivery governance required: YES / NO / UNCERTAIN
Required delivery artifact: none / DELIVERY_PLAN.md + PHASE-xx.md
Reasoning evidence:
```

For durable multi-session delivery, a Delivery Plan is needed. Separate phase files are required only when the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

HIRMOS must apply `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` before implementation readiness.
