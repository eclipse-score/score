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

Workproducts Implementation
###########################

.. workproduct:: Implementation
   :id: wp__sw_implementation
   :status: valid
   :tags: safety
   :complies: std_wp__iso26262__software_851, std_wp__iso26262__software_852

   Implementation includes source code and detailed design (e.g. in form of comments or linked graphical representations) and SW configuration (e.g. #ifdef)
   The "how to" is described in the SW Development Plan guidelines

.. workproduct:: Implementation Inspection
   :id: wp__sw_implementation_inspection
   :status: valid
   :tags: safety
   :complies: std_wp__iso26262__software_952

   Github review with integrated inspection checklist, only valid Detailed Design and Code get merged

.. workproduct:: Software Development Plan
   :id: wp__sw_development_plan
   :status: valid
   :tags: safety
   :complies: std_wp__iso26262__software_551, std_wp__iso26262__software_app_c_58

   Process description of SW development including
   - selection of design and programming language
   - design guideline
   - coding guideline (e.g. MISRA, can also include style guide or naming convention)
   - SW configuration guideline
   - Method selection (e.g. for Architecture Verification)
   - development tools

.. needextend:: "docs/process/implementation" in docname
   :+tags: implementation
