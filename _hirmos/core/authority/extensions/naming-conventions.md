# Extension Naming Conventions

## Purpose

Define the framework-wide extension doctrine for naming extension-owned files and surfaces.

Use this authority file when deciding:
- how extension ids should be formed
- how extension-owned filenames should remain stable and readable
- how public entrypoint names, hook file names, and related surfaces should be named

For broader framework-wide filename doctrine, see:
- [Extension-local spec surface rules](../shared/cross-folder-rules.md)
- [Deep reference rules](../shared/deep-reference-rules.md)

## General naming posture

Good names are descriptive, boring, and easy to scan.

Prefer names that reveal:
- the extension family
- the artifact or workflow unit
- the command or seam purpose

Do not use naming cleverness where clarity is the real need.

## Extension ids

Extension ids should use:
- lowercase letters
- numbers
- hyphens

The id should match the extension folder name.

## Public entrypoint names

Public entrypoint names should reveal the public workflow purpose.

Use names that help an operator understand whether the surface is:
- a high-level cycle
- a narrower lower-level entrypoint
- a bounded specialized run surface

When `-cycle` materially helps operator understanding for a governed workflow, use it.

For entrypoint doctrine, see:
- [Extension entrypoints](./entrypoints.md)

## Hook file names

Hook file names should be hook-target-based and easy to reason about.

A healthy hook file name helps a human understand the subscribed seam quickly.

Names should stay aligned with the declared hook target rather than inventing separate naming games.

For hook doctrine, see:
- [Extension hooks](./hooks.md)

## Extension-local spec, doc, and support filenames

Use stable lowercase kebab-case names for extension-owned doctrine and guidance files unless a stronger established framework rule applies.

Names should help the reader infer the role of the file instead of requiring discovery by opening it blindly.

## README and standard support surfaces

Use established names where the framework already gives them meaning, such as:
- `README.md`
- `extension.yaml`
- `index.md` for the main entry file when that remains the healthiest default

Do not rename standard surfaces casually.

## Review tests

When reviewing extension naming, ask:
- Are names descriptive and stable?
- Does the extension id obey the framework rule?
- Do public entrypoint names reveal their purpose?
- Are hook filenames aligned with the seam they subscribe to?
- Does the naming reduce cognitive load rather than add it?
