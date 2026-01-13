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



Requirements
############



.. feat_req:: Timestamping - Local Timestamp
   :id: feat_req__logging__timestamping_local
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support local timestamps for each log entry.

.. feat_req:: Timestamping - Original Timestamp
   :id: feat_req__logging__timestamping_original
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support original timestamps for routed log entries.

.. feat_req:: Timestamping - Timestamp Synchronization
   :id: feat_req__logging__timestamping_sync
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support timestamp synchronization for log entries coming from different :term:`logging nodes <logging node>`.

.. feat_req:: Log Severity Levels
   :id: feat_req__logging__severity_levels
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging framework shall support a log level for each log entry.

.. feat_req:: Log Prioritization
   :id: feat_req__logging__prioritization
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging framework shall prioritize logs in case of resource conflicts to ensure critical logs are not lost.

.. feat_req:: Logging of Early Startup Events
   :id: feat_req__logging__early_startup
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support logging of early startup events to capture critical initialization information.

.. feat_req:: Log entity Identifier
   :id: feat_req__logging__entity_identifier
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support :term:`logging entity identifiers<logging entity identifier>` for each log entry.

.. feat_req:: Log Filtering - Log Levels
   :id: feat_req__logging__filtering_log_levels
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support filtering by :term:`log levels <Log level>`.

.. feat_req:: Log Filtering - Logging Entity ID
   :id: feat_req__logging__filtering_entity_id
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support filtering by :term:`logging entity identifiers<logging entity identifier>`.

.. feat_req:: Message Loss Detection - Detection and Reporting
   :id: feat_req__logging__message_loss_detection
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall detect and report any message loss.

.. feat_req:: Message Loss Detection - Graceful Handling
   :id: feat_req__logging__message_loss_handling
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall provide mechanisms to handle message loss gracefully.

   Additional Information: e.g. buffering or prioritizing critical messages

.. feat_req:: Context-Specific Log Level Activation
   :id: feat_req__logging__context_log_level
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall allow context-specific :term:`log level` activation at runtime to enable fine-grained control over logging behavior.

.. feat_req:: Log Sources - User Application
   :id: feat_req__logging__log_sources_user_app
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support user application as log source.

.. feat_req:: Log Sources - Component and Platform
   :id: feat_req__logging__log_sources
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support :term:`component` features and :term:` platform` as log sources.

.. feat_req:: Log Sinks - Console
   :id: feat_req__logging__log_sinks_console
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support console as a log sink.

.. feat_req:: Log Sinks - Local File System
   :id: feat_req__logging__log_sinks_local_fs
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support local file system as log sink.



.. feat_req:: Log Sinks - Cloud Native Drive
   :id: feat_req__logging__log_sinks_cloud_drive
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support cloud-native drives via network as log sinks.

.. feat_req:: Log Sinks - Network
   :id: feat_req__logging__log_sinks_network
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support network channels, including a second dedicated Ethernet channel, as log sinks.

.. feat_req:: Log Sinks - Stdout for Unit Tests
   :id: feat_req__logging__log_sinks_stdout
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall ensure logs appear on stdout when running unit tests.

.. feat_req:: Previous boot logging
   :id: feat_req__logging__boot_logging
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__boot_logging
   :status: valid

   The logging :term:`framework` shall support logging of data to memory which survives a reboot
   cycle.

.. feat_req:: Configuration - Log Level
   :id: feat_req__logging__config_log_level
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support configuration of :term:`log levels <Log level>`.

.. feat_req:: Log Sinks - Storage Device
   :id: feat_req__logging__sink_device
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support configuration of the log storage device.

.. feat_req:: Log Sinks - multiple Storage Device
   :id: feat_req__logging__sink_multiple_device
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support multiple log storage devices.

.. feat_req:: Log Sinks - Storage Strategy
   :id: feat_req__logging__sink_strategy
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support configurable :term:`log storage strategy`.

.. feat_req:: Configuration - Buffer Size
   :id: feat_req__logging__config_buffer_size
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall allow configuration of internal buffers sizes.

.. feat_req:: Configuration - Storage Size
   :id: feat_req__logging__config_storage_size
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall allow configuration of storage size per log file.

.. feat_req:: Configuration - Permission Settings
   :id: feat_req__logging__config_permissions
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall allow configuration of permission settings for log access.

.. feat_req:: Configuration - Log Filter
   :id: feat_req__logging__config_log_filter
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall allow configuration of log filters.

.. feat_req:: Configuration - Logging Entity ID
   :id: feat_req__logging__config_entity_id
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall allow configuration of logging entity IDs.

.. feat_req:: Configuration - On-Demand Functionality
   :id: feat_req__logging__config_on_demand
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support on-demand functionality, such as enabling or disabling log storage.

.. feat_req:: Configuration - Fallback Configurations
   :id: feat_req__logging__config_fallback
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall provide fallback configurations, such as application-wide or system-wide defaults.

.. feat_req:: Configuration - Custom Types Extension
   :id: feat_req__logging__config_custom_types
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall allow extensions for custom log types.

.. feat_req:: Error Handling - Recoverable Errors
   :id: feat_req__logging__error_handling_recoverable
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   In case of recoverable error, the logging :term:`framework` shall continue the current operations.

.. feat_req:: Error Handling - Non-Recoverable Errors
   :id: feat_req__log__err_handling_nonrec
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   In case of non-recoverable error, the logging :term:`framework` shall deactivate silently and set an error state reported on shutdown.

.. feat_req:: Error Handling - Application Isolation
   :id: feat_req__logging__error_handling_isolation
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall ensure that user applications are not affected by logging :term:`framework` errors.

.. feat_req:: Compatibility - Supported Operating Systems
   :id: feat_req__logging__compat_os
   :reqtype: Interface
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall support QNX and Linux operating systems (encapsulated via OSAL).

.. feat_req:: Compatibility - Supported Programming Languages
   :id: feat_req__logging__compat_languages
   :reqtype: Interface
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support, stkh_req__dev_experience__prog_languages
   :status: valid

   The logging :term:`framework` shall support C++, Rust, and Python programming languages.

.. feat_req:: Resource Consumption - Storage
   :id: feat_req__logging__resource_storage
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall minimize storage resource consumption.

.. feat_req:: Resource Consumption - Communication Channel
   :id: feat_req__logging__resource_comm_channel
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall minimize communication channel resource consumption.

.. feat_req:: Resource Consumption - Runtime Resources
   :id: feat_req__logging__resource_runtime
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall minimize runtime resource consumption.

.. feat_req:: Resource Consumption - Performance Impact
   :id: feat_req__logging__resource_performance
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall have low impact on overall system performance.

.. feat_req:: Quality of Service - Message Handling
   :id: feat_req__logging__qos_message_handling
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall provide:term:` QoS` for handling overflows or dropping log messages.
.. ist "rovide QoS for handling overflows or dropping log messages." doppelt zu den loos detection req.?

.. feat_req:: Compatibility - DLT Protocol
   :id: feat_req__logging__compat_dlt
   :reqtype: Interface
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support, stkh_req__overall_goals__enable_cooperation
   :status: valid

   The logging :term:`framework` shall be :term:`DLT` compatible.

   Additional Information: support for DLT message format, sending and receiving DLT messages, and integration with existing DLT tools and infrastructure.

.. feat_req:: Security - Log File Access
   :id: feat_req__logging__security_log_access
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support, stkh_req__dependability__security_features
   :status: valid

   The logging :term:`framework` shall ensure that only authorized users can access log files.

.. feat_req:: Safety - ASIL Level Support
   :id: feat_req__logging__asil_support
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__safe_comput
   :status: valid

   The logging :term:`framework` shall support the ASIL level of the user function to ensure compliance with the safety requirements of the application.

   Additional Information: Freedom from interfernce must be guaranteed with regard to the calling components.

.. feat_req:: Safety - System Classification
   :id: feat_req__logging__system_class
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   The logging :term:`framework` shall be classified according to the overall system's safety concept if logging information is part of the verification strategy.
