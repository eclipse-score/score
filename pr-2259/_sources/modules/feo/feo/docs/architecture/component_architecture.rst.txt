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

.. document:: FEO Component Architecture
   :id: doc__component_feo_architecture
   :status: draft
   :security: NO
   :safety: ASIL_B
   :realizes: wp__component_arch
   :tags: component_feo

FEO Component Architecture
==========================

Overview
--------
The current implementation of the feature "FEO" (Fixed Execution Order Framework) consists of a main
component (called "FEO" component) and a set of auxiliary components that will be either replaced by or
turned into wrappers to components from other S-CORE features. In the latter case, these wrappers will
possibly become sub-components of the main component.

This document describes the architecture of the main component "FEO".

Description
-----------

Sub-Components
**************

The main component "FEO" consists of the following sub-components:

* feo: Implements activities, threads, agents, and scheduling
* feo-cpp-build: C++ and Rust Code simplifying the integration of C++ components
* feo-cpp-macros: Rust proc-macros simplifying the integration of C++ components.

Rust requires proc-macros to reside in their own crate, therefore the latter two
sub-components cannot easily be combined into a single one.


Rationale Behind Architecture Decomposition
*******************************************

The main component "FEO" has been split into three sub-components mainly according to usability
considerations and Rust compiler constraints. (Rust proc-macros must reside in their own crate.)


Static Architecture
-------------------

.. comp_arc_sta:: Static Architecture
  :id: comp_arc_sta__feo__main
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: comp_req__feo__application, comp_req__feo__scheduler, comp_req__feo__task_chain, comp_req__feo__agent, comp_req__feo__comp_cfg, comp_req__feo__act_map_cfg


  .. uml:: _assets/stat_arch.puml
     :scale: 50
     :align: center


Dynamic Architecture
--------------------

.. comp_arc_dyn:: Dynamic Architecture
  :id: comp_arc_dyn__feo__main
  :security: YES
  :safety: ASIL_B
  :fulfils: comp_req__feo__application, comp_req__feo__application_lifecycle, comp_req__feo__scheduler, comp_req__feo__task_chain, comp_req__feo__agent, comp_req__feo__activity_init, comp_req__feo__activitiy_step, comp_req__feo__activity_shutdown
  :status: valid

  The actual dynamic call sequence during the execution of a FEO application depends on the distribution
  of activities to processes as well as on the activity dependency graph defining the task chain.
  As an example, we consider the simple task chain and process distribution depicted in the following diagram

  .. uml:: _assets/act_chain.puml

  For this task chain, a possible call sequence is shown below.

  .. uml:: _assets/dyn_arch.puml
     :scale: 50
     :align: center


Interfaces
----------

.. real_arc_int:: feo::agent::PrimaryConfig
  :id: real_arc_int__feo__primary_config
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: comp_req__feo__application, comp_req__feo__task_chain, comp_req__feo__comp_cfg, comp_req__feo__act_map_cfg
  :language: rust

  See static architecture.


.. real_arc_int:: feo::agent::Primary
  :id: real_arc_int__feo__primary
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: comp_req__feo__application, comp_req__feo__task_chain, comp_req__feo__comp_cfg, comp_req__feo__act_map_cfg
  :language: rust

  See static architecture.


.. real_arc_int:: feo::agent::SecondaryConfig
  :id: real_arc_int__feo__secondary_config
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: comp_req__feo__application, comp_req__feo__task_chain, comp_req__feo__comp_cfg, comp_req__feo__act_map_cfg
  :language: rust

  See static architecture.


.. real_arc_int:: feo::agent::Secondary
  :id: real_arc_int__feo__secondary
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: comp_req__feo__application, comp_req__feo__task_chain, comp_req__feo__comp_cfg, comp_req__feo__act_map_cfg
  :language: rust

  See static architecture.


.. real_arc_int:: feo::activity::Activity
  :id: real_arc_int__feo__activity
  :security: YES
  :safety: ASIL_B
  :status: valid
  :fulfils: comp_req__feo__activity
  :language: rust

  See static architecture.

.. needextend:: docname is not None and "feo/docs/architecture" in docname
   :+tags: component_feo
