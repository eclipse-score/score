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

Release Management Plan
-----------------------

This document implements parts of the :need:`wp__platform_mgmt`.

Purpose
+++++++

The release management plan describes how releases of the SW platform and modules are performed in the S-CORE project. It
starts with a general description of a release and its scope, then describes the continuous releases in an 8-week cycle.

Objectives and scope
++++++++++++++++++++

Goal of this plan is to describe

* what is the scope of a release
* which types of releases exist
* how these are planned and executed
* how they are identified
* who is integrated and responsible

Approach
++++++++

Release Scope
^^^^^^^^^^^^^

One release contains all the files of one repository. So there is a platform release and separate releases for the modules.
It contains also all the verification reports (including their input e.g. test run logs) and documentation collaterals
(e.g. the html's for the S-CORE homepage) as created during the CI build based on the release tagged repository files.
It does not contain the binary produced in the CI build, as this is not a qualified work product of S-CORE and
the user will need to re-build in the context of their system. Furthermore the binary build with Bazel
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


General Release Planning and Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generally release planning and execution is described in :need:`wf__rel_mod_rel_note` process.
It is part of project planning and therefore also documented with the same means. Generally a release
is planned as an issue linked to a milestone in the `GitHub Milestone Planning <https://github.com/orgs/eclipse-score/projects/13>`_.
And this issue is closed by merging a pull request which creates/updates a release note.

Before every release there will be a phase in which, for the features to be released, no functional
updates will be allowed but only bug fixes, addition of tests and quality improvements.
This period will be planned by the technical leads in the milestone planning. There is no general
time-span defined for this, but for the first releases a period of four weeks is recommended as good practice.
The continuous release for S-CORE will be discussed in the next section. With increasing maturity of the modules
it is expected that this period can be reduced. Also when they are not part of the continuous releases.

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


Continuous Release Planning and Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Release interval (see :ref:`pmp_pm_release`) between S-CORE Product Increments can be divided into two phases:

**Development phase (6 weeks) :**

#. Common release requirements definition
#. Internal communication
#. Features' implementations and improvements
#. Tooling release
#. Code freeze

**Integration phase (2 weeks) :**

#. Release branch creation
#. Integration of the Modules
#. Release notes
#. Release candidate
#. Release creation

Common release requirements definition
--------------------------------------

At the beginning, the overall scope and general requirements for the Modules are discussed during
Release Team Meeting and agreed upon within the S-CORE community, providing clear goals for what must be achieved.
The scope should define minor requirements such as:

* Tooling versions
* Used toolchains
* Supported platforms

rather than specific features' implementation scopes.
Full list of tools can be found in the :need:`doc__tool_evaluation_list`.
The scope will be defined in Github issue with sub-issues for every participating Module to track progress.

Based on the operating system definitions documented in the :ref:`comp_doc_os`
the Reference Integration Team will only maintain functional/certifiable level OSs as part of the release,
while community OSs will be prepared and maintained by the OS module Maintainers. *Code freeze* applies to OSs as well.

.. note::

    Performed by: Project Leads and S-CORE community


Internal Communication
----------------------

Project Leads present scope during Tech Alignment call for final discussion and then send a communication
via mailing list to inform about the scope of upcomming release.

.. note::

    Performed by: Project Leads

Features' implementations and improvements
------------------------------------------

During the development phase, the community works on new features and improvements to the Modules.
Changes are reviewed by Commiters and Module Maintainers.

.. note::

    Performed by: S-CORE community and Module Maintainers

Tooling release
---------------

S-CORE tools, toolchains and other dependencies which are listed in the following Bazel MODULE files
located in reference integration repository:

* ``bazel_common/score_gcc_toolchains.MODULE.bazel``
* ``bazel_common/score_modules_tooling.MODULE.bazel``
* ``bazel_common/score_qnx_toolchains.MODULE.bazel``
* ``bazel_common/score_rust_toolchains.MODULE.bazel``

are released at the end of the development phase the latest.
During the integration phase, no changes other than necessary bug fixes are allowed to give time to the Modules to rebase
their dependencies and prepare their *code freeze*.

.. note::

    Performed by: Module Maintainers

Code freeze
-----------
At the end of development phase, each Module must provide a hash of the commit that represents a *code freeze*
and serves as a candidate for integration. The hash can be from the **main** or **dedicated release** branch.

.. note::

    Performed by: Module Maintainers

Release branch creation
-----------------------

The integration phase begins with the creation of a **release branch** in the ``reference_integration`` repository
originating from current **main**.

.. note::

    Performed by: Reference Integration Team

Integration of the Modules
--------------------------

Module Maintainers prepare a Pull Request to that branch with updates to the ``known_good.json`` file,
pointing to the hash of their *code freeze*. They may update other JSON fields for their Module as needed.
Automated workflows will build and test to provide clear feedback directly in the PR.
If there are any issues, Module Maintainers can either push fixes to their **dedicated release** branch
and update the hash in the PR accordingly, or provide patches (see :ref:`ref_int_patching-label`).

.. note::

    Performed by: Module Maintainers

Release notes
-------------

Project Leads create a branch ``release/version`` with new release notes in ``score_platform`` repository following template: :need:`doc__platform_release_note`.
Module Maintainers create a Pull Request to that branch with updates to the release notes,
describing the changes in their Module for the release.
Once all Modules are updated Project Leads approve the release notes and create ``score_platform`` release.

.. note::

    Performed by: Module Maintainers and Project Leads

Release candidate
-----------------

Once all Modules are merged with their *code freeze*, Module Maintainers create a tag on that exact hash following the S-CORE release process,
and ensure that the new release is present in S-CORE's ``bazel_registry``.
The Reference Integration Team prepares a final Pull Request and replaces all hashes with the dedicated release versions.

This pull request has additional workflow checking that every Maintainer has approved the PR signing off their Module's release candidate.
The approval of the Project Lead is required and from the Quality Manager for the formal aspects as well.
There is an additional ``.rst`` file listing every Module and GitHub ID of the Maintainer responsible.

.. note::

    Performed by: Reference Integration Team and Module Maintainers

Release creation
----------------

Once all previous steps are completed Reference Integration Team triggers the release creation workflow in ``release_integration``.
An automated verification process of the release begins which includes building, testing, deploying documentation and checking that
every Module has been correctly signed-off by its Maintainer. If any issue is found, the release creation process is stopped.
Once the process is aborted, the Reference Integration Team investigates the issue and works with the relevant Module Maintainer to fix it
or if the issue is severe decides, together with the Project Leads, to postpone the release. If the issue is fixed, the release creation process can be triggered again.
When successfully completed the release and its downloadable assets are ready for distribution.

.. note::

    Performed by: Reference Integration Team


Opting out of a release
-----------------------

Module Maintainers may decide that their Module will not be released with a new version for the S-CORE Product Increment.
In that case currently integrated version can be used. However, they must still ensure that the Module remains compatible with
the S-CORE release and does not fail any workflows.

If Module Maintainers cannot adapt to the newest release requirements or any S-CORE community member discovers a showstopper
for the upcoming release, they must communicate it promptly to the Project Leads and other community members.
Following discussion and impact analysis, a decision is made regarding whether to postpone or skip the S-CORE release,
and the planning is updated accordingly.

.. _ref_int_patching-label:

Patching Module
---------------

Module Maintainers prepare ``.patch`` file(s) and place them in the ``/patches/MODULE_NAME`` directory.
The patch filename must clearly indicate what it addresses.
For multiple issues, it is preferred to create multiple patches rather than a single patch addressing all issues.

A patch might be need to fix issues after the release of the module is allready in bazel registry and there is
no time for another release. Or if its only minor and it's decided to avoid therefore another release.

Target releases definition
--------------------------

Based on the operating system definitions documented in the `OS module <https://eclipse-score.github.io/score/main/modules/os/operating_systems/docs/index.html>`_,
the Reference Integration Team defines which OSs will be maintained as part of the release:

* **Functional/Certifiable level OSs** - maintained by the Reference Integration Team and included in the release
* **Community OSs** - prepared and maintained by the OS module Maintainers during the integration phase

Only changes to functional/certifiable level OSs are considered until the *code freeze*.
Community OS updates can be prepared by the OS Maintainer during the release phase if needed.

.. note::

    Performed by: Reference Integration Team and OS module Maintainers
