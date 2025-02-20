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

Review and Inspection Concept
=============================

.. doc_concept:: Workproduct Inspections Concept
   :id: doc_concept__wp_inspections
   :status: valid

Inspection Definition
^^^^^^^^^^^^^^^^^^^^^

Inspections are formal reviews supported by a checklist with documented conduct and outcome.
In this project there are inspections on the following work products, which are generally performed in the same way:

.. list-table:: Work products subject to inspection
        :header-rows: 1

        * - inspected work product Id
          - Link to checklist

        * - :need:`WP_STAKEHOLDER_REQ`
          - :need:`gd_chklst__req__inspection`

        * - :need:`WP_FEATURE_REQ`
          - :need:`gd_chklst__req__inspection`

        * - :need:`WP_SW_COMPONENT_REQ`
          - :need:`Ggd_chklst__req__inspection`

        * - :need:`WP_HSI`
          - :need:`gd_chklst__req__inspection`

        * - :need:`WP_FEATURE_AOU`
          - :need:`gd_chklst__req__inspection`

        * - :need:`WP_SW_COMPONENT_AOU`
          - :need:`gd_chklst__req__inspection`

        * - :need:`WP_FEATURE_ARCHITECTURE`
          - <link to architecture inspection checklist>

        * - :need:`WP_SW_COMPONENT_ARCHITECTURE`
          - <link to architecture inspection checklist>

        * - :need:`WP_SW_IMPLEMENTATION`
          - <link to detailed design and code inspection checklist>

Note that for testcases on unit, component and feature level (as defined in :ref:`sw_verification`)
also a review checklist is provided for guidance, but no formal inspection is required. The same is true for Safety Analysis and DFA.
The independence of testing respectively of test case review is covered by the use of GitHub also for the review of test cases.
Which means that at least the test case definition or the test case review is performed by
another person as the author of the verified work product.

Inspection Conduct
^^^^^^^^^^^^^^^^^^

Inspections are conducted by using GitHub mechanisms.
We expect that the work products need to mature during implementation and testing,
therefore we use a two-step approach for the review and inspection of work products.

The initial step is the (informal) GitHub review on every Pull-Request
(resp. Contribution Request, see :need:`GD_GUIDL__Contr_Request_Guideline`)
which creates or modifies one of the above work products (subject to inspection).
After this review the work products are in status "valid", which means they can be used for further development and verification steps.
In this review the same checklist as for the inspection should be considered, but need not to be filled out.

The last step is initiated by the safety manager, security manager or quality manager:
He asks the main work product author to set the work product's status to "review" and start a Pull-Request (PR).
GitHub will automatically ask for a review by the defined one or more "CODEOWNER" of the work product.
It is not the goal to merge this status, but to select the scope of the inspection
and use the github mechanisms for review comments and fixes of the work product.
The author additionally creates an Inspection Document by using the foreseen template.
In this document the inspection result will be documented for each checklist item
(pass/fail - with link to a ticket for the corrections, or by citing the checklist item in the github comment).
The CODEOWNER(s)=reviewers will fill out the checklist document and add their findings on the work product in the PR.
They close their review activity by documenting their verdict as "Approve" or "Request Changes".
Any one "Request Changes" will block the PR from being merged. Note that the PR author cannot "Approve" or "Request Changes".
After all requested reviews were done, the author answers the findings in GitHub comments and/or performs corrections of the work products.
Then the reviewer(s) re-review and adapt their verdict accordingly.
In case the author or the reviewer(s) cannot agree on a solution, the safety/security/quality manger
who initiated the inspection will be asked to moderate this by requesting also his review.

During the merge of the "inspection" PR, the PR documentation shall be stored permanently.

The following picture shall illustrate how a status lifecycle of a workproduct (in this example for a component requirement) will look like.

.. figure:: _assets/inspection_workflow.svg
    :width: 80%
    :align: center
    :alt: Inspections Workflow

    Review Inspections Workflow - Requirement Example

#. Create requirement
#. (Informal) Pull-Request Review
#. Merge valid requirement to main
#. During development and verification steps the requirement is reworked and again put to PR Review
#. Implementation and verification workproducts are linked
#. Safety manager initiates a (formal) Pull-Request Inspection
#. Author additionally creates/updates an Inspection Document and adds it to the Pull-Request
#. After finding resolution, the requirement is merged in valid state and as the tooling detects the Inspection Document, it sets "inspected=true"
#. In case of changes the requirement returns in the valid state (with "inspected=false") as the requiremnts version does not match the Inspection Document version

Note: This workflow can be shortcut in case an already mature work product (in this case requirement)
is part of a Pull-Request including already the relevant verification and implementation.
This could be the case when for example merging a development branch back into the main line.
In this case the workflow starts with step 6.

Inspection Know-How
^^^^^^^^^^^^^^^^^^^

For work products with ASIL rating the safety manager shall initiate the inspections,
for those which are QM but are security related the security manger may request this,
but also the quality manager may ask for inspection for critical QM work products.

Judging if the maturity of a work product is already enough to request an inspection (which is not a waste of time)
can be based for example for the requiremnts on their "Implemented by", "Verified by" and "Requirement Covered" attribute.
For example when requesting a new feature by filling out the :need:`GD_TEMP__Feat_Request_Template`
you are asked to also specify the feature's requirements
- it is not expected that the maturity of the requirements is already enough at this time to make a good inspection.
On the other end of a development "lifecycle",
of course all the ASIL rated work products must be in status "inspected" before release,
this is checked as part of the :ref:`release_management`.

Checklist Templates contain hints how to understand the checkpoints or ideas how to check,
these hints are not replicated in every PR documented, but only the checklist questions.
Reviewers shall comment also the checklist items which they mark as passed, as a memory aid,
to be able to later explain what they considered during review
(for example in case a requirement is found to be wrong after the release, to be able to do a lessons learned).

Any workproduct which is subject to inspection and is modified after an inspection
shall transition from "valid(inspected)" back to "valid" state. This shall be automaticly checked.
