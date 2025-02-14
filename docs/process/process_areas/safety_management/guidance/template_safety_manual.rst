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

Safety Manual Template
======================

.. gd_temp:: Safety Manual Template
   :id: GD_TEMP__safety_manual
   :status: valid
   :complies: STD_REQ_ISO26262__system_1, STD_REQ_ISO26262__system_2, STD_REQ_ISO26262__system_3, STD_REQ_ISO26262__system_4, STD_REQ_ISO26262__system_5, STD_REQ_ISO26262__system_6, STD_REQ_ISO26262__software_4, STD_REQ_ISO26262__software_5, STD_REQ_ISO26262__software_8, STD_REQ_ISO26262__support_65

This document implements <add "need" link>

Introduction/Scope
------------------
| <Describe here which module (or the platform) is covered by this manual.>

Assumed Platform Safety Requirements
------------------------------------
| For the <SCORE platform / module name> the following safety related stakeholder requirements are assumed to define the top level functionality (purpose) of the <SCORE platform / module name>. I.e. from these all the feature and component requirements implemented are derived.
| <List here all the stakeholder requirements, with safety not equal to QM, the module's components requirements are derived from.>

Assumptions of Use
------------------

Assumptions on the Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| Generally the assumption of the SCORE platform SEooC is that it is integrated in a safe system, i.e. the POSIX OS it runs on is qualified and also the HW related failures are taken into account by the system integrator, if not otherwise stated in the module's safety concept.
| <List here all the respective general environment AoU.>
| <List here all the OS calls the SCORE platform expects to be safe.>

Assumptions on the User
^^^^^^^^^^^^^^^^^^^^^^^
| As there is no assumption on which specific OS and HW is used, the integration testing of the stakeholder and feature requirements is expected to be performed by the user of the platform SEooC. Tests covering all stakeholder and feature requirements performed on a reference platform (tbd link to reference platform specification), reviewed and passed are included in the platform SEooC safety case.
| Additionally the components of the platform may have additional specific assumptions how they are used. These are part of every module documentation: <link to add>. Assumptions from components to their users can be fulfilled in two ways:
| 1. There are assumption which need to be fulfilled by all SW components, e.g. "every user of an IPC mechanism needs to make sure that he provides correct data (including appropriate ASIL level)" - in this case the AoU is marked as "platform".
| 2. There are assumption which can be fulfilled by a safety mechanism realized by some other SCORE platform component and are therefore not relevant for an user who uses the whole platform. But those are relevant if you chose to use the module SEooC stand-alone - in this case the AoU is marked as "module". An example would be the "JSON read" which requires "The user shall provide a string as input which is not corrupted due to HW or QM SW errors." - which is covered when using together with safe SCORE platform persistency feature.
| <Link here to all module AoUs.>

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
