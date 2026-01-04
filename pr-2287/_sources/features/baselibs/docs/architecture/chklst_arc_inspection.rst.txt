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


Architecture Inspection Checklist
=================================

.. document:: Baselibs Architecture Inspection Checklist
   :id: doc__baselibs_arc_inspection
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_arch_verification

Purpose
-------

The purpose of the software architecture checklist is to ensure that the design meets the criteria and quality as
defined per S-CORE processes and guidelines for feature and component architectural design elements.
It helps to check the compliance with requirements, identify errors or inconsistencies, and ensure adherence to best
practices.
The checklist guides evaluation of the architecture design, identifies potential problems, and aids in
communication and documentation of architectural decisions to stakeholders.

Checklist
---------

.. list-table:: Architecture Design Review Checklist
    :header-rows: 1

    * - Review Id
      - Acceptance criteria
      - Type
      - Guidance
      - passed
      - Remarks
      - Issue link
    * - ARC_01_01
      - Is the traceability from software architectural elements to requirements, and other level architectural
        elements (e.g. component to interface) established according to the "Relations between the architectural elements" as described in :need:`doc_concept__arch_process`?
      - automated
      - Trace should be checked by Sphinx. Will be removed from checklist once requirement is implemented.
      -
      -
      -
    * - ARC_01_02
      - If the architectural element is related to any supplier manuals (incl. safety and security)
        are the relevant parts covered?
      - manual
      - If the architecture makes use of supplied elements, their manuals (like safety) have to be considered (i.e. its provided functionality matches the expectation and assumptions are fulfilled). Note that in case of safety component this means that assumed Technical Safety Requirements and AoUs of the safety manual are covered.
      -
      -
      -
    * - ARC_01_03
      - Is the architectural element traceable to the lower level artifacts as defined by the workproduct traceability?
      - automated
      - Will be removed from checklist once requirement is implemented by automated tool check.
        Details of possible linking can be depicted from `traceability concept <https://eclipse-score.github.io/process_description/main/general_concepts/score_traceability_concept.html>`_
      -
      -
      -
    * - ARC_02_01
      - Is the software architecture design compliant with the (overall) feature architecture?
      - manual
      - On component level check against the feature architecture, on feature level check other features with common components used.
      -
      -
      -
    * - ARC_02_02
      - Is appropriate and comprehensible operation/interface naming present in the architectural design?
      - manual
      - Check :need:`gd_guidl__arch_design`
      -
      -
      -
    * - ARC_02_03
      - Are correctness of data flow and control flow within the architectural elements considered?
      - manual
      - E.g. examine definitions, transformations, integrity, and interaction of data; check error handling, data
        exchange between elements, correct response to inputs and documented decision making.
        Note: consistency is ensured by the process/tooling, by defining each interface only once.
      -
      -
      -
    * - ARC_02_04
      - Are the interfaces between the software architectural element and other architectural elements well-defined?
      - manual
      - Check if the interface reacts on non-defined behavior or errors; can established protocols be used; are the
        interfaces for inputs, outputs, error codes documented; is loose coupling considered and only limited exposure;
        can unit or integration test be written against the interface; data amount transferred; no sensitive data
        exposure;
      -
      -
      -
    * - ARC_02_05
      - Does the software architectural element consider the timing constraints (from the parent requirement)?
      - manual
      - If there are hard requirements on the timing a programming time estimation should be performed and also
        deadline supervision considered.
      -
      -
      -
    * - ARC_02_06
      - Is the documentation of the software architectural element, including textual and graphical descriptions
        (e.g., UML diagrams), comprehensible and complete?
      - manual
      - Use of semi-formal notation is expected for architectural elements with an allocated ASIL level.
        Is the architecture template correctly filled?
      -
      -
      -
    * - ARC_03_01
      - Is the architectural element modular and encapsulated?
      - manual
      - Check e.g. that only minimal interfaces are used. Design should be object oriented. Interfaces and interactions are clearly defined. Usage of access types (private, protected) properly set. Limited global variables.
      -
      -
      -
    * - ARC_03_02
      - Is the suitability of the software architecture for future modifications and maintainability considered?
      - manual
      - Check for e.g. loose coupling, separation of concerns, high cohesion, versioning strategy for interfaces,
        decision records, use of established design patterns.
      -
      -
      -
    * - ARC_03_03
      - Are simplicity and avoidance of unnecessary complexity present in the software architecture?
      - manual
      - Indicators for complexity are: number of use cases (corresponding to dynamic diagrams)
        allocated to single design element, number of interfaces and operations in an interface,
        function parameters, global variables, complex types, limited comprehensibility.

        Note: If the "number" above exceeds "3" a design rationale is mandatory (for all types)
      -
      -
      -
    * - ARC_03_04
      - Is the software architecture design following best practices and design principles?
      - manual
      - Refer to architectural guidelines and recommendations within the project documentation.
      -
      -
      -
