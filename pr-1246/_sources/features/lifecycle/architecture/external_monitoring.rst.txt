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

External Monitoring
###################


.. uml:: _assets/external_monitoring_static.puml
   :alt: External monitoring static Architecture

The following participants are related to the concept.

Launch Manager
--------------

As the :term:`Launch Manager` is critical component for the system, it shall support alive monitoring of itself. This means it must implement internal health management, such as
a worker thread, that wakes up every N milliseconds, checks if the component is in a consistent state, and send a notification to the external monitor.

External monitor
----------------

The aliveness of the :term:`Launch Manager` shall be monitored by an `external monitor, or a watchdog <https://en.wikipedia.org/wiki/Watchdog_timer>`_, to be able to detect "hanging" of the
`Launch Manager`. The implementation of the external watchdog is out of scope in S-SCORE, as it is ECU and/or project specific.

Watchdog Proxy
--------------

The component `Watchdog Proxy` is the project specific logical component, which has to implement the logical interface `HealthStatus` and translate alive events from the :term:`Launch Manager` as
project specific messages to the `External monitor`. The channel for sending these notifications is project specific, and can be for example `GPIO`, `UART` or `SPI`.
In a hypervisor based environment, the `external monitor` could also run with the same SoC as software only solution.

The `Watchdog Proxy` implementation is not specified in the S-CORE with high details, as the realization depends heavily on OS, :term:`Launch Manager` or even project specific needs.
For example, in Linux and `systemd` as the :term:`Launch Manager`, the interface can be `/dev/watchdog`, and `systemd` can use the interface directly.

In QNX, one could implement a component listening to the events (or even poll) from the :term:`Launch Manager` and translate these events as hardware specific notifications.

Requirements related to the external monitoring
===============================================

- :need:`feat_req__lifecycle__lm_self_health_check`
- :need:`feat_req__lifecycle__lm_ext_watchdog_notify`
- :need:`feat_req__lifecycle__lm_ext_wdg_failed_test`
- :need:`feat_req__lifecycle__lm_ext_watchdog_cfg`


Dynamic Architecture
====================

.. uml:: _assets/external_monitoring_sequence.puml
   :alt: External monitoring static arch

The most important interactions are the following:

.. list-table:: Sequence diagram Description
   :widths: 10 90
   :header-rows: 1

   * - Sequence number
     - Description
   * - 001
     - The configuration. (notification interval, startup grace period, etc.) Additionally, if a watchdog interface is used, the used interface name (eg. /dev/watchdog) must be configurable.
   * - 002
     - If the :term:`Launch Manager` provides a client library implementation, the library must connect and attach to the :term:`Launch Manager`
   * - 006
     - Check the internal status and trigger alive notification (007)
   * - 007
     - Send the alive notification to the external monitor. (UART/SPI/GPIO/etc.)
   * - 009
     - Watchdog to check if the notification fits the expected window
   * - 018
     - If the status check fails, do not trigger alive notification (or :term:`Launch Manager` has crashed)
   * - 019
     - If there is no alive notification, trigger watchdog error reaction
