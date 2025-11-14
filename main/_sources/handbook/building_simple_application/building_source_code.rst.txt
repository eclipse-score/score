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

Now, since we’ve provided the documentation for our component, it is time to add some code (as shown in the following 
`commit <https://github.com/eclipse-score/scrample/commit/5179175823ecda51775e459ad73d7230cd4c880a>`_).
 
Let us go through the most important parts of it, and start with bazel
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

`cc_binary  <https://bazel.build/reference/be/c-cpp#cc_binary>`_ produces a cpp binary,
by starting C/C++ compilation with the specified toolchain.
We will talk about defining and specifying the toolchain later in this chapter.
Let us first have a look at the content of the *cc_binary*.

*cc_binary* attributes are very well described in the bazel documentation (it definitely makes sense to check it out).
In our case, the rule has three source files that we want to compile.
Additionally, our *scrample* binary depends on the *communication* module for the ipc functionality and on the *baselibs* module
for cpp language extension and logging functionality.
We can also see that *cc_binary* for scrample has the “public” visibility.
That’s because we want to use it later in the *reference integration* module.

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

Additionally, there is also a sender/receiver and a datatype `cc_library  <https://bazel.build/reference/be/c-cpp#cc_library>`_,
separated in standalone libraries for a better testability. Scrample *cc_binary* rule depends on them as well.
Now, as we’ve defined the targets, it would be time to build the binary. For this, we need first to specify the toolchain,
that should be used for building our binary and that will call compiler and linker at the end.
We aim to run our application in QNX qemu environment, therefore we should compile our application with qcc toolchain.

Before we continue, two fundamental concepts in bazel 
(`bazel toolchains  <https://bazel.build/extending/toolchains>`_ and `bazel platforms  <https://bazel.build/extending/platforms>`_)
are worth mentioning.

A complete explanation of these concepts goes beyond this small tutorial. But in order to move forward,
it is important to give at least a brief explanation, what these concepts are about.

The *bazel toolchain* specifies -at least in our case- which compiler toolchain is used to compile and link the code.
It could be qcc, gcc or llvm toolchain.

*bazel platform* specifies for which cpu architecture the toolchain should build the binary, e.g. arm or x86.
For our small scrample example we plan to build with qcc toolchain for x86_64 platform.
In order to add qcc toolchain support to our module, we first need to extend our 
`MODULE.bazel <https://github.com/eclipse-score/scrample/blob/main/MODULE.bazel>`_  file with the toolchain information.

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

As you can see, we reference here the *score_toolchains_qnx* module, as dependency.
It contains qnx toolchain including compiler, linker, image creation tools and their configuration for the Eclipse S-CORE project.

.. tip::
    CI/CD pipeline uses its own QNX license for building the code with qnx. If you want to build the source code with
    qnx compiler locally, you will need to acquire a QNX 8.x "free for non commercial use" license and install QNX 8.x SDP
    as described in the `QNX & QEMU set-up tutorial <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu>`_.

As our application depends on baselibs and communication module (as described in the 
`src/BUILD <https://github.com/eclipse-score/scrample/blob/main/src/BUILD>`_ file),
we need to add the dependencies to these modules into the `MODULE.bazel <https://github.com/eclipse-score/scrample/blob/main/MODULE.bazel>`_
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

Additionally, we needed to add some modules, as listed above. Scrample application doesn’t need these modules,
but they are needed by the modules, that scrample application directly depends on. *platforms* and *score_bazel_platforms*
is needed by *qnx_toolchain* module and *tlrc* by *communication* module. Bazel module doesn’t inherit dependencies of the module,
from which it depends on directly. This is why you always need to specify the whole list of module dependencies in the *MODULE.bazel* file.

Until now, we’ve assumed that there is a dependency between our module and another bazel module that defines qcc toolchain.
Now we want to start using this toolchain in our module. Therefore we need to specify the platform and configure the usage of
qcc toolchain in `.bazelrc <https://github.com/eclipse-score/scrample/blob/main/.bazelrc>`_ file.

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

In lines 1-6, we define compiler options, that are related to the code itself.
Therefore, they should be used during the compilation of our source code by all toolchains.
It is important to understand, that bazel modules we depend on, are built in the context of our bazel module configuration.
This is why we also need to specify the compiler settings, that are necessary to build depending bazel modules.

Further, in line 8 we take over the common configuration also for the qnx toolchain.
Afterwards we specify compiler and linker flags, that are relevant for the qnx toolchain only.
 
In line 12-13 (highlighted in the code snippet) we define to use the *qnx toolchain*,
that we’ve previously referenced in the `MODULE.bazel <https://github.com/eclipse-score/scrample/blob/main/MODULE.bazel>`_ file.
Additionally, we want to build our code for the *x86_64-qnx platform*.
This is important, since our qnx toolchain provides support for multiple platforms, e.g. *arm* and *x86_64*.

Finally, we can compile our code. We need to specify explicitly which config should be used during the compilation, as shown in the example:

.. code-block:: python
    :linenos:

    bazel build --config=x86_64-qnx  //src:scrample

After the successfull compilation the binary can be normally found in the build folder:

.. code-block:: python
    :linenos:

    Target //src:scrample up-to-date:
        bazel-bin/src/scrample

Now it is time to run the binary in the reference QNX QEMU image.