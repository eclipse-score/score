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

Platform Verification Report
============================

.. document:: Platform Verification Report
   :id: doc__platform_verification_report
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__verification_platform_ver_report
   :tags:



In its final form (status = valid), Platform Verification Report must contain:

   - List of requirements (stakeholder and feature) and architecture tested by which test
     (can be several levels), passed/failed and completeness verdict, including normal
     operation and failure reactions
   - The list of requirements may also contain other verification methods like "Analysis"
   - Formal evidence about the performed DFA
   - Formal evidence about the performed Safety Analyses (if planned)
   - Summary reports ("all passed" or OPs, justifications, planned actions etc.) for the above safety analyses
   - Test result per test case from
     :need:`wp__verification_platform_int_test` and :need:`wp__verification_feat_int_test`
     with status passed/failed/not_run
   - Test log per test case from
     :need:`wp__verification_platform_int_test` and :need:`wp__verification_feat_int_test`
     with status passed/failed/not_run
