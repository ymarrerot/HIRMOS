# Use HIRMOS

Use this lane when you want to install HIRMOS, start a real run, or understand the normal workflow inside an AI coding tool.

## Recommended path

1. [Getting Started](getting-started/README.md)
2. [Quickstart](getting-started/quickstart.md)
3. [Commands](getting-started/commands.md)
4. [First Real Run](getting-started/first-real-run.md)
5. [Multi-Session Work](getting-started/multi-session-work.md) when the work is larger than one bounded session

## The basic rhythm

```text
hirmos start "<request>"
→ review the governed checkpoint
→ answer only decisions that matter
→ hirmos continue through the next allowed boundary
→ hirmos close when evidence supports close
```

## Work shapes

HIRMOS uses the smallest honest structure for the request:

- **single-session route** for bounded work;
- **delivery route** for larger durable work;
- **phase/session route** for the next slice of an accepted delivery;
- **IU implementation route** when implementation units are needed.

When IU mode applies, expect an IU Planning pause before IU Execution.

## Examples

- [Delivery Baseline and Phase/Session Flow](examples/delivery-baseline-and-phase-session.md)
- [Scope Authority Surfaces](examples/scope-authority-surfaces.md)
