..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
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

.. _comp_doc_os_community_autosd:

Red Hat AutoSD
##############

Overview
--------

AutoSD is the upstream binary distribution that serves as the public, in-development preview and functional precursor
of the Red Hat In-Vehicle Operating System (OS).

AutoSD is downstream of CentOS Stream, so it retains most of the CentOS Stream code with a few divergences,
such as an optimized automotive-specific kernel rather than CentOS Stream's kernel package.

Red Hat In-Vehicle OS is based on both AutoSD and RHEL, both of which are downstreams of CentOS Stream.

Requirements
------------

Integration Assistance
~~~~~~~~~~~~~~~~~~~~~~

The following fulfills :need:`aou_req__platform__integration_assistance`

+----------------+-----------------------------+
| .. centered:: Leonardo Rossetti              |
+----------------+-----------------------------+
| Github Handler | @odra                       |
+----------------+-----------------------------+
| Slack Handler  | @lrossett                   |
+----------------+-----------------------------+


Integration Manual
~~~~~~~~~~~~~~~~~~

The following fulfills :need:`aou_req__platform__os_integration_manual`


Building an Image
^^^^^^^^^^^^^^^^^

Download the wrapper script which runs our automotive-image-builder inside a linux container:

.. code:: bash

    curl -o /tmp/auto-image-builder.sh "https://gitlab.com/CentOS/automotive/src/automotive-image-builder/-/raw/main/auto-image-builder.sh"
    chmod +x /tmp/auto-image-builder.sh

To build an AutoSD image:

.. code:: bash

   sudo bash ./scripts/container-build.sh build \
   --define-file build/vars.yml \
   --build-dir outputs/ \
   --distro autosd9 \
   --mode image \
   --target qemu \
   --export qcow2 \
   build/image.aib.yml \
   outputs/disk.qcow2

If using QEMU, you can run the image using the following command:

.. code:: bash

   /usr/bin/qemu-system-x86_64 \
   -drive file=/usr/share/OVMF/OVMF_CODE_4M.fd,if=pflash,format=raw,unit=0,readonly=on \
   -drive file=/usr/share/OVMF/OVMF_VARS_4M.fd,if=pflash,format=raw,unit=1,snapshot=on,readonly=off \
   -enable-kvm \
   -m 2G \
   -smp $(nproc) \
   -machine q35 \
   -cpu host \
   -device virtio-net-pci,netdev=n0 \
   -netdev user,id=n0,hostfwd=tcp::2222-:22 \
   -daemonize \
   -display none \
   -drive file=disk.qcow2,index=0,media=disk,format=qcow2,if=virtio,id=rootdisk,snapshot=off

Mixed Critical Orchestration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upstream documentation: https://sigs.centos.org/automotive/features-and-concepts/con_mixed-criticality/

Mixed Critical Orchestration, aka MCO, can be achieved with the following components:

* Systemd: the init system that is responsible for workload orchestration
* Eclise BlueChi: extends Systemd to enable multi-node and multi domain orchestration
* QM: Quality management environment that is composed of two sub-systems: a dedicated rootfs partition + container isolation

ASIL and QM connectivity is done either via an IPC socket or shared memory (/dev/shm).

.. image:: _assets/autosd-mco.png
   :align: center

Toolchain
^^^^^^^^^

Upstream documentation: https://github.com/eclipse-score/inc_os_autosd/tree/main/toolchain

A Bazel toolchain defintion is provided for users to build their Bazel modules and components with AutoSD's tooling (compilers, libraries, etc).

Sample usage (MODULE.bazel file):

.. code:: starlark

   # Use local path during development, or git_override for published versions
   local_path_override(
       module_name = "os_autosd",
       path = "/path/to/inc_os_autosd/"
   )
   
   bazel_dep(name = "os_autosd", version = "1.0.0")
   
   # Configure AutoSD 9 GCC toolchain
   autosd_10_gcc = use_extension("@os_autosd//toolchain/autosd_10_gcc:extensions.bzl", "autosd_10_gcc_extension")
   autosd_10_gcc.configure(
       c_flags = ["-Wall", "-Wno-error=deprecated-declarations", "-Werror", "-fPIC"],
       cxx_flags = ["-Wall", "-Wno-error=deprecated-declarations", "-Werror", "-fPIC"],
   )
   
   use_repo(autosd_10_gcc, "autosd_10_gcc_repo")
   register_toolchains("@autosd_10_gcc_repo//:gcc_toolchain_linux_x86_64")

**NOTE:** AutoSD's tooling does not support cross compilation.

Bug Interface
~~~~~~~~~~~~~

The following fulfills :need:`aou_req__platform__bug_interface`

+------------------------------------+---------------------------------------------------------------------------+
|                                                                                                                |
+------------------------------------+---------------------------------------------------------------------------+
| CentOS SIG Automotive Mailing List | https://lists.centos.org/hyperkitty/list/automotive-sig@lists.centos.org/ |
+------------------------------------+---------------------------------------------------------------------------+
| Gitlab Issue Tracker               | https://gitlab.com/CentOS/automotive/sig                                  |
+------------------------------------+---------------------------------------------------------------------------+
| CentOS SIG MAtrix Channel          | https://app.element.io/#/room/#centos-automotive-sig:fedoraproject.org    |
+------------------------------------+---------------------------------------------------------------------------+
| Eclipse SDV Slack Channel          | #autosd (https://sdvworkinggroup.slack.com/archives/C0986LJ9EJH)          |
+------------------------------------+---------------------------------------------------------------------------+
