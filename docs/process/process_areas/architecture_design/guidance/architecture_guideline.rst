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

.. _arch_design_guideline:

Guideline
#########

.. gd_guidl:: Architectural Design
   :id: gd_guidl__arch__design
   :status: valid

The guideline focuses on the steps which need to be performed in order to create the architectural design. The concept behind those steps is described in :need:`[[title]] <doc_concept__arch__process>`

General Hints
=============

Attributes
----------

For all architectural need elements following mandatory attributes are defined:

.. needtable:: Overview of mandatory attributes
   :filter: "mandatory" in tags and "attribute" in tags and "architecture_design" in tags and type == "gd_req"
   :style: table
   :columns: title; id
   :colwidths: 30,70


Checks
------

For architectural elements following checks are defined:

.. needtable:: Overview of checks on architectural elements
   :filter: "check" in tags and "attribute" in tags and "architecture_design" in tags and type == "gd_req"
   :style: table
   :columns: title; id
   :colwidths: 30,70


Workflow for creating an architectural design
=============================================

This chapter describes the general guideline for architectural design within the project. In general the workflow for creating an architectural design is shown in :ref:`architecture_workflow_fig`

Those steps are:

.. list-table:: Definition of the static architectural elements
   :header-rows: 1
   :widths: 10,60,30

   * - Step
     - Description
     - Responsible
   * - 1.
     - :ref:`Create high level architecture (Concept) <create_high_level_architecture>`
     - :need:`[[title]] <rl__contributor>`
   * - 2.
     - :ref:`Model feature architecture <model_feature_architecture>`
     - :need:`[[title]] <rl__contributor>`
   * - 3.
     - :ref:`Allocate feature requirements to architectural elements <allocate_feature_requirements>`
     - :need:`[[title]] <rl__contributor>`
   * - 4.
     - :ref:`Review architectural design <review_architectural_design>`
     - :need:`[[title]] <rl__committer>`
   * - 5.
     - Merge architectural design into score repository
     - :need:`[[title]] <rl__committer>`
   * - 6.
     - :ref:`Create component architecture (Concept) <create_component_architecture>`
     - :need:`[[title]] <rl__contributor>`
   * - 7.
     - :ref:`Model component architecture <model_component_architecture>`
     - :need:`[[title]] <rl__contributor>`
   * - 8.
     - :ref:`Allocate component requirements to architectural elements <allocate_component_requirements>`
     - :need:`[[title]] <rl__contributor>`
   * - 9.
     - :ref:`Review component architecture <review_component_architecture>`
     - :need:`[[title]] <rl__committer>`
   * - 10.
     - Merge component architectural design into module
     - :need:`[[title]]  <rl__committer>`

.. _create_high_level_architecture:

Create high level architecture (Concept)
----------------------------------------

The high level architecture (HLA) shall be created in the feature tree of the platform repository.
As a starting point a :need:`template <gd_temp__arch__feature>` is available.

Based on this template the HLA shall describe the concept of the feature including supporting figures and drawings.

For this step following guidances are available:

* :ref:`Branch Naming Conventions <branch_naming>`
* :ref:`Git Guidelines <git_guidelines>`
* :need:`[[title]] Feature Architecture <gd_temp__arch__feature>`

.. _model_feature_architecture:

Model feature architecture
--------------------------

Based on the concept description a model of the feature architecture should be designed. It shall consist of the logical interfaces which the user of the feature can access including also the modules which provide the interfaces. Therefore following elements shall be used:

.. list-table:: Architectural Elements of the Feature Architecture
   :header-rows: 1
   :widths: 10,60,30

   * - Element
     - Sphinx directive
     - VS Code Template
   * - Logical Interface
     - feat_arc_int
     - feat_arc_int_t
   * - Logical Interface Operation
     - feat_arc_int_op
     - feat_arc_int_op_t
   * - SW Module
     - mod_arc_sta
     - mod_arc_sta_t

The relations of those elements are described in :numref:`metamodel_architectural_design`.

.. note::
   For the modeling of the architecture a sphinx extension is available: :ref:`arch_gen_sphinx`

   An example for modeling the architecture can be found :ref:`here <definition_architectural_design>`

.. _allocate_feature_requirements:

Allocate feature requirements to architectural elements
-------------------------------------------------------

In the next step the already derived feature requirements shall be allocated to the architectural elements. If needed also additional feature requirements, which may arise due to architectural decisions, should be created and allocated to the stakeholder requirements.

Those links shall be established from architectural elements to feature requirements via the attribute *fulfils*

.. _review_architectural_design:

Review architectural design
---------------------------

As soon as the design is in a mature state it can be reviewed according to <TBD> and merged into the main branch of the score repository.

For the review process a checklist template is available: :need:`[[title]] <gd_chklst__arch__inspection_checklist>`

Following roles should be included in the review:

* :need:`[[title]] <rl__safety_manager>`
* :need:`[[title]] <rl__security_manager>`
* :need:`[[title]] <rl__technical_lead>`
* :need:`[[title]] <rl__committer>`

.. _create_component_architecture:

Create component architecture (Concept)
---------------------------------------

Based on the HLA the concept component architecture shall be created in the SW module. As a starting point a :need:`template <gd_temp__arch__comp>` is provided. It shall describe which components need to be created and how they correlate with each other in order to provide the required functionality.

For this step following guidances are available:

* :ref:`Branch Naming Conventions <branch_naming>`
* :ref:`Git Guidelines <git_guidelines>`
* :need:`[[title]] <gd_temp__arch__comp>`

.. _model_component_architecture:

Model component architecture
----------------------------

According to the concept description of the component architecture the model for the component architecture shall be created. It shall consist of components, real interfaces and real interface operations. Depending on the size of the component also sub-components can be used.

.. list-table:: Architectural Elements of the Component Architecture
   :header-rows: 1
   :widths: 10,60,30

   * - Element
     - Sphinx directive
     - VS Code Template
   * - Component Architecture
     - comp_arc_sta
     - comp_arc_sta_t
   * - Sub-Component Architecture
     - sub_comp_arc_sta
     - sub_comp_arc_sta_t
   * - (Real) Interface
     - comp_arc_int
     - comp_arc_int_t
   * - (Real) Interface Operation
     - comp_arc_int_op
     - comp_arc_int_op_t

The relations of those elements are described in :numref:`metamodel_architectural_design`

.. _allocate_component_requirements:

Allocate component requirements to architectural elements
---------------------------------------------------------

In this step the component requirements shall be derived (see :need:`[[title]] <gd_guidl__req__engineering>`) and allocated to the architectural elements via the attribute *fulfils*.

.. _review_component_architecture:

Review component architecture
-----------------------------

As soon as the design is in a mature state it can be reviewed according to <TBD> and merged into the main branch of the module repository.

Following roles should be included in the review:

* :need:`[[title]] <rl__safety_manager>`
* :need:`[[title]] <rl__security_manager>`
* :need:`[[title]] <rl__committer>`

For the review process a checklist template is available:

:need:`[[title]] <gd_chklst__arch__inspection_checklist>`
