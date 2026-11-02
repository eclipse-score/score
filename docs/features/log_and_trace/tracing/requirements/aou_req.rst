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

.. document:: Tracing Assumption of Use
   :id: doc__tracing_aou_reqs
   :status: draft
   :version: 1
   :security: NO
   :safety: ASIL_B
   :realizes: wp__requirements_feat_aou[version==1]

Tracing Feature Assumption of Use
===============================================

.. aou_req:: Caller Logic precedence over Tracing
   :id: aou_req__tracing__caller_logic_precedence
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   A trace client shall give its own functionality precedence over tracing. It shall not wait for tracing and shall continue when trace calls fail.

.. aou_req:: Trace Client Responsible for Data Integrity
   :id: aou_req__tracing__data_integrity
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1

   The trace client is responsible for the integrity of the data it hands over, from the trace call until the API signals completion.
