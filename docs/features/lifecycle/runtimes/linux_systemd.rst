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

Lifecycle Runtime: Linux Systemd
################################

Integrating and using this module in Linux implies it has to work with existing init
systems (i.e Systemd) and watchdogs mechanisms for both SW and HW monitoring.

The main aspects of integrating the Lifecycle module into Linux include:

- Launch Manager and Systemd integration;
- Health Monitor Systemd integration (when needed);
- Using Systemd to monitor Launch Manager;
- Implement Launch Manager as a Systemd service controller.

Overview
========

A Systemd service controller is a sofwtare component that:

- Is managed by Systemd (via a unit file)
- Has access to the Systemd DBUS API (read and write)
- Can manage both static and dynamic worloads (ephemeral units)
