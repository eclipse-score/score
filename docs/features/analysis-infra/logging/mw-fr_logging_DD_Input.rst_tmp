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

This document includes the detailed design findings from the feature request review.

Logging
#######

Specification
=============
Context
-------
.. related feature from feature request
- Supported programming languages: C++, Rust, Python (e.g. for tests)

.. detailed design finding
For Rust, we would like to be able to use the log crate. It provides an (allocation-free) facade without forcing a specific logger implementation. Advantages of using this facade:

We stay with language best-practices.
New contributors directly feel at home with the logging.
Any library dependency which we might use probably logs against this facade. So we would get logs of dependencies for free by using it as well and implementing a logger for the facade.
There might be comparable defacto standards for C++ and Python.


Resource consumption
--------------------
.. related feature from feature request
- Runtime ressources
- Low impact on overall performance ---> QoS for handling overflows/dropping log messages

.. detailed design finding
Ideally, in a language like Rust, logging messages should be possible without allocations for individual logs.
Using the defacto standard log crate as facade, implementors of this facade should not allocate to write / forward log messages.
