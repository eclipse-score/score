..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

Time Architecture
=================

.. document:: Time Architecture
   :id: doc__time_architecture
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_arch[version==1]

Overview
--------

The Time feature (:term:`score::time`) provides applications with a uniform way to read
time from several distinct :term:`clock domain` s. The domain is selected explicitly by the
application, which keeps the interface consistent across domains while preventing accidental
mixing of incompatible :term:`TimePoint` types.

The architecture distinguishes three time bases (:term:`clock domain` s), each exposed through its
own clock interface:

* **Vehicle Time** — the network-synchronized (:term:`PTP protocol`) vehicle-wide time base,
   carrying a :term:`Vehicle Time status` qualifier. It is exposed through the
   :term:`Vehicle Clock`, which — because the time base depends on external synchronization — also
   offers initialization, availability checks and event subscription in addition to reading the time.
* **Local Time** — the local, non-synchronized time bases (steady, system and high-resolution).
   They are exposed through the :term:`Local Clock`, need no initialization and are always
   available.
* **Absolute Time** — an external absolute time base (e.g. UTC from GPS), carrying an
   :term:`Absolute Time status` qualifier that reflects both accuracy and security. It is exposed
   through the :term:`Absolute Clock`.

Because each :term:`clock domain` is independent and exposed through its own logical interface,
the architecture is open to future time bases (for example a further synchronized or secure
domain): a new domain is added as an additional interface without changing the existing ones.

Description
-----------

Uniform clock access
********************

All clock domains are exposed through a common, domain-agnostic interface so that
applications use the same operations regardless of which time base they read. Reading the
time returns a :term:`Snapshot` that bundles the :term:`TimePoint` with the domain's status
concept (:term:`Vehicle Time status` for the vehicle clock, :term:`Absolute Time status` for the
absolute clock; the local clocks carry no status), so callers can read the time and judge its
quality in a single call.

Rationale Behind Architecture Decomposition
*******************************************

The feature is decomposed along its **time bases**. Each :term:`clock domain` is an independent
time base with its own epoch, progression semantics, :term:`TimePoint` type and status concept.
The domains are logically and functionally independent: an application selects one explicitly,
and time values of different domains are distinct, incompatible types that cannot be mixed.

Independence does not imply isolation. A time base may build on or use another — for example a
synchronized domain interpolates between synchronization updates on top of a local monotonic base,
and the :term:`System Clock` is kept aligned to :term:`Absolute Time` through the OS
``CLOCK_REALTIME`` — but such relationships are internal and do not couple the interfaces the
domains expose.

The synchronized time bases (Vehicle Clock and Absolute Clock) additionally rely on an external
time reference and on validation of the received time. They *may* share a common supporting
component for obtaining and validating that time, but such reuse is an implementation choice, not
an architectural constraint: each synchronized domain could equally be served on its own.

Accordingly the feature exposes one self-contained logical interface per group of time bases:
the Vehicle Clock, the Absolute Clock, and the Local Clock. The local, non-synchronized clocks
(steady, system and high-resolution) are grouped behind a single interface because they share the
same minimal operation surface (a single time read); they remain distinct domains, differing only
in their semantics, which is captured in a domain table rather than in separate architectural
elements.

Requirements
------------

The Feature requirements are described in the :doc:`requirements index <../requirements/index>`.

Feature Overview
----------------

.. feat:: Time
   :id: feat__time
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1

The runtime (static and dynamic) architecture is defined in the ``inc_time`` module
(`Time Feature Architecture <https://eclipse-score.github.io/time>`_).

Time Bases
----------

Each time base is presented with the logical interface it exposes and, where it involves
runtime synchronization behavior, its dynamic view. The local, non-synchronized clocks
resolve to a direct time read from the OS.

Vehicle Time
************

The Vehicle Clock exposes the network-synchronized vehicle time. Because it depends on external
synchronization, it additionally offers subscription to synchronization events, on top of reading the time.

Logical Interface
^^^^^^^^^^^^^^^^^

.. logic_arc_int:: Vehicle Clock
   :id: logic_arc_int__time__vehicle_clock
   :included_by: feat__time
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__time__vehicle_time_time_api[version==1], feat_req__time__vehicle_time_acc_qual_api[version==1], feat_req__time__vehicle_time_time_pt_qual[version==1], feat_req__time__vehicle_time_sync_log[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: now
   :id: logic_arc_int_op__time__vehicle_now
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__time__vehicle_clock

   Returns the current vehicle-time :term:`Snapshot` (:term:`TimePoint` plus :term:`Vehicle Time status`).

.. logic_arc_int_op:: subscribe
   :id: logic_arc_int_op__time__vehicle_subscribe
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__time__vehicle_clock

   Registers a callback that is notified on vehicle-time synchronization events.

.. logic_arc_int_op:: unsubscribe
   :id: logic_arc_int_op__time__vehicle_unsubscribe
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__time__vehicle_clock

   Removes a previously registered synchronization-event callback.

Local Time
**********

The Local Clock groups the local, non-synchronized time bases, provided directly by the
operating system clocks. All variants expose a single ``now`` operation returning a
:term:`Snapshot`; they require no initialization and are always available. The concrete domains
are:

.. list-table:: Local Clock domains
   :header-rows: 1
   :widths: 30,70

   * - Domain
     - Semantics
   * - :term:`High-Resolution Clock`
     - Monotonic, nanosecond-resolution, lowest-overhead clock. Fulfils the high-precision clock API.
   * - :term:`Steady Clock`
     - Monotonic, never adjusted. Preferred for elapsed-time and timeouts. Fulfils the monotonic clock API.
   * - :term:`System Clock`
     - Wall-clock (UTC-based) OS ``CLOCK_REALTIME``, may jump or be adjusted. Used for calendar
       timestamps. Kept aligned to :term:`Absolute Time` by :term:`score::time`, so POSIX/C++
       system-clock consumers obtain the absolute time as QM data.

Logical Interface
^^^^^^^^^^^^^^^^^

.. logic_arc_int:: Local Clock
   :id: logic_arc_int__time__local_clock
   :included_by: feat__time
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__time__high_prec_clock_api[version==1], feat_req__time__monotonic_clock_api[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: now
   :id: logic_arc_int_op__time__local_now
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__time__local_clock

   Returns the current :term:`Snapshot` (a :term:`TimePoint`) of the selected local clock domain.

Absolute Time
*************

The Absolute Clock exposes an external absolute time source (e.g. UTC from GPS). Its
:term:`Absolute Time status` carries both an :term:`accuracy qualifier` and a
:term:`security qualifier`.

Logical Interface
^^^^^^^^^^^^^^^^^

.. logic_arc_int:: Absolute Clock
   :id: logic_arc_int__time__absolute_clock
   :included_by: feat__time
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__time__abs_base_api[version==1], feat_req__time__abs_acc_qual[version==1], feat_req__time__abs_sec_qual[version==1], feat_req__time__abs_sync_log[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: now
   :id: logic_arc_int_op__time__absolute_now
   :security: YES
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__time__absolute_clock

   Returns the current :term:`Snapshot` (:term:`TimePoint` with :term:`Absolute Time status`).
