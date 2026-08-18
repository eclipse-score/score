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

Building source code
=====================

SCRAMPLE provides two minimal “Hello World” applications — one in C++ and one in Rust — that
both use the S-CORE ``mw::log`` logging library.

C++ Application (``src_cpp/BUILD``)
-------------------------------------

Let’s begin with the C++ application, starting with the bazel
`src_cpp/BUILD <https://github.com/eclipse-score/scrample/blob/v0.1.2-simple-app/src_cpp/BUILD>`_ file.

.. code-block:: python
    :linenos:

    cc_binary(
        name = "scrample_cpp",
        srcs = ["main.cpp"],
        data = ["//config:logging.json"],
        visibility = ["//visibility:public"],
        deps = [
            "@score_logging//score/mw/log",
        ],
    )

The `cc_binary <https://bazel.build/reference/be/c-cpp#cc_binary>`_ produces a C++ binary.
The attributes of *cc_binary* are documented in detail in the Bazel documentation.
The *scrample_cpp* binary depends on:

- the *score_logging* module (``mw::log`` logging library)

The logging configuration is provided via ``//config:logging.json``, which is made available
at runtime through Bazel’s runfiles mechanism.

Rust Application (``src_rust/BUILD``)
--------------------------------------

The Rust application is defined in
`src_rust/BUILD <https://github.com/eclipse-score/scrample/blob/v0.1.2-simple-app/src_rust/BUILD>`_:

.. code-block:: python
    :linenos:

    load("@rules_rust//rust:defs.bzl", "rust_binary")

    RUSTC_FLAGS = select({
        "@platforms//os:qnx": [
            "-Clink-arg=-lc++",
            "-Clink-arg=-lm",
        ],
        "//conditions:default": [
            "-Clink-arg=-lstdc++",
            "-Clink-arg=-lm",
            "-Clink-arg=-lc",
        ],
    })

    rust_binary(
        name = "scrample_rust",
        srcs = ["main.rs"],
        data = ["//config:logging.json"],
        edition = "2021",
        rustc_flags = RUSTC_FLAGS,
        visibility = ["//visibility:public"],
        deps = [
            "@score_baselibs_rust//src/log/score_log",
            "@score_logging//score/mw/log/rust/score_log_bridge",
        ],
    )

The Rust binary uses:

- ``score_log`` from the *score_baselibs_rust* module as a Rust logging facade
- ``score_log_bridge`` from the *score_logging* module to bridge Rust logging to the ``mw::log`` C++ backend

The ``RUSTC_FLAGS`` select expression ensures correct C++ standard library linking on both Linux and QNX targets.

Now that the targets are defined, we can build the binaries.

Before continuing, it is helpful to introduce two fundamental Bazel concepts: toolchains and platforms.

A complete explanation is beyond the scope of this small tutorial, but the following brief overview is sufficient:

- A `Bazel toolchain <https://bazel.build/extending/toolchain>`_ specifies which compiler and linker are used (e.g., GCC, Ferrocene).
- A `Bazel platform <https://bazel.build/extending/platform>`_ defines the target CPU architecture and OS (e.g., x86_64 Linux or x86_64 QNX).

SCRAMPLE uses the same toolchain setup as the other S-CORE modules, provided by
`score_bazel_cpp_toolchains <https://github.com/eclipse-score/bazel_cpp_toolchains>`_.
To add these toolchains to our module, we extend the
`MODULE.bazel <https://github.com/eclipse-score/scrample/blob/v0.1.2-simple-app/MODULE.bazel>`_
file with the corresponding configuration:

.. code-block:: python
    :linenos:

    # C++ and QNX toolchains (same setup as score_baselibs / score_baselibs_rust)
    bazel_dep(name = "score_bazel_cpp_toolchains", version = "0.5.1", dev_dependency = True)

    gcc = use_extension("@score_bazel_cpp_toolchains//extensions:gcc.bzl", "gcc", dev_dependency = True)
    gcc.toolchain(
        name = "score_gcc_x86_64_toolchain",
        target_cpu = "x86_64",
        target_os = "linux",
        use_default_package = True,
        version = "12.2.0",
    )
    gcc.toolchain(
        name = "score_qcc_x86_64_toolchain",
        sdp_version = "8.0.0",
        target_cpu = "x86_64",
        target_os = "qnx",
        use_default_package = True,
        version = "12.2.0",
    )
    use_repo(
        gcc,
        "score_gcc_x86_64_toolchain",
        "score_qcc_x86_64_toolchain",
    )

    # Ferrocene Rust toolchains (QNX cross-compilation support)
    bazel_dep(name = "score_toolchains_rust", version = "0.9.1", dev_dependency = True)

The ``score_bazel_cpp_toolchains`` module provides GCC 12.2.0 for both Linux host builds and
QNX SDP 8.0.0 cross-compilation. The ``score_toolchains_rust`` module provides pre-built
`Ferrocene <https://ferrous-systems.com/ferrocene/>`_ toolchains for Rust.

.. tip::
    CI/CD pipeline uses its own QNX license when building the code with QNX. If you want to build the source code with
    the QNX compiler locally, you must acquire a QNX 8.x “free for non commercial use” license and install QNX 8.x SDP
    as described in the `QNX & QEMU set-up tutorial <https://github.com/eclipse-score/reference_integration/blob/v0.5.0-alpha/runners/qemu_x86_64/README.md>`_.

Since our applications depend on the logging and base libraries (as defined in the
`src_cpp/BUILD <https://github.com/eclipse-score/scrample/blob/v0.1.2-simple-app/src_cpp/BUILD>`_ and
`src_rust/BUILD <https://github.com/eclipse-score/scrample/blob/v0.1.2-simple-app/src_rust/BUILD>`_ files),
we also need to add the dependencies to these modules into the
`MODULE.bazel <https://github.com/eclipse-score/scrample/blob/v0.1.2-simple-app/MODULE.bazel>`_ file:

.. code-block:: python
    :linenos:

    bazel_dep(name = "score_baselibs", version = "0.2.7")
    bazel_dep(name = "score_baselibs_rust", version = "0.1.2")
    bazel_dep(name = "score_logging", version = "0.2.1")

.. code-block:: python
    :linenos:

    bazel_dep(name = "platforms", version = "1.0.0")
    bazel_dep(name = "score_bazel_platforms", version = "0.1.2")

Bazel modules don’t inherit transitive dependencies automatically.
This means that you must always list all required module dependencies explicitly in your *MODULE.bazel* file.

To actually use the registered toolchains, we also need to configure them in the
`.bazelrc <https://github.com/eclipse-score/scrample/blob/v0.1.2-simple-app/.bazelrc>`_ file:

.. code-block:: python
    :linenos:
    :emphasize-lines: 1, 2, 11, 12

    common --extra_toolchains=@score_gcc_x86_64_toolchain//:x86_64-linux-gcc_12.2.0
    common --extra_toolchains=@score_toolchains_rust//toolchains/ferrocene:ferrocene_x86_64_unknown_linux_gnu

    common --@score_baselibs//score/memory/shared/flags:use_typedshmd=False
    common --@score_baselibs//score/mw/log/flags:KRemote_Logging=False

    build:_common --@score_baselibs//score/json:base_library=nlohmann
    build:_common --cxxopt=-Wno-error=mismatched-new-delete
    build:_common --cxxopt=-Wno-error=deprecated-declarations

    build:x86_64-qnx --config=_common
    build:x86_64-qnx --noexperimental_merged_skyframe_analysis_execution
    build:x86_64-qnx --incompatible_enable_cc_toolchain_resolution
    build:x86_64-qnx --incompatible_strict_action_env
    build:x86_64-qnx --platforms=@score_bazel_platforms//:x86_64-qnx-sdp_8.0.0-posix
    build:x86_64-qnx --extra_toolchains=@score_qcc_x86_64_toolchain//:x86_64-qnx-sdp_8.0.0
    build:x86_64-qnx --extra_toolchains=@score_toolchains_rust//toolchains/ferrocene:ferrocene_x86_64_pc_nto_qnx800

Lines 1-2 (highlighted) register the GCC and Ferrocene toolchains for all builds.
The Ferrocene Linux toolchain is registered as a ``common`` toolchain so that proc macro crates
(compiled on the host) and QNX target crates share the same compiler metadata format,
which is required for cross-compilation compatibility.

Lines 4-5 set feature flags required by ``score_baselibs`` that are not applicable in
this demo (proprietary shared memory driver and remote logging backend).
These options must be set globally because Bazel builds all dependent modules within
the context of your module’s configuration.

Lines 11-17 (highlighted) configure Bazel to target the QNX SDP 8.0.0 platform and
select the appropriate QNX and Ferrocene toolchains.

Finally, we can compile the code. Always use an explicit build configuration:

**Host build (Linux x86_64):**

.. code-block:: bash
    :linenos:

    bazel build --config=host //src_cpp:scrample_cpp
    bazel build --config=host //src_rust:scrample_rust

**QNX cross-compilation:**

.. code-block:: bash
    :linenos:

    bazel build --config=x86_64-qnx //src_cpp:scrample_cpp
    bazel build --config=x86_64-qnx //src_rust:scrample_rust

After a successful host build, the binaries can be found in the build folder:

.. code-block:: text
    :linenos:

    bazel-bin/src_cpp/scrample_cpp
    bazel-bin/src_rust/scrample_rust

Both apps produce the same log output to the console:

.. code-block:: text

    2026/05/22 12:00:00.0000000 00000000 000 ECU1 SCRM scra log info verbose 1 Hello from SCRAMPLE!

Now it is time to run the binary in the reference QNX QEMU image.
