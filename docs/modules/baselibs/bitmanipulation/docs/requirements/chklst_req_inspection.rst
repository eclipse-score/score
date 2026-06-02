..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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


.. document:: Bitmanipulation Requirements Inspection Checklist
   :id: doc__bitmanipulation_req_inspection
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_inspect


Requirement Inspection Checklist
================================

   **Purpose**

   The purpose of this requirement inspection checklist is to collect the topics to be checked during requirements inspection.

   **Conduct**

   As described in the concept :need:`doc_concept__wp_inspections` the following "inspection roles" are expected to be filled:

   - content responsible (author): `<https://github.com/rutik7>`_
   - reviewer: `<https://github.com/mihajlo-k>`_
   - moderator: `<https://github.com/aschemmel-tech>`_
   - test expert: `<https://github.com/rahulthakre29>`_

   **Checklist**

   See also :need:`doc_concept__wp_inspections` for further information about reviews in general and inspection in particular.

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
        - Following requirements failed to comply with the requirements formulation template and were fixed in PR-2677:

          - :need:`aou_req__bitmanipulation__type_constraints`
          - :need:`aou_req__bitmanipulation__concurrent_access`
        -
      * - REQ_02_01
        - Is the requirement description *comprehensible* ?
        - If you think the requirement is hard to understand, comment here.
        - YES
        - The inspected requirements are clear and easy to understand. Some grammar mistakes were found and were fixed in PR-2677 and PR-2480:

          - :need:`comp_req__bitmanipulation__bit_operations`
          - :need:`aou_req__bitmanipulation__type_constraints`
          - :need:`aou_req__bitmanipulation__enum_constraints`
        -
      * - REQ_02_02
        - Is the requirement description *unambiguous* ?
        - Especially search for "weak words" like "about", "etc.", "relevant" and others (see the internet documentation on this). This check shall be supported by tooling.
        - YES
        - Following requirements had some ambiguities/weak word and were fixed in PR-2677:

          - :need:`comp_req__bitmanipulation__bit_operations`
          - :need:`comp_req__bitmanipulation__bounds_safety`
          - :need:`aou_req__bitmanipulation__enum_constraints`
        -
      * - REQ_02_03
        - Is the requirement description *atomic* ?
        - A good way to think about this is to consider if the requirement may be tested by one (positive) test case or needs more of these. The requirement formulation template should also avoid being non-atomic already. Note that there are cases where also non-atomic requirements are the better ones, for example if those are better understandable.
        - YES
        - One requirement was not atomic, this was fixed by splitting into these (PR-2677):

          - :need:`comp_req__bitmanipulation__bit_operations`
          - :need:`comp_req__bitmanipulation__byte_operations`
        -
      * - REQ_02_04
        - Is the requirement description *feasible* ?
        - If at the time of the inspection the requirement has already some implementation, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_impl` shows this. In case the requirement has no implementation at the time of inspection (i.e. not implemented at least as "proof-of-concept"), a development expert should be invited to the Pull-Request review to explicitly check this item.
        - YES
        - All requirements are already implemented at the time of this inspection.
        -
      * - REQ_02_05
        - Is the requirement description *independent from implementation* ?
        - This checkpoint should improve requirements definition in the sense that the "what" is described and not the "how" - the latter should be described in architecture/design derived from the requirement. But there can also be a good reason for this, for example we would require using a file format like JSON and even specify the formatting standard already on stakeholder requirement level because we want to be compatible. A finding in this checkpoint does not mean there is a safety problem in the requirement.
        - YES
        - Note on :need:`comp_req__bitmanipulation__header_only` - It's describing an implementation constraint, so it is a "how". However, this is a justified architectural decision, and it's analogous to the "JSON format" example from the checklist.
        -
      * - REQ_03_01
        - Is the *linkage to the parent feature/component requirement* correct?
        - Linkage to correct levels and ASIL attributes is checked automatically, but it needs checking if the child requirement implements (at least) a part of the parent requirement.
        - YES
        - The linkage to parent requirements is correct for all the requirements.
        -
      * - REQ_04_01
        - Is the requirement *internally and externally consistent*?
        - Does the requirement contradict other requirements within the same or higher levels? One may restrict the search to the feature for component requirements, for features to other features using same components.
        - YES
        - All the requirements are mutually consistent. However, there were inconsistencies between some requirements' titles and their descriptions, fixed in PR-2677:

          - :need:`aou_req__bitmanipulation__concurrent_access`
          - :need:`aou_req__bitmanipulation__enum_constraints`
        -
      * - REQ_05_01
        - Do the software requirements consider *timing constraints*?
        - This checkpoint encourages to think about timing constraints even if those are not explicitly mentioned in the parent requirement. If the reviewer of a requirement already knows or suspects that the code execution will be consuming a lot of time, one should think of the expectation of a "user".
        - YES
        - The overhead for bit manipulation operations is negligible.
        -
      * - REQ_06_01
        - Does the requirement consider *external interfaces*?
        - The SW platform's external interfaces (to the user) are defined in the Feature Architecture, so the Feature and Component Requirements should determine the input data use and setting of output data for these interfaces. Are all output values defined?
        - YES
        - For following requirements there was no description of the output, fixed in PR-2677:

          - :need:`comp_req__bitmanipulation__bit_operations`
          - :need:`comp_req__bitmanipulation__bounds_safety`

          Additionally, following requirement shows mismatch with the architecture, to be fixed by architecture update:

          - :need:`comp_req__bitmanipulation__byte_operations` - "extracting bytes and manipulating half-bytes" have no corresponding interface operations in the architecture.
        - #2698
      * - REQ_07_01
        - Is the *safety* attribute set correctly?
        - Derived requirements are checked automatically, see :need:`gd_req__req_linkage_safety`. But for the top level requirements (and also all AoU) this needs to be checked manually for correctness.
        - YES
        - All safety attributes set correctly.
        -
      * - REQ_07_02
        - Is the attribute *security* set correctly?
        - For component requirements this checklist item is supported by automated check: "Every requirement which satisfies a feature requirement with security attribute set to YES inherits this". But the component requirements/architecture may additionally also be subject to a :need:`wp__sw_component_security_analysis`.
        - YES
        - All security attributes set correctly.
        -
      * - REQ_08_01
        - Is the requirement *verifiable*?
        - If at the time of the inspection already tests are created for the requirement, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_test_covered` shows this. In case the requirement is not sufficiently traced to test cases already, a test expert is invited to the inspection to give their opinion whether the requirement is formulated in a way that supports test development and the available test infrastructure is sufficient to perform the test.
        - YES
        - @rahulthakre29: all requirements have test cases implemented
        -
      * - REQ_08_02
        - Is the requirement verifiable by design or code review in case it is not feasibly testable?
        - In very rare cases a requirement may not be verifiable by test cases, for example a specific non-functional requirement. In this case a requirement analysis verifies the requirement by design/code review. If such a requirement is in scope of this inspection, please check this here and link to the respective review record. A test expert is invited to the inspection to confirm their opinion that the requirement is not testable.
        - YES
        - Only one requirement is relevant for this inspection - :need:`comp_req__bitmanipulation__header_only` and it's very well verifiable by design/code review.
        -
      * - REQ_09_01
        - Do the requirements that define a safety mechanism specify the error reaction leading to a safe state?
        - Alternatively to the safe state there could also be "repair" mechanisms. Also do not forget to consider REQ_05_01 for these.
        - YES
        - There is only one requirement here that does define a safety mechanism - :need:`comp_req__bitmanipulation__bounds_safety`, findings on this were fixed in PR-2667 and PR-2696
        -


.. attention::
    The above checklist entries must be filled according to your component requirements in scope.
    It is mandatory to fill remarks also for checklist entries which are passed, to be able to understand the verdict.

Note: If a Review ID is not applicable for your requirement, then state ""n/a" in status and comment accordingly in remarks. For example "no stakeholder requirement (no rationale needed)"

The following requirements in "valid" state and with "inspected" tag set are in the scope of this inspection:

.. needtable::
   :filter: "bitmanipulation" in docname and "requirements" in docname and docname is not None and status == "valid"
   :style: table
   :types: comp_req
   :tags: bitmanipulation
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

And also the following AoUs in "valid" state and with "inspected" tag set (for these please answer the questions above as if the AoUs are requirements, except questions REQ_03_01 and REQ_03_02):

.. needtable::
   :filter: "bitmanipulation" in docname and "requirements" in docname and docname is not None and status == "valid"
   :style: table
   :types: aou_req
   :tags: bitmanipulation
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
