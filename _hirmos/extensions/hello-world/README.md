# hello-world

**The smallest runnable Hirmos extension.**

`hello-world` is a demo extension. It exists to show the smallest useful shape of a runnable extension without bringing in heavy design, implementation, or hook complexity.

---

You can use this extension without studying its internal folders. For most users, this README is enough to understand what it is for.

## Fast mental model

```text
hirmos hello-world
        │
        ▼
   hello-world
        │
        └──► prints a simple message

Optional downstream hook example:
pretty-output * can format the result when installed
```

- `*` supporting demo extension

---

## How this extension looks inside Hirmos

```text
_hirmos/
└── extensions/
    └── hello-world/
        ├── README.md                  # extension landing page
        ├── extension.yaml             # manifest
        ├── index.md                   # default runnable entrypoint
        ├── CHANGELOG.md
        └── UPGRADE_GUIDE.md
```

---

## FAQ

**Why does this extension exist?**  
To make the smallest runnable extension shape easy to understand.

**Does it read or write framework artifacts?**  
No. It is intentionally minimal.

**Can other extensions interact with it?**  
Yes. `pretty-output` is the included example of a hook-only extension that formats its output.

---

## What do you want to do next?

- Read the extension file itself: [`index.md`](./index.md)
- Compare it with the hook demo extension: [`../pretty-output/README.md`](../pretty-output/README.md)
- Learn how to build your own extensions: [`../../docs/3-extend-contribute/extensions/creating-your-first-extension.md`](../../docs/3-extend-contribute/extensions/creating-your-first-extension.md)
