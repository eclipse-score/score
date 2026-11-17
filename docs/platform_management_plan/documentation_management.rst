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

.. document:: PF Documentation Management Plan
   :id: doc__platform_documentation_mgt_plan
   :status: valid
   :version: 5
   :safety: ASIL_B
   :security: YES
   :tags: platform_management
   :realizes: wp__document_mgt_plan[version==1]

PF Documentation Management Plan
================================

Purpose
-------

The S-CORE Documentation Management Plan defines how documents are managed
throughout the project lifecycle. It establishes a consistent approach to
identifying, maintaining, reviewing, approving, and versioning project
documentation.


Objectives and Scope
--------------------

This plan defines:

* the documents managed by the S-CORE project;
* the attributes used to identify and classify these documents;
* the document lifecycle;
* the rules for reviewing and approving documents; and
* the mechanisms for maintaining the document inventory.

This plan applies to work products managed as general documents. Work products
with dedicated information models, such as requirements or architecture
elements, are managed according to their applicable definitions and processes.

Documentation Approach
----------------------

S-CORE work products are represented in different ways depending on their
purpose, content, and required structure.

Some work products have dedicated information models. For example, requirements
and architecture elements have specific attributes and relationships defined
for their respective work-product types.

Other work products are managed as general documents. These include, for
example, plans that form part of the Platform Management Plan and verification
reports.

This Documentation Management Plan primarily defines the management of these
general documents. It also provides the document inventory for all documents
included in the platform documentation build, including documents that contain
work products with dedicated information models.

Document Attributes
-------------------

Each document is described by a defined set of attributes.

The following attributes are maintained as part of the document definition:

* **Title:** identifies the document by name. Mandatory.
* **Unique ID:** uniquely identifies the document according to the applicable
  naming convention. Mandatory.
* **Version:** identifies the version of the document definition. Mandatory.
* **Safety:** indicates the safety classification applicable to the document.
  Mandatory.
* **Security:** indicates whether the document is security-relevant. Mandatory.
* **Status:** indicates the current lifecycle state of the document. Mandatory.
* **Tags:** provide additional classification for grouping and filtering
  documents. Optional.

The Documentation Management Plan is itself managed as a document. The document
definition in the header of this file therefore provides an example. See
:need:`doc__platform_documentation_mgt_plan`.


Automatically Derived Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Additional information is recorded through Git and GitHub:

* **Author:** the contributor who created or modified the document content.
* **Approver:** the CODEOWNER who performed the applicable GitHub review and
  approved the change.
* **Reviewer:** any additional reviewer who participated in the GitHub review
  without acting as the approving CODEOWNER.

This information is derived from the Git history and Pull Request review records
and does not need to be maintained manually in the document definition.

Document Lifecycle
------------------

S-CORE documents have two lifecycle states:

* **Draft:** the document is under development and is not yet considered
  complete. Existing content may already have been reviewed and may be
  applicable within its documented scope.
* **Valid:** the document is complete, reviewed, and approved for its intended
  use.

A document may transition from **Valid** back to **Draft** when changes requiring
further development or review are introduced.

For example, a verification report may have status **Valid** for a completed
release. When the report is updated for a subsequent release, its status may
return to **Draft** until the updated content has been completed, reviewed, and
approved.

Documents that are no longer applicable are removed from the active project
documentation rather than being assigned a separate lifecycle state.

Removed documents and their previous versions remain available through the Git
history and, where applicable, through release baselines. This preserves
traceability and allows historical document versions to be inspected or
recovered when required, for example to understand previous decisions or to
provide audit evidence.


Document Review and Approval
----------------------------

Each document shall be reviewed according to the review requirements defined
for the corresponding work-product type in the applicable process description.

Where defined for the work-product type, the applicable review checklist shall
be used.

The review and approval are performed through a GitHub Pull Request. At least
one CODEOWNER who is not an author of the reviewed changes shall review and
approve the document.

The GitHub Pull Request review record provides the approval evidence for the
document. Where an applicable review checklist requires additional evidence,
that evidence shall be recorded or referenced by the Pull Request.


Documentation Build
-------------------

All documentation work products, including both work products with dedicated
information models and general documents, are included in the documentation
build.

For each Pull Request, the documentation build represents the version of the
work products resulting from the proposed changes. This allows documentation
changes to be reviewed together with the corresponding project changes.

Document versioning and change history are managed using Git and GitHub in the
same manner as for other project work products. The applicable versioning,
baselining, and configuration-management rules are defined in
:need:`doc__platform_config_mgt_plan`.


Planning and Tracking
---------------------

The schedule for creating or updating documents is outside the scope of this
Documentation Management Plan.

The corresponding activities are planned and tracked through GitHub ISSUEs as
defined in the applicable Project Management Plan.


Document Inventory
------------------

The following tables provide the inventory of documents included in the
documentation build.

The S-CORE documentation is organized into folders as defined in
:ref:`platform_folder_structure`. Each folder represents a specific aspect of
the project or a defined documentation scope.

The inventory is generated automatically from the document definitions included
in the documentation build. Consequently, only documents available to the
corresponding build configuration are included.


.. _project_documents_list:

Platform Documents List
~~~~~~~~~~~~~~~~~~~~~~~

The following table lists all documents included in the documentation build.

.. needtable::
   :style: table
   :types: document
   :columns: title;id;version;status;safety;security
   :sort: title

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"]:
           results.append(need)


.. note::

   The following folder-based tables are retained temporarily for compatibility
   with the current Platform Management Plan structure. They will be removed after the Platform Management Plan has been fully updated.


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
