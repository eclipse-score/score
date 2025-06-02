..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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


.. _workflow_safety_analysis:

Workflow Safety Analysis
########################

.. workflow:: Analyse Platform Architecture
   :id: wf__analyse_platarch
   :status: valid
   :tags: safety_analysis
   :responsible: rl__safety_engineer
   :approved_by: rl__safety_manager
   :supported_by: rl__contributor, rl__committer, rl__security_manager
   :input: wp__requirements__stkh, wp__issue_track_system
   :output: wp__platform_dfa
   :contains: gd_guidl__dfa_failure_initiators, gd_temp__feat_saf_dfa
   :has: doc_concept__safety__analysis, doc_getstrt__safety_analysis

   | The DFA for the platform is executed.

.. workflow:: Analyse Feature Architecture
   :id: wf__analyse_featarch
   :status: valid
   :tags: safety_analysis
   :responsible: rl__safety_engineer
   :approved_by: rl__safety_manager
   :supported_by: rl__contributor, rl__committer, rl__security_manager
   :input: wp__requirements__feat, wp__feature_arch, wp__issue_track_system
   :output: wp__feature_safety_analysis, wp__feature_dfa
   :contains: gd_guidl__dfa_failure_initiators, gd_temp__feat_saf_dfa, gd_guidl__fault_models, gd_temp__feat_saf_fmea
   :has: doc_concept__safety__analysis, doc_getstrt__safety_analysis

   | The safety analysis and DFA for the feature is executed.

.. workflow:: Analyse Component Architecture
   :id: wf__analyse_comparch
   :status: valid
   :tags: safety_analysis
   :responsible: rl__safety_engineer
   :approved_by: rl__safety_manager
   :supported_by: rl__contributor, rl__committer, rl__security_manager
   :input:  wp__requirements__comp, wp__component_arch, wp__issue_track_system
   :output: wp__sw_component_safety_analysis, wp__sw_component_dfa
   :contains: gd_guidl__dfa_failure_initiators, gd_temp__comp_saf_dfa, gd_guidl__fault_models, gd_temp__comp_saf_fmea
   :has: doc_concept__safety__analysis, doc_getstrt__safety_analysis

   | The safety analysis and DFA for the component is executed.

.. workflow:: Monitor Safety Analyses and DFA
   :id: wf__mr_saf_analyses_dfa
   :status: valid
   :tags: safety_analysis
   :responsible: rl__safety_engineer
   :approved_by: rl__safety_manager
   :supported_by: rl__contributor, rl__committer, rl__security_manager
   :input: wp__feature_safety_analysis, wp__feature_dfa, wp__sw_component_safety_analysis, wp__sw_component_dfa
   :output: wp__verification__platform_ver_report, wp__issue_track_system
   :contains: gd_guidl__dfa_failure_initiators, gd_temp__feat_saf_dfa, gd_temp__comp_saf_dfa, gd_guidl__fault_models, gd_temp__feat_saf_fmea, gd_temp__comp_saf_fmea
   :has: doc_concept__safety__analysis, doc_getstrt__safety_analysis

   | The safety analyses and DFA are monitored.

.. workflow:: Verify Safety Analyses and DFA
   :id: wf__vy_saf_analyses_dfa
   :status: valid
   :tags: safety_analysis
   :responsible: rl__safety_engineer
   :approved_by: rl__safety_manager
   :supported_by: rl__contributor, rl__committer, rl__security_manager
   :input: wp__feature_safety_analysis, wp__feature_dfa, wp__sw_component_safety_analysis, wp__sw_component_dfa
   :output: wp__verification__platform_ver_report, wp__saf_analysis_report
   :contains: gd_guidl__dfa_failure_initiators, gd_temp__feat_saf_dfa, gd_temp__comp_saf_dfa, gd_guidl__fault_models, gd_temp__feat_saf_fmea, gd_temp__comp_saf_fmea
   :has: doc_concept__safety__analysis, doc_getstrt__safety_analysis

   | The safety analyses and DFA are monitored and verified.


RAS(IC) for Safety Analysis
***************************


.. needtable:: RASIC Overview for Safety Analysis
   :tags: safety_analysis
   :filter: "safety_analysis" in tags and type == "workflow"
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
