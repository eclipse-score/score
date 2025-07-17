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

.. document:: Documentation Management Plan
   :id: doc__documentation_mgt_plan
   :status: valid
   :safety: ASIL_B
   :tags: platform_management
   :realizes: wp__document_mgt_plan

Documentation Management Plan
-----------------------------

Purpose
+++++++

The documentation management plan describes how documents are handled in the S-CORE project.

Objectives and scope
++++++++++++++++++++

Goal of this plan is to describe

* which documents exist
* which attributes and lifecycle they have
* how they are reviewed

Approach
++++++++

Some of the work products of the S-CORE project are modelled specifically
(e.g. the requirements and architecture have a specific set of attributes)
Others are modelled as general documents (e.g. the plans which are part of the program management plan or the verification reports).

This plan deals with these documents, which have the following manually set attributes:

* Title: the name of the document (mandatory)
* Unique Id: Id following the naming pattern of the document Title (mandatory)
* Safety: which ASIL the document supports (mandatory)
* Author: Who is the main committer to the document (mandatory)
* Status: describing where in the lifecycle of the document it currently is (mandatory)
* Tags: can be used to group documents for subsequent filtering (optional)

Also the "Documentation Management" is a document, so an example for a correct document definition
can be seen in the header section above, see :need:`doc__documentation_mgt_plan`.

The following additional attributes of the document are generated automatically during the documentation build:

* Approver: from the github information on who was the last CODEOWNER performing the github review
* Reviewer: any additional reviewer performing the github review without CODEOWNER rights

The lifecycle of S-CORE documents has two states:

* Draft: The document is filled with content but not completed, the existing content is reviewed and already applicable
* Valid: The document is completed and approved

If a document is invalidated it is removed from the project entirely. A document can also transition from valid to draft,
for example if a release was done with a valid verification report and then the development for the next release is started.

Invalidated documents are still observable as part of the git history in the unlikely case of later referral
(e.g. for design decisions or audit). In this way, there is even an option to recover the content.

The review of each document is done as defined for this type of work product in the respective process description.
This means that for some of the work products dedicated checklists are defined, but for others there are not.
In any case the reviews are done in a github review at least by one CODEOWNER who is not the author of the document.

Generally all work products (specific and general documents) are subject to a documentation build,
which always contains the latest version of the documents for each pull-request.
Versioning of documents is done as for every work product with github means and is defined in the configuration management plan.

.. _project_documents_list:

The following table lists all documents of the S-CORE project. For a better overview, the documents were grouped into categories.
List of all documents
- used for process descriptions
- used for platform management plan
- additional documents
- feature documents (All documents that are used for feature descriptions)
- feature description templates (List of all documents that are in the template folder for feature descriptions)
- module description templates (List of all documents that are in the template folder for module descriptions)
- module documents (List of all documents that are used for module descriptions)

This lists shall be used for an overview of the documents in S-CORE and also for planing aspects.
Additionally checks, based on the lists can be done to ensure that all documents are available and up-to-date.

List of all documents in S-CORE that are used for process descriptions
----------------------------------------------------------------------


.. list-table:: List of all documents in S-CORE that are used for process descriptions
      :header-rows: 1

      * - Title
        - ID
        - Status
        - Tags

      * - Architecture Process
        - :need:`PROCESS_doc_concept__arch__process`
        - valid
        -

      * - Architecture Design Process
        - :need:`PROCESS_doc_getstrt__arch__process`
        - valid
        -

      * - Change Management Concept Description
        - :need:`PROCESS_doc_concept__change__process`
        - valid
        - change_management

      * - Getting Started on Change Management
        - :need:`PROCESS_doc_getstrt__change__process`
        - valid
        - change_management

      * - Configuration Management
        - :need:`PROCESS_doc_concept__configuration__process`
        - valid
        -

      * - Configuration Management Concept
        - :need:`PROCESS_doc_concept__configuration__process`
        - valid
        -

      * - Documentation Management Concept
        - :need:`PROCESS_doc_concept__documentation__process`
        - valid
        -

      * - Documentation Management Get Started
        - :need:`PROCESS_doc_getstrt__documentation__process`
        - valid
        -

      * - Concept Description
        - :need:`PROCESS_doc_concept__imp__concept`
        - valid
        - implementation

      * - Getting Started on Implementation
        - :need:`PROCESS_doc_getstrt__imp__getstrt`
        - valid
        - Implementation

      * - Concept Description
        - :need:`PROCESS_doc_concept__platform__process`
        - valid
        - platform_management

      * - Getting Started on Platform/Project Management
        - :need:`PROCESS_doc_getstrt__platform__process`
        - valid
        - platform_management

      * - Concept Description
        - :need:`PROCESS_doc_concept__problem__process`
        - valid
        - problem_resolution

      * - Getting Started on Problem Resolution
        - :need:`PROCESS_doc_getstrt__problem__process`
        - valid
        - problem_resolution

      * - Quality Management Concept
        - :need:`PROCESS_doc_concept__quality__process`
        - valid
        - quality_management

      * - Getting Started on Quality Management
        - :need:`PROCESS_doc_getstrt__quality__process`
        - valid
        - quality_management

      * - Concept Description
        - :need:`PROCESS_doc_concept__rel__process`
        - valid
        -

      * - Requirements Concept
        - :need:`PROCESS_doc_concept__req__process`
        - valid
        - requirements_engineering

      * - Getting Started on Requirements
        - :need:`PROCESS_doc_getstrt__req__process`
        - valid
        - requirements_engineering

      * - Safety Analysis Concept
        - :need:`PROCESS_doc_concept__safety__analysis`
        - valid
        - safety_analysis

      * - Getting Started on Safety Analysis
        - :need:`PROCESS_doc_getstrt__safety_analysis`
        - valid
        - safety_analysis

      * - Concept Description
        - :need:`PROCESS_doc_concept__tool__process`
        - valid
        - tool_management

      * - Getting Started on Tool Management
        - :need:`PROCESS_doc_getstrt__tool__process`
        - valid
        - tool_management

      * - Verification Concept
        - :need:`PROCESS_doc_concept__verification__process`
        - valid
        - requirements_engineering

      * - Verification Get Started
        - :need:`PROCESS_doc_getstrt__verification__process`
        - valid
        - verification

      * - Work product Inspections Concept
        - :need:`PROCESS_doc_concept__wp_inspections`
        - valid
        -


List of all documents in S-CORE that are used for platform management plan

.. list-table:: List of all documents in S-CORE that are used for platform management plan
      :header-rows: 1

      * - Title
        - ID
        - Status
        - Tags

      * - Change Management Plan
        - :need:`doc__platform_change_management_plan`
        - draft
        - platform_management

      * - Configuration Management Plan
        - :need:`doc__config_mgt_plan`
        - draft
        - platform_management

      * - Documentation Management Plan
        - :need:`doc__documentation_mgt_plan`
        - draft
        - platform_management

      * - Problem Resolution Plan
        - :need:`doc__platform_problem_resolution_plan`
        - draft
        - platform_management

      * - Project Management Plan
        - :need:`doc__project_mgt_plan`
        - draft
        - platform_management

      * - Platform Management Plan
        - :need:`doc__platform_mgt_plan`
        - valid
        - platform_management

      * - Platform Quality Management Plan
        - :need:`doc__platform_quality_plan`
        - valid
        - platform_management

      * - Release Management Plan
        - :need:`doc__platform_release_management_plan`
        - draft
        - platform_management

      * - Platform Safety Plan
        - :need:`doc__platform_safety_plan`
        - draft
        - platform_management

      * - Software Development Plan
        - :need:`doc__software_development_plan`
        - draft
        - platform_management

      * - Software Verification Plan
        - :need:`doc__verification_plan`
        - draft
        - platform_management

      * - Tool Management Plan
        - :need:`doc__platform_tool_management_plan`
        - valid
        - platform_management

List of all additional documents in S-CORE
----------------------------------------------------------------------


.. list-table:: List of all additional documents in S-CORE
      :header-rows: 1

      * - Title
        - ID
        - Status
        - Tags

      * - Contribution
        - :need:`doc__contribution_guideline`
        - valid
        -

      * - Naming Conventions
        - :need:`doc__naming_conventions`
        - valid
        -

      * - Git Guidelines
        - :need:`doc__git_coding_guidelines`
        - valid
        -

      * - Development Environment
        - :need:`doc__develop_environment`
        - valid
        -

      * - Coding Guidelines C++
        - :need:`doc__cpp_coding_guidelines`
        - valid
        -

      * - Static Code Analysis C++
        - :need:`doc__cpp__code_analysis`
        - valid
        -

      * - MISRA C++:2023 Rule Mapping
        - :need:`doc__cpp__misra2023_rule_mapping`
        - draft
        -

      * - Coding Guidelines Rust
        - :need:`doc__rust_coding_guidelines`
        - valid
        -

      * - Coding Guidelines Python
        - :need:`doc__python_coding_guidelines`
        - valid
        -

List of all feature documents in S-CORE
----------------------------------------------------------------------

Please add your feature documents in this list.

.. list-table:: List of all feature documents in S-CORE
      :header-rows: 1

      * - Title
        - ID
        - Status
        - Tags

      * - doc__logging
        - :need:`doc__logging`
        - draft
        - feature_request

      * - Base Libraries
        - :need:`doc__baselibs`
        - valid
        - feature_request

      * - Communication
        - :need:`doc__com`
        - valid
        - feature_request

      * - Inter-process Communication
        - :need:`doc__com_ipc`
        - valid
        - contribution_request, feature_request

      * - Configuration Management
        - :need:`doc__config_mgmt`
        - draft
        - contribution_request, feature_request

      * - Fixed execution order framework
        - :need:`doc__feo`
        - valid
        - feature_request

      * - Persistency Key-Value-Storage
        - :need:`doc__persistency_kvs`
        - valid
        - feature_request, persistency_kvs

List of all documents that shall be used for a feature description
------------------------------------------------------------------

.. list-table:: List of all documents that shall be used for a feature description
      :header-rows: 1

      * - Title
        - ID
        - Status
        - Tags

      * - [Your Feature Name]
        - doc__feature_name
        - draft
        - template, feature_name

      * - [Your Feature Name] Requirements
        - doc__feature_name_requirements
        - draft
        - template, feature_name

      * - [Your Feature Name] Architecture
        - doc__feature_name_architecture
        - draft
        - template, feature_name

      * - [Your Feature Name] Safety WPs
        - doc__feature_name_safety_wp
        - draft
        - template, feature_name

      * - [Your Feature Name] FMEA
        - doc__feature_name_fmea
        - draft
        - template, feature_name

      * - [Your Feature Name] DFA
        - doc__feature_name_dfa
        - draft
        - template, feature_name


List of all documents that shall be used for a module description
------------------------------------------------------------------

.. list-table:: List of all documents that shall be used for a module description
      :header-rows: 1

      * - Title
        - ID
        - Status
        - Tags

      * - [Your Module Name] Safety Manual
        - doc__module_name_safety_manual
        - draft
        - template

      * - [Your Module Name] Safety Plan
        - doc__module_name_safety_plan
        - draft
        - template

      * - [Your Module Name] Safety Plan Formal Review
        - doc__module_name_safety_plan_fdr
        - draft
        - template

      * - [Your Module Name] Safety Package Formal Review
        - doc__module_name_safety_package_fdr
        - draft
        - template

      * - [Your Module Name] Verification Report
        - doc__module_name_verification_report
        - draft
        - template

      * - [Your Module Name] Release Note
        - doc__module_name_release_note
        - draft
        - template

      * - [Your Component Name] Requirements
        - doc__component_name_requirements
        - draft
        - template, component_name

      * - [Your Component Name] Architecture
        - doc__component_name_architecture
        - draft
        - template, component_name

      * - [Your Component Name] Detailed Design
        - doc__component_name_detailed_design
        - draft
        - template, component_name

      * - [Your Component Name] FMEA
        - doc__component_name_fmea
        - draft
        - template, component_name

      * - [Your Component Name] DFA
        - doc__component_name_dfa
        - draft
        - template, component_name

      * - [Your Component Name] Component Classification
        - doc__component_name_comp_class
        - draft
        - template, component_name


Each module shall have it's own list. Please add our module.

List of all documents of module Communication
---------------------------------------------

.. list-table:: List of all documents that shall be used for a module description
      :header-rows: 1

      * - Title
        - ID
        - Status
        - Tags

      * - Entry 1
        - doc__com_entry_1
        - draft
        - template, com

List of all documents of module Persistency
-------------------------------------------

.. list-table:: List of all documents that shall be used for a module description
      :header-rows: 1

      * - Title
        - ID
        - Status
        - Tags

      * - Entry 1
        - doc__com_entry_1
        - draft
        - template, com
