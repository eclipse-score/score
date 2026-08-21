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

.. _time_feature:

Time
####

.. document:: Time
   :id: doc__time
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :tags: time, feature_request, change_management
   :realizes: wp__feat_request[version==1]


.. toctree::
   :maxdepth: 1
   :glob:
   :titlesonly:
   :hidden:

   architecture/index
   requirements/index
   requirements/aou_req

Abstract
========

The :term:`score::time` feature provides applications with a uniform, type-safe API for reading
time from three independent time bases: :term:`Vehicle Time` (network-synchronized),
local time (OS clocks) and :term:`Absolute Time` (external UTC source). The feature owns
the synchronization of the synchronized time bases and supports test-time substitution of all
clock interfaces.

Motivation
==========

Efficient and accurate time management is critical in automotive systems, affecting functionality, safety, and reliability across various applications. Time handling spans several layers, from synchronization with external time sources to the consistent use of logical time within in-vehicle software cycles. For this reason, the motivation section describes the context broadly, even if the actual feature request later focuses on a more specific scope.

External Time Synchronization
-----------------------------

.. figure:: _assets/timesync-external.drawio.svg
   :alt: External Time Synchronization
   :align: center

External time synchronization establishes a reference to a global time standard, such as UTC, through methods like GPS-based synchronization or backend servers accessed via cellular networks. These time sources are relevant for fleet-wide timestamping, telematics, and ensuring regulatory compliance (e.g., event logging, cybersecurity).

The details of external synchronization are out of scope for this request but are included to clarify the overall context.

In-Vehicle Time Synchronization
-------------------------------

.. figure:: _assets/timesync-vehicle.drawio.svg
   :alt: In-Vehicle Time Synchronization
   :align: center

Within the vehicle, synchronization ensures that all ECUs reference a consistent internal time. In modern architectures, this is achieved by designating a statically defined Time Grand Master, typically a zonal controller equipped with a fast-booting microcontroller and responsible for early vehicle functions such as key detection. This controller synchronizes with the external time source and propagates time over the in-vehicle network.

The synchronization protocols relevant here are primarily Ethernet-based. The focus lies on gPTP (IEEE 802.1AS) and the corresponding specifications in AUTOSAR Adaptive to ensure compatibility with existing ECUs. :term:`Syntonization`, the alignment of clock frequency, is as essential as synchronization and must be supported to maintain long-term timing consistency.

Bridging between different network domains (e.g., Ethernet to CAN) is outside the scope of this feature. In the system context, the High-Performance Computer (HPC) is assumed to be a slave in the time distribution topology and connects via Ethernet to the grandmaster. Time synchronization within CAN segments, typically handled by zonal controllers, is not covered by this feature.

Clocks, Accuracy, and Reading Current Time
------------------------------------------

Modern software environments contain several types of clocks (or time bases), including:

* Local clocks, such as monotonic or steady clocks
* Synchronized clocks, aligned with a vehicle-wide or external time base
* Secure or authentic clocks, protected against tampering

Mixing clock types unintentionally can lead to non-deterministic behaviors, negatively affecting system stability and correctness. Therefore, explicit selection of the time base by the application is mandatory. TimePoints of different clocks shall be incompatible types.

Applications must be able to detect when a chosen time base is invalid or unsynchronized, enabling them to define appropriate fallback or error-handling strategies. Error states or drift conditions must be detectable by the application.

Clock introspection capabilities are required, allowing applications to determine synchronization status and time elapsed since the last successful synchronization. This information is vital during error handling or fallback situations.

Access to TimePoints should be as performant as technically feasible due to their frequent use in control loops and high-frequency applications. Although specific latency targets are not defined here, low latency is a fundamental design consideration.

For cryptographic scenarios the feature also targets secure or authentic clocks. In such cases, a tamper-resistant time source is needed to ensure that time cannot be rolled back to re-enable expired certificates or bypass security controls. Authentic clocks might be signed or verified using hardware security modules.

Within :term:`score::time`, secure or authentic clocks correspond to the :term:`Absolute Clock`,
which carries a :term:`security qualifier` indicating whether the received time may be treated as
trustworthy. Hardware security module integration is out of scope for the feature.

To integrate cleanly with modern programming languages, the time access API aligns with idiomatic constructs (e.g., ``std::chrono`` in C++, ``time`` in Rust), while making clear that the source of time is provided by the S-CORE platform. The :term:`score::time` namespace wraps native types to make the time source explicit.

Consistent Logical Time Within Cause-Effect Cycles
--------------------------------------------------

.. figure:: _assets/timesync-chain.drawio.svg
   :alt: Consistent Logical Time Within Cause-Effect Cycles
   :align: center

In distributed automotive applications, control logic is often structured into cause-effect chains. These chains consist of multiple interdependent tasks executing concurrently. Within each cycle of these chains, it is critical that all tasks perceive the same logical timestamp, even if their execution occurs at different actual CPU times.

Sharing a consistent logical timestamp ensures deterministic computations. For instance, integrating sensor measurements such as speed over time into position data requires stable and jitter-resilient timestamps shared across tasks. Additionally, consistent logical time enables reproducibility in testing, simulation, and validation scenarios, as the sequence and timing of events can be reliably replayed.

Logical time must be explicitly provided to the tasks within these cause-effect chains, but its availability in background processes or non-time-sensitive tasks is not required.

Consistent logical time for cause-effect chains is out of scope for :term:`score::time`; it is a
scheduling and middleware concern, not a clock domain provided by this feature.


.. Rationale
.. ==========


Specification
=============

The core time model concepts — :term:`Clock`, :term:`TimePoint`, :term:`TimeSpan` and their
operations and properties — are formally defined in the :doc:`Terms and Definitions <glossary>`.

Architectural design
--------------------

.. toctree::
   :maxdepth: 1
   :glob:

   ./architecture/index


Requirements
============

.. toctree::
   :maxdepth: 1
   :glob:

   ./requirements/*

Security Impact
===============

:term:`Absolute Time` carries a :term:`security qualifier` indicating whether the received time
may be treated as trustworthy. :term:`Vehicle Time` and local time bases have no security
relevance. Applications consuming Absolute Time shall check the security qualifier before using
the :term:`TimePoint` in security-sensitive operations.

Safety Impact
=============

:term:`Vehicle Time` is the only time base with a safety-relevant qualifier. Its
:term:`Snapshot` carries a :term:`Time point qualifier` indicating whether the
:term:`TimePoint` may be treated as ASIL-B data or only as QM data. All other time bases
(local time bases, :term:`Absolute Time`) are QM.

Terms and Definitions
=====================

.. toctree::
   :maxdepth: 1

   glossary
