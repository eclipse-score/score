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

.. doc_tool:: github
   :id: doc_tool__github
   :status: draft
   :version: cloud
   :tcl: LOW
   :safety_affected: YES
   :security_affected: YES
   :realizes: wp__tool_verification_report
   :tags: tool_management

GitHub Verification Report
==========================

Introduction
------------
Scope and purpose
~~~~~~~~~~~~~~~~~
GitHub.com is a cloud-based platform for source code management, project management, and automation. It is used for hosting git repositories, managing issues and projects, code review, release planning, and running CI/CD workflows via GitHub Actions.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
Inputs:
 | - Source code (git repositories)
 | - Issues, project boards, milestones
 | - Workflow definitions (YAML)
 | - Pull requests, reviews

Outputs:
 | - Repository state (commits, branches, tags)
 | - Issue/project status
 | - CI/CD run results
 | - Release artifacts

.. figure:: _assets/github.drawio.svg
  :width: 100%
  :align: center
  :alt: GitHub overview

  GitHub overview

Available information
~~~~~~~~~~~~~~~~~~~~~
- Platform: GitHub.com (cloud)
- Official documentation: https://docs.github.com/
- API reference: https://docs.github.com/en/rest
- Example S-CORE integration: Bazel rules for CI/CD and code hosting

Usage constraints:
- Requires internet access and GitHub account
- API rate limits and permission model apply
- Actions runners may have resource/time limits

Installation and integration
----------------------------
Installation
~~~~~~~~~~~~
No installation required for cloud use. Access via web, git client, or API. For CI/CD, configure workflows in `.github/workflows/` and connect via Bazel rules.

Integration
~~~~~~~~~~~
- Source code hosted on GitHub.com
- Issues, projects, and milestones managed via web or API
- CI/CD workflows triggered by git events, managed via GitHub Actions
- Bazel rules used to interact with GitHub for automation

Environment
~~~~~~~~~~~
- Web browser
- Git client
- Bazel build environment

Safety evaluation
-----------------
This section outlines the safety evaluation of GitHub for its use within the S-CORE project.

.. list-table:: Safety evaluation
   :header-rows: 1
   :widths: 1 2 8 2 6 4 2 2

   * - Malfunction identification
     - Use case description
     - Malfunctions
     - Impact on safety?
     - Impact safety measures available?
     - Impact safety detection sufficient?
     - Further additional safety measure required?
     - Confidence (automatic calculation)
   * - 1
     - Repository access
     - | GitHub is unavailable (outage)
       |
       | Source code, issues, or workflows cannot be accessed or updated.
     - yes
     - (implicit) Build/test fails due to missing code
     - yes
     - no
     - high
   * - 2
     - Repository access
     - | Data corruption or loss
       |
       | Commits, issues, or workflow data is lost or corrupted.
     - yes
     - Backups, code review, branch protection
     - yes
     - no
     - high
   * - 3
     - Repository access
     - | Wrong repository/branch/tag checked out
       |
       | Build/test runs on incorrect code version due to misconfiguration or user error.
     - yes
     - Manual review, branch protection, CI checks
     - yes
     - no
     - high
   * - 4
     - Dependency management
     - | Submodules or dependencies not fetched
       |
       | Build/test fails due to missing submodules or external dependencies.
     - yes
     - (implicit) Build/test fails
     - yes
     - no
     - high
   * - 5
     - Dependency management
     - | Wrong dependency version fetched
       |
       | Build/test runs with incorrect dependency version, causing incompatibility or test failures.
     - yes
     - Pin versions, lock files, CI checks
     - yes
     - no
     - high
   * - 6
     - Workflow execution (CI/CD)
     - | Actions workflow fails to run (misconfiguration, runner unavailable)
       |
       | CI/CD jobs do not execute as expected, blocking releases or tests.
     - yes
     - (implicit) Build/test fails, manual rerun
     - yes
     - no
     - high
   * - 7
     - Workflow execution (CI/CD)
     - | Wrong workflow triggered (wrong event, branch, or path)
       |
       | CI/CD jobs run on unintended code or skip required checks.
     - yes
     - Manual review, branch protection, required checks
     - yes
     - no
     - high
   * - 8
     - Workflow execution (CI/CD)
     - | Workflow passes with undetected errors (false positive)
       |
       | CI/CD reports success but actual build/test failed or was skipped.
     - yes
     - Test coverage, manual review, required status checks
     - no
     - yes (qualification)
     - low
   * - 9
     - Workflow execution (CI/CD)
     - | Workflow fails due to external service outage (e.g., Actions runner, artifact storage)
       |
       | Build/test is blocked or incomplete due to third-party service unavailability.
     - yes
     - (implicit) Build/test fails, retry
     - yes
     - no
     - high
   * - 10
     - Artifact storage
     - | Release artifacts not published or corrupted
       |
       | Release process is blocked or produces incomplete/corrupted results.
     - yes
     - Manual verification, checksums
     - yes
     - no
     - high
   * - 11
     - Artifact storage
     - | Artifacts published to wrong location or with wrong version/tag
       |
       | Downstream consumers use incorrect or outdated artifacts.
     - yes
     - Manual review, release automation, version checks
     - yes
     - no
     - high
   * - 12
     - Issue/project management
     - | Issues, projects, or milestones are not updated or synced
       |
       | Project status is out of date, leading to miscommunication.
     - no
     - Manual review
     - yes
     - no
     - high
   * - 13
     - Issue/project management
     - | Issue or project data is lost or corrupted
       |
       | Loss of planning or tracking data, may impact traceability.
     - yes
     - Backups, audit logs
     - yes
     - no
     - high

Security evaluation
-------------------
This section outlines the security evaluation of GitHub for its use within the S-CORE project.

.. list-table:: Security evaluation
   :header-rows: 1

   * - Threat identification
     - Use case description
     - Threats
     - Impact on security?
     - Impact security measures available?
     - Impact security detection sufficient?
   * - 1
     - TBD
     - TBD
     - TBD
     - TBD
     - TBD

Result
------
GitHub requires qualification for use in safety-related software development according to ISO 26262.

**Tool Qualification**
----------------------
Based on method: validation of the software tool.

Requirements and testing aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tool requirements are derived from official documentation: https://docs.github.com/

GitHub is a cloud service and does not provide formal, vendor-defined requirements. The project team is responsible for identifying the specific GitHub features used. Based on this, requirements for the utilized features must be derived from the available documentation and GitHub validated against defined requirements.

.. [1] The tool version mentioned in this document is preliminary.
       It is subject to change and will be updated in future.
