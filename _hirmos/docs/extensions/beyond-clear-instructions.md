# Beyond Clear Instructions
*Clear instructions are not enough.*

Most people do not learn this lesson early in AI-assisted software engineering. Early marketing and early experimentation both make it seem like the main job is to get good at prompting and writing clear instructions, and then the model will take care of the rest. Clear instructions do matter, but they are only the first step.

That realization marks a new stage of the journey. Authors who absorb it stop asking the model to carry the whole burden alone and start adding the supporting structures the work actually needs. In HIRMOS, that matters for extension quality. Serious extensions need more than good intent and good prompts. They need governed collection, governed surfaced outputs when appropriate, self-validation, and fail-closed behavior when trust would otherwise be lost.

In HIRMOS, **Beyond Clear Instructions** is a framework pattern for building stronger AI-assisted workflows.

This page is the practical guide to that pattern. Use it when you want to understand it quickly, explain it to other authors, or decide whether your extension needs more than clear instructions.

## The five pillars

Beyond Clear Instructions has five pillars.

### 1. Clear instructions

This is the starting point.

The runnable surface must make the required work clear enough that an author, reviewer, or operator can understand what the entrypoint is supposed to do.

Good signs:
- the entrypoint clearly states what it must produce;
- the steps are concrete enough to follow;
- the required checks are visible instead of implied.

Weak signs:
- the entrypoint says to "analyze" or "review" without defining what a correct result must include;
- the required output is left to model intuition;
- the extension expects the model to "figure out the structure" on its own.

Clear instructions are mandatory. They are the first pillar, not the whole pattern.

## The next frontier after clear instructions

Once the work becomes more synthesis-heavy, more trust-sensitive, or more multi-step, clear instructions alone stop being enough. That is where the next four pillars matter.

### 2. Intermediate templates for collection and normalization

Use an intermediate template when the run must gather material from more than one place before producing a result.

This pillar protects the handoff between collection and synthesis. It gives the run a governed place to record what was found before anything is summarized.

Typical signals that you need it:
- multiple sources contribute to the result;
- the run combines the main entrypoint path with hooks;
- different branches or artifacts feed one final summary;
- omissions could happen between collection and synthesis.

Simple example:
- weak pattern: several inputs are read, then the model jumps straight to a final summary;
- stronger pattern: the run first fills an intermediate record showing what each source contributed, then writes the final summary from that governed record.

### 3. Required surfaced-output templates

Use a surfaced-output template when the final result needs a stable, governed shape.

This pillar protects the handoff between internal work and surfaced output. It makes sure the result appears in a form the Orchestrator can actually trust and use.

Typical signals that you need it:
- the output is trust-sensitive;
- the Orchestrator will make decisions from it;
- missing sections would mislead the reader;
- the result should always follow a known structure.

Simple example:
- weak pattern: a paused cycle returns a freeform paragraph;
- stronger pattern: the paused output must follow a required template with the expected sections present every time.

### 4. Self-validation

If the run can check its own work before surfacing it, it should.

This is the point where the entrypoint stops relying only on intention and starts checking whether the clear instructions were actually followed.

Typical self-validation questions:
- were the instructions actually followed;
- were all required sections produced;
- is the intermediate record complete;
- does the surfaced output still match the collected inputs;
- is the result honest about what is complete and what is not.

Simple example:
- weak pattern: the model produces a final report and stops;
- stronger pattern: the model checks whether the instructions were actually satisfied, including any required structure, before surfacing the result.

### 5. Closed-fail behavior

When trust would be lost by continuing, the run should fail closed.

That means the run should not quietly continue past a material defect.

Typical signals that closed-fail behavior is needed:
- the intermediate record is incomplete or misleading;
- the required surfaced-output template is incomplete or misleading;
- self-validation fails;
- the run cannot truthfully preserve trust if it continues.

Simple example:
- weak pattern: a report is missing major sections, but the run still presents it as complete;
- stronger pattern: the run stops, surfaces the defect honestly, and refuses to overclaim completion.

## How the five pillars work together

The first pillar gives the model a clear job.

The second and third pillars reduce the places where real work usually drifts:
- collection drift,
- summary drift, and
- output drift.

The fourth pillar checks whether the clear instructions were actually satisfied and whether the governed structures were actually used correctly.

The fifth pillar protects trust when that verification fails on something material. If the workflow cannot truthfully preserve trust after that point, it should not continue as if everything is fine.

That is why Beyond Clear Instructions matters. It turns clear instructions into a more trustworthy workflow.

## How HIRMOS applies this pattern in a real workflow

One place this pattern appears in HIRMOS is a governed system-design-cycle workflow exposed by a marketplace extension. Clear instructions were not enough to make that workflow trustworthy. The run had to gather inputs, normalize unresolved items from multiple producers, surface a governed result, validate its own work, and stop honestly when trust could not be preserved.

This example matters because it shows the five pillars working together in a real workflow, not just in theory.

### Pillar 1 in practice — clear instructions

In `system-design-cycle`, the runnable surface does not just say "do system design." It declares:
- the purpose of the run;
- the artifacts it must produce;
- the allowed terminal states;
- the required normalized intake artifacts;
- the hook-aware enrichment points; and
- the required runtime trust artifacts.

The governing spec goes further. It names concrete steps such as:
- verifying `REQUIREMENTS_INPUT_PACK.md`;
- checking whether `STAGED_DELIVERY_TARGETS.md` is also required;
- centralizing unresolved items before completion;
- updating `RUN_TRACE.md`, `VALIDATION_TRACE.md`, and `CYCLE_STATUS.md`; and
- blocking completion if required artifacts are missing.

What to copy into your own extension:
- name the real artifacts the run must produce;
- name the allowed terminal states;
- name the checks that decide whether the run can honestly claim completion.

### Pillar 2 in practice — intermediate templates for collection and normalization

`system-design-cycle` does not jump straight from many inputs into one final summary.

It uses intermediate artifacts to normalize the work before later synthesis. Two important examples are:
- normalized intake artifacts such as `REQUIREMENTS_INPUT_PACK.md` and, when relevant, `STAGED_DELIVERY_TARGETS.md`;
- unresolved-item collection artifacts such as `UNRESOLVED_ITEMS_INVENTORY.md`, `UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`, `UNRESOLVED_ITEMS_FEED.md`, and `UNRESOLVED_ITEMS_LEDGER.md`.

That chain is the key. The run first gathers unresolved items from multiple producers, including assumptions and open questions. Then it inventories them, reconciles them, builds a governed feed, and records them in a ledger before allowing completion.

This is exactly what pillar 2 is for: do not trust a final summary that skipped the governed collection stage.

What to copy into your own extension:
- when several producers feed one result, add an intermediate template chain instead of jumping straight to summary;
- make each stage visible enough that a reviewer can see what was collected, normalized, and carried forward;
- do not let the final summary be the first place where the combined truth appears.

### Pillar 3 in practice — required surfaced-output templates

`system-design-cycle` also governs what gets surfaced at the end.

It does not allow the run to pause or complete with an ad hoc chat paragraph. It uses required surfaced-output structures such as:
- `CYCLE_STATE_REPORT.md` when the cycle reaches a paused or completed reviewable state;
- `PAUSED_TEMPLATE.md` and `COMPLETED_TEMPLATE.md` for the surfaced cycle outcome shape; and
- a defined paused-output schema that must include cycle state, unresolved items, why they matter, proposed Orchestrator direction, and continuation options.

This is pillar 3 working in the open. The run is not only gathering the right information. It is also required to surface that information in a form the Orchestrator can inspect and trust.

What to copy into your own extension:
- if the final output is decision-shaping, require a surfaced-output template before the run can claim completion;
- make the mandatory sections explicit;
- do not let trust-sensitive outputs depend on whatever final wording the model happens to choose.

### Pillar 4 in practice — self-validation

`system-design-cycle` does not assume the job was done just because clear instructions were provided.

The cycle turns its own promises into explicit checks. For example:
- `VALIDATION_TRACE.md` records whether required intake artifacts were required, present, and usable;
- unresolved-item checks fail if a required producer is missing an `Unresolved Items` section;
- reconciliation checks fail if an inventory item remains unreconciled;
- feed checks fail if a feed item lacks source inventory item IDs;
- integrity checks fail if materially distinct unresolved items were merged without explicit justification.

This is the real point of self-validation: not just checking whether a file exists, but checking whether the clear instructions were actually satisfied. Did the run collect what it said it would collect? Did it reconcile what it said it would reconcile? Did it surface a result that still matches the governed intermediate record?

What to copy into your own extension:
- turn your most important instructions into explicit end-of-run checks;
- validate both the intermediate structures and the final surfaced result;
- treat “the file exists” and “the instructions were satisfied” as two different questions.
### Pillar 5 in practice — closed-fail behavior

`system-design-cycle` does not quietly continue when trust would be lost.

If the self-validation pillar fails on something material, the cycle does not smooth it over with a confident completion claim. It blocks completion, stays paused when needed, and surfaces the defect honestly so the Orchestrator can decide what happens next.

In practice, that means:
- required trust artifacts must exist before completion can be claimed;
- materially incomplete unresolved-item collection or reconciliation blocks completion;
- gating items remain visible instead of being hidden inside a “mostly done” summary;
- the cycle pauses for Orchestrator direction instead of pretending the work is trustworthy when it is not.

What to copy into your own extension:
- define the self-validation failures that must block completion;
- make the blocked or paused state explicit;
- prefer an honest pause or fail-closed result over a misleading success state.
## What this example should teach you

If you are designing your own extension, this is the practical lesson:
- pillar 1 tells the model what job to do;
- pillar 2 governs what gets collected before synthesis;
- pillar 3 governs what gets surfaced at the end;
- pillar 4 checks whether the instructions were actually satisfied;
- pillar 5 protects trust when that verification fails.

If you can explain your own workflow at that level and point to the concrete structures that support each pillar, you are ready to start applying this pattern.

## Practical author checklist

When designing a runnable entrypoint, ask:
- Are the instructions clear?
- Can this run self-validate before surfacing the result?
- Do we need an intermediate template before final synthesis?
- Do we need a required surfaced-output template?
- Should the run fail closed if those structures are incomplete or misleading?

If the answer to the first question is yes, that is a good start.

If the answer to the later questions is also yes, you are already in Beyond Clear Instructions territory.

## Want the canonical framework pattern?

If you want the canonical doctrine, deeper applicability rules, or the review standard for this pattern, see:
- [Beyond Clear Instructions](../../core/authority/extensions/beyond-clear-instructions.md)
