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


Feature & Enhancement Proposal (FEP)
#####################################

.. document:: Feature Request Guideline
  :id: doc__feature_request_guideline
  :status: valid
  :version: 2
  :safety: QM
  :security: NO
  :realizes: wp__training_path[version==1]

.. _feature_request_guideline:

This guide describes the **Feature & Enhancement Proposal (FEP)**: part of S-CORE's change
process, and the Analyze step for *Feature* change requests and *Feature Modification* change
requests with major impact, for example changes affecting the platform or other Feature Teams
(see the :ref:`FEP Track <fep_track>` section of the :ref:`Change Management Plan <change_mgmt_plan>`).

Component-level and single-Feature-Team changes continue through the standard Analyze step
described in the :ref:`Change Management Plan <change_mgmt_plan>`. A Feature Team may still choose
to record such a change as a Decision Record if it wants a persisted rationale; that choice does
not by itself require a Shepherd or Final Comment Period, both of which are specific to the FEP
Track.

This guide is based on or references the following documents:

* :need:`FEP Decision Record (DR-002-Proc) <dec_rec__proc__fep_process>`, which records the original
  decision and its rationale
* :ref:`Change Management Plan <change_mgmt_plan>`, which defines the underlying ISSUE/PR change
  request infrastructure used by every FEP

.. note::
  This guide describes how the FEP is currently practiced and may evolve as the Architecture
  Community refines it. :need:`DR-002-Proc <dec_rec__proc__fep_process>` remains the frozen record
  of what was originally decided; it is not updated when this guide evolves.

Roles
================================

**Author** - the :need:`Contributor <rl__contributor>` proposing the change. Responsible for
writing and maintaining the FEP, integrating feedback, and driving consensus.

**Shepherd** - a :need:`Committer <rl__committer>` of the Architecture Community, not the author,
who guides the FEP to maturity and judges when it is ready for the Final Comment Period. Finding a
Shepherd is the author's responsibility. If no one is willing to shepherd a proposal, it does not
proceed.

**Architecture Community** - all :need:`Committers <rl__committer>` of the Architecture Community
(architects and Feature Team leads) with standing to review FEPs. During the Final Comment Period,
every member is expected to either raise a substantive objection or approve, explicitly or by
silence.

Labels
================================

``fep`` is applied to the FEP PR and its tracking Issue throughout the whole lifecycle, and is what
a board or filtered view is built on.

``fep:needs-shepherd`` is applied to the tracking Issue while no Shepherd is confirmed, and removed
once one is.

``fep:fcp`` is applied to the FEP PR only while it is in its Final Comment Period. Adding it starts
the FCP; the FCP bot mirrors it to the tracking Issue and removes it from both once the FCP closes.

``fep:breaking-change`` is applied to the FEP PR of a Breaking Change FEP (see `Breaking Change FEPs -
Additional Requirements`_), so that the FCP bot requires the explicit approval quorum.

A FEP that sees no activity for an extended period, most commonly while unshepherded or shepherded
but not yet ready for FCP, may be marked with the existing ``Stale`` label like any other inactive
issue. This does not reject the FEP; it signals that it has lost momentum and may be picked up again
later.

The Process: Five Phases
================================

**Phase 0 - Idea Exploration** (informal, no status)

Post the idea informally in the S-CORE architecture channel before writing anything formal. This
surfaces obvious problems early, finds prior related proposals, and identifies whether a Shepherd
might be willing to pick it up. Move to Phase 1 once you have a willing Shepherd.

**Phase 1 - Draft + Shepherd Shaping** (status: ``Draft - Needs Shepherd`` -> ``Draft -
Shepherded``)

Open a PR with your FEP draft, using the FEP template below. At the same time, open a tracking Issue
of type *Feature Request*, labeled ``fep`` and ``fep:needs-shepherd``, set to status ``Draft - Needs
Shepherd``, and reference it in the FEP via the ``:tracking:`` field. The Issue links back to the
FEP PR, giving bidirectional traceability.

Once a Shepherd is confirmed, remove the ``fep:needs-shepherd`` label, move the tracking Issue to
status ``Draft - Shepherded``, and update it to name the Shepherd.

Author and Shepherd iterate until the proposal is complete and well-argued. When the Shepherd judges
it ready, they propose entry into the Final Comment Period to the Architecture Community chair (or
proxy). The chair/proxy then formally announces the FCP across all channels, including Slack, moves
the tracking Issue to status ``Under Review``, and adds the ``fep:fcp`` label to the FEP PR. The
FEP PR description must reference the tracking Issue (for example ``Tracking: #1234``).

**Phase 2 - Final Comment Period (FCP)** (status: ``Under Review``)

The Architecture Community has 14 calendar days to engage. Objections must be substantive and
technical; the Shepherd distinguishes blocking from non-blocking feedback and can reset the FCP once
if a significant new issue requires a revised proposal.

Silence is approval. FCP closes with no unresolved blocking objections, the FEP is accepted. FCP
closes with unresolved blocking objections, the FEP is rejected. Escalation may intervene in
exceptional cases but is not the default path. Either way, the ``fep:fcp`` label is removed from the
tracking Issue once FCP closes.

The FCP is tracked by a bot (``.github/workflows/fep-fcp.yml``):

* **Notification**: when ``fep:fcp`` is added, the bot @-mentions the maintainers of every S-CORE
  module (as registered in the ``bazel_registry`` for the modules of the reference integration) and
  the Architecture Community in a PR comment. They are informed, not added as reviewers. The list of
  notified people and the start date are recorded in that comment, so it stays traceable who was
  informed and when.
* **Taking part**: stakeholders *Approve* the PR, or submit a *Request changes* review for a
  substantive, technical objection. The Shepherd dismisses change requests judged non-blocking.
  Reminders are posted 7 and 2 days before the deadline to groups that have not responded.
* **Closing**: after 14 days, groups that did not respond count as having approved. Reviews submitted
  after the deadline are ignored. The FEP is accepted unless an undismissed change request from a
  stakeholder remains; a Breaking Change FEP also needs explicit approvals from the Architecture
  Community quorum. The result is posted to the PR and the tracking Issue, and reported as the
  ``fep/fcp`` commit status.
* **Reset**: the Shepherd (or chair/proxy) comments ``/fcp reset`` on the FEP PR to restart the 14
  days once, which notifies all stakeholders again.

**Phase 3 - Decision** (status: ``Accepted`` | ``Rejected`` | ``Withdrawn``)

If the FCP closed cleanly, the FEP PR is merged and recorded as a Decision Record. If the FCP closed
with unresolved blocking objections, the FEP is rejected. The author may withdraw at any point
before acceptance. In each case, the tracking Issue's status is updated to match: ``Accepted``,
``Rejected``, or ``Withdrawn``.

Breaking Change FEPs additionally require explicit approval from a minimum quorum of Architecture
Community members; they cannot pass by silence alone.

**Phase 4 - Implementation Tracking** (status: ``Implementing`` -> ``Implemented``)

The tracking Issue opened in Phase 1 stays open, moves to status ``Implementing``, and becomes the
implementation tracking artifact; it can carry child Task issues for the implementing teams via
GitHub's sub-issue feature. It is closed only when the implementation, not the FEP, is merged, at
which point it moves to status ``Implemented`` before closing. If implementation reveals the
accepted design is materially wrong, file a follow-up FEP rather than diverging silently.

FEP Template
================================

FEPs use the same ``dec_rec`` need type as any other Decision Record (see the `Decision Record
Template`_).

.. _Decision Record Template: https://eclipse-score.github.io/process_description/main/folder_templates/platform/docs/change/decision_record.html

``:tracking:`` field is the one FEP-specific addition, linking the FEP to its tracking Issue from
Phase 1.

Breaking Change FEPs - Additional Requirements
================================================

A proposal classified as **Breaking Change** must additionally include:

* **Impact Inventory**: explicit list of known integrators, configurations, or customer deliverables
  that will break
* **Migration Path**: concrete steps integrators must take, with estimated effort
* **Deprecation Timeline**: if a grace period is offered, how long and how the old behavior is
  signaled as deprecated
* **Sign-off from Affected Teams**: acknowledgment, not necessarily approval, from leads of teams
  known to be directly affected before FCP entry
