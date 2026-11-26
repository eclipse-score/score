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


.. document:: Stakeholder Requirements Inspection Checklist - AoU
   :id: doc__stakeholder_req_inspection_aou
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_inspect[version==1]


Platform AoU Inspection
=======================

Purpose
-------

The purpose of this requirement inspection checklist is to collect the topics to be checked during requirements inspection.

Conduct
-------

As described in the concept :need:`doc_concept__wp_inspections` the following "inspection roles" are expected to be filled:

- content responsible (author): `<https://github.com/aschemmel-tech>`_
- reviewer: `<https://github.com/masc2023>`_,`<https://github.com/NN-Architect>`_
- moderator: `<https://github.com/aschemmel-tech>`_

Checklist
---------

It is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additionally to add in the remarks why it is passed or not passed.
In case of "no" an issue link to the issue tracking system has to be added in the last column (if not solved in the same issue).
See also :need:`doc_concept__wp_inspections` for further information about reviews in general and inspection in particular.

.. list-table:: Stakeholder Requirement Inspection Checklist
    :header-rows: 1
    :widths: 10,30,50,6,6,8

    * - Review ID
      - Acceptance Criteria
      - Guidance
      - Passed
      - Remarks
      - Issue link
    * - REQ_01_01
      - Is the requirement formulation template used?
      - see :need:`gd_temp__req_formulation`, this includes the use of "shall".
      -
      -
      -
    * - REQ_02_01
      - Is the requirement description *comprehensible* ?
      - If you think the requirement is hard to understand, comment here.
      -
      -
      -
    * - REQ_02_02
      - Is the requirement description *unambiguous* ?
      - Especially search for "weak words" like "about", "etc.", "relevant" and others (see the internet documentation on this). This check shall be supported by tooling.
      -
      - Automated weak word check is enabled.
      -
    * - REQ_02_03
      - Is the requirement description *atomic* ?
      - A good way to think about this is to consider if the requirement may be tested by one (positive) test case or needs more of these. The requirement formulation template should also avoid being non-atomic already. Note that there are cases where also non-atomic requirements are the better ones, for example if those are better understandable.
      -
      -
      -
    * - REQ_02_04
      - Is the requirement description *feasible* ?
      - If at the time of the inspection the requirement has already some implementation, the answer is yes. This can be checked via traces, but also :need:`gd_req__req_attr_impl` shows this. In case the requirement has no implementation at the time of inspection (i.e. not implemented at least as "proof-of-concept"), a development expert should be invited to the Pull-Request review to explicitly check this item.
      -
      -
      -
    * - REQ_02_05
      - Is the requirement description *independent from implementation* ?
      - This checkpoint should improve requirements definition in the sense that the "what" is described and not the "how" - the latter should be described in architecture/design derived from the requirement. But there can also be a good reason for this, for example we would require using a file format like JSON and even specify the formatting standard already on stakeholder requirement level because we want to be compatible. A finding in this checkpoint does not mean there is a safety problem in the requirement.
      -
      -
      -
    * - REQ_03_01
      - Is the *rationale* correct?
      - Rationales explain why the stakeholder level requirements were created. Do those cover the requirement?
      - n/a for AoU
      - n/a for AoU
      - n/a for AoU
    * - REQ_04_01
      - Is the requirement *internally and externally consistent*?
      - Does the requirement contradict other requirements within the same or higher levels? Is the description of the requirement consistent with all its attributes (if not already part of another check, e.g. does the title fit?).
      -
      -
      -
    * - REQ_05_01
      - Do the software requirements consider *timing constraints*?
      - This checkpoint encourages to think about timing constraints even if those are not explicitly mentioned in the parent requirement. If the reviewer of a requirement already knows or suspects that the code execution will be consuming a lot of time, one should think of the expectation of a "user".
      -
      -
      -
    * - REQ_06_01
      - Does the requirement consider *external interfaces*?
      - This check is not needed, as on the level of stakeholder requirements interfaces do not need to be used to describe the function.
      - n/a
      - n/a
      - n/a
    * - REQ_07_01
      - Is the *safety* attribute set correctly?
      - For the top level requirements (and also all AoU) this needs to be checked manually for correctness.
      -
      -
      -
    * - REQ_07_02
      - Is the *security* attribute set correctly?
      - For the top level requirements (and also all AoU) this needs to be checked manually for correctness.
      -
      -
      -
    * - REQ_08_01
      - Is the requirement *verifiable*?
      - As the stakeholder requirements are only "assumed safety requirements" and also the tests do not need to be complete, this check is not applicable.
      - n/a
      - n/a
      - n/a
    * - REQ_09_01
      - Do those requirements cover assumed safety mechanisms needed by the hardware and system?
      - Note that stakeholder requirements covering safety mechanisms come from rationales.
      -
      -
      -

Note: If a Review ID is not applicable for your requirement, then state ""n/a" in status and comment accordingly in remarks.

The following AoUs in "valid_inspected" state are in the scope of this inspection:

.. needtable::
   :filter: "platform_assumptions" in docname and "requirements" in docname and docname is not None and status == "valid_inspected"
   :style: table
   :types: aou_req
   :columns: id;status;tags;safety;security
   :colwidths: 25,15,15,10,10
   :sort: title
