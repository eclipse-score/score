<!--
Copyright (c) 2025 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-002-Infra: Integration Testing in a Distributed Monolith

* **Status:** Agreed within Community
* **Owner:** Infrastructure Community
* **Date:** 2025-09-01

---
## Executive Summary

Large systems often span multiple repositories. Each repository can look “green” on its own, yet problems only show up when everything is combined. These late surprises slow down development and make debugging painful.

The concept described here turns a collection of separate repositories into a system that behaves like a single, continuously tested whole — ensuring the main line is always integrable across all components.

### Proposed Approach
- Every change in any repository is tested **in combination with the rest of the system**, not just in isolation.
- There are **two testing layers**:
  - a **fast feedback loop** (lightweight tests that run on every pull request BEFORE merge in any repository),
  - and a **deeper validation** (heavier tests run after merges or on a schedule BEFORE release in any repository).
- This setup guarantees that developers can trust the system as a whole to consistently work.

### Typical workflow

* Component PRs are created.
  * Run component local verification.
  * Run integration testing (quick).
* Post merge:
  * Run integration test (full).
* Only after successful integration testing (full) can a release be created.

### Benefits
- Problems across repositories are caught early.
- Developers spend less time coordinating merges (“merge after me” scenarios disappear).
- The project always has a “known good” baseline to fall back on, enabling stability while still moving fast.

Note: this concept is easily extendable to support multiple versions of S-CORE. But that's currently not required.

See Martin Fowler's [continuous integration](https://martinfowler.com/articles/continuousIntegration.html) article for a deeper dive into the topic.

---
## Introduction

Teams often split what is functionally a single system across many repositories. Each
repository can show a green build while the assembled system is already broken. This
article looks at how to bring system-level feedback earlier when you work that way. This
article does not argue for pull requests, trunk-based development, or continuous
integration itself. Those are well covered elsewhere. It also does not look into any
specific tools or implementations for achieving these practices - except for providing a
GitHub based example.

The context here assumes three things: you develop through pull requests with required
checks; you have multiple interdependent repositories that ship together; and you either
have or will create a central integration repository used only for orchestration. If any
of those are absent you will need to establish them first; the rest of the discussion
builds on them.

---
## Motivation / Where Problems Usually Appear
An interface change (for example a renamed field in a shared schema) is updated in two
direct consumers. Their pull requests pass. Another consumer several repositories away
still depends on the old interface and only fails once the whole set of changes reaches
main and a later integration run executes. The defect was present early but only visible
late. Investigation now needs cross-repo log hunting instead of a quick fix while the
change was still in flight.

Running full end-to-end environments on every pull request is rarely affordable.
Coordinated multi-repository changes are then handled informally through ad-hoc
ordering: “merge yours after mine”. Late detection raises cost and makes regression
origins harder to locate.

---
## Core Concepts
We model the integrated system as an explicit set of (component, commit) pairs captured
in a manifest. Manifests are derived deterministically from events: a single pull
request, a coordinated group of pull requests, or a post-merge refresh. A curated fast
subset of integration tests provides pre-merge feedback; a deeper suite runs after
merge. Passing suites produce a recorded manifest (“known good”). Coordinated
multi-repository change is treated as a first-class case—we validate the set as a unit
rather than relying on merge ordering.

Terminology (brief):
* Component - repository that participates in the assembled product (e.g. service API
  repo, shared library).
* Fast subset - curated integration tests finishing in single-digit minutes (protocol
  seams, migration boundaries, adapters).
* Tuple - mapping of component names to commit SHAs for one integrated build (e.g. {
  users: a1c3f9d, billing: 9e02b4c }).
* Known good - tuple + metadata (timestamp, suite, manifest hash) stored for later
  reproduction.

History & context: classic continuous integration assumed a single codebase; splitting
one system across repositories reintroduces coordination issues CI was intended to
remove. This adapts familiar CI principles (frequent integration, fast feedback,
reproducibility) to a multi-repository boundary. The central integration repository is a
neutral place to define participating components, build manifests, hold
integration-specific helpers (overrides, fixtures, seam tests), and persist known-good
records. It should not contain business logic; keeping it lean reduces accidental
coupling and simplifies review.

---
## Integration Workflows
We use three recurring workflows: a single pull request, a coordinated subset when
multiple pull requests must land together, and a post-merge fuller suite. Each produces
a manifest, runs an appropriate depth of tests, and may record the tuple if successful.

### Visual Overview
```{mermaid}
flowchart TB
  subgraph COMP[Component Repos]
    pr[PR opened / updated<br/>&lt;event&gt;]:::event --> comp_ci[Component tests]:::step

    trigger1[Merge to main<br/>&lt;event&gt;]:::event
  end

  subgraph INT[Integration Repo]
    comp_ci --> |dispatch|detect_changeset[Detect multi repository PRs]:::step
    knownGood[(Known good store)]:::artifact

    %% PR
    detect_changeset --> buildMan[Build PR/PRs manifest using PR/PRs SHA + known good others]:::step
    knownGood --> buildMan
    buildMan --> runSubset[Run fast subset of integration tests]:::step
    runSubset --> prFeedback[Provide Feedback in PR / all PRs]:::step

    %% Post-merge / scheduled full suite
    trigger1 -->|dispatch| fullMan[Build full manifest from latest mains of all repos]:::step
    trigger2[schedule<br/>&lt;event&gt;]:::event --> fullMan
    fullMan --> fullSuite[Run full integration test suite]:::step
    fullSuite --> fullPass{Full suite pass?}:::decision
    fullPass -->|Yes| knownGood
    fullPass -->|No| issue["Create Issue<br>(or a more clever automated bisect solution)"]:::red
  end
```
*High-level flow of integration workflows. Known good store feeds manifest construction for single and coordinated paths; full test suite success updates the store.*

### Single Pull Request
When a pull request opens or updates, its repository runs its normal fast tests. The
integration repository is also triggered with the repository name, pull request number,
and head SHA. It builds a manifest using that SHA for the changed component and the last
known-good SHAs for others, then runs the curated fast subset. The result is reported
back to the pull request. The manifest and logs are stored even when failing so a
developer can reproduce locally.

The subset is explicit rather than dynamically inferred. Tests in it should fail quickly
when contracts or shared schemas drift. If the list grows until it is slow it will
either be disabled or ignored; regular curation keeps it useful.

### Coordinated Multi-Repository Subset
Some changes require multiple repositories to move together (for example a schema
evolution, a cross-cutting refactor, a protocol tightening). We mark related pull
requests using a stable mechanism such as a common label (e.g. changeset:feature-x). The
integration workflow discovers all open pull requests sharing the label, builds a
manifest from their head SHAs, and runs the same fast subset. A unified status is posted
back to each pull request. None merge until the coordinated set is green. This removes
informal merge ordering as a coordination mechanism.

### Post-Merge Full Suite
After merges we run a deeper suite. Some teams trigger on every push to main; others run
on a schedule (hourly seems to be a common practice). Per-merge runs localise failures
but cost more; batched runs save resources but expand the search space when problems
appear. When the suite fails, retaining the manifest lets you bisect between the last
known-good tuple and the current manifest (using a scripted search across the changed
SHAs if multiple components advanced). On success we append a record for the tuple with
a manifest hash and timing data.

### Manifests
Manifests are minimal documents describing the composition. They allow reconstruction of
the integrated system later.

Single pull request example:
```
pr: 482
component_under_test:
  name: docs-as-code
  repo: eclipse-score/docs-as-code
  sha: 6bc901f2
others:
  - name: component-a
    repo: eclipse-score/component-a
    ref: 34985hf8 # based on last known-good
  - name: component-b
    repo: eclipse-score/component-b
    ref: a4fd56re # based on last known-good
subset: pr_fast
timestamp: 2025-08-13T12:14:03Z
```

Coordinated example:
```
components_under_test:
  - name: users-service
    repo: eclipse-score/users-service
    branch: feature/new_email_index
    ref: a57hrdfg
    pr: 16
  - name: auth-service
    repo: eclipse-score/auth-service
    branch: feature/lenient-token-parser
    ref: q928d46b75
    pr: 150
others:
  - name: billing-service
    repo: eclipse-score/billing-service
    ref: a4fd56re # based on last known-good
subset: pr_fast
changeset: feature-x
```

Large configuration belongs elsewhere; manifests should stay readable and diffable.

---
## Example: GitHub Actions (Conceptual)
*Conceptual outline; not yet implemented here.*

Trigger from a component repository:
```
name: integration-pr
on: [pull_request]
jobs:
  dispatch:
    runs-on: ubuntu-latest
    steps:
      - name: Dispatch to integration repo
        uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.INTEGRATION_TRIGGER_TOKEN }}
          repository: eclipse-score/reference_integration
          event-type: pr-integration
          client-payload: >-
            {"repo":"${{ github.repository }}","pr":"${{ github.event.pull_request.number }}","sha":"${{ github.sha }}"}
```

Integration repository receiver (subset):
```
on:
  repository_dispatch:
    types: [pr-integration]
jobs:
  pr-fast-subset:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Parse payload
        run: echo '${{ toJson(github.event.client_payload) }}' > payload.json

      - name: Materialize composition
        run: gen_pr_manifest.py last_known_good.yaml payload.json > manifest.pr.yaml

      - name: Render MODULE overrides
        run: render_overrides.py manifest.pr.yaml > MODULE.override.bzl

      - name: Bazel test (subset)
        run: bazel test //integration/subset:pr_fast --override_module_files=MODULE.override.bzl

      - name: Store manifest & results
        uses: actions/upload-artifact@v4
        with:
          name: pr-subset-${{ github.run_id }}
          path: |
            manifest.pr.yaml
            bazel-testlogs/**/test.log
```

Post-merge full suite:
```
on:
  schedule: [{cron: "15 * * * *"}]
  repository_dispatch:
    types: [component-merged]
jobs:
  full-suite:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate new last_known_good.yaml
        run: update_last_known_good.py last_known_good.yaml > last_known_good.yaml

      - name: Bazel test (full)
        run: bazel test //integration/full:all --test_tag_filters=-flaky

      - name: Persist known-good tuple (on success)
        if: success()
        run: |
          git add last_known_good.yaml
          git commit -m "update known good"

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: full-${{ github.run_id }}
          path: |
            bazel-testlogs/**/test.log
```

### Recording Known-Good Tuples
Known-good records are stored append-only.
```
[
  {
    "timestamp": "2025-08-13T12:55:10Z",
    "tuple": {
      "docs-as-code": "6bc901f2",
      "component-a": "91c0d4e1",
      "component-b": "a44f0cd9"
    },
    "manifest_sha256": "4c9b7f...",
    "suite": "full",
    "duration_s": 742
  }
]
```
Persisting enables reproduction (attach manifest to a defect), audit (what exactly
passed before a release), gating (choose any known-good tuple), and comparison (diff
manifests to isolate drift) without relying on (rather fragile) links to unique runs in
your CI system.

---
## Operating It
**Curating the fast subset:** Tests should fail quickly when public seams change. Keep
the list explicit (e.g. //integration/subset:pr_fast). Remove redundant tests and
quarantine flaky ones; review periodically (monthly or after significant interface
churn) to preserve signal.

**Handling failures:** For a failing pull request subset: inspect manifest + log;
reproduce locally with a script consuming the manifest. For a failing coordinated set:
treat all related pull requests as atomic. For a failing post-merge full suite: bisect
between the last known-good tuple and current manifest (script permutations if multiple
repositories changed) to narrow cause. Distinguish real regressions from test fragility.

**Trade-offs and choices:** Manifests + SHAs avoid tag noise and keep validation close
to heads. Two tiers (subset + full) offer a clear mental model; add more only with
evidence. A central orchestration repository centralises caching, secrets, and audit
history.

**Practical notes:** Cache builds to stabilise subset runtime. Hash manifests (e.g.
SHA-256) for concise references. Expose an endpoint or badge showing the latest known
good. Generate overrides; do not hand-edit ephemeral files. Optionally lint the subset
target for allowed directories.

**Avoiding pitfalls:** Diff-based dynamic test selection often misses schema or contract
drift. Ad-hoc manual edits to integration config reduce reproducibility. Merge ordering
as coordination defers detection to the last merge.

**Signs it is working:** Interface breakage is caught pre-merge. Coordinated change sets
show unified status. Multi-repository regressions are localised rapidly using stored
manifests.

---
## Releases and Bazel Registry

Bazel modules should be released only once they are verified, which in this setup is
equivalent to being included in the known-good store. This does not imply that all
verified versions need to end up in a release. That's still up to the module
maintainers.

However in some cases pre-releases are even mandatory: when two modules are verified
together (multi repo PR) and one depends on the other, the PR cannot be merged without
internally releasing the dependent module, and setting the appropriate dependency in the
other.

---
## Summary
By expressing the integrated system as explicit manifests, curating a fast integration
subset for pull requests, and running a deeper post-merge suite, you move discovery of
cross-repository breakage earlier while keeping costs predictable. Each successful run
leaves a reproducible record, making release selection and debugging straightforward.
The approach lets a distributed codebase behave operationally like a single one.

*Further reading:* Continuous Integration (Fowler), Continuous Delivery (Humble &
Farley), trunk-based development resources.
