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

Work products
-------------

Platform
^^^^^^^^

.. workproduct:: Verification Plan
   :id: wp__verification__plan
   :status: valid
   :complies: std_wp__iso26262__support_11, std_wp__iso26262__support_19

   Verification planning for each phase of the safety lifecycle must detail the work products,
   objectives, methods, criteria, environments, equipment, resources, actions for anomalies, and
   regression strategies, considering method adequacy, complexity, prior experiences, and
   technology maturity or risks.

.. workproduct:: Platform test
   :id: wp__verification__platform_test
   :status: valid
   :complies: std_wp__iso26262__support_12

   Platform Testing verfies Stakeholder Requirements performed on reference HW

.. workproduct:: Platform Verification Report
   :id: wp__verification__platform_ver_report
   :status: valid
   :complies: std_wp__iso26262__software_15, std_wp__iso26262__support_13, std_wp__iso26262__analysis_5, std_wp__iso26262__analysis_7

   Verification Report contains:

   - List of requirements (and architecture/detailed design tags) tested by which test
     (can be several levels), passed/failed and completeness verdict, including normal
     operation and failure reactions
   - The list of requirements may also contain other verification methods like "Analysis"
   - Formal evidence about the preformed DFA.
   - Formal evidence about the performed Safety Analyses

Feature
^^^^^^^

.. workproduct:: Feature Integration test
   :id: wp__verification__feat_int_test
   :status: valid
   :complies: std_wp__iso26262__software_13, std_wp__iso26262__support_12

   Integration Testing verifies feature requirements and architecture:

   - all interfaces from Static view and
   - all flows from Dynamic View and
   - performance: i.e. RAM and processor usage
     on reference HW

Module
^^^^^^

.. workproduct:: Module Verification Report
   :id: wp__verification__module_ver_report
   :status: valid
   :complies: std_wp__iso26262__software_12, std_wp__iso26262__software_15, std_wp__iso26262__support_13, std_wp__iso26262__support_20, std_wp__iso26262__analysis_5, std_wp__iso26262__analysis_7, std_wp__iso26262__support_19

   Verification Report contains:

   - List of requirements (and architecture/detailed design tags) tested by which test
     (can be several levels), passed/failed and completeness verdict, including normal
     operation and failure reactions
   - The list of requirements may also contain other verification methods like "Analysis"
   - Structural Coverage (C0 and C1, from unit testing on host) per unit
   - Static Code Analysis (including compiler warnings, automated checking of coding guidelines
     and additional checks)
   - Formal evidence about the preformed DFA.
   - Formal evidence about the performed Safety Analyses
   - Software component qualification verification report

Component
^^^^^^^^^

.. workproduct:: Component test
   :id: wp__verification__component_test
   :status: valid
   :complies: std_wp__iso26262__support_12

   Component Testing verifies Component Requirements

.. workproduct:: Component Integration test
   :id: wp__verification__comp_int_test
   :status: valid
   :complies: std_wp__iso26262__software_13, std_wp__iso26262__support_12

   Integration Testing verifies component architecture:

   - all interfaces from Static view and
   - all flows from Dynamic View and performance: i.e. RAM and processor usage on reference HW

.. workproduct:: Unit test
   :id: wp__verification__sw_unit_test
   :status: valid
   :complies: std_wp__iso26262__software_11, std_wp__iso26262__support_12

   Unit testing verifies component requirements and detailed design (traced to). Tooling defined
   in SW Development Plan and integrated in CI/Build.

Generic
^^^^^^^

.. workproduct:: Verification Specification
   :id: wp__verification__specification
   :status: valid
   :complies: std_wp__iso26262__support_12

   The verification specification must outline the verification methods, including review or
   analysis checklists, simulation scenarios.
   Test cases, test data, and test objects are part of the respective test WPs.

Inspection
^^^^^^^^^^

Inspection is handled in the respective process areas

     * :ref:`requirements_engineering` implementing :need:`wp__requirements__inspect`
     * : ref : ` arch_design_process `
       ``[make proper ref after Arch PR #500 is merged]`` implementing :need:`wp__sw_arch_verification`
     * Detailed design implementing :need:`wp__sw_code_inspect`

Tool Evaluation
^^^^^^^^^^^^^^^

As part of tool qualification as supporting function it is handled as follows

     * :need:`rl__infrastructure_tooling_community` implementing :need:`wp__tool_eval`
