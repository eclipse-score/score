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

.. document:: Documentation Management Plan
   :id: doc__documentation_mgt_plan
   :status: draft
   :safety: ASIL_B
   :tags: platform_management
   :realizes: PROCESS_wp__document_mgt_plan

Documentation Management Plan
-----------------------------

Purpose
+++++++

The documentation management plan describes how documents are handled in the S-CORE project.

Objectives and scope
++++++++++++++++++++

Goal of this plan is to describe

* which documents exist
* which attributes and lifecycle they have
* how they are reviewed

Approach
++++++++

Some of the work products of the S-CORE project are modelled specifically
(e.g. the requirements and architecture have a specific set of attributes)
Others are modelled as general documents (e.g. the plans which are part of the program management plan or the verification reports).

This plan deals with these documents, which have the following manually set attributes:

* Title: the name of the document (mandatory)
* Unique Id: Id following the naming pattern of the document Title (mandatory)
* Safety: which ASIL the document supports (mandatory)
* Author: Who is the main committer to the document (mandatory)
* Status: describing where in the lifecycle of the document it currently is (mandatory)
* Tags: can be used to group documents for subsequent filtering (optional)

Also the "Documentation Management" is a document, so an example for a correct document definition
can be seen in the header section above, see :need:`doc__documentation_mgt_plan`.

The following additional attributes of the document are generated automatically during the documentation build:

* Approver: from the github information on who was the last CODEOWNER performing the github review
* Reviewer: any additional reviewer performing the github review without CODEOWNER rights

The lifecycle of S-CORE documents has two states:

* Draft: The document is filled with content but not completed, the existing content is reviewed and already applicable
* Valid: The document is completed and approved

If a document is invalidated it is removed from the project entirely. A document can also transition from Valid to Draft,
for example if a release was done with a Valid verification report and then the development for the next release is started.

Invalidated documents are still observable as part of the git history in the unlikely case of later referral
(e.g. for design decisions or audit). In this way, there is even an option to recover the content.

The review of each document is done as defined for this type of work product in the respective process description.
This means that for some of the work products dedicated checklists are defined, but for others there are not.
In any case the reviews are done in a github review at least by one CODEOWNER who is not the author of the document.

Generally all work products (specific and general documents) are subject to a documentation build,
which always contains the latest version of the documents for each pull-request.
Versioning of documents is done as for every work product with github means and is defined in the configuration management plan.

.. _project_documents_list:

The following table lists all documents of the S-CORE project:

.. needtable::
   :style: table
   :columns: title;id;status;tags
   :colwidths: 25,25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["document"]):
      results.append(need)
