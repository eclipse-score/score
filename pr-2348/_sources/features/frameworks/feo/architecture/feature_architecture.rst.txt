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

.. document:: FEO Feature Architecture
   :id: doc__frameworks_feo_feat_arch
   :status: valid
   :security: NO
   :safety: ASIL_B
   :realizes: wp__feature_arch


FEO Feature Architecture
========================

Overview
--------
The current implementation of the feature "FEO" (Fixed Execution Order Framework) consists of a main
component and a set of auxiliary components that will be either replaced by or turned into
wrappers to components from other S-CORE features. In the latter case, these wrappers will possibly
become sub-components of the main component.

Description
-----------

Feature Components
******************

* feo: The main component

* feo_com: Interface to inter-activity data communication

  Will be replaced by or become a wrapper of the interface `mw::com` provided by the feature
  "Communication".

* feo_log: Logging macros (Rust and C++) and logger implementation

  Consists of the following sub-components:
  - feo_log: Logging macros (Rust and C++)
  - feo_logger: Logger implementation (Rust and C++)

  Will be replaced by or become a wrapper of an interface provided by the feature "Logging".

* feo_time: Interface to system clocks

  Will be replaced by or become a wrapper of an interface provided by the feature "Time".

* feo_tracing: Subscriber for Rust tracing API

  Will be replaced by or become a wrapper of an interface provided by the feature "Logging".


Utility and Example Applications
********************************

* feo_tracer: A simple tracing daemon receiving trace messages from all feo agents

  Consists of the following sub-components:
  - feo_tracer: Tracing daemon
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
split according to their functionalities. Utility applications are optional
pieces of software that can be run to test or demonstrate the feature functionality but are not
expected to be used directly in a productive system. They may become obsolete in future.


Static Architecture
-------------------

.. feat_arc_sta:: Static Architecture
  :id: feat_arc_sta__feo__main
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: feat_req__feo__application, feat_req__feo__activity, feat_req__feo__task_chain, feat_req__feo__agent
  :includes: logic_arc_int__feo__activity, logic_arc_int__feo__prim_agent, logic_arc_int__feo__sec_agent, logic_arc_int__feo__lifecycle

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

.. logic_arc_int:: Activity
  :id: logic_arc_int__feo__activity
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: feat_req__feo__application, feat_req__feo__activity

  See static architecture.


.. logic_arc_int:: Primary Agent
  :id: logic_arc_int__feo__prim_agent
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: feat_req__feo__application, feat_req__feo__activity, feat_req__feo__task_chain, feat_req__feo__agent

  See static architecture.


.. logic_arc_int:: Secondary Agent
  :id: logic_arc_int__feo__sec_agent
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: feat_req__feo__application, feat_req__feo__activity, feat_req__feo__task_chain, feat_req__feo__agent

  See static architecture.


.. logic_arc_int:: Lifecycle Listener
  :id: logic_arc_int__feo__lifecycle
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: feat_req__feo__application_lifecycle

  See static architecture.

.. needextend:: docname is not None and "frameworks/feo/architecture" in docname
   :+tags: frameworks_feo
