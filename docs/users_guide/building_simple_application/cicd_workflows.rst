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

After building and testing the module locally, we need to ensure that future changes do not break it.
In Eclipse S-CORE, this is done by `GitHub Actions <https://docs.github.com/en/actions>`_ workflows which run on every
pull request. Instead of implementing the workflow logic in every repository, most workflows call the reusable workflows
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
     - Runs the pre-commit checks on every pull request, e.g. whitespace, copyright and REUSE headers,
       YAML formatting and the Bazel lockfile
   * - ``on-pr_target.yml``
     - Runs the license check with the Eclipse Dash license tool
   * - ``docs.yml`` / ``docs-publish.yml``
     - Builds the documentation and publishes it to GitHub Pages
   * - ``on-daily.yml``
     - Daily maintenance, e.g. cleanup of outdated documentation previews
   * - ``sync-template.yml``
     - Opens a pull request with the changes of the template once a month,
       see :doc:`first_score_module`

The documentation workflow shows the typical pattern: a short workflow file in the module repository which calls a
reusable workflow, pinned to a commit of ``cicd-workflows``:

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 2, 16, 23

    name: Documentation CI
    on:
      pull_request:
      push:
        branches:
          - main
        tags:
          - "v*"
      release:
        types: [published]
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
          retention-days: 3

- Line 2 defines when the workflow runs: for every pull request, for changes on ``main``, for release tags and
  published releases, and in the merge queue.
- Line 16 calls the reusable workflow. Pin it to a commit (and note the version in a comment), so that changes in
  ``cicd-workflows`` do not unexpectedly change your pipeline.
- Line 23 passes the Bazel command that the reusable workflow executes, here the documentation build from the
  :doc:`documentation generation <doc_generation>` chapter.

Build and test workflow
^^^^^^^^^^^^^^^^^^^^^^^
The template does not contain a workflow which builds and tests the code yet. Add one for the supported platforms,
e.g. ``.github/workflows/build.yml``.
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
- Line 23: the build configuration from the :doc:`build and test <building_source_code>` chapter.
- Line 24: the QNX job runs in the GitHub environment ``workflow-approval``. It is created for every module repository
  and requires the approval of an S-CORE committer before the job gets access to the QNX secrets.
- Line 25: the QNX license and credentials are provided as organization secrets by the CI infrastructure.
  The QNX job also expects the credential helper script ``.github/tools/qnx_credential_helper.py``, which is not part
  of the template; copy it e.g. from the `persistency <https://github.com/eclipse-score/persistency/tree/main/.github/tools>`_
  repository or pass another path with the input ``credential-helper``.

Once the workflow is merged into the repository, every new pull request automatically triggers the build,
and its result is shown in the *Actions* tab of your repository and in the checks of the pull request.
The reusable workflows provide further checks, e.g. static code analysis, coverage and CodeQL scans;
they are listed in the `cicd-workflows README <https://github.com/eclipse-score/cicd-workflows>`_.

If the documentation workflow should show the test results, as described in
:doc:`documentation generation <doc_generation>`, the tests have to run in the same workflow before the
documentation build. The template's documentation workflow only builds the documentation, so its published
documentation shows the links from requirements to code, but no test results.

Next steps
----------
Once your module is released, it can be integrated into the S-CORE platform. How module versions get into the
reference integration and into an S-CORE release is described in the :ref:`integration process <integration_process>`.
