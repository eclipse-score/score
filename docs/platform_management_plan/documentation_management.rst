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
   :version: 4
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

The following tables list all documents. The documentation is structured in several folders :ref:`platform_folder_structure`,
each representing a specific aspect of the project. First the documents of the platform folders are listed.
Afterwards the documents are listed per feature: for each feature the feature documents are followed by the
documents of the implementing modules and their components. Finally all further documents, which do not belong
to one of these sections, are listed.

.. note::

   The tables of this plan are generated during the documentation build from the documents which are part of
   that build. Therefore this plan looks different depending on where it is built:

   * **S-CORE platform repository**: only the documents of the platform repository are listed. The module
     repositories are not part of this build, so the module and component tables are empty. Only the module
     documentation still located in the folder ``docs/modules`` of the platform repository is listed there.
     This documentation is not yet transferred into the module repositories, see :ref:`module_folder_structure`.
     Also the section "Further documents" is empty.
   * **Reference integration**: the module repositories and further dependencies (e.g. the process description
     and docs-as-code) are part of the build. Therefore the tables additionally contain the module and component
     documents of these repositories and the section "Further documents" lists the documents of the other dependencies.

   The structure of the plan is the same in both cases.


.. _project_documents_list:

Platform documentation
++++++++++++++++++++++

.. _documents_docs_root:

docs
####

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       if docname and "/" not in docname:
           results.append(need)

.. _documents_docs_architecture:

docs/architecture
#################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       if docname.startswith("architecture/"):
           results.append(need)

.. _documents_docs_contribute:

docs/contribute
###############

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       if docname.startswith("contribute/"):
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
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       if docname.startswith("platform_management_plan/"):
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
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       if docname.startswith("quality/"):
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
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       if docname.startswith("requirements/"):
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
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       if docname.startswith("safety/"):
           results.append(need)

.. _documents_docs_score_tools:

docs/score_tools
################

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       if docname.startswith("score_tools/"):
           results.append(need)

.. needtable::
   :style: table
   :columns: title;id;safety_affected;security_affected;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["doc_tool"]):
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       if docname.startswith("score_tools/"):
           results.append(need)


.. _documents_docs_features:
.. _documents_docs_modules:

Feature, module and component documentation
+++++++++++++++++++++++++++++++++++++++++++

In the following sections the documents of the features, that are planned for release v1.0, are listed.
The features of the platform repository (``docs/features``) are used as structure. For each feature the
documents are listed in the following order:

* Feature documents: the feature documents of the platform repository (see :ref:`platform_folder_structure`)
  and the feature documents of the implementing module(s) (``docs/features``, see :ref:`module_folder_structure`)
* Module documents: the documents on module level of the implementing module(s), e.g. module safety plan,
  safety manual, release note and verification report (``docs/module``, ``docs/verification_report``)
* Component documents: the documents of the components of the implementing module(s), e.g. requirements,
  architecture, detailed design, safety analyses and their inspection checklists (``score/<component_name>/docs``)

The modules implementing a feature are listed with their Bazel module name, which is also used as folder
name for the module documentation in the reference integration. If no module is assigned to a feature
or a table is empty, the corresponding documentation is missing in the build.

.. _documents_docs_features_ai_platform:

AI platform
###########

Modules: none

.. note::

   The incubation repositories ``inc_ai_platform`` and ``inc_gen_ai`` were archived on 2026-03-10.

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/ai_platform/"]
   module_paths = []
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

No module is assigned to this feature yet.

.. rubric:: Component documents

No module is assigned to this feature yet.

.. _documents_docs_features_baselibs:

Baselibs
########

Modules: ``score_baselibs``

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/baselibs/"]
   module_paths = ["modules/score_baselibs/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_baselibs/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_baselibs/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_code_generation:

Code generation
###############

Modules: none

.. note::

   The incubation repository ``inc_score_codegen`` was archived on 2026-03-10.

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/code_generation/"]
   module_paths = []
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

No module is assigned to this feature yet.

.. rubric:: Component documents

No module is assigned to this feature yet.

.. _documents_docs_features_communication:

Communication
#############

Modules: ``score_communication``, ``score_someip_gateway``, ``communication``

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/communication/"]
   module_paths = ["modules/score_communication/", "modules/score_someip_gateway/", "modules/communication/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_communication/", "modules/score_someip_gateway/", "modules/communication/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_communication/", "modules/score_someip_gateway/", "modules/communication/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_configuration:

Configuration
#############

Modules: ``score_config_management``

.. note::

   The incubation repository ``inc_config_management`` was archived on 2026-03-10, the module is continued in the repository ``config_management`` (``score_config_management``).

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/configuration/"]
   module_paths = ["modules/score_config_management/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_config_management/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_config_management/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_diagnostics:

Diagnostics
###########

Modules: ``score_diagnostics``

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/diagnostics/"]
   module_paths = ["modules/score_diagnostics/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_diagnostics/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_diagnostics/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_frameworks:

Frameworks (DAAL, FEO)
######################

Modules: ``score_feo``, ``score_inc_daal``, ``feo``

.. note::

   The incubation repository ``inc_feo`` was archived on 2026-03-10, the module is continued in the repository ``feo`` (``score_feo``).

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/frameworks/"]
   module_paths = ["modules/score_feo/", "modules/score_inc_daal/", "modules/feo/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_feo/", "modules/score_inc_daal/", "modules/feo/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_feo/", "modules/score_inc_daal/", "modules/feo/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_lifecycle:

Lifecycle
#########

Modules: ``score_lifecycle``

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/lifecycle/"]
   module_paths = ["modules/score_lifecycle/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_lifecycle/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_lifecycle/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_logging:

Log and trace
#############

Modules: ``score_logging``

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/log_and_trace/"]
   module_paths = ["modules/score_logging/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_logging/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_logging/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_orchestration:

Orchestration
#############

Modules: ``score_kyron``, ``orchestrator``

.. note::

   The repository ``orchestrator`` was archived on 2026-09-21. The module documentation still available in the platform repository (``docs/modules/orchestrator``) is kept.

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/orchestration/"]
   module_paths = ["modules/score_kyron/", "modules/orchestrator/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_kyron/", "modules/orchestrator/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_kyron/", "modules/orchestrator/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_os:

Operating system
################

Modules: ``os``

.. note::

   The repository ``operating_system`` was archived on 2026-03-10. The module documentation still available in the platform repository (``docs/modules/os``) is kept.

.. rubric:: Feature documents

There is no dedicated feature for the operating system.

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/os/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/os/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_persistency:

Persistency
###########

Modules: ``score_persistency``

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/persistency/"]
   module_paths = ["modules/score_persistency/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_persistency/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_persistency/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_security_crypto:

Security and crypto
###################

Modules: ``score_security_crypto``

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/security_crypto/"]
   module_paths = ["modules/score_security_crypto/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_security_crypto/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_security_crypto/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break

.. _documents_docs_features_time:

Time
####

Modules: ``score_time``

.. rubric:: Feature documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   feature_paths = ["features/time/"]
   module_paths = ["modules/score_time/"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for feature_path in feature_paths:
           if feature_path in docname:
               results.append(need)
               break
       else:
           for module_path in module_paths:
               if module_path in docname:
                   if docname.split(module_path, 1)[1].split("/")[0] == "features":
                       results.append(need)
                   break

.. rubric:: Module documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_time/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder in module_folders:
                   results.append(need)
               break

.. rubric:: Component documents

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   module_paths = ["modules/score_time/"]
   module_folders = ["docs", "index", "manuals", "module", "release", "safety_mgt", "security_mgt", "verification", "verification_report"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       for module_path in module_paths:
           if module_path in docname:
               folder = docname.split(module_path, 1)[1].split("/")[0]
               if folder not in module_folders and folder != "features":
                   results.append(need)
               break


.. _documents_further:

Further documents
+++++++++++++++++

This section lists all documents which are part of the documentation build but are not assigned to one of
the sections above, e.g. documents of included dependencies or of modules which are not yet assigned to a feature.

.. needtable::
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   platform_folders = ["architecture", "contribute", "features", "modules", "platform_management_plan", "quality", "requirements", "safety", "score_tools"]
   assigned_modules = ["score_baselibs", "score_communication", "score_someip_gateway", "communication", "score_config_management", "score_diagnostics", "score_feo", "score_inc_daal", "feo", "score_lifecycle", "score_logging", "score_kyron", "orchestrator", "os", "score_persistency", "score_security_crypto", "score_time"]
   results = []

   for need in needs.filter_types(["document"]):
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       folders = docname.split("/")
       if len(folders) == 1:
           continue
       if folders[0] == "modules":
           if folders[1] in assigned_modules:
               continue
       elif folders[0] in platform_folders:
           continue
       results.append(need)

.. needtable::
   :style: table
   :columns: title;id;safety_affected;security_affected;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   platform_folders = ["architecture", "contribute", "features", "modules", "platform_management_plan", "quality", "requirements", "safety", "score_tools"]
   assigned_modules = ["score_baselibs", "score_communication", "score_someip_gateway", "communication", "score_config_management", "score_diagnostics", "score_feo", "score_inc_daal", "feo", "score_lifecycle", "score_logging", "score_kyron", "orchestrator", "os", "score_persistency", "score_security_crypto", "score_time"]
   results = []

   for need in needs.filter_types(["doc_tool"]):
       docname = need["docname"] or ""
       if "score_platform/" in docname:
           docname = docname.split("score_platform/", 1)[1]
       folders = docname.split("/")
       if len(folders) == 1:
           continue
       if folders[0] == "modules":
           if folders[1] in assigned_modules:
               continue
       elif folders[0] in platform_folders:
           continue
       results.append(need)
