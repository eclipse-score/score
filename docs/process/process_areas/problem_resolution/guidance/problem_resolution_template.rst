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

Problem Template
================

.. gd_temp:: Problem Template
   :id: gd_temp__problem__template
   :status: valid
   :complies: std_req__iso26262__support_9, std_req__iso26262__support_10, std_req__iso26262__support_11, std_req__aspice_40__SUP-9-BP1, std_req__aspice_40__SUP-9-BP2, std_req__aspice_40__SUP-9-BP3, std_req__aspice_40__SUP-9-BP4,

Problem status
--------------
[“open”, “in review”, “in implementation”, “closed”, “rejected”, “cancelled”]


Problem submitter
-----------------
[Who is the reporter of the problem?]


Problem description
-------------------

[What is the problem?]
Determine the cause of the problem.
Determine the impact of the problem.
Is notification required due to determined impact on affected parties.

Problem supporting information
------------------------------

[How to reproduce the problem?]


Problem stakeholder
-------------------

[What are the potential stakeholder to resolve the problem?]


Problem category
----------------

[User, Bug, Quality]
[Safety anomaly, Vulnerability]

User: Problems relating to requirements, design, ore code found by user of the platform.

Bug: Problems found by contributor based on component, feature or platform integration tests.

Quality: Problems or gaps found by Quality Management activities as defined in the Quality
Management Plan.

Additional qualifier to emphasisif  potentially safety or security is affected:
Safey anomaly, Vulnerability


Problem classification
----------------------

[trivial, minor, major, critical, blocker]

Classify the problem severity

Use trivial, if the impact is negligible on the project

| Use minor, if the impact is not significant of the project
| The problem does not restrict usage of features in a significant manner
| Resolution may be scheduled to any planned future SW release

| Use major, if the impact does effect the quality of the project
| The problem can be solved with work-arounds for affected features
| Resolution shall be scheduled to next planned future SW release

| Use critical, if the impact does not prohibit to use the project, but quality cannot be guaranteed
| The problem affects a complete feature, that they are partly or complete not behave as expected
| Resolution shall be scheduled to next planned future SW release or to a new planned intermediate release

| Use blocker, if the impact prohibits using the project
| The problem affects more than one feature, that they are partly or complete not behave as expected
| Safety or Security risks identified
| Resolution shall be provided upon availability, if urgent resolution is required

Determine if Urgent resolution is required? (yes, no, only valid for blocker)


Problem expected closure date
-----------------------------

[Milestone when the problem should be resolved]


Problem solutions
-----------------

[What are measures to solve the problem?]

Specifiy the measures to resolve the problem, based on a rationale

Verify the effectiveness of the implemented measure

Report the results of the verification

Are all arguments convincing


Problem escalations
-------------------

[Document escalation activities?]
