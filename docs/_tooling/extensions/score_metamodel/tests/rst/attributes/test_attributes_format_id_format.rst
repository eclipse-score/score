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

#EXPECT: std_wp__test__test__abcd.id (std_wp__test__test__abcd): expected to consisting of this format: `<Req Type>__<Abbreviations>__<Architectural Element>`.

.. std_wp:: This is a test
   :id: std_wp__test__test__abcd

#EXPECT-NOT: std_wp__test__abce.id (std_wp__test__abce): expected to consisting of this format: `<Req Type>__<Abbreviations>__<Architectural Element>`.

.. std_wp:: This is a test
   :id: std_wp__test__abce

#EXPECT: wp__test__test__abcd.id (wp__test__test__abcd): expected to consisting of one of these 2 formats:`<Req Type>__<Abbreviations>` or `<Req Type>__<Abbreviations>__<Architectural Element>`.

.. std_wp:: This is a test
   :id: wp__test__test__abcd

#EXPECT-NOT: wp__test__abce.id (wp__test__abce): expected to consisting of one of these 2 formats:`<Req Type>__<Abbreviations>` or `<Req Type>__<Abbreviations>__<Architectural Element>`.

.. std_wp:: This is a test
   :id: wp__test__abce
