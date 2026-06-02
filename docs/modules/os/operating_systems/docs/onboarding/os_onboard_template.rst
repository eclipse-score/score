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

.. document:: [OS Name]
   :id: doc__os_onboarding
   :status: draft
   :safety: QM
   :security: YES
   :realizes: wp__feature_arch
   :tags: template

The following component needs to be defined at the top of the page (modify accordingly):

.. code-block:: rst

   .. comp:: [OS Name]
     :id: comp__os_[os_name]
     :security: [YES|NO]
     :safety: [QM|ASIL_B]
     :status: valid
     :implements: aou_req__platform__integration_assistance, aou_req__platform__os_integration_manual, aou_req__platform__bug_interface

Short overview of the operating system and why it is relevant for S-CORE.
Keep this to 3-6 lines. Mention what the OS is and the intended usage context.

Target Maintainers/Integration Assistance
-----------------------------------------

GitHub Handles of the target maintainers.


Integration Assistance
----------------------

The following fulfills :need:`aou_req__platform__integration_assistance`

- Provide the names or mailing lists that users can contact for help with S‑CORE integration.
- Use bullet points for multiple contacts.


Integration Manual
------------------

The following fulfills :need:`aou_req__platform__os_integration_manual`

- Summarise how to obtain and use the integration manual for this operaring system.
- Link to external documentation if it exists.

Supported Architectures
-----------------------

+-----------------------+--------------------------------+
| Target Architecture   | Comments                       |
+-----------------------+--------------------------------+
| <target_arch>         | <Native Only, Cross Compile>   |
+-----------------------+--------------------------------+


Build Instructions
------------------

Explain how to build an image (or how to retrieve a pre-built one) of this OS and how to build Eclipse S-CORE for it.

Provide any architecture specific details based on the architecture table.

.. code-block:: console

  # example commands to build an image
  curl -o /tmp/image-builder.sh https://example.com/image-builder.sh
  chmod +x /tmp/image-builder.sh
  sudo bash /tmp/image-builder.sh --distro <distro> --target <target>

Provide any additional context, such as how to boot or run the image (e.g. with QEMU), supported architectures, etc.

Describe any additional distinctions that need to be made based on the "Supported Architectures" section.

Toolchain
---------

- Any details worth mentioning
- Provide any architecture specific details based on the architecture table.
- Explain how to set up Bazel toolchains for this OS.
- Include a short example ``MODULE.bazel`` snippet.
- Describe any additional distinctions that need to be made based on the "Supported Architectures" section.

Bug Interface
-------------

The following fulfills :need:`aou_req__platform__bug_interface`

- Explain how users can report bugs (mailing lists, issue trackers, Matrix/Slack channels etc.).
