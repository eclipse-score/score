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
   :safety: ASIL_B
   :security: YES
   :tags: platform_management
   :realizes: wp__document_mgt_plan

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


docs/glossary
#############

.. _documents_docs_glossary:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "glossary/" in need["docname"]:
          results.append(need)


docs/contribute
###############

.. _documents_docs_contribute:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "contribute/" in need["docname"]:
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


docs/requirements
#################

.. _documents_docs_requirements:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "requirements/" in need["docname"] and not "features/" in need["docname"] and not "modules/" in need["docname"]:
          results.append(need)


docs/quality
############

.. _documents_docs_quality:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "quality/" in need["docname"]:
          results.append(need)


docs/safety
###########

.. _documents_docs_safety:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "safety/" in need["docname"]:
          results.append(need)


docs/security
#############

.. _documents_docs_security:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "security/" in need["docname"]:
          results.append(need)


docs/score_tools
################

.. _documents_docs_score_tools:

.. needtable::
   :style: table
   :columns: title;id;safety_affected;security_affected;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["doc_tool"]):
       if need["docname"] is not None and "score_tools/" in need["docname"]:
          results.append(need)


docs/verification_report
########################

.. _documents_docs_verification_report:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "verification_report/" in need["docname"]:
          results.append(need)


platform_integration_tests
###############################

.. _documents_docs_platform_integration_tests:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "platform_integration_tests/" in need["docname"]:
          results.append(need)


docs/manuals
############

.. _documents_docs_manuals:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "manuals/" in need["docname"]:
          results.append(need)


docs/score_releases
###################

.. _documents_docs_score_releases:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "score_releases/" in need["docname"]:
          results.append(need)



.. _documents_docs_features:


Feature documentation
+++++++++++++++++++++

In the following sections all documents of the features and related modules (components), that are
planned for release v0.5, are listed.

.. docs/features/ai_platform
.. #########################

.. .. _documents_docs_features_ai_platform:

.. .. needtable::
..    :style: table
..    :columns: title;id;safety;security;status
..    :colwidths: 25,45,10,10,10
..    :sort: id

..    results = []
..    name = "ai_platform"

..    # Generate list of all documents of the feature
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
..           results.append(need)

..    # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
..    for need in needs.filter_types(["document"]):
..       if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

..          act_id = need["id"].replace("doc__feature_name", "")

..          i = 0

..          for x in results:
..              if act_id in x["id"]:
..                 i = i+1

..          if i == 0:
..              need["title"] = need["title"]
..              results.append(need)

.. docs/features/analysis_infra
.. ############################

.. .. _documents_docs_features_analysis_infra:

.. .. needtable::
..    :style: table
..    :columns: title;id;safety;security;status
..    :colwidths: 25,45,10,10,10
..    :sort: id

..    results = []
..    name = "analysis_infra"

..    # Generate list of all documents of the feature
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
..           results.append(need)

..    # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
..    for need in needs.filter_types(["document"]):
..       if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

..          act_id = need["id"].replace("doc__feature_name", "")

..          i = 0

..          for x in results:
..              if act_id in x["id"]:
..                 i = i+1

..          if i == 0:
..              need["title"] = need["title"]
..              results.append(need)

docs/features/baselibs
######################

.. _documents_docs_features_baselibs:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "baselibs"

   # Generate list of all documents of the feature
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

         act_id = need["id"].replace("doc__feature_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)

docs/features/communication
###########################

.. _documents_docs_features_communication:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "communication"

   # Generate list of all documents of the feature
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

         act_id = need["id"].replace("doc__feature_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)

.. docs/features/diagnostics
.. #########################

.. .. _documents_docs_features_diagnostics:

.. .. needtable::
..    :style: table
..    :columns: title;id;safety;security;status
..    :colwidths: 25,45,10,10,10
..    :sort: id

..    results = []
..    name = "diagnostics"

..    # Generate list of all documents of the feature
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
..           results.append(need)

..    # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
..    for need in needs.filter_types(["document"]):
..       if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

..          act_id = need["id"].replace("doc__feature_name", "")

..          i = 0

..          for x in results:
..              if act_id in x["id"]:
..                 i = i+1

..          if i == 0:
..              need["title"] = need["title"]
..              results.append(need)

docs/features/frameworks
########################

.. _documents_docs_features_frameworks:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "frameworks"

   # Generate list of all documents of the feature
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

         act_id = need["id"].replace("doc__feature_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)

.. docs/features/infrastructure
.. ############################

.. .. _documents_docs_features_infrastructure:

.. .. needtable::
..    :style: table
..    :columns: title;id;safety;security;status
..    :colwidths: 25,45,10,10,10
..    :sort: id

..    results = []
..    name = "infrastructure"

..    # Generate list of all documents of the feature
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
..           results.append(need)

..    # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
..    for need in needs.filter_types(["document"]):
..       if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

..          act_id = need["id"].replace("doc__feature_name", "")

..          i = 0

..          for x in results:
..              if act_id in x["id"]:
..                 i = i+1

..          if i == 0:
..              need["title"] = need["title"]
..              results.append(need)

.. docs/features/integration
.. #########################

.. .. _documents_docs_features_integration:

.. .. needtable::
..    :style: table
..    :columns: title;id;safety;security;status
..    :colwidths: 25,45,10,10,10
..    :sort: id

..    results = []
..    name = "integration"

..    # Generate list of all documents of the feature
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
..           results.append(need)

..    # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
..    for need in needs.filter_types(["document"]):
..       if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

..          act_id = need["id"].replace("doc__feature_name", "")

..          i = 0

..          for x in results:
..              if act_id in x["id"]:
..                 i = i+1

..          if i == 0:
..              need["title"] = need["title"]
..              results.append(need)

.. docs/features/lifecycle
.. #######################

.. .. _documents_docs_features_lifecycle:

.. .. needtable::
..    :style: table
..    :columns: title;id;safety;security;status
..    :colwidths: 25,45,10,10,10
..    :sort: id

..    results = []
..    name = "lifecycle"

..    # Generate list of all documents of the feature
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
..           results.append(need)

..    # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
..    for need in needs.filter_types(["document"]):
..       if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

..          act_id = need["id"].replace("doc__feature_name", "")

..          i = 0

..          for x in results:
..              if act_id in x["id"]:
..                 i = i+1

..          if i == 0:
..              need["title"] = need["title"]
..              results.append(need)

docs/features/orchestration
###########################

.. _documents_docs_features_orchestration:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "orchestration"

   # Generate list of all documents of the feature
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

         act_id = need["id"].replace("doc__feature_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)

docs/features/persistency
#########################

.. _documents_docs_features_persistency:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "persistency"

   # Generate list of all documents of the feature
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

         act_id = need["id"].replace("doc__feature_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)

.. docs/features/time
.. ##################

.. .. _documents_docs_features_time:

.. .. needtable::
..    :style: table
..    :columns: title;id;safety;security;status
..    :colwidths: 25,45,10,10,10
..    :sort: id

..    results = []
..    name = "time"

..    # Generate list of all documents of the feature
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and name in need["docname"] and "features/" in need["docname"]:
..           results.append(need)

..    # Check all documents in folder documents related to features against the found documents. If missing the template is add to the list
..    for need in needs.filter_types(["document"]):
..       if "template" in need["tags"] and "PROCESS" in need["id"] and "feature_name" in need["id"]:

..          act_id = need["id"].replace("doc__feature_name", "")

..          i = 0

..          for x in results:
..              if act_id in x["id"]:
..                 i = i+1

..          if i == 0:
..              need["title"] = need["title"]
..              results.append(need)


.. _documents_docs_modules:

Modules documentation
+++++++++++++++++++++

docs/modules/baselibs/docs
##########################

.. _documents_docs_modules_baselibs_docs:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "baselibs"

   # Generate list of all documents of the module
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name + "/docs/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to modules against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "module_name" in need["id"]:

         act_id = need["id"].replace("doc__module_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)


docs/modules/communication/docs
###############################

.. _documents_docs_modules_communication_docs:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "communication"

   # Generate list of all documents of the module
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name + "/docs/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to modules against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "module_name" in need["id"]:

         act_id = need["id"].replace("doc__module_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)


docs/modules/feo/docs
#####################

.. _documents_docs_modules_feo_docs:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "feo"

   # Generate list of all documents of the module
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name + "/docs/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to modules against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "module_name" in need["id"]:

         act_id = need["id"].replace("doc__module_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)


.. docs/modules/lifecycle/docs
.. ###########################

.. .. _documents_docs_modules_lifecycle_docs:

.. .. needtable::
..    :style: table
..    :columns: title;id;safety;security;status
..    :colwidths: 25,45,10,10,10
..    :sort: id

..    results = []
..    name = "lifecycle"

..    # Generate list of all documents of the module
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and "modules/" + name + "/docs/" in need["docname"]:
..           results.append(need)

..    # Check all documents in folder documents related to modules against the found documents. If missing the template is add to the list
..    for need in needs.filter_types(["document"]):
..       if "template" in need["tags"] and "PROCESS" in need["id"] and "module_name" in need["id"]:

..          act_id = need["id"].replace("doc__module_name", "")

..          i = 0

..          for x in results:
..              if act_id in x["id"]:
..                 i = i+1

..          if i == 0:
..              need["title"] = need["title"]
..              results.append(need)


docs/modules/logging/docs
#########################

.. _documents_docs_modules_logging_docs:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "logging"

   # Generate list of all documents of the module
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name + "/docs/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to modules against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "module_name" in need["id"]:

         act_id = need["id"].replace("doc__module_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)


docs/modules/os/docs
####################

.. _documents_docs_modules_os_docs:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "os"

   # Generate list of all documents of the module
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name + "/docs/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to modules against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "module_name" in need["id"]:

         act_id = need["id"].replace("doc__module_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)


docs/modules/persistency/docs
#############################

.. _documents_docs_modules_persistency_docs:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "persistency"

   # Generate list of all documents of the module
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name + "/docs/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to modules against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "module_name" in need["id"]:

         act_id = need["id"].replace("doc__module_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)


docs/modules/tracing/docs
#########################

.. _documents_docs_modules_tracing_docs:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   name = "tracing"

   # Generate list of all documents of the module
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name + "/docs/" in need["docname"]:
          results.append(need)

   # Check all documents in folder documents related to modules against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
      if "template" in need["tags"] and "PROCESS" in need["id"] and "module_name" in need["id"]:

         act_id = need["id"].replace("doc__module_name", "")

         i = 0

         for x in results:
             if act_id in x["id"]:
                i = i+1

         if i == 0:
             need["title"] = need["title"]
             results.append(need)


.. _documents_docs_modules_components:


Components documentation
++++++++++++++++++++++++


docs/modules/baselibs/components
################################

.. _documents_docs_modules_baselibs_components:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   components = []
   name = "baselibs"

   # Generate list of all documents of the component(s)
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             results.append(need)

   # The folder(s) of the component(s) will be identified and added to a list. After that all documents in folder documents related to component checked against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             component_name = need["docname"]
             component_name = component_name.split("/")[2]

             n = 0
             for x in components:
                if component_name == x:
                   n = 1

             if n == 0:

                # List of all templates will be checked against the documents of the component if documents are missing or wrong named
                for need in needs.filter_types(["document"]):
                   if "template" in need["tags"] and "PROCESS" in need["id"] and "component_name" in need["id"]:

                      act_id = need["id"].replace("doc__component_name", "")

                      i = 0

                      for x in results:
                         if act_id in x["id"] and component_name in x["id"]:
                            i = i+1

                      if i == 0:
                         need["title"] = need["title"]
                         results.append(need)

             components.append(component_name)


docs/modules/communication/components
#####################################

.. _documents_docs_modules_communication_components:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   components = []
   name = "communication"

   # Generate list of all documents of the component(s)
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             results.append(need)

   # The folder(s) of the component(s) will be identified and added to a list. After that all documents in folder documents related to component checked against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             component_name = need["docname"]
             component_name = component_name.split("/")[2]

             n = 0
             for x in components:
                if component_name == x:
                   n = 1

             if n == 0:

                # List of all templates will be checked against the documents of the component if documents are missing or wrong named
                for need in needs.filter_types(["document"]):
                   if "template" in need["tags"] and "PROCESS" in need["id"] and "component_name" in need["id"]:

                      act_id = need["id"].replace("doc__component_name", "")

                      i = 0

                      for x in results:
                         if act_id in x["id"] and component_name in x["id"]:
                            i = i+1

                      if i == 0:
                         need["title"] = need["title"]
                         results.append(need)

             components.append(component_name)


docs/modules/feo/components
###########################

.. _documents_docs_modules_feo_components:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   components = []
   name = "feo"

   # Generate list of all documents of the component(s)
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             results.append(need)

   # The folder(s) of the component(s) will be identified and added to a list. After that all documents in folder documents related to component checked against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             component_name = need["docname"]
             component_name = component_name.split("/")[2]

             n = 0
             for x in components:
                if component_name == x:
                   n = 1

             if n == 0:

                # List of all templates will be checked against the documents of the component if documents are missing or wrong named
                for need in needs.filter_types(["document"]):
                   if "template" in need["tags"] and "PROCESS" in need["id"] and "component_name" in need["id"]:

                      act_id = need["id"].replace("doc__component_name", "")

                      i = 0

                      for x in results:
                         if act_id in x["id"] and component_name in x["id"]:
                            i = i+1

                      if i == 0:
                         need["title"] = need["title"]
                         results.append(need)

             components.append(component_name)


.. docs/modules/lifecycle/components
.. #################################

.. .. _documents_docs_modules_lifecycle_components:

.. .. needtable::
..    :style: table
..    :columns: title;id;safety;security;status
..    :colwidths: 25,45,10,10,10
..    :sort: id

..    results = []
..    components = []
..    name = "lifecycle"

..    # Generate list of all documents of the component(s)
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and "modules/" + name in need["docname"]:
..           if not "modules/" + name + "/docs/" in need["docname"]:
..              results.append(need)

..    # The folder(s) of the component(s) will be identified and added to a list. After that all documents in folder documents related to component checked against the found documents. If missing the template is add to the list
..    for need in needs.filter_types(["document"]):
..        if need["docname"] is not None and "modules/" + name in need["docname"]:
..           if not "modules/" + name + "/docs/" in need["docname"]:
..              component_name = need["docname"]
..              component_name = component_name.split("/")[2]

..              n = 0
..              for x in components:
..                 if component_name == x:
..                    n = 1

..              if n == 0:

..                 # List of all templates will be checked against the documents of the component if documents are missing or wrong named
..                 for need in needs.filter_types(["document"]):
..                    if "template" in need["tags"] and "PROCESS" in need["id"] and "component_name" in need["id"]:

..                       act_id = need["id"].replace("doc__component_name", "")

..                       i = 0

..                       for x in results:
..                          if act_id in x["id"] and component_name in x["id"]:
..                             i = i+1

..                       if i == 0:
..                          need["title"] = need["title"]
..                          results.append(need)

..              components.append(component_name)


docs/modules/logging/components
###############################

.. _documents_docs_modules_logging_components:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   components = []
   name = "logging"

   # Generate list of all documents of the component(s)
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             results.append(need)

   # The folder(s) of the component(s) will be identified and added to a list. After that all documents in folder documents related to component checked against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             component_name = need["docname"]
             component_name = component_name.split("/")[2]

             n = 0
             for x in components:
                if component_name == x:
                   n = 1

             if n == 0:

                # List of all templates will be checked against the documents of the component if documents are missing or wrong named
                for need in needs.filter_types(["document"]):
                   if "template" in need["tags"] and "PROCESS" in need["id"] and "component_name" in need["id"]:

                      act_id = need["id"].replace("doc__component_name", "")

                      i = 0

                      for x in results:
                         if act_id in x["id"] and component_name in x["id"]:
                            i = i+1

                      if i == 0:
                         need["title"] = need["title"]
                         results.append(need)

             components.append(component_name)


docs/modules/os/components
##########################

.. _documents_docs_modules_os_components:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   components = []
   name = "os"

   # Generate list of all documents of the component(s)
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             results.append(need)

   # The folder(s) of the component(s) will be identified and added to a list. After that all documents in folder documents related to component checked against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             component_name = need["docname"]
             component_name = component_name.split("/")[2]

             n = 0
             for x in components:
                if component_name == x:
                   n = 1

             if n == 0:

                # List of all templates will be checked against the documents of the component if documents are missing or wrong named
                for need in needs.filter_types(["document"]):
                   if "template" in need["tags"] and "PROCESS" in need["id"] and "component_name" in need["id"]:

                      act_id = need["id"].replace("doc__component_name", "")

                      i = 0

                      for x in results:
                         if act_id in x["id"] and component_name in x["id"]:
                            i = i+1

                      if i == 0:
                         need["title"] = need["title"]
                         results.append(need)

             components.append(component_name)


docs/modules/persistency/components
###################################

.. _documents_docs_modules_persistency_components:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   components = []
   name = "persistency"

   # Generate list of all documents of the component(s)
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             results.append(need)

   # The folder(s) of the component(s) will be identified and added to a list. After that all documents in folder documents related to component checked against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             component_name = need["docname"]
             component_name = component_name.split("/")[2]

             n = 0
             for x in components:
                if component_name == x:
                   n = 1

             if n == 0:

                # List of all templates will be checked against the documents of the component if documents are missing or wrong named
                for need in needs.filter_types(["document"]):
                   if "template" in need["tags"] and "PROCESS" in need["id"] and "component_name" in need["id"]:

                      act_id = need["id"].replace("doc__component_name", "")

                      i = 0

                      for x in results:
                         if act_id in x["id"] and component_name in x["id"]:
                            i = i+1

                      if i == 0:
                         need["title"] = need["title"]
                         results.append(need)

             components.append(component_name)


docs/modules/tracing/components
###############################

.. _documents_docs_modules_tracing_components:

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: id

   results = []
   components = []
   name = "tracing"

   # Generate list of all documents of the component(s)
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             results.append(need)

   # The folder(s) of the component(s) will be identified and added to a list. After that all documents in folder documents related to component checked against the found documents. If missing the template is add to the list
   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "modules/" + name in need["docname"]:
          if not "modules/" + name + "/docs/" in need["docname"]:
             component_name = need["docname"]
             component_name = component_name.split("/")[2]

             n = 0
             for x in components:
                if component_name == x:
                   n = 1

             if n == 0:

                # List of all templates will be checked against the documents of the component if documents are missing or wrong named
                for need in needs.filter_types(["document"]):
                   if "template" in need["tags"] and "PROCESS" in need["id"] and "component_name" in need["id"]:

                      act_id = need["id"].replace("doc__component_name", "")

                      i = 0

                      for x in results:
                         if act_id in x["id"] and component_name in x["id"]:
                            i = i+1

                      if i == 0:
                         need["title"] = need["title"]
                         results.append(need)

             components.append(component_name)
