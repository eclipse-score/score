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

Concept Description
###################

.. doc_concept:: Architecture Process
   :id: doc_concept__arch__process
   :status: valid

In this section a concept for the architecture design will be discussed.

Inputs
******

#. Use cases which require the architectural design?
#. Who needs which information?
#. Which standard requirements need to be fulfilled

Use Cases which require architectural information
=================================================

#. **Contribution Request**

   * Platform High Level Architecture
   * Graphical Feature Description

#. **Safety Analysis**

   * *Dependent Failure Analysis*

      * the interaction of the components with each other

   * *Qualitative safety analysis*

      * decomposition of the architectural element under analysis
      * interfaces within the architectural element under analysis (including their AoUs)
      * usage of the components (interface of the component under analysis itself)
      * allocate safety requirements to architectural elements

#. **Security Analysis**

   * TBD

#. **Safety Planning**

   * Decomposition into modules and components for the safety planning

#. **Security Planing**

   * TBD

#. **Platform SW Development**

   * Interfaces of own component and their respective contracts (including dynamic architecture) which need to be implemented
   * Interfaces of the interacting components which are used to obtain required information (including AoUs)
   * White Box view of the component itself

#. **Testing**

   * Use cases for the component including their AoUs
   * On component level an overview of the actual interfaces
   * All the interfaces and AoUs of the interacting components which need to be provided for a black box test

#. **Software Integration**

   * components which need to be integrated
   * dependencies for the integrated components including their configuration
   * order and task scheduling for all components

#. **Application SW Development**

   * public interfaces which are provided at the top level including their contracts
   * expected sequence of the single operations
   * a detailed api description of the interface

#. **Project Management**

   * High Level Architecture for project structuring and planning

Requirements based on standards
===============================

Additionally also standards specify requirements towards the architectural design:

* ISO26262
* ASPICE
* ISO21434

Their requirements are linked via the guidances.

.. _architectural_viewpoints:

Definition of architectural viewpoints
**************************************

In this section following questions shall be answered:

#. Which architectural viewpoints can we derive from the inputs?
#. Which architecture attributes are required?
#. How do the different viewpoints correlate to each other?

Based on the inputs two architectural levels are defined.

.. _feature_view:

Feature View
============

Static View
-----------

The first viewpoint is named as *feature architecture*. It displays the SW modules (= top level SW components) which are required to realize the feature including their interactions. Also the *logical interfaces* and the interaction between the feature and the user are included in this view. On this architectural level the feature requirements shall be allocated. An example for the static architecture is shown here:

.. feat_arc_sta:: Feature 1
   :id: feat_arc_sta__feature_1
   :security: YES
   :safety: QM
   :status: valid
   :includes: feat_arc_int__archdes_logical_interface_1, feat_arc_int__archdes_logical_interface_2
   :fulfils: feat_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

In all views the Components which are marked as ASIL_B related are drawn in blue color.

Dynamic View
------------

The next chart shows the dynamic behavior of the feature including the interaction of its modules with the user. Following scenarios should be included:

*  important use cases or features: how do components execute them?
*  interactions at critical external interfaces: how do components cooperate with users and neighboring components?
*  operation and administration: launch, start-up, stop
*  successful use cases
*  error and exception use cases

.. uml:: _assets/feature_architecture_dynamic.puml
   :align: center
   :caption: Dynamic Feature Architecture

Interface View
--------------

On the feature level only *logical interfaces* shall be displayed. This means that only logical names shall be provided for both the interface and the operations within. Those *logical interfaces* shall be connected to component interfaces on the module view.

.. feat_arc_int:: Logical Interface 1
   :id: feat_arc_int__archdes_logical_interface_1
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :fulfils: feat_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

SW Module View
==============

A SW Module in S-CORE represents a `Bazel Module <https://bazel.build/external/module>`_. It serves only as a container (or package) which can include components. It is not meant to be an architectural element which includes that no requirements can be allocated to it.

On this level also a view shall be defined which is called *Module View*. It represents the allocation of components into modules and displays the dependencies between the single modules. In this view also cyclic dependencies between modules can be identified.

.. mod_view_sta:: Module 3
   :id: mod_view_sta__archdes_3
   :includes: comp_arc_sta__archdes_component_1

   .. needarch::
      :scale: 50
      :align: center


      {{ draw_module(need(), needs) }}

Component View
==============

Static View
-----------

The second viewpoint is named as *component architecture* and describes the implementation of the functionalities in a white-box view of the platform. It describes the structural decomposition of the *SW components* into *lower level* SW components. In the S-CORE project this viewpoint provides more detailed information concerning the respective interfaces of a component. If a SW component interacts with a different component it is also included via a *use* relationship in the diagram. An example of the *component architecture* is displayed here:

.. comp_arc_sta:: Component 2
   :id: comp_arc_sta__archdes_component_2
   :status: valid
   :safety: ASIL_B
   :security: NO
   :includes: comp_arc_sta__archdes_sub_component_1, comp_arc_sta__archdes_sub_component_2, comp_arc_sta__archdes_sub_component_3
   :fulfils: comp_req__archdes_example_req

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}

The *lower level components* are optional and rely on the complexity of the component. Thus there is no graphic representation required for it.

Dynamic View
------------

The dynamic view of the component architecture shows the order of the interactions between the respective components. It is displayed via relations to the interface operations which are provided or used by each component.

.. uml:: _assets/component_architecture_dynamic.puml
   :align: center
   :caption: Dynamic Component Architecture

Interface View
--------------

The component interface view shows the actual interfaces of the component. Also links to their corresponding logical interfaces are displayed in this view:

.. comp_arc_int:: Component Interface 1
   :id: comp_arc_int__archdes_component_interface_1
   :status: valid
   :safety: ASIL_B
   :security: NO
   :fulfils: comp_req__archdes_example_req
   :language: cpp

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs)}}

Platform View
=============

Although it is required to create a *DFA* on platform level no additional view is required for this architectural level:

#. Features should be defined in a such way that they are independent of each other. Any dependencies should be displayed via common components in the feature view.

#. The feature set depends on the feature selection on platform level. This means that this view would depend highly on the selection of features which an integration choses to integrate on platform level. Thus this view would need to be generated based on the feature selection.

.. _architectural_design:

Specification of the architectural design
*****************************************

The architectural design shall be modeled with the help of static, dynamic and interfaces at each defined level.
For the description a natural language, diagrams or a semi-formal language *(UML)* shall be used.

The architectural elements itself including their correlations shall be modeled in a database like approach. Therefore following architectural elements shall be used:

Static view
===========

The *static view* shows the *building blocks* of the architecture. It shall be completely modeled in *sphinx needs*. Following elements are defined:

.. list-table:: Definition of the static architectural elements
   :header-rows: 1
   :widths: 15,35,35

   * - Element
     - Sphinx Needs Directive
     - Code Template
   * - Feature Architecture
     - feat_arc_sta
     - feat_arc_sta_t
   * - Component Architecture
     - comp_arc_sta
     - comp_arc_sta_t

To represent the `Bazel Modules <https://bazel.build/external/module>`_ an additional container (or package) is introduced. It can only contain components:

.. list-table:: Definition of the static module view
   :header-rows: 1
   :widths: 15,35,35

   * - Element
     - Sphinx Needs Directive
     - Code Template
   * - Module View
     - mod_view_sta
     - mod_view_sta_t

Dynamic view
============

The *dynamic view* describes the concrete behavior and interactions of the *building blocks* in form of use cases which were described above.

The dynamic view shall be modeled partly in Sphinx Needs and PlantUML. The components itself shall be generated from the sphinx needs model into the PlantUML diagram. The dynamic relations between the component and the interfaces shall be modeled in PlantUML as it would be a huge effort to model the dynamic behavior in sphinx needs and would not provide any additional benefit.

.. list-table:: Definition of the dynamic architectural elements
   :header-rows: 1
   :widths: 15,35,35

   * - Element
     - Sphinx Needs Directive
     - Code Template
   * - Dynamic Feature Architecture
     - feat_arc_dyn
     - feat_arc_sta_t
   * - Dynamic Component Architecture
     - comp_arc_dyn
     - comp_arc_dyn_t

Interface view
==============

The *interface view* focuses on the interfaces of the components and shows the operations within.

.. list-table:: Definition of the architectural elements
   :header-rows: 1
   :widths: 15,35,35

   * - (Logical) Interface
     - feat_arc_int
     - feat_arc_int_t
   * - (Logical) Interface Operation
     - feat_arc_int_op
     - feat_arc_int_op_t
   * - (Real) Interface
     - comp_arc_int
     - comp_arc_int_t
   * - (Real) Interface Operation
     - comp_arc_int_op
     - comp_arc_int_op_t

Relations between the architectural elements
============================================

The traceability between the architectural elements itself shall be established by modeling the elements in the *docs-as-code* tool. Here a "clickable" architecture can be generated which allows an easy tracing through the element tree. The previously introduced architectural components shall be connected by using following relations:

.. figure:: _assets/metamodel_architectural_design.drawio.svg
   :width: 90%
   :align: center
   :alt: Definition of the Metamodel for Architectural Design
   :name: metamodel_architectural_design

   Definition of the Metamodel for Architectural Design

Attributes of the architectural elements
****************************************

Since the architecture should be modeled in *Sphinx Needs* the corresponding attributes need to be defined. On the top level we can distinguish between attributes which need to be filled manually and attributes which are generated during the sphinx-docs build.

Following attributes need to be filled manually for each requirement:

.. list-table:: Manual attributes for architectural elements
   :header-rows: 1
   :widths: 15,85

   * - Attribute
     - Description
   * - Unique ID
     - The naming scheme for the UID is defined here: :need:`gd_req__arch__attribute_uid`
   * - Title
     - The title of the architectural element shall be expressive.
   * - Status
     - Status of the architectural element [valid,invalid]
   * - Safety
     - This attribute describes the impact of the architectural element on functional safety. Currently only following values are defined [QM, ASIL_B, ASIL_D]. Other values are not required at the moment as *ASIL decomposition* is not used so far.
   * - Security
     - This attribute describes if the architectural element has any impact on the security of the platform. [YES,NO]
   * - Fulfils
     - With this attribute the relations to the corresponding requirements shall be described

For creating architectural elements also templates for each level are available:

* Feature Architecture: :need:`[[title]] <gd_temp__arch__feature>`
* Component Architecture: :need:`[[title]] <gd_temp__arch__comp>`

.. _traceability of the architecture:

Establish traceability between requirements and architectural elements
**********************************************************************

During the architectural design process all feature and component requirements shall be allocated to a single architecture element at the corresponding level via the attribute **fulfils**.

.. _reviews of the architecture:

Reviews of the architecture
***************************

Some of the checks cannot be performed automatically. Therefore a manual inspection of the architecture is needed. The architecture review itself is included in the PR review which is triggered if a contributor wants to commit code to the main line. For this review a checklist is available: :need:`gd_chklst__arch__inspection_checklist`.
