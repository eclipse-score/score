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


.. document:: Json Architecture Inspection Checklist
   :id: doc__json_arc_inspection
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_arch_verification

Architecture Inspection Checklist
=================================

Purpose
-------

The purpose of the software architecture checklist is to ensure that the design meets the criteria and quality as
defined per project processes and guidelines for feature and component architectural design elements.
It helps to check the compliance with requirements, identify errors or inconsistencies, and ensure adherence to best
practices.
The checklist guides evaluation of the architecture design, identifies potential problems, and aids in
communication and documentation of architectural decisions to stakeholders.

Conduct
-------

As described in the concept :need:`doc_concept__wp_inspections` the following "inspection roles" are expected to be filled:

- content responsible (author): <contributor/committer explicitly named here, who is the main author, as can be seen in config mgt tooling>
- reviewer: <contributor/committer explicitly named here, who is the main content reviewer, must be different from content responsible>
- moderator: <committer explicitly named here, who is is the safety manager, security manager or quality manager initiating the inspection>

Checklist
---------

It is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additionally to add in the remarks why it is passed or not passed.
In case of "no" an issue link to the issue tracking system has to be added in the last column (if not solved in the same issue).
See also :need:`doc_concept__wp_inspections` for further information about reviews in general and inspection in particular.

.. list-table:: Architecture Design Review Checklist
    :header-rows: 1

    * - Review Id
      - Acceptance criteria
      - Guidance
      - passed
      - Remarks
      - Issue link
    * - ARC_01_01
      - Is the traceability from software architectural elements to requirements, and other level architectural elements (e.g. component to interface) established according to the "Relations between the architectural elements" as described in :need:`doc_concept__arch_process`?
      - automated
      - Trace should be checked automatically by tool support in the future. Will be removed from the checklist once the requirement (:need:`Correlations of the architectural building blocks <gd_req__arch_build_blocks_corr>`) is implemented. Refer to `Tool Requirements <https://eclipse-score.github.io/docs-as-code/main/internals/requirements/requirements.html>`_ for the current status.
      -
      -
    * - ARC_01_02
      - Does the software architecture design consider all the requirements allocated or belonging to the architectural element, including functional, non-functional, safety, and security requirements and all related design decisions?
      - manual
      - Check if all requirements allocated or belonging to the architectural element are considered in the design. This includes functional requirements (e.g. functional safety requirements), non-functional requirements (e.g. performance, reliability), and security requirements (e.g. confidentiality, integrity). Additionally, ensure that all related design decisions are taken into account and documented in the architectural design.
      -
      -
    * - ARC_01_03
      - If the architectural element is related to any supplier manuals (incl. safety and security)
        are the relevant parts covered?
      - If the architecture makes use of supplied elements, their manuals (like safety) have to be considered (i.e. its provided functionality matches the expectation and assumptions are fulfilled). Note that in case of safety component this means that assumed Technical Safety Requirements and AoUs of the safety manual are covered.
      -
      -
      -
    * - ARC_01_04
      - Is the architectural element traceable to the lower level artifacts as defined by the workproduct traceability?
      - Will be removed from checklist once the requirement (:need:`Correlations of the architectural building blocks <gd_req__arch_build_blocks_corr>`) is implemented by automated tool check. See `Tool Requirements <https://eclipse-score.github.io/docs-as-code/main/internals/requirements/requirements.html>`_.
        Details of possible linking can be depicted from :need:`doc_concept__general_traceability`.
      -
      -
      -
    * - ARC_02_01
      - Is the software architecture design compliant with the (overall) feature architecture?
      - On component level check against the feature architecture, on feature level check other features with common components used.
      -
      -
      -
    * - ARC_02_02
      - Is appropriate and comprehensible operation/interface naming present in the architectural design?
      - Check :need:`gd_guidl__arch_design`
      -
      -
      -
    * - ARC_02_03
      - Are correctness of data flow and control flow within the architectural elements considered?
      - E.g. examine definitions, transformations, integrity, and interaction of data; check error handling, data
        exchange between elements, correct response to inputs and documented decision making.
        Note: consistency is ensured by the process/tooling, by defining each interface only once.
      -
      -
      -
    * - ARC_02_04
      - Are the interfaces between the software architectural element and other architectural elements well-defined?
      - Check if the interface reacts on non-defined behaviour or errors; can established protocols be used; are the
        interfaces for inputs, outputs, error codes documented; is loose coupling considered and only limited exposure;
        can unit or integration test be written against the interface; data amount transferred; no sensitive data
        exposure;
      -
      -
      -
    * - ARC_02_05
      - Does the software architectural element consider the timing constraints (from the parent requirement)?
      - If there are hard requirements on the timing a programming time estimation should be performed and also
        deadline supervision considered.
      -
      -
      -
    * - ARC_02_06
      - Is the documentation of the software architectural element, including textual and graphical descriptions
        (e.g., UML diagrams), comprehensible and complete?
      - Use of semi-formal notation is expected for architectural elements with an allocated ASIL level.
        Is the architecture template correctly filled?
      -
      -
      -
    * - ARC_03_01
      - Is the architectural element modular and encapsulated?
      - Check e.g. that only minimal interfaces are used. Design should be object oriented. Interfaces and interactions are clearly defined. Usage of access types (private, protected) properly set. Limited global variables.
      -
      -
      -
    * - ARC_03_02
      - Is the suitability of the software architecture for future modifications and maintainability considered?
      - Check for e.g. loose coupling, separation of concerns, high cohesion, versioning strategy for interfaces,
        decision records, use of established design patterns.
      -
      -
      -
    * - ARC_03_03
      - Are simplicity and avoidance of unnecessary complexity present in the software architecture and the component?
      - Indicators for complexity are: number of use cases (corresponding to dynamic diagrams)
        allocated to single design element, number of interfaces and operations in an interface,
        function parameters, global variables, complex types, limited comprehensibility.
        The belonging code metrics (see :need:`gd_req__impl_complexity_analysis`) should be checked.

        Notes:

        If the "number of use cases" or "number of interfaces" above exceeds "3" or "number of function parameters" exceeds "5" or the "number of operations" exceeds "20" or global variables are used, a design rationale is mandatory.

        See also if component classification :need:`gd_temp__component_classification` as measure is present.

      -
      -
      -
    * - ARC_03_04
      - Is the software architecture design following best practices and design principles?
      - Refer to architectural guidelines and recommendations within the project documentation.
      -
      -
      -
    * - ARC_04_03
      - If your software architectural design of the component includes processes and tasks, are their scheduling policies and priorities (at least the needed relation one to another) defined to ensure that timing requirements are met? Please note, that the particular priorities or priority ranges will be probably defined by the project handbook or the software development plan.

        Note: see :need:`std_req__iso26262__software_743`
      - Give a reason for these scheduling policies and priorities or explain why not needed.
      -
      -
      -


.. attention::
    The above checklist entries must be filled according to your component architecture in scope.

Note: If a Review ID is not applicable for your architecture, then state ""n/a" in status and comment accordingly in remarks.

The following static views in "valid" state and with "inspected" tag set are in the scope of this inspection:

.. needtable::
   :filter: "json" in docname and "architecture" in docname and docname is not None and status == "valid"
   :style: table
   :types: comp_arc_sta
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

and the following dynamic views:

.. needtable::
   :filter: "json" in docname and "architecture" in docname and docname is not None and status == "valid"
   :style: table
   :types: comp_arc_dyn
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
