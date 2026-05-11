# system-design-agent

`system-design-agent` is HIRMOS's official **System Design** extension. In the regular-user workflow, it sits after `requirements-agent` and before `implementation-agent`:

```text
Requirements → System Design → Implementation
```

**Turn approved requirements into trusted system design artifacts.**

For most users, run:

```text
hirmos system-design
```

For deeper detail, inspect `docs/`, `entrypoints/`, `specs/`, or `templates/` intentionally.

## Installation package layout

The downloaded installation package contains this extension folder only. Install it by copying `system-design-agent/` into `_hirmos/extensions/`. Project-level runtime folders under `_hirmos/inputs/` and `_hirmos/artifacts/` are created during init or first run, not shipped inside this package.

## What it does

- Consumes Requirements artifacts produced by `requirements-agent`, especially `REQUIREMENTS_SOT.md`.
- Produces trusted system design artifacts under `_hirmos/artifacts/sot/`.
- Generates or refines approved phase contracts under `_hirmos/artifacts/phases/`.
- Captures design-stage traces, validation evidence, and unresolved-item inventory / reconciliation / feed / ledger trust artifacts under `_hirmos/artifacts/context/system-design-agent/`.
- Pauses when unresolved design or phase decisions need Orchestrator review instead of letting weak assumptions flow downstream.

## Requirements handoff

Requirements production belongs to:

```text
hirmos requirements
```

`system-design-agent` consumes Requirements outputs and does not produce Requirements for the regular-user workflow.

## Why software teams use it

- It creates a governed handoff between Requirements and Implementation.
- It makes architecture, system shape, and phase boundaries explicit before build work begins.
- It creates outputs implementation teams and AI agents can use with less ambiguity.
- It can be enriched by supporting extensions such as `prototype-ingestion` and `presentation-design` when their contributions are relevant.

## Fast mental model

```text
hirmos requirements
        │
        ▼
_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
        │
        ▼
hirmos system-design
        │
        ├──► _hirmos/artifacts/sot/SYSTEM_SOT.md
        ├──► _hirmos/artifacts/sot/ARCHITECTURE_SOT.md
        ├──► _hirmos/artifacts/sot/PHASES_SOT.md
        ├──► _hirmos/artifacts/phases/phase_<N>_<slug>_SOT.md
        └──► _hirmos/artifacts/context/system-design-agent/
        │
        ▼
hirmos implementation
```

---

## Key outputs

- Trusted system design artifacts in `_hirmos/artifacts/sot/`
- Generated phase contracts in `_hirmos/artifacts/phases/`
- Design-stage traces, unresolved-item inventory / reconciliation / feed / ledger trust artifacts, and validation evidence in `_hirmos/artifacts/context/system-design-agent/`

**Best fit:** projects that need disciplined system design, architecture direction, phase design, and staged delivery planning after requirements are established and before implementation begins.

## If you want to inspect the folder layout

```text
_hirmos/
├── artifacts/
│   ├── context/
│   │   ├── requirements-agent/           # upstream Requirements context
│   │   └── system-design-agent/          # System Design traces and runtime context
│   ├── sot/                              # trusted requirements/design artifacts
│   └── phases/                           # generated phase contracts created from approved design
└── extensions/
    └── system-design-agent/
        ├── README.md                     # extension landing page
        ├── extension.yaml                # manifest and runtime identity
        ├── entrypoints/                  # public commands such as system-design
        ├── specs/                        # behavioral truth for design work
        ├── templates/                    # entrypoint-specific output templates and scaffold templates
        ├── docs/                         # human-facing extension docs
        ├── CHANGELOG.md
        └── UPGRADE_GUIDE.md
```

---

## FAQ

**When should I use `system-design-agent`?**  
Use it after Requirements are complete enough to design the system and before Implementation begins.

**Where does it fit in the Software Development Lifecycle?**  
- **After Requirements:** it consumes `REQUIREMENTS_SOT.md` and related Requirements context.
- **Before Implementation:** it governs system design, architecture direction, phase design, and staged delivery planning.
- **At implementation handoff:** it produces reviewed outputs that implementation teams and AI agents can use with less ambiguity.

**What does it produce?**  
Its core outputs include trusted design artifacts under `_hirmos/artifacts/sot/`, approved phase contracts under `_hirmos/artifacts/phases/`, and design-stage traces plus runtime context under `_hirmos/artifacts/context/system-design-agent/`.

**Who can consume its outputs?**  
Approved outputs can be used by human implementation teams, implementation-oriented AI agents, and compatible downstream extensions.

**Can supporting extensions enrich it?**  
Yes. Supporting extensions such as `prototype-ingestion` and `presentation-design` can contribute relevant context. Requirements-stage enrichment now belongs to `requirements-agent` hook seams where applicable.

**Does it keep going when important answers are missing?**  
No. Serious design work can pause so the Orchestrator can review unresolved items and decide how to proceed.

## Where this fits next

**Usually comes before:** `implementation-agent` when reviewed design and approved phase truth are needed before build work starts.

**Usually comes after:** `requirements-agent`, which produces Requirements artifacts such as `REQUIREMENTS_SOT.md`.

## Go next

- **Run the next common SDLC stage:** `hirmos implementation` after System Design completes.
- **Inspect entrypoints:** start with `docs/entrypoints.md`.
- **See reads/writes:** open `docs/artifact-map.md`.
- **Review integration boundaries:** open `docs/integration.md`.


## Public command and reusable subcycles

Regular users should run:

```text
hirmos system-design
```

That public System Design entrypoint composes the narrowed system-level `system-design-cycle` with `phase-design-cycle` for normal greenfield implementation readiness.

- `system-design-cycle` is retained as a narrowed reusable subcycle. It consumes Requirements artifacts from `requirements-agent` and preserves system-level reliability mechanisms without producing Requirements.
- `phase-design-cycle` is required for normal greenfield System Design completion after gated blockers to phase design are resolved.

Power users may inspect or intentionally run the subcycles directly, but they are not the regular-user front door.
