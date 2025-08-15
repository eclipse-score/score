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

.. _gen_ai_requirements:

Requirements
============

.. feat_req:: GenAI Execution
   :id: feat_req__gen_ai__workloads_execution
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__gen_ai__enablement
   :status: valid

   The platform shall support the execution of Generative AI models (e.g., LLMs) on embedded automotive hardware.

.. feat_req:: GenAI Interaction Layer
   :id: feat_req__gen_ai__ui
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__gen_ai__interaction
   :status: valid

   The platform shall provide a Prompting Interface for GenAI-based agents, enabling structured prompts, streaming output, and context-aware user interaction.

.. feat_req:: GenAI Action Validation
   :id: feat_req__gen_ai__validator
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__gen_ai__safety_filter
   :status: valid

   The platform shall validate all LLM-generated actions via domain-specific policies before they are executed.

.. feat_req:: Structured Vehicle Interface
   :id: feat_req__gen_ai__structured_vapi
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__gen_ai__vehicle_com
   :status: valid

   The platform shall provide structured APIs (e.g., via MCP) to access vehicle state and invoke safe vehicle commands.
