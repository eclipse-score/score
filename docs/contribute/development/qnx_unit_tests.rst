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

Running Unit Tests on QNX
#########################

This page is the entry point for running C++/Rust unit tests for QNX 8 on a Linux development machine.
It applies to every S-CORE Bazel repository and only links to the places that own the details instead of
repeating them:

* `qnx_unit_tests <https://github.com/eclipse-score/qnx_unit_tests/blob/main/README.md>`_ (Bazel module
  ``score_qnx_unit_tests``): cross-compiled tests are booted in a QEMU micro-VM on QNX. Its README is the
  reference for ``--run_under`` / wrapper macros, debugging, excluding tests and environment variables.
* `bazel_cpp_toolchains <https://github.com/eclipse-score/bazel_cpp_toolchains/blob/main/docs/qnx_integration.md>`_:
  QCC toolchain, SDP download and license configuration.
* `cicd-workflows <https://github.com/eclipse-score/cicd-workflows/blob/main/.github/workflows/bazel-qnx.md>`_:
  QNX jobs and secrets in GitHub Actions.

.. note::

   This is about *unit tests* (single test binary in a minimal QNX image). To boot a full QNX image or run
   feature/integration tests, see the
   `reference_integration README <https://github.com/eclipse-score/reference_integration/blob/main/README.md>`_
   and its `integration process <https://github.com/eclipse-score/reference_integration/tree/main/docs/integration_process>`_.

Checklist (one-time)
====================

#. **Host tools:** Linux, Bazelisk, ``qemu-system-x86_64`` (``qemu-system-aarch64`` for AArch64) and
   access to ``/dev/kvm``
   (see `Prerequisites <https://github.com/eclipse-score/qnx_unit_tests/blob/main/README.md#prerequisites>`_).
#. **myQNX credentials** for the SDP download: ``~/.netrc`` entry for ``qnx.com`` or the variables
   ``SCORE_QNX_USER`` / ``SCORE_QNX_PASSWORD``. The repository's ``.bazelrc`` must register a
   ``qnx_credential_helper.py`` (see
   `toolchains_qnx <https://github.com/eclipse-score/toolchains_qnx#using-pre-packaged-qnx-80-sdp>`_);
   all S-CORE repositories already do.
#. **QNX license** at ``/opt/score_qnx/license/licenses``. Obtain and install it as described in
   `Obtaining QNX SDP and Licenses <https://github.com/eclipse-score/bazel_cpp_toolchains/blob/main/docs/qnx_integration.md#obtaining-qnx-sdp-and-licenses>`_
   and `toolchains_qnx <https://github.com/eclipse-score/toolchains_qnx#where-to-obtain-the-qnx-80-sdp>`_.
   QNX Software Center installs it to ``~/.qnx/license/licenses``; symlink it if you use the default path.
   Verify with ``ls -L /opt/score_qnx/license/licenses``: a dangling symlink is treated as "no license".

Running the tests
=================

Look up the QNX configs in the repository's ``.bazelrc`` (``score-qnx-x86_64`` / ``score-qnx-aarch64``)
Tests are only executed in QEMU if the config runs them
through ``score_qnx_unit_tests``.

**Recommended:** set this once in the repository's ``.bazelrc`` so that every developer and CI job gets it
(requires ``bazel_dep(name = "score_qnx_unit_tests", ..., dev_dependency = True)`` in ``MODULE.bazel``):

.. code-block:: text

   test:score-qnx-x86_64 --run_under=@score_qnx_unit_tests//src:run_under_qnx
   test:score-qnx-aarch64 --run_under=@score_qnx_unit_tests//src:run_under_qnx

Then tests are run with a plain command:

.. code-block:: shell

   bazel test --config=score-qnx-x86_64 //path/to:unit_test

If the repository does not set it yet, either add the lines above or pass the flag on the command line:

.. code-block:: shell

   bazel test --config=score-qnx-x86_64 \
       --run_under=@score_qnx_unit_tests//src:run_under_qnx \
       //path/to:unit_test

Without ``--run_under`` Bazel tries to execute the QNX binary on the host, so the test fails.
AArch64 is emulated and slow; raise ``--test_timeout`` if needed. For ``cc_test_qnx`` wrappers, shell and
GDB debugging, ``--test_env`` options (``DISABLE_KVM``, ``QEMU_CPU``, ``QNX_FORWARD_ENV``), see the
`qnx_unit_tests README <https://github.com/eclipse-score/qnx_unit_tests/blob/main/README.md>`_.

Troubleshooting
===============

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Symptom
     - Fix
   * - ``You don't have a valid license for this product``
     - License missing, expired or the symlink target does not exist (see checklist).
   * - SDP download fails
     - Check the myQNX credentials and the credential helper configuration.
   * - Very slow tests or timeouts
     - No KVM access (``DISABLE_KVM=1`` is the slow fallback) or AArch64 emulation.
