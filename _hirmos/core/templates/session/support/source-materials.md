# Source Materials

Status: active-session source-input artifact.
Lifecycle owner: Understand System State.
Primary capability: `system-state-agent/source-material-ingestion`.
Purpose: inventory and classify source materials without turning them into governed authority.

Source materials guide focus and Design inputs. They do not become governed requirements, Design authority, or Implementation authorization by themselves.

## Source Material Inventory

| ID | Source material | Type | Location | Readable? | Relevance | Priority | Notes |
|---|---|---|---|---|---|---|---|

Types may include: requirement notes, prototype, POC, screenshot, ticket, existing spec, docs, codebase evidence, external reference, conversation instruction, other.

Relevance values:

```text
primary
supporting
conflicting
stale
unreadable
not_applicable
```

## Extracted Focus Signals

| Signal | Source material ID | Direct / indirect relevance | Affected area | Evidence type | Confidence | Notes |
|---|---|---|---|---|---|---|

Evidence types:

```text
observed
inferred
assumed
unknown
blocked
not_applicable
```

## Conflicts and Priority Questions

| Conflict / question | Source materials involved | Why it matters | Proposed handling | Unresolved item ID |
|---|---|---|---|---|

## Prototype / POC Routing

List any source material that must be routed to `prototype-ingestion`.

| Source material ID | Prototype type candidate | Routing decision | Notes |
|---|---|---|---|

## Handoff to Understand System State

List source-material findings that must shape general or focused system-state understanding.

## Handoff to Design

List source-material findings that Design may use as evidence after system-state reconciliation.

## Completion

- Terminal state: COMPLETED | NEEDS_USER_DECISION | BLOCKED | NOT_APPLICABLE
- SESSION_EXECUTION.md updated: yes / no
- Unresolved-item contribution completed: yes / no / not applicable
