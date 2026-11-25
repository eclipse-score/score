..
   # *******************************************************************************
   # Copyright (c) 2024-26 Contributors to the Eclipse Foundation
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

.. document:: SW-platform stakeholder requirements
   :id: doc__stakeholder_requirements
   :status: draft
   :version: 1
   :security: YES
   :safety: ASIL_B
   :realizes: wp__requirements_stkh[version==1]



Platform Capabilities
---------------------
"What functionality does S-CORE provide?"

The Platform Capabilities are structured and visualized in the :need:`doc__platform_architecture`.


Common Capabilities
~~~~~~~~~~~~~~~~~~~

Common capabilities provide reusable functionality shared across
SW-platform components and services to promote consistency, reuse,
and maintainability across the platform.


.. stkh_req:: Base Libraries
   :id: stkh_req__functional_req__base_libraries
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Common libraries reduce duplication, improve consistency and quality across components.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide a set of base libraries offering common functionality for SW-platform components.


Base Service Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~

Base service capabilities provide fundamental platform services used by
applications and SW-platform components to support common runtime needs
such as configuration, logging, storage, and time.

Configuration Capability
^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: File Based Configuration
   :id: stkh_req__functional_req__file_based
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: File based configuration allows changes without rebuilding the software.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support configuration of applications via files (e.g. yaml, json)

.. stkh_req:: Safe Configuration
   :id: stkh_req__functional_req__safe_config
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Configuration files may hold safety relevant information.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support safe configuration.

.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Secure Configuration
   :id: stkh_req__configuration__secure
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Security-related configuration data may influence the security behavior of the system and therefore needs to be protected against unauthorized modification.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms to protect security-related
   configuration data against unauthorized modification.



Logging Capabilities
^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Logging support
   :id: stkh_req__dev_experience__logging_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

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
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support logging of data to memory which survives a reboot
   cycle.

.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Early Startup Logging
   :id: stkh_req__logging__early_startup
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Diagnostic information generated during early platform startup is required to analyze initialization and startup failures.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide logging capabilities during early platform
   startup.

Storage Capabilities
^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Data Persistency
   :id: stkh_req__functional_req__data_persistency
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Applications typically need to store data across power cycles.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support to store data on non-volatile memory e.g. disks, flash, etc.

.. stkh_req:: Support of safe Key/Value store
   :id: stkh_req__functional_req__support_of_store
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Key/Value storage is a standard way to structure file based non-volatile memory access.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall provide towards the applications a safe key/value store.


.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Safe Storage
   :id: stkh_req__storage__safe
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related persistent data may influence safety-related behavior and therefore needs to maintain its integrity and consistency across storage and retrieval operations.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide persistent storage for safety-related
   application data with mechanisms to protect its integrity and consistency
   across storage and retrieval operations.

   .. stkh_req:: Secure Storage
   :id: stkh_req__storage__secure
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Security-related persistent data may influence the security behavior of the system and therefore needs to be protected against unauthorized access and modification.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms to protect security-related
   persistent data against unauthorized access and modification.


Time Capabilities
^^^^^^^^^^^^^^^^^

Vehicle Time
""""""""""""
Common synchronized time across the vehicle/distributed ECUs.


.. stkh_req:: Vehicle Time base Synchronization
   :id: stkh_req__time__vehicle_time_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Enables the system to compare in-vehicle events chronologically.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide a framework to synchronize its local vehicle clock representation to a Time Master within the vehicle.

.. stkh_req:: Vehicle Time base API
   :id: stkh_req__time__vehicle_time_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Enables an application to correlate its data with a vehicle-internal time reference for event timestamp and chronological events comparison.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide access to the synchronized vehicle time.
   Access shall be free from interferences for the consuming components.

Note (providing tracebility as long as safety analysis is not available):
   :need:`stkh_req__time__vehicle_time_api` requires backing by :need:`aou_req__platform__veh_time_e2e_integrity`
   to guarantee end-to-end data integrity.

.. stkh_req:: Synchronize the HW clock with Vehicle Time
   :id: stkh_req__time__hw_clock_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Enables the system to compare events from different ECUs chronologically, using the same time base for timestamping ingress and egress frames.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall synchronize the local HW clock to vehicle time.

Absolute Time
"""""""""""""
Time related to an external absolute reference, e.g. UTC.

.. stkh_req:: Time Synchronization with external sources
   :id: stkh_req__time__absolute_time_sync
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables the system to validate a certificate or token with temporal validity conditions, to add a UTC-timestamp to a data set, etc.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide a framework to synchronize its local absolute clock representation to an external-to-vehicle absolute time base (e.g. UTC).

.. stkh_req:: Absolute time base API
   :id: stkh_req__time__absolute_time_api
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables an application to correlate its data with an absolute vehicle-external time reference for event timestamping and chronological events comparison.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide access to the absolute time base, synchronized with external time sources.
   Access shall be free from interferences for the consuming components.

Local Clocks
""""""""""""

Local clocks used for durations, scheduling and measurements.


.. stkh_req:: Local High Resolution Clock API
   :id: stkh_req__time__high_res_clock_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Enables an application to get the current system time, which is essential for time-sensitive operations and event scheduling, via common, mockable and standardized API.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide access to the current high resolution clock from the system time provider in nanoseconds.
   Access shall be free from interferences for the consuming components.

   Note: to which clock the high resolution clock is mapped, depends on the system design.

Note (allowing tracebility as long as safety analysis is not available):
   :need:`stkh_req__time__high_res_clock_api` requires backing by :need:`aou_req__platform__os_safety_functions`
   to guarantee FFI and clock data integrity on OS and HW level.

.. stkh_req:: Local Monotonic Clock API
   :id: stkh_req__time__monotonic_clock_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Enables an application to get the current system time, which is essential for time-sensitive operations and event scheduling, via common, mockable and standardized API.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide access to the current monotonic clock from the system time provider.
   Access shall be free from interferences for the consuming components.

   Note: to which clock the monotonic clock is mapped, depends on the system design.

Note (allowing tracebility as long as safety analysis is not available):
   :need:`stkh_req__time__monotonic_clock_api` requires backing by :need:`aou_req__platform__os_safety_functions`
   to guarantee FFI and clock data integrity on OS and HW level.


Application and Execution Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Application and execution capabilities provide the runtime mechanisms
required to structure, activate, coordinate, schedule, and manage
applications and their execution on the SW-platform.

Application Execution Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Support for Time-based Architectures
   :id: stkh_req__app_architectures__support_time
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: tbd - potentially above explanation
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support a deterministic, time-based application execution model that triggers logic based on predefined schedules or
   polling intervals.


.. stkh_req:: Support for Data-driven Architecture
   :id: stkh_req__app_architectures__support_data
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd - potentially above explanation
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support an event-driven, high-throughput application architecture where execution is triggered by data changes.

.. stkh_req:: Support for Request-driven Architecture
   :id: stkh_req__app_architectures__support_request
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd - potentially above explanation
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support a request-driven, asynchronous application architecture that processes requests on-demand.



Process and Execution Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Processes and thread management
   :id: stkh_req__execution_model__processes
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

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

Safety-related Execution
^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Safe Computation
   :id: stkh_req__functional_req__safe_comput
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safe systems require computations to be done in safe environments.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support safe computation.

Operational Mode Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Safe Mode Switch
   :id: stkh_req__dependability__safe_mode_switch
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: It is expected that the SW platform is used in systems in having engineering (development) modes and field (customer) modes, where engineering modes may allow functionality which is unsafe.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall implement Safe switch from engineering to field mode and back

Communication Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~

Communication capabilities provide the mechanisms required for data exchange
and interaction between software components within the SW-platform and with
external systems across supported communication technologies.

Internal Communication
^^^^^^^^^^^^^^^^^^^^^^
.. stkh_req:: Inter-process Communication
   :id: stkh_req__communication__inter_process
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Application software typically consists of multiple processes which need to interact.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support inter-process communication.

.. stkh_req:: Intra-process Communication
   :id: stkh_req__communication__intra_process
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Application software typically maps software building blocks into the same process.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support intra-process communication.



.. stkh_req:: ABI Compatible Data Types
   :id: stkh_req__communication__abi_compatible
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: ABI compatiblity ensures that the same memory location is correctly interpreted by different programming languages.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support ABI compatible data types for zero-copy communication between Rust and C++ applications.


External Communication
^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Extensible External Communication
   :id: stkh_req__communication__extensible_external
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: ECUs need to interact with each other. There are multiple protocols today and more to come in the future.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support external communication via well established protocols e.g. Zenoh, DDS.


Communication Technologies
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. stkh_req:: Supported network protocols
   :id: stkh_req__communication__supported_net
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support the following automotive network
   protocols

   * SOME/IP
   * DDS
   * UWB including Driver for UWB Peripheral
   * SPI (+ CSC ADI & Texas Instruments chipset support)
   * Vehicle to Grid + ISO Charge protocols
   * AVB






.. will be added with v2, just commented out to be comaptible with v1

   .. stkh_req:: SOME/IP Communication
   :id: stkh_req__communication__someip
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: The platform needs to interoperate with automotive systems using SOME/IP-based service-oriented communication.
   :status: valid
   :version: 1
   :valid_from: v1.0.0
 
   The SW-platform shall support SOME/IP communication.

   .. stkh_req:: DDS Communication
   :id: stkh_req__communication__dds
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: The platform needs to interoperate with systems using DDS-based data-centric communication.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support DDS communication.




Safety-related Communication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Safe Communication
   :id: stkh_req__communication__safe
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Distributed safe systems often require communication to be safe.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support safe communication.





Diagnostics Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~

Diagnostics capabilities provide the mechanisms required to identify,
report, access, and analyze diagnostic information and to support diagnostic
operations across applications, SW-platform components, and vehicle systems.

Diagnostic Infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Automotive diagnostics
   :id: stkh_req__communication__auto_diagnostics
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support the following diagnostic protocols
   * SOVD (ISO 17978)
   * UDS (ISO 14229) Diagnostics
   * Diagnostic trouble codes
   * Diagnostic jobs

.. stkh_req:: Fault Reporting Infrastructure
   :id: stkh_req__diagnostics__fault_reporting
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables applications and components to report faults in a structured, reusable, and system-wide accessible manner.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support a reusable fault reporting infrastructure that enables applications and SW-platform components to report, persist, and manage diagnostic fault information.


SOVD Diagnostics
^^^^^^^^^^^^^^^^

.. stkh_req:: Diagnostic via SOVD
   :id: stkh_req__diagnostics__via_sovd
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables modern, scalable diagnostics using a standard REST-based protocol to improve integration, interoperability, and maintainability.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support vehicle diagnostics via the SOVD protocol as defined in ISO 17978, to allow scalable and secure diagnostic access.


.. stkh_req:: Readout DTCs via SOVD
   :id: stkh_req__diagnostics__dtc_read_sovd
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables reading of Diagnostic Trouble Codes (DTCs) from the ECU for various use-cases like production or maintenance.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide users the ability to retrieve current Diagnostic Trouble Codes (DTCs) from the ECU via the SOVD protocol.

.. stkh_req:: Extensibility of Diagnostic Services
   :id: stkh_req__diagnostics__custom_services
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables OEMs and developers to implement system-specific or project-specific routines for diagnostic control and testing.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support extensibility mechanisms that allow integration of custom diagnostic services and routines via the SOVD interface.

Diagnostic Interoperability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Compatibility with UDS Testers
   :id: stkh_req__diagnostics__uds_tester_compat
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Ensures continued usability of existing test infrastructure, avoiding costly replacement of legacy tools and ensuring fulfillment of legal requirements.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide compatibility with UDS-based testers by offering a proxy to translate UDS requests into SOVD-compatible actions.

.. stkh_req:: Compatibility with UDS ECUs
   :id: stkh_req__diagnostics__uds_ecus
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Ensures continued operability of ECUs that are not SOVD-capable.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support integration with ECUs that use UDS by providing a compatibility adapter to translate SOVD requests to UDS commands.

Distributed Diagnostics
^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Support for Distributed and Multi-ECU Diagnostics
   :id: stkh_req__diagnostics__distributed_support
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables the system to operate in modern, distributed vehicle architectures where diagnostics span multiple ECUs and subsystems.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support distributed diagnostics across multiple ECUs and network segments, enabling routing and aggregation of diagnostic data.


Security Service Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Security service capabilities define security-related functionality and
services provided by the SW-platform for use by applications and
SW-platform components.

Cryptographic Services
^^^^^^^^^^^^^^^^^^^^^^

.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Cryptographic Services
   :id: stkh_req__security__cryptographic_services
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Security-related applications and platform services require cryptographic operations to protect the confidentiality, integrity, and authenticity of data.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide cryptographic services for security-related
   applications and SW-platform components.


   .. stkh_req:: Secure Random Number Generation
   :id: stkh_req__security__secure_random
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Cryptographic operations require random values with sufficient entropy for security-related use.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide cryptographically secure random number
   generation for security-related applications and SW-platform components.

Key and Credential Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Cryptographic Key Management
   :id: stkh_req__security__key_management
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Security-related applications and platform services require controlled management of cryptographic keys throughout their lifecycle.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms for managing cryptographic keys
   used by security-related applications and SW-platform components.

   .. stkh_req:: Certificate Management
   :id: stkh_req__security__certificate_management
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Certificate-based authentication and secure communication require certificates and associated trust information to be managed throughout their lifecycle.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms for managing certificates and
   associated trust information.

   .. stkh_req:: Hardware-backed Secure Storage
   :id: stkh_req__security__hardware_backed_storage
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Cryptographic keys and other security-sensitive assets may require protection against unauthorized access and extraction beyond software-based isolation.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support hardware-backed protection of cryptographic
   keys and other security-sensitive assets.


Secure Communication
^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Secure Onboard Communication
   :id: stkh_req__dependability__sec_onboard_com
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0


Network Security
^^^^^^^^^^^^^^^^

.. stkh_req:: Firewall
   :id: stkh_req__dependability__firewall
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

.. stkh_req:: IPSec
   :id: stkh_req__dependability__ipsec
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

.. stkh_req:: MACSec
   :id: stkh_req__dependability__macsec
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0



Security Monitoring
^^^^^^^^^^^^^^^^^^^

.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Security Event Reporting
   :id: stkh_req__security__event_reporting
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Security-relevant events need to be reported to enable detection, analysis, and reaction to security-related incidents.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide mechanisms for applications and SW-platform
   components to report security-relevant events.


AI/ML Platform Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~
"What AI/ML-specific capabilities does S-CORE provide?"

AI/ML platform capabilities provide framework functionality required to
integrate, manage, and execute AI/ML workloads on the SW-platform.

AI Workload Execution
^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: On-board ML Workloads
   :id: stkh_req__ai_platform__enablement
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Modern vehicles require the integration of ML capabilities to remain competitive and support customer expectations.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support the execution of traditional ML workloads on-board.


.. stkh_req:: On-board GenAI Workloads
   :id: stkh_req__gen_ai__enablement
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Modern vehicles require the integration of AI/ML capabilities to remain competitive and support customer expectations.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support the execution of Generative AI workloads on-board.

AI Application Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: GenAI User Interaction
   :id: stkh_req__gen_ai__interaction
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: HMIs are expected to support intelligent, natural interaction using LLM-based assistants.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support on-device GenAI-based models with user interaction.


.. stkh_req:: Seamless Integration with Vehicle Systems
   :id: stkh_req__gen_ai__vehicle_com
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: AI components must interact with vehicle state and control interfaces.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall expose structured APIs to access vehicle state and execute safe commands.


AI Model Management
^^^^^^^^^^^^^^^^^^^

.. stkh_req:: AI Model Artifact Lifecycle
   :id: stkh_req__ai_platform__model_lifecycle
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: AI models are updated independently of the application software and must be updatable and revertible in the field without re-releasing the application.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall manage AI model artifacts over their lifecycle, including versioning, update and rollback.

AI Safety
^^^^^^^^^

.. stkh_req:: Support for Safety-Critical ML
   :id: stkh_req__ai_platform__safety_critical
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Some ML-based functionality is required to be certified up to ASIL-B.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support safety-compliant (ASIL-B) deployment of AI/ML components, including inference backends and pipelines.


.. stkh_req:: Deterministic Execution Paths
   :id: stkh_req__ai_platform__runtime_determinism
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety certification requires predictable and bounded system behavior.
   :status: valid
   :version: 1
   :tags: safety_mechanism, artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall ensure deterministic behavior for AI components used in safety-relevant paths.


.. stkh_req:: Deterministic AI Agent Execution
   :id: stkh_req__ai_platform__agent_execution
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: AI-based agents share compute resources with vehicle functions of higher criticality and therefore need bounded and predictable resource usage.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall execute AI-based agents with defined scheduling and resource budgets per criticality domain.





.. stkh_req:: Action Safety and Governance
   :id: stkh_req__gen_ai__safety_filter
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: GenAI output may be unpredictable or unsafe and must be controlled before affecting vehicle behavior.
   :status: valid
   :version: 1
   :tags: safety_mechanism, artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall validate all actions proposed by GenAI models against safety and policy rules prior to execution.


.. will be removed with v2, req. is there for all functionalities

.. stkh_req:: Platform Portability (QNX + Linux)
   :id: stkh_req__ai_platform__platform_portability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: AI/ML use cases span both safety and non-safety environments, requiring portability across operating systems.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support both QNX (for safety) and Linux (for GenAI and flexibility) with reusable components.


AI Security
^^^^^^^^^^^

.. stkh_req:: Secure Model Execution
   :id: stkh_req__ai_platform__model_security
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: AI model execution must be protected against tampering or abuse.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall ensure secure, verified, and integrity-checked model execution.



Automotive Safety
-----------------
"How does S-CORE support safety-related systems?"

The following requirements define safety-related properties, mechanisms,
and system behaviors required from the SW-platform.

Safety Capability
~~~~~~~~~~~~~~~~~

.. stkh_req:: Automotive Safety Integrity Level (ASIL)
   :id: stkh_req__dependability__automotive_safety
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: The SW-platform shall be usable by safety relevant applications.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support applications with an automotive safety
   integrity level up to ASIL-B.

Fault Detection and Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Health Management
   :id: stkh_req__dependability__health_management
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: Safety applications may have systematical errors which lead to violations in the control flow.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall implement Health Management (alive, deadline, logical supervision) for time and event based taskchains


.. stkh_req:: Program Flow Monitoring
   :id: stkh_req__dependability__flow_monitoring
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: Not all POSIX operating systems provide protection of POSIX processes from timing errors (e.g. delayed execution, deadlocks)
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform safety components shall use program flow monitoring to detect run time errors or explain in their safety concept why they do not need this.

   Note1: Reasons for not needing program flow monitoring could be an OS scheduler with timing and execution guarantees.
   Or that the non/late execution of the application keeps the system in a safe state.

   Note2: The SW-Platform supports this - see :need:`stkh_req__dependability__health_management` "live, deadline, logical supervision"

.. stkh_req:: End-To-End (E2E) Protection
   :id: stkh_req__dependability__e2eprotection
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: ECU external communication is using QM rated SW and HW which may currupt messages.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall implement E2E Protection for communication





Hardware Fault Detection and Mitigation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. stkh_req:: HW Self-Test
   :id: stkh_req__dependability__hw_self_test
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: The processing HW used by the SW platform may have errors affecting computing, data and control flow.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support Built-in hardware self-tests

   Note: Support means here that a functionality offered by external SW (e.g. an OS) or HW may need to be configured and used.

.. stkh_req:: Memory Error Correction
   :id: stkh_req__dependability__mem_error_correction
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: HW errors may occurr on the memory (e.g. bitflips caused by radiation)
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support ECC Memory

   Note: Support means here that a functionality offered by external SW (e.g. an OS) or HW may need to be configured and used.

Freedom from Interference
~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Memory Protection
   :id: stkh_req__dependability__memory_protection
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: ASIL SW components memory may be corrupted by QM SW components if those are located on the the same physical memory.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support Memory Management Unit

   Note: Support means here that a functionality offered by external SW (e.g. an OS) or HW may need to be configured and used.

.. stkh_req:: Direct Memory Access (DMA) Protection
   :id: stkh_req__dependability__dma_protection
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: DMA function usually grants also QM HW direct access to memory.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support I/O Memory Management Unit protecting DMA accesses

   Note: Support means here that a functionality offered by external SW (e.g. an OS) or HW may need to be configured and used.

.. stkh_req:: Cache Protection
   :id: stkh_req__dependability__cache_protection
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: ASIL SW components memory may be corrupted by QM SW components if those are located on the the same physical memory.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support Memory Protection Unit for caches
   Note: Support means here that a functionality offered by external SW (e.g. an OS) or HW may need to be configured and used.

.. stkh_req:: No mixed ASIL
   :id: stkh_req__dependability__no_mixed_asil
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: It is assumed that POSIX processes as implemented by the OS provide isolation from memory and timing errors of other processes but not within.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform safety components running in one POSIX process shall implement the highest ASIL of their assigned functional requirements.


Fault Reaction
~~~~~~~~~~~~~~

.. stkh_req:: Safe Startup and Reset
   :id: stkh_req__dependability__safe_startup_reset
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: During startup and shutdown specific errors may occurr (e.g. inintialization errors due to insufficient resources).
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall implement and support Safe startup and reset paths


.. stkh_req:: External Supervision
   :id: stkh_req__dependability__external_supervision
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: The SW platform may run on malfunctioning HW (e.g. by undervoltage) which prevents from own error detection and recovery.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support Power management integrated circuit (PMIC), external watchdog and voltage monitoring

   Note: Support means here that a functionality offered by external SW (e.g. an OS) or HW may need to be configured and used.


.. stkh_req:: SW-platform error reaction
   :id: stkh_req__dependability__error_reaction
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety relies on error reporting, e.g. to preserve a safe system state.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v2.0.0

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
   :version: 1
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
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall react on errors (as described in :need:`stkh_req__dependability__safe_state` and :need:`stkh_req__dependability__error_reaction`) within 1 millisecond. If this is not feasible a special component AoU needs to be defined.

   Note1: The time span mentioned is the SW reaction time and not the time between the error happening and the reporting.
   For example if there is a alive supervision configured with 10ms cycle time and 5ms allowed delay,
   the error could happen in the first millisecond but will be reported earliest after 10+5ms plus the SW reaction time.

   Note2: If a user application calls a SW-platform function the (error) return is required latest after the reaction time, so there could be a timeout used by the application considering this.

Fault Tolerance
~~~~~~~~~~~~~~~

.. stkh_req:: SW Lockstep
   :id: stkh_req__dependability__sw_lockstep
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: Computing HW may suffer from systematic or random HW errors.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v2.0.0

   The SW-platform shall implement Software Lockstep




Availability
~~~~~~~~~~~~

.. stkh_req:: Availability
   :id: stkh_req__dependability__availability
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support the development of highly available systems.
   (see also `Availability <https://en.wikipedia.org/wiki/Availability>`_).

Cybersecurity
-------------
"How does S-CORE support cybersecurity?"

The following requirements define cybersecurity properties and system
behaviors required from the SW-platform.

Cybersecurity Capability
~~~~~~~~~~~~~~~~~~~~~~~~

.. will be removed with v2 with detailed functionality instead

.. stkh_req:: Security features
   :id: stkh_req__dependability__security_features
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0


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



.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Cybersecurity Assurance Level 2 Support
   :id: stkh_req__security__cal_2_support
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :rationale: Security-related applications require platform capabilities that support the implementation of cybersecurity functions and measures up to CAL-2.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide cybersecurity capabilities supporting the
   development and operation of security-related applications up to CAL-2.

   Cybersecurity-related SW-platform capabilities include, but are not limited to:

   - :need:`stkh_req__communication__secure`
   - :need:`stkh_req__configuration__secure`
   - :need:`stkh_req__storage__secure`


Identity and Access Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Identity and Access Management
   :id: stkh_req__security__iam
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Security-relevant resources and services require identification of entities and controlled access according to their assigned permissions.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms for managing identities,
   authentication information, and access permissions for entities accessing
   security-relevant platform resources and services.

.. stkh_req:: Mandatory Access Control (MAC)
   :id: stkh_req__dependability__mac
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

.. stkh_req:: Secure Access to Diagnostic Interfaces
   :id: stkh_req__diagnostics__secure_access
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Diagnostic access allows deep system introspection and manipulation, which must be protected against unauthorized use.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall enforce secure access control for all diagnostic interfaces, including authentication, encryption, and role-based access enforcement.


Secure Communication
~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Secure Communication
   :id: stkh_req__communication__secure
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Distributed secure systems often require secure communication.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support secure communication.

Platform Integrity and Hardening
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Secure Boot
   :id: stkh_req__dependability__secure_boot
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Platform Hardening
   :id: stkh_req__security__platform_hardening
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Platform software needs protection against exploitation of software vulnerabilities that could compromise the confidentiality, integrity, or availability of security-relevant platform functions.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support security hardening mechanisms that reduce
   the exploitability of vulnerabilities in platform software.

   .. note::

      Hardening mechanisms may include address-space randomization,
      compiler-based exploit mitigations, control-flow protection, and
      operating-system hardening features.


Security Lifecycle
~~~~~~~~~~~~~~~~~~

.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Secure Software Update
   :id: stkh_req__security__secure_software_update
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Software updates can modify security-relevant platform functionality and therefore need protection against unauthorized or manipulated update artifacts.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support secure software updates with mechanisms
   to verify the authenticity and integrity of software update artifacts
   before installation.

   .. stkh_req:: Secure Feature Activation
   :id: stkh_req__security__secure_feature_activation
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Activation of platform and application features needs to be protected against unauthorized modification or activation.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms to restrict activation and
   deactivation of security-relevant features to authorized entities.


Performance and Resource Efficiency
-----------------------------------
"What runtime qualities can stakeholders expect?"

Performance and resource-efficiency requirements define the timing,
resource utilization, determinism, and energy-efficiency properties
expected from the SW-platform.


Communication Efficiency
~~~~~~~~~~~~~~~~~~~~~~~~

.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: Zero-Copy Communication
   :id: stkh_req__communication__zero_copy
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: High-bandwidth and latency-sensitive applications require efficient data exchange while minimizing unnecessary copying of communication payloads.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support zero-copy communication for efficient
   exchange of large data payloads.


Timing and Latency
~~~~~~~~~~~~~~~~~~

.. stkh_req:: Short application cycles
   :id: stkh_req__execution_model__short_app_cycles
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support cycle times of less then 5 ms on application level
   if this is supported by the underlying hardware.


.. stkh_req:: Realtime capabilities
   :id: stkh_req__execution_model__realtime_cap
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support the controlled reaction on events
   (timing events, interrupts) within a defined timing interval.


Startup Performance
~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Startup performance
   :id: stkh_req__execution_model__startup_perf
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support fast startup scenarios e.g. cold boot and
   resume from hibernate mode.

Quality of Service and Resource Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Quality of service
   :id: stkh_req__communication__service_quality
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide a framework to ensure quality of service
   of applications deployed on the SW-platform. This includes but is not limited
   to:

   * QOS for applications
   * Controlled latency for communication and scheduling
   * Guaranteed network and compute quotas


Runtime Efficiency
~~~~~~~~~~~~~~~~~~

.. stkh_req:: Runtime Efficiency for Edge Devices
   :id: stkh_req__ai_platform__runtime_efficiency
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Automotive platforms have limited compute and thermal budgets.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall be optimized for runtime performance and memory footprint on embedded hardware targets.


Power Efficiency
~~~~~~~~~~~~~~~~

.. stkh_req:: Low power mode
   :id: stkh_req__execution_model__low_power
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support low power modes to safe energy.




Portability and Platform Compatibility
--------------------------------------
"Where can S-CORE execute?"


Operating System Portability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Operating System
   :id: stkh_req__functional_req__operating_system
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This allows portability of SW-platform on POSIX compliant operating systems.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support operating systems compliant with IEEE Std 1003.1 (2004 Edition or newer)

.. will be added with v2, just commented out to be comaptible with v1
   .. stkh_req:: QNX Platform Support
   :id: stkh_req__compatibility__qnx
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: QNX support enables deployment of the SW-platform on operating system environments used for production automotive systems.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support deployment and operation on QNX 8.


   .. stkh_req:: Linux Platform Support
   :id: stkh_req__compatibility__linux
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Linux support enables deployment of the SW-platform across development and Linux-based target environments.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support deployment and operation on Linux-based
   target systems.


Hardware Platform Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Chipset support for ARM64 and x64
   :id: stkh_req__hardware_support__chipset_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support arm64 and x64 architectures.


.. stkh_req:: Hardware Accelerated Computation
   :id: stkh_req__functional_req__hardware_comput
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: High computation loads typically need to be speed up hardware acceleration e.g. in ADAS applications
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support computation accelerated by a Hardware accelerator.


Virtualized and Containerized Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Virtualization support for debug and testing
   :id: stkh_req__hardware_support__debug_and_test
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall run on qemu to enable test and debug in virtualized
   environments.


.. stkh_req:: Support of container technologies
   :id: stkh_req__hardware_support__container_tech
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support deployment of self-contained application
   bundles

   * Kernel Features: e.g. cgroup, secpol, namespaces as precondition for containerization
   * e.g. SOAFFEE Like realtime capable containers: https://www.soafee.io/


Platform Lifecycle, Integration & Maintainability
-------------------------------------------------
"How can S-CORE evolve and integrate?"


API Compatibility & Standardization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Reuse of application software via managed APIs
   :id: stkh_req__overall_goals__reuse_of_app_soft
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This is a usability constraint needed for long maintenance support
   :status: valid
   :version: 1
   :valid_from: v1.0.0

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
    :version: 1
    :valid_from: v1.0.0

    The SW-platform shall where possible be based on existing standards (e.g. network protocols).

.. stkh_req:: Stable application interfaces
   :id: stkh_req__communication__stable_app_inter
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: In case of incompatible changes on external interface the portability effort shall be reduced.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide a framework to mitigate incompatible changes on
   external interfaces to keep application interfaces stable.


Integration
~~~~~~~~~~~

.. stkh_req:: Multirepo integration
   :id: stkh_req__integration__multi_repo
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Allow independent development of software modules
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform infrastructure shall support integration of multiple repositories in a unified workflow.



Configuration and Evolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Variant management
    :id: stkh_req__overall_goals__variant_management
    :reqtype: Functional
    :security: NO
    :safety: QM
    :rationale: tbd
    :status: valid
    :version: 1
    :valid_from: v1.0.0

    The SW-platform shall provide variant management support.
    Variant management support shall enable users to ensure the
    compatibility of application software across vehicle variants and vehicle
    software releases.

Engineering Lifecycle
~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Document assumptions and design decisions
   :id: stkh_req__quality__assumptions_and_dd
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: This is a usability constraint needed for long term maintenance support
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   Contributors shall specify all assumptions and design decisions as requirements which are agreed within the S-CORE community.


.. stkh_req:: Requirements traceability
   :id: stkh_req__re_requirements__traceability
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: This is a usability constraint needed for long term maintenance support
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform infrastructure shall support linking all requirements from lower to upper level, whereby on the top-level are the stakeholder requirements.



.. stkh_req:: Document requirements as code
   :id: stkh_req__requirements__as_code
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: In this project no external tool or service is used. Therefore as-code is the selected option.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform infrastructure shall support documenting all requirements as code (Docs-as-code).

Cooperation and Intellectual Property
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: IP protection
   :id: stkh_req__overall_goals__ip_protection
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support cooperation models, where partners do not
   want to disclose their intellectual property of applications to all other
   partners.


Developer Experience and Testability
------------------------------------
"How can developers build, observe, debug and test with it?"

Development
~~~~~~~~~~~

.. stkh_req:: IDL Support
   :id: stkh_req__dev_experience__idl_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide a human readable interface definition language
   with decentralized glue code generation.


.. stkh_req:: Developer experience and development toolchain
   :id: stkh_req__dev_experience__dev_toolchain
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support a state-of-the art developer experience for
   functional development and application development.

   Features:

   * IDE support for all supported languages.
   * IDL Editor with syntax highlighting.
   * Connection to qemu and real target via SSH.
   * Support of continuous integration and deployment systems.



.. stkh_req:: Programming languages for application development
   :id: stkh_req__dev_experience__prog_languages
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support implementation of applications in the following
   programming languages up to the highest ASIL level as defined in :need:`stkh_req__dependability__automotive_safety`:

   * C++
   * Rust

Debugging
~~~~~~~~~

.. stkh_req:: Debugging
   :id: stkh_req__dev_experience__debugging
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide a method and interface to enable
   debugging of the software on target and in vehicle.

Observability and Tracing
~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Tracing of execution
   :id: stkh_req__dev_experience__tracing_of_exec
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

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
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support the tracing of communication events for internal
   and external communication systems.

.. stkh_req:: Tracing of memory access
   :id: stkh_req__dev_experience__tracing_of_memory
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support the tracing of memory events (allocation, copy,
   de-allocation) for different types of memory e.g.

   * CPU Memory
   * GPU Memory

.. stkh_req:: AI Workload Observability
   :id: stkh_req__ai_platform__observability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Degradation of AI workloads is not detectable by functional monitoring alone and must be observable in the field and during development.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall expose runtime characteristics of AI workloads, such as inference latency and resource consumption, via the platform observability mechanisms.


Testing and Simulation
~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Mockup implementation for application testing
   :id: stkh_req__dev_experience__mockup_public_apis
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Enables unit, component and integration testing for both SW-platform related and non-platform related applications.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide support for mocking its public interfaces,
   enabling unit, component and integration testing of applications.

.. stkh_req:: Reprocessing and simulation support
   :id: stkh_req__dev_experience__reprocessing
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support data-collection and injection of reprocessed data.

Analysis
~~~~~~~~

.. stkh_req:: Performance analysis
   :id: stkh_req__dev_experience__perf_analysis
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support performance analysis of SW-platform and
   application software:

   * Flame-graph visualization for long termed CPU behavior
   * RAM usage statistics for long-term Memory behavior

.. stkh_req:: Timing analysis
   :id: stkh_req__dev_experience__timing_analysis
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support observation, assessment of
   timing requirements with state-of-the-art analysis tools.



Safety Mechanisms
-----------------

The following stakeholder requirements describe the assumed safety mechanisms which are needed due to complexity of the realizing
SW element(s) or due to dependency on HW. This is confirmed during safety analysis of the derived feature requirements and architecture.

.. needtable:: Expected Safety Mechanisms
   :filter: "safety_mechanism" in tags and type == "stkh_req" and is_external == False
   :style: table
   :columns: title; id; tags
   :colwidths: 30,30,30


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. To be moved out with v2


.. stkh_req:: Video subsystem
   :id: stkh_req__functional_req__video_subsystem
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide an interface for pre-processing and
   distribution of camera data via the following mechanisms

   * PCIe Graphic streams
   * Shared Memory Graphic streams
   * Display Serial Interface Driver
   * APIX serialization driver
   * ISP Driver including correction and frame pre-processing CV library (lens distortion et. al.)
   * Sensor Streamer component (binding ISP Driver & pre-processing CV library)



.. stkh_req:: Communication with external MCUs/standby controllers
   :id: stkh_req__functional_req__comm_with_control
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall define protocols and concepts for the interaction with
   external micro-controllers for

   * board management
   * external supervision for safety and security functions
   * software update
   * debugging
   * feature activation


.. stkh_req:: Compute subsystem
   :id: stkh_req__functional_req__comp_subsystem
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: tbd
   :status: valid
   :version: 1
   :valid_from: v2.0.0

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
