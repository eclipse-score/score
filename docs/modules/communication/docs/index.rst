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

.. mod:: Communication
   :id: mod__com_communication
   :includes: comp__com_configuration, comp__com_ipc_binding, comp__com_mock_binding, comp__com_frontend

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}
      comp__com_ipc_binding -r[hidden]-> comp__com_frontend
      comp__com_frontend -r[hidden]-> comp__com_mock_binding
      comp__com_mock_binding -r[hidden]-> comp__com_configuration
      logic_arc_int__tracing__tracing -r[hidden]-> logic_arc_int__logging__logging


Module Documents
================

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :glob:

   manual/index.rst
   release/release_note.rst
   safety_mgt/index.rst
   verification/module_verification_report.rst

Requirements
------------

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :glob:

   ./requirements/aou_req.rst
