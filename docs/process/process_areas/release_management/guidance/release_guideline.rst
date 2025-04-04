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

Guideline
#########

.. gd_guidl:: Release Management Guideline
   :id: gd_guidl__rel_management
   :status: draft

.. _workflow_release:

Software Module Release
-----------------------

1. **Repository Management**:

   * Each software module is contained in its own GitHub repository.
   * Ensure that the repository follows the standard naming conventions and structure.

2. **Release Planning**:

   * Create a release plan for each software module.
   * The release plan should include timelines, milestones, and deliverables.
   * Coordinate with other module owners to align release schedules.

3. **Development and Testing**:

   * Follow the development guidelines and coding standards.
   * Conduct thorough testing, including unit tests, integration tests, and system tests.
   * Ensure that all tests pass before proceeding to the release.
   * In case of failed test, evaluate and possibly justify their continued existence.

4. **Release Preparation**:

   * Update the version number according to the versioning policy.
   * Prepare release notes documenting the changes, improvements, and bug fixes.
   * Ensure the relevant safety cases are available.
   * Tag the release in the GitHub repository.

5. **Release Execution**:

   * Push the release to the main branch.
   * Create a release in the GitHub repository and attach the release notes.
   * Notify the tech lead circle about the release.


Platform Release
----------------

1. **Integration of Software Modules**:

   * The platform release integrates various software modules.
   * Ensure that all software modules are released and tagged before the platform release.

2. **Platform Release Planning**:

   * Create a platform release plan that consumes the timelines from the software module release plans.
   * Define the overall release schedule, including major and minor releases.

3. **Development and Testing**:

   * Integrate the released software modules into the platform.
   * Conduct comprehensive testing to ensure compatibility and stability.
   * Address any integration issues promptly.

4. **Release Preparation**:

   * Update the platform version number according to the versioning policy.
   * Prepare platform release notes summarizing the updates from all integrated software modules.
   * Ensure the relevant safety cases are available.
   * Tag the platform release in the GitHub repository.

5. **Release Execution**:

   * Push the platform release to the main branch.
   * Create a release in the GitHub repository and attach the platform release notes.
   * Publish within Eclipse SDV

Release Versioning Rules
------------------------

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

Tracking and Communication
---------------------------

1. **Tracking**:

   * Use the github project management tools to track the progress of software module releases and the platform release.
   * Maintain a release calendar to visualize the timelines and milestones.

2. **Communication**:

   * Regularly update all stakeholders on the release status.
   * Hold periodic meetings to discuss progress, issues, and dependencies within the tech lead circle.


Templates
=========

For the release note a template has been created for module level and for platform level

.. list-table:: Overview
   :header-rows: 1
   :widths: 37, 37

   * - Project scope
     - Template
   * - Module Release Notes
     - :need:`[[title]] <gd_temp__rel__mod_rel_note>`
   * - Platform Release Notes
     - :need:`[[title]] <gd_temp__rel__plat_rel_note>`

The above templates shall be used
