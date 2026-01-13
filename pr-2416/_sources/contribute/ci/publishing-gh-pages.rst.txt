..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

Pushing to GitHub Pages from a Forked Pull Request
===================================================

Introduction
------------

When working with GitHub Pages in repositories where contributors submit changes via forks,
special considerations must be taken due to security restrictions imposed by GitHub Actions.
This document covers how to safely publish content to GitHub Pages from a pull request originating
from a fork, based on previous research and trial runs on dummy repositories.

Why Use ``pull_request_target`` Instead of ``pull_request``?
------------------------------------------------------------

By default, GitHub Actions run with minimal permissions when triggered by a ``pull_request`` event
from a fork. This means that workflows cannot access repository secrets, preventing them from
deploying changes to GitHub Pages.

To overcome this, we can use ``pull_request_target`` instead of ``pull_request``.
The ``pull_request_target`` event runs workflows in the context of the base repository rather than
the fork, allowing access to repository secrets. However, since this introduces potential security
risks (such as arbitrary code execution with write access), additional safeguards must be implemented.

Implementing Security Measures
------------------------------

To safely allow a workflow to push to GitHub Pages, the following measures should be taken:

Require Maintainer Approval Before Running Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To prevent unauthorized code execution, an environment with required approvals is being used.
This ensures that workflows triggered by ``pull_request_target`` do not automatically execute until
approved by a maintainer.


.. code-block:: yaml

   jobs:
     deploy:
       runs-on: ubuntu-latest
       environment: github-pages
       steps:
         - name: Checkout repository (Handle all events)
           uses: actions/checkout@v4.2.2
           with:
             ref: ${{ github.head_ref || github.event.pull_request.head.ref || github.ref }}
             repository: ${{ github.event.pull_request.head.repo.full_name || github.repository }}

With this setup, GitHub will pause execution of the workflow until a maintainer approves it.

**This method is disabled at the moment.**


Handling ``pull_request_target`` Workflow Adaptations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since ``pull_request_target`` runs workflows in the context of the base repository rather than the
source fork, special considerations must be taken when checking out the repository. The following
checkout step ensures that the workflow correctly fetches the pull request source:

.. code-block:: yaml

   - name: Checkout repository (Handle all events)
     uses: actions/checkout@v4.2.2
     with:
       ref: ${{ github.head_ref || github.event.pull_request.head.ref || github.ref }}
       repository: ${{ github.event.pull_request.head.repo.full_name || github.repository }}

When checking out code in GitHub Actions, special considerations must be taken to ensure that the
correct branch and repository are selected, depending on the event type. Below are the rules for
safely handling checkouts.

Checking Out the Correct Branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table outlines how branches are checked out based on different event types:

.. list-table:: Branch Checkout Rules
   :header-rows: 1

   * - Condition
     - Event Type
     - Checked Out Branch
   * - ``github.head_ref``
     - ``pull_request_target``
     - PR branch (source branch)
   * - ``github.event.pull_request.head.ref``
     - ``pull_request``
     - PR branch (source branch)
   * - ``github.ref``
     - ``push, merge_group``
     - The branch being pushed/merged

Checking Out the Correct Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table describes how repositories are selected for checkout:

.. list-table:: Repository Checkout Rules
   :header-rows: 1

   * - Condition
     - Event Type
     - Checked Out Repository
   * - ``github.event.pull_request.head.repo.full_name``
     - ``pull_request``
     - Forked repository (if PR is from a fork)
   * - ``github.repository``
     - ``push, merge_group``
     - Default repository (same repo PRs, merges, pushes)


Conclusion
----------

By implementing these best practices, we can safely enable contributors to publish changes to
GitHub Pages while maintaining security within our ``score`` repository.
