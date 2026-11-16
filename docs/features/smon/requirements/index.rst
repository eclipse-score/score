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

Feature Requirements: System Monitoring
#######################################

.. document:: System Monitoring Requirements
   :id: doc__smon_requirements
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__requirements_feat[version==1]
   :tags: system_monitoring

CPU Monitoring Requirements
===========================

.. feat_req:: Overall CPU Load
   :id: feat_req__smon__overall_cpu_load
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall calculate the overall CPU load of the execution environment as a percentage.

.. feat_req:: Per-Core CPU Load
   :id: feat_req__smon__cpu_load_per_core
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall calculate the CPU load per individual core in the execution environment.

.. feat_req:: Per-Application CPU Load
   :id: feat_req__smon__cpu_load_per_application
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall calculate the CPU load per running application (process) in the execution environment.

.. feat_req:: CPU Load per Application Group
   :id: feat_req__smon__cpu_load_per_app_group
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall calculate the CPU load per configured application group.

.. feat_req:: Configurable CPU Load Threshold
   :id: feat_req__smon__cpu_load_threshold_comparison
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall compare the current overall CPU load against a configurable upper-bound threshold.

.. feat_req:: Fault Reporting on CPU Load Threshold Breach
   :id: feat_req__smon__cpu_threshold_fault_reporting
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   When the CPU load threshold is breached, the system monitor shall report a fault to the central error aggregator.

.. feat_req:: DTC Recording on CPU Load Threshold Breach
   :id: feat_req__smon__cpu_threshold_dtc_recording
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   When the CPU load threshold is breached, the system monitor shall record a Diagnostic Trouble Code (DTC) in the fault memory.

Memory Monitoring Requirements
==============================

.. feat_req:: Overall Volatile Memory Load
   :id: feat_req__smon__overall_memory_load
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall calculate the overall volatile memory load of the execution environment as a percentage.

.. feat_req:: Per-Application Volatile Memory Load
   :id: feat_req__smon__memory_load_per_application
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall calculate the volatile memory load per running application (process) in the execution environment.

.. feat_req:: Volatile Memory Load per Application Group
   :id: feat_req__smon__memory_load_per_app_group
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall calculate the volatile memory load per configured application group.

.. feat_req:: Total and Available System Memory
   :id: feat_req__smon__total_and_available_memory
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall provide the total and available system memory in bytes.

.. feat_req:: Per-Process Memory Breakdown
   :id: feat_req__smon__per_process_memory_breakdown
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall provide per-process memory usage as USS, RSS, PSS, and virtual memory size, where supported by the target OS.

Threshold & Alerting Requirements
=================================

.. feat_req:: Configurable Threshold Rules per Metric
   :id: feat_req__smon__threshold_rules_per_metric
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall support configurable threshold rules per metric type (e.g., overall CPU load, per-application memory load).

.. feat_req:: Configurable Comparison Operator
   :id: feat_req__smon__threshold_comparison_operator
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   Each threshold rule shall support a configurable comparison operator (e.g., greater than).

.. feat_req:: Configurable Threshold Actions
   :id: feat_req__smon__threshold_actions
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   Each threshold rule shall support configurable actions to execute upon breach: reporting an error, recording a DTC, or logging a warning.

.. feat_req:: Configurable Trigger Modes
   :id: feat_req__smon__threshold_trigger_modes
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   Each threshold action shall support a configurable trigger mode: fire on every breach (``Always``) or only on state change (``OnChange``).

.. feat_req:: Scoping Threshold Rules
   :id: feat_req__smon__threshold_scoping
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall support scoping a threshold rule to a specific application or application group.

Integration Interface Requirements
==================================

.. feat_req:: Error Reporting Required Interface
   :id: feat_req__smon__error_reporting_interface
   :reqtype: Interface
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall expose a required interface for error reporting to the central error aggregator, allowing platform adopters to provide their own implementation.

.. feat_req:: DTC Recording Required Interface
   :id: feat_req__smon__dtc_recording_interface
   :reqtype: Interface
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall expose a required interface for DTC recording in the fault memory, allowing platform adopters to provide their own implementation.

.. feat_req:: Log Message Publication Interface
   :id: feat_req__smon__logging_interface
   :reqtype: Interface
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall expose a required interface for log message publication, allowing platform adopters to bind their own logging backend.

Configuration Requirements
==========================

.. feat_req:: External Configuration File
   :id: feat_req__smon__external_configuration_file
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall read all configuration parameters from an external file (e.g., JSON) at startup, without requiring recompilation.

.. feat_req:: Application Group Configuration
   :id: feat_req__smon__app_group_configuration
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The configuration shall allow defining named application groups, each containing a list of monitored application identifiers.

.. feat_req:: Category-Based Logging Configuration
   :id: feat_req__smon__category_log_configuration
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The configuration shall allow enabling or disabling logging independently per metric category (e.g., overall, per-core, per-group, per-application).

.. feat_req:: Configurable Metrics Logging Interval
   :id: feat_req__smon__metrics_logging_interval
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The configuration shall allow setting the metrics logging interval in seconds.

.. feat_req:: Threshold Rules Configuration Definition
   :id: feat_req__smon__threshold_rules_configuration
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The configuration shall allow defining one or more threshold rules, each with its own metric target, threshold value, and list of actions.

General & Platform Requirements
===============================

.. feat_req:: Structured Periodic Metrics Publication
   :id: feat_req__smon__periodic_metrics_logging
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall publish structured log messages containing all collected metrics at the configured interval.

.. feat_req:: Graceful Termination Handling
   :id: feat_req__smon__graceful_shutdown
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall support graceful shutdown upon receiving a termination signal (e.g., ``SIGINT``, ``SIGTERM``).

.. feat_req:: Concurrent Metric Acquisition
   :id: feat_req__smon__concurrent_metric_acquisition
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall collect metrics from multiple sources concurrently to minimize the overall collection latency within a single monitoring cycle.

.. feat_req:: Platform Portability
   :id: feat_req__smon__platform_portability
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall be portable between Linux and QNX operating systems, with OS-specific behavior isolated behind a platform abstraction boundary.

.. feat_req:: Robustness Against Dynamic Process Lifecycles
   :id: feat_req__smon__dynamic_process_robustness
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :derived_from:
   :valid_from: v1.0.0
   :valid_until:
   :status: valid
   :version: 1
   :satisfied_by: feat__smon

   The system monitor shall be robust against processes or threads appearing or disappearing during an active monitoring scan without crashing or corrupting data.

.. needextend:: c.this_doc() and docname is not None and "system_monitoring" in id
   :+tags: system_monitoring
