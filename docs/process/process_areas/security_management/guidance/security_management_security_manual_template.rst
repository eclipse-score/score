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

Security Manual Template
=========================

.. gd_temp:: Security Manual Template
   :id: gd_temp__security_manual
   :status: valid
   :complies:

This document implements <add "need" link>

Introduction/Scope
------------------
| <Describe here which module (or the platform) is covered by this manual.>

Assumed Platform Security Requirements
--------------------------------------
| For the <S-CORE platform / module name> the following security related stakeholder requirements are assumed to define the top level functionality (purpose) of the <S-CORE platform / module name>. I.e. from these all the feature and component requirements implemented are derived.
| <List here all the stakeholder requirements, with security relevance, the module's components requirements are derived from.>

Assumptions of Use
------------------

Assumptions on the Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| Generally the assumption of the S-CORE platform EooC is that it is integrated in a secure system, i.e. the POSIX OS it runs on is qualified and also the HW related failures are taken into account by the system integrator, if not otherwise stated in the module's security concept.
| <List here all the OS calls the S-CORE platform expects to be secure.>

List of AoUs expected from the environment the platform / module runs on:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" in need["tags"]:
                results.append(need)

Assumptions on the User
^^^^^^^^^^^^^^^^^^^^^^^
| As there is no assumption on which specific OS and HW is used, the integration testing of the stakeholder and feature requirements is expected to be performed by the user of the platform EooC. Tests covering all stakeholder and feature requirements performed on a reference platform (tbd link to reference platform specification), reviewed and passed are included in the platform EooC security package.
| Additionally the components of the platform may have additional specific assumptions how they are used. These are part of every module documentation: <link to add>. Assumptions from components to their users can be fulfilled in two ways:
| 1. There are assumption which need to be fulfilled by all SW components, e.g. "every user of an IPC mechanism needs to make sure that he provides correct data (e.g. including appropriate security (access) control)" - in this case the AoU is marked as "platform".
| 2. There are assumption which can be fulfilled by a security control realized by some other S-CORE platform component and are therefore not relevant for an user who uses the whole platform. But those are relevant if you chose to use the module EooC stand-alone - in this case the AoU is marked as "module". An example would be the "JSON read" which requires "The user shall provide a string as input which is not corrupted due to HW or QM SW errors." - which is covered when using together with safe S-CORE platform persistency feature.

List of AoUs on the user of the platform features or the module of this security manual:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" not in need["tags"]:
                results.append(need)

Security concept of the EooC
----------------------------
| <Describe here the security concept incl. which attack paths are taken care of, reactions of the implemented functions under threatened operating conditions ... if this is not already documented sufficiently in the feature documentation "security impact" section of all the features the module is used in.>

Security Weaknesses, Vulnerabilities
------------------------------------
| Weaknesses, Vulnerabilities (bugs in security relevant SW, detected by testing or by users, which could not be fixed) known before release are documented in the platform/module release notes <add link to release note>.

References
----------
| <link to the user manual>
| <other links>
