..
   # *******************************************************************************
   # Copyright (c) 2025-2026 Contributors to the Eclipse Foundation
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


.. document:: Baselibs Requirements Inspection Checklist
   :id: doc__baselibs_req_inspection
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_inspect[version==1]


Requirement Inspection Checklist
================================

Purpose
-------

The purpose of this requirement inspection checklist is to collect the topics to be checked during requirements inspection.

Conduct
-------

As described in the concept :need:`doc_concept__wp_inspections` the following "inspection roles" are expected to be filled:

- content responsible (author): `<https://github.com/4og>`_
- reviewer: `<https://github.com/mihajlo-k>`_
- moderator: `<https://github.com/aschemmel-tech>`_
- test expert: `<https://github.com/rahulthakre29>`_

Checklist
---------

It is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additionally to add in the remarks why it is passed or not passed.
In case of "no" an issue link to the issue tracking system has to be added in the last column (if not solved in the same issue).
See also :need:`doc_concept__wp_inspections` for further information about reviews in general and inspection in particular.

.. list-table:: Feature Requirement Inspection Checklist
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
      - All requirements follow the template.
      -
    * - REQ_02_01
      - Is the requirement description *comprehensible* ?
      - If you think the requirement is hard to understand, comment here.
      - YES
      - All requirements are fairly easy to understand.
      -
    * - REQ_02_02
      - Is the requirement description *unambiguous* ?
      - Especially search for "weak words" like "about", "etc.", "relevant" and others (see the internet documentation on this). This check shall be supported by tooling.
      - NO
      - - :need:`feat_req__baselibs__core_utilities`: It's open to interpretation what "core software utilities and common infrastructure components" means. Listing them explicitly or linking this requirement to an existing list would be better. Also "multiple" seems vague, and also implies that the number of modules using base libs is relevant here. maybe just drop it.
        - :need:`feat_req__baselibs__safety`: The phrase "selected functionalities" makes is vague. It could be interpreted as such that only a "selected" subset of functionalities that need to be ASIL-B are actually ASIL-B, or maybe "selected functionalities" are on the user side? I assume that this requirement is to be understood as: "Each base library component shall be qualified at the same safety integrity level as required by its consuming platform components, up to ASIL-B.". If that is true - then it needs to be rephrased in that way.
        - :need:`feat_req__baselibs__consistent_apis`: It's unclear what is meant by ""consistent""? Consistent naming, error handling...? Consistency over time? My interpretation is that is should use uniform API design patterns across all components, but it's not entirely clear.
        - :need:`feat_req__baselibs__containers_library`: "container types not present in the C++ standard library" depends on which C++ standard is used.
      - https://github.com/eclipse-score/score/issues/2885
    * - REQ_02_03
      - Is the requirement description *atomic* ?
      - A good way to think about this is to consider if the requirement may be tested by one (positive) test case or needs more of these. The requirement formulation template should also avoid being non-atomic already. Note that there are cases where also non-atomic requirements are the better ones, for example if those are better understandable.
      - YES
      - Note: several requirements list the capabilities of the components, which makes those requirements not strictly atomic. However, this might be preferred on the feature level.
      -
    * - REQ_02_04
      - Is the requirement description *feasible* ?
      - If at the time of the inspection the requirement has already some implementation, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_impl` shows this. In case the requirement has no implementation at the time of inspection (i.e. not implemented at least as "proof-of-concept"), a development expert should be invited to the Pull-Request review to explicitly check this item.
      - YES
      - All requirements already implemented at the time of this inspection.
      -
    * - REQ_02_05
      - Is the requirement description *independent from implementation* ?
      - This checkpoint should improve requirements definition in the sense that the "what" is described and not the "how" - the latter should be described in architecture/design derived from the requirement. But there can also be a good reason for this, for example we would require using a file format like JSON and even specify the formatting standard already on stakeholder requirement level because we want to be compatible. A finding in this checkpoint does not mean there is a safety problem in the requirement.
      - YES
      - Note: there is a mention of specific "technologies" within some of the requirements that might be vaguely interpreted as "how"s, but are justified within the context.
      -
    * - REQ_03_01
      - Is the *linkage to the parent requirement* correct?
      - Linkage to correct levels and ASIL attributes is checked automatically, but it needs checking if the child requirement implements (at least) a part of the parent requirement.
      - NO
      - Following requirements are missing links to :need:`stkh_req__dependability__automotive_safety` which should be added to justify their safety classification:

        - :need:`feat_req__baselibs__json_library`
        - :need:`feat_req__baselibs__result_library`
        - :need:`feat_req__baselibs__containers_library`
        - :need:`feat_req__baselibs__bitmanipulation`
        - :need:`feat_req__baselibs__memory_library`
        - :need:`feat_req__baselibs__concurrency_library`
      - https://github.com/eclipse-score/score/issues/2885
    * - REQ_04_01
      - Is the requirement *internally and externally consistent*?
      - Does the requirement contradict other requirements within the same or higher levels? One may restrict the search to the feature for component requirements, for features to other features using same components. Is the description of the requirement consistent with all its attributes (if not already part of another check, e.g. does the title fit?).
      - NO
      - No logical inconsistencies, just minor naming issues:

        - :need:`feat_req__baselibs__json_library`: To be consistent with the titles of other requirements the title should be changed: JSON-Library -> JSON Library
        - :need:`feat_req__baselibs__flatbuffers_library`: FlatBuffers-Library -> FlatBuffers Library
        - :need:`feat_req__baselibs__result_library`: Title is "Exception-Free Development Support" but the ID is result_library. The title describes the constraint, and not the library name. This is inconsistent to the naming of other components.
        - :need:`feat_req__baselibs__filesystem_library`: Filesystem-Library -> Filesystem Library
        - :need:`feat_req__baselibs__memory_library`: Description uses "baselibs" while all other requirements use "base libraries". Internally inconsistent with naming convention used throughout the document.
      - https://github.com/eclipse-score/score/issues/2885
    * - REQ_05_01
      - Do the software requirements consider *timing constraints*?
      - This checkpoint encourages to think about timing constraints even if those are not explicitly mentioned in the parent requirement. If the reviewer of a requirement already knows or suspects that the code execution will be consuming a lot of time, one should think of the expectation of a "user".
      - YES
      - Note: the following requirements describe libraries potentially involving operations with non-deterministic or variable execution times (However, this concern should arguably be addressed on component level):

        - :need:`feat_req__baselibs__flatbuffers_library`
        - :need:`feat_req__baselibs__json_library`
        - :need:`feat_req__baselibs__containers_library`
        - :need:`feat_req__baselibs__memory_library`
        - :need:`feat_req__baselibs__concurrency_library`
      -
    * - REQ_06_01
      - Does the requirement consider *external interfaces*?
      - The SW platform's external interfaces (to the user) are defined in the Feature Architecture, so the Feature and Component Requirements should determine the input data use and setting of output data for these interfaces. Are all output values defined?
      - YES
      - The output interfaces of base libraries are coupled with individual components, and are arguably to be defined within component requirements.
      -
    * - REQ_07_01
      - Is the *safety* attribute set correctly?
      - Derived requirements are checked automatically, see :need:`gd_req__req_linkage_safety`. But for the top level requirements (and also all AoU) this needs to be checked manually for correctness.
      - YES
      - Note: the justification via traceability is missing - see comment for REQ_03_01
      -
    * - REQ_07_02
      - Is the *security* attribute set correctly?
      - For feature requirements this checklist item is supported by automated check: "Every requirement which satisfies a stakeholder requirement with security attribute set to YES inherits this". But the feature requirements/architecture may additionally also be subject to a :need:`wp__feature_security_analysis`
      - NO
      - all the feature requirements here inherit from :need:`stkh_req__functional_req__base_libraries`, which has a security set to YES. This means all the requirements here should also set this attribute to YES.
      - https://github.com/eclipse-score/score/issues/2885
    * - REQ_08_01
      - Is the requirement *verifiable*?
      - If at the time of the inspection already tests are created for the requirement, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_test_covered` shows this. In case the requirement is not sufficiently traced to test cases already, a test expert is invited to the inspection to give their opinion whether the requirement is formulated in a way that supports test development and the available test infrastructure is sufficient to perform the test.
      - YES
      - The following feature requirements are high-level and not directly testable

        - :need:`feat_req__baselibs__core_utilities`
        - :need:`feat_req__baselibs__safety`
        - :need:`feat_req__baselibs__multi_language_apis`
        - :need:`feat_req__baselibs__consistent_apis`
        - :need:`feat_req__baselibs__maintainable_design`
        - :need:`feat_req__baselibs__security`

        But these high-level requirements are decomposed into detailed component requirements that are testable.

        Following feature requirements are directly testable:

        - :need:`feat_req__baselibs__json_library`
        - :need:`feat_req__baselibs__flatbuffers_library`
        - :need:`feat_req__baselibs__result_library`
        - :need:`feat_req__baselibs__containers_library`
        - :need:`feat_req__baselibs__bitmanipulation`
        - :need:`feat_req__baselibs__filesystem_library`
        - :need:`feat_req__baselibs__memory_library`
        - :need:`feat_req__baselibs__concurrency_library`

        For these directly testable features, requirement wording is clear enough to derive test cases, and trace links from feature requirements to lower-level requirements and test cases are available
      -
    * - REQ_08_02
      - Is the requirement verifiable by design or code review in case it is not feasibly testable?
      - In very rare cases a requirement may not be verifiable by test cases, for example a specific non-functional requirement. In this case a requirement analysis verifies the requirement by design/code review. If such a requirement is in scope of this inspection, please check this here and link to the respective review record. A test expert is invited to the inspection to confirm their opinion that the requirement is not testable.
      - n/a
      - all testable
      -
    * - REQ_09_01
      - Do the feature requirements defining a safety mechanism contain the error reaction leading to a safe state?
      - Alternatively to the safe state there could also be "repair" mechanisms. Also do not forget to consider REQ_05_01 for these.
      - YES
      - Note: None of the requirements here is defining a safety mechanism, yet several components contain operation that could fail and need a safety mechanism. However, defining safety mechanisms is arguably better suited for individual libraries' component requirements.
      -


Note: If a Review ID is not applicable for your requirement, then state ""n/a" in status and comment accordingly in remarks. For example "no stakeholder requirement (no rationale needed)"

The following requirements in "valid" state and with "inspected" tag set are in the scope of this inspection:

.. needtable::
   :filter: docname is not None and "baselibs" in docname and "requirements" in docname and status == "valid"
   :style: table
   :types: feat_req
   :tags: baselibs
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

And also the following AoUs in "valid" state and with "inspected" tag set (for these please answer the questions above as if the AoUs are requirements, except questions REQ_03_01 and REQ_03_02):

.. needtable::
   :filter: docname is not None and "baselibs" in docname and "requirements" in docname and "features" in docname and status == "valid"
   :style: table
   :types: aou_req
   :tags: baselibs
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
