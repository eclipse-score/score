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

The [recommended setup](merge_queues.md) combines the choices below.
Use this page to compare their trade-offs; the [status quo](merge_queue_status_quo.md) shows existing repository configurations.
Each row describes a feature of a setup, not a separate, mutually exclusive configuration.

| Feature | Recommendation | Other choices |
| --- | --- | --- |
| Merge queue | Enabled | Direct merges |
| Up-to-date requirement | No additional requirement | Require an up-to-date PR branch |
| Early expensive checks | On demand via PR labels | Automatic on all or internal PRs, manual dispatch, or no early checks |
| Required validation checks | Collector | Individual required checks |

Early checks can use different policies for different jobs and PR origins.
For example, `communication` combines automatic internal checks, label-enabled fork checks, and individual required checks.
`lifecycle` combines a queue with an up-to-date requirement.
Not every combination currently supports fork code with secrets; see [workflow context and fork support](#workflow-context-and-fork-support).
Missing required validation checks are a gap in enforcement, regardless of the other choices.

## Merge queue

Use a merge queue to validate the combined state before merging, as described in the [how-to](merge_queues.md).
Direct merges avoid queue configuration, but need another way to validate integration with other changes,
or leave maintainers to repair failures after merging.
The up-to-date requirement below determines this trade-off for direct merges.

## Up-to-date requirement

### Require an up-to-date PR branch

Require the PR branch to be up to date with the base branch and require all necessary checks, including expensive checks, before merging.
This can provide the required validation without a queue.

Compared with the recommended setup, contributors repeatedly update their branches and rerun checks after other merges.
Maintainers coordinate merges and handle any required approvals for secret-dependent PR checks.
This can be a reasonable choice for a repository with few merges, where repeated updates are rare.

### No additional up-to-date requirement (recommended with a queue)

With a queue, omit an additional up-to-date requirement: the queue validates the combined state.
Without a queue, PRs can merge without updating their branch after other merges, unless there are conflicts;
any configured required checks still need to pass.

Without either a queue or an up-to-date requirement, the combined state is not validated before merging.
Independently passing PRs can break the default branch when combined, leaving maintainers to investigate and repair it.
For direct merges, choose this only if the repository deliberately accepts that integration risk.

## Early expensive checks

The following timing choices assume a merge queue.
Choose when selected expensive checks run before the queue and, for on-demand checks, how they are requested.
All required expensive checks still need to run in the queue.

### Optional early checks (recommended)

Run fast checks on PRs and again in the queue; always run expensive checks in the queue.
Allow contributors to investigate expensive-check failures before another queue run by requesting an early check.
This saves CI resources compared with running expensive checks on every PR update, but requires an explicit way to request them.
The how-to uses labels; manual dispatch is another option, described below.

### Expensive checks on every PR

Run expensive checks on every PR and again in the queue, with manual approval where needed for access to secrets.
Examples include `baselibs`, `inc_ecu_model`, `logging`, and `tooling`.

This gives early feedback without labels, but uses more CI resources than the recommended setup and can require more manual approvals.
It can be preferable when the checks are affordable and their feedback is useful on most PR updates.

### Early expensive checks on internal PRs

Run selected expensive checks on internal PRs and in the queue, but skip them on fork PRs.
Internal PRs use branches in the same repository; fork PRs use branches in a fork.
For example, `itf` and `qnx_unit_tests` run secret-dependent QNX checks on internal PRs after environment approval.

This avoids label handling, but fork contributors cannot request early checks to investigate a queue failure.
They need another queue run to test a fix for those checks.
It can suit repositories that accept later feedback on fork PRs.

### Expensive checks only in the queue

Run fast checks on PRs and again in the queue, but defer selected expensive checks entirely to the queue.

This needs no label or PR-origin conditions, but every investigation of an expensive-check failure requires queue runs.
It can suit checks that rarely fail and for which maintaining an early-feedback path is not worthwhile.

### Request early checks with PR labels (recommended)

Labels select optional checks within the PR workflow and keep their results alongside other PR checks.
PR authors without permission to apply labels need a maintainer to set them.
Labels do not themselves grant access to secrets or provide approval for executing fork code.

For examples of label-enabled checks, see [inc_someip_gateway's CI](https://github.com/eclipse-score/inc_someip_gateway/blob/main/.github/workflows/ci.yml)
(`test-cross` for cross-compilation) and its
[PR-target workflow](https://github.com/eclipse-score/inc_someip_gateway/blob/main/.github/workflows/ci_pull_request_target.yml)
(`test-qnx` for QNX builds).
`devcontainer` uses `test-consumer` for consumer tests.
Checks can also run automatically on internal PRs, with labels needed only for fork PRs, as in `communication`.

### Request early checks with manual dispatch

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

## Required validation checks

Require either a collector or individual checks to enforce validation results.
Enabling a queue or an up-to-date requirement does not make checks mandatory by itself.

### Individual required checks instead of a collector

List each required check in `.eclipsefdn`, as done for `communication`.
This avoids collector logic and makes the required jobs explicit in the organization configuration.
However, adding or renaming a required check also needs a change there, rather than only in the repository workflow.
This is a reasonable alternative when the check list is small and stable, or an existing setup already works well.

Collector examples include `build/overall-result` in `devcontainer` and `ci/can_merge` in `inc_someip_gateway`.
Choosing a collector or individual checks is independent of the merge strategy and the timing of expensive checks.
In either arrangement, verify the configured required checks, including intentionally skipped jobs.
