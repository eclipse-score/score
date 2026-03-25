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


Platform Safety Manual
======================

.. document:: Platform Safety Manual
   :id: doc__score_platform_safety_manual
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__module_safety_manual


Introduction/Scope
------------------

This safety manual applies to the S-CORE SW platform, defined by its modules, see :ref:`modules`
It covers all assumed (Technical) Safety Requirements of the S-CORE SW platform and all general
Assumptions of Use which are relevant for all users of any platform module.
The specific Assumptions of Use relevant only for the users of a specific module are documented in the module's safety manual.
That means that the platform safety manual always has to be read together with all its modules safety manuals.

Assumed Platform Safety Requirements
------------------------------------

For the S-CORE Platform the following functional safety related stakeholder requirements are assumed to define the top level functionality (purpose) of the S-CORE Platform. I.e. from these all the feature and component requirements implemented are derived.

.. needtable:: Assumed Platform Safety Requirements
   :filter: type == "stkh_req" and is_external == False and safety == "ASIL_B" and reqtype == "Functional"
   :style: table
   :columns: title; id; status; safety
   :colwidths: 30,30,15,15

Assumptions of Use
------------------

Assumptions on the Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generally the assumption of the project platform SEooC is that it is integrated in a safe system, i.e. the POSIX OS it runs on is qualified and also the HW related failures are taken into account by the system integrator, if not otherwise stated in the module's safety concept.

**<List here all the OS calls the project platform expects to be safe.>**

List of AoUs expected from the environment the platform runs on:

.. needtable::
   :filter: docname is not None and "platform" in docname and "assumptions" in docname
   :style: table
   :types: aou_req
   :tags: environment
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

Assumptions on the User
^^^^^^^^^^^^^^^^^^^^^^^

As there is no assumption on which specific OS and HW is used, the integration testing of the stakeholder and feature requirements is expected to be performed by the user of the platform SEooC. Tests covering all stakeholder and feature requirements performed on a reference platform (tbd link to reference platform specification), reviewed and passed are included in the platform SEooC safety package.
Additionally the components of the platform may have additional specific assumptions how they are used. These are part of every module documentation: <link to add>. Assumptions from components to their users can be fulfilled in two ways:

1. There are assumption which need to be fulfilled by all SW components, e.g. "every user of an IPC mechanism needs to make sure that he provides correct data (including appropriate ASIL level)" - in this case the AoU is marked as "platform".
2. There are assumption which can be fulfilled by a safety mechanism realized by some other project platform component and are therefore not relevant for an user who uses the whole platform. But those are relevant if you chose to use the module SEooC stand-alone - in this case the AoU is marked as "module". An example would be the "JSON read" which requires "The user shall provide a string as input which is not corrupted due to HW or QM SW errors." - which is covered when using together with safe project platform persistency feature.

List of AoUs on the user of the platform features or the module of this safety manual:

.. needtable::
   :filter: docname is not None and "platform" in docname and "assumptions" in docname
   :style: table
   :types: aou_req
   :tags: user
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

Safety concept of the SEooC
---------------------------

The S-CORE SW platform has no safety concept additional to its module's safety concept, as it does not implement additional functionality.
The expectations towards the execution environment are described in the respective AoU, this is mainly that a safe posix operating system
integrated into a target hardware which includes safety mechanisms which cover hardware related errors.


Safety Anomalies
----------------

Anomalies (bugs in ASIL SW, detected by testing or by users, which could not be fixed) known before release are documented in the platform/module release notes <add link to release note>.

References
----------

:need:`doc__platform_handbook`

`Baselibs Safety Manual <https://eclipse-score.github.io/score/main/modules/baselibs/docs/manual/safety_manual.html>`_

`IPC Safety Manual <https://eclipse-score.github.io/score/main/modules/communication/docs/manual/safety_manual.html>`_

`FEO Safety Manual <https://eclipse-score.github.io/score/main/modules/feo/docs/manual/safety_manual.html>`_

`KVS Safety Manual <https://eclipse-score.github.io/persistency/main/persistency/manual/safety_manual.html>`_
