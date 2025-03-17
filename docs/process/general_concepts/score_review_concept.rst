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

.. _review_concept:

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

        * - :need:`wp__requirements__stkh`
          - :need:`gd_chklst__req__inspection`

        * - :need:`wp__requirements__feat`
          - :need:`gd_chklst__req__inspection`

        * - :need:`wp__requirements__comp`
          - :need:`gd_chklst__req__inspection`

        * - :need:`wp__hsi`
          - :need:`gd_chklst__req__inspection`

        * - :need:`wp__requirements__feat_aou`
          - :need:`gd_chklst__req__inspection`

        * - :need:`wp__requirements__comp_aou`
          - :need:`gd_chklst__req__inspection`

        * - :need:`wp__feature_arch`
          - :need:`gd_chklst__arch__inspection_checklist`

        * - :need:`wp__component_arch`
          - :need:`gd_chklst__arch__inspection_checklist`

        * - :need:`wp__sw_implementation`
          - <link to detailed design and code inspection checklist>

Note that for testcases on unit, component and feature level (as defined in :need:`doc__verification_plan`)
also a review checklist is provided for guidance, but no formal inspection is required. The same is true for Safety Analysis and DFA.
The independence of testing respectively of test case review is covered by the use of GitHub also for the review of test cases.
Which means that at least the test case definition or the test case review is performed by
another person as the author of the verified work product.

Inspection Conduct
^^^^^^^^^^^^^^^^^^

Inspections are conducted by using GitHub mechanisms.
We expect that the requirement and architecture work products need to mature during implementation and testing
and that the inspection checklists also contain questions which can not be answered already at creation of the work product,
because also other work products content also has to be taken into account (which is not available at the beginning,
therefore we use a two-step approach for the review and inspection for these.

The detailed design and coding inspection is not of this kind. Here we define that every PR review
already has the (formal) character of an inspection, i.e. the review checklist is used.
The scope of such a detailed design / code inspection is always the change introduced, as documented in github.
The inspection is initiated by the author of the change and reviewers are invited automatically
based on the CODEOWNER(s) definition of the modified files. In case the fixing of review findings is not agreed
between reviewer(s) and author, the safety manager or quality manager can be added to the review to moderate a solution.

The initial step for requirements and architecture is the (informal) GitHub review on every Pull-Request
(resp. Contribution Request, see :need:`gd_guidl__contr_request_guideline`)
which creates or modifies one of these work products (subject to inspection).
After this review the work products are in status "valid", which means they can be used for further development and verification steps.
In this review the checklist entries shall be considered which are tagged as "incremental".

The last step is initiated by the safety manager, security manager or quality manager:
He asks the main work product author to set the work product's status to "valid(inspected)" and start a Pull-Request (PR).
GitHub will automatically ask for a review by the defined one or more "CODEOWNER" of the work product.
In the PR description the inspection result will be documented for each checklist item
(pass/fail - with link to a ticket for the corrections, or by citing the checklist item in the github comment).
The CODEOWNER(s)=reviewers will fill out the checklist and add their findings on the work product in the PR.
They close their review activity by documenting their verdict as "Approve" or "Request Changes".
Any one "Request Changes" will block the PR from being merged. Note that the PR author cannot "Approve" or "Request Changes".
After all requested reviews were done, the author answers the findings in GitHub comments and/or performs corrections of the work products.
Then the reviewer(s) re-review and adapt their verdict accordingly.
In case the author or the reviewer(s) cannot agree on a solution, the safety/security/quality manger
who initiated the inspection will be asked to moderate this by requesting also his review.

The following picture shall illustrate how a status lifecycle of a requirement workproduct will look like.
The lifecycle for an architecture work product should be similar.

.. figure:: _assets/inspection_workflow.drawio.svg
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
#. After finding resolution, the requirement is merged in valid(inspected) state
#. In case of changes the requirement returns in the valid state

Note: This workflow can be shortcut in case an already mature work product (in this case requirement)
is part of a Pull-Request including already the relevant verification and implementation.
This could be the case when for example merging a development branch back into the main line.
In this case the workflow starts with step 6.

Inspection Know-How
^^^^^^^^^^^^^^^^^^^

For work products with ASIL rating the safety manager shall initiate the inspections,
for those which are QM but are security related the security manger may request this,
but also the quality manager may ask for inspection for critical QM work products.

Judging if the maturity of a work product is already enough to request an inspection
can be based for example for the requiremnts on their "Implemented by", "Verified by" and "Requirement Covered" attribute.
For example when requesting a new feature by filling out the :need:`gd_temp__change__feature_request`
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

Process Requirements
^^^^^^^^^^^^^^^^^^^^

.. gd_req:: Storage of pull requests documentation
   :id: gd_req__general__pull_request_storage
   :status: valid
   :complies: std_req__iso26262__support_9, std_req__iso26262__software_24
   :satisfies: wf__monitor_verify_requirements, wf__mr_vy_arch

   The content of pull requests (conversation, commits, files changed) shall be stored permanently
   for every release.

   Note: Expectation is that this should be part of configuration management, but as this process
   is not defined at the moment this requirement is added here.

.. gd_req:: Hash value for inspected requirements
   :id: gd_req__general__requirements_hash
   :status: valid
   :complies: std_req__iso26262__support_9, std_req__iso26262__software_24
   :satisfies: wf__monitor_verify_requirements, wf__mr_vy_arch

   The hash value of a requirement shall not change by an inspection. In case the status of the
   requirement is used to notify if a requirement is inspected (or another attribute is introduced),
   this shall be ignored for hashing (i.e. hash value for valid and valid(inspected) shall be equal).
   In case hashing is also used for architecture versioning this shall be done in similar way.

.. gd_req:: Checklist templates in pull requests
   :id: gd_req__general__checklist_templates
   :status: valid
   :complies: std_req__iso26262__support_9, std_req__iso26262__software_24, std_req__iso26262__software_31
   :satisfies: wf__monitor_verify_requirements, wf__mr_vy_arch

   For all the pull requests modifying a work product subject to inspection,
   a template for the pull request containing the applicable checklist items shall be provided.
   Ideally this is automatically applied based on the files modified in the PR.
   The requirements and architecture inspections are not automatically applied.

.. gd_req:: Status Check
   :id: gd_req__general__status_check
   :status: valid
   :complies: std_req__iso26262__support_9, std_req__iso26262__software_24
   :satisfies: wf__monitor_verify_requirements, wf__mr_vy_arch

   It shall be checked that only a PR with the inspection checklist filled out can set a status to valid(inspected).
