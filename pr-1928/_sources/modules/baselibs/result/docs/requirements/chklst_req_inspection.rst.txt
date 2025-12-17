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


.. document:: Result Library Requirements Inspection Checklist
   :id: doc__result_library_req_inspection
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_inspect


Requirement Inspection Checklist
================================

   **Purpose**
   The purpose of this requirement inspection checklist is to collect the topics to be checked during requirements inspection.

   **Conduct**

   As described in the concept :need:`doc_concept__wp_inspections` the following "inspection roles" are expected to be filled:

   - author: these are the persons who did the last commits on the requirements in scope (can be derived from version mgt tool)
   - reviewer: these are all persons committing into this inspection document or giving a pull request verdict on it (can be derived from version mgt tool)
   - moderator: only needed for conflict resolution between author and reviewers, is the safety manager, security manager or quality manager called in as a reviewer (can be derived from version mgt tool)
   - test expert: `<https://github.com/rahulthakre29>`_

   **Checklist**

   .. list-table:: Component Requirement Inspection Checklist
      :header-rows: 1
      :widths: 10,30,50,6,6,8

      * - Review ID
        - Acceptance Criteria
        - Guidance
        - Passed
        - Remarks
        - Issue link
      * - REQ_01_01
        - Is the requirement formulation template used?
        - see :need:`gd_temp__req_formulation`, this includes the use of "shall".
        - YES
        - none
        - none
      * - REQ_02_01
        - Is the requirement description *comprehensible* ?
        - If you think the requirement is hard to understand, comment here.
        - YES
        - Fixed: :need:`comp_req__result__std_integration` : it is not clear what "standard library optional type, with enforced error handling" means.
        - `#2229 <https://github.com/eclipse-score/score/issues/2229>`_
      * - REQ_02_02
        - Is the requirement description *unambiguous* ?
        - Especially search for "weak words" like "about", "etc.", "relevant" and others (see the internet documentation on this). This check shall be supported by tooling.
        - YES
        - Fixed: :need:`aou_req__result__thread_safety` : uses "appropriate"
        - `#2229 <https://github.com/eclipse-score/score/issues/2229>`_
      * - REQ_02_03
        - Is the requirement description *atomic* ?
        - A good way to think about this is to consider if the requirement may be tested by one (positive) test case or needs more of these. The sentence template should also avoid being non-atomic already. Note that there are cases where also non-atomic requirements are the better ones, for example if those are better understandable.
        - YES
        - (old) finding explained
        - none
      * - REQ_02_04
        - Is the requirement description *feasible* ?
        - If at the time of the inspection the requirement has already some implementation, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_impl` shows this. In case the requirement has no implementationat the time of inspection (i.e. not implemented at least as "proof-of-concept"), a development expert shall be invited to the inspection to explicitly check this item.
        - YES
        - existing implementation taken over by S-CORE baselibs
        - none
      * - REQ_02_05
        - Is the requirement description *independent from implementation* ?
        - This checkpoint should improve requirements definition in the sense that the "what" is described and not the "how" - the latter should be described in architecture/design derived from the requirement. But there can also be a good reason for this, for example we would require using a file format like JSON and even specify the formatting standard already on stakeholder requirement level because we want to be compatible. A finding in this checkpoint does not mean there is a safety problem in the requirement.
        - YES
        - This is appropriate for the component level. No use of exceptions and standard library relation is a S-CORE platform condition.
        - none
      * - REQ_03_01
        - For stakeholder requirements: Is the *rationale* correct?
        - Rationales explain why the top level requirements were created. Do those cover the requirement?
        - n/a
        - no stakeholder requirements in scope
        - n/a
      * - REQ_03_02
        - For other requirements: Is the *linkage to the parent requirement* correct?
        - Linkage to correct levels and ASIL attributes is checked automatically, but it needs checking if the child requirement implements (at least) a part of the parent requirement.
        - YES
        - linking is appropriate, that it exists is checked automatically
        - none
      * - REQ_04_01
        - Is the requirement *internally and externally consistent*?
        - Does the requirement contradict other requirements within the same or higher levels? One may restrict the search to the feature for component requirements, for features to other features using same components.
        - YES
        - no contradicting requirements or AoU found in the Result component requirements and the linked feature requirements.
        - none
      * - REQ_05_01
        - Do the software requirements consider *timing constraints*?
        - Think about timing constraints even if those are not explicitly mentioned in the parent requirement. If the reviewer of a requirement already knows or suspects that the code execution will be consuming a lot of time, one should think of the expectation of a "user".
        - YES
        - No timing requirements found and also no timing problems expected
        - none
      * - REQ_06_01
        - Does the requirement set consider *external interfaces*?
        - The SW platform's external interfaces (to the user) are defined in the Feature Architecture, so the Feature and Component Requirements should determine the input data use and setting of output data for these interfaces. Are all output values defined?
        - YES
        - Fixed: This could be improved by using the interfaces defined in :need:`comp_arc_sta__baselibs__result`
        - `#2229 <https://github.com/eclipse-score/score/issues/2229>`_
      * - REQ_07_01
        - Is the *safety* attribute set correctly?
        - Derived requirements are checked automatically, see :need:`gd_req__req_linkage_safety`. But for the top level requirements (and also all AoU) this needs to be checked manually for correctness.
        - YES
        - all requirements are ASIL B as expected
        - none
      * - REQ_07_02
        - Is the attribute *security* set correctly?
        - Stakeholder requirements security attribute should be set based on Threat Analysis and Risk Assessment (TARA) (process is TBD). For feature/component requirements this checklist item is supported by automated check: "Every requirement which satisfies a requirement with security attribute set to YES inherits this". But the feature/component requirements/architecture may additionally also be subject to a Software Security Criticality Analysis (process is TBD).
        - YES
        - all requirements have no security implication as expected (no security impact analysis done)
        - none
      * - REQ_08_01
        - Is the requirement *verifiable*?
        - If at the time of the inspection already tests are created for the requirement, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_test_covered` shows this. In case the requirement is not sufficiently traced to test cases already, a test expert is invited to the inspection to give his opinion whether the requirement is formulated in a way that supports test development and the available test infrastructure is sufficient to perform the test.
        - YES
        - all requirements have test cases implemented
        - none
      * - REQ_09_01
        - For stakeholder requirements: Do those cover assumed safety mechanisms needed by the hardware and system?
        - Note that stakeholder requirements covering safety mechanisms come from rationales, whereas feature/component requirements are covering safety mechanisms coming from :need:`gd_chklst__safety_analysis`
        - n/a
        - no stakeholder requirements in scope
        - n/a
      * - REQ_09_02
        - For feature/component requirements: Do the requirements defining a safety mechanism contain the error reaction leading to a safe state?
        - Alternatively to the safe state there could also be "repair" mechanisms. Also do not forget to consider REQ_05_01 for these.
        - YES
        - Fixed: There should be an AoU covering this, :need:`aou_req__result__value_handling` is not.
        - `#2229 <https://github.com/eclipse-score/score/issues/2229>`_

Note: If a Review ID is not applicable for your requirement, then state "n/a" in status and comment accordingly in remarks. For example "no stakeholder requirement (no rationale needed)"

The following requirements in "valid" state and with "inspected" tag set are in the scope of this inspection:

.. needtable::
   :filter: docname is not None and "result" in docname and "requirements" in docname and status == "valid"
   :style: table
   :types: comp_req
   :tags: result_library
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title


And also the following AoUs in "valid" state and with "inspected" tag set (for these please answer
the questions above as if the AoUs are requirements, except questions REQ_03_01 and REQ_03_02):

.. needtable::
   :filter: docname is not None and "result" in docname and "requirements" in docname and status == "valid"
   :style: table
   :types: aou_req
   :tags: result_library
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
