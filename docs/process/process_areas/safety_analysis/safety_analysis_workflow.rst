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

todo: need to add guidance and standard links

.. workflow:: Analyse Feature Architecture
   :id: wf__analyse_featarch
   :status: draft
   :tags: safety_analysis
   :responsible: rl__committer
   :approved_by: rl__safety_manager
   :supported_by: rl__technical_lead, rl__security_manager
   :input: wp__requirements__feat, wp__feature_arch, wp__issue_track_system
   :output: wp__feature_safety_analysis, wp__feature_dfa

   | The safety analysis and DFA for the feature is executed.

.. workflow:: Analyse Component Architecture
   :id: wf__analyse_comparch
   :status: draft
   :tags: safety_analysis
   :responsible: rl__committer
   :approved_by: rl__safety_manager
   :supported_by: rl__module_lead, rl__security_manager
   :input:  wp__requirements__comp, wp__component_arch, wp__issue_track_system
   :output: wp__sw_component_safety_analysis, wp__sw_component_dfa

   | The safety analysis and DFA for the component is executed.

.. workflow:: Monitor/Verify Safety Analyses and DFA
   :id: wf__mr_vy_saf_analyses_dfa
   :status: draft
   :tags: safety_analysis
   :responsible: rl__committer
   :approved_by: rl__safety_manager
   :supported_by: rl__technical_lead, rl__module_lead, rl__security_manager
   :input: wp__feature_safety_analysis, wp__feature_dfa, wp__sw_component_safety_analysis, wp__sw_component_dfa
   :output: wp__sw_arch_verification, wp__issue_track_system

   | The safety analyses and DFA are monitored and verified.
   | The inspection shall be implemented as an integral part of the review tool.




RAS(IC) for Safety Analysis
***************************


.. needtable:: RASIC Overview for Safety Analysis
   :tags: safety_analysis
   :filter: "safety_analysis" in tags and type == "workflow"
   :style: table
   :sort: status
   :columns: id as "Activity";responsible as "Responsible";approved_by as "Approver";supported_by as "Supporter"
   :colwidths: 30,30,30,30
