# Versioning Contract

## Purpose

Define the authoritative Hirmos versioning contract for both the framework itself and installed extensions.

Use this authority file when deciding:
- how framework versioning is declared
- how extension versioning is declared
- how extension-to-core compatibility is expressed
- what changelog and upgrade surfaces are expected
- what minimum release and upgrade signals should exist for maintainers and reviewers

This file is the canonical versioning doctrine for Hirmos. Do not restate competing versioning rules elsewhere.

## Scope

This contract covers:
- framework versioning
- extension versioning
- extension-to-core compatibility declarations
- changelog expectations
- upgrade-guide expectations
- minimum release and upgrade signals used by review and maintenance workflows

This file does not replace:
- [Extension manifest authority](../core/extension-manifest-authority.md) for canonical manifest field interpretation
- concrete framework or extension `CHANGELOG.md` files, which record actual change history
- concrete framework or extension `UPGRADE_GUIDE.md` files, which record actual upgrade guidance for a specific release line

## Framework versioning

The framework declares its current version through:
- `/_hirmos/VERSION`

The framework records framework-level release history through:
- [Framework changelog](../../../CHANGELOG.md)

The framework records framework-level upgrade guidance through:
- [Framework upgrade guide](../../../UPGRADE_GUIDE.md)

Framework versioning should remain explicit and easy to inspect from the framework root.

## Extension versioning

Each installed extension declares its own version through:
- `version` in `extension.yaml`

Each installed extension declares its framework-compatibility range through:
- `requires_core` in `extension.yaml`

Extension versioning is independent from the framework version. Compatibility is expressed through `requires_core`, not by reusing the framework version number.

For the exact Core interpretation of `version` and `requires_core`, see:
- [Extension manifest authority](../core/extension-manifest-authority.md#version)
- [Extension manifest authority — `requires_core`](../core/extension-manifest-authority.md#requires_core)

## Release and upgrade signals

Healthy versioned surfaces expose enough maintainer-visible signals that change and compatibility are easy to reason about.

### Framework release and upgrade signals

The framework should expose:
- `/_hirmos/VERSION`
- [Framework changelog](../../../CHANGELOG.md)
- [Framework upgrade guide](../../../UPGRADE_GUIDE.md)

### Extension release and upgrade signals

A healthy installed extension should normally expose:
- `version` in `extension.yaml`
- `requires_core` in `extension.yaml`
- `CHANGELOG.md`
- `UPGRADE_GUIDE.md`

The minimum acceptable strength of these surfaces may vary by maturity, but the extension should not leave versioning and upgrade expectations ambiguous.

## Changelog expectations

A changelog should help a maintainer or reviewer answer:
- what changed
- whether the change is additive, behavioral, or breaking
- whether downstream adopters should care

A changelog should not be a vague placeholder once an extension or framework has begun evolving across multiple meaningful revisions.

## Upgrade guide expectations

An upgrade guide should help a maintainer or adopter answer:
- what needs action during upgrade
- whether any migration or manual adjustment is required
- what changed in contract, behavior, or artifact expectations

An upgrade guide may be minimal for an initial stable baseline, but it should grow as real upgrade complexity appears.

## Review implications

When review commands evaluate versioning and maintenance hygiene, they should use this contract as the primary authoritative source.

Review should look for:
- explicit version declarations
- explicit compatibility declarations where applicable
- changelog presence and usefulness appropriate to maturity
- upgrade guidance presence and usefulness appropriate to maturity
- clarity rather than ambiguity in release and upgrade signals

## Reuse over restatement

When another file needs to mention Hirmos versioning expectations, prefer referencing this authority file rather than restating the rule locally.

Use:
- a whole-file reference when the full contract is relevant
- a deep reference when only framework versioning, extension versioning, or release and upgrade signals are the true basis
