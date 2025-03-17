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

Architecture Guideline
######################

.. gd_guidl:: Architectural Design
   :id: gd_guidl__arch__design
   :status: valid

The guideline focuses on the steps which need to be performed in order to create the architectural design. The concept behind those steps is described in the :need:`[[title]] <doc_concept__arch__process>`

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
     - :ref:`Create feature architecture (Concept) <create_feature_architecture>`
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
     - | :ref:`Create component architecture (Concept) <create_component_architecture>`
       | :ref:`Allocate component requirements to architectural elements <allocate_component_requirements>`
     - :need:`[[title]] <rl__contributor>`
   * - 7.
     - :ref:`Model component architecture <model_component_architecture>`
     - :need:`[[title]] <rl__contributor>`
   * - 8.
     - :ref:`Review component architecture <review_component_architecture>`
     - :need:`[[title]] <rl__committer>`
   * - 9.
     - Merge component architectural design into module
     - :need:`[[title]]  <rl__committer>`

.. _create_feature_architecture:

Create feature architecture (Concept)
----------------------------------------

The feature architecture (= high level architecture) shall be created in the feature tree of the platform repository.
As a starting point a :need:`template <gd_temp__arch__feature>` is available.

Based on this template the feature architecture shall describe the concept of the feature including supporting figures and drawings.

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
   :widths: 10,30,30

   * - Element
     - Sphinx directive
     - VS Code Template
   * - Feature Architecture
     - feat_arc_sta, feat_arc_dyn
     - feat_arc_sta_t, feat_arc_dyn_t
   * - Logical Interface
     - feat_arc_int
     - feat_arc_int_t
   * - Logical Interface Operation
     - feat_arc_int_op
     - feat_arc_int_op_t

The relations of the static elements are described in :numref:`metamodel_architectural_design`.

.. note::
   For the modeling of the architecture a sphinx extension is available: :ref:`arch_gen_sphinx`

   An example for modeling the architecture can be found :ref:`here <definition_architectural_design>`

.. _allocate_feature_requirements:

Allocate feature requirements to architectural elements
-------------------------------------------------------

In the next step the already derived feature requirements shall be allocated to the architectural elements depending on the content of the requirement. Functional Requirement may either be allocated to static or dynamic architecture. Interface requirements shall only be allocated to the interface architecture.

If needed also additional feature requirements, which may arise due to architectural decisions, should be created and allocated to the feature architecture itself.

Those links shall be established from architectural elements to feature requirements via the attribute *fulfils*

.. _review_architectural_design:

Review architectural design
---------------------------

As soon as the design is in a mature state it can be reviewed according to :need:`doc_concept__wp_inspections`
and merged into the main branch of the score repository.

For the review process a checklist template is available: :need:`[[title]] <gd_chklst__arch__inspection_checklist>`

Following roles should be included in the review:

* :need:`[[title]] <rl__safety_manager>`
* :need:`[[title]] <rl__security_manager>`
* :need:`[[title]] <rl__technical_lead>`
* :need:`[[title]] <rl__committer>`

.. _create_component_architecture:

Create component architecture (Concept)
---------------------------------------

Based on the *feature architecture* the concept for the *component architecture* shall be created in the SW module. It shall describe which components need to be created and how they correlate with each other in order to provide the required functionality. As a starting point a :need:`template <gd_temp__arch__comp>` is provided.

For this step following guidances are available:

* :ref:`Branch Naming Conventions <branch_naming>`
* :ref:`Git Guidelines <git_guidelines>`
* :need:`[[title]] <gd_temp__arch__comp>`

.. _allocate_component_requirements:

Allocate component requirements to architectural elements
---------------------------------------------------------

In this step the component requirements shall be derived (see :need:`[[title]] <gd_guidl__req__engineering>`) and allocated to the architectural elements via the attribute *fulfils*.

.. _model_component_architecture:

Model component architecture
----------------------------

According to the architecture design description the model for the component architecture shall be created. It shall consist of components, real interfaces and real interface operations. Depending on the size of the component it can also be split into multiple (sub) components.

.. list-table:: Architectural Elements of the Component Architecture
   :header-rows: 1
   :widths: 10,30,30

   * - Element
     - Sphinx directive
     - VS Code Template
   * - Component Architecture
     - comp_arc_sta, comp_arc_dyn
     - comp_arc_sta_t, comp_arc_dyn_t
   * - (Real) Interface
     - comp_arc_int
     - comp_arc_int_t
   * - (Real) Interface Operation
     - comp_arc_int_op
     - comp_arc_int_op_t

The relations of the static elements are described in :numref:`metamodel_architectural_design`

.. _review_component_architecture:

Review component architecture
-----------------------------

As soon as the design is in a mature state it can be :ref:`reviewed <review_concept>` and merged into the main branch of the module repository.

Following roles should be included in the review:

* :need:`[[title]] <rl__safety_manager>`
* :need:`[[title]] <rl__security_manager>`
* :need:`[[title]] <rl__committer>`

For the review process a checklist template is available:

:need:`[[title]] <gd_chklst__arch__inspection_checklist>`

UML diagram selection
=====================

Static architecture
-------------------
As can be seen from the examples presented in :need:`feat_arc_sta__feature_1` and :need:`comp_arc_sta__archdes_component_2`
for the static architecture a UML component diagram is expected (and supported by the tooling).

Dynamic architecture
--------------------
The :need:`doc_concept__arch__process` shows the usage of UML sequence diagrams to describe dynamic
behaviour. This is also the expected default diagram. Alternatively also state machine diagrams can be used
to describe stateful behaviour. Other types like the activity diagram are not encouraged to use,
if an activity diagram is used instead of a sequence diagram, this has to be argued as part of the
architecture description.

Generally dynamic views are expected in the feature view and the component view based on the following considerations:

- Do not use dynamic views, if the fulfillment of the requirements by the architecture is already understandable with the static view.
- Simple caller/callee relation is not expected to be modelled (this would mean that the examples would be too simple for modelling).
- It should be more than two components involved.
- In case of safety related calls/communication also the error cases shall be displayed (see the "alt" boxes in the examples).
- If there would be only small difference between the feature and the component view, one can be omitted, preferrably the feature view.
- If the described feature or components support multiple use cases (e.g. in different life cycle phases).
  these should be described also in multiple dynamic views.
