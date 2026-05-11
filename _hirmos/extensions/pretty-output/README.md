# pretty-output

**A tiny hook-only extension that formats another extension’s output.**

`pretty-output` is a demo extension. It shows how a non-runnable extension can attach to a published hook and add behavior without owning the original command.

---

You can use this extension without studying its internal folders. For most users, this README is enough to understand what it is for.

## Fast mental model

```text
hello-world ── exposes hook ──► hello-world.after-main-output
                                     ▲
                                     │
                               pretty-output *
                                     │
                                     └──► formats the final output
```

- `*` supporting demo extension

---

## How this extension looks inside Hirmos

```text
_hirmos/
└── extensions/
    └── pretty-output/
        ├── README.md                  # extension landing page
        ├── extension.yaml             # manifest
        ├── hooks/                     # hook-owned behavior files
        ├── index.md                   # extension overview entry file
        ├── CHANGELOG.md
        └── UPGRADE_GUIDE.md
```

---

## FAQ

**Can I run `pretty-output` directly?**  
No. It is a hook-only extension.

**What does it need to work?**  
It needs a target extension that exposes the hook it subscribes to. In this demo, that target is `hello-world`.

**Why does this extension exist?**  
To show the smallest useful shape of a hook-only extension.

---

## What do you want to do next?

- Compare it with the runnable demo extension: [`../hello-world/README.md`](../hello-world/README.md)
- Read the contributed hook file: [`hooks/hello-world.after-main-output.md`](./hooks/hello-world.after-main-output.md)
- Learn how hook authoring works: [`../../docs/3-extend-contribute/extensions/hooks-authoring.md`](../../docs/3-extend-contribute/extensions/hooks-authoring.md)
