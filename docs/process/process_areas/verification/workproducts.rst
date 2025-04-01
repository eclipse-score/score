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

.. _verification_work_products:

Verification Work Products
##########################

Platform
********

.. workproduct:: Verification Plan
   :id: wp__verification__plan
   :status: valid
   :complies: std_wp__iso26262__support_951, std_wp__iso26262__support_952, std_wp__iso26262__support_1252

   Verification planning for each phase of the safety lifecycle must detail the work products,
   objectives, methods, criteria, environments, equipment, resources, actions for anomalies, and
   regression strategies, considering method adequacy, complexity, prior experiences, and
   technology maturity or risks.
   This also covers the work product Verification Specification.

.. workproduct:: Platform test
   :id: wp__verification__platform_test
   :status: valid
   :complies: std_wp__iso26262__support_952

   Platform Testing verifies Stakeholder Requirements performed on reference HW.
   Depending on the nature of the project, respective tailoring (e.g. for reduced requirements
   coverage) has to be reflected in the :need:`wp__verification__plan` and :need:`wp__platform_safety_plan`.

.. workproduct:: Platform Verification Report
   :id: wp__verification__platform_ver_report
   :status: valid
   :complies: std_wp__iso26262__software_1053, std_wp__iso26262__support_953, std_wp__iso26262__analysis_752, std_wp__iso26262__analysis_852

   Verification Report contains:

   - List of requirements (stakeholder and feature) and architecture tested by which test
     (can be several levels), passed/failed and completeness verdict, including normal
     operation and failure reactions
   - The list of requirements may also contain other verification methods like "Analysis"
   - Formal evidence about the preformed DFA.
   - Formal evidence about the performed Safety Analyses

Feature
*******

.. workproduct:: Feature Integration test
   :id: wp__verification__feat_int_test
   :status: valid
   :complies: std_wp__iso26262__software_1051, std_wp__iso26262__support_952

   Integration Testing verifies feature requirements and architecture:

   - all interfaces from Static view and
   - all flows from Dynamic View and
   - performance: i.e. RAM and processor usage
     on reference HW

Module
******

.. workproduct:: Module Verification Report
   :id: wp__verification__module_ver_report
   :status: valid
   :complies: std_wp__iso26262__software_952, std_wp__iso26262__software_1053, std_wp__iso26262__support_953, std_wp__iso26262__support_1253, std_wp__iso26262__analysis_752, std_wp__iso26262__analysis_852, std_wp__iso26262__support_1252, std_wp__isopas8926__4526

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
*********

.. workproduct:: Component test
   :id: wp__verification__component_test
   :status: valid
   :complies: std_wp__iso26262__software_1051, std_wp__iso26262__support_952, std_wp__isopas8926__4525

   Component Testing verifies Component Requirements

.. workproduct:: Component Integration test
   :id: wp__verification__comp_int_test
   :status: valid
   :complies: std_wp__iso26262__software_1051, std_wp__iso26262__support_952, std_wp__isopas8926__4525

   Component Integration Testing verifies the detailed design and component architecture:

   - all interfaces from Static view and
   - all flows from Dynamic View
   - integration of units into components based on detailed design

   Performance (i.e. RAM and processor usage) is only tested on reference HW.

.. workproduct:: Unit test
   :id: wp__verification__sw_unit_test
   :status: valid
   :complies: std_wp__iso26262__software_951, std_wp__iso26262__support_952, std_req__iso26262__software_845, std_wp__isopas8926__4525

   Unit testing verifies detailed design (traced to).
   Respective tooling is defined in :need:`wp__platform_mgmt`, :need:`wp__verification__plan` and integrated in CI/Build.
   Unit testing is in responsible of the :need:`rl__contributor` providing the :need:`wp__sw_implementation`.

Inspection
**********

Inspection activities on requirement, architecture and detailed design are handled within these process areas.

The work products are handled within these process areas:

     * :ref:`requirements_engineering` implementing :need:`wp__requirements__inspect`
     * :ref:`arch_design_process` implementing :need:`wp__sw_arch_verification`
     * :ref:`implementation` implementing :need:`wp__sw_implementation_inspection`

Tool Verification
*****************

As part of tool management as supporting function it is handled as follows

     * :ref:`general_concepts_tool_verification` describes implementation of :need:`wp__tool_verification`

It is planned in the :need:`wp__platform_mgmt`
