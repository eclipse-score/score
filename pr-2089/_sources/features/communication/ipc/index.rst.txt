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

.. _communication_ipc:

Inter-process Communication
###########################

.. document:: Inter-process Communication
   :id: doc__com_ipc
   :status: valid
   :tags: contribution_request, feature_request

.. toctree::
   :maxdepth: 1
   :glob:
   :titlesonly:
   :hidden:

   docs/**/index
   docs/roadmap

Feature flag
============

To activate this feature, use the following feature flag:

``experimental_ipc``

.. _ipc_overview:

Overview
========

This contribution describes a framework to exchange information between processes.
This framework includes:

- a communication mechanism that enables zero-copy communication
- a mock binding for testing

The proposed IPC mechanism (called LoLa) is optimized for micro-kernel operating systems (like e.g. QNX). By
utilizing shared memory, it enables low latency communication also for mixed-criticality systems (e.g. processes of
different safety integrity level). The possibility for mixed-criticality systems is especially enabled by certain
implementation choices and safety mechanisms that will continue to ensure freedom from interference between separate
processes.

.. _ipc_description:

Description
===========

As S-CORE is targeting high-performance ECUs application will run on different processes of the OS. To fulfill the system needs, these processes need to exchange information. The IPC framework is not a one-fits-all. For example, it does not replace a standardized platform API that an application links against.

For the IPC framework also the Key- and Secondary Aspects of the general communication framework are valid as mentioned in :ref:`com_rationale`

The basic idea of the ipc binding concept is to use two main operating system facilities:

#. Shared Memory: Shall be used for the heavy lifting of data exchange
#. Message Passing: Shall be used as notification mechanism

A more detailed description is provided in the architecture chapter :ref:`ipc_architecture`

.. _ipc_specification:

Specification
=============

For IPC also the specification of communication applies: :ref:`com_specification`

Architecture
------------

The architecure of communication is diplayed :ref:`here<ipc_architecture>`

Requirements
------------

The requirements for communication are listed :ref:`here<ipc_requirements>`

.. _ipc_security:

Security Impact
---------------

In addition to the security impact of :ref:`commnication<com_security_impact>` the IPC binding achieves the security goals:

- :need:`confidentiality <feat_req__ipc__confidentiality>`
- :need:`integrity <feat_req__ipc__integrity>`
- :need:`availability <feat_req__ipc__availability>` (per criticality-level)
