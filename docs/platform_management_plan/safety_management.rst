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

.. _safety_management:

Safety management
------------------------

Purpose
+++++++

Objectives and scope
++++++++++++++++++++

Tailoring
^^^^^^^^^
Tailoring of safety activities:

* The tailoring is divided into project wide and module specific rules.
* Project wide tailoring is documented in this document - this is based on developement of a platform SEooC.
* Module SEooC specific tailoring is documented in the module development Safety Plans - this may be based on SEooC specifics or because component qualification according to ISO 26262 part 8 clause 12 (or ISO PAS 8926) is selected.
* In case of a change request on an existing feature (i.e. a contribution request), the subsequent safety planning will be done based on an impact analysis.

The following ISO26262 defined safety work products are not relevant for the SCORE SW platform development:

Because these are in responsibility of the system integrator: :need:`STD_WP_ISO26262__management_11`,
:need:`STD_WP_ISO26262__system_2`, :need:`STD_WP_ISO26262__system_3`, :need:`STD_WP_ISO26262__system_4`,
:need:`STD_WP_ISO26262__system_5`, :need:`STD_WP_ISO26262__system_6`, :need:`STD_WP_ISO26262__system_7`,
:need:`STD_WP_ISO26262__system_8`, :need:`STD_WP_ISO26262__system_9`, :need:`STD_WP_ISO26262__system_10`,
:need:`STD_WP_ISO26262__system_11`

Because there is no calibration used for the SCORE SW platform components, only configuration: :need:`STD_WP_ISO26262__software_19`,
:need:`STD_WP_ISO26262__software_21`, :need:`STD_WP_ISO26262__software_24`

Because distributed development is not how the project is organized. All contributors are seen as part of the project team.
When used, OSS components are qualified and external SEooCs are integrated in the project scope: :need:`STD_WP_ISO26262__support_1`,
:need:`STD_WP_ISO26262__support_2`, :need:`STD_WP_ISO26262__support_3`, :need:`STD_WP_ISO26262__support_4`, :need:`STD_WP_ISO26262__support_5`

Because in the SCORE SW platform HW elements are out of scope: :need:`STD_WP_ISO26262__support_21`, :need:`STD_WP_ISO26262__support_22`, :need:`STD_WP_ISO26262__support_23`

Because in the SCORE SW platform a proven in use argument will not be applied: :need:`STD_WP_ISO26262__support_24`, :need:`STD_WP_ISO26262__support_25`

Because in the SCORE SW platform interfacing of out of scope of ISO 26262 applications is not planned: :need:`STD_WP_ISO26262__support_26`

Because in the SCORE SW platform integration of safety-related systems not developed according to ISO 26262 is not planned: :need:`STD_WP_ISO26262__support_27`

Because in the SCORE SW platform no ASIL decomposition is planned: :need:`STD_WP_ISO26262__analysis_1`, :need:`STD_WP_ISO26262__analysis_2`



Approach
++++++++
