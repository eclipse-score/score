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

   Organization-specific rules and processes for functional safety and cybersecurity.

.. workproduct:: Training path
   :id: wp__training_path
   :status: draft
   :tags: safety

   Evidence of competence management.

.. workproduct:: Quality management system
   :id: wp__qms
   :status: draft
   :tags: safety

   Evidence of quality management.

.. workproduct:: Quality report
   :id: wp__qms_report
   :status: draft
   :tags: safety

   | Evidence of quality conformance:
   | * Identifies what tasks/activities/process produce the information
   | * Identifies when the data was collected
   | * Identifies source of any associated data
   | * Identifies the associated quality criteria
   | * Identifies any associated measurements using the information

.. workproduct:: Issue tracking system
   :id: wp__issue_track_system
   :status: draft
   :tags: requirements_management, safety_management

   | - Identified safety anomaly reports
   | - Change requests (= Contribution Request)
   | - Impact analysis
   | - change request plan
   | - Change report
   |
   | Safety anomaly: Conditions that deviate from expectations and that can lead to harm.
   | The documentation of a change shall contain the list of changed work products, the details of the change and the planned date of deployment of the change.

.. workproduct:: Feature Request
   :id: wp__feat_request
   :status: draft
   :tags: contribution_management, safety_management

   | - Feature request
   | - Change request

.. workproduct:: Platform Management Plan
   :id: wp__platform_mgmt
   :status: valid
   :complies: std_wp__iso26262__support_6, std_wp__iso26262__support_7, std_wp__iso26262__support_14, std_wp__iso26262__support_15

   The Platform Management Plan shall include the Project Management Plan, Configuration Management Plan, Change Management Plan, Documentation Management Plan and Problem Resolution Plan.
   Plan to ensure that all work products can be uniquely identified and reproduced in a controlled manner at any time.
   Plan to ensure that relations and differences between versions can be traced.
   Plan to manage, analyse and control changes of the work products during the project life cycle.
   Documents should be precise, concise, clearly structured, understandable for intended users, verifiable, maintainable, and organized according to in-house procedures to facilitate information retrieval.
   Documentation guideline requirements must be defined for each WP. Each work product or document must include a title, author and approver, unique revision identification, change history, and status.

.. workproduct:: Software Development Plan
   :id: wp__sw_dev_plan
   :status: draft
   :tags: process

   | Process description of SW development including
   | - selection of design and programming language
   | - design guideline
   | - coding guideline (e.g. MISRA, can also include style guide or naming convention)
   | - SW configuration guideline
   | - Method selection (e.g. for Architecture Verification)
   | - development tools
   |
   | Compare also `Gitub documentation <https://docs.github.com/en>`_
   | Compare also `Eclipse Project Handbook <https://www.eclipse.org/projects/handbook/>`_


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


.. workproduct:: Feature Architecture
   :id: wp__feature_architecture
   :status: draft
   :tags: safety

   Feature Architecture linked to Feature Requirements, i.e. interaction of components
   - Static view (UML) - Feature interfaces (to outside of Feature) and Interfaces between own Components
   - Dynamic view (UML) - Sequences of component interactions and state diagrams

   Technical concept on platform level.

.. workproduct:: Feature Safety Analyses
   :id: wp__feature_safety_analyses
   :status: draft
   :tags: safety

   Bottom-Up Safety Analysis with e.g. FMEA method, verifies the feature architecture (as part of SW Safety Concept)
   - Detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use

.. workproduct:: Feature DFA
   :id: wp__feature_dfa
   :status: draft
   :tags: safety

   Dependent Failure Analysis on platform/feature level
   - Detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use
   Perform analysis on interactions between safety related and non-safety related modules or modules with different ASIL of one feature. Including potential influences from the rest of the SW platform.

.. workproduct:: Platform Build Configuration
   :id: wp__platform_sw_build_config
   :status: draft
   :tags: safety

   Build configuration capable to create the SEooC Library for the reference HW, platform level.
   Note: Embedded software in the sense of the Iso (i.e. deployed on the production HW) is not part of our delivery.

.. workproduct:: Platform Release Notes
   :id: wp__platform_sw_release_note
   :status: draft
   :tags: safety_management

   Release notes describe the qualified SW version including known bugs from own testing and field reporting, with clear statement, that these bugs do not lead to violation of any safety requirements or with corresponding workaround measures. Platform level.


Component development
^^^^^^^^^^^^^^^^^^^^^

.. workproduct:: Hardware-software interface (HSI) specification
   :id: wp__hsi
   :status: draft
   :tags: safety

   | The HSI specification shall specify the hardware and software interaction and be consistent with the technical safety concept.
   | The HSI specification shall include the component's hardware parts that are controlled by software and hardware resources that support the execution of the software.

.. workproduct:: Component Architecture
   :id: wp__sw_component_architecture
   :status: draft
   :tags: safety

   Component Architecture linked to Component Requirements
   - Static view (UML) - Component interfaces (to outside of Component) and Interfaces between own Sub-Components
   - Dynamic view (UML) - Sequences of Sub-Components interactions and Components States
   Note: In case no sub-components exist, this can be covered by Detailed Design (in "Implementation" workproduct)

.. workproduct:: Component Safety Analyses
   :id: wp__sw_component_safety_analyses
   :status: draft
   :tags: safety

   Bottom-Up Safety Analysis with e.g. FMEA method, verifies the component architecture (as part of SW Safety Concept)
   - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use

.. workproduct:: Component DFA
   :id: wp__sw_component_dfa
   :status: draft
   :tags: safety

   Dependent Failure Analysis on component/module level
   - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use
   Perform analysis of safety related and non-safety related sub-elements or sub-elements with different ASIL.
   Perform analysis on interactions between safety related and non-safety related sub-components or sub-components with different ASIL of one component. Including potential influences from the other components in the component's module.

.. workproduct:: Architecture Verification
   :id: wp__sw_arch_verification
   :status: draft
   :complies: std_wp__iso26262__software_8

   Depends on architecture, FMEA and DFA tooling.
   May include several methods like inspection, modelling ... Which are selected in SW Development Plan.

.. workproduct:: Implementation
   :id: wp__sw_implementation
   :status: draft
   :tags: safety

   Implementation includes source code and detailed design (e.g. in form of comments or linked graphical representations) and SW configuration (e.g. #ifdef)
   The "how to" is described in the SW Development Plan guidelines

.. workproduct:: Code Inspection
   :id: wp__sw_code_inspect
   :status: draft
   :complies: std_wp__iso26262__software_12

   github review with integrated inspection checklist (includes manual checking of coding guidelines)

.. workproduct:: Module Build Configuration
   :id: wp__module_sw_build_config
   :status: draft
   :tags: safety

   Build configuration capable to create the SEooC Library for the reference HW, module level.
   Note: Embedded software in the sense of the Iso (i.e. deployed on the production HW) is not part of our delivery.

.. workproduct:: Module Release Notes
   :id: wp__module_sw_release_note
   :status: draft
   :tags: safety_management

   Release notes describe the qualified SW version including known bugs from own testing and field reporting, with clear statement, that these bugs do not lead to violation of any safety requirements or with corresponding workaround measures. Module level.


Supporting activities
---------------------

.. workproduct:: Software tool criteria evaluation report
   :id: wp__tool_eval
   :status: draft
   :tags: process, safety

   According to the tool evaluation process, each tool's confidence level (TCL) must be determined. Based on TCL the appropriate qualification methods shall be applied.


Note: All the work products are set to status "draft", as the linkage to standard requirements is missing currently on purpose, namely to those of ISO 26262.
