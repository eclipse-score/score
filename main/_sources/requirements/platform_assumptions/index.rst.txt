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

SW-platform Assumptions
=======================

.. document:: SW-platform Assumptions
   :id: doc__platform_assumptions
   :status: draft
   :security: YES
   :safety: ASIL_B
   :realizes: wp__requirements_sw_platform_aou

Assumptions on Environment
--------------------------

In this section assumptions are described which need to be fulfilled by the architecture level below the SW-platform,
i.e. by the elements or organizations outside of S-CORE, but used by S-CORE platform components. These include elements like
the operating system, programming language libraries, hypervisor or processing hardware.
For "organizations" two roles are used in the AoU text:

- Supplier: is the provider of an element the S-CORE SW-platform is using but which is developed and maintained externally.
- System Integrator: uses the S-CORE SW-platform as a part of a system he provides to a customer. The system integrator can be for example a Tier1 providing an electronic control unit to a OEM or an OEM providing a car to his end-customer. S-CORE does not know which.

To fulfill these assumptions is the responsibility of the mentioned roles.

Note that the "supplier" AoUs were created with an OS supplier in mind but are really general AoUs for any external SW element S-CORE uses.

Assumptions on the external SW element integration - Community Level
--------------------------------------------------------------------

This is the lowest level of integration, the higher levels will build on this.
It also contains expectations towards an supplier which can be used as criteria for supplier selection
by the system integrator. Building and running of external SW element is enabled, but no pro-active support from S-CORE
is provided for e.g. build or test problems. No guarantees that S-CORE builds or runs with the external SW element.

.. aou_req:: integration assistance
   :id: aou_req__platform__integration_assistance
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The supplier shall provide a contact point for integration assistance.

.. aou_req:: integration manual
   :id: aou_req__platform__os_integration_manual
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The supplier shall provide an integration manual.

.. aou_req:: bug interface
   :id: aou_req__platform__bug_interface
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The supplier shall provide a bug reporting interface.

   Note: There is no guarantee provided to fix these bugs.

There are no AoUs on the system integrator on this level,
as this level is not expected sufficient for a product release, only for incubation/prototype.

Assumptions on the external SW element integration - Functional Level
---------------------------------------------------------------------

This is the middle level of integraton, the higher level will build on this.
It is the level where the S-CORE SW-platform will functionally "work" with the external SW element.

.. aou_req:: bazel tooling
   :id: aou_req__platform__bazel_tooling
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The supplier shall provide tools for Bazel to be able to build the S-CORE SW-platform with the external SW element
   and support the run and test of the S-CORE SW-platform.

.. aou_req:: bug fixing
   :id: aou_req__platform__bug_fixing
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The supplier shall fix bugs reported in a predictable manner.

   Note: For OSS community providing an external SW element this requirement could be covered by analyzing how bugs were treated in the past. For companies by the definition of a service level process.

.. aou_req:: SW-platform testing
   :id: aou_req__platform__testing
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The system integrator shall run the tests provided by S-CORE (platform, feature, component and Unit level for his selected S-CORE modules) on his selected OS/Hypervisor/HW combination,
   or provide equivalent argumentation.

   Note1: S-CORE will run these tests for one or more reference OS/Hypervisor/HW combination, if not all passing, remaining issues are documented in release notes. In case the selected combination is equal to a S-CORE reference and the complete S-CORE SW-platform is used, this AoU may be skipped.

   Note2: Equivalent argumentation could be for example that the test environments for unit tests would be sufficiently equal in S-CORE project and at the integrator.

.. aou_req:: SW-platform integration bug reporting
   :id: aou_req__platform__bug_report
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :status: valid

   The system integrator shall report the bugs found during integration of the S-CORE SW-platform on his selected OS/Hypervisor/HW combination to the external SW element supplier and S-CORE for analysis.

Assumptions on the external SW element integration - Certifiable Level
----------------------------------------------------------------------

This is the highest level of integraton. This is the level where the S-CORE SW-platform will be certifiable with an external SW element.

.. aou_req:: integration levels
   :id: aou_req__platform__levels
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The supplier and system integrator shall fulfill all the levels AoUs in a safe way (i.e. the "safety" attribute will be raised to the level in this AoU).

   Note: This includes for example :need:`aou_req__platform__bazel_tooling`, :need:`aou_req__platform__bug_fixing`

.. aou_req:: safety AoU
   :id: aou_req__platform__safety_aou
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The supplier shall provide Assumptions of (safe) Use for the external SW element.

   Note: This may be part of an external SW element's safety manual.

.. aou_req:: safety functions
   :id: aou_req__platform__safety_functions
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The supplier shall provide a list of safe external SW element functions.

.. aou_req:: safety anomaly reporting
   :id: aou_req__platform__safety_anomaly
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The supplier shall perform safety anomaly reporting on critical bugs in the external SW element.

   Note: This could be fulfilled by listing per release version all known and user reported bugs which affect the safe external SW element functions.

.. aou_req:: safety matching
   :id: aou_req__platform__safety_matching
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   If the system using the SW-platform has safety goals, the system integrator shall integrate the SW-platform with external SW elements providing safety functions.
   This includes to make sure that the safety functions S-CORE SW-platform requires match with the ones provided by these external SW elements (as in :need:`aou_req__platform__safety_functions`).

   Note1: A list of safety functions needed from external SW elements is compiled by the S-CORE project here (TBD).

   Note2: The integrator can expect that for the safe S-CORE reference integration (incl. OS and other external SW elements) this AoU is fulfilled by S-CORE SW-platform already, but without guarantee.

   Note3: This applies also if the system integrator would replace a S-CORE SW-platform element with another SW element which is external to S-CORE.

.. aou_req:: safety integration
   :id: aou_req__platform__safety_integration
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   If the system using the SW-platform has safety goals, the system integrator shall make sure that the AoUs relevant for external SW element safety functions (as in :need:`aou_req__platform__safety_aou`) are fulfilled by the S-CORE SW-platform.

   Note1: This could be done by contributing the required updates to the S-CORE project if S-CORE elements are affected.

   Note2: The system integrator can expect that for the safe S-CORE reference integration (incl. OS and other external SW elements) this AoU is fulfilled by S-CORE SW-platform already, but without guarantee.

   Note3: This applies also if the system integrator would replace a S-CORE SW-platform element with another SW element which is external to S-CORE.

.. aou_req:: Integrator safety anomaly reporting
   :id: aou_req__platform__integration_safety_anomaly
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   If the system using the SW-platform has safety goals, the system integrator shall perform safety anomaly reporting taking into account also the reporting of all the components he integrates.

   Note: This includes all the modules of the S-CORE SW platform used by the system integrator.
   The relevant safety critical bugs or safety anomalies are published by S-CORE as defined in the :need:`doc__platform_problem_resolution_plan`.


Assumptions on Applications
---------------------------

In this section assumptions are described which need to be fulfilled by the applications running on top of the SW-platform.

.. aou_req:: Avoidance of Exceptions
   :id: aou_req__platform__no_exceptions
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   All applications using the SW-platform shall not handle exceptions.

   Note: Exceptions create additional overhead which may be a safety risk. Therefore, all exceptions are expected to lead directly to a termination of the application causing the exception.
   This is supported by the library safecpp/aborts_upon_exception supplied by S-CORE "base libraries" feature.

.. aou_req:: Error Reaction
   :id: aou_req__platform__error_reaction
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   Safety applications using the SW-platform shall read error information from the requested S-CORE functions and perform an appropriate reaction.

   Note: For many errors detected by SW-platform elements there could be mitigation actions to be applied by the user application.
   So the SW-platform reports the errors to the user application and does not stop execution as a standard reaction. See :need:`stkh_req__dependability__safe_state`.

.. aou_req:: No mixed ASIL
   :id: aou_req__platform__no_mixed_asil
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   Safety application components running in one POSIX process shall implement the highest ASIL of their assigned requirements.

.. aou_req:: Program Flow Monitoring
   :id: aou_req__platform__flow_monitoring
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   Safety applications using the SW-platform shall use program flow monitoring to detect run time errors or explain in their safety concept why they do not need this.

   Note1: Reasons for not needing program flow monitoring could be an OS scheduler with timing and execution guarantees.
   Or that in case of non/late execution of the application the safety integrity of the system is not affected.

   Note2: The SW-Platform supports this - see :need:`stkh_req__dependability__safety_features` "live, deadline, logical supervision"

Assumptions on Safety System
----------------------------

In this section assumptions are described which need to be fulfilled by the system or system integrator.

.. aou_req:: Safe HW platform
   :id: aou_req__platform__hardware_safety
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   If the system using the SW-platform has safety goals, the system shall provide state-of-the art hardware safety mechanisms.

   Note1: A selection of hardware safety mechanisms is collected in :need:`stkh_req__dependability__safety_features`

   Note2: These safety mechanisms are mostly OS/Hypervisor/HW specific, so the system integrator can only expect S-CORE support for the reference OS/Hypervisor/HW combination.

.. aou_req:: External Health Management
   :id: aou_req__platform__external_health_management
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   If the system using the SW-platform has safety goals, the system shall provide an external health management element which is able to initiate a safe system state.

   Note: This can be an "External Hardware Watchdog"

.. aou_req:: Process Isolation
   :id: aou_req__platform__process_isolation
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   If the system using the SW-platform has safety goals, the used operating system shall offer POSIX processes isolation.
   This shall cover memory isolation. Timing isolation may be covered.
