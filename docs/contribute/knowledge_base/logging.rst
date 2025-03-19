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

Logging
#######

Log Level Guidelines
====================

Logging is a critical part of both application development and maintenance. A well-defined log level structure helps separate the concerns of developers and end users, ensuring that relevant information is communicated at the right level of detail.

Developer-Oriented Log Levels
-----------------------------

- **TRACE**
  Used for logging detailed application events, such as when a resource is created or destroyed.
  *Example:* Logging the creation of a new object instance.

- **DEBUG**
  Used for debugging purposes, particularly when a function returns a result (e.g., ``Result`` in Rust or an ``expected`` in C++) that contains an error.
  *Example:* Logging unexpected errors during function execution to help diagnose issues.

User-Oriented Log Levels
------------------------

- **INFO**
  Provides general information about the application's operations that may be of interest to the user.
  *Example:* Notifying the user of a successful operation or process completion.

- **WARN**
  Indicates warnings for the user when internal recoverable misbehaviors occur, but the application's functionality is not severely restricted.
  *Example:* Logging minor issues that could lead to future problems but are currently being handled gracefully.

- **ERROR**
  Signals severe failures that are still recoverable, meaning the error is contained within a result (e.g., ``Result`` in Rust or an ``expected`` in C++) and the application can continue if the user takes corrective action.
  *Example:* Logging errors that require user intervention to recover from a malfunction.

- **FATAL**
  Indicates critical failures where the application will terminate (panic) after the log output.
  *Example:* Logging a critical error that forces the application to shut down immediately.
