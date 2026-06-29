# Working with Existing Projects

HIRMOS is current-state-first, so existing projects are first-class.

A project can be greenfield, brownfield, mixed, or somewhere in between. HIRMOS starts by understanding the current system state, then selects the smallest safe work shape for the request.

## What HIRMOS should inspect

Depending on the request, HIRMOS may inspect:

- source code and project structure;
- package/build/test configuration;
- existing docs and README files;
- existing HIRMOS accepted state and history;
- prototypes, screenshots, notes, or uploaded references;
- unresolved items and carry-forward records.

## Work shape still matters

Existing projects do not automatically require durable delivery.

| Request | Likely shape |
|---|---|
| Small fix or doc update | single governed session |
| Local feature with clear scope | session baseline, then implementation |
| Larger MVP or release | delivery baseline, then phase/session work |
| Ambiguous architectural change | design session before implementation |

## What to watch for

A good HIRMOS run should distinguish:

- accepted current system state;
- raw notes or prototypes;
- assumptions that can safely proceed;
- gated decisions that need user input;
- production-readiness limitations.

Implementation should not start until the relevant session/delivery authority is accepted. When IU mode applies, implementation should wait until the IU plan is accepted.
