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
   :status: valid
   :version: 2
   :safety: ASIL_B
   :security: YES
   :tags: platform_management
   :realizes: wp__document_mgt_plan[version==1]

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

* Title: The name of the document (mandatory)
* Unique Id: Id following the naming pattern of the document Title (mandatory)
* Safety: Which ASIL the document supports (mandatory)
* Author: Who is the main committer to the document (mandatory, but set automatically by the github information)
* Status: Describing where in the lifecycle of the document it currently is (mandatory)
* Tags: Can be used to group documents for subsequent filtering (optional)

Also the "Documentation Management" is a document, so an example for a correct document definition
can be seen in the header section above, see :need:`doc__documentation_mgt_plan`.

The following additional attributes of the document are generated automatically during the documentation build:

* Approver: from the github information on who was the last CODEOWNER performing the github review
* Reviewer: any additional reviewer performing the github review without CODEOWNER rights

The lifecycle of S-CORE documents has two states:

* Draft: The document is filled with content but not completed, the existing content is reviewed and already applicable
* Valid: The document is completed and approved

If a document is invalidated it is removed from the project entirely. A document can also transition from valid to draft,
for example if a release was done with a valid verification report and then the development for the next release is started.

Invalidated documents are still observable as part of the git history in the unlikely case of later referral
(e.g. for design decisions or audit). In this way, there is even an option to recover the content.

The review of each document is done as defined for this type of work product in the respective process description.
This means that for some of the work products dedicated checklists are defined, but for others there are not.
In any case the reviews are done in a github review at least by one CODEOWNER who is not the author of the document.

Generally all work products (specific and general documents) are subject to a documentation build,
which always contains the latest version of the documents for each pull-request.
Versioning of documents is done as for every work product with github means and is defined in the configuration management plan.

The time schedule is not part of the documentation management plan. As described in the project management plan GitHub issues
is used to plan and track the work.

The following tables lists all documents. The documentation is structured in several folders :ref:`platform_folder_structure`,
each representing a specific aspect of the project. The following sections lists all documents that are available in each folder.
Afterwards an additional section is provided with the collected documents for the features, modules and components. Missing
documents are listed as well, so that it is easy to identify missing documents.


.. _project_documents_list:


Platform documentation
++++++++++++++++++++++

.. _documents_docs_contribute:

docs/contribute
###############

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "contribute/" in need["docname"]:
          results.append(need)


.. _documents_docs_glossary:

docs/glossary
#############

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "glossary/" in need["docname"]:
          results.append(need)


.. _documents_docs_handbook:

docs/handbook
#############

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "handbook/" in need["docname"]:
          results.append(need)

.. _documents_docs_manuals:

docs/manuals
#############

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "manuals/" in need["docname"]:
          results.append(need)

.. _doc_platform_management_plan:

docs/platform_management_plan
#############################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "platform_management_plan/" in need["docname"]:
          results.append(need)

.. _documents_docs_quality:

docs/quality
############

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "quality/" in need["docname"]:
          results.append(need)

.. _documents_docs_requirements:

docs/requirements
#################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "requirements/" in need["docname"] and not "features/" in need["docname"] and not "modules/" in need["docname"]:
          results.append(need)

.. _documents_docs_safety:

docs/safety
###########

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "safety/" in need["docname"]:
          results.append(need)

.. _documents_docs_score_tools:

docs/score_tools
################

.. needtable::
   :style: table
   :columns: title;id;safety_affected;security_affected;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["doc_tool"]):
       if need["docname"] is not None and "score_tools/" in need["docname"]:
          results.append(need)

.. _documents_docs_security:

docs/security
#############

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "security/" in need["docname"]:
          results.append(need)

.. _documents_docs_tools:

docs/tools
##########

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "tools/" in need["docname"]:
          results.append(need)


.. _documents_docs_features:

Feature documentation
+++++++++++++++++++++

In the following sections all documents of the features and related modules (components), that are
planned for release v0.5, are listed.

.. _documents_docs_features_baselibs:

docs/features/baselibs
######################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "features/baselibs/" in need["docname"]:
          results.append(need)

.. _documents_docs_features_communication:

docs/features/communication
###########################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "features/communication/" in need["docname"]:
          results.append(need)

.. _documents_docs_features_frameworks:

docs/features/frameworks
########################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "features/frameworks/" in need["docname"]:
          results.append(need)

.. _documents_docs_features_orchestration:

docs/features/orchestration
###########################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "features/orchestration/" in need["docname"]:
          results.append(need)

.. _documents_docs_features_persistency:

docs/features/persistency
#########################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "features/persistency/" in need["docname"]:
          results.append(need)


.. _documents_docs_modules:

Modules documentation
+++++++++++++++++++++

.. _documents_docs_modules_communication_docs:

docs/modules/communication/docs
###############################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/communication/" in need["docname"]:
          results.append(need)

.. _documents_docs_modules_feo_docs:

docs/modules/feo/docs
#####################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/feo/" in need["docname"]:
          results.append(need)


.. _documents_docs_modules_logging_docs:

docs/modules/logging/docs
#########################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/logging/" in need["docname"]:
          results.append(need)

.. _documents_docs_modules_os_docs:

docs/modules/os/docs
####################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/os/" in need["docname"]:
          results.append(need)

.. _documents_docs_modules_tracing_docs:

docs/modules/tracing/docs
#########################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/tracing/" in need["docname"]:
          results.append(need)


.. _documents_docs_modules_components:
