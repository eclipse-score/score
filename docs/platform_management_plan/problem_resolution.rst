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

.. document:: Problem Resolution Plan
   :id: doc__platform_problem_resolution_plan
   :status: draft
   :safety: ASIL_B
   :tags: platform_management
   :realizes: wp__prm_plan

Problem Resolution / Problem Resolution Plan
--------------------------------------------

This document implements parts of the :need:`wp__platform_mgmt`.

Purpose
+++++++
The purpose of the Problem Resolution is to guide the resolution of problems
of a project including their creation, analysis, resolution, and control.
Where a problem is defined as a deviation of an expected results.


Objectives and Scope
++++++++++++++++++++

Problem Resolution Goals
^^^^^^^^^^^^^^^^^^^^^^^^

* Problems are recorded, identified and classified.
* Problems are analyzed and assessed to determine an appropriate solution.
* Problems resolution are initiated and monitored.
* Problems resolution are closed and communicated to affected parties.

Approach
++++++++

Problem Resolution Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contributions in general to the **S-CORE** project are described here
(compare :need:`gd_guidl__contr_request_guideline`).

A Problem Resolution is a specific contribution, and
it is the **ONLY** way to report problems in the **S-CORE** project.

Problem Resolution Infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:need:`GitHub Issues (ISSUE) <gd_guidl__issue_guideline>` are used for managing problems and their
potential resolution. The tool is used to create, analyse, initiate and to monitor the
problem reported within **S-CORE**.

The next figure gives an overview, how problems are created in **S-CORE**. An ISSUE is
used to create a problem report including required attributes as defined in
:ref:`prm_process_problem_attributes`. Therefore the Problem Template :ref:`prm_templates`
shall be used.

.. figure:: _assets/score_problem_resolution_overview.drawio.svg
  :width: 100%
  :align: center
  :alt: Problem Resolution Overview


Problem Resolution Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:ref:`prm_process_problem_attributes` are implemented as follows:

:need:`[[title]] <gd_req__problem__attr_uid>` is identical to the ISSUE number.

:need:`[[title]] <gd_req__problem__attr_status>` is defined by the combination of the ISSUE state
and the state in the Projects dashboard view.

.. list-table:: Problem Status
   :header-rows: 1
   :widths: 15,85,15

   * - Status
     - Issue status
     - Projects dashboard status
   * - open
     - ``Open``
     - ``No Status``
   * - in review
     - ``Open``
     - ``Todo``
   * - in implementation
     - ``Open``
     - ``In Progress``
   * - closed
     - ``Closed``
     - ``Done``
   * - rejected
     - ``Closed``
     - any beside ``Done``
   * - cancelled
     - ``Closed as not planned``
     - any beside ``Done``

:need:`[[title]] <gd_req__problem__attr_title>` is identical to the ISSUE title.

:need:`[[title]] <gd_req__problem__attr_impact_description>` is defined in the description part of the
ISSUE using the Problem Template :ref:`prm_templates`.

:need:`[[title]] <gd_req__problem__attr_category>` is defined in the description part of the
ISSUE using the Problem Template :ref:`prm_templates`.

:need:`[[title]] <gd_req__problem__attr_classification>` is defined in the description part of the
ISSUE using the Problem Template :ref:`prm_templates`.

Problems are clustered in the following categories:

.. list-table:: Problem Categories
   :header-rows: 1
   :widths: 15,85,15

   * - Category
     - Description
     - Infrastructure
   * - User
     - Created by any user or :need:`Contributor <rl__contributor>` to report potential identified problems
     - ISSUE with type BUG
   * - Bug
     - Created by :need:`Contributor <rl__contributor>` to report problems found during verification
     - ISSUE with type BUG and with label ``<test level>``
   * - Quality
     - Created by :need:`Contributor <rl__contributor>` or :need:`Contributor <rl__committer>` to report problems during quality management activities
     - ISSUE with type BUG and with label ``quality``

:need:`[[title]] <gd_req__problem__attr_milestone>` is defined by the Milestone of a ISSUE.


Problem Resolution Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In General, every Problem resolution follows the following steps:
| (color is refering to the following figure: Problem Resolution Simple Workflow Overview)

* 1. Create the Problem report (grey color)
* 2. Analyse the Problem report (blue color)
* 3. Initiate the implementation of the Problem resolution and track it to closure (yellow color)
* 3. Close Problem resolution (purple color)


**To 1. Create the Problem report:**

An ISSUE is the **ONLY** way to create and manage a Problem in **S-CORE**.

The figure below shows the workflow for the simplest case of a problem resolution workflow.

An ISSUE with the type ``Bug`` is created in status ``Open``.
The title of the ISSUE reflects the potential problem. Further add here the
:need:`Problem Template <gd_temp__problem__template>` and fill it out accordingly.

Planning is done by setting the milestone of the ISSUE accordingly.

Problem status: ``open`` is implemented as
ISSUE status ``Open`` and Projects status ``No Status``.

To trigger the next step: Problem status: ``in review``
keep the ISSUE status ``Open`` and set the Projects status ``Todo``.

To cancel the problem report: Problem status: ``cancelled``
set the ISSUE status ``Closed as not planned``.

.. figure:: _assets/score_problem_resolution_workflow_simple.drawio.svg
  :width: 100%
  :align: center
  :alt: Problem Resolution Simple Workflow Overview

  Problem Resolution Simple Workflow Overview


**To 2. Analyse the Problem report:**

The Problem report is reviewed and analysed from the :need:`Committer <rl__committer>` and the
review results are resolved by the :need:`Contributor <rl__contributor>`. The results
are documented in the ISSUE. As long as the information is not sufficient, the related ISSUE is kept in
status status ``Open`` and Projects status ``Todo``, means ``in review``.

If the information is sufficient and it is decided to initiate the problem resolution, the
ISSUE status is kept ``Open`` and the Projects status is set to ``In Progress``.

:ref:`prm_checklist` can help to verify whether the information is complete.

In case affected parties need to be informed :need:`Technical Lead <rl__technical_lead>` or
:need:`Module Lead <rl__module_lead>` will notfiy them.

Otherwise, if no problem resolution is planned, the problem is rejected.
To reject the problem report: Problem status: ``rejected``
set the ISSUE status ``Closed``.


**To 3. Initiate and Monitor the Problem resolution:**

:need:`Contributor <rl__contributor>` starts all required activities to resolve the problem.
These may include starting Change Requests or in general plannig activites by creating ISSUEs and
required PRs.

All ISSUEs or PRs created to resolve the problem are linked to the problem report ISSUE to enable
monitoring of the activities.

All activities defined are tracked until closure, means that all linked ISSUEs or PRs are closed or
merged, respectively.

If all are closed or merged :need:`Contributor <rl__contributor>` sets Projects status to ``Done``
to trigger the final review from the :need:`Committer <rl__committer>` to close the problem resolution.


In case it is cancelled, set the ISSUE status ``Closed as not planned``.

The problem resolution may also rejected in this phase, the ISSUE status is set to ``Closed``.

**To 4. Close the Problem resolution:**

:need:`Committer <rl__committer>` checks finally if the Problem is completely resolved. In this
case all linked ISSUEs or PRs are closed or merged, respectively.

Especially the solution measure must be checked for their effectivness and the argumentation
is convincing.

:ref:`prm_checklist` can help to verify whether it can be closed.

If this is the case the ISSUE status is set to ``Closed``, otherwise the Projects status is set
back to ``In Progress``.


Problem Resolution SW Platform Work Products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: SW Platform work products
    :header-rows: 1

    * - work product Id
      - Link to process
      - Process status
      - Link to issue
      - Link to WP
      - WP status

    * - :need:`wp__issue_track_system`
      - :doc:`index`
      - :ndf:`copy('status', need_id='doc__platform_mgt_plan')`
      - n/a
      - `Project issues <https://github.com/eclipse-score/score/issues>`_
      - established

    * - :need:`wp__platform_mgmt`
      - :need:`wf__cr_mt_platform_mngmt_plan`
      - :ndf:`copy('status', need_id='wf__cr_mt_platform_mngmt_plan')`
      - <Link to issue>
      - :doc:`index`
      - :ndf:`copy('status', need_id='doc__platform_mgt_plan')`

    * - :need:`wp__process_definition`
      - :need:`wf__def_app_process_definition`
      - :ndf:`copy('status', need_id='wf__def_app_process_definition')`
      - `Process community issues <https://github.com/orgs/eclipse-score/projects/7>`_
      - :ref:`process_description`
      - <automated>
