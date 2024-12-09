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
   :id: TOOL_REQ__BAZEL__unified_build_test_integration
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: STKH_REQ__INT_multi_repo_integration
   :status: valid

   Bazel shall be used for building, testing and integrating software.


Process tools
-------------


.. tool_req:: Sphinx-needs for process modelling
   :id: TOOL_REQ__Sphinx-needs__Process_Modelling
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: STKH_REQ__RE_requirements_as_code
   :status: valid

   Spinx-needs shall be used to model all processes within SCORE.
