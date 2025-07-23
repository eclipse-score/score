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

Launch manager
##############

The :term:`Launch manager` is a component that provides a framework for managing the lifecycle of
processes in the S-CORE platform.
It allows for launching, monitoring, and controlling processes based on defined configurations and
requirements.
As such it is a central part of the lifecycle management in S-CORE and knows about the state of all
processes in the system

Static Architecture
===================

.. logic_arc_int:: Alive Interface
   :id: logic_arc_int__lifecycle__alive_if
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces


.. comp_arc_sta:: Launch Manager
   :id: comp_arc_sta__lifecycle__launch_manager
   :status: valid
   :safety: ASIL_B
   :implements: logic_arc_int__lifecycle__controlif, logic_arc_int__lifecycle__alive_if
   :uses: logic_arc_int__logging__logging, logic_arc_int__baselibs__json, logic_arc_int__os__fork
   :security: NO
   :includes:
   :fulfils:

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_component(need(), needs) }}


Dynamic Architecture
====================

The dynamic behaviour of the :term:`Launch Manager` is defined by a configuration data, which spawn
a directed acyclic graph (DAG) of processes and so called :term:`Run Targets`.
The :term:`Run Targets` are virtual nodes in the DAG and reperesent :term:`Operting Modes` of the system.

.. uml:: _assets/launch_manager_target_tree.puml
   :scale: 50
   :align: center


Requirements
============

- :need:`feat_req__lifecycle__launch_support`
- :need:`feat_req__lifecycle__process_ordering`
- :need:`feat_req__lifecycle__parallel_launch_support`
- :need:`feat_req__lifecycle__waitfor_support`
- :need:`feat_req__lifecycle__process_input_output`
- :need:`feat_req__lifecycle__essential_processes`
- :need:`feat_req__lifecycle__essential_process_fail`
- :need:`feat_req__lifecycle__error_reaction_config`
- :need:`feat_req__lifecycle__process_launch_args`
- :need:`feat_req__lifecycle__uid_gid_support`
- :need:`feat_req__lifecycle__total_wait_time_support`
- :need:`feat_req__lifecycle__polling_interval`
- :need:`feat_req__lifecycle__launch_priority_support`
- :need:`feat_req__lifecycle__cwd_support`
- :need:`feat_req__lifecycle__terminal_support`
- :need:`feat_req__lifecycle__std_handle_redir`
- :need:`feat_req__lifecycle__builtin_command_support`
- :need:`feat_req__lifecycle__secpol_non_root`
- :need:`feat_req__lifecycle__retries_configurable`
- :need:`feat_req__lifecycle__procmgr_support`
- :need:`feat_req__lifecycle__fd_inheritance`
- :need:`feat_req__lifecycle__support_secpol_type`
- :need:`feat_req__lifecycle__supplementary_groups`
- :need:`feat_req__lifecycle__scheduling_policy`
- :need:`feat_req__lifecycle__runmask_support`
- :need:`feat_req__lifecycle__aslr_support`
- :need:`feat_req__lifecycle__process_rlimit_support`
- :need:`feat_req__lifecycle__detach_parent_process`
- :need:`feat_req__lifecycle__critical_processes`
- :need:`feat_req__lifecycle__running_processes`
- :need:`feat_req__lifecycle__drop_supervsion`
- :need:`feat_req__lifecycle__multi_start_support`
- :need:`feat_req__lifecycle__validate_conditions`
- :need:`feat_req__lifecycle__validation_conditions`
- :need:`feat_req__lifecycle__process_ownership`
- :need:`feat_req__lifecycle__consistent_dependencies`
- :need:`feat_req__lifecycle__stop_process_dependents`
- :need:`feat_req__lifecycle__stop_order_spec`
- :need:`feat_req__lifecycle__oci_compliant`
- :need:`feat_req__lifecycle__request_group_stop`
- :need:`feat_req__lifecycle__request_group_restart`
-

TODO: complete requiremeents
