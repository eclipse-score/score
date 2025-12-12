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

.. _stakeholder_requirements:

Stakeholder Requirements
========================

Overall goals
-------------

.. stkh_req:: Reuse of application software via managed APIs
   :id: stkh_req__overall_goals__reuse_of_app_soft
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This is a usability constraint needed for long maintenance support
   :status: valid

   The SW-platform shall enable the reuse of application software via a set of managed APIs.
   These APIs shall be developed via a well-defined life-cycle ensuring
   non-breaking changes.


.. stkh_req:: Enable cooperation via standardized APIs
    :id: stkh_req__overall_goals__enable_cooperation
    :reqtype: Non-Functional
    :security: NO
    :safety: QM
    :rationale: To enable cooperation with other cooperation partners.
    :status: valid

    The SW-platform shall where possible be based on existing standards (e.g. network protocols).

.. stkh_req:: Variant management
    :id: stkh_req__overall_goals__variant_management
    :reqtype: Functional
    :security: NO
    :safety: QM
    :rationale: tbd
    :status: valid

    The SW-platform shall provide variant management support.
    Variant management support shall enable users to ensure the
    compatibility of application software across vehicle variants and vehicle
    software releases.


.. stkh_req:: IP protection
   :id: stkh_req__overall_goals__ip_protection
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support cooperation models, where partners do not
   want to disclose their intellectual property of applications to all other
   partners.



Functional requirements
-----------------------

.. stkh_req:: File Based Configuration
   :id: stkh_req__functional_req__file_based
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: File based configuration allows changes without rebuilding the software.
   :status: valid

   The SW-platform shall support configuration of applications via files (e.g. yaml, json)

.. stkh_req:: Support of safe Key/Value store
   :id: stkh_req__functional_req__support_of_store
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Key/Value storage is a standard way to structure file based non-volatile memory access.
   :status: valid
   :tags: safety_mechanism

   The SW-platform shall provide towards the applications a safe key/value store.

   Note: This is part of 0.5 release and therefore can only support ASIL_B. Goal is ASIL_D.

.. stkh_req:: Safe Configuration
   :id: stkh_req__functional_req__safe_config
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Configuration files may hold safety relevant information.
   :status: valid
   :tags: safety_mechanism

   The SW-platform shall support safe configuration.

   Note: This is part of 0.5 release and therefore can only support ASIL_B. Goal is ASIL_D.


.. stkh_req:: Safe Computation
   :id: stkh_req__functional_req__safe_comput
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safe systems require computations to be done in safe environments.
   :status: valid

   The SW-platform shall support safe computation.

   Note: This is part of 0.5 release and therefore can only support ASIL_B. Goal is ASIL_D.


.. stkh_req:: Base Libraries
   :id: stkh_req__functional_req__base_libraries
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Common libraries reduce duplication, improve consistency and quality across components.
   :status: valid

   The SW-platform shall provide a set of base libraries offering common functionality for SW-platform components.


.. stkh_req:: Hardware Accelerated Computation
   :id: stkh_req__functional_req__hardware_comput
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: High computation loads typically need to be speed up hardware acceleration e.g. in ADAS applications
   :status: valid

   The SW-platform shall support computation accelerated by a Hardware accelerator.


.. stkh_req:: Data Persistency
   :id: stkh_req__functional_req__data_persistency
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Applications typically need to store data across power cycles.
   :status: valid

   The SW-platform shall support to store data on non-volatile memory e.g. disks, flash, etc.


.. stkh_req:: Operating System
   :id: stkh_req__functional_req__operating_system
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This allows portability of SW-platform on POSIX compliant operating systems.
   :status: valid

   The SW-platform shall support operating systems compliant with IEEE Std 1003.1 (2004 Edition or newer)

.. stkh_req:: Video subsystem
   :id: stkh_req__functional_req__video_subsystem
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall provide an interface for pre-processing and
   distribution of camera data via the following mechanisms

   * PCIe Graphic streams
   * Shared Memory Graphic streams
   * Display Serial Interface Driver
   * APIX serialization driver
   * ISP Driver including correction and frame pre-processing CV library (lens distortion et. al.)
   * Sensor Streamer component (binding ISP Driver & pre-processing CV library)


.. stkh_req:: Compute subsystem
   :id: stkh_req__functional_req__comp_subsystem
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall provide the following frameworks towards the
   applications:

   * Math library: Eigen Blaze like safety enhanced math front-end library
   * Graphics and compute API: Vulkan GPU back-end and CPU (SIMD capable)-based compute libraries:

     * Deep Neural Network API:  (including pytorch, tensorflow conversion scripts)
     * Computer Vision API: e.g. like OpenCV
     * Linear algebra API: e.g. BLAS / Lapack
     * AVB Sensor streams
     * PCIe Sensor streams
     * Shared Memory Sensor streams
     * GSML serialized data

.. stkh_req:: Communication with external MCUs/standby controllers
   :id: stkh_req__functional_req__comm_with_control
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall define protocols and concepts for the interaction with
   external micro-controllers for

   * board management
   * external supervision for safety and security functions
   * software update
   * debugging
   * feature activation


Dependability
-------------

.. stkh_req:: Automotive Safety Integrity Level
   :id: stkh_req__dependability__automotive_safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: The SW-platform shall be usable by safety relevant applications.
   :status: valid

   The SW-platform shall support applications with an automotive safety
   integrity level up to ASIL-B.

   Note: This is part of 0.5 release and therefore can only support ASIL_B. Goal is ASIL_D.


.. stkh_req:: Safety features
   :id: stkh_req__dependability__safety_features
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: There are state-of-the-art safety mechanisms to check HW and SW errors. These are expected to be supported either by the SW-platform alone or by using HW or OS provided safety features.
   :status: valid
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support the following safety feature:

   * Health Management (alive, deadline, logical supervision) for time and event based taskchains
   * E2E Protection for communication
   * Built-in hardware self-tests
   * Safe reset paths
   * IO MMU protecting DMA accesses
   * Memory Management Unit
   * Memory Protection Unit for caches
   * ECC Memory
   * Software Lockstep
   * Power management integrated circuit (PMIC), external watchdog and voltage monitoring
   * Safe switch from engineering to field mode and back


.. stkh_req:: SW-platform error reaction
   :id: stkh_req__dependability__error_reaction
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety relies on error reporting, e.g. to preserve a safe system state.
   :status: valid
   :tags: safety_mechanism

   The SW-platform shall react in the following way on errors:

   - report the error (incl. details if available) to the calling user function

   Note: See also :need:`stkh_req__dependability__safe_state`


.. stkh_req:: Safe SW-platform state
   :id: stkh_req__dependability__safe_state
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: A safe state definition is a common expectation of safety integrity standards.
   :status: valid
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall react in the following way on errors:

   - in case of an unrecoverable error (e.g. access violations), report the error to the external health monitor

   Note1: Together with :need:`stkh_req__dependability__error_reaction` the "safe state" of the SW-platform can be described as "error reported".

   Note2: The implementation of the reporting of an unrecoverable error must take into account that after such an error
   the functions of the SW-platform may be corrupted (solution for this may be a cyclic triggering of an external watchdog in the healthy case
   and stopping the triggering in the error case).


.. stkh_req:: Error report timing
   :id: stkh_req__dependability__error_report_timing
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: It is assumed that there is a need to know how much time is allowed between the ocurrence of an error and the reporting, so we define a feasible time span.
   :status: valid
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall react on errors (as described in :need:`stkh_req__dependability__safe_state` and :need:`stkh_req__dependability__error_reaction`) within 1 millisecond. If this is not feasible a special component AoU needs to be defined.

   Note1: The time span mentioned is the SW reaction time and not the time between the error happening and the reporting.
   For example if there is a alive supervision configured with 10ms cycle time and 5ms allowed delay,
   the error could happen in the first millisecond but will be reported earliest after 10+5ms plus the SW reaction time.

   Note2: If a user application calls a SW-platform function the (error) return is required latest after the reaction time, so there could be a timeout used by the application considering this.


.. stkh_req:: No mixed ASIL
   :id: stkh_req__dependability__no_mixed_asil
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: It is assumed that POSIX processes as implemented by the OS provide isolation from memory and timing errors of other processes but not within.
   :status: valid

   The SW-platform safety components running in one POSIX process shall implement the highest ASIL of their assigned functional requirements.


.. stkh_req:: Program Flow Monitoring
   :id: stkh_req__dependability__flow_monitoring
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: Not all POSIX operating systems provide protection of POSIX processes from timing errors (e.g. delayed execution, deadlocks)
   :status: valid
   :valid_from: v1.0.0

   The SW-platform safety components shall use program flow monitoring to detect run time errors or explain in their safety concept why they do not need this.

   Note1: Reasons for not needing program flow monitoring could be an OS scheduler with timing and execution guarantees.
   Or that the non/late execution of the application keeps the system in a safe state.

   Note2: The SW-Platform supports this - see :need:`stkh_req__dependability__safety_features` "live, deadline, logical supervision"


.. stkh_req:: Availability
   :id: stkh_req__dependability__availability
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support the development of highly available systems.
   (see also `Availability <https://en.wikipedia.org/wiki/Availability>`_).


.. stkh_req:: Security features
   :id: stkh_req__dependability__security_features
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support the following security features:

   * Mandatory access control
   * Secure boot
   * Secure onboard communication
   * IPSec and MACSec
   * Firewall
   * Certificate installation and storage in HSM or ARM trustzone.
   * Kernel hardening (ASLR, Pointer obfuscation …) in libc and compiler
   * Identity and Access Management
   * Secure Feature Activation
   * Secure software update


Application architectures
-------------------------

In modern software systems, the architectural design plays a critical role in determining how components interact, how they process
data, and how they manage workloads. Each architectural pattern is tailored to address specific challenges in terms of execution
model, resource consumption, communication strategy, and discovery. The three major architectures that we'll focus on — **Time-based
(Deterministic, Polling-based)**, **Data-driven (Event-driven, High-throughput)**, and **Request-driven (Asynchronous, Sporadic
interaction)** — each emphasize different operational priorities.

1. **Time-based Architecture (Deterministic, Polling-based):** Time-based architecture operates by triggering actions
   at fixed intervals, using scheduled polling to ensure consistent, predictable behavior. This architecture ensures
   high availability and deterministic execution, meaning that actions always happen at a predefined time, making it
   ideal for systems that require reliability. However, it can lead to inefficient CPU usage, as the system continues
   to poll even when no new data is available. The communication is synchronous and unidirectional, with the system
   staying up-to-date by polling for new information. Discovery is data-centric, meaning that the application focuses
   only on the data being communicated and not on the identity of the data source.

2. **Data-driven Architecture (Event-driven, High-throughput):** In a data-driven architecture, actions are triggered
   by events or data changes. The system optimizes for high throughput and performance, making it well-suited for
   applications where responsiveness to data is critical. The execution is non-deterministic, meaning that timing
   depends on when data arrives, which can lead to unpredictable bottlenecks, especially during data surges. The
   communication is unidirectional and driven by updates to data, decoupling the producers and consumers of the data.
   Discovery is data-centric, as applications react to events regardless of their origin, optimizing for low latency
   and dynamic scalability.

3. **Request-driven Architecture (Asynchronous, Sporadic interaction):** A request-driven architecture is triggered
   only when a request is made, making it ideal for applications that handle sporadic, unpredictable workloads. The
   system remains idle during inactivity, saving resources until a task is triggered. This model does not provide
   deterministic behavior, and response times depend on when requests arrive. Communication is bi-directional, with
   requests and responses flowing between client and server. Discovery is service-instance-centric, requiring knowledge
   of specific server instances, especially for stateful systems where session continuity or state preservation is
   crucial.


.. stkh_req:: Support for Time-based Architectures
   :id: stkh_req__app_architectures__support_time
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: tbd - potentially above explanation
   :status: valid
   :tags: safety_mechanism

   The SW-platform shall support a deterministic, time-based application execution model that triggers logic based on predefined schedules or
   polling intervals.


.. stkh_req:: Support for Data-driven Architecture
   :id: stkh_req__app_architectures__support_data
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd - potentially above explanation
   :status: valid

   The SW-platform shall support an event-driven, high-throughput application architecture where execution is triggered by data changes.

.. stkh_req:: Support for Request-driven Architecture
   :id: stkh_req__app_architectures__support_request
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd - potentially above explanation
   :status: valid

   The SW-platform shall support a request-driven, asynchronous application architecture that processes requests on-demand.



Execution model
---------------

.. stkh_req:: Processes and thread management
   :id: stkh_req__execution_model__processes
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support the following scheduling strategies:

   * Process Management

     * Startup and Shutdown of processes
     * Recovery
     * Machine State Management (modelled via simple JSON file)

   * Cross-process synchronization of threads (Activities)

     * Event activated multi-process taskchains
     * Time-sliced activated multi-process taskchains
     * memory management (via PMR),
     * signal handling, error handling (FPU Exceptions, other traps …)

.. stkh_req:: Short application cycles
   :id: stkh_req__execution_model__short_app_cycles
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support cycle times of less then 5 ms on application level
   if this is supported by the underlying hardware.

.. stkh_req:: Realtime capabilities
   :id: stkh_req__execution_model__realtime_cap
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support the controlled reaction on events
   (timing events, interrupts) within a defined timing interval.

.. stkh_req:: Startup performance
   :id: stkh_req__execution_model__startup_perf
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support fast startup scenarios e.g. cold boot and
   resume from hibernate mode.

.. stkh_req:: Low power mode
   :id: stkh_req__execution_model__low_power
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support low power modes to safe energy.

Communication
-------------

.. stkh_req:: Inter-process Communication
   :id: stkh_req__communication__inter_process
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Application software typically consists of multiple processes which need to interact.
   :status: valid

   The SW-platform shall support inter-process communication.

.. stkh_req:: ABI Compatible Data Types
   :id: stkh_req__communication__abi_compatible
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: ABI compatiblity ensures that the same memory location is correctly interpreted by different programming languages.
   :status: valid

   The SW-platform shall support ABI compatible data types for zero-copy communication between Rust and C++ applications.

.. stkh_req:: Intra-process Communication
   :id: stkh_req__communication__intra_process
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Application software typically maps software building blocks into the same process.
   :status: valid

   The SW-platform shall support intra-process communication.

.. stkh_req:: Stable application interfaces
   :id: stkh_req__communication__stable_app_inter
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: In case of incompatible changes on external interface the portability effort shall be reduced.
   :status: valid

   The SW-platform shall provide a framework to mitigate incompatible changes on
   external interfaces to keep application interfaces stable.

.. stkh_req:: Extensible External Communication
   :id: stkh_req__communication__extensible_external
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: ECUs need to interact with each other. There are multiple protocols today and more to come in the future.
   :status: valid

   The SW-platform shall support external communication via well established protocols e.g. Zenoh, DDS.


.. stkh_req:: Safe Communication
   :id: stkh_req__communication__safe
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Distributed safe systems often require communication to be safe.
   :status: valid
   :tags: safety_mechanism

   The SW-platform shall support safe communication.

   Note: This is part of 0.5 release and therefore can only support ASIL_B. Goal is ASIL_D.


.. stkh_req:: Secure Communication
   :id: stkh_req__communication__secure
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Distributed secure systems often require secure communication.
   :status: valid

   The SW-platform shall support secure communication.

.. stkh_req:: Supported network protocols
   :id: stkh_req__communication__supported_net
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support the following automotive network
   protocols

   * SOME/IP
   * DDS
   * UWB including Driver for UWB Peripheral
   * SPI (+ CSC ADI & Texas Instruments chipset support)
   * Vehicle to Grid + ISO Charge protocols
   * AVB


.. stkh_req:: Quality of service
   :id: stkh_req__communication__service_quality
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall provide a framework to ensure quality of service
   of applications deployed on the SW-platform. This includes but is not limited
   to:

   * QOS for applications
   * Controlled latency for communication and scheduling
   * Guaranteed network and compute quotas


.. stkh_req:: Automotive diagnostics
   :id: stkh_req__communication__auto_diagnostics
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support the following diagnostic protocols
   * SOVD (ISO 17978)
   * UDS (ISO 14229) Diagnostics
   * Diagnostic trouble codes
   * Diagnostic jobs

Time
----

.. stkh_req:: Vehicle Time base Synchronization
   :id: stkh_req__time__vehicle_time_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Enables the system to compare events chronologically.
   :status: valid

   The SW-platform shall provide a time synchronization framework to synchronize its clock
   to Time Master within the vehicle.

.. stkh_req:: Vehicle Time base API
   :id: stkh_req__time__vehicle_time_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Enables an application to correlate its data with a vehicle-internal time reference for event timestamp and chronological events comparison.
   :status: valid

   The SW-platform shall provide access to synchronized vehicle time.

.. stkh_req:: Synchronize the HW clock with Vehicle Time
   :id: stkh_req__time__hw_clock_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Enables the system to compare events from different ECUs chronologically, using the same time base for timestamping ingress and egress frames.
   :status: valid

   The SW-platform shall synchronize the local HW clock to vehicle time.

.. stkh_req:: Time Synchronization with external sources
   :id: stkh_req__time__absolute_time_sync
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables the system to validate a certificate or token with temporal validity conditions, adding a UTC-timestamp to a data set.
   :status: valid

   The SW-platform shall provide a framework to synchronize the clock to external-to-vehicle absolute time base (UTC).

.. stkh_req:: Absolute time base API
   :id: stkh_req__time__absolute_time_api
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables an application to correlate its data with an absolute vehicle-external time reference for event timestamping and chronological events comparison.
   :status: valid

   The SW-platform shall provide access to the absolute time base, synchronized with external time sources.

.. stkh_req:: Local High precision Clock API
   :id: stkh_req__time__high_precision_clock_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Enables an application to get the current system time, which is essential for time-sensitive operations and event scheduling, via common, mockable and standardized API.
   :status: valid

   The SW-platform shall provide access to the current high precision clock from the system time provider in nanoseconds.

   Note: to which clock the high precision clock is mapped, depends on the system design.

.. stkh_req:: Local Monotonic Clock API
   :id: stkh_req__time__monotonic_clock_api
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Enables an application to get the current system time, which is essential for time-sensitive operations and event scheduling, via common, mockable and standardized API.
   :status: valid

   The SW-platform shall provide access to the current monotonic clock from the system time provider.

   Note: to which clock the monotonic clock is mapped, depends on the system design.

AI SW-platform
--------------


.. stkh_req:: On-board ML Workloads
   :id: stkh_req__ai_platform__enablement
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Modern vehicles require the integration of ML capabilities to remain competitive and support customer expectations.
   :status: valid
   :tags: artificial_intelligence

   The SW-platform shall support the execution of traditional ML workloads on-board.


.. stkh_req:: Support for Safety-Critical ML
   :id: stkh_req__ai_platform__safety_critical
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Some ML-based functionality is required to be certified up to ASIL-B.
   :status: valid
   :tags: artificial_intelligence

   The SW-platform shall support safety-compliant (ASIL-B) deployment of AI/ML components, including inference backends and pipelines.


.. stkh_req:: Runtime Efficiency for Edge Devices
   :id: stkh_req__ai_platform__runtime_efficiency
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Automotive platforms have limited compute and thermal budgets.
   :status: valid
   :tags: artificial_intelligence

   The SW-platform shall be optimized for runtime performance and memory footprint on embedded hardware targets.


.. stkh_req:: Platform Portability (QNX + Linux)
   :id: stkh_req__ai_platform__platform_portability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: AI/ML use cases span both safety and non-safety environments, requiring portability across operating systems.
   :status: valid
   :tags: artificial_intelligence

   The SW-platform shall support both QNX (for safety) and Linux (for GenAI and flexibility) with reusable components.


.. stkh_req:: Secure Model Execution
   :id: stkh_req__ai_platform__model_security
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: AI model execution must be protected against tampering or abuse.
   :status: valid
   :tags: artificial_intelligence

   The SW-platform shall ensure secure, verified, and integrity-checked model execution.


.. stkh_req:: Deterministic Execution Paths
   :id: stkh_req__ai_platform__runtime_determinism
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety certification requires predictable and bounded system behavior.
   :status: valid
   :tags: safety_mechanism, artificial_intelligence

   The SW-platform shall ensure deterministic behavior for AI components used in safety-relevant paths.


.. stkh_req:: On-board GenAI Workloads
   :id: stkh_req__gen_ai__enablement
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Modern vehicles require the integration of AI/ML capabilities to remain competitive and support customer expectations.
   :status: valid
   :tags: artificial_intelligence

   The SW-platform shall support the execution of Generative AI workloads on-board.


.. stkh_req:: GenAI User Interaction
   :id: stkh_req__gen_ai__interaction
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: HMIs are expected to support intelligent, natural interaction using LLM-based assistants.
   :status: valid
   :tags: artificial_intelligence

   The SW-platform shall support on-device GenAI-based models with user interaction.


.. stkh_req:: Action Safety and Governance
   :id: stkh_req__gen_ai__safety_filter
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: GenAI output may be unpredictable or unsafe and must be controlled before affecting vehicle behavior.
   :status: valid
   :tags: safety_mechanism, artificial_intelligence

   The SW-platform shall validate all actions proposed by GenAI models against safety and policy rules prior to execution.


.. stkh_req:: Seamless Integration with Vehicle Systems
   :id: stkh_req__gen_ai__vehicle_com
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: AI components must interact with vehicle state and control interfaces.
   :status: valid
   :tags: artificial_intelligence

   The SW-platform shall expose structured APIs to access vehicle state and execute safe commands.


Diagnostics and Fault Management
--------------------------------

.. stkh_req:: Diagnostic via SOVD
   :id: stkh_req__diagnostics__via_sovd
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables modern, scalable diagnostics using a standard REST-based protocol to improve integration, interoperability, and maintainability.
   :status: valid

   The SW-platform shall support vehicle diagnostics via the SOVD protocol as defined in ISO 17978, to allow scalable and secure diagnostic access.

.. stkh_req:: Fault Reporting Infrastructure
   :id: stkh_req__diagnostics__fault_reporting
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables applications and components to report faults in a structured, reusable, and system-wide accessible manner.
   :status: valid

   The SW-platform shall support a reusable fault reporting infrastructure that enables applications and SW-platform components to report, persist, and manage diagnostic fault information.

.. stkh_req:: Readout DTCs via SOVD
   :id: stkh_req__diagnostics__dtc_read_sovd
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables reading of Diagnostic Trouble Codes (DTCs) from the ECU for various use-cases like production or maintenance.
   :status: valid

   The SW-platform shall provide users the ability to retrieve current Diagnostic Trouble Codes (DTCs) from the ECU via the SOVD protocol.

.. stkh_req:: Extensibility of Diagnostic Services
   :id: stkh_req__diagnostics__custom_services
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables OEMs and developers to implement system-specific or project-specific routines for diagnostic control and testing.
   :status: valid

   The SW-platform shall support extensibility mechanisms that allow integration of custom diagnostic services and routines via the SOVD interface.

.. stkh_req:: Compatibility with UDS Testers
   :id: stkh_req__diagnostics__uds_tester_compat
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Ensures continued usability of existing test infrastructure, avoiding costly replacement of legacy tools and ensuring fulfillment of legal requirements.
   :status: valid

   The SW-platform shall provide compatibility with UDS-based testers by offering a proxy to translate UDS requests into SOVD-compatible actions.

.. stkh_req:: Compatibility with UDS ECUs
   :id: stkh_req__diagnostics__uds_ecus
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Ensures continued operability of ECUs that are not SOVD-capable.
   :status: valid

   The SW-platform shall support integration with ECUs that use UDS by providing a compatibility adapter to translate SOVD requests to UDS commands.

.. stkh_req:: Support for Distributed and Multi-ECU Diagnostics
   :id: stkh_req__diagnostics__distributed_support
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables the system to operate in modern, distributed vehicle architectures where diagnostics span multiple ECUs and subsystems.
   :status: valid

   The SW-platform shall support distributed diagnostics across multiple ECUs and network segments, enabling routing and aggregation of diagnostic data.

.. stkh_req:: Secure Access to Diagnostic Interfaces
   :id: stkh_req__diagnostics__secure_access
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Diagnostic access allows deep system introspection and manipulation, which must be protected against unauthorized use.
   :status: valid

   The SW-platform shall enforce secure access control for all diagnostic interfaces, including authentication, encryption, and role-based access enforcement.


Hardware support
----------------

.. stkh_req:: Chipset support for ARM64 and x64
   :id: stkh_req__hardware_support__chipset_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support arm64 and x64 architectures.


.. stkh_req:: Virtualization support for debug and testing
   :id: stkh_req__hardware_support__debug_and_test
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall run on qemu to enable test and debug in virtualized
   environments.


.. stkh_req:: Support of container technologies
   :id: stkh_req__hardware_support__container_tech
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support deployment of self-contained application
   bundles

   * Kernel Features: e.g. cgroup, secpol, namespaces as precondition for containerization
   * e.g. SOAFFEE Like realtime capable containers: https://www.soafee.io/



Developer experience
--------------------

.. stkh_req:: IDL Support
   :id: stkh_req__dev_experience__idl_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall provide a human readable interface definition language
   with decentralized glue code generation.


.. stkh_req:: Developer experience and development toolchain
   :id: stkh_req__dev_experience__dev_toolchain
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support a state-of-the art developer experience for
   functional development and application development.

   Features:

   * IDE support for all supported languages.
   * IDL Editor with syntax highlighting.
   * Connection to qemu and real target via SSH.
   * Support of continuous integration and deployment systems.


.. stkh_req:: Performance analysis
   :id: stkh_req__dev_experience__perf_analysis
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support performance analysis of SW-platform and
   application software:

   * Flame-graph visualization for long termed CPU behavior
   * RAM usage statistics for long-term Memory behavior

.. stkh_req:: Tracing of execution
   :id: stkh_req__dev_experience__tracing_of_exec
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support the tracing of events (start, stop) of executable
   entities and kernel threads on all computation units e.g.

   * CPU
   * GPU
   * Neural Network Processors
   * Image Processors
   * etc.

.. stkh_req:: Tracing of communication
   :id: stkh_req__dev_experience__tracing_of_comm
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: tbd
   :status: valid

   The SW-platform shall support the tracing of communication events for internal
   and external communication systems.

.. stkh_req:: Tracing of memory access
   :id: stkh_req__dev_experience__tracing_of_memory
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support the tracing of memory events (allocation, copy,
   de-allocation) for different types of memory e.g.

   * CPU Memory
   * GPU Memory

.. stkh_req:: Timing analysis
   :id: stkh_req__dev_experience__timing_analysis
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support observation, assessment of
   timing requirements with state-of-the-art analysis tools.

.. stkh_req:: Debugging
   :id: stkh_req__dev_experience__debugging
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall provide a method and interface to enable
   debugging of the software on target and in vehicle.

.. stkh_req:: Mockup implementation for application testing
   :id: stkh_req__dev_experience__mockup_public_apis
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Enables unit, component and integration testing for both SW-platform related and non-platform related applications.
   :status: valid

   The SW-platform shall provide support for mocking its public interfaces,
   enabling unit, component and integration testing of applications.

.. stkh_req:: Programming languages for application development
   :id: stkh_req__dev_experience__prog_languages
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support implementation of applications in the following
   programming languages up to the highest ASIL level as defined in :need:`stkh_req__dependability__automotive_safety`:

   * C
   * C++
   * Rust


.. stkh_req:: Reprocessing and simulation support
   :id: stkh_req__dev_experience__reprocessing
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support data-collection and injection of reprocessed data.


.. stkh_req:: Logging support
   :id: stkh_req__dev_experience__logging_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support the following logging setups:

   * Logging to external disk via mounted filesystem on top of PCIe driver
   * Logging via second dedicated Ethernet Channel
   * Logging/sensor data Gathering via Cloud native filesystem on top of second Ethernet Channel
   * Gathering of raw sensor data e.g. video streams
   * Diagnostic Log and Trace / Logcat format is supported
   * Logging of early startup events

.. stkh_req:: Previous boot logging
   :id: stkh_req__dev_experience__boot_logging
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The SW-platform shall support logging of data to memory which survives a reboot
   cycle.



Integration
-----------

.. stkh_req:: Multirepo integration
   :id: stkh_req__integration__multi_repo
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Allow independent development of software modules
   :status: valid

   The SW-platform infrastructure shall support integration of multiple repositories in a unified workflow.


Quality
-------

.. stkh_req:: Document assumptions and design decisions
   :id: stkh_req__quality__assumptions_and_dd
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This is a usability constraint needed for long term maintenance support
   :status: valid

   Contributors shall specify all assumptions and design decisions as requirements which are agreed within the S-CORE community.


Requirements Engineering
------------------------

.. stkh_req:: Requirements traceability
   :id: stkh_req__re_requirements__traceability
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: This is a usability constraint needed for long term maintenance support
   :status: valid

   he SW-platform infrastructure shall support linking all requirements from lower to upper level, whereby on the top-level are the stakeholder requirements.

.. stkh_req:: Document requirements as code
   :id: stkh_req__requirements__as_code
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: In this project no external tool or service is used. Therefore as-code is the selected option.
   :status: valid

   The SW-platform infrastructure shall support documenting all requirements as code (Docs-as-code).

Safety Mechanisms
-----------------

The following stakeholder requirements are assumed to be fulfilled by a safety mechanism due to complexity of the realizing
SW element(s) or due to dependency on HW. This is confirmed during safety analysis of the derived feature requirements and architecture.

.. needtable:: Expected Safety Mechanisms
   :filter: "safety_mechanism" in tags and type == "stkh_req" and is_external == False
   :style: table
   :columns: title; id; tags
   :colwidths: 30,30,30
