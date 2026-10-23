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

.. document:: Tracing Assumption of Use Requirements
   :id: doc__tracing_aou_reqs
   :status: draft
   :version: 1
   :security: NO
   :safety: ASIL_B
   :realizes: wp__requirements_feat_aou[version==1]

Tracing Feature Assumption of Use Requirements
===============================================

.. aou_req:: Tracing Not Used in Production
   :id: aou_req__tracing__not_in_production
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   Tracing shall not be used in production.

.. aou_req:: Caller Logic Priority Over Tracing
   :id: aou_req__tracing__caller_logic_priority
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   Callers shall prioritize their own logic over tracing.

.. aou_req:: Trace Client Responsible for Data Contiguity
   :id: aou_req__tracing__data_contiguity
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   It is the responsibility of the trace client to maintain data contiguity.
