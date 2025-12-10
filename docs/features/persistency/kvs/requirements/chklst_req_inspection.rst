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

Requirement Inspection Checklist Persistency KVS
================================================

.. document:: Requirements Inspection Checklist Persistency KVS
  :id: doc__req_inspection_persistency
  :status: valid
  :safety: ASIL_B
  :security: NO
  :tags: persistency
  :realizes: wp__requirements_inspect

**Purpose**
The purpose of this requirement inspection checklist is to collect the topics to be checked during requirements inspection.

**Conduct**

 As described in the concept :need:`doc_concept__wp_inspections` the following "inspection roles" are expected to be filled:

    author: these are the persons who did the last commits on the requirements in scope (can be derived from version mgt tool)

    reviewer: these are all persons committing into this inspection document or giving a pull request verdict on it (can be derived from version mgt tool)

    moderator: only needed for conflict resolution between author and reviewers, is the safety manager, security manager or quality manager called in as a reviewer (can be derived from version mgt tool)

    test expert: <one of the reviewers explicitly named here, to cover REQ_08_01 as described>



**Checklist**

.. list-table:: Requirement Inspection Checklist Persistency KVS
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
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_02_01
    - Is the requirement description *comprehensible* ?
    - If you think the requirement is hard to understand, comment here.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_02_02
    - Is the requirement description *unambiguous* ?
    - Especially search for "weak words" like "about", "etc.", "relevant" and others (see the internet documentation on this). This check shall be supported by tooling.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_02_03
    - Is the requirement description *atomic* ?
    - A good way to think about this is to consider if the requirement may be tested by one (positive) test case or needs more of these. The sentence template should also avoid being non-atomic already. Note that there are cases where also non-atomic requirements are the better ones, for example if those are better understandable.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_02_04
    - Is the requirement description *feasible* ?
    - If at the time of the inspection the requirement has already some implementation, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_impl` shows this. In case the requirement has no implementation at the time of inspection (i.e. not implemented at least as "proof-of-concept"), a development expert should be invited to the Pull-Request review to explicitly check this item.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_02_05
    - Is the requirement description *independent from implementation* ?
    - This checkpoint should improve requirements definition in the sense that the "what" is described and not the "how" - the latter should be described in architecture/design derived from the requirement. But there can also be a good reason for this, for example we would require using a file format like JSON and even specify the formatting standard already on stakeholder requirement level because we want to be compatible. A finding in this checkpoint does not mean there is a safety problem in the requirement.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_03_01
    - For stakeholder requirements: Is the *rationale* correct?
    - Rationales explain why the top level requirements were invented. Do those cover the requirement?
    - N/A
    - No stakeholder requirements for Persistency KVS needed.
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_03_02
    - For other requirements: Is the *linkage to the parent requirement* correct?
    - Linkage to correct levels and ASIL attributes is checked automatically, but it needs checking if the child requirement implements (at least) a part of the parent requirement.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_04_01
    - Is the requirement *internally and externally consistent*?
    - Does the requirement contradict other requirements within the same or higher levels? One may restrict the search to the feature for component requirements, for features to other features using same components.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_05_01
    - Do the software requirements consider *timing constraints*?
    - This checkpoint encourages to think about timing constraints even if those are not explicitly mentioned in the parent requirement. If the reviewer of a requirement already knows or suspects that the code execution will be consuming a lot of time, one should think of the expectation of a "user".
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_06_01
    - Does the Requirement consider *external interfaces*?
    - The SW platform's external interfaces (to the user) are defined in the Feature Architecture, so the Feature and Component Requirements should determine the data consumed and set on these interfaces. Are output values completely defined?
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_07_01
    - Is the *ASIL Attribute* set correctly?
    - Derived requirements are checked automatically, see :need:`gd_req__req_linkage_safety`. But for the top level requirements this needs to be checked for correctness. Also AoU from external components need check for correct ASIL as those are the "origin" of safety requirements towards the SW platform.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_07_02
    - Is the attribute *security* set correctly?
    - Stakeholder requirements security attribute should be set based on Threat Analysis and Risk Assessment (TARA) (process is TBD). Checklist item is supported by automated check: "Every requirement which satisfies a requirement with security attribute set to YES inherits this". Expectation is that the feature/component requirements/architecture may also be subject to a Software Security Criticality Analysis (process is TBD).
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_08_01
    - Is the requirement *verifiable*?
    - Expectation is that at the time of the inspection already tests are created for the requirement. This can be checked via traces, but also :need:`gd_req__req_attr_test_covered` shows this. In case the requirement is not mature enough at the time of inspection (i.e. missing test cases), a test expert should be invited to the Pull-Request review to explicitly check this item.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_09_01
    - For stakeholder requirements: Do those cover assumed safety mechanisms needed by the hardware and system?
    - Note that stakeholder requirements covering safety mechanisms come from rationales, whereas feature/component requirements are covering safety mechanisms coming from :need:`gd_chklst__safety_analysis`
    - YES
    - N/A
    - No stakeholder requirements for Persistency KVS needed.
  * - REQ_09_02
    - For feature/component requirements: Do the requirements defining a safety mechanism contain the error reaction leading to a safe state?
    - Alternatively to the safe state there could also be "repair" mechanisms. Also do not forget to consider REQ_05_01 for these.
    - YES
    - Repair mechanisms are described. Persistency is developed as full deterministic. Potential failures are considered in safety analysis.
    - https://github.com/eclipse-score/score/issues/960
