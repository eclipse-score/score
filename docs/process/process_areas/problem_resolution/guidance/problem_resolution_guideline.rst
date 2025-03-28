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

.. gd_guidl:: Problem Resolution Guideline
   :id: gd_guidl__problem__problem
   :status: valid
   :complies: std_req__aspice_40__SUP-9-BP1, std_req__aspice_40__SUP-9-BP5, std_req__aspice_40__SUP-9-BP6, std_req__aspice_40__SUP-9-BP7

This document describes the general guidances for Problem Resolution based on the concept which is defined :need:`[[title]]<doc_concept__problem__process>`.

General Hints
=============

The detailed implementation of the Problem Resolution for **S-CORE** is described in the :need:`[[title]]<doc__platform_problem_resolution_plan>`.

Templates
---------

To create problem reports, **S-CORE** provides the following template: :need:`[[title]]<gd_temp__problem__template>`.

Attributes
----------

For all Problems following mandatory attributes need to be defined:

.. needtable:: Overview of mandatory problem resolution attributes
   :tags: problem_resolution
   :filter: "mandatory" in tags and "attribute" in tags and type == "gd_req"
   :style: table
   :columns: title
   :colwidths: 30


* ID: Unique integer number
* For the remaining attributes only predefined values can be used. A more detailed description can
  be found here: :ref:`prm_attributes`


.. _workflow_prm_requirements:

Activities for Problem Resolution
=================================

This section describes in detail which steps need to be performed for a Problem resolution.

Refer to the :need:`Problem Resolution Plan <doc__platform_problem_resolution_plan>` for examples
how to create problem reports.

.. list-table:: Activities for Problem Resolution
   :header-rows: 1
   :widths: 10,60,30

   * - Step
     - Description
     - Responsible
   * - :ref:`1. <prm_create_problem_report>`
     - Create Problem Report
     - :need:`[[title]] <rl__contributor>`
   * - :ref:`2. <prm_analyze_problem_report>`
     - Analyse Problem Report
     - :need:`[[title]] <rl__contributor>`
   * - :ref:`3. <prm_initiate_problem_resolution>`
     - Initiate and Monitor Problem Resolution
     - :need:`[[title]] <rl__contributor>`
   * - :ref:`4. <prm_monitor_problem_resolution>`
     - Close Problem Resolution
     - :need:`[[title]] <rl__committer>`


.. _prm_create_problem_report:

Create Problem Report
---------------------

:need:`[[title]] <rl__contributor>` creates the problem report in the defined Issue Tracking
System based on the provided template.
It is expected, that the UID will be provided by the Issue Tracking System.

The title of the Problem report should reflect the topic accordingly.

The description should reflect the detailed problem root causes and impact.

Copy therefore the :need:`Problem Template <gd_temp__problem__template>` into the created Problem
Report (Issue Tracking System).

Set the status of the Problem to "open", when ready to analyse and review set to "in review".

.. _prm_analyze_problem_report:

Analyse Problem Report
----------------------

The **S-CORE** :need:`[[title]] <rl__committer>` analyzes the problem together with the
:need:`[[title]] <rl__contributor>` and takes a decision for accepting or to
rejecting it.

If accepted, the status is set to "in implementation" and :need:`[[title]] <rl__contributor>`
can start with the iniation of the problem resolution, otherwise the status is set to "rejected".

:need:`[[title]] <rl__contributor>` has the freedom to cancel it at any time by setting the status
to "cancelled".

.. _prm_initiate_problem_resolution:

Initiate and Monitor Problem Resolution
---------------------------------------

:need:`[[title]] <rl__contributor>` initiates the resolution of the Problem.

Therefore further activities needs to be planned and linked to the Problem Report.

During the resolution the responsible lead :need:`[[title]] <rl__technical_lead>` or
:need:`[[title]] <rl__module_lead>` reports regularly the status to the affected **S-CORE** teams.

:need:`[[title]] <rl__contributor>` has the freedom to cancel it at any time by setting the status
to "cancelled".

.. _prm_monitor_problem_resolution:

Close Problem Resolution
------------------------

During the resolution the :need:`[[title]] <rl__contributor>` monitors all activities linked to
the problem, until they are closed.

:need:`[[title]] <rl__committer>` checks finally if the problem resolution is sufficient before
the status is finally closed.
To check, if is is sufficient, :need:`Problem Checklist <gd_chklst__problem__cr_review>` may used.

:need:`[[title]] <rl__committer>` has the freedom to reject it at any time by setting the status
to "reject".
