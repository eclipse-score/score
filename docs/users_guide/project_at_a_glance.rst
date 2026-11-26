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

.. _project_at_a_glance:

Project at a Glance
===================

The short track through S-CORE: how the project is organized, which meetings matter, the key processes
and where to find the details.

.. image:: _assets/project_organization.drawio.svg
   :alt: S-CORE project organization: Project Lead Circle, Communities and Feature Teams
   :align: center
   :width: 75%

Who does what
-------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Body
     - Responsibility
   * - **Project Lead Circle (PLC)**
     - Strategic and technical decisions, triage of feature requests, adding/removing repositories,
       release planning and approval, escalation
   * - **Communities**
     - Topics that span all modules; each has a Community Lead and a deputy
   * - **Feature Teams**
     - One module each, from architecture to integration test; each has a Lead and at least one Committer

Most important meetings
-----------------------

All meetings are open to everyone. Dates and times are in the
`S-CORE calendar <https://calendar.google.com/calendar/u/0/embed?src=c_2ampi2bmoka3qter4dceap1d5g@group.calendar.google.com&ctz=Europe/Berlin>`__;
the *General Information* discussion of each team and community (*info*) names its members, meeting, Slack channel
and backlog, and the minutes are posted in the
`GitHub Discussions <https://github.com/orgs/eclipse-score/discussions>`__.

.. list-table::
   :header-rows: 1
   :widths: 28 54 18

   * - Meeting
     - What happens
     - Links
   * - **Project Lead Circle (PLC)**
     - Status of milestones, bugs and open feature requests; review of product increments, epics and tasks;
       decisions on releases, versioning, scope and escalations.
     - `info <https://github.com/orgs/eclipse-score/discussions/104>`__ · `minutes <https://github.com/orgs/eclipse-score/discussions/516>`__
   * - **Leads Alignment** (Project Leads, Community Leads, Feature Team Leads)
     - All leads sync: cross-team dependencies, blockers, information from the PLC to the teams and
       escalations from the teams to the PLC.
     - `minutes <https://github.com/orgs/eclipse-score/discussions/434>`__
   * - **Architecture Community**
     - Architecture questions, contribution pitches and FEP reviews; cancelled when there are no agenda items.
     - `info <https://github.com/orgs/eclipse-score/discussions/110>`__ · `minutes <https://github.com/orgs/eclipse-score/discussions/2457>`__
   * - **SW Development Process Community**
     - Process development (news, updates, improvements), safety, security and quality management, process
       implementation in the tooling.
     - `info <https://github.com/orgs/eclipse-score/discussions/108>`__ · `minutes <https://github.com/orgs/eclipse-score/discussions/407>`__
   * - **Safety Topics / Safety Management**
     - Safety management and safety analyses across modules.
     - `minutes <https://github.com/orgs/eclipse-score/discussions/2234>`__
   * - **Security Topics / Security Management**
     - Security management, threat analyses and security topics across modules.
     - `minutes <https://github.com/orgs/eclipse-score/discussions/2226>`__
   * - **Infrastructure Community**
     - Toolchains (C++, Rust, Python), CI/CD, devcontainer, docs-as-code, repository standards.
     - `info <https://github.com/orgs/eclipse-score/discussions/107>`__ · `minutes <https://github.com/orgs/eclipse-score/discussions/236>`__
   * - **Testing Community**
     - Test strategy, ITF and test tooling.
     - `info <https://github.com/orgs/eclipse-score/discussions/109>`__ · `minutes <https://github.com/orgs/eclipse-score/discussions/2391>`__
   * - **Integration & Release** (reference_integration)
     - Integration status, results of the weekly pre-release check, release preparation (release branches,
       release notes, known issues).
     - `info <https://github.com/orgs/eclipse-score/discussions/2884>`__ · `minutes <https://github.com/orgs/eclipse-score/discussions/1595>`__
   * - **Feature Team meetings**
     - Progress, issue and PR triage, planning of the module:
       Baselibs (`info <https://github.com/orgs/eclipse-score/discussions/1223>`__, `minutes <https://github.com/orgs/eclipse-score/discussions/2390>`__),
       Communication/IPC (`info <https://github.com/orgs/eclipse-score/discussions/112>`__, `minutes <https://github.com/orgs/eclipse-score/discussions/categories/communication-ft>`__),
       Lifecycle (`info <https://github.com/orgs/eclipse-score/discussions/1798>`__, `minutes <https://github.com/orgs/eclipse-score/discussions/2386>`__),
       Logging (`info <https://github.com/orgs/eclipse-score/discussions/114>`__, `minutes <https://github.com/orgs/eclipse-score/discussions/categories/logging-ft>`__),
       Persistency (`info <https://github.com/orgs/eclipse-score/discussions/116>`__, `minutes <https://github.com/orgs/eclipse-score/discussions/2518>`__),
       Config Management (`info <https://github.com/orgs/eclipse-score/discussions/2283>`__, `minutes <https://github.com/orgs/eclipse-score/discussions/2311>`__),
       Time (`info <https://github.com/orgs/eclipse-score/discussions/2890>`__, `minutes <https://github.com/orgs/eclipse-score/discussions/2645>`__).
     - see each team

How the meetings work together
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: _assets/project_meetings.drawio.svg
   :alt: S-CORE meetings and the main processes between them
   :align: center
   :width: 75%

|

#. **Feature request:** a Feature Team (or any contributor) brings a FEP to the **Architecture Community**;
   it is reviewed there, goes through the Final Comment Period and ends as a Decision Record, which the
   **PLC** sees for its roadmap.
#. **Integration & release:** Feature Teams release their modules; the **reference_integration** meeting
   checks them every week in the pre-release check and prepares the platform release, which the **PLC**
   approves.
#. **Status & escalation:** Feature Teams report status and blockers to the **Leads Alignment**; what cannot
   be solved there goes to the **PLC**, and decisions flow back the same way.
#. **Rules & tooling:** the **Process, Safety and Security** meetings define the rules, **Infrastructure and
   Testing** provide toolchains, CI and test frameworks that all Feature Teams use.

Communities in one line
-----------------------

- **Architecture:** platform architecture, new features (FEP review), coding guidelines
- **Process:** development process incl. safety, security, quality (``process_description``)
- **Infrastructure:** toolchains, devcontainer, docs-as-code, CI/CD, Bazel registry
- **Testing:** test strategy, ITF, testing tools
- **Integration & Release:** ``reference_integration``, platform releases
- **Marketing & Communication:** website, events, public relations

Most important concepts
-----------------------

Common
^^^^^^

- **Decisions go up, work goes sideways:** the PLC decides; Communities set common rules; Feature Teams build
  the modules.
- **Teams are created or closed by the PLC.** A new team gets a GitHub team, repositories, CODEOWNERS, a
  project board, a label (``community:`` / ``ft:``) and a Slack channel.
- **Everything is open:** all meetings are in the S-CORE calendar and open to everyone; minutes are public in
  the GitHub Discussions.
- **Members and leads are defined by the CODEOWNERS** of the owned repositories.

Feature Request (FEP)
^^^^^^^^^^^^^^^^^^^^^

New features and changes with impact on the platform or other teams go through the
**Feature & Enhancement Proposal (FEP)** track: the proposal is reviewed by the Architecture Community and
decided after a Final Comment Period; changes inside one team use the normal Issue/PR flow. The process is
described in the :ref:`FEP guideline <feature_request_guideline>`.

As defined in the :doc:`Project Management Plan </platform_management_plan/project_management>`, the PLC triages
incoming requests and is notified once a FEP enters its Final Comment Period.

Decision Record (DR)
^^^^^^^^^^^^^^^^^^^^

- Every relevant decision is a **Decision Record** (``dec_rec`` need) in :doc:`/design_decisions/index`,
  created by PR.
- Grouped by category: **strategy, architecture, infrastructure, process, integration, AI**
  (e.g. ``DR-003-Strat`` module maturity levels).
- Status: ``proposed`` → ``accepted``; a DR keeps the original decision and rationale, guidelines built on it
  may evolve separately.
- Accepted FEPs become DRs; a team may also write a DR for its own decisions to persist the rationale.

Integration & Release process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Releases** are `milestones <https://github.com/eclipse-score/score/milestones>`__ in the score repository,
  planned and approved by the PLC.
- **Modules** release independently (strict SemVer) into the
  `S-CORE Bazel registry <https://github.com/eclipse-score/bazel_registry>`__. SemVer applies to the
  **public API and features**: only a backward-incompatible change (breaking API change, removed or
  incompatibly changed feature) means a new MAJOR version; compatible enhancements are MINOR, fixes PATCH.
- **Reference Integration** pins every module in
  `known_good.json <https://github.com/eclipse-score/reference_integration/blob/main/known_good.json>`__
  (release or exact commit), builds them together and runs tests, showcases and images on all target
  platforms (see :ref:`integration_process`).
- **Weekly pre-release check:** every week all modules are bumped to their latest release on a pre-release
  branch to see early whether they still work together; modules already pinned to a newer, not yet released
  commit keep that commit, so the check may also include unreleased code.
- **Release:** release candidate branch → release note with module versions and **maturity** per module
  (Release / Experimental / Preview, :need:`DR-003 <dec_rec__strat__module_maturity_levels>`).

Module Maturity
^^^^^^^^^^^^^^^

Every module in a platform release carries exactly one maturity level
(:need:`dec_rec__strat__module_maturity_levels`). This lets all modules be part of the release while telling
users how far each one is.

.. list-table::
   :header-rows: 1
   :widths: 16 24 34 26

   * - Level
     - Process artifacts
     - Requirements
     - Quality statement
   * - **Preview**
     - none or incomplete
     - undetermined
     - not possible
   * - **Experimental**
     - complete
     - not all implemented / tested, gaps are transparent
     - yes, with known gaps
   * - **Release**
     - complete, only minor deviations
     - all implemented and fully tested
     - yes

- **Artifacts first:** without the process artifacts (verification report, traceability, inspection
  checklists) no quality statement is possible, so the module stays Preview.
- **Declared by the module:** each module sets ``:maturity: preview | experimental | release`` on its ``mod``
  need in its own docs (docs-as-code); the release note shows it per module.
- **Not yet defined:** exact border between minor and major deviations, who approves a level, and downgrades
  when the process changes.

Most important links
--------------------

All links to organization, meetings, contribution, decisions, integration & release, repositories and tooling
are collected in :ref:`useful_links`.
