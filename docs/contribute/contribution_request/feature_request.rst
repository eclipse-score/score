..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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


Feature Request Guideline
##############################

.. document:: Feature Request Guideline
  :id: doc__feature_request_guideline
  :status: valid
  :safety: QM
  :security: NO
  :realizes: wp__training_path

This Feature Request Guideline is a "How-To for Dummies" for proposing/contributing a new feature or changes to an existing feature.
This Guideline is based on or references following documents:

* :ref:`Contribution Guideline <contribute_contribution_guideline>`
* :ref:`Change Management Plan <change_mgmt_plan>`
* :need:`Feature Template <gd_temp__change_feature_request>`

Creation of Feature Request
================================
.. _feature_request_guideline:


1. As the very first step, you will need to become an official contributor, as described in
`Actions to Ensure Proper Contribution  <https://eclipse-score.github.io/score/main/contribute/general/contribution_attribution.html#contribution-attribution>`_

2. Afterwards you will be able to create a GitHub Issue in the main `score repository <https://github.com/eclipse-score>`_
and mark it

* with label *feature_request* if you want to propose a new feature, or
* with label *feature_modification* if you want to propose changes to an existing feature,

as described in the :ref:`Change Management Plan <change_mgmt_plan>`.

Please put a short description of your *feature request* into the GitHub Issue description, so that
everyone can immediately understand, what the *feature request* is about.

The acceptance criteria for a feature request to be accepted are:

.. code-block:: markdown

  - Feature Request is written according to the [Change Management](https://eclipse-score.github.io/score/main/process/process_areas/change_management/change_management_concept.html) & [Feature Request Template](https://eclipse-score.github.io/score/main/process/process_areas/change_management/guidance/change_management_feature_template.html)
  - Feature requirements written according to the [Requirements Engineering](https://eclipse-score.github.io/score/main/process/process_areas/requirements_engineering/requirements_concept.html)
  - If necessary: extend the stakeholder requirements written according to the [Requirements Engineering](https://eclipse-score.github.io/score/main/process/process_areas/requirements_engineering/requirements_concept.html)


Technical Leads review regularly all new incoming *feature requests* (GitHub Issues labeled as *feature_request* or *feature_modification*).
This happens normally on Monday in the `Technical Lead circle <https://github.com/orgs/eclipse-score/discussions/104>`_.
As soon as you've labeled your GitHub Issue with *feature request*/*feature_modification* label,
TLs will see the *feature request* and will add it to the special GitHub project,
`Feature Request GitHub Project <https://github.com/orgs/eclipse-score/projects/4>`_.
Inside of this *Feature Request GitHub Project* additional states, as shown in the table below,
are used for a better tracking of the *feature requests*.
These states symbolize the status of the *feature request* and not the "GitHub" states of the issue, therefore we will further speak about
*feature request status*. The initial status of every *feature request* is set to "Draft".

======================       ====================
FR status                    Description
======================       ====================
**Draft**                    Feature Request is in the initial state
**In Progress**              This is actively being worked on
**In Review**                Feature Request should be reviewed by the technical leads
**Accepted**                 Feature Request was accepted
**Rejected**                 Feature request was rejected
**Changes Requested**        Changes requested
**POC Needed**               "Proof of concept" in incubation repository is needed
======================       ====================

3. After you have created a GitHub Issue, next step would be to start working on the *feature request*.
First of all, change the status of *Feature Request* to "in Progress" state.
*Feature Requests*, that stay in the status "Draft" longer as 4 weeks, will be deleted.
Afterwards create a PR with your proposal in the `/docs/features <https://github.com/eclipse-score/score/tree/main/docs/features>`_ score repository.
There you will find currently existing features as subfolders. Please choose the one that fits your *feature request* the most or
create a new subfolder, if none of existing feature match your *feature request*. Please take care, that the PR follows the :need:`Feature Template <gd_temp__change_feature_request>`.
You should try to put as much information as possible, as a good exhaustive description is a prerequisite for *feature request* to be accepted.

It is important to understand, that *feature request* consists of an GitHub Issue, that is used to track organizational information and
PR, that contains the technical content. This is explained once again in detailed in the :ref:`Change Management Worlflow <change_mgmt_workflow>`
chapter of :ref:`Change Management Plan <change_mgmt_plan>` document. GitHub Issue always stays assigned to the owner of the *feature request*.
*Feature Request* PR will always be assigned to the owner of the *feature request* as well, but will additionally get the list of reviewers, that
should review this *feature request* PR.


Review of Feature Request
================================
* As soon as you're done with description of your *feature request*, please put the status into "Ready for Review" so that Technical Leads know,
  that they can start with the process of reviewing the *feature request*. Technical Leads will first do a short review of your *feature request*:

  * In case the impact of your *feature request* is trivial, then TLs can process your *feature request* immediately.
  * Normally, TL circle will put the lead of the appropriate *FT* or *Community* as reviewer to the corresponding PR of the *feature request* for better analysis.
    The CTF/Community lead will change the status of the *feature request* issue to "in Review" as soon as they will start reviewing your *feature request*.
    The review can be delegated to any other participants of the FT or Community.

    * In case *feature request* can not be clearly assigned to any already existing team, Technical Lead circle will pick at least two suitable candidates
      from the project to review the *feature request* PR. In that case, *feature request* should be reviewed by all reviewers.

  * In case of big architectural impact, Technical Lead circle can additionally decide to request a review for *feature request* PR from software architecture community.

* After the review is done, the TL circle will set the status of the *feature request* accordingly and will
  also put all further necessary information as GitHub Issue comments. The outcome of the review could be like following:

  * **Accepted** - You *feature request* is accepted. The *feature request* GitHub Issue should contain now a link to a new GitHub issue of type 'Epic',
    that was created by Technical Leads, where detailed information regarding your feature is documented.
    The epic should be also already assigned to the corresponding team (FT/Community).
    If none of the FTs/Communities match the new *feature request*, then a new FT/Community will be founded.
    You will be invited to the FT/Community for break down of the *feature request* and planning.
    You can now merge the *feature request* PR and close the *feature request* issue.
  * **Rejected** - You *feature request* was rejected. It could be either because your description was
    not mature enough or because the proposal technically doesn't fit into S-CORE roadmap or architecture.
    You will be able to find the summary of the review in the corresponding *feature request* issue comments.
    The review comments will be done directly in the *feature request* PR.
  * **Changes Requested** - We like your idea, but we would like to request some modifications.
    This could be rather technical topics or also syntax issues in the description.
    You will be able to find the summary of the review in the corresponding *feature request* issue comments.
    The review comments will be done directly in the *feature request* PR.
  * **POC needed** - We generally like your idea, but we don't have enough technical understanding of the *feature request*,
    e.g. technical scope is too big, and we need a POC to be able to understand better,
    how the proposed *feature request* fits into the overall solution. You will find in the GitHub issue comments
    the decsription for both the scope of the PoC and the requirements and the acceptance criteria for the requested PoC.
    Also, a so called *incubation repository* will be created by the reviewers of the *feature request*, where you should implement your POC.
    Please be aware, that POC is not a guarantee, that you *feature request* will be accepted.
