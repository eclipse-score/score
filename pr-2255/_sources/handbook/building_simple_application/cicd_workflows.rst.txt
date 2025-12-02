..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

.. toctree::
   :maxdepth: 1
   :glob:

After successfully building the scrample binary, we need to ensure, that future changes do not breakt the build. 

To achieve this, we create a CI/CD workflow that triggers a `GitHub action <https://docs.github.com/en/actions>`_
to build the scrample application whenever a new PR is opened.

To achieve this, first create a workflow file named `build.yml <https://github.com/eclipse-score/scrample/blob/main/.github/workflows/build.yml>`_
in the .github folder.

Then fill the workflow file with the following content:

.. code-block::
    :linenos:
    :emphasize-lines: 2, 8, 11, 15, 21, 26, 28

    name: Scrample Build
    on:
        pull_request:
            types: [opened, reopened, synchronize]
        merge_group:
            types: [checks_requested]
    jobs:
        build_target:
            runs-on: ubuntu-latest
            steps:
            - name: Checkout repository
                uses: actions/checkout@v4.2.2
            - name: Setup Bazel
                uses: bazel-contrib/setup-bazel@0.9.1
            - name: Setup QNX License
                env:
                SCORE_QNX_LICENSE: ${{ secrets.SCORE_QNX_LICENSE }}
                run: |
                mkdir -p /opt/score_qnx/license
                echo "${SCORE_QNX_LICENSE}" | base64 --decode > /opt/score_qnx/license/licenses
            - name: Bazel build scrample with qnx toolchain
                env:
                SCORE_QNX_USER: ${{ secrets.SCORE_QNX_USER }}
                SCORE_QNX_PASSWORD: ${{ secrets.SCORE_QNX_PASSWORD }}
                run: |
                bazel build --config x86_64-qnx --credential_helper=*.qnx.com=${{ github.workspace }}/.github/tools/qnx_credential_helper.py -- \
                //src:scrample
            - name: Cleanup QNX License
                if: always()
                run: rm -rf /opt/score_qnx


First, as shown in line 2 we define when the workflow should run.
In this case, it is triggered whenever a PR is opened, created or synchronized.

Next, we specify the job to be executed. For now, there is a single job that builds the scrample application, as shown in the line 8.
Finally, we need to define the steps of the build job:

- Line 11: checkout the repository.
- Line 13: set up bazel.
- Line 15: set up the QNX license using the CI secrets stored in the CI infrastructure.
- Line 21: uild the scrample binary using the same bazel command executed locally.
- Line 28: clean-up temporary QNX files from the remote build machine.

Once the workflow is merged into the repository, every new PR we will automatically trigger the build and its result in the
`Actions sections <https://github.com/eclipse-score/reference_integration/actions>`_.