<!-- ----------------------------------------------------------------------------
  Copyright (c) 2026 Contributors to the Eclipse Foundation

  See the NOTICE file(s) distributed with this work for additional
  information regarding copyright ownership.

  This program and the accompanying materials are made available under the
  terms of the Apache License Version 2.0 which is available at
  https://www.apache.org/licenses/LICENSE-2.0

  SPDX-License-Identifier: Apache-2.0
----------------------------------------------------------------------------- -->

# Merge queue alternatives and trade-offs

Use this page to choose a configuration for your repository.
For setup instructions, follow the [how-to](merge_queues.md); for existing configurations, see the [status quo](merge_queue_status_quo.md).

## Decisions at a glance

Each row is one decision. A repository combines choices across rows, and individual jobs can use different early-check policies.

| Feature | Recommendation | Other choices |
| --- | --- | --- |
| Merge queue | Enabled | Direct merges |
| Up-to-date requirement | No additional requirement | Require an up-to-date PR branch |
| Early expensive checks | On demand via PR labels | Automatic on all or internal PRs, manual dispatch, or no early checks |
| Required validation checks | Collector | Individual required checks |

For example:

* `communication` runs selected checks automatically on internal PRs, enables them by label for fork PRs, and requires individual checks.
* `lifecycle` uses both a queue and an up-to-date requirement.

Missing required validation checks leave a gap in enforcement regardless of these choices.
For combinations involving fork code and secrets, also check [workflow context and fork support](#workflow-context-and-fork-support).

## Merge queue

**Recommended: use a queue.** It validates the combined state before merging, as described in the [how-to](merge_queues.md).

**Alternative: merge directly.** This avoids queue configuration, but integration still needs validation.
An up-to-date requirement can provide it; without either mechanism, maintainers may need to repair failures after merging.

## Up-to-date requirement

### With a queue: omit the additional requirement (recommended)

The queue already validates changes against the latest base branch.
Prefer the queue over an additional up-to-date requirement.
Review legacy protections as well as rulesets when configuring it.

### Without a queue: require an up-to-date PR branch

Require an up-to-date PR branch and all necessary checks, including expensive checks, before merging.
This can provide integration validation without a queue.

The cost is repeated work: after other PRs merge, contributors update their branches and rerun checks.
Maintainers coordinate merges and handle any approvals needed for secret-dependent PR checks.
This can suit repositories with few merges, where repeated updates are rare.

### Without either mechanism: accept the integration risk

Without a queue or an up-to-date requirement, authors need to update their branches only to resolve conflicts.
Any configured required checks still need to pass, but the latest combined state is not validated before merging.
Independently passing PRs can therefore break the default branch when combined.
Choose this only if the repository accepts that maintainers may need to investigate and repair those failures.

## Early expensive checks

The timing choices below assume a merge queue: fast checks run on PRs and again in the queue,
and all required expensive checks run in the queue.
Choose a policy for each expensive check, then choose how to request any optional early runs.

### Choose when checks run

| Early-check policy | Benefit | Trade-off |
| --- | --- | --- |
| **On demand (recommended)** | Contributors can investigate expensive-check failures before another queue run; fewer runs than checking every PR update. | Needs an explicit request through labels or dispatch. |
| **Every PR** | Early feedback on every update, without label handling. | More CI usage and potentially more approvals for access to secrets. Best suited to affordable checks whose feedback is usually useful. |
| **Internal PRs only** | No label handling for checks restricted to same-repository branches. | Fork contributors must use queue runs to investigate failures and test fixes. |
| **Queue only** | No early-run request or PR-origin conditions to maintain. | Every investigation needs queue runs. Best suited to checks that rarely fail. |

Internal PRs use branches in the same repository; fork PRs use branches in a fork.
Examples of automatic checks include `baselibs`, `inc_ecu_model`, `logging`, and `tooling` on all PRs,
and secret-dependent QNX checks in `itf` and `qnx_unit_tests` on internal PRs after environment approval.
For checks on all PRs, provide manual approval wherever access to secrets requires it.

### Choose how to request optional checks

#### PR labels (recommended)

Labels select optional checks within the PR workflow and keep their results alongside other PR checks.
PR authors without permission to apply labels need a maintainer to set them.
Labels do not themselves grant access to secrets or provide approval for executing fork code.

Examples:

* `inc_someip_gateway` uses `test-cross` for cross-compilation in its [CI workflow](https://github.com/eclipse-score/inc_someip_gateway/blob/main/.github/workflows/ci.yml) and `test-qnx` for QNX builds in its [PR-target workflow](https://github.com/eclipse-score/inc_someip_gateway/blob/main/.github/workflows/ci_pull_request_target.yml).
* `devcontainer` uses `test-consumer` for consumer tests.
* `communication` runs selected checks automatically on internal PRs and uses labels for fork PRs.

#### Manual dispatch

Offer a caller workflow with `workflow_dispatch` that invokes the shared Bazel workflow.
A maintainer can select an internal feature or release branch and start expensive checks when needed.
This avoids label conditions, but each early run requires someone with write access to start it.
See [GitHub's instructions for manual workflow runs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow).

The caller workflow must be available on the default branch for manual dispatch.
For how branch selection affects release builds, see [workflow context and fork support](#workflow-context-and-fork-support)
and [GitHub's dispatch event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch).

A dispatch run is a separate workflow run, rather than part of the PR workflow's collector.
Use it for early feedback; required queue checks must still validate the merge-group revision before merging.
Dispatch in a fork does not grant access to upstream secrets; supporting fork QNX checks still needs the execution path described below.

### Workflow context and fork support

Distinguish the **workflow definition** from the **code revision it checks out**:

| Trigger | Workflow context | Consequence for release branches |
| --- | --- | --- |
| `pull_request_target` | Default branch, even for PRs targeting a release branch. | Checking out release-branch or PR code does not select its workflow definition; default-branch workflow changes can become incompatible with that code. |
| `workflow_dispatch` | The selected internal branch's workflow version and revision. | A release branch can retain its own build setup after diverging from the default branch. |

See GitHub's references for [PR-target events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_target)
and [dispatch events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch).

For a fork PR, an upstream dispatch needs an explicit way to select and check out the reviewed fork revision.
The branch selector alone does not provide that path, and dispatch in a fork does not grant upstream secrets.
Approval must apply to the exact revision that is executed.

The shared workflows currently differ:

* [QNX workflow](https://github.com/eclipse-score/cicd-workflows/blob/main/.github/workflows/qnx-build.yml): provides an environment-approval job for fork PRs triggered through `pull_request_target`, distinguishing them from internal PRs and merge-queue runs.
* [Bazel workflow](https://github.com/eclipse-score/cicd-workflows/blob/main/.github/workflows/bazel.yml): leaves event and label selection to the caller, has no environment-approval job, and rejects `pull_request_target`. It also has no repository or revision inputs for an upstream dispatch to check out fork code.

The shared Bazel workflow therefore does not yet replace the gated QNX workflow for early secret-dependent checks on fork PRs.

## Required validation checks

Require either a collector or individual checks to enforce validation results.
Enabling a queue or an up-to-date requirement does not make checks mandatory by itself.

| Mechanism | Where required jobs are listed | Trade-off |
| --- | --- | --- |
| **Collector (recommended)** | The workflow lists its dependencies; `.eclipsefdn` requires the stable collector name. | Jobs can be added or renamed within the repository, but the collector needs to handle failures and intentional skips correctly. |
| **Individual checks** | `.eclipsefdn` lists each required check. | No collector logic, and the organization configuration names the checks explicitly; adding or renaming one also requires a change there. |

Individual checks can suit a small, stable check list or an existing setup that works well, as in `communication`.
Collector examples include `build/overall-result` in `devcontainer` and `ci/can_merge` in `inc_someip_gateway`.

Either mechanism can be combined with any merge strategy or early-check policy.
Verify that the configured required checks cover the intended jobs and handle intentional skips correctly.
