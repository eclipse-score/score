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
   :id: WF_ANALYSE_FeatArch
   :status: draft
   :tags: safety_analysis
   :responsible: RL_committer
   :approver: RL_safety_manager
   :supporter: RL_technical_lead, RL_security_manager
   :input: WP_FEATURE_REQ, WP_FEATURE_ARCHITECTURE, WP_ISSUE_TRACK_SYSTEM
   :output: WP_FEATURE_SAFETY_ANALYSES, WP_FEATURE_DFA

   | The safety analysis and DFA for the feature is executed.

.. workflow:: Analyse Component Architecture
   :id: WF_ANALYSE_CompArch
   :status: draft
   :tags: safety_analysis
   :responsible: RL_committer
   :approver: RL_safety_manager
   :supporter: RL_module_lead, RL_security_manager
   :input:  WP_SW_COMPONENT_REQ, WP_SW_COMPONENT_ARCHITECTURE, WP_ISSUE_TRACK_SYSTEM
   :output: WP_SW_COMPONENT_SAFETY_ANALYSES, WP_SW_COMPONENT_DFA

   | The safety analysis and DFA for the component is executed.

.. workflow:: Monitor/Verify Safety Analyses and DFA
   :id: WF_MR_VY_SAF_ANALYSES_DFA
   :status: draft
   :tags: safety_analysis
   :responsible: RL_committer
   :approver: RL_safety_manager
   :supporter: RL_technical_lead, RL_module_lead, RL_security_manager
   :input: WP_FEATURE_SAFETY_ANALYSES, WP_FEATURE_DFA, WP_SW_COMPONENT_SAFETY_ANALYSES, WP_SW_COMPONENT_DFA
   :output: WP_SW_ARCH_VERIFICATION, WP_ISSUE_TRACK_SYSTEM

   | The safety analyses and DFA are monitored and verified.
   | The inspection shall be implemented as integral part of the review tool.
