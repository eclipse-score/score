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
:decision: Bazel-native flat layout — headers next to sources with full project-prefixed include paths; non-public headers isolated in an impl/ subpackage with restricted Bazel visibility
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
Components rely on Bazel's `hdrs` attribute to designate public headers, with headers
and sources living together in a flat directory, and the dominant pattern in
`communication` and `baselibs` draws the public/private boundary with an `impl/`
subpackage plus Bazel `visibility`. The main gap is not the layout itself but the lack
of a *single, documented* convention (include-path style, private-header placement,
target granularity), which this decision fills.

### Goals

- Make the public API surface of a component obvious without reading `BUILD.bazel`.
- Map cleanly onto Bazel's `hdrs`/`srcs` split with minimal boilerplate.
- Produce clean, collision-free `#include` paths for consumers.
- Keep the public API consumable by non-Bazel tools and build systems without source rewrites.
- Keep the developer's day-to-day workflow (edit `.h` next to `.cc`) reasonable.

### External references

- **[The Canonical Project Structure (P1204R0)](https://open-std.org/JTC1/SC22/WG21/docs/papers/2018/p1204r0.html)** —
  WG21 paper (Boris Kolpackov, 2018) proposing a canonical layout for new C++
  projects. It places headers and sources **next to each other** under a
  project-named subdirectory (`<name>/<name>/…`), uses project-prefixed include
  paths (`#include <name/foo.hpp>`), and keeps implementation-detail/private headers
  in a `details/`/`private/` subdirectory. Its *Source Directory* section explicitly
  argues **against** the separate `include/` + `src/` split.
- **[The Pitchfork Layout (PFL)](https://github.com/vector-of-bool/pitchfork)** —
  a community convention whose *separated* variant places public headers under
  `include/` and private headers/sources under `src/`. It is an unfinished,
  experimental effort: the repository has **no releases** and no commits since
  ~2018, so it is a historical reference point rather than a maintained standard.
- **[Bazel C++ use cases](https://bazel.build/tutorials/cpp-use-cases)** — the Bazel
  documentation presents the `include/` layout only as a *legacy adoption* case and
  steers new projects toward repo-root-relative include paths.

These references do **not** converge: the Canonical Project Structure and Bazel
deliberately keep headers next to sources, whereas the (dormant) Pitchfork Layout
separates them. This DR follows the former.

---

## Options Considered

### Option A: Bazel-native flat layout (headers next to sources) — recommended

Headers and sources live **next to each other** in the component's package, and the
public/private boundary is drawn by Bazel: public headers go in `hdrs`, everything
non-public is isolated in an `impl/` subpackage whose `visibility` is restricted to
the component. Headers are included by their **full, project-prefixed repo-root path**
(`#include "score/mw/my_component/my_component.h"`), which keeps include paths globally
unique. This matches the WG21 Canonical Project Structure and the Bazel recommendation
for new projects, and it is the dominant pattern already used by `communication` and
`baselibs`.

```
score/mw/my_component/
├── BUILD.bazel
├── my_component.h            # public  -> hdrs
├── my_component.cc           # source  -> srcs
└── impl/                     # non-public: restricted visibility
    ├── BUILD.bazel
    ├── internal_helper.h     # implementation detail
    └── internal_helper.cc
```

#### Advantages

- **Encapsulation enforced by Bazel, not by hope:** `impl/` visibility is restricted
  to the component's own subpackages, so no external target can depend on internal
  headers — even the ones a public, templated header must `#include`. The boundary
  holds for template/inline APIs, which the `include/`-vs-`src/` split cannot (see
  Option B).
- **Headers and sources stay together:** Declarations sit next to their
  implementations. Editing, grep'ing, "go to file", and code browsing (e.g. on GitHub)
  all land on the pair immediately, and the source tree makes *likely affected code*
  visible by vicinity — a maintainability property, not just a navigation convenience.
- **No `strip_include_prefix` machinery:** The header's on-disk path *is* its include
  path. Non-Bazel tools and other build systems see the file exactly where the
  `#include` says it is, so packaging and IDE indexing work without source rewrites.
- **Collision-free include paths:** The repo-root project prefix
  (`score/mw/my_component/…`) makes every include path globally unique, exactly like
  an `include/<component>/` nesting would — the uniqueness comes from the prefix, not
  from a dedicated `include/` directory.
- **Cheap moves and API changes:** Promoting a private header to public, or extracting
  a sub-library, is a `BUILD.bazel`/visibility edit plus at most a move into or out of
  `impl/`; consumer include paths stay stable.
- **Small, cache-friendly targets:** The layout naturally encourages one focused
  `cc_library` per package rather than a single repo-wide `glob`, preserving Bazel's
  incremental-build and caching benefits.

#### Disadvantages

- **Public surface is discoverable via package/visibility rules, not a single
  directory:** A reviewer identifies the API from what is *not* under `impl/` (and from
  `hdrs`) rather than from one folder. The `impl/` convention makes this clear in
  practice, but it is less immediately obvious than a dedicated `include/` tree.
- **Discipline required on include paths:** Contributors must consistently use the
  full project-prefixed path; a reset prefix (`strip_include_prefix = "."`) would
  collapse paths to bare filenames and bypass the project-scoped include convention.

---

### Option B: Separate `include/` directory (Pitchfork-style split)

Public headers are placed in a dedicated `include/` directory, nested under the
component name (`include/my_component/*.h`); private headers and sources live under
`src/`. Consumers reach public headers via `strip_include_prefix = "include"`.

```
score/mw/my_component/
├── BUILD.bazel
├── include/
│   └── my_component/
│       └── my_component.h     # public -> hdrs
└── src/
    ├── my_component.cc        # source  -> srcs
    ├── internal_helper.h      # private -> srcs
    └── internal_helper.cc
```

#### Advantages

- **Public API is greppable in one place:** For a component with a *purely* runtime
  (non-templated) API, the `include/` tree lists the public contract without reading
  `BUILD.bazel`.
- **Folder-copy packaging *when* the split holds:** If no public header includes a
  private one, exporting the public API is a copy of `include/`.

#### Disadvantages

- **The encapsulation benefit is a false promise for template/inline APIs.** Public
  headers routinely `#include` implementation-detail headers (templates, inline
  functions). Those details must then also live under `include/` (e.g. in a `details/`
  subdir), so the split degrades into "all headers in `include/`" and negates its own
  main advantage. This is the central argument of P1204R0 §4 against the split, and it
  directly affects S-CORE's templated APIs.
- **`strip_include_prefix` makes non-Bazel packaging *harder*, not easier.** The
  include path the source uses (`my_component/my_component.h`) no longer matches the
  header's on-disk location (`include/my_component/my_component.h`). Any tool that is
  not Bazel-aware — other build systems, IDEs, static analyzers, downstream packagers
  — sees mismatched paths and needs source-level rewrites to compile.
- **Cumbersome navigation and maintenance:** Every edit hops between `include/` and
  `src/`; grep and code browsing are split across two trees; the vicinity signal for
  "likely affected code" is lost.
- **Extra nesting and boilerplate:** `include/my_component/` plus `strip_include_prefix`
  on every target, and source generators rarely support writing headers and sources to
  different directories.
- **Poor fit for Bazel and for modules:** Bazel documents this layout only as a
  *legacy adoption* case; keeping template-referenced private headers out of the public
  package fights Bazel's "no referencing files in other packages" rule and pushes
  toward large, cache-unfriendly targets.
- **No collision advantage over Option A:** Uniqueness comes from the component-name
  prefix, which Option A already provides via the repo-root path.
- **Conflicts with the module folder structure decision:** Reintroducing `src/` (and an
  `include/` tree) contradicts `dec_rec__platform__module_folder_structure`
  (DR-003-proc, Alternative C), which removes the component-level `src/` folder (see
  *Relationship to DR-003-proc*).

---

### Option C: Hybrid (public headers in `include/`, private next to sources)

A hybrid that keeps `include/my_component/` for strictly public headers while leaving
private headers next to their `.cc`.

```
score/mw/my_component/
├── BUILD.bazel
├── include/
│   └── my_component/
│       └── my_component.h     # public -> hdrs
├── my_component.cc            # source  -> srcs
├── internal_helper.h          # private -> srcs
└── internal_helper.cc
```

This option is **not recommended.** It inherits Option B's `strip_include_prefix`
tooling problems while adding an inconsistent private-header location, and — like
Option B — it cannot cleanly separate public from private for template/inline APIs,
where an implementation-detail header included by a public header would have to move
into `include/`. In practice it collapses toward either Option A or "all headers in
`include/`", so it is listed only for completeness.

---

## Evaluation Criteria

| Criterion                                       | A: Bazel-native flat | B: Separate `include/` | C: Hybrid |
|-------------------------------------------------|:--------------------:|:----------------------:|:---------:|
| Encapsulation enforced (incl. template APIs)    |         ++           |           -            |    -      |
| Public API greppable without `BUILD.bazel`      |          +           |          ++            |    +      |
| Collision-free `#include` paths                 |         ++           |          ++            |    ++     |
| Works with non-Bazel tools / packaging          |         ++           |           --           |    -      |
| Headers next to sources (maintainability)       |         ++           |           --           |    +      |
| Bazel-idiomatic / small cache-friendly targets  |         ++           |           -            |   +/-     |
| Low Bazel boilerplate                           |         ++           |           -            |    -      |
| Fit for modularized / template-heavy code       |         ++           |           --           |    -      |
| Alignment with Canonical Structure & Bazel      |         ++           |           --           |    -      |

Legend: `++` strong fit, `+` partial, `+/-` neutral, `-` weak, `--` poor.

---

## Decision Proposal

**Option A: Bazel-native flat layout.** Public and private headers live next to their
sources in the component package; the public/private boundary is enforced by Bazel by
isolating non-public headers in an `impl/` subpackage with restricted `visibility`; and
all headers are included by their full, project-prefixed repo-root path
(`#include "score/mw/my_component/my_component.h"`). Targets are kept small and focused
rather than repo-wide globs.

This matches the WG21 Canonical Project Structure, the Bazel recommendation for new
projects, and the pattern already dominant in `communication` and `baselibs`, so it
requires **no large-scale migration** of existing code.

The separate `include/` split (Option B) and the hybrid (Option C) are **rejected**:
their headline benefit — physical public/private separation — does not survive
template/inline APIs (a public header that includes an implementation-detail header
forces that header back into the public tree), and `strip_include_prefix` decouples the
include path from the on-disk location, which breaks non-Bazel tooling and makes
packaging harder rather than easier.

### Rationale

1. **Encapsulation actually holds.** Restricting `impl/` visibility guarantees that no
   external target can depend on an internal header, including the
   implementation-detail headers that public *template* headers must `#include`. The
   `include/`/`src/` split cannot promise this, because those details end up in the
   public tree anyway (P1204R0 §4).

2. **The include path matches the file on disk.** Without `strip_include_prefix`, the
   path a source writes is exactly where the header lives, so non-Bazel build systems,
   IDEs, analyzers, and packagers work without source rewrites.

3. **Collision-free by prefix.** The repo-root project prefix
   (`score/mw/my_component/…`) makes include paths globally unique — the same guarantee
   `include/<component>/` would give, without the extra directory. Collision safety is
   orthogonal to the directory split and achievable in every option.

4. **Maintainability by vicinity.** Headers next to sources keep declaration and
   definition together and make likely-affected code visible in the tree; grep and
   GitHub browsing are not split across `include/` and `src/`.

5. **Idiomatic and cheap.** It is what Bazel and the Canonical Project Structure
   recommend, it keeps targets small and cache-friendly, and it needs no migration of
   the existing `communication`/`baselibs` code.

The main cost — a public surface that is discovered via the `impl/` convention and
Bazel visibility rather than a single `include/` folder — is mitigated by consistently
applying the `impl/` pattern and by keeping `hdrs` lists explicit and small.

### Relationship to DR-003-proc (Module Folder Structure)

This decision must stay consistent with the process decision on the module folder
structure, `dec_rec__platform__module_folder_structure` (proposed in
[PR #3194](https://github.com/eclipse-score/score/pull/3194)). That DR selects
**Alternative C**, which **removes the component-level `src/` folder** and places the
component's include and source files (plus unit tests) directly under
`score/<component_name>/`, with optional `<lower_level_comp>/` nesting.

- **Option A aligns with it.** Headers and sources sit directly in the component
  package (no `src/`, no top-level `include/`), and the finer-grained `impl/`
  subpackage is a permitted sub-structure choice under Alternative C's opt-out clause.
- **Options B and C conflict with it.** Both reintroduce a `src/` folder and add an
  `include/` tree — exactly the `src/` split that DR-003-proc removed. Adopting Option
  B/C would require overriding the process decision per module. This conflict was
  raised in the review of this DR and is a further reason to prefer Option A.

---

## Bazel Usage

### Defining a component

Public headers go into `hdrs`; implementation lives under an `impl/` subpackage whose
visibility is restricted to the component. No `strip_include_prefix` is needed, and
targets stay small (one focused `cc_library` per package rather than a repo-wide
glob).

```python
# score/mw/my_component/BUILD.bazel
cc_library(
    name = "my_component",
    srcs = ["my_component.cc"],
    hdrs = ["my_component.h"],
    deps = ["//score/mw/my_component/impl:internal_helper"],
    visibility = ["//visibility:public"],
)
```

```python
# score/mw/my_component/impl/BUILD.bazel
cc_library(
    name = "internal_helper",
    srcs = ["internal_helper.cc"],
    hdrs = ["internal_helper.h"],
    # only the component itself may depend on implementation details
    visibility = ["//score/mw/my_component:__subpackages__"],
)
```

A header at `score/mw/my_component/my_component.h` is included by its full repo-root
path:

```cpp
#include "score/mw/my_component/my_component.h"
```

Implementation-detail headers use the same full-path scheme
(`#include "score/mw/my_component/impl/internal_helper.h"`) and are unreachable from
outside the component because of the restricted `impl/` visibility — even when a
public, templated header includes them.

> **Note on `strip_include_prefix` / `include_prefix` / `includes`:** avoid these for
> public APIs. They decouple the include path from the on-disk location, which breaks
> non-Bazel tooling and packaging. Use them only when a third-party layout forces it.

### Consuming the component within the repository

```python
cc_library(
    name = "app",
    srcs = ["app.cc"],
    deps = ["//score/mw/my_component"],
)
```

```cpp
// app.cc
#include "score/mw/my_component/my_component.h"   // impl/ headers are not reachable
```

Bazel rejects an `#include` of an `impl/` header from an external target, because that
target is outside the `impl/` package's visibility. The package layout and the build
system enforce the same boundary.

### Consuming the component as a Bazel module (bzlmod)

The full repo-root include path is stable whether the component is consumed in-repo,
via `local_path_override`, or as a released module:

```python
# MODULE.bazel (downstream)
bazel_dep(name = "score_my_component", version = "1.0.0")
```

```python
cc_library(
    name = "downstream",
    srcs = ["downstream.cc"],
    deps = ["@score_my_component//score/mw/my_component"],
)
```

```cpp
#include "score/mw/my_component/my_component.h"
```

Because the include path is the repo-root path — with no prefix stripping — the
consumer's source is identical across in-repo, override, and registry consumption, and
it also matches what non-Bazel tools expect.

### Consumer view across the layouts

How consuming a component as a module looks from the outside:

| Option | Producer `BUILD.bazel` (public headers) | Consumer `#include` | Works with non-Bazel tools |
|--------|------------------------------------------|---------------------|:--------------------------:|
| **A: Bazel-native flat** | `hdrs = ["my_component.h"]` — no prefix handling; `impl/` visibility-restricted | `#include "score/mw/my_component/my_component.h"` — full repo-root path, namespaced by package | yes — path matches file on disk |
| **B: Separate `include/`** | `hdrs = glob(["include/**/*.h"])`, `strip_include_prefix = "include"` | `#include "my_component/my_component.h"` | no — path ≠ on-disk location |
| **C: Hybrid** | as B | `#include "my_component/my_component.h"` | no — as B |

The Option A include path is already unique and namespaced by its package location, so
it needs no prefix machinery, and it is the one path that also matches what non-Bazel
tools and other build systems see on disk.

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
  encodes the public/private model via `hdrs`/`srcs`, and the
  [Bazel C++ use cases](https://bazel.build/tutorials/cpp-use-cases) doc treats the
  `include/` split only as a *legacy adoption* case. This is **Option A**.
- **WG21 Canonical Project Structure (P1204R0):** The
  [P1204R0 paper](https://open-std.org/JTC1/SC22/WG21/docs/papers/2018/p1204r0.html)
  keeps headers and sources **together** under a project-named directory and its
  *Source Directory* section explicitly argues **against** the `include/` + `src/`
  split (it "offers little benefit … has a number of real drawbacks, and does not fit
  modularized projects well"). This also aligns with **Option A**.
- **Pitchfork Layout (PFL):** The
  [Pitchfork Layout](https://github.com/vector-of-bool/pitchfork) is the main
  reference for the separated `include/` + `src/` variant (**Options B/C**). It is an
  unfinished, experimental convention with no releases and no activity since ~2018, so
  there is **no single mandated "industry standard"** here — real-world C++ projects
  use both styles.

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
  `//score/mw/com:__subpackages__`). This is **Option A**, and it is exactly the
  layout this DR recommends.
- Where a clean external include path *is* wanted, S-CORE reaches for different Bazel
  levers — `includes` (futurecpp), `strip_include_prefix`/`include_prefix`
  (static_reflection, lifecycle) — rather than a single agreed mechanism. The
  `lifecycle` pattern even keeps a flat on-disk layout but *synthesizes* a logical
  `score/mw/...` path via `include_prefix`.

The absence of a unified convention — and the divergence in both directory layout and
Bazel mechanism — across these repositories is a primary motivation for this design
decision.

---


## Consequences

### Positive

- Encapsulation is enforced by Bazel `visibility` (via the `impl/` subpackage) and
  holds even for template/inline public APIs.
- Include paths match on-disk locations, so non-Bazel tools, IDEs, analyzers, and
  packagers work without source rewrites.
- Consumers get stable, collision-free, project-prefixed include paths regardless of
  how the dependency is resolved (in-repo, override, or registry module).
- Headers stay next to sources, preserving maintainability and the "likely affected
  code" vicinity signal.
- No migration is required for the existing `communication`/`baselibs` code, which
  already follows this layout; and the decision aligns with the Canonical Project
  Structure and Bazel guidance.

### Negative / Costs

- The public surface is discovered via the `impl/` convention and Bazel visibility
  rather than a single `include/` folder, so the convention must be applied
  consistently.
- Contributors must consistently use full project-prefixed include paths and must not
  reset the prefix (e.g. `strip_include_prefix = "."`).

### Follow-Up Actions

- Provide a component template / scaffolding (directory skeleton + `BUILD.bazel`) that
  encodes the flat layout with an `impl/` subpackage and restricted `visibility`.
- Document the convention in the S-CORE contribution guidelines and C++ coding
  guidelines, including the full-path include rule and the `impl/` visibility pattern.
- Consider a lightweight CI/lint check that flags implementation-detail headers
  reachable from external targets, or public headers included via non-canonical
  (non-repo-root) paths.
