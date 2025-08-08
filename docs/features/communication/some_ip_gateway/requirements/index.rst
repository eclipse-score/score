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

.. feat_req:: Plug-In-IFC for SOME/IP protocol stacks
   :id: feat_req__some_ip_gateway__stack_plugin_ifc
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__communication__extensible_external
   :status: valid

   The SOME/IP Gateway shall support an interface to plug-in a SOME/IP stack implementation.

.. feat_req:: Plug-In-IFC for End-to-End protection modules
   :id: feat_req__some_ip_gateway__e2e_plugin_ifc
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__safe
   :status: valid

   The SOME/IP Gateway shall support an interface to plug-in a E2E protection service implementation.


.. feat_req:: SOME/IP Gateway Access Control
   :id: feat_req__some_ip_gateway__access_control
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The SOME/IP Gateway shall support access control to restrict access to the gateway services.

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
