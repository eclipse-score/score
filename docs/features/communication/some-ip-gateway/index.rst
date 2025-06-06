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

.. _some_ip_gateway_feature:

SOME/IP-Gateway
###########################

.. document:: SOME/IP-Gateway
   :id: _some_ip_gateway_feature
   :status: valid
   :safety: ASIL_B
   :tags: contribution_request, feature_request


.. toctree::
   :hidden:

   architecture/index.rst
   requirements/index.rst
   roadmap.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_some-ip-gateway``

Abstract
========

This contribution describes how data-exchange that is outside the scope of internal communication (IPC) shall be handled in modules that service data-input and data-output to a platform.
Services handling data in this context can be considered as gateways.
The focus is on a gateway to handle SOME/IP communication with external devices or counterparts, therefore this feature request is called: SOME/IP-Gateway

This feature request includes:
- A description of how a SOME/IP gateway service (or data broker) shall be implemented
- How the SOME/IP gateway services shall integrate with the zero-copy communication from IPC (which might become a general description of how services plug-in to the IPC context)

.. _Motivation:

Motivation
==========

S-CORE is targeting high-performance automotive systems with safety impact. Applications integrated on S-CORE will be distributed across multiple processes and frameworks (like FEO)
that schedule software components (i.e. activities) with the need to exchange data.
For data-exchange between applications the IPC feature is providing high-speed communication capabilities, but when it comes to communication with applications outside the scope of
the S-CORE platform, services are required that will handle protocols for communication with both side. This is for instance the case when communication with rest of vehicle or sensors
needs to be realized with the SOME/IP protocol.

For software component developers it should be unrecognized that data is originated from a SOME/IP communication channel, the data should be provided with the same API as in IPC.
Nonetheless integrators and architects will have to configure the system to receive or send data over SOME/IP, hence provide it as a SOME/IP service.

SOME/IP Gateway Security Goals
------------------------------

The security approach for SOME/IP shall achieve the following security goals:

- to be defined

Safety Impact
=============

  # The safety impact was already exhaustively covered in :ref:`mot_mixed_criticality` and :ref:`spec_mixed_criticality`.

  # Overall, the communication framework supports use cases up to ASIL-B (:need:`feat_req__ipc__asil`).
  # Future extension to ASIL-D use cases is feasible but not in scope for now.

License Impact
==============

[How could the copyright impacted by the license of the new contribution?]


How to Teach This
=================
