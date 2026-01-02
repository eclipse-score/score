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

Feature Request
###############

.. document:: doc__logging
   :id: doc__logging
   :status: draft
   :safety: ASIL_B
   :tags: feature_request


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_logging``

Abstract
========

This feature request proposes the development of a safe, efficient and robust logging framework within S-CORE.


Motivation
==========

- currently no solution available in the score platform

Rationale
=========

Logging provides the possibility to understand the running system by capturing detailed information about system
events and application-level activities.

Specification
=============

[Describe the requirements, architecture of any new feature.] [or]
[Describe the change to requirements, architecture, implementation, process, documentation, infrastructure of any change request.]

Functionality
-------------

Logging has to support the following features:

- Timestamping

  - local timestamp for each log entry
  - original timestamp for routed log entries
  - timestamp synchronization for log entries coming from different logging nodes-

- Log severity levels
- Log prioritization in case of resource conflicts
- logging of early startup events
- Log filtering

  - Support application and context identifier like in DLT
  - Filtering by log levels for components and application level
  - Out of scope "time" (tooling topic)
  - logs filtering by logging entity ID (e.g., ECU ID, Application ID, Context ID such as in DLT)
  - logs filtering by log level (e.g., FATAL, ERROR, WARN, INFO, DEBUG, VERBOSE such as in DLT)

  .. - Filtering options: it should have filter on app id and more fine-tuned filters on context ids.

- message loss detection

  - optional functionality for logging. Important for tracing.
  - Message loss detection

    - The logging framework must detect and report any message loss.
    - It should provide mechanisms to handle message loss gracefully, such as buffering or prioritizing critical messages.
    - The log consumer must be informed about any message loss to ensure the trustworthiness of the logs.
  - would become mandatory in case verification is done via logging feature (not recommended)

- Context specific log level activation at runtime

Log Sources
-----------

- user application
- component features & platform

Log Sinks
---------
- log sinks shall be transparent to the application (e.g. by a facade )
- console
- File system

  - local
  - external mounted PCIe Drive
  - Cloud native drive via network

- Network (incl. second dedicated Ethernet Channel)
- Logs shall appear on stdout when running unit tests

Configuration
-------------

- Log level
- Log Sinks

  - Log storage device
  - Log storage strategy (e.g., on system shutdown, on each message, on demand, on file size, on cache size, with circular or linear buffer)

- Buffer size
- Storage size (e.g. storage size of log files)
- Permission settings
- log filter
- Logging entity ID (e.g., ECU ID, Application ID, Context ID such as in DLT)
- On-demand functionality (e.g., enable / disable the log storage)
- Provide fallback configs. E.g.: App, System-wide

- Possibility to provide an extension for custom types

Error handling
--------------

- reboot/reset
- On logging errors, the framework should continue if recoverable; otherwise, deactivate silently and set an error state reported on shutdown.
- The user application should not be affected by logging framework errors.

Context
-------

- Supported operating system: QNX, Linux (encapsulation via OSAL)
- Supported programming languages: C++, Rust, Python (e.g. for tests)

Resource consumption
--------------------

- Storage
- Communication Channel
- Runtime resources
- Low impact on overall performance ---> QoS for handling overflows/dropping log messages

Norms/Standards
---------------
The logging framework should be compatible with the Diagnostic Log and Trace (DLT) protocol. This includes:

- Support for DLT message format
- Ability to send and receive DLT messages
- Integration with existing DLT tools and infrastructure

Backwards Compatibility
=======================
\-

Security Impact
===============

- only authorized users should be able to access the log files

Safety Impact
=============

- The interface should support the ASIL level of the user function.
- Dependent on the Safety concept of the over all system, the logging should be classified accordingly.
  That could be the case if the logging information are part of the verification strategy..

License Impact
==============

- not known

How to Teach This
=================

How to Use: Logging Guideline


Definitions
===========

Logging
-------

Write out some message
General progress description (incl. Context)
- state changes
- Infos
- errors

When logging from a library, it shall be possible to easily associate the logs to the library. A solution could be to provide contexts.

Tracing
-------

Example - User need to correlate kernel traces to user traces for debugging , analyzing etc
Follow the control flow (on function call basis)of the application.

Recompute
---------

All data to recompute a module (Input, Output, States)
