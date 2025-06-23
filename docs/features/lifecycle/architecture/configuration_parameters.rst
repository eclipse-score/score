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

Configuration Parameters
########################


Launch Manager Configuration Parameters
=======================================


Component Configuration Parameters
==================================
- UID feat_req__lifecycle__lm_uid_gid
- GID feat_req__lifecycle__lm_uid_gid
- supplementary groups feat_req__lifecycle__lm_supplementary
- runmask feat_req__lifecycle__lm_runmask
- priority feat_req__lifecycle__lm_priority
- ability
- security policies
- cwd (current working directory) feat_req__lifecycle__lm_cwd
- environmental variables feat_req__lifecycle__lm_env_var
- command to be executed
- arguments feat_req__lifecycle__lm_arguments
- stdin feat_req__lifecycle__lm_std_out_in_err_redir
- stdout feat_req__lifecycle__lm_std_out_in_err_redir
- stderr feat_req__lifecycle__lm_std_out_in_err_redir
- aslr feat_req__lifecycle__lm_aslr
- rlimits feat_req__lifecycle__lm_rlimit


Dependency and recovery Parameters
==================================





Requirements related to the external monitoring
===============================================

- :need:`feat_req__lifecycle__lm_self_health_check`
- :need:`feat_req__lifecycle__lm_ext_watchdog_notify`
- :need:`feat_req__lifecycle__lm_ext_wdg_failed_test`
- :need:`feat_req__lifecycle__lm_ext_watchdog_cfg`


Dynamic Architecture
====================
