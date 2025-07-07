..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

SOME/IP Gateway Requirements
############################


Functional Requirements
=======================



Security Impact
===============



Safety Impact
=============

.. feat_req:: SOME/IP Gateway ASIL level
   :id: feat_req__some_ip_gateway__asil
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__communication__safe
   :status: valid

   The SOME/IP Gateway shall support safe communication up to ASIL-B.

.. feat_req:: SOME/IP Gateway QM network stack
   :id: feat_req__some_ip_gateway__network_stack
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__communication__safe
   :status: valid

   If SOME/IP network stacks are available as QM only.
