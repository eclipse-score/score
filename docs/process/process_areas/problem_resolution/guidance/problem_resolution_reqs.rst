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
   :tags: attribute, mandatory
   :satisfies: wf__problem__cr_an_problem, wf__problem__ini_mon_problem
   :complies: std_req__aspice_40__SUP-9-BP1

   Each Problem shall have a unique ID. It shall be in an integer number.

.. gd_req:: Problem attribute: status
   :id: gd_req__problem__attr_status
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__problem__cr_an_problem, wf__problem__ini_mon_problem
   :complies:

   Each Problem shall have a status:

      * open
      * in review
      * in implementation
      * closed
      * rejected
      * cancelled

.. gd_req:: Problem attribute: title
   :id: gd_req__problem__attr_title
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__problem__cr_an_problem, wf__problem__ini_mon_problem
   :complies: std_req__aspice_40__SUP-9-BP1

   Reason for problem report

.. gd_req:: Problem attribute: description
   :id: gd_req__problem__attr_impact_description
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__problem__cr_an_problem, wf__problem__ini_mon_problem
   :complies: std_req__aspice_40__SUP-9-BP1

   Exact description of the Problem, including potential cause and impact of the problem.

   Record especially, if functional safety or cybersecurity may affected here.

   Record potential affected parties, and if it may requried to notify them about the potential
   problem.

.. gd_req:: Problem attribute: category
   :id: gd_req__problem__attr_category
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__problem__cr_an_problem, wf__problem__ini_mon_problem
   :complies: std_req__aspice_40__SUP-9-BP1, std_req__aspice_40__SUP-9-BP2

   Each Problem shall have a category identifier:

      * trivial
      * minor
      * major
      * critical
      * blocker

.. gd_req:: Problem attribute: classification
   :id: gd_req__problem__attr_classification
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__problem__cr_an_problem, wf__problem__ini_mon_problem
   :complies: std_req__aspice_40__SUP-9-BP1

   Each Problem shall have a classification identifier:

      * User
      * Bug
      * Quality

.. gd_req:: Problemt attribute: milestone
   :id: gd_req__problem__attr_milestone
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__problem__cr_an_problem, wf__problem__ini_mon_problem
   :complies: std_req__aspice_40__SUP-9-BP1, std_req__aspice_40__SUP-9-BP6

   Milestone until the Problem must be implemented (used for prioritization)


.. _prm_process_problem_requests_checks:

Problem Resolution Checks
'''''''''''''''''''''''''

.. gd_req:: Problem Resolution mandatory attributes provided
   :id: gd_req__problem__attr_mandatory
   :status: valid
   :tags: attribute, check
   :satisfies: wf__problem__cr_an_problem, wf__problem__ini_mon_problem
   :complies:

   It shall be checked if all mandatory attributes for each Problem
   is provided by the user. For all requirements following attributes shall be mandatory:

   .. needtable:: Overview mandatory problem attributes
      :filter: "mandatory" in tags and "attribute" in tags and type == "gd_req__problem"
      :style: table
      :columns: title
      :colwidths: 30
