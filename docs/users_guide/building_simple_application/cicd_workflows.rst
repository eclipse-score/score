..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

CI/CD Workflows
================

After successfully building the binaries, we need to ensure that future changes do not break the build.
In Eclipse S-CORE, this is done by `GitHub Actions <https://docs.github.com/en/actions>`_ workflows which run on every
pull request. Instead of implementing the workflow logic in every repository, the workflows call the reusable workflows
from `eclipse-score/cicd-workflows <https://github.com/eclipse-score/cicd-workflows>`_.

Workflows of a module repository
--------------------------------
The `module template <https://github.com/eclipse-score/module_template/tree/main/.github/workflows>`_ already contains
the basic workflows:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Workflow
     - Purpose
   * - ``on-pr.yml``
     - Runs the pre-commit checks, e.g. formatting, on every pull request
   * - ``on-pr_target.yml``
     - Runs the license check with the Eclipse Dash license tool
   * - ``docs.yml`` / ``docs-publish.yml``
     - Builds the documentation and publishes it to GitHub Pages
   * - ``on-daily.yml``
     - Daily maintenance, e.g. cleanup of outdated documentation previews
   * - ``sync-template.yml``
     - Keeps the repository in sync with later changes of the template

The documentation workflow shows the typical pattern: a short workflow file in the module repository which calls a
reusable workflow, pinned to a commit of ``cicd-workflows``:

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 2, 14, 21

    name: Documentation CI
    on:
      pull_request:
      push:
        branches:
          - main
        tags:
          - "v*"
      merge_group:
        types: [checks_requested]

    jobs:
      build-docs:
        uses: eclipse-score/cicd-workflows/.github/workflows/docs.yml@8d80e8df150cae21d53cbc8031d0f970648f7a67 # v0.0.3
        permissions:
          contents: write
          pages: write
          pull-requests: write
          id-token: write
        with:
          bazel-target: "--lockfile_mode=error //:docs -- --github_user=${{ github.repository_owner }} --github_repo=${{ github.event.repository.name }}"

- Line 2 defines when the workflow runs: for every pull request, for changes on ``main``, for release tags and in the merge queue.
- Line 14 calls the reusable workflow. Pin it to a commit (and note the version in a comment), so that changes in
  ``cicd-workflows`` do not unexpectedly change your pipeline.
- Line 21 passes the Bazel command that the reusable workflow executes, here the documentation build from the
  :doc:`documentation generation <doc_generation>` chapter.

Build and test workflow
^^^^^^^^^^^^^^^^^^^^^^^
Add a workflow which builds and tests your code for the supported platforms, e.g. ``.github/workflows/build.yml``.
The reusable workflows ``tests.yml`` and ``qnx-build.yml`` take care of the Bazel setup, the caches and,
for QNX, the license handling:

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 8, 14, 16, 23, 24, 25

    name: Build & Test
    on:
      pull_request:
        types: [opened, reopened, synchronize]
      merge_group:
        types: [checks_requested]
    jobs:
      linux:
        uses: eclipse-score/cicd-workflows/.github/workflows/tests.yml@8d80e8df150cae21d53cbc8031d0f970648f7a67 # v0.0.3
        permissions:
          contents: read
          pull-requests: read
        with:
          bazel-target: "test --config=score-linux-x86_64 //score/..."

      qnx:
        uses: eclipse-score/cicd-workflows/.github/workflows/qnx-build.yml@8d80e8df150cae21d53cbc8031d0f970648f7a67 # v0.0.3
        permissions:
          contents: read
          pull-requests: read
        with:
          bazel-target: "//score/..."
          bazel-config: "score-qnx-x86_64"
          environment-name: "workflow-approval"
        secrets:
          score-qnx-license: ${{ secrets.SCORE_QNX_LICENSE }}
          score-qnx-user: ${{ secrets.SCORE_QNX_USER }}
          score-qnx-password: ${{ secrets.SCORE_QNX_PASSWORD }}

- Lines 8 and 14: the job ``linux`` builds and runs all tests for Linux x86_64 with the same Bazel command you use locally.
- Line 16: the job ``qnx`` cross-compiles the code with the QNX toolchain.
- Line 23: the build configuration from the :doc:`building source code <building_source_code>` chapter.
- Line 24: the QNX job uses secrets, which are gated by the GitHub environment ``workflow-approval``,
  e.g. for pull requests from forks.
- Line 25: the QNX license and credentials are provided as organization secrets by the CI infrastructure.

Once the workflow is merged into the repository, every new pull request automatically triggers the build,
and its result is shown in the *Actions* tab of your repository and in the checks of the pull request.
The reusable workflows provide further checks, e.g. static code analysis, coverage and CodeQL scans;
they are listed in the `cicd-workflows README <https://github.com/eclipse-score/cicd-workflows>`_.

Workflows of the reference integration
--------------------------------------
The running example is part of the reference integration, so it is checked by the workflows of that repository
on every pull request:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Workflow
     - What it checks for the example
   * - `build_and_test_linux.yml <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/build_and_test_linux.yml>`_,
       ``build_and_test_qnx.yml``, ``build_and_test_autosd.yml``, ``build_and_test_ebclfsa.yml``
     - Service and consumer build for every target platform and are packaged into the reference images
   * - `test_and_docs.yml <https://github.com/eclipse-score/reference_integration/blob/main/.github/workflows/test_and_docs.yml>`_
     - Runs the platform integration tests (``bazel test --config=linux-x86_64 //platform_integration_tests:pit``),
       incl. ``test_platform_version`` which starts the *Platform Version Check* on the Linux image,
       and builds the documentation with the test results
   * - ``build_and_test_linux_target.yml``
     - Unpacks the release archives (platform and showcases) into plain Ubuntu and Debian containers
       and runs all showcases there
   * - ``known_good_correct.yml``, ``bzlmod-lock.yml``
     - Check that ``known_good.json``, the generated Bazel files and the lockfile are consistent

How the example gets into the reference images and how its test is defined is shown in the next chapter.
