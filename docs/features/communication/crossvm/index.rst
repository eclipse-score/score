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

.. _crossvm_feature:

Cross Virtual Machine Communication
###################################

.. document:: Cross-VM Communication
   :id: doc__com_crossvm
   :status: valid
   :safety: ASIL_B
   :tags: feature_modification_request


.. toctree::
   :maxdepth: 2

   ./requirements/index


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_crossvm_com``

Abstract
========

This feature provides mechanisms for communication and data exchange between processes in different Virtual Machines (VM).
It includes two classes of communication/data-exchange:

1. One-way data sharing into a VM for (vehicle) state read-only for the VM (snapshot state)
   - Read-only for consumer (VM)
   - Support for consistent data-sets (consumer must be able to get a consistent version of related data items)
   - Consistent access must be lock-free
   - Producer time stamps shall be available for related data-sets

2. Streamed data based on shared queues (stream of events or data)
   - Queues shall be configurable by client (VM) (number of elements etc..)
   - Size of a queue
   - Allocation of buffers for the data elements
   - Queues shall support lock-free access to data elements
   - Support for bi-directional communication via writable data elements by the client
   - Asynchronous bi-directional support via multiple queues

Motivation
==========

Cross-VM communication mechanisms are essential to ensure efficient and reliable data exchange between VMs.

Rationale
=========

These communication mechanisms are developed to address specific needs for data sharing and streaming in a VM environment, ensuring consistent and lock-free access to data.

Specification
=============

The Cross-VM communication feature consists of the following mechanisms:

- **One-way data sharing**: Allows read-only access to vehicle state data in a VM, ensuring consistency and lock-free access.
- **Streamed data**: Utilizes shared queues for streaming events or data, configurable by the client, supporting bi-directional communication.

General requirements:
---------------------

- Multiple chunks of shared memory shall be supported to allow required access control.
- Notifications for data updates shall be available (virtual IRQs in a VM).
- Notifications shall be configurable by consumers of data (using flags or watermarks in shared memory from client to producer).

Backwards Compatibility
=======================

It should be shure that both Cross-VM and normal IPC work seamlessly together

Security Impact
===============

Cross-VM communication mechanisms present varying security risks as vulnerabilities could affect multiple components simultaneously.
Each mechanism requires individual security impact analysis based on its functionality and usage patterns.

Safety Impact
=============

- Due to wide usage of these communication mechanisms throughout the platform, extra care is needed in design, implementation, and testing to minimize safety impact.
- Mechanisms are developed at various integrity levels from QM (non-safety) up to ASIL-B, depending on their intended use cases.
- Freedom from Interference has to be taken into account when different VMs

License Impact
==============

The Cross-VM communication mechanisms are licensed under Apache License 2.0.

How to Teach This
=================

Each mechanism is expected to have a user manual that includes an API reference and usage examples where necessary.

Rejected Ideas
==============

There are no rejected ideas related to the Cross-VM communication feature at this time.

Open Issues
===========

There are currently no open issues related to the Cross-VM communication feature.
