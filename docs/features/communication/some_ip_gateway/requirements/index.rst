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
   :satisfies: stkh_req__communication__extensible_external, stkh_req__communication__supported_net
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

.. feat_req:: Compatibility with `some-ip.com <https://some-ip.com/>`_ Protocol Specification
   :id: feat_req__some_ip_gateway__someip_protocol
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__supported_net
   :status: valid

   The SOME/IP protocol implementation shall be fully compatible and complying with the SOME/IP protocol specification from `some-ip.com <https://some-ip.com/>`_.

.. feat_req:: Compatibility with `some-ip.com <https://some-ip.com/>`_ E2E Protocol Specification
   :id: feat_req__some_ip_gateway__e2e_specs
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__supported_net
   :status: valid

   The E2E protection implementation shall be fully compatible and complying with the E2E protocol specification from `some-ip.com <https://some-ip.com/>`_.

.. feat_req:: Compatibility with `some-ip.com <https://some-ip.com/>`_ SOME/IP Service Discovery Protocol Specification
   :id: feat_req__some_ip_gateway__someip_sd_protocol
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__communication__supported_net
   :status: valid

   The Service Discovery implementation shall be fully compatible and complying with the SOME/IP service discovery specification from `some-ip.com <https://some-ip.com/>`_.
