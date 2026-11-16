<!-- ----------------------------------------------------------------------------
  Copyright (c) 2026 Contributors to the Eclipse Foundation

  See the NOTICE file(s) distributed with this work for additional
  information regarding copyright ownership.

  This program and the accompanying materials are made available under the
  terms of the Apache License Version 2.0 which is available at
  https://www.apache.org/licenses/LICENSE-2.0

  SPDX-License-Identifier: Apache-2.0
----------------------------------------------------------------------------- -->

# Merge queue guidance for maintainers

This is optional guidance for repository maintainers, not a project-wide requirement.
Maintainers can choose another setup when its trade-offs suit their repository better.
The alternatives below explain those trade-offs.

## How-to: Recommended setup

Use GitHub's native merge queue with optional label-enabled checks on PRs:

* Run fast checks on PRs and again in the queue.
* Run expensive checks, such as QNX builds, in the queue; allow labels to enable them earlier on a PR.
* Require a stable collector check that aggregates the results needed for merging.

The queue validates the combined state of the latest default branch, the PR, and PRs ahead of it.
Optional early checks let contributors investigate expensive-check failures before queueing again.
Labels only control PR checks; the corresponding checks always run in the queue.

### 1. Configure workflow triggers and optional checks

1. Identify the checks that should block a merge, including build, test, and any necessary expensive checks.
   A workflow running on PRs or merge groups does not by itself make its result mandatory.
2. Trigger validation workflows on `merge_group` with `checks_requested` in addition to the appropriate PR event.
   Check out and validate the merge-group revision, rather than the PR head, in queue runs.
3. For optional early checks, include `labeled` and `unlabeled` PR events so label changes update the checks.
   Select these jobs by PR label, but always select them for merge-group events.
4. Handle access to secrets explicitly.
   Labels do not replace any necessary environment approval for fork PRs.

For early QNX checks on fork PRs, use an execution path with explicit approval and access to the required secrets.
The shared Bazel workflow does not currently provide that path; see
[workflow context and fork support](#workflow-context-and-fork-support) for the available QNX workflow and its limitations.

### 2. Aggregate results in a collector check

We recommend a collector job, such as `PR mergeable`, as the required check.
The workflow lists the jobs it depends on and aggregates their results.
This keeps changes to the list of required jobs within the repository, without changing the organization configuration each time a job is added or renamed.

The collector needs to run even after dependencies fail or are skipped, reject failures and cancellations,
and accept skipped checks only when they are intentionally optional for that event.
A check omitted intentionally on PRs still needs to execute successfully in the queue before the collector passes there.

Report the required check under the same name on PRs and merge groups.
Do not skip an entire required workflow through event or path filters: its check can remain pending and block merging.
GitHub accepts conditionally skipped jobs as successful, so listing a check as required does not by itself ensure that it runs.
See [GitHub's guidance on skipped required checks](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks#handling-skipped-but-required-checks).

### 3. Require the queue and collector in branch protection

In [.eclipsefdn's Otterdog configuration](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet):

* Configure `required_merge_queue` for the repository's default branch.
* Add the collector to `required_status_checks` using its reported check name.
* Review existing legacy branch protections as well as rulesets.
  Prefer the queue over an additional strict up-to-date requirement: the queue already validates against the latest base branch.

A queue without required validation checks does not enforce build or test results.
Likewise, a collector that exists in a workflow but is absent from the required-check list does not block a merge.

### 4. Verify merge-blocking behavior

Before relying on the setup, verify that:

* A successful PR can enter the queue and merge after a successful queue run.
* Required failures and cancellations block merging.
* Optional PR checks are skipped as intended.
* Expensive checks run in the queue for fork PRs without labels.

GitHub's [merge queue documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)
describes the event and required-check configuration.

### 5. Document labels and failure recovery

Explain which labels enable early checks and how to recover from a failed queue run.
PR authors without permission to apply labels need a maintainer to set them.
After investigating a failure and testing a fix on the PR, queue the PR again for validation against the latest combined state.
Early PR checks do not replace this final queue run.

Maintainers remain responsible for ongoing CI maintenance and for repairing a broken default branch.
Merge queues reduce the risk of integration failures, but do not fix flaky SDK downloads or tests;
caching and reliability improvements remain separate work.

## Alternatives and trade-offs

The how-to above describes the recommended setup.
This chapter compares other choices: when expensive checks run, how contributors request early checks,
which workflow context executes them, and how merging is enforced.
These choices can be combined independently.

### When to run expensive checks

#### Optional early checks (recommended)

Run fast checks on PRs and again in the queue; always run expensive checks in the queue.
Allow contributors to investigate expensive-check failures before another queue run by requesting an early check.
This saves CI resources compared with running expensive checks on every PR update, but requires an explicit way to request them.
The how-to uses labels; manual dispatch is another option, described below.

#### Expensive checks on every PR

Run expensive checks on every PR and again in the queue, with manual approval where needed for access to secrets.
Examples include `baselibs`, `inc_ecu_model`, `logging`, and `tooling`.

This gives early feedback without labels, but uses more CI resources than the recommended setup and can require more manual approvals.
It can be preferable when the checks are affordable and their feedback is useful on most PR updates.

#### Early expensive checks on internal PRs

Run selected expensive checks on internal PRs and in the queue, but skip them on fork PRs.
Internal PRs use branches in the same repository; fork PRs use branches in a fork.
For example, `itf` and `qnx_unit_tests` run secret-dependent QNX checks on internal PRs after environment approval.

This avoids label handling, but fork contributors cannot request early checks to investigate a queue failure.
They need another queue run to test a fix for those checks.
It can suit repositories that accept later feedback on fork PRs.

#### Expensive checks only in the queue

Run fast checks on PRs and again in the queue, but defer selected expensive checks entirely to the queue.

This needs no label or PR-origin conditions, but every investigation of an expensive-check failure requires queue runs.
It can suit checks that rarely fail and for which maintaining an early-feedback path is not worthwhile.

### How to request early checks

#### PR labels (recommended)

Labels select optional checks within the PR workflow and keep their results alongside other PR checks.
PR authors without permission to apply labels need a maintainer to set them.
Labels do not themselves grant access to secrets or provide approval for executing fork code.

For examples of label-enabled checks, see [inc_someip_gateway's CI](https://github.com/eclipse-score/inc_someip_gateway/blob/main/.github/workflows/ci.yml)
(`test-cross` for cross-compilation) and its
[PR-target workflow](https://github.com/eclipse-score/inc_someip_gateway/blob/main/.github/workflows/ci_pull_request_target.yml)
(`test-qnx` for QNX builds).
`devcontainer` uses `test-consumer` for consumer tests.
Checks can also run automatically on internal PRs, with labels needed only for fork PRs, as in `communication`.


#### Manual dispatch

Offer a caller workflow with `workflow_dispatch` that invokes the shared Bazel workflow.
A maintainer can select an internal feature or release branch and start expensive checks when needed.
This avoids label conditions, but each early run requires someone with write access to start it.
See [GitHub's instructions for manual workflow runs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow).

The workflow must be available on the default branch for manual dispatch.
Selecting another branch runs that branch's workflow version and revision, so a release branch can retain its own CI configuration.
See [GitHub's dispatch event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch).

A dispatch run is a separate workflow run, rather than part of the PR workflow's collector.
Use it for early feedback; required queue checks must still validate the merge-group revision before merging.
Dispatch in a fork does not grant access to upstream secrets; supporting fork QNX checks still needs the execution path described below.

### Workflow context and fork support

Keep the workflow definition separate from the code revision it checks out.
With `pull_request_target`, GitHub uses the default-branch context even for PRs targeting a release branch.
Checking out the PR revision changes the build input, but does not select the release branch's workflow definition.
As a result, default-branch workflow changes can become incompatible with release-branch builds.
See [GitHub's event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_target).

Dispatch can select an internal branch's workflow definition as well as its code revision.
This makes it useful for release branches whose build setup has diverged from the default branch.
For a fork PR, an upstream dispatch needs an explicit way to select and check out the reviewed fork revision;
the branch selector alone does not provide that path.

The shared [QNX workflow](https://github.com/eclipse-score/cicd-workflows/blob/main/.github/workflows/qnx-build.yml)
provides an environment-approval job for fork PRs triggered through `pull_request_target`.
Its approval logic distinguishes those runs from internal PRs and merge-queue runs.
Approval must apply to the exact revision that is executed.

The shared [Bazel workflow](https://github.com/eclipse-score/cicd-workflows/blob/main/.github/workflows/bazel.yml)
leaves event and label selection to its caller, has no environment-approval job, and rejects `pull_request_target`.
It also has no repository or revision inputs for checking out fork code from an upstream dispatch.
Its QNX support therefore does not yet replace the gated QNX workflow for early secret-dependent checks on fork PRs.

### Merge strategy and required checks

#### Direct merges with an up-to-date requirement

Require the PR branch to be up to date with the base branch and require all necessary checks, including expensive checks, before merging.
This can provide the required validation without a queue.

Compared with the recommended setup, contributors repeatedly update their branches and rerun checks after other merges.
Maintainers coordinate merges and handle any required approvals for secret-dependent PR checks.
This can be a reasonable choice for a repository with few merges, where repeated updates are rare.

#### Direct merges without an up-to-date requirement

Merge PRs without requiring an up-to-date branch; any configured required checks still need to pass.
Repositories without required validation checks also fall into this configuration.
PR authors do not need to update their branch after other PRs merge, unless there are merge conflicts.

Compared with the recommended setup, this leaves the combined state unvalidated before merging.
Independently passing PRs can break the default branch when combined, leaving maintainers to investigate and repair it.
Choose this only if the repository deliberately accepts that integration risk.

#### Individual required checks instead of a collector

List each required check in `.eclipsefdn`, as done for `communication`.
This avoids collector logic and makes the required jobs explicit in the organization configuration.
However, adding or renaming a required check also needs a change there, rather than only in the repository workflow.
This is a reasonable alternative when the check list is small and stable, or an existing setup already works well.

Collector examples include `build/overall-result` in `devcontainer` and `ci/can_merge` in `inc_someip_gateway`.
Choosing a collector or individual checks is independent of the merge strategy and the timing of expensive checks.
In either arrangement, verify the configured required checks, including intentionally skipped jobs.

## Status quo

Configured default-branch setups as of 2026-11-15, covering 48 repositories with at least one non-bot commit
on their default branch in the preceding 30 days
([organization configuration](https://github.com/eclipse-score/.eclipsefdn/blob/a7ed6c57933c53fecf3c944c5ebcba16fb142d6c/otterdog/eclipse-score.jsonnet)):

| Configuration | Repositories |
| --- | --- |
| Queue with label-enabled early checks (recommended) | `communication`, `devcontainer`, `inc_someip_gateway` |
| Queue with expensive checks on every PR | `baselibs`, `inc_ecu_model`, `logging`, `time`, `tooling` |
| Queue with early expensive checks on internal PRs | `itf`, `qnx_unit_tests` |
| Queue with expensive checks only in the queue | None |
| Direct merges with an up-to-date requirement | `kyron`, `reference_integration` |
| Direct merges without an up-to-date requirement | `.github`, `bazel_cpp_toolchains`, `bazel_platforms`, `bazel_registry`, `bazel_registry_ui`, `cicd-actions`, `cicd-workflows`, `config_management`, `contributor_training`, `coverage_tool`, `dash-license-scan`, `dev_playground`, `docs-as-code`, `eclipse-score-website`, `eclipse-score-website-preview`, `inc_diagnostics`, `inc_security_crypto`, `infrastructure`, `mcp-servers`, `module_template`, `openssl`, `os_autosd`, `os_images`, `process_description`, `qnx_sdp`, `qnx_sdp_pkg`, `rules_imagefs`, `sbom-tool`, `score`, `score-crates`, `score_cpp_policies`, `score_rust_policies`, `testing_tools`, `tools` |
| Queue with expensive checks on every PR and an up-to-date requirement | `lifecycle` |
| Queue without required validation checks | `persistency` |

The repositories listed under either direct-merge setup or "Queue without required validation checks" have no required validation checks configured.
Enabling a queue or requiring an up-to-date branch does not by itself make build and test results mandatory.

Two additional gaps are worth noting:

* `lifecycle`'s required collector does not include its separate QNX jobs.
* `time` has a QNX queue collector in its workflow, but that collector is not listed as a required check.
