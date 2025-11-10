CI/CD Workflows
================

After we've managed to build our scrample binary, we need to ensure, that the build is not broken
by the future changes. For this we should create a CI/CD workflow, that triggers a
`GitHub action <https://docs.github.com/en/actions>`_
for building our scrample application every time a new PR is raised.

To achieve this, first let us create a workflow file `build.yml <https://github.com/eclipse-score/scrample/blob/main/.github/workflows/build.yml>`_
in the .github folder.

Next, we should fill the workflow file with content as shown below:

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

First, as shown in the line 2, we need to define when the workflow should be executed. In our case, we want to build the
scrample application everytime the PR is *opened*, *created* or *synchronized*.

Second, we need to define which jobs should be executed. For now, it is only one job that builds the scrample application, as shown
in the line 8.

Finally, we need to define steps of the build job:

- in the line 11 we checkout the repository
- in the line 13 we setup the bazel
- in the line 15 we set up the QNX license, using CI lisense, that is stored in the secret storage
  of the CI infrastructure
- finally, in the line 21 we define the step to build the scrample application. After setting the QNX variables
  we run the bazel command, that we also ran locally, to build the *scrample binary*
- as last step, in the line 28 we do a clean up and remove all unnecessary files from the remote build machine.

As soon, as the workflow is merged to the repository, every time someone creates a PR, we will see the execution
of the build target in the `Actions sections <https://github.com/eclipse-score/reference_integration/actions>`_
of the repository.
