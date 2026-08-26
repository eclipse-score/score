..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

.. _introduction:

Introduction
============

.. document:: Introduction
   :id: doc__introduction
   :status: valid
   :version: 1
   :safety: QM
   :security: NO
   :realizes: wp__training_path[version==1]

This section gives you the conceptual foundation for working with S-CORE.
Before diving into code or contribution workflows, read through these pages
to understand how the platform is structured and what drives its design:

* **Technologies** (:ref:`technology_introduction`) — the toolchain and infrastructure that power S-CORE, from
  build system to documentation and CI/CD.
* **Architecture** (:ref:`architecture_introduction`) — the high-level decomposition of the platform into
  features and modules, and the principles behind it.
* **Module Structure** (:ref:`module_introduction`) — how an individual S-CORE module is laid out on disk,
  what each folder contains, and the conventions every module follows.
* **Integration Process** (:ref:`integration_introduction`) — how modules are continuously built, tested, and
  assembled into the reference integration.

.. grid:: 3
   :gutter: 3
   :class-container: score-grid score-grid-getstarted

   .. grid-item-card::
      :link: ../contribute/index
      :link-type: doc
      :text-align: center

      :octicon:`code-square;1.5em`

      Contribution Guideline
      ^^^
      Follow a step-by-step guide to build and integrate your first S-CORE
      module — from source code to CI/CD and doc

   .. grid-item-card::
      :link: ../users_guide/index
      :link-type: doc
      :text-align: center

      :octicon:`rocket;1.5em`

      User`s Guide
      ^^^
      Check how you can start building Applications on top of S-CORE.

   .. grid-item-card::
      :link: useful_links
      :link-type: doc
      :text-align: center

      :octicon:`link;1.5em`

      Useful links
      ^^^
      A collection of useful links for getting more information.


.. toctree::
   :maxdepth: 1
   :hidden:
   :glob:

   version_control_introduction
   technology_introduction
   architecture_introduction
   module_introduction.rst
   integration_introduction.rst
   useful_links.rst
