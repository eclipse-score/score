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
   :tcl: HIGH
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
GitHub.com is a cloud-based platform for source code management, project management, and automation.
It is used for hosting git repositories, managing issues and projects, code review,
release planning, and running CI/CD workflows via GitHub Actions.

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


Available information
~~~~~~~~~~~~~~~~~~~~~
- Platform: GitHub.com (cloud)
- Official documentation: https://docs.github.com/
- API reference: https://docs.github.com/en/rest
- S-CORE GitHub organization: https://github.com/eclipse-score


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
     - Issue/Project management
     - | Issues, projects, or milestones are not updated or synced.
       | Project status is out of date, leading to miscommunication.
     - no
     - | Manual status checks during regular meetings.
       | All teams have regular sync points to verify project status. Sync happens on ticket basis.
       | So when ticket is lost, it will be detected during these regular meetings.
     - yes
     - no
     - high
   * - 2
     - Issue/Project management
     - | Issue or project data is lost or corrupted.
       | Loss of planning or tracking data, may impact traceability.
     - yes
     - | Manual status checks during regular meetings.
       | All teams have regular sync points to verify project status. Sync happens on ticket basis.
       | So when ticket is lost, it will be detected during these regular meetings.
     - yes
     - no
     - high
   * - 3
     - Repository access
     - | GitHub is unavailable.
       | Source code, issues, or workflows cannot be accessed or updated.
     - no
     - no
     - yes
     - no
     - high
   * - 4
     - Repository access
     - | Data corruption or loss.
       | Commits, issues, or workflow data is lost or corrupted.
     - yes
     - | PR reviews.
       | Code reviews and approvals help catch data issues before merging.
     - yes
     - no
     - high
   * - 5
     - Repository access
     - | Wrong repository/branch/tag checked out.
       | Build/test runs on incorrect code version due to misconfiguration or user error.
     - yes
     - | PR reviews.
       | Code reviews and approvals help catch data issues before merging.
     - yes
     - no
     - high
   * - 6
     - Workflows (CI/CD)
     - | Actions workflow fails to run (misconfiguration, runner unavailable).
       | CI/CD jobs do not execute as expected, blocking releases or tests.
     - no
     - no
     - yes
     - no
     - high
   * - 7
     - Workflows (CI/CD)
     - | Wrong workflow triggered (wrong event, branch, or path).
       | CI/CD jobs run on unintended code or skip required checks.
     - yes
     - | PR reviews
       | Code reviews and approvals help catch data issues before merging.
     - yes
     - no
     - high
   * - 8
     - Workflows (CI/CD)
     - | Workflow passes with undetected errors (false positive).
       | CI/CD reports success but actual build/test failed or was skipped.
     - yes
     - | Log analysis.
       | Ensure that underlying build/test tools correctly return error code and have proper logging.
     - yes
     - no
     - high
   * - 9
     - Workflows (CI/CD)
     - | Workflow fails due to external service outage (e.g., Actions runner, artifact storage).
       | Build/test is blocked or incomplete due to third-party service unavailability.
     - no
     - no
     - yes
     - no
     - high
   * - 10
     - Artifact storage
     - | Release artifacts not published or corrupted.
       | Release process is blocked or produces incomplete/corrupted results.
     - no
     - no
     - yes
     - no
     - high
   * - 11
     - Artifact storage
     - | Artifacts published to wrong location or with wrong version/tag.
       | Downstream consumers use incorrect or outdated artifacts.
     - yes
     - | Manual review of release process and artifacts.
       | Release process includes manual checks to verify artifact correctness.
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
GitHub does not require qualification for use in safety-related software development according to ISO 26262.
Suggested safety and security measures should be applied to mitigate identified risks.



.. [1] The tool version mentioned in this document is preliminary.
       It is subject to change and will be updated in future.
