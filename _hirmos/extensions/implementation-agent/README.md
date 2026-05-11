# implementation-agent

`implementation-agent` is HIRMOS’s main implementation extension. In Software Development Lifecycle terms, it sits after approved system design and phase scope exist and before delivery is complete, turning that approved design into governed implementation prompts, reviewable execution, phase-reviewed implementation results, verification evidence, and trustworthy implementation outputs that teams and AI agents can use with confidence.

**Turn approved system design into governed implementation outputs.**

For most users, this README is the right starting point. Open `docs/`, `entrypoints/`, `specs/`, or `templates/` only when you intentionally want deeper detail.


## Public command

The public HIRMOS Implementation step is backed by:

```text
hirmos implementation
```

This default command uses `entrypoints/implementation.md`. It covers the regular-user Implementation step while preserving the existing planning and execution cycles as advanced/reusable surfaces.

The public Implementation step:

1. verifies approved System Design and selected phase context;
2. runs or refreshes implementation planning when needed;
3. pauses after planning for explicit Orchestrator approval before execution;
4. executes the selected/current phase only after approval;
5. validates results and surfaces Evidence-backed Review.

Power users may still use the explicit cycle commands when they intentionally need lower-level control:

```text
hirmos implementation:implementation-planning-cycle
hirmos implementation:implementation-execution-cycle
```

## Installation package layout

The downloaded installation package contains this extension folder only. Install it by copying `implementation-agent/` into `_hirmos/extensions/`. Project-level runtime folders under `_hirmos/inputs/` and `_hirmos/artifacts/` are created during init or first run, not shipped inside this package.

## What it does

- Consumes trusted upstream truth from artifacts such as `_hirmos/artifacts/sot/` and `_hirmos/artifacts/phases/`.
- Generates bounded implementation prompts under `_hirmos/artifacts/prompts/`.
- Runs governed implementation execution with review and correction instead of uncontrolled retries.
- Captures implementation runtime context and trust artifacts under `_hirmos/artifacts/context/implementation-agent/`.
- Stores execution evidence and operational records under `_hirmos/artifacts/ops/`.
- Pauses honestly when implementation can no longer proceed safely or truthfully.

## Why software teams use it

- It creates a disciplined bridge between approved design truth and actual implementation work.
- It makes AI-assisted build work easier to review because prompts, runs, and evidence are preserved.
- It reduces drift between approved scope and implementation activity.
- It helps human implementation teams and implementation-oriented AI agents work from the same approved truth.

## Fast mental model

```text
upstream design-oriented and custom workflow         
extensions can provide implementation-agent inputs

                                             ╔══════════════════╗
_hirmos/artifacts/sot/─────┐   ┌─────────────║     FRAMEWORK    ║
_hirmos/artifacts/phases/──│   │             ║       CORE       ║
                           │   │             ╚══════════════════╝
                           ▼   ▼      
                  ┌──────────────────────┐
                  │ implementation-agent │
                  │         **           │
                  └──────────┬───────────┘     
                             │
                             ├──► _hirmos/artifacts/context/implementation-agent/
                             ├──► _hirmos/artifacts/prompts/
                             ├──► _hirmos/artifacts/ops/
                             └──► project file changes + verification evidence

** major official extension

```

Common upstream example: any governed design workflow **

---

## Key outputs

- Generated implementation prompts in `_hirmos/artifacts/prompts/`
- Implementation runtime context and trust artifacts in `_hirmos/artifacts/context/implementation-agent/`
- Execution records and verification evidence in `_hirmos/artifacts/ops/`
- Implementation changes and outputs produced during approved execution

**Best fit:** projects that already have approved Requirements and System Design artifacts and now need disciplined implementation planning, approval-gated execution, Evidence-backed Review, and verification.

## If you want to inspect the folder layout

```text
_hirmos/
├── artifacts/
│   ├── sot/                        # approved design truth consumed by implementation work
│   ├── phases/                     # approved phase contracts consumed by implementation work
│   ├── prompts/                    # generated implementation prompts
│   ├── context/
│   │   └── implementation-agent/   # implementation-planning/execution trust artifacts
│   └── ops/                        # runs, reviews, retries, and phase review records
└── extensions/
    └── implementation-agent/
        ├── README.md               # extension landing page
        ├── extension.yaml          # manifest and runtime identity
        ├── entrypoints/            # public implementation commands
        ├── specs/                  # behavioral truth for planning and execution
        ├── templates/              # execution templates, including paused and completion templates
        ├── docs/                   # human-facing extension docs
        ├── CHANGELOG.md
        └── UPGRADE_GUIDE.md
```

---

## FAQ

**When should I use `implementation-agent`?**  
Use it when approved System Design and phase scope already exist and you want governed implementation planning, approval-gated execution, and Evidence-backed Review.

**Where it fits in the Software Development Lifecycle?**  
- **After approved design exists:** it starts once trusted upstream artifacts such as reviewed system design and approved phase scope are available.  
- **At implementation planning and execution:** it governs prompt generation, implementation runs, review, correction, and verification.  
- **At implementation handoff:** it preserves prompts, context, and evidence so human teams and AI agents can inspect what happened and continue responsibly.

**What does it need before it can run well?**  
It works best when strong upstream design artifacts already exist, especially approved system design and approved phase scope.

**What does it produce?**  
Its core outputs include implementation prompts under `_hirmos/artifacts/prompts/`, execution context under `_hirmos/artifacts/context/implementation-agent/`, operational records under `_hirmos/artifacts/ops/`, phase review/evidence artifacts, and implementation changes made during approved runs.

**Who can use its outputs?**  
Its outputs are designed for both human implementation teams and implementation-oriented AI agents.

**Does it keep retrying until something works?**  
No. Retry is bounded. When correction stops being honest or useful, the workflow should pause instead of pretending the issue is solved.

## Where this fits next

**Usually comes after:** governed design or approved implementation scope from any disciplined upstream process. `system-design-agent` is a common optional upstream example, not a required dependency.

**Commonly paired with:** [solution-brief](https://hirmos.dev/marketplace/solution-brief/) later when implementation-backed project understanding needs to be summarized for external readers.

## Go next

- **Bring approved scope:** use any trusted design or implementation-scope source before running implementation work.
- **See a common outward-facing follow-up:** solution-brief is useful when implementation-backed understanding later needs to be summarized for external readers.
- **Browse the official marketplace:** visit [hirmos.dev](https://hirmos.dev).

## Optional reading

- **Inspect this extension more deeply after installation:** start with `docs/entrypoints.md`.
- **See what this extension reads and writes after installation:** open `docs/artifact-map.md`.
- **Review integration boundaries after installation:** open `docs/integration.md`.

