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

Launch Manager Configuration
############################

The :term:`Launch Manager` supports a set of configuration parameters, which are grouped in the following categories:

Component Configuration Parameters
==================================

These parameters specify the arguments needed for spawning a process.

- :need:`feat_req__lifecycle__uid_gid_support`
- :need:`feat_req__lifecycle__supplementary_groups`
- :need:`feat_req__lifecycle__runmask_support`
- :need:`feat_req__lifecycle__launch_priority_support`
- :need:`feat_req__lifecycle__cwd_support`
- :need:`feat_req__lifecycle__process_launch_args`
- :need:`feat_req__lifecycle__std_handle_redir`
- :need:`feat_req__lifecycle__aslr_support`
- :need:`feat_req__lifecycle__process_rlimit_support`
- :need:`feat_req__lifecycle__support_secpol_type`

Dependency parameters
=====================

These parameters specify how the components depend on each other.

Recovery parameters
===================

These parameters specify the recovery actions for a component, when it fails.

Alive monitoring parameters
===========================

These parameters specify the alive monitoring rules for the application.

Requirements related to the external monitoring
===============================================

These parameters specify how the :term:`Launch Manager` itself is monitored.

- :need:`feat_req__lifecycle__lm_self_health_check`
- :need:`feat_req__lifecycle__lm_ext_watchdog_notify`
- :need:`feat_req__lifecycle__lm_ext_wdg_failed_test`
- :need:`feat_req__lifecycle__lm_ext_watchdog_cfg`


Static Architecture
===================

.. logic_arc_int:: Configuration parameters static architecture
   :id: logic_arc_int__lifecycle__cfg_params_static
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces

   .. uml:: _assets/config_params_static.puml
      :scale: 50
      :align: center
