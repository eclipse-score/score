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

Safety Manual
=============

.. note:: Document header

.. document:: Baselibs Safety Manual
   :id: doc__baselibs_safety_manual
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__module_safety_manual


Introduction/Scope
------------------
| <Describe here which module (or the platform) is covered by this manual.>

Assumed Platform Safety Requirements
------------------------------------
| For the <Project platform / module name> the following safety related stakeholder requirements are assumed to define the top level functionality (purpose) of the <Project platform / module name>. I.e. from these all the feature and component requirements implemented are derived.
| <List here all the stakeholder requirements, with safety not equal to QM, the module's components requirements are derived from.>

Assumptions of Use
------------------

Assumptions on the Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| Generally the assumption of the project platform SEooC is that it is integrated in a safe system, i.e. the POSIX OS it runs on is qualified and also the HW related failures are taken into account by the system integrator, if not otherwise stated in the module's safety concept.
| The platform-wide AoUs are collected in :need:`doc__platform_assumptions`
|
| To support :need:`aou_req__platform__safety_matching`:
| <List here all the OS/libcxx calls the module expects to be safe.>

List of additional AoUs expected from the environment the module runs on:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" in need["tags"] and "baselibs" in need["tags"]:
                results.append(need)


Assumptions on the User
^^^^^^^^^^^^^^^^^^^^^^^
| As there is no assumption on which specific OS and HW is used, the integration testing of the stakeholder and feature requirements is expected to be performed by the user of the platform SEooC. Tests covering all stakeholder and feature requirements performed on a reference platform (tbd link to reference platform specification), reviewed and passed are included in the platform SEooC safety case.
| Additionally the components of the platform may have additional specific assumptions how they are used. These are part of every module documentation: <link to add>. Assumptions from components to their users can be fulfilled in two ways:
| 1. There are assumption which need to be fulfilled by all SW components, e.g. "every user of an IPC mechanism needs to make sure that he provides correct data (including appropriate ASIL level)" - in this case the AoU is marked as "platform".
| 2. There are assumption which can be fulfilled by a safety mechanism realized by some other project platform component and are therefore not relevant for an user who uses the whole platform. But those are relevant if you chose to use the module SEooC stand-alone - in this case the AoU is marked as "module". An example would be the "JSON read" which requires "The user shall provide a string as input which is not corrupted due to HW or QM SW errors." - which is covered when using together with safe project platform persistency feature.

List of AoUs on the user of the module of this safety manual:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" not in need["tags"] and "baselibs" in need["tags"]:
                results.append(need)

Safety concept of the SEooC
---------------------------
| <Describe here the safety concept incl. which faults are taken care of, reactions of the implemented functions under anomalous operating conditions ... if this is not already documented sufficiently in the feature documentation "safety impact" section of all the features the module is used in.>

Safety Anomalies
----------------
| Anomalies (bugs in ASIL SW, detected by testing or by users, which could not be fixed) known before release are documented in the platform/module release notes <add link to release note>.

References
----------
| <link to the user manual>
| <other links>
