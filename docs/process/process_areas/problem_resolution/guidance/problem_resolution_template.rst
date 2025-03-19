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

.. _prm_templates:

Problem Report Template
=======================

.. gd_temp:: Problem Template
   :id: gd_temp__problem__template
   :status: valid
   :complies: std_req__aspice_40__SUP-9-BP1, std_req__aspice_40__SUP-9-BP2, std_req__aspice_40__SUP-9-BP3, std_req__aspice_40__SUP-9-BP4,

Problem status
--------------
[“open”, “in review”, “in implementation”, “closed”, “rejected”]

If possible, use for problem status the properties of the selected Issue Tracking System
(for implementation see here :need:`doc__platform_problem_resolution_plan`)

| (to be filled out during :need:`wf__problem__create_pr`)
| (to be updated during :need:`wf__problem__analyse_pr`)
| (to be updated during :need:`wf__problem__initiate_monitor_pr`)

Problem submitter
-----------------
[Who is the reporter of the problem?]

(to be filled out during :need:`wf__problem__create_pr`)

Problem description
-------------------

[What is the problem?]

| Determine the cause of the problem, if possible.
| Determine the impact of the problem, if possible.
| Is notification required due to determined impact on affected parties?

| (to be filled out during :need:`wf__problem__create_pr`)
| (to be updated during :need:`wf__problem__analyse_pr`)

Problem supporting information
------------------------------

[How to reproduce the problem?]

(to be filled out during :need:`wf__problem__create_pr`)

Problem anaylsis results
------------------------

[What is the problem analysis result?]

| Especially document rejection Reason
| Determine the safety/security impact, if applicable

(to be filled out during :need:`wf__problem__analyse_pr`)

Problem stakeholder
-------------------

[What are the potential stakeholder to resolve the problem?]

Add affected feautre, if possible

If possible, use for problem status the properties of the selected Issue Tracking System
(see implementation here :need:`doc__platform_problem_resolution_plan`)

(to be filled out during :need:`wf__problem__create_pr`)

Problem category
----------------

[User, Bug]

[Safety affected, Security affected, Quality affected]

User: Problems relating to requirements, design, ore code found by user of the platform.

| Bug:
| Problems found by contributor based on component, feature or platform integration tests.
| Problems or gaps found by Quality Management activities as defined in the Quality Management Plan.

Safety, Security, Quality: Additional qualifier to highlight, if safety, security or quality is affected

(to be filled out during :need:`wf__problem__create_pr`)

Problem classification
----------------------

[minor, major, critical, blocker]

Classify the problem severity

| Use minor, if the impact is not significant of the project
| The problem does not restrict usage of features in a significant manner
| Resolution may be scheduled to any planned future SW release

| Use major, if the impact does effect the quality of the project
| The problem can be solved with work-arounds for affected features
| Resolution shall be scheduled to next planned future SW release

| Use critical, if the impact does not prohibit to use the project, but quality cannot be guaranteed
| The problem affects a complete feature, that they are partly or complete not behave as expected
| Resolution shall be scheduled to next planned future SW release or to a new planned intermediate release, if urgent resolution is required

| Use blocker, if the impact prohibits using the project
| The problem affects more than one feature, that they are partly or complete not behave as expected
| Safety or Security risks identified
| Resolution shall be provided upon availability

Determine if Urgent resolution is required? (yes, no, only valid for critical, blocker)

| (to be filled out during :need:`wf__problem__create_pr`)
| (to be updated during :need:`wf__problem__analyse_pr`)

Problem expected closure date
-----------------------------

[Milestone when the problem should be resolved]

If possible, use for problem status the properties of the selected Issue Tracking System
(for implementation see here :need:`doc__platform_problem_resolution_plan`)

(to be filled out during :need:`wf__problem__create_pr`)

Problem solutions
-----------------

[What are measures to solve the problem?]

Specifiy the measures to resolve the problem, based on a rationale

Verify the effectiveness of the implemented measure

Report the results of the verification

Are all arguments convincing

| (to be filled out during :need:`wf__problem__initiate_monitor_pr`)
| (to be updated during :need:`wf__problem__close_pr`)

Problem escalations
-------------------

[Document escalation activities?]

| (to be filled out during :need:`wf__problem__initiate_monitor_pr`)
| (to be updated during :need:`wf__problem__close_pr`)
