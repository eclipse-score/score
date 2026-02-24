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



**<In its final form (status = valid), Platform Verification Report must contain:>**

**1. List of requirements and architecture tested**

       - List of requirements (stakeholder and feature) tested by which test
       - List of architecture elements tested by which test (can be several levels)
       - For all tests "passed/failed" shall be reported
       - For all tests, completeness verdict shall be report, including normal operation and failure reactions
       - The list of requirements may also contain other verification methods like “Analysis”

**2. Safety analyses**
       - Formal evidence about the performed Platform DFA
       - Formal evidence about the performed Platform Safety Analyses (this has to be compared against safety plan, i.e. needed only if FMEA actually planned on platform level)
       - Final statement resume (i.e. all passed, or are there open points, further actions needed, justifications etc.)

**2. Integration test results**
       - Test results per test case from Platform Integration Test (:need:`wp__verification_platform_int_test`)
       - Test results per test case from  Feature Integration test (:need:`wp__verification_feat_int_test`)
       - All test results shall include status ("passed/failed/not_run")

**3. Integration test logs**
       - Test log per test case from Platform Integration Test (:need:`wp__verification_platform_int_test`)
       - Test log per test case from  Feature Integration test (:need:`wp__verification_feat_int_test`)
       - All test results shall include status ("passed/failed/not_run")
