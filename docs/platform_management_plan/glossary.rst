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

.. document:: Platform Management Glossary
   :id: doc__platform_management_glossary
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :tags: platform_management
   :realizes: wp__project_mgt[version==1]

Glossary
========

This glossary collects terms used in the Platform Management Plan (PMP) and
shared terms used across the S-CORE workspace.

PMP Terms
---------

.. glossary::

   Platform Management Plan (PMP)
      The project-level management framework that defines how S-CORE plans,
      governs, tracks, and improves platform development activities.

   Change Request
      The required vehicle to introduce a new feature or component, or to
      modify existing scope, including analysis, implementation, and closure.

   Problem Resolution
      The workflow to report, analyze, resolve, and close a deviation from an
      expected result.

   Configuration Item
      Any project artifact under configuration control, including documents,
      code files, tool versions, and related metadata.

   Baseline
      A consistent, tagged set of repository artifacts used as a controlled
      reference for releases and traceable reconstruction.

   Release Branch
      A branch derived from main and used to prepare a release with restricted
      changes such as fixes and verification improvements.

   Experimental Release
      A release during development where safety-package related artifacts may
      still be incomplete.

   Official Release
      A release with full process execution and documented release evidence,
      including release notes and verification artifacts.

   Platform Verification
      Verification activity at integrated platform level, including platform
      integration tests on reference hardware.

   Quality Manager
      Independent role responsible for quality assurance guidance, process
      conformance support, and reporting.

   Security Manager
      Role responsible for coordinating platform security activities,
      vulnerability handling, and related escalations.

   Safety Manager
      Role responsible for coordinating functional safety activities,
      tailoring, planning, and safety-related reviews.

   Project Lead Circle (PLC/TLC)
      Steering body for strategic technical and project decisions, including
      release planning, repository scope, and escalations.

   Community Lead
      Person coordinating cross-functional community work streams such as
      architecture, process, infrastructure, testing, and integration.

Workspace and Tooling Terms
---------------------------

.. glossary::

   Docs-as-Code
      Documentation approach where requirements, plans, and process artifacts
      are maintained as versioned text and generated automatically.

   Sphinx
      Documentation generator used to build HTML output from reStructuredText
      sources.

   Sphinx-Needs
      Sphinx extension used to model project artifacts as typed, traceable
      objects with attributes and links.

   PlantUML
      Text-based diagramming tool used for architecture and interaction
      diagrams.

   Draw.io
      Diagramming tool used for process and concept visuals where free-form
      diagrams are needed.

   Bazel
      Build and test system used across the workspace for software,
      documentation, and automation targets.

   MODULE.bazel
      Repository module metadata file used to define versioning and dependency
      relationships for Bazel module resolution.

   Continuous Integration (CI)
      Automated build, test, and verification execution for contributions and
      integration quality gates.

   GitHub Issues
      Primary tracking mechanism for planning, change requests, problem
      reports, and vulnerability handling.

   GitHub Pull Request (PR)
      Review and merge mechanism used to implement and approve controlled
      changes to project artifacts.

   CODEOWNERS
      Repository ownership mapping used to enforce review and approval from
      designated responsible roles.

   Dependabot
      Automated dependency monitoring and update mechanism used to identify
      known vulnerabilities in external packages.

   Software Bill of Materials (SBOM)
      Structured inventory of software components and metadata used for supply
      chain transparency and vulnerability management.

   SPDX
      Open standard format for software bill of materials and license
      information exchange.

   CycloneDX
      Open SBOM format focused on software supply chain security use cases.

   CVE
      Publicly tracked identifier for a disclosed software vulnerability.

   CVSS
      Standard scoring system used to rate vulnerability severity.

Standards and Abbreviations
---------------------------

.. glossary::

   ISO 26262
      International standard for functional safety of road vehicles, applied in
      S-CORE with project-defined tailoring.

   ISO SAE 21434
      International standard for road-vehicle cybersecurity engineering,
      applied in S-CORE with project-defined tailoring.

   ASPICE
      Automotive SPICE process assessment model used as process quality
      reference for software engineering and management practices.

   ASIL
      Automotive Safety Integrity Level classification used to define required
      rigor for safety-related development and verification activities.

   QM
      Quality Management classification for non-safety-rated software parts,
      typically allowing reduced rigor compared to ASIL-rated parts.

   SEooC
      Safety Element out of Context. A safety element developed independently
      of a concrete system integration context.

   OoC
      Out of Context. Development approach where a platform or component is
      engineered without a fully fixed end-system context.

   Tool Confidence Level (TCL)
      Classification used in tool management to decide whether tool
      qualification is required for safe and secure use.

   PLC
      Project Lead Circle. Project-level leadership function represented in the
      combined PLC/TLC steering format.

   TLC
      Technical Lead Circle. Technical leadership function represented in the
      combined PLC/TLC steering format.

   ARC
      Architecture Community. Cross-functional community for architecture
      topics, including feature discussions and coding-guideline alignment.

   PRC
      Process Community. Cross-functional community responsible for defining
      and maintaining development processes and process implementation.

   INF
      Infrastructure Community. Cross-functional community responsible for
      common development infrastructure and toolchain topics.

   MCM
      Module Community Management. Community function used to coordinate module
      community management activities in project governance.

   CodeQL
      Static analysis technology used in CI to detect vulnerabilities,
      weaknesses, and code quality issues.

   Eclipse Contributor Agreement (ECA)
      Eclipse Foundation agreement required for contribution eligibility and
      correct contribution attribution.
