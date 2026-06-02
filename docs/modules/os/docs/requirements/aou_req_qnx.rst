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

Assumptions of Use - QNX
########################

.. document:: QNX Assumptions of Use
   :id: doc__os_aou_qnx
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp

Note: Document is draft until all relevant restrictions from the QNX safety manual(s) are included.

The assumption of use identifiers below are extracted from all QNX safety manual restrictions for the relevant
components of the "OS". Recommendations are not extracted because S-CORE does not implement these.

The list enables feature teams with access to the QNX safety manual to link to their architecture
(static or dynamic views) the AoUs which their module's components cover.
This can be used by the system integrator as a starting point to show compliance to the QNX AoU.
In the below list all AoU/Restrictions are set to "invalid" if those are not applicable to the S-CORE
SW platform, including an argumentation why.

The verification for such an AoU is done in the same way as for other requirements, i.e. if these are
non-functional and "non-testable" then a "requirement analysis" is done as described in
:need:`doc__component_name_req_inspection` checklist item REQ_08_02. To document this a PR is created
to modify the component architecture "fulfils" attribute, add the respective requirements to the
requirements inspection checklist's scope and document findings like for other inspections.

.. aou_req:: RST-0001
   :id: aou_req__os__rst0001
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   see QNX OsSafetyManual, expect to be verified by requirements analysis

.. aou_req:: RST-0002
   :id: aou_req__os__rst0002
   :reqtype: Non-Functional
   :security: YES
   :safety: ASIL_B
   :status: invalid

   not relevant for S-CORE, no target HW

more to come ...
