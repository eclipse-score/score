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

.. Test xy
#EXPECT: stkh_req__test__abcd.content (This should really work): contains a weak word: `really`.

.. stkh_req:: This is a test
   :id: stkh_req__test__abcd

   This should really work

#EXPECT-NOT: stkh_req__test__abce.title (This should work): contains a weak word

.. stkh_req:: This is a test
   :id: stkh_req__test__abce

   This should work
