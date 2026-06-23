# Next.js TypeScript Execution Stack Rules

Status: stack guidance.
Purpose: Guidance for Next.js projects using TypeScript and common React app structure.

Stack guidance is not repository authority. Repository evidence and accepted HIRMOS system state govern actual commands, structure, and constraints.

## Autonomous progress stack rules

Stack guidance should help HIRMOS proceed, not defer. Use safe stack-specific defaults when repository evidence supports them. Route back or block when the next action is unsafe, destructive, credential-dependent, or outside active scope.

## Production-shaped execution rules

When implementing Next.js TypeScript work:

- prefer production-shaped local defaults over demo shortcuts;
- do not implement long-running AI/provider/image work as hidden awaited request-time work unless explicitly authorized;
- do not use SQLite/local file persistence as the default when PostgreSQL is the recommended production database, unless explicitly authorized;
- do not claim metered-state/billing safety from preflight checks alone when concurrent requests are possible;
- add or run critical-flow smoke evidence when the session changes the main product path;
- record any production-shape limitation before close.
