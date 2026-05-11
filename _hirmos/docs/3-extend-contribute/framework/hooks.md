# Hooks

Hooks let one extension extend another without editing shared framework files.

In Hook System v1:
- the owning extension declares the hook points it exposes;
- other installed extensions may subscribe to those hook points;
- the core validates and orders matching subscriptions;
- hook execution stays visible in traces and reporting.

Hook System v1 uses **Action Hooks only**.

For the authoritative contract, see:
- [_hirmos/core/authority/core/hook-execution-control.md](../../../core/authority/core/hook-execution-control.md)
- [_hirmos/core/authority/core/extension-manifest-authority.md](../../../core/authority/core/extension-manifest-authority.md)

For practical authoring guidance, see:
- [_hirmos/docs/3-extend-contribute/extensions/hooks-authoring.md](../extensions/hooks-authoring.md)