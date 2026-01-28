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

.. mod:: Baselibs
   :id: mod__baselibs
   :includes: comp__baselibs_json, comp__baselibs_message_passing, comp__baselibs_memory_shared, comp__baselibs_result, comp__baselibs_bit_manipulation, comp__baselibs_containers, comp__baselibs_filesystem, comp__baselibs_utils, comp__baselibs_concurrency
   :status: valid
   :safety: ASIL_B
   :security: YES

.. mod_view_sta:: Baselibs Static View
   :id: mod_view_sta__baselibs__baselibs
   :includes: comp__baselibs_json, comp__baselibs_message_passing, comp__baselibs_memory_shared, comp__baselibs_result, comp__baselibs_bit_manipulation, comp__baselibs_containers, comp__baselibs_filesystem, comp__baselibs_utils, comp__baselibs_concurrency

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}

.. _baselibs_module_docs:

Module Documents
================

.. toctree::
   :maxdepth: 1
   :glob:

   manual/index.rst
   safety_mgt/index.rst
   verification/module_verification_report.rst
   release/release_note.rst
