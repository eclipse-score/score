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

Feature Architecture: FEO
=========================

Overview
--------
The current implementation of the feature "FEO" (Fixed Execution Order Framework) consists of a main
component and a set of auxiliary components that will be either replaced by or turned into
wrappers to components from other Score features. In the latter case, these wrappers will possibly
become sub-components of the main component.

In addition, the implementation comes with a few utility and example applications for demonstrating
its functionality that do not belong to the feature itself and might become obsolete or be
moved to another place in the project space.

Description
-----------

Feature Components
******************

* feo: The main component

    Consists of the following sub-components:

    - feo: Implements activities, threads, agents, and scheduling
    - feo-cpp-build: C++ and Rust Code simplifying the integration of C++ components
    - feo-cpp-macros: Rust proc-macros simplifying the integration of C++ components.

    Rust requires proc-macros to reside in their own crate, therefore the latter two
    sub-components cannot easily be combined into a single one.

* feo-com: Backends for inter-activity data communication

    Will be replaced by or become a wrapper of the interface `mw::com` provided by the feature
    "Communication".

* feo-log: Logging macros (Rust and C++) and logger implementation

    Consists of the following sub-components:

    - feo-log: Logging macros (Rust and C++)
    - feo-logger: Logger implementation (Rust and C++)

    Will be replaced by or become a wrapper of an interface provided by the feature "Logging".

* feo-time: Interface to system clocks

    Will be replaced by or become a wrapper of an interface provided by the feature "Time".

* feo-tracing: Subscriber for Rust tracing API

    Will be replaced by or become a wrapper of an interface provided by the feature "Logging".


Utility and Example Applications
********************************

* feo-tracer: A simple tracing daemon receiving trace messages from all feo agents

    Consists of the following sub-components:

    - feo-tracer: Tracing daemon
    - perfetto-model: Support for the Perfetto trace file format

    Will be replaced by an alternative solution provided by the feature "Tracing".

* logd: A simple logging daemon receiving log output from all feo agents

    Will be replaced by an alternative solution provided by the feature "Logging".

* mini-adas: Example of a minimal dummy ADAS activity set

* cycle-benchmark: A simple configurable benchmarking application to measure the FEO cycle time


Rationale Behind Architecture Decomposition
*******************************************

The feature has been split into a main component, auxiliary components as well as utility and
example applications. The main component implements the functionality that is expected to
be required by most systems making use of FEO. Auxiliary components are parts of the code
that are likely to be replaced by components from other features in the future. They have been
split according to their functionality and/or well-known APIs. Utility applications are optional
pieces of software that can be run to test or demonstrate the feature functionality but are not
expected to be used directly in a productive system. They may become obsolete in future.

The main component has been split into three sub-components mainly according to usability
considerations and Rust compiler constraints. (Rust proc-macros must reside in their own crate.)


Static Architecture
-------------------

.. feat_arc_sta:: Static Architecture
  :id: feat_arc_sta__feo__main
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: feat_req__feo__application, feat_req__feo__activity, feat_req__feo__task_chain, feat_req__feo__agent
  :includes: logic_arc_int__feo__logic_int

  .. uml:: _assets/stat_arch.puml
     :scale: 50
     :align: center


Dynamic Architecture
--------------------

.. feat_arc_dyn:: Dynamic Architecture
  :id: feat_arc_dyn__feo__main
  :security: YES
  :safety: ASIL_B
  :fulfils: feat_req__feo__application, feat_req__feo__activity, feat_req__feo__task_chain, feat_req__feo__agent
  :status: valid

  .. uml:: _assets/dyn_arch.puml
     :scale: 50
     :align: center


Logical Interfaces
------------------

.. logic_arc_int:: Logical Interface
  :id: logic_arc_int__feo__logic_int
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: feat_req__feo__application, feat_req__feo__activity, feat_req__feo__task_chain, feat_req__feo__agent

  See static architecture.
