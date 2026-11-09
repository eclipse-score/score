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

.. document:: Log and Trace
   :id: doc__log_and_trace
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

Logging and tracing help developers understand the running system by capturing
information about system events and application-level activities.

Specification
=============

The :doc:`feature requirements <requirements/index>` specify functionality,
configuration, error handling, resource consumption, compatibility, security,
and safety.

The :doc:`feature architecture <architecture/index>` describes the logging and
tracing interfaces. Terms are defined in the :doc:`glossary <glossary>`.

Backwards Compatibility
=======================

Existing requirement and interface IDs are retained. The previously published
Bazel label for the logging requirements remains available as an alias to the
moved requirements file.

Security Impact
===============

- only authorized users should be able to access the log files

Safety Impact
=============

- Logging output is QM only and must not be used as the basis for safety decisions.
- The ASIL B scope of the logging framework concerns freedom from interference
   with the calling application, not the safety integrity of the log output.

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

The :term:`logging entity identifier` associates a log entry with its application
and context. For a shared library, this identifies both the emitting application
and the library context; the library name alone does not identify the application.

Tracing
-------

Tracing captures execution events and data for analysis. For example, developers
can correlate kernel and user-space traces or follow application control flow
at function-call granularity.

Recompute
---------

Captured data can be an input to offline analysis. This feature does not provide
a recompute or replay framework.


.. toctree::
   :maxdepth: 1

   requirements/index
   requirements/chklst_req_inspection
   architecture/index
   glossary.rst
