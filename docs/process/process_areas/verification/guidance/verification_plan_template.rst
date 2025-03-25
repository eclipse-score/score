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

.. _verification_plan_template:

Verification Plan Template
##########################

.. gd_temp:: Platform Verification Plan Template
    :id: gd_temp__verification__plan
    :status: valid
    :complies: std_wp__iso26262__support_951, std_wp__iso26262__support_1252

    This document implements :need:`wp__verification__plan`.

    It provides a template for a software verification plan and should be adapted to the specific
    project needs.

      The document should start with a header following the :need:`doc__documentation_mgt_plan`.

      .. code-block:: rst

         .. document:: Software Verification Plan
            :id: doc__verification_plan
            :status: draft
            :safety: ASIL_B
            :tags: platform_management

         Software Verification Plan
         **************************

         This document provides a template for a software verification plan.
         It should be adapted to the specific needs of project.


         Purpose
         =======

         This section should briefly describe the overall goal of the verification plan.
         It should state the plan's intended audience and the information it aims to provide.
         This might include clarifying the scope of the verification activities and linking to
         other relevant documents.


         Objectives and Scope
         ====================

         Objectives
         ----------

         This section outlines the key objectives of the software verification effort.
         Examples include correctness, completeness, reliability, performance, maintainability,
         compliance, and traceability. Each objective should be clearly defined and measurable.

         Verification Scope and Constraints
         ----------------------------------

         This section details what software components and functionalities are included in the
         verification process. It should also clearly specify any limitations or exclusions.
         This section should address external dependencies and integrations.


         Risks and Mitigation
         --------------------

         This section identifies potential risks associated with the verification activities and outlines
         strategies to mitigate those risks. This may involve referencing the :need:`wp__platform_mgmt`.


         Schedules
         ---------

         This section defines the timeline for different verification activities.
         It might include milestones, deadlines, and dependencies between tasks.


         Approach
         ========

         General Approach
         ----------------

         This section provides a high-level overview of the verification strategy.
         It should describe the overall methodology (e.g., Continuous Integration),
         approaches used, and rationale behind the choices made.

         Software Integration
         --------------------

         This section details how software components are integrated into the system.
         It should describe the integration process, including procedures for handling new features,
         bug fixes, and code changes.

         Levels of Integration and Verification
         --------------------------------------

         This section defines the different levels of integration and verification that will be performed
         (e.g., unit, component, system). Each level should be clearly defined, with associated criteria
         for successful completion.

         Verification Methods
         --------------------

         This section lists the specific verification methods used, such as static analysis,
         dynamic testing, reviews, and inspections. Each method should be briefly described,
         including its purpose and applicability at different levels of verification.
         Reference tables can list methods, identifiers, applicable levels and ASIL relevance.

         Test Derivation Methods
         ^^^^^^^^^^^^^^^^^^^^^^^

         This section details the techniques used to derive test cases (e.g., boundary value analysis,
         equivalence partitioning, requirements tracing). It should clarify which techniques are used
         at each level of testing and for different ASIL levels.  Again, a reference table is recommended.

         Quality Criteria
         ----------------

         This section specifies the quality criteria that must be met for successful verification.
         These criteria might include code coverage metrics, defect density, or other relevant measures.
         The criteria should be defined with quantifiable goals for different ASIL levels.

         Test Development
         ----------------

         This section describes the process for developing and maintaining test cases.
         It should cover aspects such as test automation, test data management, and version control.

         Pre-existing test cases
         ^^^^^^^^^^^^^^^^^^^^^^^
         This section describes how pre-existing test cases are handled which are e.g. available
         from an OSS component. It should be stated how they are reviewed, integrated, extended
         (e.g. with respective documentation), and adopted to the needs described in the project
         (e.g. usage of documentation templates and traceability)

         Test Execution and Result Analysis
         ----------------------------------

         This section describes how tests will be executed and the procedures for analyzing the results.
         It should outline the tools and processes used for test execution and reporting.

         Test Selection and Regression Testing
         -------------------------------------

         This section describes the approach to selecting test cases for execution and the strategy for
         regression testing to ensure that new changes don't introduce regressions.

         Work Products and Traceability
         ------------------------------

         This section lists all the key deliverables related to the verification process.
         It should also describe how traceability between requirements, design, code, and test
         cases is maintained.


         Environments and Resources
         ==========================

         Roles
         -----

         This section defines the roles and responsibilities of individuals involved in the
         verification process. It can refer and should be based on the definition in the
         verification process :ref:`verification_roles`.

         Tools
         -----

         This section lists the tools used for verification, including build systems, test frameworks,
         static analysis tools, and other relevant software.

         Verification Setups and Variants
         --------------------------------

         This section describes the different test environments and configurations used for verification.

         Test Execution Environment and Reference Hardware
         -------------------------------------------------

         This section describes the hardware and software environments used for test execution.
         It should include information about any specific hardware platforms or simulators used.
         It should also define how the verification environment interacts with the CI system, including
         access control and maintenance.
