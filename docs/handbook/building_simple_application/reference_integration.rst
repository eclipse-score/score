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

Reference integration
=======================

.. toctree::
   :maxdepth: 1
   :glob:

After building the scrample binary for the qnx x86 image,
we can now run it inside the reference qnx image for the x86 platform.

The reference integration repository already provides a
`reference qnx image  <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu>`_. 

This image is intentionally minimal and contains only the essential tooling in the
`IFS image <https://www.qnx.com/developers/docs/8.0/com.qnx.doc.neutrino.building/topic/intro/intro_ifs.html>`_.

For more details of the qnx reference image in Eclipse S-CORE, refer to the reference integration
`README.md <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/README.md>`_. 

To create an ifs image, qnx_ifs bazel rule in
`qnx_qemu/build/BUILD <https://github.com/eclipse-score/reference_integration/blob/99618797cb518fe2fac0e5dc53b95718bc675911/qnx_qemu/build/BUILD#L45>`_
file is used:


.. code-block:: python
    
    qnx_ifs(
        name = "init",
        build_file = "init.build",
        srcs = [
            "system.build",
            ":scripts",
            ":configs",
        ],
        visibility = [
            "//:__pkg__"
        ],
    )

The snippet above defines an *ifs image* named *init*. 

The *build_file* attribute points to the `init.build <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/build/init.build>`_
script, which acts as the entry point for the *ifs image*.
It defines the image content and the initial start-up steps. 

For more information, refer to the official `QNX OS Image Build Files <https://www.qnx.com/developers/docs/8.0/com.qnx.doc.neutrino.building/topic/buildfiles/buildfile.html>`_
documentation.

The *init.build* file also includes `system.build <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/build/system.build>`_ file,
which is used - among other things - to deploy local files to the *ifs image*, as shown in the example below for the *dhcp.conf*

.. code-block:: python
    
    # DHCP client configuration
    [perms=644] /etc/dhcpcd.conf = configs/dhcpcd.conf                                     # DHCP client configuration file

This is where we need to add our scrample application binary and its runtime configuration.
Before doing so, we must first add the scrample binary as a dependency of the ifs image.

The first step is to update the `MODULE.bazel <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/MODULE.bazel>`_
file with the dependency to the scrample module and all modules it depends on.

Next, we need to extend `.bazelrc <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/.bazelrc>`_
file with the compiler settings needed to build these modules.

Both steps follow the same pattern described earlier in the :ref:`Building source code <building_source_code>` chapter.
Once all dependencies are set up, we can add our scrample binary as dependency of the *ifs_image* target in the
`qnx_qemu/build/BUILD <https://github.com/eclipse-score/reference_integration/blob/99618797cb518fe2fac0e5dc53b95718bc675911/qnx_qemu/build/BUILD#L45>`_:


.. code-block:: python
    :linenos:
    :emphasize-lines: 8, 9, 12

    qnx_ifs(
        name = "init",
        build_file = "init.build",
        srcs = [
            "system.build",
            ":scripts",
            ":configs",
            "@score_scrample//src:scrample",
            "//scrample_integration:etc_configs",
        ],
        ext_repo_maping = {
            "SCRAMPLE_PATH": "$(location @score_scrample//src:scrample)",
        },
        visibility = [
            "//:__pkg__"
        ],
    )

In lines 8 and 9, we add the dependencies for the *scrample binary* and *scrample runtime config*.

Because the *scrample_binary* target is defined in the scrample bazel module,
we must reference it explicit using the scrample module prefix *@score_scrample*.

The *scrample runtime configuration* is located in *reference_integration* repository and includes
the `IPC services definition file <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/scrample_integration/etc/mw_com_config.json>`_
and `logging config file <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/scrample_integration/etc/logging.json>`_.

As shown in the *scrample runtime config* `BUILD <https://github.com/eclipse-score/reference_integration/blob/701e208bf943fe7ed7bf096f5e2e1c8575ec9b4a/qnx_qemu/scrample_integration/BUILD#L15>`_
file, we use the *bazel* function `export_files <https://bazel.build/reference/be/functions#exports_files>`_
to make files available to the external qnx tool `mkifs <https://www.qnx.com/developers/docs/8.0/com.qnx.doc.neutrino.utilities/topic/m/mkifs.html>`_,
which is triggered by q*nx_ifs()* in the background.

For the same reason, we declare in line 12 the path to the built *scrample binary* as the environment variable *SCRAMPLE_PATH*.
(Remember: all targets from other modules are rebuilt in the context of the current module’s configuration.) 
This allows as to reference the binary during *mkifs* execution.
Finally, we add the scrample artifact to the `system.build file <https://github.com/eclipse-score/reference_integration/blob/main/qnx_qemu/build/system.build#L279>`_ file, as shown below:

.. code-block::

    [perms=777] /etc/logging.json = scrample_integration/etc/logging.json                                     
    [perms=777] /etc/mw_com_config.json = scrample_integration/etc/mw_com_config.json

    [perms=777] /scrample = ${SCRAMPLE_PATH}

This copies the artifacts to their final location in the *ifs image* on the target.
Now we are ready to build the *ifs image*, start qemu and to test our application.
First, we start qemu, which will also build the ifs image in the background.
According to the `QEMU tutorial <https://github.com/eclipse-score/reference_integration/tree/main/qnx_qemu#3-build--run-the-qnx-image-on-qemu>`_
in the *reference integration* repository, run the following command:
 
.. code-block:: python

    bazel run --config=x86_64-qnx //:run_qemu

If everything was successfull, you should see following output:

.. code-block:: python

    [INFO] [QEMU] IP address set to: 169.254.158.190
    [INFO] [QEMU] ---> DHCP configuration completed successfully
    [INFO] [QEMU] ---> Network configuration completed
    [INFO] [QEMU] ---> Setting hostname
    [INFO] [QEMU] Hostname set to: Qnx_S-core
    [INFO] [QEMU] ---> adding /tmp_discovery folder

Now we can run the scrample binary. 
It supports two modes: one for sending data and one for receiving it. 
Start two processes in different modes to let them communicate with each other

.. code-block:: python

    /scrample -n 10 -t 100 -m send & ./scrample -n 5 -t 100 -m recv

You can find the explanation of all command-line arguments in the scrample
`main.cpp <https://github.com/eclipse-score/scrample/blob/aa8a49e9df6ffa8a0b50414eb81c0a82cb1eba04/src/main.cpp#L41>`_ file.
If everything works correctly, you should now see output indicating that the two processes are communicating with each other. 
It should look similar to the following:

.. code-block:: python

    [INFO] [test_scrample] 2025/11/10 07:53:49.1229574 145754 000 ECU1 IPBR lola log info verbose 2 No explicit applicationID configured. Falling back to using process UID.  Ensure unique UIDs for applications using mw::com.
    [INFO] [test_scrample] 2025/11/10 07:53:49.1229574 145754 000 ECU1 IPBR lola log info verbose 2 No explicit applicationID configured. Falling back to using process UID.  Ensure unique UIDs for applications using mw::com.
    [INFO] [test_scrample] 2025/11/10 07:53:49.1229578 145784 000 ECU1 IPBR lola log info verbose 10 Calculated sizes of shm-objects for service_id:instance_id  6432 : 1  are as follows:
    [INFO] [test_scrample] QM-Ctrl:  1736 , ASIL_B-Ctrl:  0 , Data:  109984
    [INFO] [test_scrample] 2025/11/10 07:53:49.1229580 145811 000 ECU1 IPBR lola log info verbose 2 Successfully created offer path /tmp_discovery/mw_com_lola/service_discovery/6432/1
    [INFO] [test_scrample] 2025/11/10 07:53:50.1230079 150796 000 ECU1 IPBR lola log info verbose 2 Successfully created offer path /tmp_discovery/mw_com_lola/service_discovery/6432/1
    [INFO] [test_scrample] score/MapApiLanesStamped: Running as proxy, looking for services
    [INFO] [test_scrample] score/MapApiLanesStamped: Found service, instantiating proxy
    [INFO] [test_scrample] score/MapApiLanesStamped: Subscribing to service
    [INFO] [test_scrample] score/MapApiLanesStamped: Received sample: 4
    [INFO] [test_scrample] score/MapApiLanesStamped: Received sample: 5
    [INFO] [test_scrample] score/MapApiLanesStamped: Proxy received valid data
    [INFO] [test_scrample] score/MapApiLanesStamped: Cycle duration 100ms
    [INFO] [test_scrample] score/MapApiLanesStamped: Received sample: 6
    [INFO] [test_scrample] score/MapApiLanesStamped: Proxy received valid data
    [INFO] [test_scrample] score/MapApiLanesStamped: Cycle duration 100ms
    [INFO] [test_scrample] score/MapApiLanesStamped: Received sample: 7
    [INFO] [test_scrample] score/MapApiLanesStamped: Proxy received valid data
    [INFO] [test_scrample] score/MapApiLanesStamped: Cycle duration 100ms
    [INFO] [test_scrample] score/MapApiLanesStamped: Received sample: 8

By the way, the same workflow is implemented as one of our `integration tests <https://github.com/eclipse-score/reference_integration/blob/701e208bf943fe7ed7bf096f5e2e1c8575ec9b4a/qnx_qemu/test/itf/test_scrample.py#L28>`_,
which you can run with the following command

.. code-block:: python

    bazel test --config=qemu-integration --test_output=streamed //:test_scrample_qemu
