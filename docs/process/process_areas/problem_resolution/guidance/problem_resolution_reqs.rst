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

.. _prm_process_requirements:

Process Requirements
====================

.. _prm_process_problem_attributes:

Problem Attributes
------------------

.. gd_req:: Problem attribute: UID
   :id: gd_req__problem__attr_uid
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1

   Each Problem shall have a unique ID. It shall be in an integer number.

.. gd_req:: Problem attribute: status
   :id: gd_req__problem__attr_status
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1

   Each Problem shall have a status:

      * open
      * in review
      * in implementation
      * closed
      * rejected

.. gd_req:: Problem attribute: title
   :id: gd_req__problem__attr_title
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1

   Reason for Problem Report

.. gd_req:: Problem attribute: description
   :id: gd_req__problem__attr_impact_description
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1, std_req__aspice_40__SUP-9-BP2

   Exact description of the Problem, including potential cause and impact of the problem.

   Record especially, if functional safety or cybersecurity may affected here.

   Record potential affected parties, and if it may requried to notify them about the potential
   problem.

.. gd_req:: Problem attribute: analysis results
   :id: gd_req__problem__attr_anaylsis_results
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP2

   Record analysis results (e.g. reason for rejection, safety, security, quality impact)

.. gd_req:: Problem attribute: stakeholder
   :id: gd_req__problem__attr_stakeholder
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP2, std_req__aspice_40__SUP-9-BP5

   Assign responsible stakeholder for analysing the problem
   Assign responsible stakeholder to resolve the problem

.. gd_req:: Problem attribute: classification
   :id: gd_req__problem__attr_classification
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1, std_req__aspice_40__SUP-9-BP2

   Each Problem shall have a classification identifier:

      * minor
      * major
      * critical
      * blocker

.. gd_req:: Problem attribute: category
   :id: gd_req__problem__attr_category
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1

   Each Problem shall have a category identifier:

      * User
      * Bug

.. gd_req:: Problem attribute:: safety affected
   :id: gd_req__problem__attr_safety_affected
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1

   Each Problem shall have a safety relevance identifier:

      * Yes
      * No

.. gd_req:: Problem attribute:: security affected
   :id: gd_req__problem__attr_security_affected
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1

   Each Problem shall have a security relevance identifier:

      * Yes
      * No

.. gd_req:: Problem attribute:: quality affected
   :id: gd_req__problem__attr_quality_affected
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1

   Each Problem shall have a quality relevance identifier:

      * Yes
      * No

.. gd_req:: Problem attribute: milestone
   :id: gd_req__problem__attr_milestone
   :status: valid
   :tags: problem_resolution, attribute, mandatory
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1, std_req__aspice_40__SUP-9-BP6

   Milestone until the Problem must be implemented (used for prioritization)


Problem Resolution Checks
'''''''''''''''''''''''''

.. gd_req:: Problem Resolution mandatory attributes provided
   :id: gd_req__problem__check_mandatory
   :status: valid
   :tags: problem_resolution, attribute, check
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1

   It shall be checked if all mandatory attributes for each Problem
   is provided by the user. For all requirements following attributes shall be mandatory:

   .. needtable:: Overview mandatory problem attributes
      :filter: "mandatory" in tags and "attribute" and "problem_resolution" in tags
      :style: table
      :columns: title
      :colwidths: 30

.. gd_req:: Problem Report issues closing constraints
   :id: gd_req__problem__check_closing
   :status: valid
   :tags: problem_resolution, attribute, check
   :satisfies: wf__problem__create_pr, wf__problem__analyse_pr, wf__problem__initiate_monitor_pr, wf__problem__close_pr
   :complies: std_req__aspice_40__SUP-9-BP1

   ISSUEs related to Problem Reports shall not automatically closed, if linked ISSUEs or PRs are closed or merged and
   these ISSUEs shall be closed only manually from the :need:`Committer <rl__committer>`.
