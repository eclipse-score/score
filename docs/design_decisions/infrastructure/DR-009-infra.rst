..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-009-Infra: Alternatives for implementing a merge queue
=========================================================

- **Date:** 2026-09-22

.. dec_rec:: Alternatives for implementing a merge queue
   :id: dec_rec__infra__merge_queue
   :status: accepted
   :version: 1
   :context: Infrastructure
   :decision: GitHub native merge queue

Context / Problem
-----------------

The main branch must always work and remain in a stable, validated state.
This requires running expensive checks, which are either currently not implemented or skipped at pull requests.
Now the situation became unbearable with main breaking occasionally due to uncoordinated and not well tested merges.

We need a way to keep main or the default branch both green and up to date while allowing a high throughput of small, independent PRs.
The solution should be easy to operate, compatible with the repository's existing branch protection rules, and should not impose a custom maintenance burden on contributors.

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

- Keep the default branch in a stable and validated state.
- Re-run required checks against the latest base branch state before merge.
- Preserve human review and required status checks.
- Keep the workflow understandable for contributors and maintainers.
- Minimise operational and maintenance effort.

Non-Goals
~~~~~~~~~

- Replacing GitHub pull requests as the review workflow.
- Changing the content review policy or required reviewers.
- Introducing a bespoke scheduling system for every repository.
- Removing the need for branch protection or required checks.

Options Considered
------------------

Option A: No merge queue; keep merging manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Continue to merge pull requests directly into the default branch using the existing branch protection and CI rules.
This is the current baseline.

In practice, this means that:

* each PR is validated only at the time it is first checked,
* maintainers must manually coordinate merges,
* the default branch may be temporarily unstable during bursts of merges,
* workflows accessing secrets always need manual approval for pull requests from forks,
* contributors must re-trigger checks repeatedly when their branch becomes stale.

Effort 💚: No new implementation effort.

Safety 😡: Weakest option because it does not prevent a stale branch from merging and does not guarantee final-state validation.

UX 😡: Contributors repeatedly have to rebase and re-run validation.

Maintainability 💚: Very simple, but with high operational friction.

Option B: Use the GitHub native merge queue with labels to enable expensive checks in pull requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use GitHub's built-in merge queue feature together with protected branch rules.
The queue works by temporarily placing PRs in a queue for the default branch and then validating the combined branch state before merging.

All workflows executed in the pull request are also run in the merge queue.
In addition to these, expensive workflows are executed in the merge queue to ensure the final state of the combined branch is validated before merging.

The expensive workflows can be selectively enabled using labels on the pull request.
This is useful if in a previous merge queue run an expensive workflow failed and needs to be re-run without re-triggering all the standard checks.

The key benefits are:

* automatic handling of rebasing onto the latest target branch,
* validation of the exact commit that would land in the branch,
* queue ordering that avoids the most common stale-PR problems,
* workflows accessing secrets do not require manual approval in the merge queue (content has been reviewed when entering the merge queue),
* expensive workflows can be selectively enabled using labels on the pull request.

This option works especially well for repositories where branch protection is already enforced and where jobs are mostly standard GitHub Actions workloads.

Because some checks are performed twice (pull request, merge queue) it is important to keep them fast and reliable.

Effort 💚: Low.

Safety 💚: Strong because every queued PR is checked against the latest branch state before merge.

UX 💚: Pull requests process is largely unchanged.

Maintainability 💚: Excellent; no custom service or bot to maintain.

Evaluation
----------

.. csv-table::
   :header: Criteria, Option A, Option B
   :widths: 15, 10, 10

   Safety, 😡, 💚
   Effort, 💚, 💚
   UX, 😡, 💚
   Maintainability, 💚, 💚

Decision
--------

We choose Option B: use the GitHub native merge queue and labels.

This is the best fit for the repository and project workflow because it is operationally lightweight,
keeps the default branch in a validated state, and aligns with standard GitHub branch protection and CI tooling.

We will keep the policy simple:

* protect the default branch with required status checks,
* enable merge queue for the relevant repositories,
* document the contributor workflow in the contributor guide,
* treat the queue as a tool to reduce merge churn, not as a replacement for review.

This gives us fast integration without creating another infrastructure component that would require ongoing support.
