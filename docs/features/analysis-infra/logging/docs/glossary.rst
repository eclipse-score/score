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

Glossary
########
.. glossary::

   logging node
      ECU or Partition (real or virtual) which generates log messages

   DLT
      Diagnostic Log and Trace

   framework
      Framework is a structured and extensible foundation for developing specific types of functionality in this case, logging. It supplies a set of default behaviors and configurable options, allowing developers to tailor and extend its capabilities to meet their application and system need.

   platform
      Platform is the execution environment on which S-Core runs. It includes, for example, hardware (HW), operating system (OS), ...

   component
      Component is a S-Core component

   log level
      Log Level is the severity of a log message, necessary to categorize logs based on their importance e.g., FATAL, ERROR, WARN, INFO, DEBUG, VERBOSE such as in DLT

   logging entity
      SW entity which generates log messages

   logging entity identifier
      unique identifier for the logging entity, e.g., ECU ID / application ID / context ID, similar to DLT.

   log storage strategy
      strategy to write/sync the cached log messages in the log storage location e.g., on system shutdown, on each message, on demand, on file size, on cache size, with circular or linear buffer

   QoS
      Quality of Service
