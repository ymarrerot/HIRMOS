# Working with Existing Projects

Use this page when HIRMOS is being installed into a project that already has code, docs, configuration, data models, tests, deployment assumptions, or prior decisions.

## The core rule

HIRMOS is current-state-first.

That means the AI agent should not treat your request as if it were starting from a blank slate unless the current system state actually supports that conclusion.

A project may be:

- greenfield — little or no existing implementation;
- brownfield — meaningful existing implementation or architecture;
- mixed — some areas are new, while others must preserve existing behavior;
- unknown — not enough evidence yet.

You do not need to classify the project yourself. HIRMOS should infer the project type from evidence and adjust the session accordingly.

## What HIRMOS should inspect

For existing projects, HIRMOS should inspect enough current state to avoid unsafe assumptions:

- relevant source files;
- current architecture or docs;
- package/dependency/configuration files;
- tests and validation scripts;
- existing user flows or runtime surfaces;
- current accepted-state artifacts if prior HIRMOS sessions exist;
- known unresolved items or carry-forward records.

The inspection should be focused. HIRMOS does not need to read everything if the request is narrow, but it should read enough to avoid designing against an imaginary system.

## What should happen before implementation

Before implementing in an existing project, HIRMOS should make clear:

- what existing behavior must be preserved;
- what files or modules appear affected;
- what assumptions it is carrying;
- what decisions are gated;
- what validation evidence is required;
- what is intentionally out of scope for the current session.

## Existing-system preservation

For brownfield or mixed work, a good HIRMOS run should avoid:

- replacing working architecture without justification;
- bypassing existing conventions;
- ignoring tests or validation commands;
- treating mock/demo code as production code without saying so;
- claiming completion without evidence against the existing app.

When preservation risk is high, HIRMOS should record that risk and constrain the implementation plan.

## Existing HIRMOS projects

If the project already contains `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`, HIRMOS should use it as the durable accepted-state navigation point.

Current state artifacts do not replace code inspection. They help the agent understand what prior sessions accepted, rejected, deferred, or carried forward.

## What to watch for

Be cautious if HIRMOS:

- skips current-state inspection;
- assumes the project is greenfield without evidence;
- proposes a broad rewrite when the request is narrow;
- loses track of existing validation commands;
- ignores unresolved items from prior sessions;
- implements before establishing a governed session scope.


## Generated artifact wording note

Generated HIRMOS artifacts should explain routing from current-state evidence and governance need. Project-type labels are supporting metadata, not the primary authority for selecting delivery, phase, or session shape.
