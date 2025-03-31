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

Component Classification Guideline
==================================

.. gd_guidl:: Classification of a component
   :id: gd_guidl__component_classification
   :status: valid
   :complies: std_req__isopas8926__441, std_req__isopas8926__4421, std_req__isopas8926__4422, std_req__isopas8926__4423, std_req__isopas8926__4424, std_req__isopas8926__4425, std_req__isopas8926__4426, std_req__isopas8926__4427, std_req__isopas8926__4428, std_req__isopas8926__4429, std_req__isopas8926__44210, std_req__isopas8926__44321, std_req__isopas8926__44322, std_req__isopas8926__4433

Purpose
-------
Re-use of existing elements like open source software in safety context is wanted.

Objectives
----------
Definition of a method to classify existing elements to be qualifiable for a safety context.

The classification shall have three outcomes:

* Existing element is qualifiable according part 8 clause 12 of ISO 26262 for the safety context (Q)
* Existing element may qualifiable for the safety context, but some additional effort is required (QR)
* Existing element is NOT qualifiable for the safety context (NQ)

Approach
--------

The classification is based on two criteria:

* The uncertainty of the Processes (P) applied for the development of the existing element
* The uncertainty of finding systematic faults based on the Complexity (C) of the existing element

| Assumption is that the context for the usage of the existing element is always the operation environment and context of the *S-CORE* platform.
| (P) shall be natural values out of the set[1,2,3]
| (C) shall be natural values out of the set[1,2,3]
|
| Both criteria may influence the presence of systematic faults, which may increases the likelihood for violating safety relevant requirements allocated to the existing element.
|
| The outcome of the classification (CLAS_OUT) shall be a function of (P) and (C).
| (CLAS_OUT) shall be values out of the set[Q, QR, NQ]
|
| Step 1: Determine (P): the uncertainty of the Processes applied
| Step 2: Determine (C): the uncertainty of finding systematic faults based on the Complexity
| Step 3: Determine (CLAS_OUT): the classification outcome
| Step 4: Document all results and rationale for choosing (P) and (C) and (CLAS_OUT)
| Step 5: Based on (CLAS_OUT) select the following activities:
|        - Q: Follow the processes for qualification of software components in a safety context.
|        - QR: Follow the process for impact analysis, define sub-elements, if applicable, define in the safety plan the additional effort required in addition to processes for qualification of software components
|        - NQ: Do no use this element in safety context
|

Figure 1: Overview of the workflow component classification

.. image:: _assets/wf_component_classification.drawio.svg
  :width: 800
  :alt: Overview of the workflow component classification



Step 1: Determination of (P)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apply the process measures to determine (P).

The result of a process measure shall have as outcome [NE, PE, NE]

* HE: High Evidence
* PE: Partly Evidence but Manageable within *S-CORE*
* NE: No Evidence

.. list-table:: Determination of P
    :header-rows: 1

    * - **Id**
      - **Indicator for applying process**
      - **Process measure/Tool**
      - **HE**
      - **PE**
      - **NE**
    * - 1
      - Are rules, state-of-the art processes applied for the design, implementation and verification?
      - Community Rules, Language specific compiler rules Rust: compiler (e.g. rustc) warnings, linter (e.g. clippy) warnings
      - available enforced
      - available
      - Not available
    * - 2
      - Are requirements available?
      - Documented requirements
      - available
      - available partly
      - Not available
    * - 3
      - Are specifications for functionalities and properties available (architecture)?
      - Documented functionalities and properties
      - available
      - available partly
      - Not available
    * - 4
      - Are design specifications available?
      - Documented specification
      - available
      - available partly
      - Not available
    * - 5
      - Are configuration specification and data available, if applicable?
      - Documented specification and data
      - available
      - available partly
      - Not available
    * - 6
      - Are verification measures including tests and reports available?
      - Available and executable tests
      - available passing
      - available partly pass
      - Not available
    * - 7
      - to be extended, if required
      -
      -
      -
      -


| (P=1) shall be selected when none of the determined process measures indicate PE or NE.
| (P=2) shall be selected when at least one of the determined process measures indicate PE or NE but the gaps evaluated are acceptable, means the risk of systematic faults due to these gaps is sufficiently low in the context of *S-CORE* or manageable by mitigating the gaps.
| (P=3) in all other cases.
|
| Other existing documentation could be used to cover lack in other documents 1-6 to get from NE to HE or PE


Step 2: Determination of (C)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Apply the complexity measures to determine (C).
| The result of a complexity measure shall have as outcome [NH, HM, NM]
| - NH: Not High
| - HM: High but Manageable within *S-CORE*
| - NM: high and Not Manageable within *S-CORE*

**Complexity measure for programming language: RUST**

.. list-table:: Determination of C
    :header-rows: 1

    * - **Id**
      - **Indicator for high complexity**
      - **Process measure/Tool**
      - **NH**
      - **HM**
      - **NM**
    * - 1
      - High amount of Lines of Code
      - Lines of Code (without comments), (generated code is excluded, e.g. ProtoCmpl)
      - lower as 1000
      - ~ 1000
      - higher as 1000
    * - 2
      - Unsafe code used / total unsafe code
      - Count:
            * LoUC+N: lines of unsafe code with safety note
            * LoUC  : lines of unsafe code, no safety note
      - lower as 10 LoUC+N
      - higher as 10 LoUC+N or lower as 10 LoUC
      - higher as 10 LoUC
    * - 3
      - Test exists / Coverage (Function, Line) (maybe better testability, but how to measure?)
      - Existing Tests / Coverage
      - Yes / higher 90%
      - Yes / higher 60%
      - No
    * - 4
      - High amount of public function interfaces
      - Number of public function interfaces
      - lower as 5
      - ~ 5
      - higher as 5
    * - 5
      - High amount of function parameters
      - Number of parameters
      - lower as 5
      - ~ 5
      - higher as 5
    * - 6
      - Cyclomatic complexity or others (t.b.d.)
      - rust-code-analysis (mozilla)  (?)
      - t.b.d
      - t.b.d
      - t.b.d
    * - 7
      - to be extended, if required
      -
      -
      -
      -

| **Complexity measure for programming language: CPP**
| TODO
|
| (C=1) shall be selected when none of the determined complexity measures indicate HM or NM.
| (C=2) shall be selected when at least one of the determined complexity measures indicate HM or NM, but the gaps evaluated are acceptable, means the risk of systematic faults due to these gaps is sufficiently low in the context of *S-CORE* or manageable by mitigating the gaps.
| (C=3) in all other cases.


Step 3: Determination of (CLAS_OUT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select CLAS_OUT depending on the determined values of (C) and (P)

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

Step 4: Document all results and rationale for choosing (P) and (C) and (CLAS_OUT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this the template :need:`gd_temp__component_classification` shall be used.

Step 5: Based on (CLAS_OUT) select the activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As soon as the contribution request containing this is in status "Accepted", the module safety plan for the component development is created/adapted based on the following: (select according to above result)

**If CLAS_OUT=Q : Follow the processes for qualification of software components in a safety context**

This is namely (for ASIL B) to provide the following work products according to the SW platform process:

* :need:`wp__requirements__comp` including their inspection
* :need:`wp__requirements__comp_aou` derived from the OSS components user manual and interface description, includes specification of the component's configuration
* :need:`wp__verification__component_test` to test requirement and AoU implementation

Integration of the OSS component is performed via the modules's SW build config and checked by feature integration tests (component integration if the OSS element is considered as a sub-component).

**If CLAS_OUT=QR : Follow the process for pre-existing software architectural elements**

* Based on the gaps detected in this classification which lead to a QR instead of a Q, add additional work products or improve the existing work products with the goal to get a better P or C rating ("1").
* In case of too high complexity based on the Ids 1 and 4, a :need:`wf__cr_mt_comparch` shall be derived from the OSS component source code and a classification done on the sub-components in this architecture. This could be repeated again and again until sufficiently low complex sub-components were broken down.
* If the classification of the (sub-)component is Q after the above, do as in section "Q:"

**If CLAS_OUT=NQ : Do no use this element in safety context**

* In case of NQ only the component classification document from Step 4 will be stored for this OSS component.
* Then either another OSS component will be selected or a development from scratch is planned.
