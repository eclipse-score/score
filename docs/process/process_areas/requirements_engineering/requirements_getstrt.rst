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

Getting Started on Requirements
###############################

.. doc_getstrt:: Getting Started on the Requirements
   :id: DOC_GETSTRT__req__process
   :status: valid
   :tags: requirements_engineering

This paragraph describes the general guidances for requirements based on the concept which is defined :need:`[[title]]<DOC_CONCEPT__req__process>`.

Let`s start with an example code for a requirement before we go into the details of the requirement guidance.

.. code-block:: rst

   .. feat_req:: <Title>
      :id: FEAT_REQ__<ID>
      :reqtype: <Functional|Interface|Process|Legal|Non-Functional>
      :security: <YES|NO>
      :safety: <QM|ASIL_B|ASIL_D>
      :satisfies: <link to parent requirement id>
      :status: <valid|invalid>

      <Description>

It displays the directive *feat_req* including its mandatory attributes. For these attributes following guidances are available:

* Title and description: For the formulation of requirements following template shall be used :need:`[[title]]<GD_TEMP__req__formulation>`
* ID: The naming convention for the ID is defined here <TBD>.
* For the remaining attributes only predefined values can be used. A more detailed description can be found here: :ref:`attributes of the requirements`

Checks for Requirements
***********************

During the sphinx build checks will be performed on the requirements. Those are specified via following requirements:

.. needtable:: Overview checks for requirement
   :filter: "check" in tags and "attribute" in tags and type == "gd_req"
   :style: table
   :columns: title;id
   :colwidths: 60,40

Templates for Requirements
**************************

Templates displaying the correct syntax and attribute definition are provided for each requirement type. For VScode code snippets are included in the workspace settings which will provide in-place the definition of requirements including all mandatory attributes:

.. list-table:: Overview
   :header-rows: 1
   :widths: 33, 33, 33

   * - Requirement Level
     - Template
     - VS Code Snippet
   * - Stakeholder Requirements
     - :need:`[[title]] <GD_TEMP__req__stkh_req>`
     - stkh_req_t
   * - Feature Requirements
     - :need:`[[title]] <GD_TEMP__req__feat_req>`
     - feat_req_t
   * - Component Requirements
     - :need:`[[title]] <GD_TEMP__req__comp_req>`
     - comp_req_t
   * - AoU Requirements
     - :need:`[[title]] <GD_TEMP__req__aou_req>`
     - aou_req_t
   * - Process Requirements
     - :need:`[[title]] <GD_TEMP__req__process_req>`
     - gd_req_t

Furthermore the requirements need to be versioned. Therefore a hash value of the requirement will to be calculated. The concept is described: :ref:`traceability concept for requirements`

Workflow for Creating a Requirement
***********************************

Following steps need to be executed to generate a requirement, for each step a guidance is available:

.. list-table:: Workflow for creating a requirement
   :header-rows: 1
   :widths: 40,40,20

   * - Step
     - Guidance
     - Responsible
   * - Create Branch
     - :ref:`branch_naming`
     - :need:`[[title]] <RL_contributor>`
   * - Create Requirement
     - :ref:`requirement templates`
     - :need:`[[title]] <RL_contributor>`
   * - Commit Changes
     - :ref:`git_guidelines`
     - :need:`[[title]] <RL_contributor>`
   * - Review
     - :ref:`requirement inspection checklist`
     - | :need:`[[title]] <RL_safety_manager>`
       | :need:`[[title]] <RL_committer>`

.. _requirement_workflow:

.. figure:: _assets/requirements_workflow.svg
   :alt: Requirements Workflow
   :align: center
   :width: 80%

   Requirements Workflow

:numref:`requirement_workflow` displays the workflow for creating requirements. The Steps are in Detail:


#. | Create parent requirement
   | Calculate Hash value of parent requirement
#. Review parent requirement
#. Merge valid parent requirement to main
#. | Create sub requirement
   | Link sub requirement to parent requirement
   | Calculate Hash value of sub requirement
#. Review sub requirement
#. Merge valid sub requirement to main
#. Generate formal review document
#. Formal requirement review including req coverage
#. Merge valid formal review document to main

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


.. _aou_traceability:

.. figure:: _assets/aou_traceability.svg
   :alt: AoU traceability
   :align: center
   :width: 100%

   AoU traceability

:numref:`aou_traceability` is an extension of the workproduct traceability to show the handling of (external) AoU. Note that the component level displayed in green shows two components - on the right the one exporting AoU to be fulfilled by others, left the component which fulfills and exports AoU (but without the traceability shown on the right to reduce complexity).

Tooling Support
***************

Additionally tooling is provided to assist the :need:`[[title]] <RL_contributor>` to define the requirements in spinx needs. The current feature set is described as IDE requirements:

<TBD>

.. needtable:: Implemented IDE Requirements
   :tags: sphinx, ide
   :style: table
   :columns: title;id
   :filter: "ide" in tags and type == "tool_req"
   :colwidths: 70,30

A *HowTo* which describes the setup of Sphinx Needs in VScode is available here: <TBD>

For all RST files also a linter is configured, it will be automatically run in the CI upon check-in.
Locally it can be run via

.. code-block:: shell

   bazel test //:format.check

