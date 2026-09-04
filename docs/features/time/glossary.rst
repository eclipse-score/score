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

Time Glossary
=============

Time Feature
------------

.. glossary::
    score::time
      The Time feature. It provides applications with access to several time bases — local,
      vehicle and absolute — through a uniform :term:`Clock` interface, and owns the
      synchronization of the synchronized time bases.

Core Time Model
---------------

.. glossary::
    Clock
      A source of time. A clock produces a progressing sequence of
      :term:`TimePoint` values for a given :term:`clock domain`. All clocks are read
      through a uniform interface, independent of the underlying time base.

    Clock domain
      The kind of time a :term:`Clock` represents (e.g. :term:`Vehicle Time` or the
      :term:`Local Clock` variants). The domain is selected explicitly by the application;
      each domain has its own :term:`TimePoint` type and status concept, so time values of
      different domains are incompatible and cannot be mixed unintentionally.

    TimePoint
      A specific point in time issued by a :term:`Clock`. TimePoints of one
      :term:`clock domain` are ordered (the relations *equal* and *less than* are defined),
      so two TimePoints of the same domain can be subtracted to yield a :term:`TimeSpan`.

    TimeSpan
      A duration, i.e. the difference between two :term:`TimePoint` values of the same
      :term:`clock domain`. Supported operations include ``TimePoint - TimePoint``,
      ``TimePoint + TimeSpan``, ``TimeSpan + TimeSpan``, scaling by a factor, equality and
      comparison. Subtraction saturates to zero (negative TimeSpans are not produced).

    Snapshot
      The value returned when reading a :term:`Clock`. It bundles a :term:`TimePoint` with
      the domain-specific status concept (e.g. :term:`Vehicle Time status`, or no status for
      the local clocks), allowing a caller to read the time and judge its quality in a single
      call.

    Epoch
      The reference TimePoint at which a :term:`Clock` starts counting. The semantics of the
      epoch are a documented property of the clock (e.g. the Unix system clock epoch is
      ``1970-01-01 00:00:00 UTC``).

    Resolution
      The smallest time difference an individual :term:`TimePoint` can represent. For an
      ideal clock the resolution equals the reciprocal of the :term:`frequency`, but in
      practice it may be coarser.

    Frequency
      The rate at which a :term:`Clock` updates the :term:`TimePoint` values it issues.

    Monotonic
      Property of a :term:`Clock` whose successive TimePoints never decrease
      (``TP[n+1] >= TP[n]``). A *strictly monotonic* clock never repeats a value. The
      :term:`System Clock` is not monotonic (it may jump backward).

    Steady
      Property of a :term:`Clock` whose TimePoints advance in fixed increments of exactly
      ``1 / frequency``, without jumps or rate adjustments.

    Delay Tag
      A timestamp of an event — a datagram, frame, message, or any produced value — expressed in
      the :term:`Vehicle Time` base. Comparing a Delay Tag against a later :term:`Vehicle Time`
      yields the time elapsed since the event, for example to compensate a transmission delay.

Clocks and Clock Domains
------------------------

Naming convention: a **"… Time"** term names a :term:`clock domain` — a *time base*, i.e. the
kind of time and its properties (epoch, monotony, status concept, synchronization source). A
**"… Clock"** term names the :term:`Clock` interface that *provides* that time base to
applications (the ``now`` operation, plus initialization, availability and subscription where the
time base requires it). The local time bases keep their conventional names
(:term:`Steady Clock`, :term:`System Clock`, :term:`High-Resolution Steady Clock`) even though they are
all provided by the single :term:`Local Clock` interface.

.. glossary::
    Vehicle Time
      The :term:`clock domain` (time base) representing the vehicle-wide synchronized time,
      driven by the external :term:`Grand Master` via the :term:`gPTP`.
      Reading it yields a :term:`Snapshot` carrying a :term:`Vehicle Time status`. It is exposed
      to applications through the :term:`Vehicle Clock`.

    Vehicle Clock
      The :term:`Clock` interface that provides :term:`Vehicle Time`. Because that time base
      depends on external synchronization, the interface additionally offers initialization,
      availability checks and subscription to synchronization events, on top of reading the time.

    Local Clock
      The :term:`Clock` interface that provides the local, non-synchronized time bases —
      :term:`Steady Clock`, :term:`System Clock` and :term:`High-Resolution Steady Clock`. They need no
      initialization and are always available.

    Steady Clock
      A monotonic, non-adjustable local time base. It never goes backward, which makes it the
      standard choice for measuring elapsed time and computing timeouts.

    System Clock
      A wall-clock (UTC-based) local time base — the OS ``CLOCK_REALTIME``, also reachable through
      standard POSIX (``clock_gettime``) and C++ (``std::chrono::system_clock``) APIs. It may jump
      or be adjusted, so it is used for calendar timestamps, not for measuring elapsed time. Its
      value is kept aligned to :term:`Absolute Time` by :term:`score::time`; consumers reading it
      thus obtain the absolute time, but as QM data without the :term:`accuracy qualifier` and
      :term:`security qualifier`.

    High-Resolution Steady Clock
      A monotonic, nanosecond-resolution local time base optimized for low-overhead timing.
      Used for tight timing loops and deadline checks.

    Absolute Time
      The :term:`clock domain` (time base) representing an external absolute time source
      (e.g. UTC from GPS). Reading it yields a :term:`Snapshot` carrying an
      :term:`Absolute Time status`. It is exposed to applications through the
      :term:`Absolute Clock`. Its transmission delay is compensated using a :term:`Delay Tag`.

    Absolute Clock
      The :term:`Clock` interface that provides :term:`Absolute Time`.

Time Quality and Status
-----------------------

.. glossary::
    Vehicle Time status
      The status concept attached to a :term:`Vehicle Time` :term:`Snapshot`. It indicates
      the reliability of the time value — for example whether it is synchronized, whether a
      timeout occurred, and whether the time leaped to the future or the past — together with
      a rate-deviation measurement. It also carries the :term:`accuracy qualifier` and the
      :term:`Time point qualifier`, letting a caller decide both whether the time value is
      reliable and whether it may be treated as ASIL-B data.

    Accuracy qualifier
      An indication of how accurate a :term:`TimePoint` is, i.e. how close it is to the
      corresponding point in the reference time base. The accuracy qualifier is a property of
      the :term:`clock domain` and is reflected in the :term:`Snapshot` returned by the :term:`Clock` interface.

    Security qualifier
      An indication of the security level of a :term:`TimePoint`, i.e. whether it may be
      treated as trustworthy data or not.

    Time point qualifier
      An indication of the integrity level of a :term:`TimePoint`, i.e. whether it may be
      treated as ASIL-B data or only as QM data.

    Absolute Time status
      The status concept attached to an :term:`Absolute Time` :term:`Snapshot`. It indicates the :term:`accuracy qualifier` and
      the :term:`security qualifier` of the time value, letting a caller decide whether the value is reliable enough for its use case.

Synchronization Infrastructure
------------------------------

.. glossary::
    PTP
      Precision Time Protocol - a protocol (IEEE 1588) used to synchronize clocks in a
      network.

    gPTP
      Generalized Precision Time Protocol, the IEEE 802.1AS profile of the
      :term:`PTP` used for in-vehicle Ethernet time synchronization.

    Syntonization
      Alignment of clock *frequency* (rate) between nodes, as opposed to synchronization
      which aligns the absolute :term:`TimePoint`. Both are required for long-term timing
      consistency.

    Grand Master
      The external, network-wide time source (the PTP Grand Master) that the system
      synchronizes to using the :term:`gPTP`.
