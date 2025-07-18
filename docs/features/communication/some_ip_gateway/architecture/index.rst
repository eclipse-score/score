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

.. _some_ip_gateway_architecture:

SOME/IP Gateway Architecture
############################

.. note::
   For now we store the component architecture in the feature tree, because multi-repo docs are not yet supported.
   Once this support becomes available the component architecture will be moved to the module.

.. toctree::
   :titlesonly:

SOME/IP Gateway on one side is a regular participant in IPC and uses the according mechanisms to publish
data or to subscribe to data. As such it will need to know and understand the data types that are used in
the IPC network.

It also is a participant in the SOME/IP network and provides services for the service oriented communication.
This shall be possible by including SOME/IP stacks that are AUTOSAR compliant.

There need to be some components between the two communication networks as data types and their according representations and
transmission cadence can be different. Translation of data types could be handled in some translation module
that might be independent of the rest of the gateway. But buffering / queuing of messages, events, signals
should be mostly freely programmable by integrators using the SOME/IP gateway.


.. figure:: some_ip_gateway_architecture.drawio.svg
   :align: center
   :name: _some_ip_gateway_architecture

   General overview of SOME/IP Gateway


SOME/IP stacks as supplied by AUTOSAR vendors mostly are available as QM only.
In the case that SOME/IP implementations are not developed under ASIL-B constraints, adequate measures need to be taken to
separate this QM component from the otherwise ASIL-B compliant components. This may be achieved through separate processes,
which again will require dedicated inter-process-communication between the SOME/IP-stack and the rest of the gateway.
It is preferred to avoid such additional IPC.

.. figure:: some_ip_gateway_details.drawio.svg
   :align: center
   :name: _some_ip_gateway_details

   Detailed components view of SOME/IP Gateway
