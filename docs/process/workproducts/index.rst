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

Workproducts
============


.. figure:: _assets/wp_traceability_model.drawio.svg
  :width: 100%
  :align: center
  :alt: Project work product traceability model
  :name: wp_traceability_model

  Project development work product traceability model


Platform management
--------------------

General
^^^^^^^

.. workproduct:: Policies
   :id: wp__policies
   :status: draft
   :tags: requirements_management
   :complies: std_wp__iso26262__management_551

   Policies for functional safety and cybersecurity.

.. workproduct:: Training path
   :id: wp__training_path
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__management_552

   Trainings for safety and security for S-CORE

.. workproduct:: Quality management plan
   :id: wp__qms
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__management_553

   Quality management process descriptions and definitions

.. workproduct:: Quality report
   :id: wp__qms_report
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__management_553

   | Evidence of quality conformance:
   | * Identifies what tasks/activities/process produce the information
   | * Identifies when the data was collected
   | * Identifies source of any associated data
   | * Identifies the associated quality criteria
   | * Identifies any associated measurements using the information

Process
^^^^^^^

.. workproduct:: Process Definition
   :id: wp__process_definition
   :status: draft
   :tags: process

   Process definitions.

.. workproduct:: Process Improvement Report
   :id: wp__process_impr_report
   :status: draft
   :tags: process

   Process improvement report.

.. workproduct:: Process Management Strategy
   :id: wp__process_plan
   :status: draft
   :tags: process

   Plan to manage and guide execution of the process management activities.


Product development
-------------------

Platform development
^^^^^^^^^^^^^^^^^^^^

.. workproduct:: Feature Safety Analysis
   :id: wp__feature_safety_analysis
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752

   Bottom-Up Safety Analysis with e.g. FMEA method, verifies the feature architecture (as part of SW Safety Concept)
   - Detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use

.. workproduct:: Feature DFA
   :id: wp__feature_dfa
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753

   Dependent Failure Analysis on platform/feature level
   - Detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use
   Perform analysis on interactions between safety related and non-safety related modules or modules with different ASIL of one feature. Including potential influences from the rest of the SW platform.

.. workproduct:: Platform Build Configuration
   :id: wp__platform_sw_build_config
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__software_1052

   Build configuration capable to create the SEooC Library for the reference HW, platform level.
   Note: Embedded software in the sense of the Iso (i.e. deployed on the production HW) is not part of our delivery.

.. workproduct:: Platform Release Notes
   :id: wp__platform_sw_release_note
   :status: draft
   :tags: safety_management
   :complies: std_wp__iso26262__management_656

   Release notes describe the qualified SW version including known bugs from own testing and field reporting, with clear statement, that these bugs do not lead to violation of any safety requirements or with corresponding workaround measures. Platform level.

.. workproduct:: Hardware-software interface document
   :id: wp__hsi
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__software_652, std_wp__isopas8926__4522

   | The document shall specify the hardware and software interaction and be consistent with the safety concept.
   | It shall include the platform's hardware parts that are controlled by software and hardware resources that support the execution of the software.


Component development
^^^^^^^^^^^^^^^^^^^^^

.. workproduct:: Component Safety Analysis
   :id: wp__sw_component_safety_analysis
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__analysis_851, std_wp__iso26262__software_752, std_wp__isopas8926__4524

   Bottom-Up Safety Analysis with e.g. FMEA method, verifies the component architecture (as part of SW Safety Concept)
   - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use

.. workproduct:: Component DFA
   :id: wp__sw_component_dfa
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__analysis_751, std_wp__iso26262__software_753

   Dependent Failure Analysis on component/module level
   - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use
   Perform analysis of safety related and non-safety related sub-elements or sub-elements with different ASIL.
   Perform analysis on interactions between safety related and non-safety related sub-components or sub-components with different ASIL of one component. Including potential influences from the other components in the component's module.

.. workproduct:: Architecture Verification
   :id: wp__sw_arch_verification
   :status: draft
   :complies: std_wp__iso26262__software_754

   Depends on architecture, FMEA and DFA tooling.
   May include several methods like inspection, modelling ... Which are selected in SW Development Plan.

.. workproduct:: Module Build Configuration
   :id: wp__module_sw_build_config
   :status: draft
   :tags: safety
   :complies: std_wp__iso26262__software_1052

   Build configuration capable to create the SEooC Library for the reference HW, module level.
   Note: Embedded software in the sense of the Iso (i.e. deployed on the production HW) is not part of our delivery.

.. workproduct:: Module Release Notes
   :id: wp__module_sw_release_note
   :status: draft
   :tags: safety_management
   :complies: std_wp__iso26262__management_656

   Release notes describe the qualified SW version including known bugs from own testing and field reporting, with clear statement, that these bugs do not lead to violation of any safety requirements or with corresponding workaround measures. Module level.


Supporting activities
---------------------

.. workproduct:: Tool Verification Report
   :id: wp__tool_verification
   :status: draft
   :tags: process, safety, security
   :complies: std_wp__iso26262__support_1151, std_wp__iso26262__support_1152

   According to the safety tool process, each tool's confidence level (TCL) must be determined. Based on TCL the appropriate qualification methods shall be applied.


Note: All the work products in this list are set to status "draft", as their producing workflows are not final and complete.


S-CORE Workproduct Linkage
--------------------------

.. needpie:: S-CORE workproducts contained in exactly one S-CORE workflow
   :labels: Not-Linked, Linked Workproduct, Linked Workproduct To Multiple Workflows
   :legend:
   :colors: red, green, blue
   :filter-func: score_metamodel.checks.standards.my_pie_workproducts_contained_in_exactly_one_workflow
