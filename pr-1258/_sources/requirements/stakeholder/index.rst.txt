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

   The platform shall enable the reuse of application software via a set of managed APIs.
   These APIs shall be developed via a well-defined life-cycle ensuring
   non-breaking changes.


.. stkh_req:: Enable cooperation via standardized APIs
    :id: stkh_req__overall_goals__enable_cooperation
    :reqtype: Non-Functional
    :security: NO
    :safety: QM
    :rationale: To enable cooperation with other cooperation partners.
    :status: valid

    The software platform shall where possible be based on existing standards (e.g. network protocols).

.. stkh_req:: Variant management
    :id: stkh_req__overall_goals__variant_management
    :reqtype: Functional
    :security: NO
    :safety: QM
    :rationale: tbd
    :status: valid

    The software platform shall provide variant management support.
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

   The software platform shall support cooperation models, where partners do not
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

   The platform shall support configuration of applications via files (e.g. yaml, json)

.. stkh_req:: Support of safe Key/Value store
   :id: stkh_req__functiona_req__support_of_store
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Key/Value storage is a standard way to structure file based non-volatile memory access.
   :status: valid

   The software platform shall provide towards the applications a safe
   (ISO26262-2018) key/value store.

   Note: This is part of 0.1 release and therefore can only support ASIL_B. Goal is ASIL_D.

.. stkh_req:: Safe Configuration
   :id: stkh_req__functional_req__safe_config
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Configuration files may hold safety relevant information.
   :status: valid

   The platform shall support safe configuration.
   Note: This is part of 0.1 release and therefore can only support ASIL_B. Goal is ASIL_D.


.. stkh_req:: Safe Computation
   :id: stkh_req__functional_req__safe_comput
   :reqtype: Functional
   :security: NO
   :safety: ASIL_D
   :rationale: Safe systems require computations to be done in safe environments.
   :status: valid

   The platform shall support safe computation.


.. stkh_req:: Hardware Accelerated Computation
   :id: stkh_req__functional_req__hardware_comput
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: High computation loads typically need to be speed up hardware acceleration e.g. in ADAS applications
   :status: valid

   The platform shall support computation accelerated by a Hardware accelerator.


.. stkh_req:: Data Persistency
   :id: stkh_req__functional_req__data_persistency
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Applications typically need to store data across power cycles.
   :status: valid

   The platform shall support to store data on non-volatile memory e.g. disks, flash, etc.


.. stkh_req:: Operating System
   :id: stkh_req__functional_req__operating_system
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This allows portability of platform on POSIX compliant operating systems.
   :status: valid

   The platform shall support operating systems compliant with IEEE Std 1003.1 (2004 Edition or newer)

.. stkh_req:: Video subsystem
   :id: stkh_req__functional_req__video_subsystem
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The software platform shall provide an interface for pre-processing and
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

   The compute subsystem shall provide the following frameworks towards the
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

   The software platform shall define protocols and concepts for the interaction with
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
   :rationale: The platform shall be usable by safety relevant applications.
   :status: valid

   The software platform shall support applications with an automotive safety
   integrity level up to ASIL-B.

   Note: This is part of 0.1 release and therefore can only support ASIL_B. Goal is ASIL_D.


.. stkh_req:: Safety features
   :id: stkh_req__dependability__safety_features
   :reqtype: Functional
   :security: NO
   :safety: ASIL_D
   :rationale: tbd
   :status: valid

   The following safety feature shall be supported by the software platform:

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
   * Safe switch from engineering for field mode and back


.. stkh_req:: Availability
   :id: stkh_req__dependability__availability
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The software platform shall support the development of highly available systems.
   (see also `Availability <https://en.wikipedia.org/wiki/Availability>`_).


.. stkh_req:: Security features
   :id: stkh_req__dependability__security_features
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: tbd
   :status: valid

   The following security features shall be supported by the platform

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

   The platform shall support a deterministic, time-based application execution model that triggers logic based on predefined schedules or
   polling intervals.


.. stkh_req:: Support for Data-driven Architecture
   :id: stkh_req__app_architectures__support_data
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: tbd - potentially above explanation
   :status: valid

   The platform shall support an event-driven, high-throughput application architecture where execution is triggered by data changes.

.. stkh_req:: Support for Request-driven Architecture
   :id: stkh_req__app_architectures__support_request
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: tbd - potentially above explanation
   :status: valid

   The platform shall support a request-driven, asynchronous application architecture that processes requests on-demand.



Execution model
---------------

.. stkh_req:: Processes and thread management
   :id: stkh_req__execution_model__processes
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The platform shall support the following scheduling strategies:

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

   Cycle times of less then 5 ms on application level shall by supported by the
   platform assumed this is supported by the underlying hardware.

.. stkh_req:: Realtime capabilities
   :id: stkh_req__execution_model__realtime_cap
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The platform shall support the controlled reaction on events
   (timing events, interrupts) within a defined timing interval.

.. stkh_req:: Startup performance
   :id: stkh_req__execution_model__startup_perf
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The software platform shall support fast startup scenarios e.g. cold boot and
   resume from hibernate mode.

.. stkh_req:: Low power mode
   :id: stkh_req__execution_model__low_power
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The software platform shall support low power modes to safe energy.

Communication
-------------

.. stkh_req:: Inter-process Communication
   :id: stkh_req__communication__inter_process
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Application software typically consists of multiple processes which need to interact.
   :status: valid

   The platform shall support inter-process communication.


.. stkh_req:: Intra-process Communication
   :id: stkh_req__communication__intra_process
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Application software typically maps software building blocks into the same process.
   :status: valid

   The platform shall support intra-process communication.

.. stkh_req:: Stable application interfaces
   :id: stkh_req__communication__stable_app_inter
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: In case of incompatible changes on external interface the portability effort shall be reduced.
   :status: valid

   The platform shall provide a framework to mitigate incompatible changes on
   external interfaces to keep application interfaces stable.

.. stkh_req:: Extensible External Communication
   :id: stkh_req__communication__extensible_external
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: ECUs need to interact with each other. There are multiple protocols today and more to come in the future.
   :status: valid

   The platform shall support external communication via well established protocols e.g. Zenoh, DDS.


.. stkh_req:: Safe Communication
   :id: stkh_req__communication__safe
   :reqtype: Functional
   :security: NO
   :safety: ASIL_D
   :rationale: Distributed safe systems often require communication to be safe.
   :status: valid

   The platform shall support safe communication.


.. stkh_req:: Secure Communication
   :id: stkh_req__communication__secure
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Distributed secure systems often require secure communication.
   :status: valid

   The platform shall support secure communication.

.. stkh_req:: Supported network protocols
   :id: stkh_req__communication__supported_net
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The software platform shall support the following automotive network
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

   The software platform shall provide a framework to ensure quality of service
   of applications deployed on the platform. This includes but is not limited
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

   The following diagnostic protocols shall be supported
   * UDS (ISO14229) Diagnostics
   * Diagnostic trouble codes
   * Diagnostic jobs


AI Platform
-----------


.. stkh_req:: On-board ML Workloads
   :id: stkh_req__ai_platform__enablement
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Modern vehicles require the integration of ML capabilities to remain competitive and support customer expectations.
   :status: valid

   The platform shall support the execution of traditional ML workloads on-board.


.. stkh_req:: Support for Safety-Critical ML
   :id: stkh_req__ai_platform__safety_critical
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Some ML-based functionality is required to be certified up to ASIL-B.
   :status: valid

   The platform shall support safety-compliant (ASIL-B) deployment of AI/ML components, including inference backends and pipelines.


.. stkh_req:: Runtime Efficiency for Edge Devices
   :id: stkh_req__ai_platform__runtime_efficiency
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Automotive platforms have limited compute and thermal budgets.
   :status: valid

   The AI platform shall be optimized for runtime performance and memory footprint on embedded hardware targets.


.. stkh_req:: Platform Portability (QNX + Linux)
   :id: stkh_req__ai_platform__platform_portability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: AI/ML use cases span both safety and non-safety environments, requiring portability across operating systems.
   :status: valid

   The platform shall support both QNX (for safety) and Linux (for GenAI and flexibility) with reusable components.


.. stkh_req:: Secure Model Execution
   :id: stkh_req__ai_platform__model_security
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: AI model execution must be protected against tampering or abuse.
   :status: valid

   The platform shall ensure secure, verified, and integrity-checked model execution.


.. stkh_req:: Deterministic Execution Paths
   :id: stkh_req__ai_platform__runtime_determinism
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety certification requires predictable and bounded system behavior.
   :status: valid

   The platform shall ensure deterministic behavior for AI components used in safety-relevant paths.


.. stkh_req:: On-board GenAI Workloads
   :id: stkh_req__gen_ai__enablement
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Modern vehicles require the integration of AI/ML capabilities to remain competitive and support customer expectations.
   :status: valid

   The platform shall support the execution of Generative AI workloads on-board.


.. stkh_req:: GenAI User Interaction
   :id: stkh_req__gen_ai__interaction
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: HMIs are expected to support intelligent, natural interaction using LLM-based assistants.
   :status: valid

   The platform shall support on-device GenAI-based models with user interaction.


.. stkh_req:: Action Safety and Governance
   :id: stkh_req__gen_ai__safety_filter
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: GenAI output may be unpredictable or unsafe and must be controlled before affecting vehicle behavior.
   :status: valid

   The platform shall validate all actions proposed by GenAI models against safety and policy rules prior to execution.


.. stkh_req:: Seamless Integration with Vehicle Systems
   :id: stkh_req__gen_ai__vehicle_com
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: AI components must interact with vehicle state and control interfaces.
   :status: valid

   The platform shall expose structured APIs to access vehicle state and execute safe commands.


Hardware support
----------------

.. stkh_req:: Chipset support for ARM64 and x64
   :id: stkh_req__hardware_support__chipset_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The platform shall support arm64 and x64 architectures.


.. stkh_req:: Virtualization support for debug and testing
   :id: stkh_req__hardware_support__debug_and_test
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The software platform shall run on qemu to enable test and debug in virtualized
   environments.


.. stkh_req:: Support of container technologies
   :id: stkh_req__hardware_support__container_tech
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The software platform shall support deployment of self-contained application
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

   The platform shall provide a human readable interface definition language
   with decentralized glue code generation.


.. stkh_req:: Developer experience and development toolchain
   :id: stkh_req__dev_experience__dev_toolchain
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The platform shall support a state-of-the art developer experience for
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

   The software platform shall support performance analysis of platform and
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

   The platform shall support the tracing of events (start, stop) of executable
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

   The platform shall support the tracing of communication events for internal
   and external communication systems.

.. stkh_req:: Tracing of memory access
   :id: stkh_req__dev_experience__tracing_of_memory
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The platform shall support the tracing of memory events (allocation, copy,
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

   The software platform shall support observation, assessment of
   timing requirements with state-of-the-art analysis tools.

.. stkh_req:: Debugging
   :id: stkh_req__dev_experience__debugging
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The software platform shall provide a method and interface to enable
   debugging of the software on target and in vehicle.


.. stkh_req:: Programming languages for application development
   :id: stkh_req__dev_experience__prog_languages
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The platform shall support implementation of applications in the following
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

   The platform shall support data-collection and injection of reprocessed data.


.. stkh_req:: Logging support
   :id: stkh_req__dev_experience__logging_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid

   The platform shall support the following logging setups:

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

   The platform shall support logging of data to memory which survives a reboot
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

   Integration of multiple repositories shall be supported in a unified workflow.


Quality
-------

.. stkh_req:: Document assumptions and design decisions
   :id: stkh_req__quality__assumptions_and_dd
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This is a usability constraint needed for long term maintenance support
   :status: valid

   All assumptions and design decisions made shall be specified as requirements and agreed within the S-CORE community.


Requirements Engineering
------------------------

.. stkh_req:: Requirements traceability
   :id: stkh_req__re_requirements__traceability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This is a usability constraint needed for long term maintenance support
   :status: valid

   All requirements shall be linked from lower to upper level, whereby the top-level are the stakeholder requirements.

.. stkh_req:: Document requirements as code
   :id: stkh_req__requirements__as_code
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: In this project no external tool or service is used. Therefore as-code is the selected option.
   :status: valid

   Requirements shall be documented as code (Docs-as-code).
