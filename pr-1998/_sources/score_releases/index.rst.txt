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

.. _releases:

S-CORE Releases
===============

A **Release** is a crucial aspects of the project life cycle within the `Eclipse Development Process <https://www.eclipse.org/projects/handbook/#release>`_. It is a officially distributed, versioned, and deployable collection of Project artifacts intended for distribution beyond the Project Developers. It brings together the initial set of core modules, reference integrations, and supporting infrastructure needed to build. For further information about the platform releases and module releases see `release documentation <https://eclipse-score.github.io/process_description//main/process_areas/release_management/release_workproducts.html>`_ in the process description.

S-CORE Releases Overview
========================

Roadmap
--------
Roadmap is a living document.

.. image:: _assets/score_timeline.svg
   :width: 700
   :alt: Infrastructure overview
   :align: center

Overview
--------

.. image:: _assets/architecture.drawio.svg
   :width: 1000
   :alt: Infrastructure overview
   :align: center

SW Module List
--------------

.. list-table:: S-CORE software modules overview
   :header-rows: 1

   * - SW Module Name
     - Committer List
     - Release
     - Date
     - Feature (Change) Request
     - Repo
     - GitHub Discussions
   * - IPC
     - Holger Grandy, Gerd Schäfer, Nico Hartmann, Sven Kappel, Thilo Schmitt
     - v0.5
     - Q4
     - _
     - `inc_mw_com <https://github.com/eclipse-score/inc_mw_com>`_
     - `Communication CTF <https://github.com/orgs/eclipse-score/discussions/categories/communication-ft>`_
   * - Fixed Execution Order Framework (incl. Orchestrator)
     - Holger Grandy, Gerd Schäfer, Nico Hartmann, Sven Kappel, Thilo Schmitt
     - v0.5
     - Q4
     - _
     - `inc_feo <https://github.com/eclipse-score/inc_feo>`_
     - `FEO CTF <https://github.com/orgs/eclipse-score/discussions/categories/feo-ft>`_
   * - Logging
     - Holger Grandy, Gerd Schäfer, Nico Hartmann
     - v0.5
     - Q4
     - _
     - `inc_mw_log <https://github.com/eclipse-score/inc_mw_log>`_
     - `Logging CTF <https://github.com/orgs/eclipse-score/discussions/categories/logging-ft>`_
   * - Persistency
     - Gerd Schäfer, Nico Hartmann, Sven Kappel
     - v0.5
     - Q4
     - _
     - `inc_mw_per <https://github.com/eclipse-score/inc_mw_per>`_
     - `Persistency CTF <https://github.com/orgs/eclipse-score/discussions/categories/persistency-ft>`_
   * - Integration Testing Framework
     - Holger Grandy
     - v0.5
     - Q4
     - _
     - _
     - _
   * - SOME/IP
     - _
     - _
     - _
     - _
     - _
     - _
   * - Lifecycle
     - _
     - _
     - _
     - _
     - _
     - _
   * - Diagnosis
     - _
     - _
     - _
     - _
     - _
     - _
   * - OS Abstraction Layer
     - _
     - _
     - _
     - _
     - _
     - _
   * - Time Sync
     - _
     - _
     - _
     - _
     - _
     - _
   * - Firewall
     - _
     - _
     - _
     - _
     - _
     - _

.. toctree::
   :hidden:
   :maxdepth: 2

   platform_release_note
