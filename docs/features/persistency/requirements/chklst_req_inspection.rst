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
   :id: doc__feature_persistency_requirements_chklst
   :status: draft
   :version: 2
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_inspect[version==1]
   :tags: persistency

Persistency Requirement Inspection Checklist
============================================

Purpose
-------

The purpose of this requirement inspection checklist is to collect the topics to be checked during requirements inspection.

Conduct
-------

As described in the concept :need:`doc_concept__wp_inspections` the following "inspection roles" are expected to be filled:

- content responsible (author): `<https://github.com/Ahmed-Elsaka-JC>`_
- reviewer: `<https://github.com/aschemmel-tech>`_, `<https://github.com/umaucher>`_
- moderator: `<https://github.com/PandaeDo>`_
- test expert: `<https://github.com/PiotrKorkus>`_

Checklist
---------

It is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additionally to add in the remarks why it is passed or not passed.
In case of "no" an issue link to the issue tracking system has to be added in the last column (if not solved in the same issue).
See also :need:`doc_concept__wp_inspections` for further information about reviews in general and inspection in particular.

.. note::

   **Pre-check for the re-inspection (version 2)**

   The columns "Passed", "Remarks" and "Issue link" contain a pre-check prepared by the safety manager as a basis
   for discussion. "Proposal: YES/NO" is not an inspection result; the inspection participants confirm or correct
   each entry, the moderator replaces the proposals by the final results.

   Version 1 of this checklist (`#960 <https://github.com/eclipse-score/score/issues/960>`_) was passed without findings.
   Since then the feature requirements were changed:

   - changed: :need:`feat_req__persistency__cfg` (version 2: global settings, maximum number of key-value pairs,
     maximum key size, security and redundancy settings removed; access mode, "Need Defaults", "Need Kvs" added)
   - changed: :need:`feat_req__persistency__storage_backends` (version 2: redundancy by multiple backends of the same
     type removed, backend selection per KVS instance via compile time parameter)
   - new: :need:`feat_req__persistency__cfg_priority`
   - removed: ``feat_req__persistency__direct_access``, ``feat_req__persistency__dev_mode``,
     ``feat_req__persistency__prod_mode`` (parent ``stkh_req__dependability__safety_features_11`` no longer exists)
   - ``valid_from`` added to all requirements, note added to :need:`feat_req__persistency__update_mechanism`

   The pre-check covers all feature requirements listed below, with focus on the changed and new ones.

.. list-table:: Persistency Feature Requirement Inspection Checklist
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
      - Proposal: NO
      - - :need:`feat_req__persistency__cfg_priority` - subject is "The Persistency Configuration file", not the Persistency.
        - Normative "shall" statements inside notes, which are not requirements: :need:`feat_req__persistency__cfg` (operation without configuration file), :need:`feat_req__persistency__access_control` (role/permission based policies), :need:`feat_req__persistency__snapshot_create` (prevention of implicit snapshots), :need:`feat_req__persistency__versioning`. Either move into the requirement text or reword as explanation.
      - new issue to be created after inspection
    * - REQ_02_01
      - Is the requirement description *comprehensible* ?
      - If you think the requirement is hard to understand, comment here.
      - Proposal: NO
      - - :need:`feat_req__persistency__cfg` - the configuration items "Access Mode", "Need Defaults" and "Need Kvs" are not explained; their meaning is only clear with knowledge of the implementation.
        - :need:`feat_req__persistency__cfg_priority` - "configuration by code" is not defined (compile time defaults of :need:`feat_req__persistency__cfg` or API parameters?).
      - new issue to be created after inspection
    * - REQ_02_02
      - Is the requirement description *unambiguous* ?
      - Especially search for "weak words" like "about", "etc.", "relevant" and others (see the internet documentation on this). This check shall be supported by tooling.
      - Proposal: NO
      - - :need:`feat_req__persistency__cfg_priority` - "higher priority": unclear whether per attribute (merge) or the file replaces the code configuration completely.
        - Weak words: "sensible default values" (:need:`feat_req__persistency__cfg`), "time consuming operations like" (:need:`feat_req__persistency__async_api`), "frequently accessed" (:need:`feat_req__persistency__cached_access`), "minimize" (:need:`feat_req__persistency__write_amplification`), "report" without receiver (:need:`feat_req__persistency__integrity_check`).
        - Unchanged since version 1; the weak words may be accepted with rationale, :need:`feat_req__persistency__cfg_priority` needs rework.
      - new issue to be created after inspection
    * - REQ_02_03
      - Is the requirement description *atomic* ?
      - A good way to think about this is to consider if the requirement may be tested by one (positive) test case or needs more of these. The requirement formulation template should also avoid being non-atomic already. Note that there are cases where also non-atomic requirements are the better ones, for example if those are better understandable.
      - Proposal: YES
      - - Non-atomic, but acceptable for understandability: :need:`feat_req__persistency__cfg` (file support, list of items, optionality, defaults), :need:`feat_req__persistency__storage_backends` (multiple backends + selection), :need:`feat_req__persistency__snapshot_create`, :need:`feat_req__persistency__tooling`.
        - Recommendation: split :need:`feat_req__persistency__cfg`, as its component requirements only cover parts of it (see REQ_10_01 of ``doc__kvs_req_inspection`` in the persistency module).
      -
    * - REQ_02_04
      - Is the requirement description *feasible* ?
      - If at the time of the inspection the requirement has already some implementation, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_impl` shows this. In case the requirement has no implementation at the time of inspection (i.e. not implemented at least as "proof-of-concept"), a development expert should be invited to the Pull-Request review to explicitly check this item.
      - Proposal: YES
      - - :need:`feat_req__persistency__cfg` and :need:`feat_req__persistency__storage_backends` were adapted to the implementation plan, i.e. feasible.
        - Not yet implemented (``valid_from`` v1.5.0 / v2.0.0): :need:`feat_req__persistency__versioning`, :need:`feat_req__persistency__update_mechanism`, :need:`feat_req__persistency__confidential_storage` - development expert to confirm feasibility.
      -
    * - REQ_02_05
      - Is the requirement description *independent from implementation* ?
      - This checkpoint should improve requirements definition in the sense that the "what" is described and not the "how" - the latter should be described in architecture/design derived from the requirement. But there can also be a good reason for this, for example we would require using a file format like JSON and even specify the formatting standard already on stakeholder requirement level because we want to be compatible. A finding in this checkpoint does not mean there is a safety problem in the requirement.
      - Proposal: NO
      - - :need:`feat_req__persistency__cfg` - "Need Defaults" and "Need Kvs" are names of implementation parameters; describe the behaviour instead (e.g. "default values required", "persisted data required at start").
        - :need:`feat_req__persistency__storage_backends` - "compile time configuration parameter" is a design decision; acceptable if intended as user-visible constraint.
      - new issue to be created after inspection
    * - REQ_03_01
      - Is the *linkage to the parent requirement* correct?
      - Linkage to correct levels and ASIL attributes is checked automatically, but it needs checking if the child requirement implements (at least) a part of the parent requirement.
      - Proposal: YES
      - - :need:`feat_req__persistency__cfg_priority` -> :need:`stkh_req__functional_req__file_based` is correct.
        - Removed requirements: parent of ``dev_mode`` / ``prod_mode`` does not exist anymore; :need:`stkh_req__dependability__availability` is still covered by :need:`feat_req__persistency__async_api` after removal of ``direct_access``.
        - ASIL_B children of QM parents (e.g. :need:`feat_req__persistency__cfg`, :need:`feat_req__persistency__update_mechanism`) are allowed by :need:`gd_req__req_linkage_safety`; the safety relevance comes from the safety analysis.
      -
    * - REQ_04_01
      - Is the requirement *internally and externally consistent*?
      - Does the requirement contradict other requirements within the same or higher levels? One may restrict the search to the feature for component requirements, for features to other features using same components. Is the description of the requirement consistent with all its attributes (if not already part of another check, e.g. does the title fit?).
      - Proposal: NO
      - - :need:`feat_req__persistency__cfg` and :need:`feat_req__persistency__cfg_priority` have the identical title "Configuration"; title of the new requirement does not fit (e.g. "Configuration priority").
        - Removal of the limits from :need:`feat_req__persistency__cfg` (maximum key size, maximum number of key-value pairs) is inconsistent with the safety analysis in the persistency module: ``feat_saf_fmea__persistency__constraint_max`` ("key, value or persisted data exceeds the configured maximum") and ``feat_saf_dfa__persistency__memory_depletion`` are mitigated by :need:`feat_req__persistency__cfg`.
        - :need:`feat_req__persistency__dynamic_memory_alloc` requires allocation during initialization only; without configured limits for keys / number of key-value pairs it is unclear how the required memory is determined.
        - :need:`feat_req__persistency__tooling` (second bullet) duplicates :need:`feat_req__persistency__default_value_file`.
      - new issue to be created after inspection
    * - REQ_05_01
      - Do the software requirements consider *timing constraints*?
      - This checkpoint encourages to think about timing constraints even if those are not explicitly mentioned in the parent requirement. If the reviewer of a requirement already knows or suspects that the code execution will be consuming a lot of time, one should think of the expectation of a "user".
      - Proposal: YES
      - - Unchanged since version 1: :need:`feat_req__persistency__fast_access` (time complexity), :need:`feat_req__persistency__async_api` for time consuming operations.
        - Removal of ``direct_access`` (loading without full load into RAM) may increase the start-up time for large data sets - to be confirmed as accepted.
      -
    * - REQ_06_01
      - Does the requirement consider *external interfaces*?
      - The SW platform's external interfaces (to the user) are defined in the Feature Architecture, so the Feature and Component Requirements should determine the input data use and setting of output data for these interfaces. Are all output values defined?
      - Proposal: YES
      - - Configuration file content defined by :need:`feat_req__persistency__cfg`; file format left to the component level (JSON).
        - Output of :need:`feat_req__persistency__integrity_check` ("report") is not further defined; error handling towards the application is covered by the AoU ``aou_req__persistency__error_handling`` (persistency module).
      -
    * - REQ_07_01
      - Is the *safety* attribute set correctly?
      - Derived requirements are checked automatically, see :need:`gd_req__req_linkage_safety`. But for the top level requirements (and also all AoU) this needs to be checked manually for correctness.
      - Proposal: YES
      - - :need:`feat_req__persistency__cfg_priority` ASIL_B is consistent with :need:`feat_req__persistency__cfg`.
        - To be discussed: :need:`feat_req__persistency__tooling` is ASIL_B, although it addresses development, testing and debugging tools (rather a tool qualification topic).
      -
    * - REQ_07_02
      - Is the attribute *security* set correctly?
      - For component requirements this checklist item is supported by automated check: "Every requirement which satisfies a feature requirement with security attribute set to YES inherits this". But the component requirements/architecture may additionally also be subject to a :need:`wp__sw_component_security_analysis`.
      - Proposal: YES
      - - :need:`feat_req__persistency__cfg_priority` security YES is plausible (a manipulated configuration file overrides the code configuration).
        - :need:`feat_req__persistency__cfg` keeps security YES although "Security settings" were removed; "Access Mode" remains - plausible.
        - To be confirmed with the security analysis: :need:`feat_req__persistency__integrity_check` is security NO although it detects manipulated data.
      -
    * - REQ_08_01
      - Is the requirement *verifiable*?
      - If at the time of the inspection already tests are created for the requirement, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_test_covered` shows this. In case the requirement is not sufficiently traced to test cases already, a test expert is invited to the inspection to give their opinion whether the requirement is formulated in a way that supports test development and the available test infrastructure is sufficient to perform the test.
      - Proposal: NO
      - - Feature integration tests in reference_integration reference only 9 of 33 feature requirements (default values, datatypes, store, multiple KVS, reset to default, integrity check).
        - Not traced to tests, among others: :need:`feat_req__persistency__cfg`, :need:`feat_req__persistency__cfg_priority`, :need:`feat_req__persistency__storage_backends`, snapshots, :need:`feat_req__persistency__reset_resistant`, :need:`feat_req__persistency__recovery_from_reset`, :need:`feat_req__persistency__multiple_app`. Test expert to assess.
        - :need:`feat_req__persistency__cfg_priority` is only testable after clarification (see REQ_02_02).
      - new issue to be created after inspection
    * - REQ_08_02
      - Is the requirement verifiable by design or code review in case it is not feasibly testable?
      - In very rare cases a requirement may not be verifiable by test cases, for example a specific non-functional requirement. In this case a requirement analysis verifies the requirement by design/code review. If such a requirement is in scope of this inspection, please check this here and link to the respective review record. A test expert is invited to the inspection to confirm their opinion that the requirement is not testable.
      - Proposal: NO
      - - Not or hardly testable, no review record linked: :need:`feat_req__persistency__os_agnostic`, :need:`feat_req__persistency__write_amplification`, :need:`feat_req__persistency__dynamic_memory_alloc`, :need:`feat_req__persistency__fast_access`, :need:`feat_req__persistency__variant_management`.
      - new issue to be created after inspection
    * - REQ_09_01
      - Do the requirements that define a safety mechanism specify the error reaction leading to a safe state?
      - Alternatively to the safe state there could also be "repair" mechanisms. Also do not forget to consider REQ_05_01 for these.
      - Proposal: NO
      - - :need:`feat_req__persistency__reset_resistant` / :need:`feat_req__persistency__recovery_from_reset` define a repair mechanism (consistent state).
        - :need:`feat_req__persistency__integrity_check` only requires "detect and report"; the reaction of the Persistency on corrupted data (e.g. fall back to last consistent snapshot or default values, no further write) is not specified.
        - Not filled in version 1.
      - new issue to be created after inspection
    * - REQ_10_01
      - Is the requirement description *complete* ?
      - For every requirement in the inspection, follow to its parent (stakeholder) requirement(s) and then check if this/these are fulfilled completely by its/their linked children (feature requirements, including those which are not in scope of the inspection).
      - Proposal: YES
      - - :need:`stkh_req__functional_req__support_of_store` ("safe key/value store") remains covered after removal of the redundancy part of :need:`feat_req__persistency__storage_backends` (reset resistance, recovery, integrity check).
        - :need:`stkh_req__dependability__security_features` is covered by :need:`feat_req__persistency__access_control` only - to be confirmed with the security analysis.
        - Not covered by this checkpoint: completeness of the component requirements against the feature requirements, see REQ_10_01 of ``doc__kvs_req_inspection`` in the persistency module.
      -

Note: If a Review ID is not applicable for your requirement, then state "n/a" in status and comment accordingly in remarks.

The following requirements in "valid_inspected" state are in the scope of this inspection:

.. needtable::
   :filter: docname is not None and "features/persistency/requirements" in docname
   :style: table
   :types: feat_req
   :tags: persistency
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

And also the following AoUs in "valid_inspected" state (for these please answer the questions above as if the AoUs are requirements, except question REQ_03_01):

.. needtable::
   :filter: docname is not None and "features/persistency" in docname
   :style: table
   :types: aou_req
   :tags: persistency
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

.. note::

   The feature level AoUs of the Persistency (``aou_req__persistency__*``) are maintained in the persistency module
   (``docs/features/persistency/safety_analysis/aou_requirements.rst``) and are therefore not listed in the table above.
   They are inspected together with the component requirements in ``doc__kvs_req_inspection``.
