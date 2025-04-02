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

Config management
-----------------

Purpose
+++++++

The Configuration Management Plan defines how the integrity of all work products can be reached and maintained.

Objectives and scope
++++++++++++++++++++

Goal of this plan is to describe

* how all work products in the project are identified
* the infrastructure to store the work products
* how to make all work products available to all concerned parties
* where to find which work product
* how to retrieve specific versions of a work product
* how to modify a work product
* how to create and store versions of work products
* how to manage baselines

Approach
++++++++

.. gd_guidl:: Configuration
   :id: gd_guidl__configuration
   :status: valid
   :complies: std_req__iso26262__support_741, std_req__iso26262__support_742, std_req__iso26262__support_743, std_req__iso26262__support_744, std_req__iso26262__support_745

Identification
^^^^^^^^^^^^^^

Each work product is identified by its sphinx-needs Id. Spinx-needs checks for Id duplicates.
The work products are stored in text or code files (these are identified by their filenames) within GitHub repositories.
There is one `platform repository <https://GitHub.com/eclipse-score/score/>`_ and one repository for each module.

Retrieval
^^^^^^^^^

Work products can be retrieved from GitHub repositories by everybody according to the Eclipse Foundation guidelines.
Their content is defined in the process/workproducts and process_area/<area_name>/workproducts files.
To find the location of the work products, the :ref:`platform_folder_structure` can be used.
To show the content of a certain version of a file the GitHub "History" function can be used which shows all committs
into this file and these committs show the change history (which is also available via "Blame" function for every line of the files).
Also baselines (which are sets of files) can be shown via GitHub by switching to a "tag" created to mark the baseline versons.
These baselines are used to build the release, i.e. the documentation, code and verification reports for this tag.
For release versioning rules check the respective section of release guideline.

Modification
^^^^^^^^^^^^

Files or new work products contained in them are created in local branches by the :need:`Contributor <rl__contributor>`
and shared for review and incorporation into the main branch via GitHub pull-requests,
which are after their acceptance merged by the :need:`Committer <rl__committer>`.
See also :need:`doc__platform_change_management_plan`.

Branches and Baselines
^^^^^^^^^^^^^^^^^^^^^^

Git defines branches as a means of parallel development. In the S-CORE project the following types of branches will be used:

* local branches - created from "remote" branches, in these the development of the contributors takes place, no restriction on naming.
* main branch - a "remote" branch which contains all the latest file versions checked by CI, reviewed, accepted and merged.
* release branch - a "remote" branch derived from main branch which is used to prepare a release,
  no functional code changes are allowed, only bug fixes and verification based improvements.
  Only the technical lead is allowed to approve a merge into a release branch. The branch name is "release-<MAJOR_version>.<MINOR_version>

"remote" branch: is not "local" to the developer but resides on the "remote" GitHub server.

Baselines are created by using the GitHub "tag" function. The tag name shall correspond to
the release branch name the tag is created, adding patch version and pre-release tag.
See also release management (Todo: add link when https://github.com/eclipse-score/score/pull/578 is merged).

Every change in the release repository is also taken over into the main branch. The module development team
can decide how to ensure this (e.g. by development in main and cherrypick to release branch).
