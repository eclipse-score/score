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

.. gd_guidl:: Feature Request Guideline
  :id: gd_guidl__featr_request_guideline
  :status: valid
  :tags: contribution_management

In case you want to propose or to request a new feature or major changes in an existing feature, you will need to follow Feature Request Guideline.

Creation of Feature Request
================================
* As the very first step, you will need to become of an official contributor, as described in
  `Actions to Ensure Proper Contribution  <https://eclipse-score.github.io/score/main/contribute/general/contribution_attribution.html#contribution-attribution>`_
* Afterwards you will be able to create a GitHub issue and mark it with following label *feature_request*.
* As soon as you've labeled your issue properly, you *feature request* should be visible in `Feature Request GitHub Project <https://github.com/orgs/eclipse-score/projects/4>`_.
  The initial status should be "Draft".
* Next step would be to start working on the *feature request*. First of all, set the corresponding GitHub issue into "in Progress" status.
  Issues, that stay in the status "Draft" for a loner period of time, will be deleted. Depending on the maturity of the *feature request*, following two options are possible:  
  
  * If the Feature Request is "just an idea" and you do not have any concrete requirements,
    feature architecture diagramms  or source code, then you could put the description of you *feature request* directly to the description of the GitHub issues.
    A good exhaustive description is a prerequisite for feature request to be accepted.
  * If you already have some requirements, feature architecture description or code, then you could create a PR in the `score repository <https://github.com/eclipse-score/score/tree/main/docs/features>`_
    with your proposal.  

Review of Feature Request
================================
* As soon as you're done with description of your *feature request*, please put the status into "Ready for Review" so that we know, we can review the *feature request*.
  Technical Leads will do a short review of your *feature request* and will assign it to the appropriate team for better analysis. They will change the status to "in Review" as soon as they will start
  reviewing your *feature request*.
* The outcome of the review could be like following:
  
  * **Accepted** - You feature request is accepted. The technical leads will create a GitHub issue of type 'Epic', where detailed information regarding your feature will be documented.
    Afterwards the epic will be assigned to the corresponding team (CFT/Community). If none of the CFTs/Communities match the new *feature request*, then a new CFT/Community will be founden. You will be invited to 
    the CFT/Community for break down of the *feature request* and planning.
  * **Rejected** - You *feature request* was rejected. It could be either because you description was not mature enough or because the proposal technically doesn't fit into S-CORE roadmap or architecture.
    You will be able to find the result of the review in the corresponding GitHub issue comments.
  * **Changes Requested** - We like your idea, but we would like to request some modifications. This could be rather technical topics or also syntax issues in the description.
    You will find all necessary information in GitHub Issue comments.
  * **POC needed** - We generally like your idea but we don't have enough technical understanding of the feature request, e.g. technical scope is too big, and we need a POC to be able to understand better,
    how the proposed *feature request* fits into the overall solution. You will find in the GitHub issue comments the information what your POC should focus on.
    Also a so called *incubation repository* will be created by the reviewers of the *feature request*, where you should implement your POC.
    Please be aware, that POC is not a guarantee, that you *feature request* will be accepted. 
  

