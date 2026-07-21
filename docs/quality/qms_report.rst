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


Quality Report
==============

.. document:: Quality Report
   :id: doc__score_qms_report
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__qms_report[version==1]
   :tags:


This document implements :need:`wp__qms_report` and based on the :need:`wp__qms_plan`. It summarizes
the results of the quality related activities. It shall be referred in the :need:`wp__platform_sw_release_note`
of a platform release.

The Quality Report contains:

1. Quality Overview
===================

The goal of this first version of the Quality Report is to provide an overview of the quality related activities
and their results. The Quality Report is a living document and will be updated at least with every platform release.
More important for the moment is to identify gaps and to close them.

1.1. Quality Objectives and Goals
=================================

Quality Objectives
------------------

.. list-table:: Standards to comply with
    :header-rows: 1
    :widths: 15,45,15,40

    * - #
      - **Standard Name**
      - **Version**
      - **Status**
    * - 1
      - Automotive SPICE PAM
      - 4.0
      - Requirements fully linked to process descriptions
    * - 2
      - ISO 262626:2018
      - 2018
      - Requirements and work products fully linked to process descriptions
    * - 3
      - ISO/SAE 21434:2021
      - 2021
      - Requirements linked to 75%, work products linked to 100% to process descriptions
    * - 4
      - ISO PAS 8926:2024 (will be integrated into ISO 26262 3rd edition as updated part 8 clause 12)
      - 2024
      - Requirements and work products fully linked to process descriptions


Quality Performance Objectives
------------------------------

.. list-table:: Quality assurance activities and frequency of performing them
    :header-rows: 1

    * - #
      - **Activities**
      - **Cadence**
      - **Status**
    * - 1
      - Platform process audit
      - Once for every platform release or on demand
      - Open
    * - 2
      - Feature process conformance checks
      - Once for every feature release
      - Open
    * - 3
      - Work product review
      - Once for every feature release
      - Open
    * - 4
      - Platform release verification and approval
      - Once for every release
      - Open
    * - 5
      - Process consulting / Quality trainings
      - Continuously
      - On the job, not explicitly documented yet
    * - 6
      - Process monitoring / Process improvement
      - Continuously
      - Open


Quantitative Quality Goals
--------------------------

.. list-table:: Quantitative Quality Goals
    :header-rows: 1

    * - #
      - **Quality Criteria**
      - **Source**
      - **Target value**
      - **Allowed variation**
      - **Metric**
    * - 1
      - One Platform process audit per release
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of the Platform process audit has be done for every release
      - Delta audit allowed to achieve 100%
      - Ensured by the process quality management, :need:`wf__exe_pltprocess_audit` - Platform process audit is available
    * - 2
      - One process conformance check for every feature release
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - One process conformance check has been done for every stable feature release
      - Feature is released as experimental
      - Ensured by the process quality and tool management, :need:`wp__qms_report` - Process conformance is available
    * - 3
      - Only quality-assured project/platform work products are delivered to the community
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of project/platform work products are quality-assured
      - Feature is released as experimental
      - Ensured by the process quality and tool management, :need:`wp__verification_platform_ver_report` - Work products contain the verification of the quality assurance
    * - 4
      - Only quality-assured project/platform releases are delivered to the community
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of project/platform releases delivered to the community are quality-assured
      - Feature is released as experimental
      - Ensured by the process release management, :need:`wp__platform_sw_release_note` contain the verification and approval of the quality-assurance
    * - 5
      - Only quality-trained personnel are part of the :need:`rl__committer`
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of personnel are trained as per committer role description in :need:`rl__committer`
      - None
      - Ensured by the process platform management, :need:`wp__training_path` contain the training material and evidences for conducted trainings
    * - 6
      - No overdue quality assurance closure activities
      - :need:`stkh_req__dependability__automotive_safety`, :doc:`../requirements/stakeholder/index`
      - 100% of the quality improvement, non-conformance issues are closed
      - None
      - Ensured by the process quality management, :need:`wp__issue_track_system` contain improvements and non-conformance


Work Product Quality Goals
--------------------------

For all generated work products, the following quality goals are defined:

.. list-table:: Work Product Quality Goals
    :header-rows: 1

    * - #
      - **Quality Criteria**
      - **Source**
      - **Target value**
      - **Allowed variation**
      - **Metric**
    * - 1
      - All work products have to be available and valid. Templates, checklists, and guidelines shall be used. Plans have to be up to date. The training material shall be available in the training path. The issues in the issue tracking system following the planning strategy.
      - All Repositories that contain work products and that are in development or maintenance phase
      - 100%
      - There is no allowed variation for the work products
      - The metric for the work products is ensured by the process that contains the work product. Only valid work products can be merged. Reviews are required and therefore checklists are prepared. If applicable, script based checks are implemented.

Evaluation Quality Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Processes are partially applied. So it's proved that they are applicable with some open gaps regarding implementation and
verification which are not final proved for the moment. The quality objectives and goals has to be archieved for the complete
project.



1.2. Lists of all work products
===============================


Quality Management Generic work products
----------------------------------------

.. list-table:: Quality related work products
    :header-rows: 1

    * - Workproduct Id
      - Link to WP
      - WP Status

    * - :need:`wp__chm_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='doc__platform_change_management_plan')`

    * - :need:`wp__config_mgt_plan`
      - :need:`doc__config_mgt_plan`
      - :ndf:`copy('status', need_id='doc__config_mgt_plan')`

    * - :need:`wp__document_mgt_plan`
      - :ref:`project_documents_list`
      - :ndf:`copy('status', need_id='doc__documentation_mgt_plan')`

    * - :need:`wp__feature_arch`
      - :need:`doc__baselibs_architecture`
      - :ndf:`copy('status', need_id='doc__baselibs_architecture')`

    * - :need:`wp__feat_request`
      - :need:`doc__baselibs`
      - :ndf:`copy('status', need_id='doc__baselibs')`

    * - :need:`wp__requirements_feat`
      - :need:`doc__baselibs_requirements`
      - :ndf:`copy('status', need_id='doc__baselibs_requirements')`

    * - :need:`wp__fdr_reports`
      - :need:`doc__baselibs_req_inspection`
      - :ndf:`copy('status', need_id='doc__baselibs_req_inspection')`

    * - :need:`wp__feature_arch`
      - :need:`doc__baselibs_architecture`
      - :ndf:`copy('status', need_id='doc__baselibs_architecture')`

    * - :need:`wp__feat_request`
      - :need:`doc__com`
      - :ndf:`copy('status', need_id='doc__com')`

    * - :need:`wp__requirements_feat`
      - :need:`doc__communication_requirements`
      - :ndf:`copy('status', need_id='doc__communication_requirements')`

    * - :need:`wp__fdr_reports`
      - -
      - -

    * - :need:`wp__feature_arch`
      - :need:`doc__frameworks_feo_feat_arch`
      - :ndf:`copy('status', need_id='doc__frameworks_feo_feat_arch')`

    * - :need:`wp__feat_request`
      - :need:`doc__frameworks_feo`
      - :ndf:`copy('status', need_id='doc__frameworks_feo')`

    * - :need:`wp__requirements_feat`
      - :need:`doc__frameworks_feo_feat_reqs`
      - :ndf:`copy('status', need_id='doc__frameworks_feo_feat_reqs')`

    * - :need:`wp__fdr_reports`
      - :need:`doc__req_inspection_frameworks_feo`
      - :ndf:`copy('status', need_id='doc__req_inspection_frameworks_feo')`

    * - :need:`wp__feature_arch`
      - :need:`doc__lifecycle`
      - :ndf:`copy('status', need_id='doc__lifecycle')`

    * - :need:`wp__feat_request`
      - :need:`doc__lifecycle`
      - :ndf:`copy('status', need_id='doc__lifecycle')`

    * - :need:`wp__requirements_feat`
      - :need:`feat_req__lifecycle__launch_support`
      - :ndf:`copy('status', need_id='feat_req__lifecycle__launch_support')`

    * - :need:`wp__fdr_reports`
      - -
      - -

    * - :need:`wp__feature_arch`
      - :need:`doc__orchestration_architecture`
      - :ndf:`copy('status', need_id='doc__orchestration_architecture')`

    * - :need:`wp__feat_request`
      - :need:`doc__orchestration`
      - :ndf:`copy('status', need_id='doc__orchestration')`

    * - :need:`wp__requirements_feat`
      - :need:`doc__orchestration_requirements`
      - :ndf:`copy('status', need_id='doc__orchestration_requirements')`

    * - :need:`wp__fdr_reports`
      - -
      - -

    * - :need:`wp__feature_arch`
      - :need:`doc__persistency_architecture`
      - :ndf:`copy('status', need_id='doc__persistency_architecture')`

    * - :need:`wp__feat_request`
      - :need:`doc__persistency`
      - :ndf:`copy('status', need_id='doc__persistency')`

    * - :need:`wp__requirements_feat`
      - :need:`doc__feature_persistency_requirements`
      - :ndf:`copy('status', need_id='doc__feature_persistency_requirements')`

    * - :need:`wp__fdr_reports`
      - :need:`doc__feature_persistency_requirements_chklst`
      - :ndf:`copy('status', need_id='doc__feature_persistency_requirements_chklst')`

    * - :need:`wp__platform_arch`
      - -
      - -

    * - :need:`wp__platform_dfa`
      - :need:`doc__score_platform_dfa`
      - :ndf:`copy('status', need_id='doc__score_platform_dfa')`

    * - :need:`wp__platform_handbook`
      - :need:`doc__platform_handbook`
      - :ndf:`copy('status', need_id='doc__platform_handbook')`

    * - :need:`wp__fdr_reports`
      - :need:`doc__score_platform_safety_analysis_fdr`
      - :ndf:`copy('status', need_id='doc__score_platform_safety_analysis_fdr')`

    * - :need:`wp__platform_safety_manual`
      - :need:`doc__score_platform_safety_manual`
      - :ndf:`copy('status', need_id='doc__platform_safety_manual')`

    * - :need:`wp__platform_safety_plan`
      - :need:`doc__score_platform_safety_plan`
      - :ndf:`copy('status', need_id='doc__score_platform_safety_plan')`

    * - :need:`wp__platform_security_manual`
      - -
      - -

    * - :need:`wp__platform_security_plan`
      - -
      - -

    * - :need:`wp__sw_platform_sbom`
      - -
      - -

    * - :need:`wp__fdr_reports`
      - :need:`doc__score_platform_safety_plan_fdr`
      - :ndf:`copy('status', need_id='doc__score_platform_safety_plan_fdr')`

    * - :need:`wp__platform_sw_release_note`
      - -
      - -

    * - :need:`wp__platform_sw_release_plan`
      - :need:`doc__platform_release_management_plan`
      - :ndf:`copy('status', need_id='doc__platform_release_management_plan')`

    * - :need:`wp__prm_plan`
      - :need:`doc__platform_problem_resolution_plan`
      - :ndf:`copy('status', need_id='doc__platform_problem_resolution_plan')`

    * - :need:`wp__process_description`
      - <https://eclipse-score.github.io/process_description/main/>`_
      - -

    * - :need:`wp__platform_mgmt`
      - :need:`doc__platform_mgt_plan`
      - :ndf:`copy('status', need_id='doc__platform_mgt_plan')`

    * - :need:`wp__qms_plan`
      - :need:`doc__platform_quality_plan`
      - :ndf:`copy('status', need_id='doc__platform_quality_plan')`

    * - :need:`wp__requirements_stkh`
      - :need:`doc__stakeholder_requirements`
      - :ndf:`copy('status', need_id='doc__stakeholder_requirements')`

    * - :need:`wp__sw_development_plan`
      - :need:`doc__software_development_plan`
      - :ndf:`copy('status', need_id='doc__software_development_plan')`

    * - :need:`wp__tailoring_work_products`
      - :need:`doc__platform_quality_plan`
      - :ndf:`copy('status', need_id='doc__platform_quality_plan')`

    * - :need:`wp__tlm_plan`
      - :need:`doc__platform_tool_management_plan`
      - :ndf:`copy('status', need_id='doc__platform_tool_management_plan')`

    * - :need:`wp__verification_plan`
      - :need:`doc__verification_plan`
      - :ndf:`copy('status', need_id='doc__verification_plan')`

    * - :need:`wp__verification_platform_int_test`
      - :ref:`project_documents_list`
      - -


1.3. Lists of all reports
=========================

Quality related work products
-----------------------------

.. list-table:: Quality related work products
    :header-rows: 1

    * - Workproduct Id
      - Link to WP
      - Status

    * - :need:`wp__process_impr_report`
      - -
      - -

    * - :need:`wp__qms_report`
      - :need:`doc__score_qms_report`
      - :ndf:`copy('status', need_id='doc__score_qms_report')`

    * - :need:`wp__tool_verification_report`
      - -
      - -

    * - :need:`wp__verification_platform_ver_report`
      - -
      - -

1.4. Test coverage
==================

    - Overview of test coverage (overall, requirements, architecture)
    - Ratio of test coverage to the :need:`wp__verification_plan`

1.5. Issues
===========

Issues are tracked in the :need:`wp__issue_track_system`. The issues are tagged with "quality"
<https://github.com/eclipse-score/score/issues?q=is%3Aissue%20state%3Aopen%20label%3Aquality>`_

1.6. Process Improvement
========================

Issues are tracked in the :need:`wp__issue_track_system`. The issues are tagged with "quality"
<https://github.com/eclipse-score/score/issues?q=is%3Aissue%20state%3Aopen%20label%3Aquality%20label%3Acommunity%3Aprocess>`_
