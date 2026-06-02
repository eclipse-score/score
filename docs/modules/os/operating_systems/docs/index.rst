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

.. _comp_doc_os:

Operating Systems
=================

.. toctree::
   :maxdepth: 2
   :hidden:

   onboarding/index
   community/index
   functional/index
   certifiable/index

An operating system is an environment on which S-CORE is integrated and executed.

In the context of the OS module, **S-CORE acts as the operaring system integrator**:
S-CORE maintainers integrate and validate specific OS environments as S-CORE
reference operating systems and document the practical usage for downstream users.

Operating Systems are categorized into the following **levels**:

* **Community Level**: integrated on a best-effort basis. S-CORE provides **no guarantees**
  that the operating system builds or runs reliably.
* **Functional Level**: S-CORE provides **functional guarantees** (build + tests for the
  reference integration).
* **Certifiable Level**: S-CORE provides **certifiability-oriented guarantees** for the
  reference integration and documents additional safety/security expectations.

The concrete level requirements are defined in :ref:`platform_assumptions`.

Roles and Responsibilities
--------------------------

Operating system integrations follow the process requirements defined in:
:ref:`platform_assumptions`.

Two roles from the process requirements are relevant:

* **Supplier**: provides an external SW element (e.g. OS / hypervisor) that S-CORE uses.
* **System Integrator**: integrates the S-CORE operring system into a system.

In the S-CORE Software Platforms, these roles map to:

* **OS Maintainer** (Supplier role): resolves the *supplier* requirements.
  The OS maintainer provides the prerequisites so that the OS can be considered
  for promotion to a level.

* **S-CORE** (System Integrator role): resolves the *system integrator* requirements.
  Once S-CORE accepts an OS at **Functional** or **Certifiable** level, S-CORE
  must ensure that the accepted guarantees remain valid across all increments.
