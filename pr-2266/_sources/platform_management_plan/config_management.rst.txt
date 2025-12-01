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

.. document:: Configuration Management Plan
   :id: doc__config_mgt_plan
   :status: draft
   :safety: ASIL_B
   :security: YES
   :tags: platform_management
   :realizes: wp__config_mgt_plan

Config management / Configuration Management Plan
-------------------------------------------------

Purpose
+++++++

The Configuration Management Plan defines how the integrity of all work products
and other project relevant artifacts can be reached and maintained.


Objectives and scope
++++++++++++++++++++

Goal of this plan is to describe

* how all configuration items in the project are identified
* the infrastructure to store the configuration items
* how to make all configuration items available to all concerned parties
* where to find which configuration item
* how to retrieve specific versions of a configuration item
* how to modify a configuration item and how to control this
* how to create and store versions of configuration items
* how to manage baselines
* how to backup and recover (including long term storage)
* how to report the configuration status

note: for definition of "configuration items" check :need:`doc_concept__configuration_process`


Approach
++++++++

The steps below describe how configuration identification, retrieval, modification, branches and baselines, backup and recovery are organized.


Lifecycle
^^^^^^^^^

The configuration management of the S-CORE project is in place during the complete development lifecycle.
I.e. in Concept Phase, Development Phase and Maintenance.


Identification and Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each work product is identified by its sphinx-needs Id, this includes documents identified as such (by the document header as defined in :need:`gd_temp__documentation`).
The complete list of project documents is defined in the :need:`doc__documentation_mgt_plan`.
Ids are checked for uniqueness, see :need:`gd_req__configuration_uid`.
sphinx-needs is also used to document the work products properties/attributes defined in the process area descriptions.
The work products are stored in text or code files (these are identified by their filenames) within GitHub repositories.
There is one `platform repository <https://GitHub.com/eclipse-score/score/>`_ and one repository for each module.

For other artefacts these are either

- files - are identified by their path/filename (and configured also in GitHub)
- precompiled tools/binaries - bazel build configuration identifies those by their hash (see MODULE.bazel).
- (external) tools/binaries to be built in S-CORE CI - bazel build configuration identifies those by their version.


Retrieval
^^^^^^^^^

Work products and files can be retrieved from GitHub repositories by everybody according to the Eclipse Foundation guidelines.
Their content is defined in the process/workproducts and process_area/<area_name>/workproducts files.
To find the location of the work products, the :ref:`platform_folder_structure` can be used.
To show the content of a certain version of a file the GitHub "History" function can be used which shows all commits
into this file and these commits show the change history (which is also available via "Blame" function for every line of the files).
Also baselines (which are sets of files) can be shown via GitHub by switching to a "tag" created to mark the baseline versions.
These baselines are used to build the release, i.e. the documentation, code and verification reports for this tag.
For release versioning rules check the respective section of release guideline.

For other artifacts: these are pulled into S-CORE integration repository by forking to be handled as above.


Control and Modification
^^^^^^^^^^^^^^^^^^^^^^^^

Files or new work products contained in them are created in local branches by the :need:`Contributor <rl__contributor>`
and shared for review and incorporation into the main branch via GitHub pull-requests,
which are after their acceptance merged by the :need:`Committer <rl__committer>`. The same applies for changes in existing configuration items.
All modifications (differences between before and after) are documented in the pull-requests and are the main input to the pull-request reviews.
See also :need:`doc__platform_change_management_plan`.

For tool/binaries modifications (version changes) are controlled by the bazel build files. These build files, like other files, are also maintained in GitHub.


Branches and Baselines
^^^^^^^^^^^^^^^^^^^^^^

Branches are used as a means of parallel development. In the S-CORE project the following types of branches will be used:

* local branches - created from "remote" branches, in these the development of the contributors takes place, no restriction on naming.
* main branch - a "remote" branch (named "main") which contains all the latest file versions checked by CI, reviewed, accepted and merged.
* release branch - a "remote" branch derived from main branch which is used to prepare a release,
  no functional code changes are allowed, only bug fixes and verification based improvements.
  Only the technical lead is allowed to approve a merge into a release branch. The branch name is given as defined in :need:`doc_concept__rel_process`.

The "remote" branch is not "local" to the developer but resides on the "remote" GitHub server.

In S-CORE all configuration items are kept in GitHub, this means that there only needs to be one baseline (per repository) for these
(and not multiple ones for each of the work products types which are maintained in separate tools).
Baselines are created by using the GitHub "tag" function. The tag name shall correspond to
the release branch name the tag is created, adding patch version and pre-release tag.
See also :need:`doc__platform_release_management_plan`.

As described in "Identification and Properties" above, there are several repositories for the modules and the platform integration.
Baselines are created individually in these repositories, even a different version schema could be adopted.
In case of dependent repositories, the repository dependent upon on has to be base-lined first, to be available
to refer to this baseline when integrating it. That means that for example a platform baseline also
documents the versions (baselines) of the modules the platform consists of. This can then also be seen in the platform release note.

Every change in the release repository is also taken over into the main branch. The module development team
can decide how to ensure this (e.g. by development in main and cherry-pick to release branch).


Backup and Recovery
^^^^^^^^^^^^^^^^^^^

Backup and recovery are covered by the Eclipse Foundation hosting the GitHub service for S-CORE.
For the long term storage, additional measures are taken, see :need:`gd_req__config_workproducts_storage`


Status and Reporting
^^^^^^^^^^^^^^^^^^^^

Work products defined in our processes have "status" attributes. These are used to communicate to all the stakeholders.
The main communication means is a document list containing all documents including their status.
This list is part of the Documentation Management Plan :need:`doc__documentation_mgt_plan` as part of the Platform Management Plan,
as defined in :need:`gd_guidl__documentation`.
Completeness of the configuration items (within a baseline) is checked at least for every release
against the list of planned documents, which is also part of the Documentation Management Plan.

Note that work products consisting of several elements (documented as needs) will be collected in one file
which will form a document (e.g. there will be a document (doc__*) "feature xy requirements" and in it all the feature's requirements(feat_req__*)).
This applies to requirements, architecture, detailed design and safety analysis.
The files containing the source code and test code are not part of documents as above,
their status is implicitly "valid", as these are subject to code and test review before every merge.

Also the used tools status and version is reported within a "tool list" which may be part of
the Documentation Management Plan or referenced from it (and also need to be checked for completeness).


Configuration Management Tooling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Almost all requirements of the standards towards configuration management can be covered by
standard versioning tooling of the Eclipse Foundation and of the S-CORE project
("Docs-as-Code" identification of work products).
The respective tools used in the project are:

* versioning tool: GitHub
* "Docs-as-Code" tool: sphinx-needs
* CI build tool: Bazel

Note 1: A versioning tool covers part of configuration management but not all (namely: storage, retrieval, control and modification, branching and base-lining).

Note 2: A "Docs-as-Code" tool is used to identify, attribute and link parts of text files and generate human and machine readable documentation.
