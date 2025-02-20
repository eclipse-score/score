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

Safety Analysis
===============


Workflows
---------

todo: need to add guidance and standard links


.. workflow:: Analyse Feature Architecture
   :id: wf_analyse_featarch
   :status: draft
   :tags: safety_analysis
   :responsible: rl_committer
   :approved_by: rl_safety_manager
   :supported_by: rl_technical_lead, rl_security_manager
   :input: wp_feature_req, wp_feature_architecture, wp_issue_track_system
   :output: wp_feature_safety_analyses, wp_feature_dfa

   | The safety analysis and DFA for the feature is executed.

.. workflow:: Analyse Component Architecture
   :id: wf_analyse_comparch
   :status: draft
   :tags: safety_analysis
   :responsible: rl_committer
   :approved_by: rl_safety_manager
   :supported_by: rl_module_lead, rl_security_manager
   :input:  wp_sw_component_req, wp_sw_component_architecture, wp_issue_track_system
   :output: wp_sw_component_safety_analyses, wp_sw_component_dfa

   | The safety analysis and DFA for the component is executed.

.. workflow:: Monitor/Verify Safety Analyses and DFA
   :id: wf_mr_vy_saf_analyses_dfa
   :status: draft
   :tags: safety_analysis
   :responsible: rl_committer
   :approved_by: rl_safety_manager
   :supported_by: rl_technical_lead, rl_module_lead, rl_security_manager
   :input: wp_feature_safety_analyses, wp_feature_dfa, wp_sw_component_safety_analyses, wp_sw_component_dfa
   :output: wp_sw_arch_verification, wp_issue_track_system

   | The safety analyses and DFA are monitored and verified.
   | The inspection shall be implemented as integral part of the review tool.
