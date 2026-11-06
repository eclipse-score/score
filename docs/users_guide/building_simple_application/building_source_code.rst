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

The running example consists of a small C++ service and its client. Both are built on two S-CORE modules:
mw::com from ``score_communication`` for the inter-process communication and the CRC32 calculation
from ``score_baselibs``. The sources are located in the
`reference integration <https://github.com/eclipse-score/reference_integration>`_:

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - File
     - Content
   * - `deploy/platform_info/platform_info.h <https://github.com/eclipse-score/reference_integration/blob/main/deploy/platform_info/platform_info.h>`_
     - Service interface and version check, shared by service and consumer
   * - `deploy/platform_info/platform_info.cpp <https://github.com/eclipse-score/reference_integration/blob/main/deploy/platform_info/platform_info.cpp>`_
     - Creation, CRC32 check and comparison of the reported S-CORE version
   * - `deploy/platform_info/gen_platform_info.py <https://github.com/eclipse-score/reference_integration/blob/main/deploy/platform_info/gen_platform_info.py>`_
     - Generates a C++ header with the module versions from ``known_good.json``
   * - `deploy/platform_info/platform_info_service.cpp <https://github.com/eclipse-score/reference_integration/blob/main/deploy/platform_info/platform_info_service.cpp>`_
     - The service (provider)
   * - `deploy/platform_info/etc/mw_com_config.json <https://github.com/eclipse-score/reference_integration/blob/main/deploy/platform_info/etc/mw_com_config.json>`_
     - mw::com configuration of the service
   * - `showcases/standalone/platform_info_consumer.cpp <https://github.com/eclipse-score/reference_integration/blob/main/showcases/standalone/platform_info_consumer.cpp>`_
     - The client (consumer)

Service interface
-----------------
An mw::com service is described by a C++ interface template. The platform info service has a single *field*,
``platform_info``, i.e. a value that the service sets and that clients can read and subscribe to:

.. code-block:: cpp
    :linenos:

    // Fixed-size, zero-terminated strings: the value lives in shared memory.
    struct ModuleVersion
    {
        std::array<char, kNameSize> name;
        std::array<char, kVersionSize> version;
    };

    struct PlatformInfo
    {
        std::array<char, kTimestampSize> known_good_timestamp;
        std::uint32_t module_count;
        std::array<ModuleVersion, kMaxModules> modules;
        std::uint32_t crc32;
    };

    template <typename Trait>
    class PlatformInfoInterface : public Trait::Base
    {
      public:
        using Trait::Base::Base;

        typename Trait::template Field<PlatformInfo, score::mw::com::WithNotifier> platform_info_{*this, "platform_info"};
    };

    using PlatformInfoSkeleton = score::mw::com::AsSkeleton<PlatformInfoInterface>;
    using PlatformInfoProxy = score::mw::com::AsProxy<PlatformInfoInterface>;

The same interface yields both sides of the communication: the *skeleton* is used by the service to provide the field,
the *proxy* is used by the client to access it. Because mw::com exchanges the data via shared memory,
``PlatformInfo`` only contains fixed-size types.

The service implementation is short: it creates the skeleton for the instance specifier ``score/platform/info``,
publishes the value and offers the service until it is stopped:

.. code-block:: cpp
    :linenos:

    score::mw::com::runtime::InitializeRuntime(score::string_manipulation::GetArguments(argc, argv));

    auto instance_specifier = score::mw::com::InstanceSpecifier::Create(std::string{kInstanceSpecifier});
    auto skeleton = PlatformInfoSkeleton::Create(std::move(instance_specifier).value());

    const auto platform_info = MakePlatformInfo();
    skeleton->platform_info_.Update(platform_info);
    skeleton->OfferService();

The client does the opposite: it searches the service via service discovery, creates a proxy,
subscribes to the field and checks the received value:

.. code-block:: cpp
    :linenos:

    auto found = PlatformInfoProxy::FindService(instance_specifier.value());
    auto proxy = PlatformInfoProxy::Create(handles.front());

    proxy->platform_info_.Subscribe(1U);
    proxy->platform_info_.GetNewSamples(
        [&info](score::mw::com::SamplePtr<PlatformInfo> sample) noexcept { info = *sample; }, 1U);

    if (!score::platform::info::IsValid(info.value()))  // CRC32 check with score_baselibs
    {
        return Fail("the S-CORE version reported by the platform fails the CRC32 check");
    }
    const auto differences = score::platform::info::Compare(score::platform::info::MakePlatformInfo(), info.value());

The snippets omit the error handling and the timeouts; see the source files for the complete implementation.

mw::com configuration
---------------------
Which service type, binding and instance belong to the instance specifier ``score/platform/info`` is not compiled
into the binaries, but defined in the mw::com configuration
`etc/mw_com_config.json <https://github.com/eclipse-score/reference_integration/blob/main/deploy/platform_info/etc/mw_com_config.json>`_:

.. code-block:: json
    :linenos:

    "serviceInstances": [
      {
        "instanceSpecifier": "score/platform/info",
        "serviceTypeName": "/score/platform/PlatformInfo",
        "instances": [
          {
            "instanceId": 1,
            "asil-level": "QM",
            "binding": "SHM",
            "fields": [
              { "fieldName": "platform_info", "numberOfSampleSlots": 2, "maxSubscribers": 5 }
            ]
          }
        ]
      }
    ]

mw::com reads ``./etc/mw_com_config.json`` relative to the working directory, or the file passed with
``--service_instance_manifest`` (short ``-s``). Service and client use the same file, so they agree on the service definition.

Bazel targets
-------------
The Bazel targets of the service are defined in
`deploy/platform_info/BUILD <https://github.com/eclipse-score/reference_integration/blob/main/deploy/platform_info/BUILD>`_:

.. code-block:: python
    :linenos:
    :emphasize-lines: 4, 20, 21, 30, 31

    # The S-CORE module versions the platform is built from, as compile-time constants.
    genrule(
        name = "platform_info_data",
        srcs = ["//:known_good.json"],
        outs = ["platform_info_data.h"],
        cmd = "$(execpath :gen_platform_info) $(execpath //:known_good.json) $@",
        tools = [":gen_platform_info"],
    )

    # Service interface and version check: shared by service and consumer.
    cc_library(
        name = "platform_info_interface",
        srcs = [
            "platform_info.cpp",
            ":platform_info_data",
        ],
        hdrs = ["platform_info.h"],
        visibility = ["//showcases:__subpackages__"],
        deps = [
            "@score_baselibs//score/hash/code/crc:crc_ieee",
            "@score_communication//score/mw/com",
        ],
    )

    cc_binary(
        name = "platform_info_service",
        srcs = ["platform_info_service.cpp"],
        deps = [
            ":platform_info_interface",
            "@score_baselibs//score/string_manipulation/arguments",
            "@score_communication//score/mw/com",
        ],
    )

- The `genrule <https://bazel.build/reference/be/general#genrule>`_ ``platform_info_data`` generates the header
  ``platform_info_data.h`` from ``known_good.json``. Bazel regenerates it whenever ``known_good.json`` changes,
  so service and consumer always carry the versions they were built from.
- The `cc_library <https://bazel.build/reference/be/c-cpp#cc_library>`_ ``platform_info_interface`` contains
  the shared interface. Its dependencies reference targets of other Bazel modules with the ``@<module>//<package>:<target>``
  syntax, here mw::com and the CRC32 calculation.
- The `cc_binary <https://bazel.build/reference/be/c-cpp#cc_binary>`_ ``platform_info_service`` produces the
  executable of the service.

The consumer is defined in the same way in
`showcases/standalone/BUILD <https://github.com/eclipse-score/reference_integration/blob/main/showcases/standalone/BUILD>`_
and depends on the shared interface library:

.. code-block:: python
    :linenos:

    cc_binary(
        name = "platform_info_consumer",
        srcs = ["platform_info_consumer.cpp"],
        deps = [
            "//deploy/platform_info:platform_info_interface",
            "@score_baselibs//score/string_manipulation/arguments",
            "@score_communication//score/mw/com",
        ],
    )

Toolchains and platforms
------------------------
Before building the binaries, it is helpful to introduce two fundamental Bazel concepts: toolchains and platforms.

A complete explanation is beyond the scope of this small tutorial, but the following brief overview is sufficient:

- A `Bazel toolchain <https://bazel.build/extending/toolchain>`_ specifies which compiler and linker are used (e.g., GCC, QCC, Ferrocene).
- A `Bazel platform <https://bazel.build/extending/platform>`_ defines the target CPU architecture and OS (e.g., x86_64 Linux or x86_64 QNX).

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

The reference integration uses the same setup, but names its configurations after the reference images:
``linux-x86_64``, ``linux-aarch64``, ``qnx-x86_64``, ``qnx-aarch64``, ``autosd-x86_64`` and ``eb-aarch64``
(see its `.bazelrc <https://github.com/eclipse-score/reference_integration/blob/main/.bazelrc>`_).
There, the shared configuration ``_common`` also sets build settings of the integrated modules, e.g.:

.. code-block:: text

    build:_common --@score_communication//score/memory/shared/flags:use_typedshmd=False
    build:_common --@score_baselibs//score/json:base_library=nlohmann

These options must be set in the repository that builds the binaries, because Bazel builds all dependent modules
within the configuration of the root module.

.. tip::
    The CI/CD pipeline uses its own QNX license when building the code with QNX. If you want to build the source code with
    the QNX compiler locally, you must acquire a QNX 8.x "free for non commercial use" license and install QNX 8.x SDP
    as described in the `QNX & QEMU set-up tutorial <https://github.com/eclipse-score/reference_integration/blob/main/runners/qemu_x86_64/README.md>`_.

Building the binaries
---------------------
Always use an explicit build configuration. In the reference integration:

**Linux x86_64:**

.. code-block:: bash
    :linenos:

    bazel build --config=linux-x86_64 //deploy/platform_info:platform_info_service //showcases/standalone:platform_info_consumer

**QNX x86_64 cross-compilation:**

.. code-block:: bash
    :linenos:

    bazel build --config=qnx-x86_64 //deploy/platform_info:platform_info_service //showcases/standalone:platform_info_consumer

In your own module, use the configurations of the template instead, e.g.
``bazel build --config=score-linux-x86_64 //score/...``.

After a successful build, the binaries can be found in the build folder:

.. code-block:: text
    :linenos:

    bazel-bin/deploy/platform_info/platform_info_service
    bazel-bin/showcases/standalone/platform_info_consumer

Running the example
-------------------
The Linux binaries can be started directly on the host. mw::com needs the directory for its service discovery,
the service is started in the background and the consumer gets the deployed mw::com configuration:

.. code-block:: bash
    :linenos:

    mkdir -p /tmp/mw_com_lola/service_discovery
    cd deploy/platform_info
    ../../bazel-bin/deploy/platform_info/platform_info_service &
    ../../bazel-bin/showcases/standalone/platform_info_consumer --service_instance_manifest etc/mw_com_config.json
    kill %1

The service logs the S-CORE version it reports, and the consumer confirms that it found the service and that the
versions match:

.. code-block:: text

    platform_info_service: offering score/platform/info for S-CORE known_good 2026-08-28T09:19:12Z
      score_baselibs ee40fece5abacb28ea641b448446a04175038b17
      ...
    platform_info_consumer: found the platform info service
    platform_info_consumer: platform runs S-CORE known_good 2026-08-28T09:19:12Z
      ...
    platform_info_consumer: S-CORE version check passed (8 modules match)

If the service is not running, or reports a different S-CORE version, the consumer exits with ``1`` and names the reason,
e.g. the module whose version differs.

Now it is time to make sure that every change is built and tested automatically.
