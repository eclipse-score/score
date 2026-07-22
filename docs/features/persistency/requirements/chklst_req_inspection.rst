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


.. document:: Persistency Requirements Inspection Checklist
   :id: doc__persistency_req_inspection
   :status: draft
   :version: 2
   :safety: ASIL_B
   :security: NO
   :tags: persistency
   :realizes: wp__requirements_inspect[version==1]


Requirement Inspection Checklist
================================

Purpose
-------

The purpose of this requirement inspection checklist is to collect the topics to be checked during requirements inspection.

Conduct
-------

As described in the concept :need:`doc_concept__wp_inspections` the following "inspection roles" are expected to be filled:

- content responsible (author): `<https://github.com/sbachmann-qorix>`_
- reviewer: `<https://github.com/vinodreddy-g>`_
- moderator: `<https://github.com/PandaeDo>`_
- test expert: `<https://github.com/PiotrKorkus>`_

Checklist
---------

It is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additionally to add in the remarks why it is passed or not passed.
In case of "no" an issue link to the issue tracking system has to be added in the last column (if not solved in the same issue).
See also :need:`doc_concept__wp_inspections` for further information about reviews in general and inspection in particular.

.. list-table:: Persistency Requirements Inspection Checklist
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
    -
    -
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
    -
    -
    - 
  * - REQ_02_04
    - Is the requirement description *feasible* ?
    - Expectation is that at the time of the inspection the requirement has already some implementation. This can be checked via traces, but also :need:`gd_req__req_attr_impl` shows this. In case the requirement is not mature enough at the time of inspection (i.e. not implemented at least as "proof-of-concept"), a development expert should be invited to the Pull-Request review to explicitly check this item.
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
    - Is the *linkage to the parent requirement* correct?
    - Linkage to correct levels and ASIL attributes is checked automatically, but it needs checking if the child requirement implements (at least) a part of the parent requirement.
    -
    -
    -
  * - REQ_04_01
    - Is the requirement *internally and externally consistent*?
    - Does the requirement contradict other requirements within the same or higher levels? One may restrict the search to the feature for component requirements, for features to other features using same components. Is the description of the requirement consistent with all its attributes (if not already part of another check, e.g. does the title fit?).
    -
    -
    -
  * - REQ_05_01
    - Do the software requirements consider *timing constraints*?
    - This checkpoint encourages to think about timing constraints even if those are not explicitly mentioned in the parent requirement. If the reviewer of a requirement already knows or suspects that the code execution will be consuming a lot of time, one should think of the expectation of a "user".
    -
    -
    -
  * - REQ_06_01
    - Does the Requirement consider *external interfaces*?
    - The SW platform's external interfaces (to the user) are defined in the Feature Architecture, so the Feature and Component Requirements should determine the data consumed and set on these interfaces. Are output values completely defined?
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_07_01
    - Is the *safety* attribute set correctly?
    - Derived requirements are checked automatically, see :need:`gd_req__req_linkage_safety`. But for the top level requirements (and also all AoU) this needs to be checked manually for correctness.
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_07_02
    - Is the attribute *security* set correctly?
    - For feature requirements this checklist item is supported by automated check: "Every requirement which is derived from a stakeholder requirement with security attribute set to YES inherits this". But the feature requirements/architecture may additionally also be subject to a :need:`wp__feature_security_analysis`
    - Yes
    - No remarks
    - https://github.com/eclipse-score/score/issues/960
  * - REQ_08_01
    - Is the requirement *verifiable*?
    - If at the time of the inspection already tests are created for the requirement, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_test_covered` shows this. In case the requirement is not sufficiently traced to test cases already, a test expert is invited to the inspection to give their opinion whether the requirement is formulated in a way that supports test development and the available test infrastructure is sufficient to perform the test.
    -
    -
    -
  * - REQ_08_02
    - Is the requirement verifiable by design or code review in case it is not feasibly testable?
    - In very rare cases a requirement may not be verifiable by test cases, for example a specific non-functional requirement. In this case a requirement analysis verifies the requirement by design/code review. If such a requirement is in scope of this inspection, please check this here and link to the respective review record. A test expert is invited to the inspection to confirm their opinion that the requirement is not testable.
    -
    -
    -
  * - REQ_09_01
    - Do the feature requirements defining a safety mechanism contain the error reaction leading to a safe state?
    - Alternatively to the safe state there could also be "repair" mechanisms. Also do not forget to consider REQ_05_01 for these.
    -
    -
    -
  * - REQ_10_01
    - Is the requirement description *complete* ?
    - For every requirement in the inspection, follow to its parent (feature) requirement(s) and then check if this/these are fulfilled completely by its/their linked children (component requirements, including those which are not in scope of the inspection).
    -
    -
    -


The following requirements in "valid" state and with "inspected" tag set are in the scope of this inspection:

.. needtable::
   :filter: "feature_name" in docname and "requirements" in docname and docname is not None and status == "valid"
   :style: table
   :types: feat_req
   :tags: persistency
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

And also the following AoUs in "valid" state and with "inspected" tag set (for these please answer the questions above as if the AoUs are requirements, except questions REQ_03_01 and REQ_03_02):

.. needtable::
   :filter: "feature_name" in docname and "requirements" in docname and docname is not None and status == "valid"
   :style: table
   :types: aou_req
   :tags: persistency
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
