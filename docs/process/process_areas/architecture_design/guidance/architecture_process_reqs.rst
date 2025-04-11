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

.. _arch_process_requirements:

Process Requirements
====================

Architectural Structuring
-------------------------

.. gd_req:: Hierarchical structure of architectural elements
   :id: gd_req__arch__hierarchical_structure
   :status: valid
   :complies: std_req__iso26262__support_6431, std_req__iso26262__support_6432
   :satisfies: wf__cr_mt_featarch

   Architectural elements shall be hierarchically structured on two levels:

   * Feature
   * Component

   Additionally there shall be a view for the *Top Level SW component* container.

.. gd_req:: Architecture Views
   :id: gd_req__arch__viewpoints
   :status: valid
   :complies: std_req__iso26262__support_6432, std_req__iso26262__software_742
   :satisfies: wf__cr_mt_featarch

   The architecture shall be shown with following views on each architectural level:

   * static view
   * dynamic view
   * interface view

   An additional view only shall be created on module level.

.. gd_req:: Architecture Modeling
   :id: gd_req__arch__model
   :status: valid
   :complies: std_req__iso26262__support_6431, std_req__iso26262__support_6432
   :satisfies: wf__cr_mt_featarch

   For architecture design a model based approach should be used.

.. gd_req:: Structuring of the architectural building blocks
   :id: gd_req__arch__build_blocks
   :status: valid
   :complies: std_req__iso26262__support_6431, std_req__iso26262__support_6432
   :satisfies: wf__cr_mt_featarch

   For modeling the viewpoints following elements shall be used:

   * Feature
   * Module
   * Component
   * Logical Interfaces
   * Interfaces
   * Interface Operation

.. gd_req:: Correlations of the architectural building blocks
   :id: gd_req__arch__build_blocks_corr
   :status: valid
   :complies: std_req__iso26262__support_6431, std_req__iso26262__support_6432
   :satisfies: wf__cr_mt_featarch

   For modeling the viewpoints following relations shall be used:

   .. figure:: ../_assets/metamodel_architectural_design.drawio.svg
      :width: 100%
      :align: center
      :alt: Definition of the Metamodel for Architectural Design

.. gd_req:: Building Blocks Dynamic Architecture
   :id: gd_req__arch__build_blocks_dynamic
   :status: valid
   :satisfies: wf__cr_mt_featarch

   It shall be possible to provide the required architectural building blocks inside the dynamic architecture.

Attributes of Architectural Elements
------------------------------------

.. gd_req:: Architecture attribute: UID
   :id: gd_req__arch__attribute_uid
   :status: valid
   :tags: attribute,mandatory
   :complies: std_req__iso26262__support_6425, std_req__iso26262__support_6432

   Each architectural element shall have a unique ID. It shall be in a format which is also human readable and consists of

      * type of architectural element
      * last part of the feature tree
      * keyword describing the content of the requirement.

   The naming convention is defined here: :ref:`naming_convention_needs`

.. gd_req:: Architecture attribute: security
   :id: gd_req__arch_attr_security
   :status: valid
   :tags: attribute, mandatory

   Each requirement shall have a security relevance identifier:

      * Yes
      * No

.. gd_req:: Architecture attribute: safety
   :id: gd_req__arch__attr_safety
   :status: valid
   :tags: attribute, mandatory
   :complies: std_req__iso26262__support_6421, std_req__iso26262__support_6425

   Each requirement shall have a automotive safety integrity level (ASIL) identifier:

      * QM
      * ASIL_B
      * ASIL_D

.. gd_req:: Architecture attribute: status
   :id: gd_req__arch__attr_status
   :status: valid
   :tags: attribute, mandatory
   :complies: std_req__iso26262__support_6425

   Each requirement shall have a status:

      * valid
      * invalid

.. gd_req:: Architecture attribute: fulfils
   :id: gd_req__arch__attr_fulfils
   :status: valid
   :tags: attribute, mandatory
   :complies: std_req__iso26262__support_6425

   Each architectural element shall have a link to a requirement.

Traceability to Requirements
----------------------------

.. gd_req:: Architecture traceability
   :id: gd_req__arch__traceability
   :status: valid
   :tags: architecture_design
   :complies: std_req__iso26262__support_6432
   :satisfies: wf__cr_mt_featarch

   Requirements shall be fulfilled by the architecture at the corresponding level.

   **Examples:**

   * feat_req <-> feat_arch_(sta|dyn|int)
   * comp_req <-> comp_arch_(sta|dyn|int)

   .. note::
      In general the traceability is visualized in :numref:`wp_traceability_model`

Checks for Architectural Design
-------------------------------

.. gd_req:: Architecture mandatory attributes
   :id: gd_req__arch__attr_mandatory
   :status: valid
   :tags: attribute, check

   It shall be checked if all mandatory attributes for each architectural element is provided by the user. For all elements following attributes shall be mandatory:

   .. needtable:: Overview mandatory requirement attributes
      :filter: "mandatory" in tags and "attribute" in tags and "architecture_design" in tags and type == "gd_req"
      :style: table
      :columns: title
      :colwidths: 30

.. gd_req:: Architecture linkage safety
   :id: gd_req__arch__linkage_safety
   :status: valid
   :tags: attribute, check

   It shall be checked that every valid safety architectural element is linked against its top level element as defined in :need:`gd_req__arch__build_blocks_corr`.

.. gd_req:: Architecture linkage requirement
   :id: gd_req__arch__linkage_requirement
   :status: valid
   :tags: attribute, check

   It shall be checked that each architectural element (safety!=QM) is linked against a safety requirement (safety!=QM).

.. gd_req:: Architecture linkage requirement type
   :id: gd_req__arch__linkage_requirement_type
   :status: valid
   :tags: attribute, check

   It shall be checked that requirements can only be linked to architectural elements according to the defined traceability:

   * Functional feature requirements <-> static / dynamic feature architecture
   * Interface feature requirements <-> interface feature architecture
   * Functional component requirements <-> static / dynamic component architecture
   * Interface component requirements <-> interface component architecture

.. gd_req:: Architecture linkage safety
   :id: gd_req__arch__linkage_safety_trace
   :status: valid
   :tags: attribute, check

   It shall be checked that safety architectural elements (Safety != QM) can only be linked against safety architectural elements.

.. gd_req:: Architecture linkage security
   :id: gd_req__arch__linkage_security_trace
   :status: valid
   :tags: attribute, check

   It shall be checked that security relevant architectural elements (Security == YES) can only be linked against security relevant architectural elements.

.. gd_req:: Architecture check consistency modules
   :id: gd_req__arch__consistency_model
   :status: valid
   :tags: model, check

   It shall be checked if all mentioned SW components are available in the modules repository.

.. gd_req:: Architecture check consistency interfaces
   :id: gd_req__arch__consistency_interf
   :status: valid
   :tags: model, check

   It shall be checked if all mentioned component interfaces are available in the modules repository.

.. gd_req:: Architecture check consistency dynamic architecture
   :id: gd_req__arch__consistency_dynamic
   :status: valid
   :tags: model, check

   It shall be checked if all SW components which are mentioned in the dynamic architecture are defined in the static architecture.
