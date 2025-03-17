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

Guideline
#########

.. gd_guidl:: Requirements Guideline
   :id: gd_guidl__req__engineering
   :status: valid

This document describes the general guidances for requirements based on the concept which is defined :need:`[[title]]<doc_concept__req__process>`.

General Hints
=============

Templates
---------

*Need* templates displaying the correct syntax and attribute definition are provided for each requirement type. For VScode code snippets are included in the workspace settings which will provide in-place the definition of requirements including all mandatory attributes:

.. list-table:: Overview
   :header-rows: 1
   :widths: 37, 37, 25

   * - Requirement Level
     - Template
     - VS Code Snippet
   * - Stakeholder Requirements
     - :need:`[[title]] <gd_temp__req__stkh_req>`
     - stkh_req_t
   * - Feature Requirements
     - :need:`[[title]] <gd_temp__req__feat_req>`
     - feat_req_t
   * - Component Requirements
     - :need:`[[title]] <gd_temp__req__comp_req>`
     - comp_req_t
   * - AoU Requirements
     - :need:`[[title]] <gd_temp__req__aou_req>`
     - aou_req_t
   * - Process Requirements
     - :need:`[[title]] <gd_temp__req__process_req>`
     - gd_req_t

Additionally for the formulation of requirements following template is available: :need:`[[title]]<gd_temp__req__formulation>`

Attributes
----------

For all requirements following mandatory attributes need to be defined:

.. needtable:: Overview of mandatory requirement attributes
   :tags: requirements_engineering
   :filter: "mandatory" in tags and "attribute" in tags and type == "gd_req"
   :style: table
   :columns: title
   :colwidths: 30


* Title and description: For the formulation of requirements following template shall be used :need:`[[title]]<gd_temp__req__formulation>`
* ID: The naming convention for the ID is defined :ref:`here <naming_convention_needs>`.
* Furthermore the requirements need to be versioned. Therefore a hash value of the requirement will to be calculated. The concept is described: :ref:`traceability concept for requirements`
* For the remaining attributes only predefined values can be used. A more detailed description can be found here: :ref:`attributes of the requirements`

Checks
------

During the sphinx build checks will be performed on the requirements. Those are specified via following process requirements:

.. needtable:: Overview checks for requirement
   :tags: requirements_engineering
   :filter: "check" in tags and "attribute" in tags and type == "gd_req"
   :style: table
   :columns: title;id
   :colwidths: 60,40

.. _workflow_requirements:

Workflow for Creating a Requirement
===================================

This section describes in detail which steps need to be performed to create a requirement based on :numref:`requirements_workflow_fig`

.. list-table:: Workflow for creating a requirement
   :header-rows: 1
   :widths: 10,60,30

   * - Step
     - Description
     - Responsible
   * - :ref:`1. <create_parent_requirement>`
     - Create parent requirement
     - :need:`[[title]] <rl__contributor>`
   * - :ref:`2. <review_parent_requirement>`
     - Review parent requirement
     - :need:`[[title]] <rl__committer>`
   * - 3.
     - Merge valid parent requirement to main branch
     - :need:`[[title]] <rl__committer>`
   * - :ref:`4. <derive_child_requirement>`
     - Derive child requirement and establish traceability
     - :need:`[[title]] <rl__contributor>`
   * - :ref:`5. <review_child_requirement>`
     - Review child requirement
     - :need:`[[title]] <rl__committer>`
   * - 6.
     - Merge valid child requirement to main branch
     - :need:`[[title]] <rl__committer>`
   * - :ref:`7. <generate_linkage_document>`
     - Generate linkage document
     - :need:`[[title]] <rl__contributor>`
   * - :ref:`8. <formal_requirement_review>`
     - Perform formal review of requirements
     - :need:`[[title]] <rl__committer>`

.. _create_parent_requirement:

Create parent requirement
-------------------------

In this step the parent requirements shall be created. Stakeholder- and feature requirements should be generated in the score repository.

Therefore following guidelines are available:

* :ref:`Branch Naming Conventions <branch_naming>`
* :ref:`Git Guidelines <git_guidelines>`
* :ref:`Requirement Templates <requirement templates>`

.. _review_parent_requirement:

Review parent requirement
-------------------------

As soon as the parent requirements are in a mature state it can be :ref:`reviewed <review_concept>` and merged into the main branch of the score repository. However this is not the formal inspection of the requirements, this will follow in an upcoming step.

Following roles should be included in the review:

* :need:`[[title]] <rl__safety_manager>`
* :need:`[[title]] <rl__security_manager>`
* :need:`[[title]] <rl__committer>`

.. _derive_child_requirement:

Derive child requirement and establish traceability
---------------------------------------------------

In an upcoming step the child requirements shall be derived from the parent requirements. Feature requirements shall be placed in the score repository again, while component requirements shall be placed in the module repository. During this process the derived requirements shall also be linked according to the defined traceability matrix to the parent requirements.

Following guidelines are available:

* :ref:`Branch Naming Conventions <branch_naming>`
* :ref:`Git Guidelines <git_guidelines>`
* :ref:`Requirement Templates <requirement templates>`

.. _review_child_requirement:

Review child requirement
------------------------

As soon as also the child requirements are in a mature state they can be :ref:`reviewed <review_concept>` and merged into the main branch of the respective repository. Again this is not a formal inspection as it will be performed in a later step.

.. _generate_linkage_document:

Generate linkage document
-------------------------

As parent and child requirements are now available the linkage of the requirements can be established. This should be performed as described in :ref:`coverage_of_requirements`


.. _formal_requirement_review:

Perform formal review of requirements
-------------------------------------

In a last step the requirements shall be formally inspected. Therefore a checklist exists: :need:`[[title]] <gd_chklst__req__inspection>`

Following roles should be included in the review:

* :need:`[[title]] <rl__safety_manager>`
* :need:`[[title]] <rl__security_manager>`
* :need:`[[title]] <rl__committer>`


Workflow for Creating and Linking Assumption of Use (AoU)
*********************************************************

An AoU is a category of requirement which is originates from a safety concept of an architectural element (and thus it is confirmed by a safety analysis). As it can not be fulfilled by the architecture element (e.g. component) itself, it needs to be fulfilled by the user of the module.
In Safety Elements out of Context (SEooC) the AoUs will normally be part of the safety manual.
In this project (as it develops SEooCs) these AoUs are created both internally and externally - if existing SEooCs are integrated into the platform (e.g. a qualified Operating System).
For AoU which arise from Score specific modules the template is almost identical to the one for feature/component requirements. The only difference is that it defined such that the attribute "satisfies" is replaced with the attribute "mitigates" (see picture below).
For externally provided AoUs of course the sentence template cannot be taken into account, as these are only imported from an external safety manual. It is also not possible to link it to other development artifacts via the attribute "mitigates".

AoUs can be of different class and shall be handled by tracing those

* to Feature/Component Architecture (via satisfies), if those are on Component Level and can be fulfilled there
* to Stakeholder Requirements (via satisfies), if AoU are of general nature and can be fulfilled by platform
* or by containing those in Platform Safety Manual, if AoU cannot be fulfilled by platform but need to be satisfied by the user of the platform


.. figure:: ../_assets/aou_traceability.drawio.svg
   :align: center
   :width: 100%
   :name: aou_traceability

   AoU Traceability

:numref:`aou_traceability` is an extension of the workproduct traceability to show the handling of (external) AoU. Note that the component level displayed in green shows two components - on the right the one exporting AoU to be fulfilled by others, left the component which fulfills and exports AoU (but without the traceability shown on the right to reduce complexity).
