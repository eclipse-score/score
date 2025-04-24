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
#CHECK: check_options

.. Required option: `status` is missing
#EXPECT: std_wp__test__abcd: is missing required option: `status`.

.. std_wp:: This is a test
   :id: std_wp__test__abcd

.. All required options are present
#EXPECT-NOT: is missing required option

.. std_wp:: This is a test
   :id: std_wp__test__abce
   :status: active

.. Satisfies link refers to wrong requirement type
#EXPECT: feat_req__abce.satisfies (['std_wp__test__abce']): does not follow pattern `^stkh_req__.*$`.

.. feat_req:: Child requirement
   :id: feat_req__abce
   :satisfies: std_wp__test__abce
