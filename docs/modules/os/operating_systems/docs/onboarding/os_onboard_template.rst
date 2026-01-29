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

OS Name
=======

.. os: <os_name>
   :id: os__<os_name name snake case>
   :level: <community/functional/certifiable>
   :maintainer: <GitHub Handles>

Short overview of the platform and why it is relevant for S-CORE.
Keep this to 3-6 lines. Mention what the OS is and the intended usage context.

Target maintainers/integration assistance
-----------------------------------------

GitHub Handles of the target maintainers.


Integration assistance
----------------------

The following fulfills :need:`aou_req__platform__integration_assistance`

- Provide the names or mailing lists that users can contact for help with S‑CORE integration.
- Use bullet points for multiple contacts.


Integration manual
------------------

The following fulfills :need:`aou_req__platform__os_integration_manual`

- Summarise how to obtain and use the integration manual for this platform.
- Link to external documentation if it exists.


Build instructions
------------------

Explain how to build an image of this platform and how to build Eclipse S-CORE for it.

.. code-block:: console

  # example commands to build an image
  curl -o /tmp/image-builder.sh https://example.com/image-builder.sh
  chmod +x /tmp/image-builder.sh
  sudo bash /tmp/image-builder.sh --distro <distro> --target <target>

Provide any additional context, such as how to boot or run the image (e.g. with QEMU).

Toolchain
---------

- Explain how to set up Bazel toolchains for this platform.
- Include a short example ``MODULE.bazel`` snippet.


Bug interface
-------------

The following fulfills :need:`aou_req__platform__bug_interface`

- Explain how users can report bugs (mailing lists, issue trackers, Matrix/Slack channels etc.).
