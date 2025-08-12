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
   :tags: platform_management

Config management / Configuration Management Plan
-------------------------------------------------

Purpose
+++++++

The Configuration Management Plan defines how the integrity of all work products
and other project relevant artefacts can be reached and maintained.


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

note: for definition of "configuration items" check :need:`PROCESS_doc_concept__configuration__process`


Approach
++++++++

.. gd_guidl:: Configuration
   :id: gd_guidl__configuration
   :status: valid
   :complies: PROCESS_std_req__iso26262__support_741, PROCESS_std_req__iso26262__support_742, PROCESS_std_req__iso26262__support_743, PROCESS_std_req__iso26262__support_744, PROCESS_std_req__iso26262__support_745, PROCESS_std_req__aspice_40__SUP-8-BP1, PROCESS_std_req__aspice_40__SUP-8-BP3, PROCESS_std_req__aspice_40__SUP-8-BP4, PROCESS_std_req__aspice_40__SUP-8-BP5, PROCESS_std_req__aspice_40__SUP-8-BP8


Identification
^^^^^^^^^^^^^^

Each work product is identified by its sphinx-needs Id, this includes documents identified as such (see project documents list in :need:`doc__documentation_mgt_plan`).
Spinx-needs checks for Id duplicates.
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

For other artefacts: these are pulled into S-CORE integration repository by forking to be handled as above.


Modification
^^^^^^^^^^^^

Files or new work products contained in them are created in local branches by the :need:`Contributor <PROCESS_rl__contributor>`
and shared for review and incorporation into the main branch via GitHub pull-requests,
which are after their acceptance merged by the :need:`Committer <PROCESS_rl__committer>`. The same applies for changes in existing configuration items.
See also :need:`doc__platform_change_management_plan`.

For other artefacts modifications are controlled by the bazel build files which are also under configuration control.


Branches and Baselines
^^^^^^^^^^^^^^^^^^^^^^

Git defines branches as a means of parallel development. In the S-CORE project the following types of branches will be used:

* local branches - created from "remote" branches, in these the development of the contributors takes place, no restriction on naming.
* main branch - a "remote" branch (named "main") which contains all the latest file versions checked by CI, reviewed, accepted and merged.
* release branch - a "remote" branch derived from main branch which is used to prepare a release,
  no functional code changes are allowed, only bug fixes and verification based improvements.
  Only the technical lead is allowed to approve a merge into a release branch. The branch name is "release-<MAJOR_version>.<MINOR_version>

The "remote" branch is not "local" to the developer but resides on the "remote" GitHub server.

Baselines are created by using the GitHub "tag" function. The tag name shall correspond to
the release branch name the tag is created, adding patch version and pre-release tag.
See also :need:`doc__platform_release_management_plan`.

Every change in the release repository is also taken over into the main branch. The module development team
can decide how to ensure this (e.g. by development in main and cherrypick to release branch).


Backup and Recovery
^^^^^^^^^^^^^^^^^^^

Backup and recovery are covered by the Eclipse Foundation hosting the GitHub service for S-CORE.
For the long term storage, additional measures are taken, see :need:`PROCESS_gd_req__workproducts_storage`
