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



.. mod_view_sta:: OS
   :id: mod_view_sta__os__os
   :includes: comp__os_libc, comp__os_message_passing

   The module "OS" is not a part of the S-CORE SW-Platform, but it is a crucial external SW element.
   Its components are modelled in S-CORE to be able to describe dependencies of S-CORE features to
   this external component.
   As it is external to S-CORE, the (folder/file) structure of the documentation may be different from the other modules.
   Its main content is the POSIX operating system environment (sometimes also already called a "SW platform").
   But also other SW components are modelled as a part of it as these are often provided by the "OS" supplier.
   One example of these "other" SW components are the C/C++ libs which may come from a processor manufacturer instead.
   S-CORE expects to support integration of more than one operating system, so these may be seen already in this module view,
   as different components.

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

Module Documents
================

.. toctree::
   :maxdepth: 2
   :titlesonly:

   requirements/index.rst
   requirements/aou_req.rst
