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

Log and Trace
#############

.. document:: doc__logging
   :id: doc__logging
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :tags: feature_request
   :realizes: wp__feat_request[version==1]


Feature flag
============

To activate logging, use the following feature flag:

``experimental_logging``

Abstract
========

This feature request proposes the development of a safe, efficient and robust logging and tracing framework within S-CORE.


Motivation
==========

A common logging and tracing feature is needed to support debugging and analysis
of platform components and applications.

Rationale
=========

Logging provides the possibility to understand the running system by capturing detailed information about system
events and application-level activities.

Specification
=============

The :doc:`feature requirements <requirements/index>` specify functionality,
configuration, error handling, resource consumption, compatibility, security,
and safety.

The :doc:`feature architecture <architecture/index>` describes the logging and
tracing interfaces. Terms are defined in the :doc:`glossary <glossary>`.

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

Logging records messages about application and system activity, including:

- state changes
- informational messages
- warnings
- errors

When logging from a library, it shall be possible to easily associate the logs to the library. A solution could be to provide contexts.

Tracing
-------

Example - User need to correlate kernel traces to user traces for debugging , analyzing etc
Follow the control flow (on function call basis) of the application.

Recompute
---------

All data to recompute a module (Input, Output, States)


.. toctree::
   :maxdepth: 1

   requirements/index
   requirements/chklst_req_inspection
   architecture/index
   glossary.rst
