# AGENTS.md — Eclipse S-CORE Feature Pipeline (Generic Template)

> **What is AGENTS.md:** A [README for AI coding agents](https://agents.md/) that standardizes how
> automated assistants (Copilot, Codex, Cursor, Gemini CLI, Claude Code, Aider, Jules, …) work on
> **[Eclipse S-CORE](https://eclipse-score.github.io/score/main/)** *features*.
> Place this file at the repo root; place a tailored copy in each
> [`docs/features/<feature>/`](https://eclipse-score.github.io/score/main/features/index.html) folder.
> **Precedence:** the closest `AGENTS.md` to the edited file wins; explicit user chat prompts override everything.

---

## 1. Project overview

- **Project:** [Eclipse Safe Open Vehicle Core (S-CORE)](https://eclipse.dev/score/) — an open-source,
  functional-safety-compliant software platform for Software Defined Vehicles (SDVs) / high-performance ECUs.
- **A *Feature*** is the highest-level logical entity: a set of interrelated components managed together,
  owning its **feature requirements** and **feature architecture**
  ([Features index](https://eclipse-score.github.io/score/main/features/index.html)).
- **Main repo:** [`eclipse-score/score`](https://github.com/eclipse-score/score) holds stakeholder requirements,
  the high-level architecture, the feature list, and the decomposition into modules. Most features are also
  implemented in their own [module repositories](https://github.com/eclipse-score).
- **Compliance targets:** [ISO 26262](https://www.iso.org/standard/68383.html) (functional safety, up to ASIL_B),
  [ISO 21434](https://www.iso.org/standard/70918.html) (cybersecurity) and ASPICE. Final-system compliance stays
  with the series project — S-CORE is a generic foundation, not a ready-to-integrate product.

## 1a. Where to place this file

- **This file → repository root:** `eclipse-score/score/AGENTS.md` (and, optionally, the root of each
  [module repo](https://github.com/eclipse-score) such as `persistency/AGENTS.md`).
- **Feature-scoped copies → one per feature folder:** `docs/features/<feature>/AGENTS.md`.
- **Discovery rule (nearest wins):** an agent editing `docs/features/persistency/requirements/foo.rst`
  reads `docs/features/persistency/AGENTS.md` first, then falls back to the root `AGENTS.md`; an explicit
  user chat instruction overrides both ([precedence model](https://agents.md/)).
- **Optional overrides:** drop an `AGENTS.override.md` beside an `AGENTS.md` for temporary/personal
  instructions without touching the shared file (it takes precedence at the same level).
- **File must be committed** (not git-ignored) so every contributor and CI-based agent sees it.

```text
score/
├── AGENTS.md                         # ROOT — global agent context (place here)
└── docs/features/
    ├── persistency/AGENTS.md         # feature-scoped (nearest wins)
    ├── communication/AGENTS.md
    └── <feature>/AGENTS.md           # one per feature
```

## 2. Features (list)

Each feature lives under [`docs/features/<folder>/`](https://github.com/eclipse-score/score/tree/main/docs/features)
and, when implemented, in a matching module repo.

- [AI Platform](https://github.com/eclipse-score/score/tree/main/docs/features/ai_platform) — `ai_platform`
- [Analysis Infrastructure](https://github.com/eclipse-score/score/tree/main/docs/features/analysis-infra) — `analysis-infra`
- [Base Libraries](https://github.com/eclipse-score/score/tree/main/docs/features/baselibs) — `baselibs` · `feat__baselibs` · ASIL_B · [repo](https://github.com/eclipse-score/baselibs)
- [Code Generation](https://github.com/eclipse-score/score/tree/main/docs/features/code_generation) — `code_generation`
- [Communication (LoLa)](https://github.com/eclipse-score/score/tree/main/docs/features/communication) — `communication` · `feat__com_communication` · ASIL_B · [repo](https://github.com/eclipse-score/communication)
- [Configuration](https://github.com/eclipse-score/score/tree/main/docs/features/configuration) — `configuration`
- [Diagnostic & Fault Management](https://github.com/eclipse-score/score/tree/main/docs/features/diagnostics) — `diagnostics` · [repo](https://github.com/eclipse-score/inc_diagnostics)
- [Frameworks (FEO)](https://github.com/eclipse-score/score/tree/main/docs/features/frameworks) — `frameworks` · `feat__feo` · ASIL_B · [repo](https://github.com/eclipse-score/feo)
- [Lifecycle](https://github.com/eclipse-score/score/tree/main/docs/features/lifecycle) — `lifecycle` · `feat__lifecycle` · ASIL_B · [repo](https://github.com/eclipse-score/lifecycle)
- [NonIPC](https://github.com/eclipse-score/score/tree/main/docs/features/nonipc) — `nonipc`
- [Orchestration](https://github.com/eclipse-score/score/tree/main/docs/features/orchestration) — `orchestration` · `feat__orchestration` · ASIL_B · [repo](https://github.com/eclipse-score/orchestrator)
- [Persistency](https://github.com/eclipse-score/score/tree/main/docs/features/persistency) — `persistency` · `feat__persistency` · ASIL_B · [repo](https://github.com/eclipse-score/persistency)
- [Security & Cryptography](https://github.com/eclipse-score/score/tree/main/docs/features/security_crypto) — `security_crypto` · [repo](https://github.com/eclipse-score/inc_security_crypto)
- [Time](https://github.com/eclipse-score/score/tree/main/docs/features/time) — `time` · [repo](https://github.com/eclipse-score/time)

> Cross-cutting feature IDs also tracked in the platform: `feat__logging`, `feat__os`, `feat__tracing`.

## 3. Repository & folder hierarchy (src / docs)

```text
<repo-root>/
├── AGENTS.md                     # Root agent context (this file)
├── MODULE.bazel / BUILD / .bazelrc  # Bazel build definitions
├── .devcontainer/                # Reproducible dev environment (recommended)
├── .github/workflows/            # CI/CD: build, tests, docs, integration gates
├── src/                          # Source code (C++ / Rust)
├── tests/ (or test/)             # Unit & integration tests (gtest/gmock, cargo test)
└── docs/
    ├── index.rst
    └── features/
        ├── index.rst             # Feature list (needtable of feat__*)
        └── <feature>/            # e.g. persistency, communication, time …
            ├── AGENTS.md         # Feature-scoped agent context (nearest wins)
            ├── index.rst         # Feature landing page
            ├── requirements/     # feat_req__<feature>__* (sphinx-needs)
            └── architecture/     # feature architecture, interfaces, diagrams
```

## 4. Dev environment & setup

- **Preferred:** open the repo in the [S-CORE devcontainer](https://github.com/eclipse-score/devcontainer)
  (`Reopen in Container` in VS Code). All tools/compilers/extensions are pre-installed.
- **Manual:** install [Bazelisk](https://github.com/bazelbuild/bazelisk), Python 3.x, Graphviz/Dot, and a C++
  compiler (gcc). See the [Development Environment guide](https://eclipse-score.github.io/score/main/contribute/development/development_environment.html).
- **Toolchain:** Bazel (build/test/docs orchestration), [Sphinx + sphinx-needs](https://eclipse-score.github.io/docs-as-code/main/)
  (docs & traceability), PlantUML + draw.io (diagrams), C++ & Rust, gtest/gmock.

## 5. Build, test & docs commands

```bash
bazel run  //:help              # List useful bazel commands
bazel test //...                # Run all tests
bazel test //:format.check      # Check formatting
bazel run  //:format.fix        # Auto-fix formatting
bazel run  //:copyright.check   # Check license headers
bazel run  //:copyright.fix     # Fix license headers
bazel run  //:docs              # Build docs -> _build
bazel run  //:live_preview      # Live docs preview at http://127.0.0.1:8000
bazel run  //:ide_support       # Enable Esbonio live preview/linting in the IDE
bazel test --test_tag_filters=docs-build   # Run only docs-tagged tests
```

- Fix any test, type, or formatting error until the whole suite is green **before** committing.
- Add or update tests and requirements traceability for any code you change.

## 6. Code, requirements & docs conventions

- **Requirements & architecture** are written in reStructuredText using **sphinx-needs** directives
  (`feat_req__<feature>__*`, architecture `comp_arc_*`), kept traceable to tests and stakeholder requirements.
- Follow the language coding guidelines in [`docs/contribute`](https://github.com/eclipse-score/score/tree/main/docs/contribute)
  (C++ and Rust guidelines) and let `format.fix` / linters enforce style — do not hand-format.
- Every source and doc file must carry a valid **license header** (Apache-2.0). Verify with `copyright.check`.
- Keep feature requirements, architecture, and diagrams in sync when changing behavior.

## 7. Pull request & commit guidelines

- **Commit messages** follow the repo `.gitlint` rules; use conventional prefixes (`feat`, `fix`, `chore`, `docs`).
- **Before pushing:** run `bazel test //...`, `format.check`, and `copyright.check`.
- Keep PRs feature-scoped; reference the feature ID (e.g. `ft:persistency`) and any requirement IDs.
- Ensure CI gates in [`.github/workflows`](https://github.com/eclipse-score/score/tree/main/.github/workflows) pass.

## 8. AI security & governance (short)

- **Human-in-the-loop:** agents propose; a maintainer reviews and approves every change. No auto-merge.
- **Never** weaken safety/security artifacts (ASIL ratings, crypto, requirements) without explicit human sign-off.
- **No secrets** in code, docs, prompts, or logs; never commit credentials or tokens.
- **Stay in scope:** edit only the nearest feature's files; keep changes traceable (requirement → arch → test).
- **Compliance:** respect ISO 26262 / ISO 21434 / ASPICE intent; flag, don't bypass, safety-relevant checks.

## 9. Links

- Features index — https://eclipse-score.github.io/score/main/features/index.html
- AGENTS.md standard — https://agents.md/
- Existing PR (AI agent context) — https://github.com/eclipse-score/score/pull/2967
- Docs-as-Code — https://eclipse-score.github.io/docs-as-code/main/
- Contribution guide — https://github.com/eclipse-score/score/blob/main/CONTRIBUTION.md
