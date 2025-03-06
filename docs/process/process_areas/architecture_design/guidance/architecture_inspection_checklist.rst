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

.. _architecture_inspection_checklist:

Inspection Checklist Template
=============================

.. gd_chklst:: Architecture Inspection Checklist Template
    :id: gd_chklst__arch__inspection_checklist
    :status: valid
    :tags: architecture_design
    :complies: std_req__iso26262__software_10

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
      - ASIL (marks level from which check is applicable)
      - passed
      - Remarks
      - Issue link
    * - ARC_01_01
      - Is the traceability from software architectural elements to requirements, and other level architectural
        elements (e.g. component to interface) established according to the defined :ref:`metamodel<metamodel_architectural_design>`?
      - automated
      - QM
      -
      - Trace should be checked by Sphinx. Will be removed from checklist once requirement is implemented.
      -
    * - ARC_01_02
      - Is each architectural element traceable by its own identifier?
      - automated
      - QM
      -
      - Ids for architectural elements are enforced by tool. Will be removed from checklist once requirement is implemented.
      -
    * - ARC_01_03
      - If the architectural element is related to any supplier manuals (incl. safety and security)
        are the relevant parts covered?
      - manual
      - >= ASIL_B
      -
      - If the architecture makes use of supplied elements, their manuals (like safety) and AoUs have to be considered.
      -
    * - ARC_01_04
      - Is the architectural element traceable to the lower level artifacts as defined by the workproduct traceability?
      - automated
      - QM
      -
      - Will be removed from checklist once requirement is implemented by automated tool check.
        Details of possible linking can be depicted from :ref:`wp_traceability_model`
      -
    * - ARC_02_01
      - Is the software architecture design compliant with the overall platform/feature architecture?
      - manual
      - QM
      -
      - Check against platform overview and related platform artifacts as per workproducts definition.
        Also consider :ref:`arch_design_process`
      -
    * - ARC_02_02
      - Is appropriate and comprehensible variable/function/interface naming present in the architectural design?
      - manual
      - QM
      -
      - Check :ref:`arch_design_guideline`
      -
    * - ARC_02_03
      - Are consistency and correctness of data flow and control flow within the architectural elements considered?
      - manual
      - QM
      -
      - E.g. examine definitions, transformations, integrity, and interaction of data; check error handling, data
        exchange between elements, correct response to inputs, no unreachable code, and documented decision making.
      -
    * - ARC_02_04
      - Are the interfaces between the software architectural element and other architectural elements well-defined?
      - manual
      - QM
      -
      - Check if the interface reacts on non-defined behaviour or errors; can established protocols be used; are the
        interfaces for inputs, outputs, error codes documented; is loose coupling considered and only limited exposure;
        can unit or integration test be written against the interface; data amount transferred; no sensitive data
        exposure;
      -
    * - ARC_02_05
      - Does the software architectural element consider the timing constraints (from the parent relationship)?
      - manual
      - QM
      -
      -
      -
    * - ARC_02_06
      - Is the documentation of the software architectural element, including textual and graphical descriptions
        (e.g., UML diagrams), comprehensible and complete?
      - manual
      - QM
      -
      - Use of semi-formal notation is expected for architectural elements with an allocated ASIL level.
      -
    * - ARC_03_01
      - Is the architectural element modular and encapsulated?
      - manual
      - QM
      -
      - Check e.g. that only minimal interfaces are used. Design should be object oriented. Interfaces and interactions are clearly defined. Usage of access types (private, protected) properly set. Limited global variables.
      -
    * - ARC_03_02
      - Is the suitability of the software architecture for future modifications and maintainability considered?
      - manual
      - QM
      -
      - Check for e.g. loose coupling, separation of concerns, high cohesion, versioning strategy for interfaces,
        decision records, use of established design patterns.
      -
    * - ARC_03_03
      - Are simplicity and avoidance of unnecessary complexity present in the software architecture?
      - manual
      - QM
      -
      - Indicators for complexity are: number of requirements allocated to single design element, number of interfaces,
        parameters, global variables, complex types, limited comprehensibility.
      -
    * - ARC_03_04
      - Is the software architecture design following best practices and design principles?
      - manual
      - QM
      -
      - Refer to architectural guidelines and recommendations within the project documentation.
      -
