<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->
(DR-003-Arch)=
# DR-003-Arch: Public Header Location and Directory Structure for C++ Components

* **Date:** 2026-08-19

```{dec_rec} Public Header Location and Directory Structure for C++ Components
:id: dec_rec__arch__public_header_layout
:status: proposed
:version: 1
:context: Architecture
:decision: Separate include/ directory for public API headers, private headers next to sources
```

---

## Context / Problem

As we modularize our C++ components with Bazel, we need a standardized directory
layout that defines where public (API) and private (implementation) headers live.
This decision directly impacts API encapsulation, developer workflow, packaging for
non-Bazel consumers, and integration with Bazel's strict header visibility model
(`hdrs` vs. `srcs`).

Bazel is authoritative here: a `cc_library` distinguishes between headers that form
the compilable public surface of a target (`hdrs`) and headers that are purely
internal to the compilation of that target (`srcs`). A downstream target may only
`#include` headers that appear in the `hdrs` of a library it directly depends on.
The physical directory layout does not by itself enforce this boundary — the `BUILD`
file does. The question is therefore how to structure directories so that the
physical layout *reinforces* the logical API boundary that Bazel enforces, rather
than working against it.

### Current state in S-CORE

Within S-CORE there is mostly **no separate `include/` directory** in use today.
Components rely completely on Bazel's `hdrs` attribute to designate public headers,
with headers and sources living together in a flat directory. This works for Bazel,
but it makes the public contract of a component invisible at the file-system level:
a developer has to open `BUILD.bazel` to learn which headers are public, and
extracting a clean public SDK for non-Bazel consumers requires filtering.

### Goals

- Make the public API surface of a component obvious without reading `BUILD.bazel`.
- Map cleanly onto Bazel's `hdrs`/`srcs` split with minimal boilerplate.
- Produce clean, collision-free `#include` paths for consumers.
- Enable simple, folder-level packaging of the public API for non-Bazel consumers.
- Keep the developer's day-to-day workflow (edit `.h` next to `.cc`) reasonable.

### External references

- **[The Pitchfork Layout (PFL)](https://github.com/vector-of-bool/pitchfork)** —
  in particular the *separated header placement* convention, where public headers
  live under [`include/`](https://joholl.github.io/pitchfork-website/#tld.include)
  and private headers/sources live under `src/`.
- **[The Canonical Project Structure (P1204R0)](https://open-std.org/JTC1/SC22/WG21/docs/papers/2018/p1204r0.html)** —
  WG21 paper describing a canonical layout with public headers under a
  project-named subdirectory.

Both references converge on placing public headers under a dedicated,
project-named include root.

---

## Options Considered

### Option A: Flat Directory Structure (headers and sources mixed)

All public headers, private headers, and source files live together in the same
directory (e.g. `libs/my_lib/`). Public vs. private is expressed *only* through the
Bazel `hdrs`/`srcs` split. This is the current de-facto S-CORE convention.

```
libs/my_lib/
├── BUILD.bazel
├── my_lib.h          # public  -> hdrs
├── my_lib.cc         # source  -> srcs
├── internal_helper.h # private -> srcs
└── internal_helper.cc
```

#### Advantages

- **Zero Bazel path overhead:** No `strip_include_prefix` / `includes` juggling. The
  header's on-disk path *is* its include path, so there is one obvious way to write
  an `#include` and no divergence between what the file tree shows and what the
  compiler sees.
- **Easier local navigation:** Declarations sit next to their implementations; no
  jumping between distant folders in the IDE. Refactoring that splits or renames a
  unit touches a single directory, and "go to file" / fuzzy-open lands on the pair
  immediately.
- **Less nesting:** Avoids redundant paths like `.../my_lib/include/my_lib/`, which
  keeps both the file tree and relative `#include` statements short.
- **Lowest friction for small or leaf components:** For a component with one or two
  public headers, a private helper, and its sources, the flat layout has the best
  effort-to-value ratio — the `include/` + `src/` split adds structure that such a
  component does not need. This matches how most of S-CORE is organized today.
- **Single source of truth for the API boundary:** The public surface is defined in
  exactly one place — the `hdrs` list in `BUILD.bazel`. There is no second, implicit
  contract encoded in the directory layout that could drift out of sync with the
  build file (e.g. a header physically under `include/` but not actually in `hdrs`,
  or vice versa).
- **Bazel already enforces the boundary:** A consumer can only `#include` headers a
  dependency lists in `hdrs`; reaching for a private header in `srcs` fails the
  build regardless of where the file physically sits. The encapsulation guarantee
  therefore does not depend on the directory structure at all — the flat layout
  loses no *enforcement*, only *visibility*.
- **Cheapest migrations and moves:** Moving a component, extracting a sub-library, or
  promoting a private header to public is a `BUILD.bazel` edit only — no files move
  on disk, so diffs stay small and reviews stay focused on the API change itself.
- **Fewer glob edge cases:** With everything in one directory, `glob` patterns are
  simple and there is no risk of a misplaced file silently falling outside an
  `include/**` or `src/**` pattern.

#### Disadvantages

- **Public API not visible from the file tree:** Developers must read `BUILD.bazel`
  to learn which headers are public.
- **Accidental API exposure:** A private header may be listed in `hdrs` by mistake,
  or a consumer may reach for an internal header.
- **Poor scalability:** As the library grows the folder becomes cluttered.
- **Packaging difficulty:** Extracting only public headers for external (non-Bazel)
  delivery requires filtering scripts rather than a folder copy.
- **Weaker as a published module:** Without a prefix to strip, a consumer sees the
  producer's repo-relative path, which leaks the internal layout and is not
  namespaced by component:

  ```cpp
  // consuming @my_lib as a module, flat layout
  #include "libs/my_lib/my_lib.h"
  ```

  Getting the clean `#include "my_lib/my_lib.h"` requires adding `include_prefix`
  (or naming the flat dir `my_lib/`), i.e. reintroducing the Bazel path machinery
  Option A set out to avoid.

---

### Option B: Separate `include/` Directory (industry standard)

Public headers are placed in a dedicated `include/` directory, nested under the
component name (`include/my_lib/*.h`) to prevent include-path collisions. Private
headers and sources live under `src/`.

```
libs/my_lib/
├── BUILD.bazel
├── include/
│   └── my_lib/
│       └── my_lib.h       # public -> hdrs
└── src/
    ├── my_lib.cc          # source  -> srcs
    ├── internal_helper.h  # private -> srcs
    └── internal_helper.cc
```

#### Advantages

- **High encapsulation:** The public contract is physically isolated. It is
  immediately clear to a consumer what may be used.
- **Clean BUILD files:** `hdrs = glob(["include/**/*.h"])` and
  `srcs = glob(["src/**"])` without risk of accidentally exposing private files.
- **Standardized packaging:** Exporting the public API is a single folder copy.
- **Clear architectural intent:** Naturally enforces good API-design discipline and
  aligns with the Pitchfork Layout and the Canonical Project Structure.
- **Collision-free includes:** The `my_lib/` nesting guarantees globally unique
  include paths, e.g. `#include "my_lib/my_lib.h"`.

#### Disadvantages

- **Bazel path handling:** Requires `strip_include_prefix = "include"` so consumers
  can write `#include "my_lib/my_lib.h"` rather than `include/my_lib/my_lib.h`.
- **Folder redundancy:** The `include/my_lib/` nesting feels redundant to some.
- **Navigation overhead:** Minor cost from switching between `include/` and `src/`
  during active development.

---

### Option C: Hybrid Directory Structure

Only strictly public API headers are placed in `include/my_lib/*.h`. All private
headers (`*.h`) and implementation sources (`*.cc`) sit directly in the main
directory (or a local `src/` next to it).

```
libs/my_lib/
├── BUILD.bazel
├── include/
│   └── my_lib/
│       └── my_lib.h       # public -> hdrs
├── my_lib.cc              # source  -> srcs
├── internal_helper.h      # private -> srcs
└── internal_helper.cc
```

#### Advantages

- **Reduced navigation overhead:** Developers open `include/` only when changing the
  public contract; internal headers stay next to their `.cc`.
- **Clear Bazel separation:** `hdrs` matches `include/**`, `srcs` matches the rest.
- **Clean API packaging:** Copying `include/` still yields a pristine public SDK
  with no leakage of private helpers.

#### Disadvantages

- **Inconsistent private-header location:** Some headers live in `include/`, some in
  the root — developers may be unsure where to look.
- **Strict include conventions required:** Private headers use relative paths
  (`#include "internal_helper.h"`) while public headers use the nested path
  (`#include "my_lib/my_lib.h"`), which must be applied consistently.

---

## Evaluation Criteria

| Criterion                         | A: Flat | B: Separate `include/` | C: Hybrid |
|-----------------------------------|:-------:|:----------------------:|:---------:|
| Public API visible in file tree   |   --    |          ++            |    +      |
| API encapsulation / leak safety   |    -    |          ++            |    +      |
| Clean `#include` paths (no collisions) |  +/-  |          ++            |    +      |
| Bazel `hdrs`/`srcs` clarity        |    -    |          ++            |    +      |
| Non-Bazel packaging (folder copy)  |   --    |          ++            |    +      |
| Bazel boilerplate (low is better)  |   ++    |           -            |   +/-     |
| Local navigation (edit .h next .cc)|   ++    |           -            |    +      |
| Scalability of large components    |    -    |          ++            |    +      |
| Consistency / low cognitive load   |    +    |          ++            |    -      |
| Alignment with PFL / P1204         |    -    |          ++            |    +      |

---

## Decision Proposal

**Option B: Separate `include/` Directory** — public API headers live under
`include/<component>/`, private headers and sources live under `src/`.

For components that are small, header-heavy, or where the public/private split is
trivial, **Option C (Hybrid)** is an accepted variation: keep the `include/<component>/`
public root, but allow private headers to sit next to their `.cc` in `src/` (or the
component root). The invariant that must always hold is: **everything a consumer is
allowed to `#include` lives under `include/<component>/`, and nothing else does.**

**Accepted alternative — flat layout with an `impl/` subpackage.** Because the
dominant pattern in `communication` and `baselibs` today is a flat layout that draws
the public/private boundary with an `impl/` subpackage plus Bazel `visibility` (see
*Prior Art & Existing S-CORE Practice*), that pattern is **explicitly accepted** as an
equivalent alternative to Option B/C. It satisfies the same invariant by a different
mechanism: public headers live at the component root, everything non-public lives
under `<component>/impl/**` whose `visibility` is restricted to the component's own
subpackages. Components choosing this variant **must** keep implementation headers out
of any `hdrs` reachable by external consumers and restrict `impl/` visibility
accordingly. This avoids a large-scale migration of existing components while still
guaranteeing an enforced, discoverable API boundary. The trade-off versus Option B is
that the public surface is discoverable via package/visibility rules rather than a
single directory, and packaging for non-Bazel consumers is less trivial.

### Rationale

1. **The public contract becomes a first-class, visible artifact.** A reviewer or
   consumer can see the entire API surface by looking at `include/<component>/`
   without opening `BUILD.bazel`. This is the single biggest weakness of the current
   flat approach.

2. **It maps directly onto Bazel's `hdrs`/`srcs` model.** The directory boundary and
   the Bazel visibility boundary coincide, so the file layout reinforces the
   guarantee Bazel already enforces, instead of leaving it implicit.

3. **Collision-free include paths.** Nesting under the component name
   (`include/my_lib/`) guarantees that `#include "my_lib/foo.h"` is globally unique
   across the whole build graph, which matters at S-CORE scale with many modules.

4. **Trivial packaging for non-Bazel consumers.** Delivering the public SDK is a
   folder-level copy of `include/`, not a filtering script over a mixed directory.

5. **Ecosystem alignment.** The layout matches the Pitchfork Layout (separated
   header placement) and the WG21 Canonical Project Structure, lowering the barrier
   for external contributors and tooling.

The main cost — a small amount of Bazel boilerplate (`strip_include_prefix`) and the
`include/<component>/` nesting — is one-time, mechanical, and easily templated.

---

## Bazel Usage

### Defining a component

Public headers go into `hdrs` and are exposed through `strip_include_prefix` so that
the on-disk `include/` prefix is removed from the include path consumers see:

```python
# libs/my_lib/BUILD.bazel
cc_library(
    name = "my_lib",
    srcs = glob([
        "src/**/*.cc",
        "src/**/*.h",      # private headers are NOT part of the public API
    ]),
    hdrs = glob(["include/**/*.h"]),
    strip_include_prefix = "include",
    visibility = ["//visibility:public"],
)
```

With `strip_include_prefix = "include"`, a header at
`libs/my_lib/include/my_lib/my_lib.h` is included by consumers as:

```cpp
#include "my_lib/my_lib.h"
```

Within the component's own sources, private headers are included with a path
relative to `src/`, e.g. `#include "internal_helper.h"`, and never leak through
`hdrs`.

> **Note on alternatives:** `include_prefix` can *add* a prefix, and `includes`
> adds a directory to the compiler search path (with the well-known
> `-I`/`-isystem` caveats). `strip_include_prefix` is preferred because it is
> hermetic, does not pollute the include path of downstream targets, and yields the
> clean `<component>/<header>.h` form. Avoid `includes` for public APIs unless a
> third-party layout forces it.

### Consuming the component within the repository

```python
cc_library(
    name = "app",
    srcs = ["app.cc"],
    deps = ["//libs/my_lib"],
)
```

```cpp
// app.cc
#include "my_lib/my_lib.h"   // only headers under include/my_lib/ are reachable
```

Bazel will reject an `#include` of a private header from `src/`, because it is not in
the `hdrs` of `//libs/my_lib`. The directory layout and the build system thus enforce
the same boundary.

### Consuming the component as a Bazel module (bzlmod)

When a component is published as a Bazel module, the `include/<component>/` layout
carries over unchanged. A downstream repository adds the dependency in its
`MODULE.bazel`:

```python
# MODULE.bazel (downstream)
bazel_dep(name = "my_lib", version = "1.0.0")
```

and consumes it exactly as an in-repo target:

```python
cc_library(
    name = "downstream",
    srcs = ["downstream.cc"],
    deps = ["@my_lib//:my_lib"],
)
```

```cpp
#include "my_lib/my_lib.h"
```

Because the public include root is stable and prefix-stripped, the include paths a
consumer writes are identical whether the component is consumed in-repo, via a
`local_path_override`, or as a released module from a registry. This decouples the
consumer's source from the producer's on-disk layout and is the key property that
makes the module boundary clean.

### Consumer view across the three layouts

How consuming `@my_lib` as a module looks from the outside, for each option:

| Option | Producer `BUILD.bazel` (public headers) | Consumer `#include` |
|--------|------------------------------------------|---------------------|
| **A: Flat** | `hdrs = glob(["*.h"])` — no prefix handling | `#include "libs/my_lib/my_lib.h"` — leaks repo layout, not namespaced |
| **A: Flat + prefix** | `hdrs = [...]`, `include_prefix = "my_lib"` | `#include "my_lib/my_lib.h"` — clean, but re-adds the boilerplate A avoided |
| **B: Separate `include/`** | `hdrs = glob(["include/**/*.h"])`, `strip_include_prefix = "include"` | `#include "my_lib/my_lib.h"` — clean and stable |
| **C: Hybrid** | `hdrs = glob(["include/**/*.h"])`, `strip_include_prefix = "include"` | `#include "my_lib/my_lib.h"` — clean and stable |

In all cases the `deps` and `MODULE.bazel` entry are identical
(`deps = ["@my_lib//:my_lib"]`, `bazel_dep(name = "my_lib", version = "1.0.0")`);
only the resulting `#include` path differs. Options B and C give the same clean,
layout-independent path out of the box; Option A only matches it by reintroducing a
prefix.

---

## Prior Art & Existing S-CORE Practice

There is **no single mandated industry layout** for public C++ headers with Bazel;
two established schools of thought exist, and S-CORE currently mixes both.

### External guidance

- **Bazel-native / Google style (no `include/`):** The
  [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html#Header_Files)
  requires headers to be included by their **repo-root-relative path**
  (`#include "score/mw/foo/bar.h"`), with no dedicated `include/` directory. The
  [Bazel `cc_library` reference](https://bazel.build/reference/be/c-cpp#cc_library)
  encodes the same public/private model via `hdrs`/`srcs`. This is essentially
  **Option A**, but with repo-root paths rather than bare filenames.
- **General open-source convention (dedicated `include/`):** The
  [Pitchfork Layout (PFL)](https://github.com/vector-of-bool/pitchfork) and the
  [WG21 Canonical Project Structure (P1204R0)](https://open-std.org/JTC1/SC22/WG21/docs/papers/2018/p1204r0.html)
  both place public headers under a project-named `include/<lib>/` root — matching
  **Options B/C**.

### Existing practice inside S-CORE

The following reflects the state of the `eclipse-score` GitHub organization on the
**`main` branch as of 2026-08-19**. It is a snapshot and may change; re-check the
current `main` before relying on it. As of that date there is **no unified
convention** — the following patterns coexist:

| Pattern | Example repo | Mechanism |
|---------|--------------|-----------|
| **Flat, headers next to sources; public/private via an `impl/` subpackage + Bazel `visibility`** (dominant) | `communication` (`score/mw/com`), most of `baselibs` (`os`, `json`, `mw/log`, `concurrency`, `filesystem`) | plain `hdrs`/`srcs`, repo-root include paths (`#include "score/mw/com/types.h"`); implementation headers under `.../impl/` with restricted visibility |
| `include/` directory, exposed via `includes` | `baselibs` (`language/futurecpp`) | headers under `include/score/*.hpp`, `includes = ["include"]` → `#include <score/utility.hpp>` |
| `include/` directory, exposed via `strip_include_prefix` (+ `include_prefix`) | `baselibs` (`static_reflection_with_serialization`) | `strip_include_prefix = "include"`, `include_prefix = "static_reflection_with_serialization"` |
| Flat + `strip_include_prefix = "."` | `baselibs` (`utils/base64`) | prefix reset so header is included as `#include "base64.h"` |
| Flat on disk + synthesized logical path via `include_prefix` | `lifecycle`, `inc_daal` | `include_prefix = "score/mw/lifecycle"`, `strip_include_prefix = "/score/launch_manager/src"` |

Two observations worth calling out:

- The **dominant** real-world pattern in both `communication` and `baselibs` is *not*
  a dedicated top-level `include/` (Option B). It is a **flat layout** where the
  public/private boundary is drawn by an `impl/` subpackage plus Bazel `visibility`
  (e.g. `communication` keeps its public API in `score/mw/com/*.h` and hides
  everything under `score/mw/com/impl/**`, whose visibility is restricted to
  `//score/mw/com:__subpackages__`). This is closer to **Option A** at repo scale and
  shows the recommendation of this DR is not yet the prevailing practice.
- Where a clean external include path *is* wanted, S-CORE reaches for different Bazel
  levers — `includes` (futurecpp), `strip_include_prefix`/`include_prefix`
  (static_reflection, lifecycle) — rather than a single agreed mechanism. The
  `lifecycle` pattern even keeps a flat on-disk layout but *synthesizes* a logical
  `score/mw/...` path via `include_prefix`.

The absence of a unified convention — and the divergence in both directory layout and
Bazel mechanism — across these repositories is a primary motivation for this design
decision.

---

## Header Name Collisions Across Modules

A common worry is what happens when several modules expose an identically named
header — for example `error.h`. The important point is that collisions are decided by
the **include-path string**, not the file name. Two `error.h` files coexist without
issue as long as their include paths differ:

```cpp
#include "score/filesystem/error.h"         // baselibs
#include "score/concurrency/future/error.h" // baselibs
```

Both exist side by side in `baselibs` today with no conflict, because the package
prefix makes them unique. A problem only arises when the path is shortened to the bare
file name and two dependencies provide it:

```cpp
#include "error.h"   // provided by module A AND module B → ambiguous
```

If a target depends on both libraries, `-I`/`-isystem` ordering decides which file
wins — the wrong header may be included, silently violating the One Definition Rule.
The **Bazel module name does not protect against this**: `@module_a` / `@module_b` do
not appear in the C++ include path by default; the path is determined solely by the
package location and by `strip_include_prefix` / `include_prefix` / `includes`.

Consequences per option:

- **Option A (flat, repo-root includes):** collision-safe *as long as* headers are
  included by their full repo-root path. The danger is resetting the prefix
  (`strip_include_prefix = "."` as in `utils/base64`, or `includes = ["."]`), which
  collapses the path to `#include "error.h"` and re-introduces the ambiguity globally.
- **Option B (`include/<component>/`):** collision-safe, but the protection comes from
  the **component-name nesting**, not from the `include/` directory itself. A flat
  `include/error.h` (without the `<component>` subdirectory) still collides.
- **Option C (Hybrid):** same as B — public headers stay unique via
  `include/<component>/`.
- **Flat + `impl/` + visibility:** same as A — the repo-root path is preserved, and
  the restricted `impl/` visibility additionally shrinks the set of externally
  reachable headers.

**Rule:** Uniqueness must be guaranteed by the include-path **prefix** (the project or
component name) — via the repo package path under Option A, or via the
`include/<component>/` nesting under Options B/C. A bare `include/` without a
component-named subdirectory does **not** solve the problem.

---

## Consequences

### Positive

- The public API of every C++ component is visible, isolated, and self-documenting.
- Bazel `hdrs`/`srcs` boundaries align with the physical layout, reducing accidental
  API leakage.
- Consumers get stable, collision-free include paths regardless of how the dependency
  is resolved (in-repo, override, or registry module).
- Public SDK packaging for non-Bazel consumers is a folder copy.
- The layout is consistent with widely used community conventions (PFL, P1204).

### Negative / Costs

- A modest, one-time increase in Bazel boilerplate (`strip_include_prefix`) and the
  `include/<component>/` nesting.
- Minor day-to-day navigation overhead from the `include/` ↔ `src/` split.
- Existing flat components must be migrated to gain the benefits (can be incremental).

### Follow-Up Actions

- Provide a component template / scaffolding (directory skeleton + `BUILD.bazel`) that
  encodes the `include/<component>/` + `src/` layout and `strip_include_prefix`.
- Document the convention in the S-CORE contribution guidelines and C++ coding
  guidelines, including the private-vs-public include-path rules.
- Define a migration path for existing flat components (opportunistic, per module).
- Consider a lightweight CI/lint check that flags private headers appearing in `hdrs`
  or public headers being included via non-canonical paths.
