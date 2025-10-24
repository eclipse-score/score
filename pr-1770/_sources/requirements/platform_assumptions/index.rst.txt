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

.. _platform_assumptions:

SW Platform Assumptions
=======================

.. document:: SW Platform Assumptions
   :id: doc__platform_assumptions
   :status: draft
   :security: YES
   :safety: ASIL_B
   :realizes: PROCESS_wp__requirements_stkh

Assumptions on Environment
--------------------------

In this section assumptions are described which need to be fulfilled by the architecture level below the SW platform,
i.e. by the elements outside of S-CORE, but used by S-CORE platform components. These include elements like
the operating system, programming language libraries, hypervisor or processing hardware.

To fulfill these assumptions is the responsibility of the integrator.

.. aou_req:: OS safety features
   :id: aou_req__platform__os_safety_features
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The Integrator shall integrate the SW platform with an OS providing safety functions, if the system using the SW platform has safety goals.

   Note: A list of OS safety functions needed is compiled by the S-CORE project here (TBD).

Assumptions on the OS integration - Community Level
---------------------------------------------------

This is the lowest level of integration, the higher levels will build on this.
It also contains expectations towards an OS supplier which can be used as criteria for OS selection
by the integrator. Building and running of OS is enabled, but no pro-active support from S-CORE
is provided for e.g. build or test problems. No guarantees that S-CORE builds or runs on the OS.

.. aou_req:: OS integration assistance
   :id: aou_req__platform__os_integration_assistance
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The OS supplier shall provide a contact point for integration assistance.

.. aou_req:: OS integration manual
   :id: aou_req__platform__os_integration_manual
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The OS supplier shall provide an integration manual.

.. aou_req:: OS bug interface
   :id: aou_req__platform__os_bug_interface
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The OS supplier shall provide a bug reporting interface.

   Note: There is no guarantee provided to fix these bugs.

TBD: AoUs on the S-CORE SW Platform integrator with respect to OS integration on this level.

Assumptions on the OS integration - Functional Level
----------------------------------------------------

This is the middle level of integraton, the higher level will build on this.
It is the level where the S-CORE SW platform will functionally "work" on the supplied OS.

.. aou_req:: OS bazel tooling
   :id: aou_req__platform__os_bazel_tooling
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The OS supplier shall provide tools for Bazel to be able to build the S-CORE SW platform on the supplier OS
   and support the run and test of the S-CORE SW platform on the supplier OS.

.. aou_req:: OS bug fixing
   :id: aou_req__platform__os_bug_fixing
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The OS supplier shall fix bugs reported in a predictable manner.

   Note: For OSS community providing an OS this requirement could be covered by analyzing how bugs were treated in the past. For companies by the definition of a service level process.

TBD: AoUs on the S-CORE SW Platform integrator with respect to OS integration on this level.

Assumptions on the OS integration - Certifiable Level
-----------------------------------------------------

This is the highest level of integraton. This is the level where the S-CORE SW platform will be certifiable on the supplied OS.

.. aou_req:: OS integration levels
   :id: aou_req__platform__os_levels
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The OS supplier shall provide all the levels AoUs in a safe way (i.e. the "safety" attribute will be raised to the level in this AoU).

   Note: This includes for example :need:`aou_req__platform__os_bazel_tooling`, :need:`aou_req__platform__os_bug_fixing`

.. aou_req:: OS safety AoU
   :id: aou_req__platform__os_safety_aou
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The OS supplier shall provide Assumptions of (safe) Use.

.. aou_req:: OS safety functions
   :id: aou_req__platform__os_safety_functions
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The OS supplier shall provide a list of safe OS functions.

.. aou_req:: OS safety anomaly reporting
   :id: aou_req__platform__os_safety_anomaly
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The OS supplier shall perform safety anomaly reporting.

   Note: This could be fulfilled by listing per release version all known and user reported bugs which affect the safe OS functions.

TBD: AoUs on the S-CORE SW Platform integrator with respect to OS integration on this level.

Assumptions of Use
------------------

In this section assumptions are described which need to be fulfilled by the applications running on top of the SW platform.

TBD
