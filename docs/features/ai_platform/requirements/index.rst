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

.. _ai_platform_requirements:

Requirements
============

.. feat_req:: ML Execution
   :id: feat_req__ai_platform__workloads_execution
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   The platform shall support the execution of traditional ML models on embedded automotive hardware.

.. feat_req:: ASIL-B ML Inference
   :id: feat_req__ai_platform__safety_backends
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__safety_critical
   :status: valid

   The platform shall support deployment of safety-certified inference backends and abstraction layers for ASIL-B use cases.

.. feat_req:: Efficient Embedded Runtime
   :id: feat_req__ai_platform__embedded_efficiency
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__ai_platform__runtime_efficiency
   :status: valid

   The platform shall optimize runtime performance and memory usage to meet the constraints of automotive edge hardware.

.. feat_req:: Cross-OS Portability
   :id: feat_req__ai_platform__qnx_linux_support
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__ai_platform__platform_portability
   :status: valid

   The platform shall support portable AI components that run on both QNX (ASIL-B) and Linux environments.

.. feat_req:: Verified Model Execution
   :id: feat_req__ai_platform__model_verification
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__ai_platform__model_security
   :status: valid

   The platform shall ensure model artifacts are verified via cryptographic signatures before execution, and model loading is restricted to trusted paths.

.. feat_req:: Static Backend Selection
   :id: feat_req__ai_platform__static_backend
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__runtime_determinism
   :status: valid

   The platform shall select inference backends statically at build time to ensure deterministic runtime behavior.
