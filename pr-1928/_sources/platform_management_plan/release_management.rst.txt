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

.. document:: Release Management Plan
   :id: doc__platform_release_management_plan
   :status: draft
   :safety: ASIL_B
   :security: NO
   :tags: platform_management
   :realizes: wp__platform_sw_release_plan

Release management Plan
-----------------------

This document implements parts of the :need:`wp__platform_mgmt`.

Purpose
+++++++

The release management plan describes how releases of the SW platform and modules are performed in the S-CORE project.

Objectives and scope
++++++++++++++++++++

Goal of this plan is to describe

* what is the scope of a release
* which types of releases exist
* how these are planned and executed
* how they are identified

Approach
++++++++

Release Scope
^^^^^^^^^^^^^

One release contains all the files of one repository. So there is a platform release and separate releases for the modules.
It contains also all the verification reports (including their input e.g. test run logs) and documentation collaterals
(e.g. the html's for the S-CORE homepage) as created during the CI build based on the release tagged repository files.
It does not contain the binary produced in the CI build, as this is not a qualified work product of S-CORE and
the user will need to re-build in the context of his system. Furthermore the binary build with Bazel
is reproducible, so this can be re-created from source any time.

Release Types
^^^^^^^^^^^^^

Release types are strongly associated with the release version numbering, which is explained in
"Identification" section below.

S-CORE has two major kinds of releases: experimental and official. These correspond with the "feature flags"
defined in :need:`doc__project_mgt_plan`.

* **Experimental** means that the development artifacts needed for the safety package work products may be incomplete.
  These releases are done during development phase to be able to sync between the module repositories.
* **Official** means that the processes are fully executed to produce all work products and are documented
  with a release note as in :need:`gd_temp__rel_plat_rel_note` or :need:`gd_temp__rel_mod_rel_note`.
  For an official release also consider `Eclipse Project Handbook - Releases <https://www.eclipse.org/projects/handbook/#release-releases>`_.


Release Planning and Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generally release planning and execution is described in :need:`wf__rel_mod_rel_note` process.
It is part of project planning and therefore also documented with the same means. Generally a Release
is planned as an issue linked to a milestone in the `GitHub Milestone Planning <https://github.com/orgs/eclipse-score/projects/13>`_.
And this issue is closed by merging a pull request which creates/updates a release note.

Before every release there will be a phase in which, for the features to be released, no functional
updates will be allowed but only bug fixes, addition of tests and quality improvements.
This period will be planned by the technical leads in the milestone planning. There is no general
time-span defined for this, but for the first releases a period of four weeks is recommended as good practice.
With increasing maturity of the modules it is expected that this period can be reduced.

As defined in the process, the releases on module and platform level need to be coordinated.
Major version updates denote API incompatibility, so the modules in a platform release are expected to have the same
major version.

For the release execution follow the steps described in :ref:`module_release_manual`.

Identification
^^^^^^^^^^^^^^

1. Semantic Versioning Format

   Use the format MAJOR.MINOR.PATCH for version numbers.


2. Version Components

   * MAJOR: Incremented for incompatible API changes.
   * MINOR: Incremented for backward-compatible functionality additions.
   * PATCH: Incremented for backward-compatible bug fixes.

3. Rules for Incrementing Versions

   * Major Version (MAJOR)

      Increment the MAJOR version when making changes that break backward compatibility.

      Examples:

      * Removing or renaming public APIs.
      * Significant changes to the architecture that require modifications from dependent modules.

   * Minor Version (MINOR)

      Increment the MINOR version when adding new features or functionality in a backward-compatible manner.

      Examples:

      * Adding new APIs or modules.
      * Enhancements to existing features that do not affect existing functionality.

   * Patch Version (PATCH)

      Increment the PATCH version when making backward-compatible bug fixes.

      Examples:

      * Fixing bugs or issues in the existing code.
      * Minor improvements that do not add new features or change existing ones.

4. Pre-Release Versions

   * Use pre-release versions for features or fixes that are not yet ready for production.
   * Format: MAJOR.MINOR.PATCH-<pre-release-tag>, e.g., 1.0.0-alpha, 1.0.0-beta.

5. Tagging Releases

   * Tag each release in the repository with the version number.
   * Format: vMAJOR.MINOR.PATCH, e.g., v1.3.0.
