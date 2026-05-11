# Public vs Private Extension Structure

Use this page to separate the parts of an extension people are meant to run or integrate with from the parts that stay internal. This is mainly a design and maintenance guide for keeping extension surfaces clear.

Need the canonical execution-surface rule? See [_hirmos/core/authority/core/entrypoint-execution-contract.md](../../../core/authority/core/entrypoint-execution-contract.md).

Extensions should be treated like packages with a public surface and private internals.

## Public surfaces

Public surfaces are the parts of an extension the framework is meant to run or integrate with directly.

These include:

- the default entrypoint declared by `entry`
- named public entrypoints declared by `entrypoints`
- declared hooks
- the documented extension contract in `README.md`

## Private internals

Private internals are files the extension uses to support public behavior without making those files permanent public contract.

These may include:

- helper docs
- internal Specs
- templates
- internal notes
- implementation-only support files

## Why the distinction matters

Without a public/private distinction:

- every internal file starts looking runnable
- refactoring becomes harder
- extension APIs become noisy and unstable
- coherence is harder to preserve

## Rule

Not every internal file should be runnable publicly.

Only manifest-declared entrypoints should be treated as public runnable surfaces.