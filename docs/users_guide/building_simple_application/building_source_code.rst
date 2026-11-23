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

.. _building_source_code:

Build and test
==============

The running example is the component ``component_example`` of the module template. It consists of the following files
in `score/component_example <https://github.com/eclipse-score/module_template/tree/main/score/component_example>`_
and `score/tests <https://github.com/eclipse-score/module_template/tree/main/score/tests>`_:

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - File
     - Content
   * - ``score/component_example/src/component_example.hpp``
     - Interface of the component
   * - ``score/component_example/src/component_example.cpp``
     - Implementation
   * - ``score/component_example/src/component_example_test.cpp``
     - Unit test
   * - ``score/component_example/tests/component_example_test.cpp``
     - Component integration test
   * - ``score/component_example/BUILD``
     - Bazel targets of the component
   * - ``score/component_example/docs/``
     - Documentation of the component, see :doc:`documentation generation <doc_generation>`
   * - ``score/tests/test_main.cpp``, ``score/tests/test_main.rs``, ``score/tests/BUILD``
     - Feature integration tests of the module in C++ and Rust

The code
--------
The interface declares two functions:

.. code-block:: cpp
    :linenos:

    namespace score {
    namespace component_example {

    // Unit
    std::string make_hello();

    // Component API
    std::string make_hello_message(const std::string& name);

    }  // namespace component_example
    }  // namespace score

``make_hello()`` stands for a *unit*, the smallest part of the component which is tested on its own.
``make_hello_message()`` is the *component API*, which other components and modules use.
The implementation combines both:

.. code-block:: cpp
    :linenos:
    :emphasize-lines: 7

    #include "score/component_example/src/component_example.hpp"

    std::string make_hello() {
        return "Hello";
    }

    // req-traceability: comp_req__mod_temp_component_name__some_title
    std::string make_hello_message(const std::string& name) {
        return make_hello() + ", " + name + "!";
    }

Line 7 links the implementation to the component requirement it implements. The
:doc:`documentation generation <doc_generation>` chapter shows how this link appears in the documentation.
Include paths start at the root of the repository, e.g. ``score/component_example/src/...``.

Bazel targets
-------------
The Bazel targets of the component are defined in
`score/component_example/BUILD <https://github.com/eclipse-score/module_template/blob/main/score/component_example/BUILD>`_:

.. code-block:: python
    :linenos:

    cc_library(
        name = "component_example",
        srcs = ["src/component_example.cpp"],
        hdrs = ["src/component_example.hpp"],
        visibility = ["//visibility:public"],
    )

    cc_test(
        name = "component_example_unit_tests",
        size = "small",
        srcs = ["src/component_example_test.cpp"],
        deps = [
            ":component_example",
            "@googletest//:gtest_main",
        ],
    )

    cc_test(
        name = "component_example_component_integration_tests",
        size = "small",
        srcs = ["tests/component_example_test.cpp"],
        deps = [
            ":component_example",
            "@googletest//:gtest_main",
        ],
    )

- The `cc_library <https://bazel.build/reference/be/c-cpp#cc_library>`_ ``component_example`` contains the code of the
  component. ``visibility = ["//visibility:public"]`` allows other packages and modules to use it.
- The two `cc_test <https://bazel.build/reference/be/c-cpp#cc_test>`_ targets build the tests with GoogleTest.
  ``gtest_main`` provides the ``main()`` function, so the test files only contain the test cases.
- The ``BUILD`` file additionally contains the ``docs_bundle`` of the component, which is explained in the
  :doc:`documentation generation <doc_generation>` chapter.

Targets of other modules are referenced with the ``@<module>//<package>:<target>`` syntax, e.g.
``@googletest//:gtest_main``. To use an S-CORE module, declare it with ``bazel_dep`` in ``MODULE.bazel``
(see :doc:`first_score_module`) and add its targets to ``deps``, e.g. the CRC32 calculation of ``score_baselibs``:

.. code-block:: python

    deps = [
        "@score_baselibs//score/hash/code/crc:crc_ieee",
    ],

Test levels
-----------
S-CORE distinguishes the test levels described in the :ref:`software verification plan <software_verification_plan>`.
The template contains an example for each of them:

.. list-table::
   :header-rows: 1
   :widths: 20 22 18 40

   * - Test level
     - Location
     - Framework
     - Example
   * - Unit test
     - ``score/<component>/src/``
     - GoogleTest
     - ``component_example_unit_tests`` tests the unit ``make_hello()``
   * - Component integration test
     - ``score/<component>/tests/``
     - GoogleTest
     - ``component_example_component_integration_tests`` tests the component API ``make_hello_message()``
       against the component requirement
   * - Feature integration test
     - ``score/tests/``
     - GoogleTest, Rust test
     - ``feature_integration_tests_cpp`` and ``feature_integration_tests_rust`` test the module as a whole;
       the Rust test is only a placeholder

The template uses the simplest form for all levels: plain GoogleTest tests for C++ and the built-in test framework
for Rust. For more extensive tests, S-CORE provides dedicated frameworks: the test scenarios from
`testing_tools <https://github.com/eclipse-score/testing_tools>`_ for component integration tests, which are
implemented in C++ or Rust and driven by pytest, and the
`Integration Testing Framework (ITF) <https://github.com/eclipse-score/itf>`_ for feature integration tests,
which runs pytest-based tests on Docker containers, QEMU virtual machines or real hardware.
See :ref:`Overview of technologies <technology_overview>` for details.

The component integration test shows how a test declares what it verifies:

.. code-block:: cpp
    :linenos:
    :emphasize-lines: 2, 3, 4, 5

    TEST(ComponentExampleTest, MakeHelloMessageReturnsExpectedGreeting) {
        RecordProperty("PartiallyVerifies", "comp_req__mod_temp_component_name__some_title");
        RecordProperty("TestType", "requirements-based");
        RecordProperty("DerivationTechnique", "requirements-analysis");
        RecordProperty("Description", "Verify make_hello_message returns the greeting for each name.");

        EXPECT_EQ(make_hello_message("World"), "Hello, World!");
        EXPECT_EQ(make_hello_message("SCORE"), "Hello, SCORE!");
    }

GoogleTest writes these properties into the test result. The documentation build reads them and links the test
to the requirement, see :doc:`documentation generation <doc_generation>`.


Toolchains and platforms
------------------------
Before building the binaries, it is helpful to introduce two fundamental Bazel concepts: toolchains and platforms.

A complete explanation is beyond the scope of this small tutorial, but the following brief overview is sufficient:

- A `Bazel toolchain <https://bazel.build/extending/toolchains>`_ specifies which compiler and linker are used (e.g., GCC, QCC, Ferrocene).
- A `Bazel platform <https://bazel.build/extending/platforms>`_ defines the target CPU architecture and OS (e.g., x86_64 Linux or x86_64 QNX).

All S-CORE modules use the same toolchains, provided by
`score_bazel_cpp_toolchains <https://github.com/eclipse-score/bazel_cpp_toolchains>`_ (GCC and QCC) and
`score_toolchains_rust <https://github.com/eclipse-score/toolchains_rust>`_ (Ferrocene),
and the platforms defined in `score_bazel_platforms <https://github.com/eclipse-score/bazel_platforms>`_.
In the module template, they are registered in the ``MODULE.bazel`` block *S-CORE Toolchains (DO NOT MODIFY)*, e.g.:

.. code-block:: python
    :linenos:

    gcc = use_extension("@score_bazel_cpp_toolchains//extensions:gcc.bzl", "gcc")

    gcc.toolchain(
        name = "score_gcc_x86_64_toolchain",
        target_cpu = "x86_64",
        target_os = "linux",
        use_default_package = True,
        version = "12.2.0",
    )

The template contains such toolchains for Linux (x86_64, aarch64), QNX SDP 8.0 (x86_64, aarch64),
Red Hat AutoSD and Elektrobit corbos Linux for Safety Applications.
The file `score.bazelrc/score_toolchain.bazelrc <https://github.com/eclipse-score/module_template/blob/main/score.bazelrc/score_toolchain.bazelrc>`_
combines each platform with its toolchains into a build configuration:

.. code-block:: text
    :linenos:

    build:score-linux-x86_64 --config=_score_common
    build:score-linux-x86_64 --extra_toolchains=@score_gcc_x86_64_toolchain//:x86_64-linux-gcc_12.2.0
    build:score-linux-x86_64 --platforms=@score_bazel_platforms//:x86_64-linux-gcc_12.2.0-posix

    build:score-qnx-x86_64 --config=_score_common
    build:score-qnx-x86_64 --platforms=@score_bazel_platforms//:x86_64-qnx-sdp_8.0.0-posix
    build:score-qnx-x86_64 --extra_toolchains=@score_qcc_x86_64_toolchain//:x86_64-qnx-sdp_8.0.0
    build:score-qnx-x86_64 --extra_toolchains=@score_toolchains_rust//toolchains/ferrocene:ferrocene_x86_64_pc_nto_qnx800

Without ``--config``, Bazel builds for the host with the LLVM toolchain that the template registers in ``MODULE.bazel``
(``toolchains_llvm``). This is fine for a quick local test run; for the S-CORE target platforms, always use
one of the ``score-*`` configurations.

.. tip::
    The CI/CD pipeline uses its own QNX license when building the code with QNX. If you want to build the source code with
    the QNX compiler locally, you need a QNX license, e.g. the free community license *QNX Everywhere*, installed at
    ``/opt/score_qnx/license/licenses``, and access to the QNX SDP download. The setup is described in the
    `QNX integration guide <https://github.com/eclipse-score/bazel_cpp_toolchains/blob/main/docs/qnx_integration.md>`_
    of ``score_bazel_cpp_toolchains``.

Building and running the tests
------------------------------
Build all targets of the module for Linux x86_64:

.. code-block:: bash

    bazel build --config=score-linux-x86_64 //score/...

Run all tests of the module, or only the tests of one test level:

.. code-block:: bash

    # all tests
    bazel test --config=score-linux-x86_64 //score/...

    # unit tests of the component
    bazel test --config=score-linux-x86_64 //score/component_example:component_example_unit_tests

    # component integration tests of the component
    bazel test --config=score-linux-x86_64 //score/component_example:component_example_component_integration_tests

    # feature integration tests
    bazel test --config=score-linux-x86_64 //score/tests/...

The first run takes a while, because Bazel downloads the toolchains and dependencies. Afterwards, Bazel only
rebuilds what has changed and reuses the results of unchanged tests; such tests are marked as ``(cached)``
in the test summary.

The results of each test, incl. the JUnit XML file ``test.xml``, are stored in ``bazel-testlogs/``, e.g.
``bazel-testlogs/score/component_example/component_example_unit_tests/``.

Checks before a pull request
----------------------------
The CI/CD workflows of your repository run further checks on every pull request. Run them locally before you push:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Command
     - Check
   * - ``pre-commit run --all-files``
     - Whitespace, copyright and REUSE headers, YAML formatting and the Bazel lockfile,
       as configured in ``.pre-commit-config.yaml``; install the tool with ``pip install pre-commit`` if needed
   * - ``bazel test //:format.check``
     - Formatting of the source code, e.g. C++, Rust, Python and Starlark; ``bazel run //:format.fix`` fixes it
   * - ``bazel run //:copyright.check``
     - Copyright headers of the files in ``score/``, ``BUILD`` and ``MODULE.bazel``

The next chapter shows how the component is documented and how requirements, code and tests are linked.
