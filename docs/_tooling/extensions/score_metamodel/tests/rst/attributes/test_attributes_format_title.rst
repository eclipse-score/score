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

#EXPECT: feat_req__test__abcd.title (This must work): contains a stop word: `must`.

.. feat_req:: This must work
   :id: feat_req__test__abcd

#EXPECT-NOT: feat_req__test__abce.title (This is a test): contains a stop word

.. feat_req:: This is a test
   :id: feat_req__test__abce
