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

Building source code
=====================

.. toctree::
   :maxdepth: 1
   :glob:

.. _building_source_code:

Now that we have added the documentation for our component, we can continue by adding some source code (as shown in the following 
`commit <https://github.com/eclipse-score/scrample/commit/5179175823ecda51775e459ad73d7230cd4c880a>`_).

Let’s begin with the most relevant parts of the implementation, starting with the bazel 
`src/BUILD <https://github.com/eclipse-score/scrample/blob/main/src/BUILD>`_ file.

.. code-block:: python
    :linenos:

    cc_binary(
        name = "scrample",
        srcs = [
            "assert_handler.cpp",
            "assert_handler.h",
            "main.cpp",
        ],
        visibility = ["//visibility:public"],
        deps = [
            ":sample_sender_receiver",
            "@score_communication//score/mw/com",
            "@boost.program_options",
            "@score_baselibs//score/language/futurecpp",
            "@score_baselibs//score/mw/log",
        ],
    )

The `cc_binary  <https://bazel.build/reference/be/c-cpp#cc_binary>`_ produces a cpp binary,
by starting C/C++ compilation with the specified toolchain. We will define the toolchain later in this chapter.
Let’s first look at the content of the cc_binary.

The attributes of *cc_binary*  are documented in detail in the bazel documentation, and it is worth reviewing them. 
In this example, the rule includes three source files. The *scrample* binary depends on: 

- the *communication* module (IPC functionality) 
- the *baselibs* module (cpp language extension and logging)

The scrample target is marked with “public” visibility so that it can be used later in the *reference integration* module.

.. code-block:: python
    :linenos:

    cc_library(
        name = "sample_sender_receiver",
        srcs = [
            "sample_sender_receiver.cpp",
        ],
        hdrs = [
            "sample_sender_receiver.h",
        ],
        deps = [
            ":datatype",
            "@score_communication//score/mw/com",
            "@score_baselibs//score/mw/log",
        ],
    )

    cc_library(
        name = "datatype",
        srcs = [
            "datatype.cpp",
        ],
        hdrs = [
            "datatype.h",
        ],
        deps = [
            "@score_communication//score/mw/com",
            "@score_baselibs//score/language/futurecpp",
        ],
    )

The sender/receiver logic and the datatype handling are implemented as separate
`cc_library  <https://bazel.build/reference/be/c-cpp#cc_library>`_ targets to improve testability. 

The scrample cc_binary depends on both libraries. 

Now that the targets are defined, we can build the binary. 

To do so, we must first specify the toolchain that compile and link  the code.
Since we want to run the application in QNX qemu environment, we will build it using the qcc toolchain.
Before continuing, it is helpful to introduce two fundamental bazel concepts:bazel toolchains and bazel platforms.

A complete explanation is beyond the scope of this small tutorial, but the following brief overview is sufficient: 

- A `bazel toolchains  <https://bazel.build/extending/toolchain>`_ specifies which compiler toolchain and linker are used (e.g., qcc, gcc or llvm).
- A `bazel platforms  <https://bazel.build/extending/platform>`_ defines the target cpu architecture (e.g., arm or x86). 

For the scrample example, we want to use the qcc toolchain for x86_64 platform.
To add qcc toolchain support to our module, we extend the
`MODULE.bazel <https://github.com/eclipse-score/scrample/blob/main/MODULE.bazel>`_ file with the corresponding toolchain configuration.

.. code-block:: python
    :linenos:

    # Configure the target toolchain.
    bazel_dep(name = "score_toolchains_qnx", version = "0.0.2", dev_dependency=True)
    qnx = use_extension("@score_toolchains_qnx//:extensions.bzl", "toolchains_qnx", dev_dependency=True)
    qnx.sdp(
        sha256 = "f2e0cb21c6baddbcb65f6a70610ce498e7685de8ea2e0f1648f01b327f6bac63",
        strip_prefix = "installation",
        url = "https://www.qnx.com/download/download/79858/installation.tgz",
    )
    use_repo(qnx, "toolchains_qnx_sdp")
    use_repo(qnx, "toolchains_qnx_qcc")

The score_toolchains_qnx module is referenced here as a dependency.
It contains qnx toolchain, including compiler, linker, image creation tools, and their configuration for the Eclipse S-CORE project.

.. tip::
    CI/CD pipeline uses its own QNX license when building the code with qnx. If you want to build the source code with
    qnx compiler locally, you must acquire a QNX 8.x "free for non commercial use" license and install QNX 8.x SDP
    as described in the `QNX & QEMU set-up tutorial <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu>`_.

Since our application depends on baselibs and communication module (as defined in the 
`src/BUILD <https://github.com/eclipse-score/scrample/blob/main/src/BUILD>`_ file),
we also need to add the dependencies to these modules into the `MODULE.bazel <https://github.com/eclipse-score/scrample/blob/main/MODULE.bazel>`_
file as well, as shown below:

.. code-block:: python
    :linenos:

    bazel_dep(name = "score-baselibs", version = "0.1.1")

    bazel_dep(name = "communication", version = "0.1.1")

.. code-block:: python
    :linenos:
    
    bazel_dep(name = "platforms", version = "0.0.11")

    bazel_dep(name = "score_bazel_platforms", version = "0.0.2")

    # TRLC dependency for requirements traceability
    bazel_dep(name = "trlc", version = "0.0.0")
    git_override(
        module_name = "trlc",
        commit = "ede35c4411d41abe42b8f19e78f8989ff79ad3d8",
        remote = "https://github.com/bmw-software-engineering/trlc.git",
    )

In addition to the previously mentioned modules, we also need to add some modules, as listed above. 

The scrample application does not use these modules directly, but the modules it depends on do. For example: 
- *platforms* and *score_bazel_platforms* are required by the qnx_toolchain module 
- *tlrc* is required by the *communication* module 

Bazel modules don’t inherit transitive dependencies automatically.
This means that you must always list all required module dependencies explicitly in your *MODULE.bazel* file.
So far, we have assumed that our module depends on another bazel module providing the qcc toolchain. 
To actually use this toolchain, we now need to specify the platform and configure the usage of qcc toolchain in
`.bazelrc <https://github.com/eclipse-score/scrample/blob/main/.bazelrc>`_ file.

.. code-block:: python
    :linenos:
    :emphasize-lines: 12

    build:_common --@score_baselibs//score/mw/log/detail/flags:KUse_Stub_Implementation_Only=False
    build:_common --@score_baselibs//score/mw/log/flags:KRemote_Logging=False
    build:_common --@score_baselibs//score/json:base_library=nlohmann
    build:_common --@score_baselibs//score/memory/shared/flags:use_typedshmd=False
    build:_common --@score_communication//score/mw/com/flags:tracing_library=stub
    build:_common --cxxopt=-Wno-error=mismatched-new-delete

    build:x86_64-qnx --config=_common
    build:x86_64-qnx --noexperimental_merged_skyframe_analysis_execution
    build:x86_64-qnx --incompatible_enable_cc_toolchain_resolution
    build:x86_64-qnx --incompatible_strict_action_env
    build:x86_64-qnx --platforms=@score_bazel_platforms//:x86_64-qnx
    build:x86_64-qnx --extra_toolchains=@toolchains_qnx_qcc//:qcc_x86_64

Lines 1-6 define compiler options that apply to the source code itself.

These options must be used by all toolchains, because bazel builds not only your module,
but also all dependent modules within the context of your bazel module’s configuration.
For this reason, you must specify the compiler settings that are required to build your dependencies as well.

In line 8, we apply the common configuration to the qnx toolchain.
Afterwards, we specify additional compiler and linker flags that apply only to the qnx toolchain.

Lines 12-13 (highlighted in the code snippet) configure bazel to use the *qnx toolchain* referenced earlier
in the `MODULE.bazel <https://github.com/eclipse-score/scrample/blob/main/MODULE.bazel>`_ file.

We also build our code for the *x86_64-qnx platform*. This is important, since our qnx toolchain supports multiple platforms
(e.g., *arm* and *x86_64*).

Finally, we can compile the code.  During the build, we must explicitly select the configuration to use, as shown in the example:

.. code-block:: python
    :linenos:

    bazel build --config=x86_64-qnx  //src:scrample

After the successfull compilation the binary can be normally found in the build folder:

.. code-block:: python
    :linenos:

    Target //src:scrample up-to-date:
        bazel-bin/src/scrample

Now it is time to run the binary in the reference QNX QEMU image.