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

.. _tool_requirements:

Tool Requirements
=================


Integration tools
-----------------


.. tool_req:: Bazel for unified build, test and integration
   :id: tool_req__tool__bazel_build
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__integration__multi_repo
   :status: valid

   Bazel shall be used for building, testing and integrating software.


Process tools
-------------


.. tool_req:: Sphinx-needs for process modelling
   :id: tool_req__tool__sphinx_needs_process
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__requirements__as_code
   :status: valid

   Spinx-needs shall be used to model all processes within S-CORE.


.. tool_req:: PlantUML Theming
   :id: tool_req__tool__sphinx_needs_theming
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__requirements__as_code
   :status: valid

   The PlantUML theming feature shall support a consistent *look-and-feel* for all diagrams.
   Details and Instructions are described in document :need:`doc__plantuml_theming`.
   A brief example is shown below.

   .. needarch::
      :scale: 50
      :align: center
      :config: score_config

      Alice -> Bob: Hi Bob
      Bob --> Alice: hi Alice
