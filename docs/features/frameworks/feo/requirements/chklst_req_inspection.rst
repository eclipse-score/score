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


.. document:: FEO Feature Requirements Inspection Checklist
   :id: doc__req_inspection_frameworks_feo
   :status: draft
   :version: 2
   :security: NO
   :safety: ASIL_B
   :tags: frameworks_feo
   :realizes: wp__requirements_inspect[version==1]


FEO Feature Requirement Inspection Checklist
============================================


   **Purpose**
   The purpose of this requirement inspection checklist is to collect the topics to be checked during requirements inspection.

   **Checklist**

   .. list-table:: Feature Requirement Inspection Checklist FEO
      :header-rows: 1
      :widths: 10,30,50,6,6,8

      * - Review ID
        - Acceptance Criteria
        - Guidance
        - Passed
        - Remarks
        - Issue link
      * - REQ_01_01
        - Is the requirement sentence template used?
        - see :need:`gd_temp__req_formulation`, this includes the use of "shall".
        - No
        - Reformulate requirements according template, may split as not atomic
        - `Issue for Findings <https://github.com/eclipse-score/score/issues/1888>`_
      * - REQ_02_01
        - Is the requirement description *comprehensible* ?
        - If you think the requirement is hard to understand, comment here.
        - No
        - May add diagrams to support natural language, split in more atomic requirements
        - `Issue for Findings <https://github.com/eclipse-score/score/issues/1888>`_
      * - REQ_02_02
        - Is the requirement description *unambiguous* ?
        - Especially search for "weak words" like "about", "etc.", "relevant" and others (see the internet documentation on this). This check shall be supported by tooling.
        - Yes
        -
        -
      * - REQ_02_03
        - Is the requirement description *atomic* ?
        - A good way to think about this is to consider if the requirement may be tested by one (positive) test case or needs more of these. The sentence template should also avoid being non-atomic already. Note that there are cases where also non-atomic requirements are the better ones, for example if those are better understandable.
        - No
        - Split in more atomic requirements
        - `Issue for Findings <https://github.com/eclipse-score/score/issues/1888>`_
      * - REQ_02_04
        - Is the requirement description *feasible* ?
        - Expectation is that at the time of the inspection the requirement has already some implementation. This can be checked via traces, but also :need:`gd_req__req_attr_impl` shows this. In case the requirement is not mature enough at the time of inspection (i.e. not implemented at least as "proof-of-concept"), a development expert should be invited to the Pull-Request review to explicitly check this item.
        - No
        - Implementation exists, but currently not traceability is established
        - `Issue for Findings <https://github.com/eclipse-score/score/issues/1888>`_
      * - REQ_02_05
        - Is the requirement description *independent from implementation* ?
        - This checkpoint should improve requirements definition in the sense that the "what" is described and not the "how" - the latter should be described in architecture/design derived from the requirement. But there can also be a good reason for this, for example we would require using a file format like JSON and even specify the formatting standard already on stakeholder requirement level because we want to be compatible. A finding in this checkpoint does not mean there is a safety problem in the requirement.
        - No
        - May create Assumptions of Use in addition
        - `Issue for Findings <https://github.com/eclipse-score/score/issues/1888>`_
      * - REQ_03_01
        - Is the *linkage to the parent requirement* correct?
        - Linkage to correct levels and ASIL attributes is checked automatically, but it needs checking if the child requirement implements (at least) a part of the parent requirement.
        - No
        - stkh_req__execution_model__processes is QM, but feature depends on that, so it looks furhter AoU are needed
        - `Issue for Findings <https://github.com/eclipse-score/score/issues/1888>`_
      * - REQ_04_01
        - Is the requirement *internally and externally consistent*?
        - Does the requirement contradict other requirements within the same or higher levels? One may restrict the search to the feature for component requirements, for features to other features using same components.
        - Yes
        -
        -
      * - REQ_05_01
        - Do the software requirements consider *timing constraints of the parent requirement*?
        - This bullet point encourages to think about timing constraints even if those are not explicitly mentioned in the parent requirement. If the reviewer of a requirement already knows or suspects that the implementation will be time consuming, one should think of the expectation of a "user".
        - Yes
        -
        -
      * - REQ_06_01
        - Does the Requirement consider *external interfaces*?
        - The SW platform's external interfaces (to the user) are defined in the Feature Architecture, so the Feature and Component Requirements should determine the data consumed and set on these interfaces. Are output values completely defined?
        - No
        - Feature request has some assumptions not phrased as requirements or Aou yet
        - `Issue for Findings <https://github.com/eclipse-score/score/issues/1888>`_
      * - REQ_07_01
        - Is the *safety* attribute set correctly?
        - Derived requirements are checked automatically, see :need:`gd_req__req_linkage_safety`. But for the top level requirements this needs to be checked for correctness. Also AoU from external components need check for correct ASIL as those are the "origin" of safety requirements towards the SW platform.
        - Yes
        -
        -
      * - REQ_07_02
        - Is the *security* attribute set correctly?
        - For feature requirements this checklist item is supported by automated check: "Every requirement which is derived from a stakeholder requirement with security attribute set to YES inherits this". But the feature requirements/architecture may additionally also be subject to a :need:`wp__feature_security_analysis`
        - No
        - E.g. Trustable computation should include security considerations
        - `Issue for Findings <https://github.com/eclipse-score/score/issues/1888>`_
      * - REQ_08_01
        - Is the requirement *verifiable*?
        - If at the time of the inspection already tests are created for the requirement, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_test_covered` shows this. In case the requirement is not sufficiently traced to test cases already, a test expert is invited to the inspection to give their opinion whether the requirement is formulated in a way that supports test development and the available test infrastructure is sufficient to perform the test.
        - No
        - Follow the requirements template to make it verifiable.
        - `Issue for Findings <https://github.com/eclipse-score/score/issues/1888>`_
      * - REQ_08_02
        - Is the requirement verifiable by design or code review in case it is not feasibly testable?
        - In very rare cases a requirement may not be verifiable by test cases, for example a specific non-functional requirement. In this case a requirement analysis verifies the requirement by design/code review. If such a requirement is in scope of this inspection, please check this here and link to the respective review record. A test expert is invited to the inspection to confirm their opinion that the requirement is not testable.
        -
        -
        -
      * - REQ_09_01
        - Do the feature requirements defining a safety mechanism contain the error reaction leading to a safe state?
        - Alternatively to the safe state there could also be "repair" mechanisms. Also do not forget to consider REQ_05_01 for these.
        - Yes
        - May consider reformulating of Error Handling to Safety Mechanism, including Safe State definition
        -
      * - REQ_10_01
        - Is the requirement description *complete* ?
        - For every requirement in the inspection, follow to its parent (stakeholder) requirement(s) and then check if this/these are fulfilled completely by its/their linked children (feature requirements, including those which are not in scope of the inspection).
        -
        -
        -
