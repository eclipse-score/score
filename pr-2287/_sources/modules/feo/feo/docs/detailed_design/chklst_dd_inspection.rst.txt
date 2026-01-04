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

.. document:: FEO Implementation Inspection Checklist
   :id: doc__impl_inspection_component_feo
   :status: draft
   :security: NO
   :safety: ASIL_B
   :tags: component_feo
   :realizes: wp__sw_implementation_inspection

FEO Implementation Inspection Checklist
=======================================

Purpose
-------

The purpose of this checklist is to collect the topics to be checked during implementation,
i.e. in the detailed design and the source code of the units.

The checklist shall be agnostic to which programming language is used. Differences shall be treated
by linking to C++ or Rust specific documentation.

Checklist
---------

.. list-table:: FEO Implementation Checklist
   :header-rows: 1
   :widths: 10,30,50,6,6,8

   * - Review ID
     - Acceptance Criteria
     - Guidance
     - Passed
     - Remarks
     - Issue link
   * - IMPL_01_01
     - Is the design according to guidelines?
     - see :need:`gd_temp__detailed_design` and :need:`doc_concept__imp_concept`
       (e.g. are the views done with the proposed UML diagrams)
     -
     -
     -
   * - IMPL_01_02
     - Is the implementation according to specification?
     - Check if the linked component requirements are fulfilled
       and detailed design also matches architecture description.
     -
     -
     -
   * - IMPL_01_03
     - Are the design decisions and constraints documented?
     - Check also for plausibility of these.
     -
     -
     -
   * - IMPL_01_04
     - Are all external libraries used by the component specified in the detailed design?
     - Check the automated dependency analysis.
       Also make sure ASIL rated units also only use ASIL or FFI rated libraries.
     -
     -
     -
   * - IMPL_02_01
     - Are the static and dynamic code analysis reports verified for violations?
     - All violations in ASIL related code must be justified. This includes the checks of coding guidelines.
     -
     -
     -
   * - IMPL_02_02
     - Do manual checks, that are derived from the coding guideline, find no safety critical error?
     - Check this list for C++ <link> and this list for Rust <link>
     -
     -
     -
   * - IMPL_02_03
     - Are detailed design and source code consistent?
     - Check if the static and dynamic design descriptions match the code (e..g. naming of elements)
       and that the respective traceability is established (doxygen style comments)
     -
     -
     -
