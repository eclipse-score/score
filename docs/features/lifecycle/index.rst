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

.. _chm_feature_templates:


Lifecycle
---------

.. note:: Document header

.. document:: Lifecycle
   :id: doc__lifecycle
   :status: draft
   :safety: ASIL_B
   :tags: feature_request


Feature flag
------------

To activate this feature, use the following feature flag:

``experimental_lifecycle``


Abstract
--------

The lifecycle feature provides a set of functionalities to manage the lifecycle of
components in the S-SCORE platform. The goal is to ensure that components can be
started, stopped, and monitored effectively, providing a robust framework for managing the state of the system.

Motivation
----------

For every ecu handling of startup, shutdown, and monitoring of components is crucial to
ensure the system operates correctly and efficiently. Additionally we need do provide the
means to set the system in different operating modes, such as normal operation, engineering/debug mode,
flash mode etc.


Rationale
---------

Main task of the lifecycle system is to start and stop :term:`processes` depending on the
overall state the user wants to achieve and the functional dependencies between
the :term:`processes`.

:term:`Lifecycle Component` can be very simple like a single process or more complex like a set of processes
which are started in a certain order and with certain dependencies between them or containers.

We call a state of the system an :term:`Operating Mode`, which is defined via the
:term:`Lifecycle Component` running on the system at a certain point in time.
A lifecycle component is a configuration unit, which describes the executable, which shall be executed
and the :term:`sandbox` the platform has to provide to run this executable.

E.g. the :term:`sandbox` shall describe

- environment variables, which shall be set via the lifecycle system
- secpol policies on QNX, which shall be applied to the process
- cgroup configurations on Linux, which shall be applied to the process
- user and group IDs under which the process shall be started
- ...



Via the configuration we define a certain operting mode and add all the components, which are needed to
realize this operating mode as dependencies.


A second task of the lifecycle system is to supervise the aliveness of the :term:`processes`,
which are started and to initiate appropriate actions in case of a failure, which
might result in many cases in a change of the :term:`Operating Mode`.


The Lifecycle feature addresses the following stakeholder requirements:

• :need:`stkh_req__execution_model__processes`: Comprehensive process lifecycle management
  including startup, shutdown, recovery, and cross-process synchronization of threads

• :need:`stkh_req__functional_req__file_based`: Modular configuration file support allowing changes
  without rebuilding software, enabling flexible system setup and module management

• :need:`stkh_req__dependability__safety_features`: Implementation of monitoring safety mechanisms

A second task of the lifecycle system is to supervise the aliveness of the processes, which are started
and to initiate appropriate actions in case of a failure, which might result in many cases in
a change of the operting mode.

Support of containers
=====================

A :term:`Sandbox` can e.g. realized as a container, which is  a lightweight, standalone executable
package that includes everything needed to run a piece of software,
including the code, runtime, libraries, and system tools.
In the context of the S-SCORE platform, container can be used to encapsulate applications and their dependencies,
ensuring consistent execution across different environments.

Main task of the lifecycle system is to start and stop components with an OCI compliant runtime
environment `<https://github.com/opencontainers/runtime-spec>`__ depending on the overall state the
user wants to achieve and the functional dependencies between the processes.

A `container` is a lightweight, standalone executable package that includes everything needed to run a piece of software,
including the code, runtime, libraries, and system tools.
In the context of the S-SCORE platform, containers are used to encapsulate applications and their dependencies,
ensuring consistent execution across different environments.

We call a runtime-state of the system an `operating mode`, which is defined via the processes running on the
system at a certain point in time the with the `OCI` runtime.

Coming from the OCI Specification the `operation modes` is a superset of the `OCI` states

- Creating
- Created
- Running
- Stopped

Via the configuration we define a certain operting mode and add all the components, which are needed to
realize this operating mode as dependencies.

A `lifecycle component` is a configuration unit, which describes the `executable`, which shall be executed
and the `sandbox` the platform has to provide to run this executable.
E.g. the `sandbox`` shall describe

- environment variables, which shall be set via the lifecycle system
- secpol policies on QNX, which shall be applied to the process
- cgroup configurations on linux, which shall be applied to the process
- user and group ids under which the process shall be started.
- ...

A second task of the lifecycle system is to supervise the aliveness of the processes, which are started
and to initiate appropriate actions in case of a failure, which might result in many cases in
a change of the operting mode.

Specification
-------------

.. feat_arc_sta:: Feature architecture
   :id: feat_arc_sta__lifecycle__overview
   :security: YES
   :safety:  ASIL_B
   :status: valid
   :fulfils:
   :includes: logic_arc_int__lifecycle__controlif, logic_arc_int__lifecycle__health_monitor_if, logic_arc_int__lifecycle__alive_if


   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}




The overall functionality of the feature can be split into 2 subfeatures, which are
closely coupled to each other:

* **Lifecycle Management**: This subfeature is responsible for the management of
  the lifecycle of a :term:`Lifecycle Component`, including starting and stopping :term:`processes`,
  managing their dependencies, and handling different operating modes.

* **Health Monitoring**: Provides platform functionality to monitor certain health
  conditions of applications:

  * Alive Monitoring
  * Deadline Monitoring
  * Logical Programflow Monitoring



Architecture
============

The concept is based on 2 major components:

* **:term:`Launch Manager`**: Responsible for starting and stopping components based on
  the defined operating modes and alive supervision of the started components

* **:term:`Health Monitor`**: Provides process local monitoring functionalities such as
  deadline monitoring and logical program flow monitoring








Requirements
============

.. toctree::
   :maxdepth: 1
   :glob:

   requirements/*

Modules
=======


.. mod_view_sta:: Lifecycle
   :id: mod_view_sta__lifecycle__1
   :includes: comp_arc_sta__lifecycle__launch_manager, comp_arc_sta__lifecycle__healthmonitor

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_module(need(), needs) }}


The overall concept is based on 2 components:

* Component Launch Manager: Responsible for starting and stopping components based on the defined operating modes
  and alive supervision of the started components
* Component Health Monitor: Provides process local monitoring fucntionalities
  such as deadline monitoring and logical program flow monitoring.




.. uml:: architecture/_assets/overview_static.puml
    :scale: 50
    :align: center

-----------------------------------------------------

.. uml::
    :scale: 50
    :align: center

    title Dependency based lifecycle management

    state debug #lightblue
    state running #lightblue
    state ready_for_shutdown #lightblue

    state app1: /opt/bin/app1
    state app2: /opt/bin/app2
    state app3: /opt/bin/app3

    state ssh: /usr/bin/ssh
    state setup_filesystems: /etc/setup_filesystems.sh
    state eth_driver: /bin/net-dev-eth
    state filesystem: /bin/net-dev-ufs
    state flash_driver: /bin/dev-emmc

    [*] --> debug
    [*] -[hidden]-> running
    [*] -[hidden]-> ready_for_shutdown


    running --> app1
    app1 --> app2
    app2 --> networking
    running --> app3
    app3 --> networking

    debug --> ssh
    ssh --> networking
    networking --> setup_filesystems
    setup_filesystems --> filesystem
    networking --> eth_driver
    filesystem --> flash_driver

    legend right
        |Color| Type |
        |<#lightblue>| Operating modes provided by the ControlInterface|
    endlegend

Architecture
------------

.. toctree::
   :maxdepth: 1
   :glob:

   ./architecture/application_health_monitor
   ./architecture/control_interface
   ./architecture/external_monitoring
   ./architecture/configuration_parameters
   ./architecture/launch_manager


Requirements
------------

.. toctree::
   :maxdepth: 1
   :glob:

   requirements/*

Backwards Compatibility
-----------------------

New feature

Security Impact
---------------

TBD

Safety Impact
-------------

TBD


License Impact
--------------

TBD


How to Teach This
-----------------



Rejected Ideas
==============

TBD


Open Issues
===========

TBD


Footnotes
---------

[A collection of footnotes cited in the CR, and a place to list non-inline hyperlink targets.]
