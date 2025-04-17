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
#CHECK: check_extra_options

#EXPECT: std_wp__test__abcd: has these extra options: `safety`.

.. std_wp:: This is a test
   :id: std_wp__test__abcd
   :safety: QM

#EXPECT-NOT: std_wp__test__abce: has these extra options

.. std_wp:: This is a test
   :id: std_wp__test__abce
