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

Workproducts
============


.. _wp_traceability_model:

.. figure:: _assets/wp_traceability_model.drawio.svg
  :width: 100%
  :align: center
  :alt: Project work product traceability model

  Project development work product traceability model


Platform management
--------------------

General
^^^^^^^

.. workproduct:: Policies
   :id: WP_POLICIES
   :status: draft
   :tags: requirements_management

   Organization-specific rules and processes for functional safety and cybersecurity.

.. workproduct:: Training path
   :id: WP_TRAINING_PATH
   :status: draft
   :tags: safety

   Evidence of competence management.

.. workproduct:: Quality management system
   :id: WP_QMS
   :status: draft
   :tags: safety

   Evidence of quality management.

.. workproduct:: Quality report
   :id: WP_QMS_REPORT
   :status: draft
   :tags: safety

   | Evidence of quality conformance:
   | * Identifies what tasks/activities/process produce the information
   | * Identifies when the data was collected
   | * Identifies source of any associated data
   | * Identifies the associated quality criteria
   | * Identifies any associated measurements using the information

.. workproduct:: Issue tracking system
   :id: WP_ISSUE_TRACK_SYSTEM
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
   :id: WP_FEAT_REQUEST
   :status: draft
   :tags: contribution_management, safety_management

   | - Feature request
   | - Change request

.. workproduct:: Platform Management Plan
   :id: WP_PLATFORM_MGMT
   :status: draft
   :tags: safety_management

   The Platform Management Plan shall include the Project Management Plan, Configuration Management Plan, Change Management Plan, Documentation Management Plan and Problem Resolution Plan.
   Plan to ensure that all work products can be uniquely identified and reproduced in a controlled manner at any time.
   Plan to ensure that relations and differences between versions can be traced.
   Plan to manage, analyse and control changes of the work products during the project life cycle.
   Documents should be precise, concise, clearly structured, understandable for intended users, verifiable, maintainable, and organized according to in-house procedures to facilitate information retrieval.
   Documentation guideline requirements must be defined for each WP. Each work product or document must include a title, author and approver, unique revision identification, change history, and status.

.. workproduct:: Software Development Plan
   :id: WP_SW_DEV_PLAN
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
   :id: WP_PROCESS_DEFINITION
   :status: draft
   :tags: process

   Process definitions.

.. workproduct:: Process Improvement Report
   :id: WP_PROCESS_IMPR_REPORT
   :status: draft
   :tags: process

   Process improvement report.

.. workproduct:: Process Management Strategy
   :id: WP_PROCESS_PLAN
   :status: draft
   :tags: process

   Plan to manage and guide execution of the process management activities.

Safety
^^^^^^

.. workproduct:: Platform Safety Plan
   :id: WP_PLATFORM_SAFETY_PLAN
   :status: draft
   :tags: safety_management

   Plan to manage and guide the execution of the safety activities of a project including dates, milestones, tasks, deliverables, responsibilities (including the Safety Manager appointment)  and resources.
   Guidelines on how an impact analysis shall be concluded on each item or element involved together with it's connected items or elements.
   This is on following level:
   - Project/Platform (contains definitions how safety planning is performed generally in the project)

.. workproduct:: Module Safety Plan
   :id: WP_MODULE_SAFETY_PLAN
   :status: draft
   :tags: safety_management

   Plan to manage and guide the execution of the safety activities of a project including dates, milestones, tasks, deliverables, responsibilities (including the Safety Manager appointment) and resources.
   Guidelines on how an impact analysis shall be concluded on each item or element involved together with it's connected items or elements.
   This is on following level:
   - Project/Platform (contains definitions how safety planning is performed generally in the project)
   - Module (contains activities planning based on a Contribution Request)

.. workproduct:: Platform Safety Case
   :id: WP_PLATFORM_SAFETY_CASE
   :status: draft
   :tags: safety_management

   Argument that functional safety is achieved for items, or elements, and satisfied by evidence compiled from work products of activities during development. For Platform SEooC.

.. workproduct:: Module Safety Case
   :id: WP_MODULE_SAFETY_CASE
   :status: draft
   :tags: safety_management

   Argument that functional safety is achieved for items, or elements, and satisfied by evidence compiled from work products of activities during development. For Module SEooC.


.. workproduct:: Confirmation Review Reports
   :id: WP_CMR_REPORTS
   :status: draft
   :tags: safety

   Confirmation that a work product provides sufficient and convincing evidence of their contribution to the achievement of functional safety considering the corresponding objectives and requirements of ISO 26262.
   Will contain confirmation review report for Safety Plan, Safety Case, Safety Analyses and Dependent Failure Analyses (DFA)

.. workproduct:: Functional Safety Assessment Report
   :id: WP_ASSESSMENT_REPORT
   :status: draft
   :tags: safety

   Examination of whether a characteristic of a component achieves the ISO 26262 objectives and examination of an implemented process with regard to the process objectives.


Product development
-------------------

Platform development
^^^^^^^^^^^^^^^^^^^^

.. workproduct:: Stakeholder Requirements
   :id: WP_STAKEHOLDER_REQ
   :status: draft
   :tags: requirements_management

   Technical requirements from a stakeholder viewpoint and Assumptions of use based on the integration as SW platform SEooC in an assumed context.

.. workproduct:: Tool Requirements
   :id: WP_TOOL_REQ
   :status: draft
   :tags: requirements_management

   SW Requirements for tools to ensure automatic enforcement of rules and as input for software tool qualification.

.. workproduct:: Feature Requirements
   :id: WP_FEATURE_REQ
   :status: draft
   :tags: requirements_management

   SW Requirements describing in a more detailed way the functionality which will fulfill a set of stakeholder requirements. A "feature" consists of a set of requirements. These feature requirements shall also be the basis for integration testing on platform level.

.. workproduct:: Feature Assumptions of Use
   :id: WP_FEATURE_AOU
   :status: draft
   :tags: safety

   SW Safety Requirements for the user of the feature, exportable requirements for the user to integrate in their req mgt system.

.. workproduct:: Platform Safety Manual
   :id: WP_PLATFORM_SW_SAFETY_MANUAL
   :status: draft
   :tags: safety

   The safety manual exists for every SEooC/qualified component. It describes:
   - The Assumed Platform Requirements (Safety related);
   - the safety concept of the SEooC (i.e. which faults are taken care of);
   - the Assumptions of Use (of the features);
   - a link to the user manual;
   - the reactions of the implemented functions under anomalous operating conditions; and
   - a description of known anomalies with corresponding workaround measures.
   This is on platform level.

.. workproduct:: Feature Architecture
   :id: WP_FEATURE_ARCHITECTURE
   :status: draft
   :tags: safety

   Feature Architecture linked to Feature Requirements, i.e. interaction of components
   - Static view (UML) - Feature interfaces (to outside of Feature) and Interfaces between own Components
   - Dynamic view (UML) - Sequences of component interactions and state diagrams

   Technical concept on platform level.

.. workproduct:: Feature Safety Analyses
   :id: WP_FEATURE_SAFETY_ANALYSES
   :status: draft
   :tags: safety

   Bottom-Up Safety Analysis with e.g. FMEA method, verifies the feature architecture (as part of SW Safety Concept)
   - Detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use

.. workproduct:: Feature DFA
   :id: WP_FEATURE_DFA
   :status: draft
   :tags: safety

   Dependent Failure Analysis on platform/feature level
   - Detection and prevention mitigations linked to Software Feature Requirements or Assumptions of Use
   Perform analysis on interactions between safety related and non-safety related modules or modules with different ASIL of one feature. Including potential influences from the rest of the SW platform.

.. workproduct:: Platform Build Configuration
   :id: WP_PLATFORM_SW_BUILD_CONFIG
   :status: draft
   :tags: safety

   Build configuration capable to create the SEooC Library for the reference HW, platform level.
   Note: Embedded software in the sense of the Iso (i.e. deployed on the production HW) is not part of our delivery.

.. workproduct:: Feature Integration test
   :id: WP_FEATURE_INTEGRATION_TEST
   :status: draft
   :tags: safety

   Integration Testing verifies feature requirements and architecture:
   - all interfaces from Static view and
   - all flows from Dynamic View and
   - performance: i.e. RAM and processor usage
   on reference HW

.. workproduct:: Platform test
   :id: WP_PLATFORM_TEST
   :status: draft
   :tags: safety

   Platform Testing verfies Stakeholder Requirements performed on reference HW

.. workproduct:: Platform Verification Report
   :id: WP_PLATFORM_SW_VERIFICATION_REPORT
   :status: draft
   :tags: safety

   Verification Report contains:
   - List of requirements (and architecture/detailed design tags) tested by which test (can be several levels), passed/failed and completeness verdict, including normal operation and failure reactions
   - The list of requirements may also contain other verification methods like "Analysis"
   - Formal evidence about the preformed DFA.
   - Formal evidence about the performed Safety Analyses

.. workproduct:: Platform Release Notes
   :id: WP_PLATFORM_SW_RELEASE_NOTE
   :status: draft
   :tags: safety_management

   Release notes describe the qualified SW version including known bugs from own testing and field reporting, with clear statement, that these bugs do not lead to violation of any safety requirements or with corresponding workaround measures. Platform level.


Component development
^^^^^^^^^^^^^^^^^^^^^

.. workproduct:: Component Requirements
   :id: WP_SW_COMPONENT_REQ
   :status: draft
   :tags: requirements_management

   | SW Requirements for own and OSS qualified components/libraries. QM and ASIL requirements are distinguished by attributes/tags.

.. workproduct:: Component Assumptions of Use
   :id: WP_SW_COMPONENT_AOU
   :status: draft
   :tags: safety

   SW Safety Requirements for the user of the component, exportable requirements for the user to integrate in their req mgt system.

.. workproduct:: Module Safety Manual
   :id: WP_MODULE_SW_SAFETY_MANUAL
   :status: draft
   :tags: safety

   The safety manual exists for every SEooC/qualified component. It describes:
   - The Assumed Platform Requirements (Safety related);
   - the safety concept of the SEooC (i.e. which faults are taken care of);
   - the Assumptions of Use (of the modules's components);
   - a link to the user manual;
   - the reactions of the implemented functions under anomalous operating conditions; and
   - a description of known anomalies with corresponding workaround measures.
   This is on module level.

.. workproduct:: Hardware-software interface (HSI) specification
   :id: WP_HSI
   :status: draft
   :tags: safety

   | The HSI specification shall specify the hardware and software interaction and be consistent with the technical safety concept.
   | The HSI specification shall include the component's hardware parts that are controlled by software and hardware resources that support the execution of the software.

.. workproduct:: Requirements Inspection
   :id: WP_SW_REQ_INSPECT
   :status: draft
   :tags: safety

   | Depends on requirements management tooling, expect text based requirements maintained in git.
   | - github review with integrated inspection checklist, only valid requirements get merged
   |
   | Compare also `Gitub documentationt <https://docs.github.com/en>`_

.. workproduct:: Component Architecture
   :id: WP_SW_COMPONENT_ARCHITECTURE
   :status: draft
   :tags: safety

   Component Architecture linked to Component Requirements
   - Static view (UML) - Component interfaces (to outside of Component) and Interfaces between own Sub-Components
   - Dynamic view (UML) - Sequences of Sub-Components interactions and Components States
   Note: In case no sub-components exist, this can be covered by Detailed Design (in "Implementation" workproduct)

.. workproduct:: Component Safety Analyses
   :id: WP_SW_COMPONENT_SAFETY_ANALYSES
   :status: draft
   :tags: safety

   Bottom-Up Safety Analysis with e.g. FMEA method, verifies the component architecture (as part of SW Safety Concept)
   - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use

.. workproduct:: Component DFA
   :id: WP_SW_COMPONENT_DFA
   :status: draft
   :tags: safety

   Dependent Failure Analysis on component/module level
   - Detection and prevention mitigations linked to Software Component Requirements or Assumptions of Use
   Perform analysis of safety related and non-safety related sub-elements or sub-elements with different ASIL.
   Perform analysis on interactions between safety related and non-safety related sub-components or sub-components with different ASIL of one component. Including potential influences from the other components in the component's module.

.. workproduct:: Architecture Verification
   :id: WP_SW_ARCH_VERIFICATION
   :status: draft
   :tags: safety

   Depends on architecture, FMEA and DFA tooling.
   May include several methods like inspection, modelling ... Which are selected in SW Development Plan.

.. workproduct:: Implementation
   :id: WP_SW_IMPLEMENTATION
   :status: draft
   :tags: safety

   Implementation includes source code and detailed design (e.g. in form of comments or linked graphical representations) and SW configuration (e.g. #ifdef)
   The "how to" is described in the SW Development Plan guidelines

.. workproduct:: Unit test
   :id: WP_SW_UNIT_TEST
   :status: draft
   :tags: safety

   Unit testing verifies component requirements and detailed design (traced to). Tooling defined in SW Development Plan and integrated in CI/Build.

.. workproduct:: Code Inspection
   :id: WP_SW_CODE_INSPECT
   :status: draft
   :tags: safety

   github review with integrated inspection checklist (includes manual checking of coding guidelines)

.. workproduct:: Module Verification Report
   :id: WP_MODULE_SW_VERIFICATION_REPORT
   :status: draft
   :tags: safety

   Verification Report contains:
   - List of requirements (and architecture/detailed design tags) tested by which test (can be several levels), passed/failed and completeness verdict, including normal operation and failure reactions
   - The list of requirements may also contain other verification methods like "Analysis"
   - Structural Coverage (C0 and C1, from unit testing on host) per unit
   - Static Code Analysis (including compiler warnings, automated checking of coding guidelines and additional checks)
   - Formal evidence about the preformed DFA.
   - Formal evidence about the performed Safety Analyses
   - Software component qualification verification report

.. workproduct:: Component Integration test
   :id: WP_SW_COMPONENT_INTEGRATION_TEST
   :status: draft
   :tags: safety

   Integration Testing verifies component architecture:
   - all interfaces from Static view and
   - all flows from Dynamic View and
   performance: i.e. RAM and processor usage on reference HW

.. workproduct:: Module Build Configuration
   :id: WP_MODULE_SW_BUILD_CONFIG
   :status: draft
   :tags: safety

   Build configuration capable to create the SEooC Library for the reference HW, module level.
   Note: Embedded software in the sense of the Iso (i.e. deployed on the production HW) is not part of our delivery.

.. workproduct:: Module Release Notes
   :id: WP_MODULE_SW_RELEASE_NOTE
   :status: draft
   :tags: safety_management

   Release notes describe the qualified SW version including known bugs from own testing and field reporting, with clear statement, that these bugs do not lead to violation of any safety requirements or with corresponding workaround measures. Module level.


.. workproduct:: Component test
   :id: WP_SW_COMPONENT_TEST
   :status: draft
   :tags: safety

   Component Testing verifies Component Requirements

.. workproduct:: Software component classification
   :id: WP_SW_COMPONENT_CLASS
   :status: draft
   :tags: process, safety

   The classification shall include:
   - the unique identification of the pre-developed software component;
   - the maximum ASIL of the safety requirements allocated to it;
   - a development processes analysis; and
   - a complexity analysis of the pre-developed SW component; and
   - finally a SW component classification as input for the safety planning (which is to cover the determined gaps, if any, by additional verification measures).


Supporting activities
---------------------

.. workproduct:: Verification Plan
   :id: WP_VERIFICATION_PLAN
   :status: draft
   :tags: process, safety

   Verification planning for each phase of the safety lifecycle must detail the work products, objectives, methods, criteria, environments, equipment, resources, actions for anomalies, and regression strategies, considering method adequacy, complexity, prior experiences, and technology maturity or risks.

.. workproduct:: Verification Specification
   :id: WP_VERIFICATION_SPEC
   :status: draft
   :tags: process, safety

   The verification specification must outline the verification methods, including review or analysis checklists, simulation scenarios.
   Test cases, test data, and test objects are part of the respective test WPs.

.. workproduct:: Software tool criteria evaluation report
   :id: WP_TOOL_EVAL
   :status: draft
   :tags: process, safety

   According to the tool evaluation process, each tool's confidence level (TCL) must be determined. Based on TCL the appropriate qualification methods shall be applied.


Tailoring
---------

.. workproduct:: Tailoring Documents
   :id: WP_TAILORING
   :status: draft
   :tags: process

   This workproduct argues why some workproducts are not needed in the project.
   It may have several levels:
   - Project/Platform
   - Feature/Component
   It belongs to the Safety Plan.

Note: All the work products are set to status "draft", as the linkage to standard requirements is missing currently on purpose, namely to those of ISO 26262.
