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
#############

.. document:: Time
   :id: doc__time
   :status: valid
   :safety: ASIL_B
   :tags: change_management


.. toctree::
   :hidden:

   requirements.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_time``


Abstract
========


Motivation
==========

Efficient and accurate time management is critical in automotive systems, affecting functionality, safety, and reliability across various applications. Generally, time relevance can be categorized into the following levels:

* External Time Synchronization
* In-Vehicle Time Synchronization
* Clocks, Accuracy, and Reading Current Time
* Consistent Logical Time Within Cause-Effect Cycles


External Time Synchronization
--------------------------------

External time synchronization aims to align the vehicle's internal time reference with a global or external standard. The primary objective is to synchronize with universal time standards such as UTC, which enables accurate timestamping of data across geographically distributed systems, crucial for telematics, fleet management, and regulatory compliance (e.g., event logging, diagnostics, cybersecurity). Additional use cases include ensuring consistent timing across vehicles in a fleet to facilitate coordinated operations or data analysis. Typical synchronization methods include GPS-based satellite synchronization, backend server synchronization over cellular networks.


In-Vehicle Time Synchronization
----------------------------------

In-vehicle synchronization ensures all Electronic Control Units (ECUs) within a vehicle operate based on a consistent internal time reference, crucial for real-time and safety-critical applications such as autonomous driving, audio/video streaming, and event logging. The synchronization architecture generally involves designating a single ECU as the *Time Grand Master*, typically the ECU with the fastest boot-up time (often a zonal controller hosting a microcontroller portion). Other ECUs synchronize their internal clocks to this master.

Given the distributed nature of automotive E/E architectures, direct end-to-end synchronization across all ECUs is impractical due to latency and accumulated errors. Instead, synchronization typically occurs via peer-to-peer communication, with time gateways or zonal controllers acting as local masters within subnetworks to maintain accuracy. Network-specific synchronization protocols, such as gPTP for Ethernet, ensure robust, standardized synchronization.

S-CORE must support industry-standard synchronization protocols like gPTP (IEEE 802.1AS) for Ethernet-based networks, including restrictions defined in AUTOSAR's Time Synchronization Protocol. For CAN-based networks, synchronization standards defined by AUTOSAR, such as the Time Synchronization over CAN, should be supported.

todo: time syntonization vs synchronization
todo: add standards for other technologies
   for 1.0 concentrate (ntp), gptp, can?
   extend for time e.g. via someip

todo: should we support only gPTP or also PTP? for >1.0
todo: should we support NPT? for >1.0

for 1.0 we focus

Clocks, Accuracy, and Reading Current Time
---------------------------------------------

Software stacks contain multiple clock sources:

- Local Clocks: These include monotonic, system, steady, and high-resolution clocks, providing internal time references independent of external synchronization.
- Synchronized Clocks: These clocks are synchronized to external or internal standards and are critical for tasks requiring accurate timestamps or coordinated execution.
- Secure Clocks: Used specifically in cryptographic contexts to validate digital certificates or ensure secure transaction timestamps; these require protection against tampering and robust synchronization.

Programming languages typically abstract these clocks (e.g., ``std::chrono`` in C++, ``std::time`` in Rust). Therefore, the integration of S-CORE with existing language-specific abstractions is essential for consistency and ease of use.

TODO: differentiate between time base (e.g. identify source, synchronized clocks) and how the time is accessed (synchronized clock available via std::chrono)
TODO: S-CORE time/clocks should be explicitly targeted and not implicitly hidden in e.g. std::chrono. score::chrono e.g. could provide a  thin wrapper for std::chrono but the user should explicitly choose a score supported time to avoid confusion with std::chrono.

TODO: asking for a time stamp, should be as fast as possible.

TODO: states of synchronized clocks, how to handle them? e.g. asking for current time when the clock is not synchronized. Error handling should be possible on per app use-case.
TODO: should we expose the information on time difference since the last synchronization? dedicated api required.

TODO: alignment with Crypto feature request on secure clocks

note: the daemon that is responsible for the nw time synrchonization should also synchronize the local hw clock.

TODO: use existing time synchronization form OS or develop own? Use OS provided might me used for development but finally we need a qualified time synchronization for production.


Consistent Logical Time Within Cause-Effect Cycles
-----------------------------------------------------

In automotive applications, cause-effect chains or distributed algorithms frequently collaborate within defined execution cycles. Within these cycles, it is crucial that all involved algorithms reference the **same logical time** despite potential differences in actual execution start times. Maintaining consistent logical timing within cycles ensures accurate data integration and computational coherence. This consistency is particularly vital in applications such as sensor fusion, control systems, and coordinated vehicle dynamics, where discrepancies in perceived time could lead to inaccuracies in integrated values (e.g., vehicle speed, acceleration, or positional calculations).

The capability to record and replay logical time is also crucial for providing a sufficient simulation environment for algorithms. This feature enables developers to test and validate algorithms under controlled and repeatable conditions, ensuring their robustness and reliability before deployment. By simulating consistent logical time, it becomes possible to analyze the behavior of distributed systems, identify potential issues, and optimize performance in scenarios that closely mimic real-world operations.

todo: add reasoning why "the same logical time" is crucial in a cause-effect/task chain (e.g., integrating speed to ...)

note: potentially exposing the current time stamp by the executor and make it available via IPC to the activities. within activities this could be abstraced by a time api but therefore the time is recordable and replayable.

Differentiation between where logical time is required.





.. Rationale
.. ==========


Specification
=============


.. Backwards Compatibility
.. =======================


Security Impact
===============


Safety Impact
=============


.. License Impact
.. ==============


How to Teach This
==================

.. Rejected Ideas
.. ==============

.. Open Issues
.. ===========

Glossary
========


.. _footnotes:

Footnotes
=========
