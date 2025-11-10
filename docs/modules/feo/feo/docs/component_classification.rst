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


.. document:: FEO Component Classification
   :id: doc__feo_comp_class
   :status: draft
   :security: NO
   :safety: ASIL_B
   :realizes: wp__sw_component_class
   :tags: component_feo

Component Classification
========================

| Classification of FEO Component
|
| <Link to OSS component source (e.g. in github) including the selected version>
|
| Additional documentation considered:
| <list of documentation links>


Step 1: Determine (P): the uncertainty of the Processes applied
---------------------------------------------------------------

| Apply the process measures to determine (P).
| The result of a process measure shall have as outcome [HE, PE, NE]
| - HE: High Evidence
| - PE: Partly Evidence but Manageable
| - NE: No Evidence

.. list-table:: Determine (P)
        :header-rows: 1

        * - Id
          - Indicator for applying process
          - Result
          - Rationale for result

        * - 1
          - Are rules, state-of-the art processes applied for the design, implementation and verification?
          - <HE|PE|NE>
          - <Rationale for result>

        * - 2
          - Are requirements available?
          - <HE|PE|NE>
          - <Rationale for result>

        * - 3
          - Are specifications for functionalities and properties available (architecture)?
          - <HE|PE|NE>
          - <Rationale for result>

        * - 4
          - Are design specifications available?
          - <HE|PE|NE>
          - <Rationale for result>

        * - 5
          - Are configuration specification and data available, if applicable?
          - <HE|PE|NE>
          - <Rationale for result>

        * - 6
          - Are verification measures including tests and reports available?
          - <HE|PE|NE>
          - <Rationale for result>


| (P=1) shall be selected when none of the determined process measures indicate PE or NE.
| (P=2) shall be selected when at least one of the determined process measures indicate PE or NE, but the gaps evaluated are acceptable, means
|       the risk of systematic faults due to these gaps is sufficiently low or manageable by mitigating the gaps.
| (P=3) in all other cases.

<component name> is determined as P=<1|2|3>


Step 2: Determine (C): the uncertainty of finding systematic faults based on the Complexity
-------------------------------------------------------------------------------------------

| Apply the complexity measures to determine (C).
| The result of a complexity measure shall have as outcome [NH, HM, NM]
| - NH: Not High
| - HM: High but Manageable
| - NM: high and Not Manageable
|
| **Complexity measure for programming language: <C++ or RUST>**

<select the correct table below (table for C++ is TBD)>

.. list-table:: Determine (C) for RUST
    :header-rows: 1

    * - Id
      - Indicator for high Complexity
      - Complexity measure Tool
      - Result
      - Number

    * - 1
      - High amount of Lines of Code
      - Lines of Code (without comments) (generated code is excluded, e.g. ProtoCmpl)
      - <NH|HM|NM>
      - <Number>

    * - 2
      - Unsafe code used / total unsafe code
      - Count:
            * LoUC+N: lines of unsafe code with safety note
            * LoUC  : lines of unsafe code, no safety note
      - <NH|HM|NM>
      - <Number>

    * - 3
      - | Test exists / Coverage (Function, Line)
        | (maybe better: testability, but how to measure?)
      - Existing Tests Coverage
      - <NH|HM|NM>
      - <Number>

    * - 4
      - High amount of public function interfaces
      - Number of public function interfaces
      - <NH|HM|NM>
      - <RNumber>

    * - 5
      - High amount of function parameters
      - Number of parameters
      - <NH|HM|NM>
      - <Number>


| (C=1) shall be selected when none of the determined complexity measures indicate HM or NM.
| (C=2) shall be selected when at least one of the determined complexity measures indicate HM or NM, but the gaps evaluated are acceptable, means
|       the risk of systematic faults due to these gaps is sufficiently low in the context of the project or manageable by mitigating the gaps.
| (C=3) in all other cases.
|

<component name> is determined as C=<1|2|3>


Step 3: Determine (CLAS_OUT): the classification outcome
--------------------------------------------------------

| Select CLAS_OUT depending on the determined values of (C) and (P)

+-------+-----------------------+
| ( C ) | ( P )                 |
+-------+-------+-------+-------+
|       |  1    |  2    |  3    |
+=======+=======+=======+=======+
| 1     |  Q    |  Q    | QR    |
+-------+-------+-------+-------+
| 2     |  QR   | QR    | QR    |
+-------+-------+-------+-------+
| 3     |  QR   | QR    | NQ    |
+-------+-------+-------+-------+

<component name> is classified as CLAS_OUT=<Q|QR|NQ>


Step 4: Document all results and rationale for choosing (P) and (C) and (CLAS_OUT)
----------------------------------------------------------------------------------
This document


Step 5: Based on (CLAS_OUT) select the activities
-------------------------------------------------

| As soon as the change request containing this is in status "Accepted", the module safety plan for the component development is adapted based on the following: (select according to above result)
| - Q: Follow the processes for qualification of software components in a safety context.
| - QR: Follow the process for pre-existing software architectural elements
| - NQ: Do no use this element in safety context
