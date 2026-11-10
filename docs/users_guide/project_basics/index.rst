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
.. _project_basics:

Overview
========

This section gives you the conceptual foundation for working with S-CORE.
Before diving into code or contribution workflows, read through these pages
to understand how the platform is structured and what drives its design:

- **Technologies** — the toolchain and infrastructure that power S-CORE, from
  build system and development environment to documentation, CI/CD and testing.
- **Software Architecture** — the high-level decomposition of the platform into
  layers, features and modules, and how the architecture evolves.
- **Module Structure** — the most important repositories and Bazel modules of S-CORE,
  what each of them provides and how they depend on each other.
- **Integration Process** — how modules are released, continuously built, tested
  and assembled into the reference integration and finally into an S-CORE release.

.. toctree::
   :maxdepth: 1
   :glob:

   technology_overview.rst
   software_architecture_overview.rst
   module_structure_overview.rst
   integration_process.rst
..    */index
