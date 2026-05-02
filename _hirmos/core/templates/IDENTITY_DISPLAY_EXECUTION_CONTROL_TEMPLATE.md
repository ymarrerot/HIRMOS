# IDENTITY DISPLAY EXECUTION CONTROL TEMPLATE

## Purpose

Define the Core-owned chat-facing terminal output wrapper required by `Identity display execution control`. This file is a template, not the governing doctrine for the control.

## Canonical rendered shape

```text
[Identity when applicable]

<Response body>
```

Rules:
- the identity line appears first when the active producer is Core or when the resolved extension declares `runtime.identity`;
- the response body follows after one blank line;
- the response body must not be missing;
- extensions do not own wrapper rendering or wrapper validation.

## Identity line

Allowed values:
- `[HIRMOS]` for bootstrap, command dispatch, and genuinely framework-native/Core-native terminal output;
- the manifest-declared identity rendered in brackets, for example `[System Design Agent]`;
- omitted only when the active producer is an extension that does not declare `runtime.identity`.

## Response body

Rules:
- Core authors the response body when Core is the active producer;
- an extension authors the response body when the resolved extension entrypoint is the active producer;
- the wrapper must not be missing the response body;
- the response body must not be wrapped in additional `Identity` or `Response` headings.

## Validation expectations

When satisfying `Identity display execution control`, validate that:
- the canonical rendered shape is present;
- the identity line is correct for the active producer when applicable;
- the response body is present;
- wrapper ownership and body ownership are coherent.
