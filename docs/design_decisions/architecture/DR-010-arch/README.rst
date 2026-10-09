.. _feature_system_monitoring:

#########################################
Feature Request: System Monitoring (SMon)
#########################################

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **Feature ID**
     - SCORE-SMON
   * - **Requested by**
     - Valeo
   * - **Domain**
     - Platform Services / Health Monitoring
   * - **Status**
     - Proposed
   * - **Target Platforms**
     - Linux, QNX

.. contents:: Table of Contents
   :depth: 3
   :local:

----

**********************************
1. Motivation & Problem Statement
**********************************

Modern automotive Domain Controller ECUs run dozens of concurrent applications — navigation stacks,
ADAS pipelines, infotainment services, and communication middleware — all sharing a single hardware
platform. Without a dedicated, standardized system monitoring layer at the middleware level, the
following problems arise:

* **Silent resource exhaustion:** A misbehaving application can consume excessive CPU or memory
  without any system-level detection, leading to degraded performance or safety-critical failures
  with no traceable fault record.

* **No standardized fault reporting path:** Individual application teams implement ad-hoc watchdog
  logic, making it impossible to consolidate health data into a unified error aggregator or fault
  memory (DTC store) in a consistent and maintainable way.

* **Platform fragmentation:** Monitoring utilities written for one OS (e.g., Linux) are not
  portable to another (e.g., QNX), creating duplicated effort and inconsistent monitoring behavior
  across ECU variants within the same vehicle program.

* **Lack of application-group awareness:** OEM system integrators need to monitor the health of
  **logical groups** of applications (e.g., "ADAS stack", "Infotainment cluster") as a unit, not
  just individual processes in isolation.

* **No configurable threshold-based alerting:** There is no standard mechanism to define
  upper-bound thresholds per metric and automatically trigger graduated responses
  (warn → report error → record DTC) when those thresholds are breached.

.. note::
   S-CORE currently provides no standardized middleware component that addresses periodic,
   system-level health monitoring with configurable thresholds, fault reporting integration,
   and cross-platform portability for automotive ECUs.

----

*******************
2. Goals & Scope
*******************

2.1 Goals
=========

The System Monitor (SMon) feature shall:

#. Provide a **standardized, reusable middleware component** for periodic CPU and memory health
   monitoring on automotive ECUs.
#. Enable **configurable threshold-based alerting** that integrates with the platform's error
   aggregator and fault memory.
#. Support **logical grouping of applications** for aggregate health monitoring, as required by
   OEM integration scenarios.
#. Be **portable across Linux and QNX** operating systems without requiring changes to the
   monitoring logic.
#. Expose **well-defined integration interfaces** for error reporting, DTC recording, and logging,
   so that platform adopters can bind their own backend implementations.
#. Be **fully configurable at runtime** via an external configuration file, without requiring
   recompilation.

2.2 Out of Scope
================

The following items are explicitly **out of scope** for this feature request:

* Network I/O, Disk I/O, or GPU monitoring (identified as future extensions)
* A graphical dashboard or visualization frontend
* AUTOSAR Classic (Adaptive Platform scope only)
* Functional Safety (FuSa) certification artifacts (may be addressed in a follow-up)

----

************************
3. Needs & Requirements
************************

3.1 CPU Monitoring Needs
========================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Req. ID
     - Need Description
   * - SMON-CPU-001
     - The system monitor shall calculate the **overall CPU load** of the execution environment
       as a percentage.
   * - SMON-CPU-002
     - The system monitor shall calculate the **CPU load per individual core** in the execution
       environment.
   * - SMON-CPU-003
     - The system monitor shall calculate the **CPU load per running application** (process) in
       the execution environment.
   * - SMON-CPU-004
     - The system monitor shall calculate the **CPU load per configured application group**.
   * - SMON-CPU-005
     - The system monitor shall compare the current overall CPU load against a **configurable
       upper-bound threshold**.
   * - SMON-CPU-006
     - When the CPU load threshold is breached, the system monitor shall **report a fault to the
       central error aggregator**.
   * - SMON-CPU-007
     - When the CPU load threshold is breached, the system monitor shall **record a Diagnostic
       Trouble Code (DTC)** in the fault memory.

3.2 Memory Monitoring Needs
============================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Req. ID
     - Need Description
   * - SMON-MEM-001
     - The system monitor shall calculate the **overall volatile memory load** of the execution
       environment as a percentage.
   * - SMON-MEM-002
     - The system monitor shall calculate the **volatile memory load per running application**
       (process) in the execution environment.
   * - SMON-MEM-003
     - The system monitor shall calculate the **volatile memory load per configured application
       group**.

3.3 Threshold & Alerting Needs
================================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Req. ID
     - Need Description
   * - SMON-THR-001
     - The system monitor shall support **configurable threshold rules** per metric type
       (e.g., overall CPU load, per-application memory load).
   * - SMON-THR-002
     - Each threshold rule shall support a **configurable comparison operator**
       (e.g., greater than).
   * - SMON-THR-003
     - Each threshold rule shall support **configurable actions** to execute upon breach:
       reporting an error, recording a DTC, or logging a warning.
   * - SMON-THR-004
     - Each threshold action shall support a **configurable trigger mode**: fire on every
       breach (``Always``) or only on state change (``OnChange``).
   * - SMON-THR-005
     - The system monitor shall support **scoping a threshold rule** to a specific application
       or application group (not only system-wide metrics).

3.4 Integration Interface Needs
=================================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Req. ID
     - Need Description
   * - SMON-INT-001
     - The system monitor shall expose a **required interface for error reporting** to the
       central error aggregator, allowing platform adopters to provide their own implementation.
   * - SMON-INT-002
     - The system monitor shall expose a **required interface for DTC recording** in the fault
       memory, allowing platform adopters to provide their own implementation.
   * - SMON-INT-003
     - The system monitor shall expose a **required interface for log message publication**,
       allowing platform adopters to bind their own logging backend.

3.5 Configuration Needs
========================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Req. ID
     - Need Description
   * - SMON-CFG-001
     - The system monitor shall read **all configuration parameters from an external file**
       (e.g., JSON) at startup, without requiring recompilation.
   * - SMON-CFG-002
     - The configuration shall allow defining **named application groups**, each containing a
       list of monitored application identifiers.
   * - SMON-CFG-003
     - The configuration shall allow **enabling or disabling logging** independently per metric
       category (e.g., overall, per-core, per-group, per-application).
   * - SMON-CFG-004
     - The configuration shall allow setting the **metrics logging interval** (in seconds).
   * - SMON-CFG-005
     - The configuration shall allow defining **one or more threshold rules**, each with its own
       metric target, threshold value, and list of actions.

3.6 General & Platform Needs
==============================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Req. ID
     - Need Description
   * - SMON-GEN-001
     - The system monitor shall **publish structured log messages** containing all collected
       metrics at the configured interval.
   * - SMON-GEN-002
     - The system monitor shall support **graceful shutdown** upon receiving a termination
       signal (e.g., ``SIGINT``, ``SIGTERM``).
   * - SMON-GEN-003
     - The system monitor shall **collect metrics from multiple sources concurrently** to
       minimize the overall collection latency within a single monitoring cycle.
   * - SMON-GEN-004
     - The system monitor shall be **portable between Linux and QNX** operating systems, with
       OS-specific behavior isolated behind a platform abstraction boundary.
   * - SMON-GEN-005
     - The system monitor shall be **robust against processes or threads appearing or
       disappearing** during an active monitoring scan (i.e., no crash or data corruption due
       to process lifecycle events).

----

***********************
4. Integration Context
***********************

The SMon component sits between the **OS runtime** (from which it reads raw metrics) and three
**platform-provided services** to which it reports:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - External Service
     - Role
   * - **Central Error Aggregator**
     - Receives fault notifications when configured thresholds are breached.
   * - **Fault Memory (DTC Store)**
     - Receives DTC records for persistent fault logging.
   * - **Logging Backend**
     - Receives structured metric snapshots and threshold warning messages.

.. important::
   These three integration points are **required interfaces** that must be fulfilled by the
   platform adopter. SMon does not mandate a specific implementation of any of them.

.. figure:: assets/context_diagram.png
   :alt: SMon Integration Context Diagram
   :align: center

   *Figure 1 — High-level functional context of the SMon component within the ECU software stack.*

----

*********************************
5. Anticipated Future Extensions
*********************************

The following needs are **not in scope** for this initial feature request but are identified as
natural extensions of the proposed monitoring framework:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Future Need
     - Description
   * - **Additional metric sources**
     - Network I/O (e.g., SOME/IP, DDS traffic), Disk I/O, GPU utilization — extending the
       same monitoring framework via the existing source abstraction.
   * - **Threshold hysteresis**
     - Preventing alert "flapping" by requiring sustained threshold breaches over N consecutive
       cycles before triggering, and a separate lower watermark for clearing.
   * - **Live telemetry streaming**
     - Streaming real-time metrics over a network transport to external visualization tools or
       IDE dashboards.
   * - **Cross-platform unit test coverage**
     - Enabling platform-specific monitor logic to be verified on a Linux development host via
       OS-call mocking, without requiring access to a QNX target.