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
For other setups, [compare alternatives](merge_queue_alternatives.md).
To see existing combinations, [explore current repository setups](merge_queue_status_quo.md).

## How-to: Recommended setup

Use GitHub's native merge queue with optional label-enabled checks on PRs:

* Run fast checks on PRs and again in the queue.
* Run expensive checks, such as QNX builds, in the queue; allow labels to enable them earlier on a PR.
* Require a stable collector check that aggregates the results needed for merging.

The queue validates the combined state of the latest default branch, the PR, and PRs ahead of it.
Optional early checks let contributors investigate expensive-check failures before queueing again.
Labels only control PR checks; the corresponding checks always run in the queue.

## Setup checklist

* [Configure workflow triggers and optional checks](#merge-queue-workflows)
* [Aggregate results in a collector check](#merge-queue-collector)
* [Require the queue and collector in branch protection](#merge-queue-branch-protection)
* [Verify merge-blocking behavior](#merge-queue-verification)
* [Document labels and failure recovery](#merge-queue-contributor-workflow)

(merge-queue-workflows)=
## 1. Configure workflow triggers and optional checks

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
[workflow context and fork support](merge_queue_alternatives.md#workflow-context-and-fork-support) for the available QNX workflow and its limitations.

(merge-queue-collector)=
## 2. Aggregate results in a collector check

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

(merge-queue-branch-protection)=
## 3. Require the queue and collector in branch protection

In [.eclipsefdn's Otterdog configuration](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet):

* Configure `required_merge_queue` for the repository's default branch.
* Add the collector to `required_status_checks` using its reported check name.
* Review existing legacy branch protections as well as rulesets.
  Prefer the queue over an additional strict up-to-date requirement: the queue already validates against the latest base branch.

A queue without required validation checks does not enforce build or test results.
Likewise, a collector that exists in a workflow but is absent from the required-check list does not block a merge.

(merge-queue-verification)=
## 4. Verify merge-blocking behavior

Before relying on the setup, verify that:

* A successful PR can enter the queue and merge after a successful queue run.
* Required failures and cancellations block merging.
* Optional PR checks are skipped as intended.
* Expensive checks run in the queue for fork PRs without labels.

GitHub's [merge queue documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)
describes the event and required-check configuration.

(merge-queue-contributor-workflow)=
## 5. Document labels and failure recovery

Explain which labels enable early checks and how to recover from a failed queue run.
PR authors without permission to apply labels need a maintainer to set them.
After investigating a failure and testing a fix on the PR, queue the PR again for validation against the latest combined state.
Early PR checks do not replace this final queue run.

Maintainers remain responsible for ongoing CI maintenance and for repairing a broken default branch.
Merge queues reduce the risk of integration failures, but do not fix flaky SDK downloads or tests;
caching and reliability improvements remain separate work.

## Further reading

```{toctree}
:maxdepth: 1

Compare alternatives <merge_queue_alternatives>
Explore current repository setups <merge_queue_status_quo>
```
