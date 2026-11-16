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

Use this guide to configure automatic checks before merging changes.
This guidance is optional. Maintainers can choose another configuration for their repository.

* To choose a different setup, [compare alternatives](merge_queue_alternatives.md).
* To inspect existing setups, see the [repository status quo](merge_queue_status_quo.md).

## Recommended setup

Use GitHub's native merge queue, with labels to request early expensive checks:

| Checks | On a PR | In the merge queue |
| --- | --- | --- |
| Fast checks | Run automatically | Always run |
| Expensive checks, such as QNX builds | Run when enabled by a label | Always run |

Require a stable collector check that aggregates the results needed for merging.

The queue validates the combined state of the latest default branch, the PR, and PRs ahead of it.
Optional early checks let contributors investigate expensive-check failures before queueing again.
Labels only control PR checks; the corresponding checks always run in the queue.

## Setup checklist

1. [Configure workflow triggers and optional checks](#configure-workflow-triggers-and-optional-checks)
2. [Aggregate results in a collector check](#aggregate-results-in-a-collector-check)
3. [Require the queue and collector in branch protection](#require-the-queue-and-collector-in-branch-protection)
4. [Verify merge-blocking behavior](#verify-merge-blocking-behavior)
5. [Document labels and failure recovery](#document-labels-and-failure-recovery)

## Configure workflow triggers and optional checks

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

## Aggregate results in a collector check

We recommend a collector job, such as `PR mergeable`, as the required check.
Make the collector depend on every job needed for merging and evaluate their results.
Keep this dependency list in the repository workflow, so adding or renaming a job does not also require an organization-configuration change.

Configure the collector to:

* Run even when dependencies fail or are skipped.
* Reject failures and cancellations.
* Accept skipped jobs only when they are intentionally optional for that event.
* Require expensive checks to run successfully in the queue, even when they were optional on the PR.

Report the required check under the same name on PRs and merge groups.
Two kinds of skipping need particular care:

* **Workflow filters:** event or path filters can skip an entire required workflow, leaving its check pending and blocking a merge.
* **Job conditions:** GitHub treats conditionally skipped jobs as successful. Listing a job as required does not ensure that it runs; account for intentional skips in the collector.

See [GitHub's guidance on skipped required checks](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks#handling-skipped-but-required-checks).

## Require the queue and collector in branch protection

In [.eclipsefdn's Otterdog configuration](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet):

* Configure `required_merge_queue` for the repository's default branch.
* Add the collector to `required_status_checks` using its reported check name.
* Review existing legacy branch protections as well as rulesets.
  Prefer the queue over an additional strict up-to-date requirement: the queue already validates against the latest base branch.

A queue without required validation checks does not enforce build or test results.
Likewise, a collector that exists in a workflow but is absent from the required-check list does not block a merge.

## Verify merge-blocking behavior

Before relying on the setup, verify that:

* A successful PR can enter the queue and merge after a successful queue run.
* Required failures and cancellations block merging.
* Optional PR checks are skipped as intended.
* Expensive checks run in the queue for fork PRs without labels.

GitHub's [merge queue documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)
describes the event and required-check configuration.

## Document labels and failure recovery

Document the two actions PR authors need:

* **Request early checks:** list the available labels and explain how to ask a maintainer to apply them when the author lacks permission.
* **Recover from a queue failure:** investigate the failure, test the fix on the PR, and queue the PR again to validate the latest combined state.

Early PR checks do not replace the final queue run.

Maintainers remain responsible for ongoing CI maintenance and for repairing a broken default branch.
Merge queues reduce the risk of integration failures, but do not fix flaky SDK downloads or tests;
caching and reliability improvements remain separate work.

## Further reading

```{toctree}
:maxdepth: 1

Compare alternatives <merge_queue_alternatives>
Explore current repository setups <merge_queue_status_quo>
```
