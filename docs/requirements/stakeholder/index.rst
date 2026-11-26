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

.. document:: SW-platform stakeholder requirements
   :id: doc__stakeholder_requirements
   :status: draft
   :version: 2
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
   :id: stkh_req__common__base_libraries
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Common base libraries reduce duplication and promote consistent, reliable, and maintainable implementations across SW-platform components.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide reusable base libraries for common
   functionality shared across SW-platform components.

Base Service Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~

Base service capabilities provide fundamental platform services used by
applications and SW-platform components to support common runtime needs
such as configuration, logging, storage, and time.

Configuration Capability
^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: File-Based Configuration
   :id: stkh_req__configuration__file_based
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Applications need to be configurable without requiring modification or rebuilding of the application software.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support configuration of applications through
   external configuration files without requiring modification or rebuilding
   of the application software.

.. stkh_req:: Safe Configuration
   :id: stkh_req__configuration__safe
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Configuration data may influence safety-related behavior; loss of its integrity could therefore lead to unintended safety-related behavior of the SW-platform.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall protect the integrity of safety-related configuration data.

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

.. stkh_req:: Logging Support
   :id: stkh_req__logging__support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Logging enables development, integration, operation, and troubleshooting by providing diagnostic and runtime information about SW-platform components and applications.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide logging capabilities for applications and
   SW-platform components, including the collection, storage, and forwarding
   of log data.

.. stkh_req:: Persistent Logging
   :id: stkh_req__logging__persistent
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Log data preserved across platform restart cycles is required to analyze failures that cause a restart or prevent normal system operation.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall preserve configured log data across platform restart
   cycles to enable analysis after a restart.


.. stkh_req:: Early Startup Logging
   :id: stkh_req__logging__early_startup
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Diagnostic information generated during early platform startup is required to analyze initialization and startup failures.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide logging capabilities during early platform
   startup.


Storage Capabilities
^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Data Persistency
   :id: stkh_req__storage__data_persistency
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Applications need to preserve data across application restarts and platform power cycles.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide persistent storage capabilities for
   application data.

.. stkh_req:: Key/Value Storage
   :id: stkh_req__storage__key_value_store
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Applications require a simple persistent storage mechanism for structured data that can be addressed and retrieved by key.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide persistent key/value storage for
   application data.

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


.. stkh_req:: Vehicle Time Base Synchronization
   :id: stkh_req__time__vehicle_time_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: A synchronized vehicle time base enables events occurring across distributed vehicle systems to be consistently timestamped, correlated, and ordered.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide a synchronized vehicle time base based on an
   external vehicle time source.


.. stkh_req:: Vehicle Time Base API
   :id: stkh_req__time__vehicle_time_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related applications require access to a common synchronized vehicle time reference for timestamping and correlation of data and events.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide safety-related applications with access to
   the synchronized vehicle time base.

   .. note::

      Until the corresponding safety analysis is available,
      :need:`stkh_req__time__vehicle_time_api` requires
      :need:`aou_req__platform__veh_time_e2e_integrity` to ensure end-to-end
      integrity of the provided vehicle time information.


.. stkh_req:: Local Clock Synchronization with Vehicle Time
   :id: stkh_req__time__local_clock_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Synchronization of the clock with vehicle time enables consistent timestamping and chronological correlation of communication events across ECUs.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall synchronize the local clock with the
   synchronized vehicle time base.


Absolute Time
"""""""""""""
Time related to an external absolute reference, e.g. UTC.

.. stkh_req:: Absolute Time Synchronization
   :id: stkh_req__time__absolute_time_sync
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: An absolute time reference enables applications and platform services to timestamp data and evaluate time-dependent information such as certificates and tokens.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide an absolute time base synchronized with an
   external absolute time source.


.. stkh_req:: Absolute Time Base API
   :id: stkh_req__time__absolute_time_api
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Enables applications to timestamp and correlate data and events using a common absolute time reference.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide applications with access to the synchronized
   absolute time base.

Local Clocks
""""""""""""
Local clocks used for durations, scheduling and measurements.

.. stkh_req:: Local High-Resolution Clock API
   :id: stkh_req__time__high_res_clock_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related applications may require precise measurement of time intervals and execution of time-dependent operations using a high-resolution local clock.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide safety-related applications with access to
   a local high-resolution clock.

   .. note::

      The mapping of the high-resolution clock to the underlying system clock
      depends on the system design.

   .. note::

      Until the corresponding safety analysis is available,
      :need:`stkh_req__time__high_res_clock_api` requires
      :need:`aou_req__platform__os_safety_functions` to ensure freedom from
      interference and clock data integrity at OS and hardware level.


.. stkh_req:: Local Monotonic Clock API
   :id: stkh_req__time__monotonic_clock_api
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related applications require a monotonic time source for reliable measurement of elapsed time and time-dependent operations independent of adjustments to synchronized time bases.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide safety-related applications with access to
   a local monotonic clock.

   .. note::

      The mapping of the monotonic clock to the underlying system clock depends
      on the system design.

   .. note::

      Until the corresponding safety analysis is available,
      :need:`stkh_req__time__monotonic_clock_api` requires
      :need:`aou_req__platform__os_safety_functions` to ensure freedom from
      interference and clock data integrity at OS and hardware level.


Application and Execution Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Application and execution capabilities provide the runtime mechanisms
required to structure, activate, coordinate, schedule, and manage
applications and their execution on the SW-platform.

Application Execution Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Time-based Application Execution
   :id: stkh_req__execution__time_based
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Real-time and cyclic applications require predictable activation of application functionality based on defined timing constraints.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support time-based application execution in which
   application activities are activated according to defined timing
   conditions.

.. stkh_req:: Data-driven Application Execution
   :id: stkh_req__execution__data_driven
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Data-processing applications require execution models in which application functionality is activated by the availability or change of data.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support data-driven application execution in which
   application activities are activated in response to the availability or
   change of input data.


.. stkh_req:: Request-driven Application Execution
   :id: stkh_req__execution__request_driven
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Service-oriented applications require application functionality to be invoked on demand in response to incoming requests.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support request-driven application execution in which
   application functionality is invoked on demand in response to incoming
   requests.


Process and Execution Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Process Lifecycle Management
   :id: stkh_req__execution__process_lifecycle
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Applications require coordinated lifecycle management of their processes during startup, recovery, and shutdown.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide lifecycle management for application
   processes, including startup, shutdown, and recovery.


.. stkh_req:: Application Execution and Scheduling
   :id: stkh_req__execution__scheduling
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Applications require coordinated activation and execution of activities according to their execution model and timing constraints.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms for activating and scheduling
   application activities according to their execution model.


.. stkh_req:: Cross-process Synchronization
   :id: stkh_req__execution__cross_process_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Application functionality distributed across multiple processes requires coordinated execution of dependent activities.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms for synchronizing dependent
   application activities across process boundaries.

Safety-related Execution
^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Safe Execution
   :id: stkh_req__execution__safe
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related applications require an execution environment that supports the required safety integrity.
   :status: valid
   :version: 1
   :valid_from: v1.0.0


   The SW-platform shall provide execution capabilities suitable for
   safety-related computation up to ASIL-B.

Operational Mode Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Controlled Operational Mode Transition
   :id: stkh_req__execution__op_mode_transition
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: Engineering modes may enable functionality or access paths that are not permitted during normal vehicle operation and therefore require controlled transitions between operational modes.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support controlled transitions between engineering
   and field operation modes.


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
   :rationale: Software components deployed in separate processes require communication mechanisms for exchanging data and coordinating their interaction.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support communication between software components
   deployed in separate processes.


.. stkh_req:: Intra-process Communication
   :id: stkh_req__communication__intra_process
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Software components deployed within the same process require communication mechanisms for exchanging data and coordinating their interaction without requiring inter-process communication.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support communication between software components
   deployed within the same process.


.. stkh_req:: Cross-Language Data Compatibility
   :id: stkh_req__communication__x_lang_comp
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Software components implemented in different supported programming languages require compatible data representations to exchange data without language-specific representation dependencies.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide compatible data representations across
   supported programming languages.


External Communication
^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Extensible External Communication
   :id: stkh_req__communication__extensible_external
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Automotive systems require communication with systems outside the SW-platform's own communication and runtime domain using different communication technologies.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support extensible external communication through
   established communication technologies.

Communication Technologies
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Communication Technologies
   :id: stkh_req__communication__technologies
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: The platform needs to integrate into different automotive system architectures and communicate with external systems using established automotive communication technologies.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support established communication technologies
   required for integration into automotive system architectures.

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
   :rationale: Safety-related functions distributed across components require communication capabilities that maintain the integrity of exchanged information.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide communication capabilities that protect
   the integrity of safety-related information exchanged between software
   components.

Diagnostics Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~

Diagnostics capabilities provide the mechanisms required to identify,
report, access, and analyze diagnostic information and to support diagnostic
operations across applications, SW-platform components, and vehicle systems.

Diagnostic Infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Automotive Diagnostics
   :id: stkh_req__diagnostics__auto_diagnostics
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Automotive diagnostics enable fault identification, maintenance, production, and service activities throughout the vehicle lifecycle.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide diagnostic capabilities for applications,
   SW-platform components, and vehicle-level diagnostic systems.

.. stkh_req:: Fault Reporting Infrastructure
   :id: stkh_req__diagnostics__fault_reporting
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Applications and SW-platform components need a common mechanism to report and manage diagnostic faults consistently across the platform.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide a common fault reporting capability that
   enables applications and SW-platform components to report and manage
   diagnostic fault information.

SOVD Diagnostics
^^^^^^^^^^^^^^^^

.. stkh_req:: Diagnostics via SOVD
   :id: stkh_req__diagnostics__via_sovd
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: SOVD enables standardized and scalable diagnostic access for software-defined vehicle architectures.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide diagnostic access via SOVD in accordance
   with ISO 17978.


.. stkh_req:: Read DTCs via SOVD
   :id: stkh_req__diagnostics__dtc_read_sovd
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Diagnostic users need access to Diagnostic Trouble Codes for production, maintenance, fault analysis, and service activities.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide access to Diagnostic Trouble Codes (DTCs)
   via SOVD.

.. stkh_req:: Extensibility of Diagnostic Services
   :id: stkh_req__diagnostics__custom_services
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: OEMs and vehicle projects require project-specific diagnostic functionality in addition to standardized diagnostic services.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall enable integration of project-specific diagnostic
   services and routines accessible via SOVD.

Diagnostic Interoperability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Compatibility with UDS Testers
   :id: stkh_req__diagnostics__uds_tester_compat
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Existing UDS-based diagnostic infrastructure needs to remain usable during the transition to SOVD-based diagnostics.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support diagnostic access from UDS-based diagnostic
   testers to SOVD-based diagnostic services.


.. stkh_req:: Compatibility with UDS ECUs
   :id: stkh_req__diagnostics__uds_ecus
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: SOVD-based diagnostic systems need to interact with vehicle ECUs that provide diagnostics via UDS.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support diagnostic access to UDS-based ECUs from
   SOVD-based diagnostic systems.

Distributed Diagnostics
^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Distributed Diagnostics
   :id: stkh_req__diagnostics__distributed_support
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Vehicle diagnostics need to operate across distributed vehicle architectures comprising multiple ECUs and network segments.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support diagnostic operations across multiple ECUs
   and network segments.

Security Service Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Security service capabilities define security-related functionality and
services provided by the SW-platform for use by applications and
SW-platform components.

Cryptographic Services
^^^^^^^^^^^^^^^^^^^^^^

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

.. stkh_req:: SecOC Communication
   :id: stkh_req__security__secoc
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Security-related onboard communication requires protection against unauthorized modification, message forgery, and replay of communicated data.
   :status: valid
   :version: 1
   :valid_from: v3.0.0

   The SW-platform shall support SecOC for protecting the authenticity,
   integrity, and freshness of security-related onboard communication.


Network Security
^^^^^^^^^^^^^^^^

.. stkh_req:: Network Traffic Filtering
   :id: stkh_req__security__network_filtering
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Network-connected systems require control over permitted network communication to restrict unauthorized or unintended network traffic.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide mechanisms for filtering network traffic
   according to configurable network security policies.


.. stkh_req:: IPsec Communication
   :id: stkh_req__security__ipsec
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: IP-based communication may require standardized mechanisms to protect the confidentiality, integrity, and authenticity of network communication.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support IPsec for protected IP-based communication.


.. stkh_req:: MACsec Communication
   :id: stkh_req__security__macsec
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Ethernet communication may require standardized link-layer protection against unauthorized access and manipulation.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support MACsec for protected Ethernet communication.


Security Monitoring
^^^^^^^^^^^^^^^^^^^

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

.. stkh_req:: On-board ML Workload Execution
   :id: stkh_req__ai__ml_workloads
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: AI-enabled vehicle applications require local execution of ML workloads to use vehicle data and provide functionality without depending on external compute infrastructure.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support on-board execution of ML workloads.


.. stkh_req:: On-board Generative AI Workload Execution
   :id: stkh_req__ai__genai_workloads
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Generative AI applications may require local execution of generative AI workloads to provide vehicle functionality without depending on continuous external compute connectivity.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support on-board execution of generative AI
   workloads.

AI Application Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. stkh_req:: Interactive GenAI Application Support
   :id: stkh_req__ai__interactive_genai
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Interactive vehicle applications require integration of on-board generative AI models into user-facing application functionality.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support integration of on-board generative AI
   models into interactive applications.


.. stkh_req:: AI Vehicle System Integration
   :id: stkh_req__ai__vehicle_integration
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: AI applications require controlled interaction with vehicle information and services to integrate AI functionality into vehicle systems.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall provide defined interfaces enabling AI applications
   to access permitted vehicle information and interact with vehicle services.

AI Model Management
^^^^^^^^^^^^^^^^^^^

.. stkh_req:: AI Model Artifact Lifecycle
   :id: stkh_req__ai__model_lifecycle
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: AI model artifacts may evolve independently of application software and therefore require independent lifecycle and version management.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support lifecycle management of AI model artifacts,
   including versioning, update, and rollback.

AI Safety
^^^^^^^^^

.. stkh_req:: Safety-related AI/ML Support
   :id: stkh_req__ai__safety_support
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related vehicle functionality may use AI/ML components and therefore requires platform capabilities supporting their integration and execution up to ASIL-B.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall provide capabilities supporting integration and
   execution of AI/ML components in safety-related applications up to
   ASIL-B.

.. stkh_req:: Predictable AI Workload Execution
   :id: stkh_req__ai__predictable_execution
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related AI workloads require predictable and bounded execution behavior to support timing analysis and verification of safety-related functions.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall support predictable and bounded execution of AI
   workloads used by safety-related applications.

.. stkh_req:: Governed AI Actions
   :id: stkh_req__ai__action_governance
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :rationale: AI-generated actions that may affect vehicle behavior require control before execution to prevent violations of applicable safety and security constraints.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall provide mechanisms for controlling AI-generated
   actions affecting vehicle behavior according to defined safety and
   security constraints before execution.


AI Security
^^^^^^^^^^^

.. stkh_req:: AI Model Integrity Protection
   :id: stkh_req__ai__model_integrity
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Manipulated AI model artifacts may alter application behavior and therefore require authenticity and integrity verification before execution.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall verify the authenticity and integrity of AI model
   artifacts before they are used for execution and shall prevent their execution
   if authenticity or integrity cannot be successfully verified.

Automotive Safety
-----------------
"How does S-CORE support safety-related systems?"

The following requirements define safety-related properties, mechanisms,
and system behaviors required from the SW-platform.

Safety Capability
~~~~~~~~~~~~~~~~~

.. stkh_req:: ASIL-B SW-platform Support
   :id: stkh_req__safety__asil_b_support
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related applications require platform capabilities that support the implementation of safety functions up to ASIL-B.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support the development and execution of
   safety-related applications up to ASIL-B.

Safety-related SW-platform capabilities include, but are not limited to:

- :need:`stkh_req__communication__safe`
- :need:`stkh_req__configuration__safe`
- :need:`stkh_req__execution__safe`
- :need:`stkh_req__storage__safe`
- :need:`stkh_req__ai__action_governance`
- :need:`stkh_req__ai__predictable_execution`
- :need:`stkh_req__ai__safety_support`

Fault Detection and Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Health Management
   :id: stkh_req__safety__health_management
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related applications require supervision of execution behavior to detect violations of expected timing and control flow.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall provide health management for safety-related
   application activities, including alive, deadline, and logical supervision.

.. stkh_req:: Program Flow Monitoring
   :id: stkh_req__safety__flow_monitoring
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related execution may require supervision of the expected execution sequence to detect missing, repeated, or incorrectly ordered execution of application activities.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms for monitoring the expected
   execution sequence of safety-related application activities.


.. stkh_req:: End-to-End (E2E) Protection
   :id: stkh_req__safety__e2e_protection
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related communication may traverse QM-rated software and hardware elements that can introduce corruption, loss, repetition, or incorrect sequencing of communicated data.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall provide end-to-end protection mechanisms for
   detecting faults affecting safety-related communication.

Hardware Fault Detection and Mitigation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Hardware Self-Test
   :id: stkh_req__safety__hw_self_test
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Hardware faults in processing resources may affect computation, data integrity, and control flow of safety-related software.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support hardware self-test mechanisms for detecting
   hardware faults that may affect safety-related operation.

   .. note::

      Support means that functionality provided by external software,
      the operating system, or hardware may need to be configured and used
      by the SW-platform.

.. stkh_req:: Memory Error Detection and Correction
   :id: stkh_req__safety__mem_error_correction
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Random hardware faults in memory may corrupt data used by safety-related software and therefore need to be detected and, where supported, corrected.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support mechanisms for detecting memory errors that
   may affect safety-related operation and for correcting such errors where
   correction is supported by the underlying hardware.

   .. note::

      Support means that error detection and correction mechanisms provided
      by hardware or external software may need to be configured, monitored,
      and used by the SW-platform.


Freedom from Interference
~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Memory Protection
   :id: stkh_req__safety__memory_protection
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related software needs to be protected against unintended memory access by software components of lower criticality sharing the same memory resources.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support memory protection mechanisms that prevent
   unintended memory access between software components of different
   criticality.

   .. note::

      Support means that memory protection mechanisms provided by hardware
      or external software, such as an operating system, may need to be
      configured and used by the SW-platform.


.. stkh_req:: Direct Memory Access (DMA) Protection
   :id: stkh_req__safety__dma_protection
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: DMA-capable hardware may access memory independently of the CPU and may interfere with memory used by safety-related software.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support mechanisms that restrict DMA-capable
   hardware to permitted memory regions.

   .. note::

      Support means that DMA protection mechanisms provided by hardware
      or external software, such as an operating system, may need to be
      configured and used by the SW-platform.

.. stkh_req:: Shared Resource Interference Protection
   :id: stkh_req__safety__shared_resource_protection
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Software components of different criticality may share hardware resources and may interfere with each other's timing or execution behavior.
   :status: invalid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support mechanisms to control interference between
   software components of different criticality when accessing shared
   hardware resources.


.. stkh_req:: ASIL Consistency within a Process
   :id: stkh_req__safety__asil_consistency_process
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Process-level isolation does not provide freedom from interference between software components executing within the same process.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   SW-platform components executing within the same process shall satisfy
   the highest ASIL allocated to safety-related functionality within that
   process.


Fault Reaction
~~~~~~~~~~~~~~

.. stkh_req:: Safe Startup and Reset
   :id: stkh_req__safety__safe_startup_reset
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Failures during startup and reset may prevent safety-related functionality from reaching or maintaining a defined operational state.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall provide mechanisms for detecting and handling failures
   during startup and reset that may affect safety-related operation.

.. stkh_req:: External Supervision
   :id: stkh_req__safety__external_supervision
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Certain hardware or platform failures may prevent the SW-platform from detecting or reacting to failures using internal mechanisms.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall support external supervision mechanisms capable of
   detecting failures when internal supervision or fault reaction is no
   longer reliable.

   .. note::

      External supervision may be provided by mechanisms such as an external
      watchdog, voltage monitoring, or a power management integrated circuit
      (PMIC).

.. stkh_req:: Error Reporting and Propagation
   :id: stkh_req__safety__error_reporting
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related applications and supervision mechanisms require detected errors to be reported so that appropriate fault reactions can be initiated.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v2.0.0

   The SW-platform shall report detected safety-relevant errors to the
   affected application.


.. stkh_req:: Safe SW-platform state
   :id: stkh_req__safety__safe_state
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Unrecoverable platform errors require reliable notification to an external supervision mechanism that can initiate the system-specific safety reaction.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v1.0.0

   The SW-platform shall notify an external supervision mechanism when an
   unrecoverable error prevents continued safety-related operation.

   .. note::

      The system-level safe state and the corresponding safety reaction are
      defined by the integrating system. The SW-platform provides the
      information or mechanism required to trigger that reaction.

.. stkh_req:: Error Reporting Reaction Time
   :id: stkh_req__safety__error_report_timing
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Safety-related fault handling requires a bounded time between detection of an error and reporting of that error to the responsible application or supervision mechanism.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall report a detected safety-relevant error to the
   responsible application or supervision mechanism within the reaction-time
   constraint defined by the applicable safety concept or Assumption of Use.

   .. note::

      The reaction time starts when the error is detected. It does not include
      the time required by the responsible supervision mechanism to detect
      the underlying fault.

Fault Tolerance
~~~~~~~~~~~~~~~

.. stkh_req:: Redundant Software Execution
   :id: stkh_req__safety__sw_lockstep
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :rationale: Hardware faults affecting computation may lead to erroneous execution of safety-related software and may require redundant execution for fault detection or tolerance.
   :status: valid
   :version: 1
   :tags: safety_mechanism
   :valid_from: v2.0.0

   The SW-platform shall support redundant execution of safety-related
   software with mechanisms for detecting divergent execution results.

Availability
~~~~~~~~~~~~

.. stkh_req:: Availability and Recovery Support
   :id: stkh_req__dependability__availability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Applications and platform services may require continued or restored operation following recoverable failures to maintain required system availability.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support continued or restored operation of
   applications and platform services following recoverable failures.



Cybersecurity
-------------
"How does S-CORE support cybersecurity?"

The following requirements define cybersecurity properties and system
behaviors required from the SW-platform.

Cybersecurity Capability
~~~~~~~~~~~~~~~~~~~~~~~~

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

.. stkh_req:: Mandatory Access Control
   :id: stkh_req__security__mandatory_access_control
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Security-relevant platform resources and services require protection against unauthorized access and interaction between applications and processes.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall provide mandatory access control mechanisms to
   restrict access of applications and processes to platform resources
   according to defined security policies.

.. stkh_req:: Secure Access to Diagnostic Interfaces
   :id: stkh_req__diagnostics__secure_access
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Diagnostic interfaces provide access to system information and functions that may affect system operation and configuration and therefore require protection against unauthorized access.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall restrict access to security-relevant diagnostic
   functions and data to authorized entities.


Secure Communication
~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Secure Communication
   :id: stkh_req__communication__secure
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: Security-related communication requires protection against unauthorized modification, disclosure, and impersonation according to the applicable cybersecurity concept.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide mechanisms to protect the confidentiality,
   integrity, and authenticity of security-related communication as required
   by the applicable cybersecurity concept.


Platform Integrity and Hardening
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Secure Boot
   :id: stkh_req__security__secure_boot
   :reqtype: Functional
   :security: YES
   :safety: QM
   :rationale: The integrity and authenticity of software executed during platform startup need to be verified to prevent unauthorized or manipulated software from being loaded.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support verification of the authenticity and
   integrity of software before it is executed during platform startup.

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

.. stkh_req:: Short Application Cycle Support
   :id: stkh_req__performance__short_cycles
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Time-critical automotive applications require short application cycles to meet their end-to-end timing constraints.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support application cycle times below 5 ms on
   supported target configurations under defined reference conditions.


.. stkh_req:: Real-Time Execution Support
   :id: stkh_req__performance__realtime
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Time-critical applications require predictable and bounded response to timing and external events.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support execution of time-critical application
   activities and events for which explicit response-time bounds are specified.

Startup Performance
~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Startup and Resume Performance
   :id: stkh_req__performance__startup
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Automotive applications require timely availability of SW-platform functionality after system startup and resume from energy-saving states.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support bounded startup and resume times for cold
   startup and resume from supported low-power states.

Quality of Service and Resource Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Quality of Service Support
   :id: stkh_req__performance__qos
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Applications with different performance needs and criticality require controlled allocation of shared platform resources to achieve predictable runtime behavior.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support quality-of-service constraints for
   applications through controlled allocation and prioritization of
   shared platform resources, including:

   * compute resources,
   * communication resources, and
   * execution and scheduling resources.

Runtime Efficiency
~~~~~~~~~~~~~~~~~~

.. stkh_req:: Runtime Resource Efficiency
   :id: stkh_req__performance__runtime_efficiency
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Automotive target systems have constrained processing, memory, and thermal resources that must be used efficiently by the SW-platform.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support resource-efficient operation on embedded
   automotive target systems with respect to processing and memory
   utilization.

Power Efficiency
~~~~~~~~~~~~~~~~

.. stkh_req:: Low-Power Operation
   :id: stkh_req__performance__low_power
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Vehicle systems require energy-saving operating modes when full SW-platform functionality is not needed to reduce power consumption during periods of limited activity.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support controlled transitions between normal
   operation and energy-saving operating modes.


Portability and Platform Compatibility
--------------------------------------
"Where can S-CORE execute?"


Operating System Portability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: POSIX Operating System Portability
   :id: stkh_req__portability__posix
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Compliance with standardized POSIX interfaces enables portability of SW-platform components across supported operating systems.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support portability of its platform components
   across supported operating systems compliant with IEEE Std 1003.1
   (2004 Edition or newer).

   Supported operating systems are defined by:

   - :need:`stkh_req__compatibility__qnx`
   - :need:`stkh_req__compatibility__linux`


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

.. stkh_req:: ARM64 and x86-64 Architecture Support
   :id: stkh_req__compatibility__processor_arch
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Support for multiple processor architectures enables deployment of the SW-platform across automotive target and development hardware environments.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support deployment and operation on ARM64 and
   x86-64 processor architectures.


.. stkh_req:: Hardware Accelerator Support
   :id: stkh_req__compatibility__hw_acceleration
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Hardware accelerator support enables compute-intensive applications to use target-specific acceleration capabilities to meet performance and resource-efficiency needs.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall enable applications to utilize available hardware
   accelerators for compute-intensive workloads.


Virtualized and Containerized Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Virtualized Execution for Development and Testing
   :id: stkh_req__compatibility__virt_exec
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Virtualized execution, such as through QEMU, enables development, automated testing, debugging, and continuous integration without requiring physical target hardware.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support execution in virtualized environments
   for development and testing.


.. stkh_req:: Containerized Application Execution
   :id: stkh_req__compatibility__container_exec
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Containerized execution enables portable application deployment, isolation, and lifecycle management across supported platform environments.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support deployment and execution of applications
   using containerization mechanisms.



Platform Lifecycle, Integration & Maintainability
-------------------------------------------------
"How can S-CORE evolve and integrate?"


API Compatibility & Standardization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Managed Application APIs
   :id: stkh_req__compatibility__managed_app_apis
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: A defined API lifecycle enables predictable evolution of application-facing APIs and supports long-term reuse of application software.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall manage application-facing APIs according to a
   defined lifecycle covering their introduction, evolution, deprecation,
   and removal.


.. stkh_req:: Support for Standardized Interfaces
   :id: stkh_req__compatibility__standard_interface
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Use of established standards promotes interoperability and integration with external software ecosystems while reducing dependency on proprietary interfaces.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support established standards for externally
   visible interfaces and communication protocols where applicable
   standards exist for the required functionality.


.. stkh_req:: Stable Application Interfaces
   :id: stkh_req__compatibility__stable_app_interface
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Stable application-facing interfaces reduce migration effort and enable applications to remain compatible across SW-platform releases.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall maintain compatibility of application-facing
   interfaces across releases or provide a defined migration path when
   incompatible changes are required.


Integration
~~~~~~~~~~~

.. stkh_req:: Multi-Repository Integration
   :id: stkh_req__integration__multi_repo
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Independent development of SW-platform modules requires coordinated integration and validation across multiple source-code repositories.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support integration and validation of independently
   developed modules from multiple source-code repositories as a consistent
   SW-platform.

Configuration and Evolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Variant Management
   :id:  stkh_req__configuration__variant_management
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Vehicle programs require controlled management of software variants across different vehicle configurations and SW-platform releases.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support definition, configuration, and management
   of software variants and their compatibility across vehicle configurations
   and SW-platform releases.


Engineering Lifecycle
~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Assumptions and Design Decision Documentation
   :id: stkh_req__eng__assumptions_and_decisions
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Documenting relevant assumptions and design decisions preserves engineering rationale and supports review, maintainability, and architectural evolution.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform engineering process shall ensure that relevant assumptions
   and design decisions are documented, maintained, and traceable to the
   affected engineering artifacts.


.. stkh_req:: Requirements Traceability
   :id: stkh_req__requirements__traceability
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Bidirectional requirements traceability enables demonstration of requirements decomposition, coverage, and consistency throughout the requirements hierarchy.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform engineering infrastructure shall provide bidirectional
   traceability between stakeholder requirements and their derived
   requirements across all requirements levels.


.. stkh_req:: Requirements as Code
   :id: stkh_req__requirements__as_code
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Managing requirements as version-controlled source files enables collaborative review, reproducible change tracking, automation, and integration with the software engineering workflow.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform engineering infrastructure shall manage requirements as
   version-controlled source files integrated with the software engineering
   workflow.

Cooperation and Intellectual Property
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Intellectual Property Protection
   :id: stkh_req__cooperation__ip_protection
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Cooperation between organizations requires integration of proprietary applications without requiring disclosure of their implementation details or intellectual property.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall enable integration and deployment of proprietary
   applications without requiring disclosure of their implementation details
   to other platform participants.


Developer Experience and Testability
------------------------------------
"How can developers build, observe, debug and test with it?"

Development
~~~~~~~~~~~

.. stkh_req:: Interface Definition Language Support
   :id: stkh_req__dev__idl_support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: A human-readable interface definition language enables implementation-independent interface specification and automated generation of integration artifacts for supported programming languages.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide a human-readable interface definition
   language and support automated generation of the required integration
   artifacts for supported programming languages.

.. stkh_req:: Development Toolchain Support
   :id: stkh_req__dev__toolchain
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Integrated development tooling enables efficient implementation, build, deployment, debugging, testing, and continuous integration of SW-platform components and applications.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide development toolchain support for
   platform and application development.

   The development toolchain shall support:

   * IDE integration for all supported programming languages.
   * Editing of interface definitions with syntax highlighting and validation.
   * Deployment and debugging on virtualized and physical target environments.
   * Integration with continuous integration and deployment systems.

.. stkh_req:: Programming Language Support
   :id: stkh_req__dev__programming_languages
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Support for C++ and Rust enables application development using programming languages suitable for performance-critical and safety-related automotive software.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support application development using the following
   programming languages:

   * C++
   * Rust

   The SW-platform development environment shall support the use of these
   programming languages for applications developed up to the highest ASIL
   level supported by the SW-platform as defined in
   :need:`stkh_req__safety__asil_b_support`.

Debugging
~~~~~~~~~

.. stkh_req:: Target Debugging Support
   :id: stkh_req__dev__debugging
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Target debugging enables developers to analyze and diagnose software behavior during integration, testing, and in-vehicle operation.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support target debugging during in-vehicle operation
   when enabled by the applicable operational mode.

Observability and Tracing
~~~~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Execution Tracing
   :id: stkh_req__observability__exec_tracing
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Execution tracing enables analysis of runtime behavior, scheduling, timing, and resource utilization across heterogeneous computation units.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support tracing of execution events required to
   reconstruct the temporal execution behavior of software entities and
   execution contexts across supported computation units, including:

   * CPU
   * GPU
   * Neural processing units
   * Image processing units

.. stkh_req:: Communication Tracing
   :id: stkh_req__observability__com_tracing
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Communication tracing enables analysis of message flow, timing, and communication behavior across internal and external communication paths.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall support tracing of communication events across
   internal and external communication paths.


.. stkh_req:: Memory Tracing
   :id: stkh_req__observability__memory_tracing
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Memory tracing enables analysis of memory usage, data movement, and resource behavior across supported memory domains.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support tracing of memory-related events across
   supported memory domains, including allocation, deallocation, and
   data transfer.

.. stkh_req:: AI Workload Observability
   :id: stkh_req__observability__ai_workloads
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Observability of AI workload performance and resource utilization enables detection and analysis of runtime degradation during development and in-field operation.
   :status: valid
   :version: 1
   :tags: artificial_intelligence
   :valid_from: v2.0.0

   The SW-platform shall expose performance and resource-utilization
   information of AI workloads, including inference latency and resource
   consumption, through the platform observability mechanisms during
   development and in-field operation.

Testing and Simulation
~~~~~~~~~~~~~~~~~~~~~~

.. stkh_req:: Mockable Platform Interfaces
   :id: stkh_req__test__mockable_interfaces
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Mockable platform interfaces enable isolated unit, component, and integration testing of applications without requiring the complete SW-platform runtime environment.
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The SW-platform shall enable its application-facing interfaces to be
   mocked for unit, component, and integration testing of applications.


.. stkh_req:: Reprocessing and Simulation Support
   :id: stkh_req__test__reprocessing
   :reqtype: Functional
   :security: NO
   :safety: QM
   :rationale: Recording and replaying runtime data enables reproducible testing, simulation, and analysis of application and SW-platform behavior.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall support recording of runtime data and subsequent
   injection of recorded or modified data for reprocessing, testing, and
   simulation.

Analysis
~~~~~~~~

.. stkh_req:: Performance Analysis
   :id: stkh_req__analysis__performance
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Performance analysis enables identification of resource bottlenecks and long-term performance trends in SW-platform components and applications.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide runtime information required to analyze
   the performance and resource utilization of SW-platform components
   and applications over time, including:

   * CPU utilization and execution behavior
   * Memory utilization and consumption


.. stkh_req:: Timing Analysis
   :id: stkh_req__analysis__timing
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :rationale: Timing analysis enables verification that SW-platform components and applications meet their defined timing requirements under representative runtime conditions.
   :status: valid
   :version: 1
   :valid_from: v2.0.0

   The SW-platform shall provide runtime information required to analyze
   and assess the timing behavior of SW-platform components and applications
   against defined timing requirements.
