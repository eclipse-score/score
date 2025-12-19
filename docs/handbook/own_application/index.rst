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
.. _use_own_application:

.. toctree::
   :maxdepth: 1
   :glob:

Use
====

===============
Getting Started
===============

This guide explains how to set up and use the Communication module of Eclipse S-CORE.

To integrate the communication module into your project, follow these steps:


-----------
1. Setup
-----------

Start by creating a new project in your preferred IDE (e.g., Visual Studio Code). A ready-to-use devcontainer is available under:

-	https://github.com/eclipse-score/devcontainer

Reference documentation for the communication module:

-	Overview: https://github.com/eclipse-score/communication
-	User Facing API: https://github.com/eclipse-score/communication/blob/main/score/mw/com/doc/user_facing_API_examples.md


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.1 Add this to your MODULE.bazel:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: MODULE.bazel
   :class: dropdown

   .. code-block:: starlark

      module(name = "use_com_test")

      bazel_dep(name = "score_toolchains_gcc", version = "0.5", dev_dependency=True)

      gcc = use_extension("@score_toolchains_gcc//extensions:gcc.bzl", "gcc", dev_dependency=True)
      gcc.toolchain(
          url = "https://github.com/eclipse-score/toolchains_gcc_packages/releases/download/0.0.1/x86_64-unknown-linux-gnu_gcc12.tar.gz",
          sha256 = "457f5f20f57528033cb840d708b507050d711ae93e009388847e113b11bf3600",
          strip_prefix = "x86_64-unknown-linux-gnu",
      )

      use_repo(gcc, "gcc_toolchain", "gcc_toolchain_gcc")

      bazel_dep(name = "rules_rust", version = "0.61.0")

      crate = use_extension("@rules_rust//crate_universe:extensions.bzl", "crate")

      crate.spec(package = "futures", version = "0.3.31")
      crate.spec(package = "libc", version = "0.2.155")
      crate.spec(package = "clap", version = "4.5.4", features = ["derive"])

      crate.from_specs(name = "crate_index")
      use_repo(crate, "crate_index")

      bazel_dep(name = "rules_boost", repo_name = "com_github_nelhage_rules_boost")
      archive_override(
          module_name = "rules_boost",
          urls = ["https://github.com/nelhage/rules_boost/archive/refs/heads/master.tar.gz"],
          strip_prefix = "rules_boost-master",
      )

      bazel_dep(name = "boost.program_options", version = "1.87.0")
      bazel_dep(name = "score_baselibs", version = "0.1.3")
      bazel_dep(name = "score_communication", version = "0.1.1")

      # TRLC dependency for requirements traceability
      bazel_dep(name = "trlc", version = "0.0.0")
      git_override(
        module_name = "trlc",
        commit = "ede35c4411d41abe42b8f19e78f8989ff79ad3d8",
        remote = "https://github.com/bmw-software-engineering/trlc.git",
      )

Be aware that the version numbers change over time. Always check the latest versions in the respective bazel registry

-	https://github.com/eclipse-score/bazel_registry/tree/main/modules


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.2 Insert this into your .bazelrc:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: .bazelrc
   :class: dropdown

   The following code was originally contained in a collapsible section.

   .. code-block:: text

      common --@score-baselibs//score/mw/log/detail/flags:KUse_Stub_Implementation_Only=False
      common --@score-baselibs//score/mw/log/flags:KRemote_Logging=False
      common --@score-baselibs//score/json:base_library=nlohmann
      common --@communication//score/mw/com/flags:tracing_library=stub

      common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/v0.5.0-beta/

      common --registry=https://bcr.bazel.build

^^^^^^^^^^^^^
1.3 Run Bazel
^^^^^^^^^^^^^

If you start with an empty project, add an empty file named ``BUILD`` into your project root.
Now you can now run build the project with the command bazel ``bazel build //...``

(At this point nothing happens yet, because no targets are defined).
You can now either continue with this guide to create a minimal consumer-producer example or start coding your own application


------------
2. Use it :)
------------

Once your project is set up, you can start sending and receiving messages.

^^^^^^^^^^^^^^^^^^^^
2.1 Basic Structure
^^^^^^^^^^^^^^^^^^^^

Create a folder named ``src`` in your root project directory.
Inside ``src``, create the following folders:

-	``consumer``
-	``producer``

additional folders if needed.


^^^^^^^^^^^
2.2 Message
^^^^^^^^^^^
Before sending messages, define the data type to be exchanged.
Create a file named ``message_data.h`` in your ``src`` directory.

.. code-block:: cpp

   #ifndef SCORE_MESSAGE_DATA_H
   #define SCORE_MESSAGE_DATA_H

   #include "score/mw/com/types.h"

   namespace com_example
   {

   struct Message
   {
     std::string message;
   };

   template <typename Trait>
   class IPCInterface : public Trait::Base
   {
     public:
       using Trait::Base::Base;

       typename Trait::template Event<Message> message_{*this, "message"};
   };

   using IPCInterfaceProxy = score::mw::com::AsProxy<IPCInterface>;
   using IPCInterfaceSkeleton = score::mw::com::AsSkeleton<IPCInterface>;

   } // namespace com_example

   #endif //SCORE_MESSAGE_DATA_H

**What this code does:**

-	struct ``Message`` defines the payload - here is a simple ``message``  string.
-	``IPCInterface`` defines the communication interface used by producer and consumer.

This interface is necessary so producer and consumer know what to send/receive.
The interface provides two roles:

-	``IPCInterfaceProxy``: client-role
-	``IPCInterfaceSkeleton``: server-role

More details are available in the `Eclipse S-Core Communication Doc <https://eclipse-score.github.io/score/main/features/communication/docs/architecture/index.html#frontend>`_.


^^^^^^^^^^^^
2.3 Producer
^^^^^^^^^^^^

The producer sends data.
Navigate to the ``producer`` directory and create a new file called ``producer.h``.

.. code-block:: cpp

   #ifndef SCORE_PRODUCER_H
   #define SCORE_PRODUCER_H

   #include "score/mw/com/impl/instance_specifier.h"
   #include "src/message_data.h"

   class Producer
   {
     public:
       Producer(const score::mw::com::impl::InstanceSpecifier& instance_specifier);
       ~Producer() = default;

       int RunProducer(const std::chrono::milliseconds cycle_time,
                       const std::size_t num_cycles);

     private:
       score::Result<com_example::IPCInterfaceSkeleton> create_result;
   };

   #endif //SCORE_PRODUCER_H

As you can see, the header is lightweight; we will only need to use the Constructor and ``RunProducer`` from outside.

``create_result`` is our ``IPCInterfaceSkeleton`` specified with the ``instance_specifier`` from our ``score_mw_com.json``.

After that, create the file ``producer.cpp``.


.. code-block:: cpp

   #include "producer.h"
   #include "src/message_data.h"

   Producer::Producer(const score::mw::com::impl::InstanceSpecifier& instance_specifier)
     : create_result(com_example::IPCInterfaceSkeleton::Create(instance_specifier))
   {
   }

   int Producer::RunProducer(const std::chrono::milliseconds cycle_time,
                         const std::size_t num_cycles)
   {
     if (!create_result.has_value())
     {
       std::cerr << "Skeleton was not created. Cannot run producer!\n";
       return EXIT_FAILURE;
     }
     auto& skeleton = create_result.value();

     const auto offer_result = skeleton.OfferService();

     if (!offer_result.has_value())
     {
       std::cerr << "Unable to offer service for skeleton!\n";
       return EXIT_FAILURE;
     }

     std::cout << "Starting to send data\n";

     for (std::size_t cycle = 0U; cycle < num_cycles || num_cycles == 0U; ++cycle)
     {
       auto cycle_message = "Message " + std::to_string(cycle);
       auto message = com_example::Message{.message=cycle_message};
       std::cout << "Sending: " << cycle_message << std::endl;
       skeleton.message_.Send(std::move(message));

       std::this_thread::sleep_for(cycle_time);
     }

     skeleton.StopOfferService();

     return EXIT_SUCCESS;
   }

**What happens in the code:**

The constructor initializes the communication skeleton ``create_result``.

``RunProducer``:

-	checks if the initialization of ``create_result`` was successful
-	offers service
-	enters a loop and sends our messages
-	stops offering the service at the end


^^^^^^^^^^^^
2.4 Consumer
^^^^^^^^^^^^
On the other side, the consumer will consume/receive the data.

Navigate to the ``consumer`` directory and create a new file called ``consumer.h``.

^^^^^^^^^^^^^^
2.5 Next steps
^^^^^^^^^^^^^^
For a complete example implementation, see the example folder

https://github.com/eclipse-score/communication/tree/main/score/mw/com/example/ipc_bridge
