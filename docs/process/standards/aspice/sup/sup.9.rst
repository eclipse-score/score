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

SUP.9 Problem Resolution Management
-----------------------------------

The purpose of the Problem Resolution Management Process is to ensure that problems are identified,
recorded, analyzed, and their resolution is managed and controlled.

Process outcomes
~~~~~~~~~~~~~~~~

1. Problems are uniquely identified, recorded and classified.
2. Problems are analyzed and assessed to determine an appropriate solution.
3. Problem resolution is initiated.
4. Problems are tracked to closure.
5. The status of problems including trends identified are reported to stakeholders.

Base practices
~~~~~~~~~~~~~~

.. std_req:: SUP.9.BP1: Identify and record the problem
   :id:std_bp__aspice-40__SUP-9-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-13-07

   Each problem is uniquely identified, described and recorded.
   A status is assigned to each problem to facilitate tracking.
   Supporting information is provided to reproduce and diagnose the problem.

   .. note::

      Problems may relate to e.g., product, resources, or methods.

   .. note::
      Example values for the problem status are “new”, “solved”, “closed”, etc.

   .. note::
      Supporting information may include e.g, the origin of the problem, how it can be reproduced, environmental information, by whom it has been detected.

   .. note::

      Unique identification supports traceability to changes made as needed by the change request management process (SUP.10).

.. std_req:: SUP.9.BP2: Determine the cause and the impact of the problem
   :id:std_bp__aspice-40__SUP-9-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-13-07,std_bp__aspice-40__iic-15-55

   Analyze the problem, determine its cause, including common causes if existing, and impact.
   Involve relevant parties. Categorize the problem.

   .. note::

      Problem categorization (e.g., light, medium, severe) may be based on severity, criticality, urgency, etc.

.. std_req:: SUP.9.BP3: Authorize urgent resolution action
   :id:std_bp__aspice-40__SUP-9-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-13-07

   Obtain authorization for immediate action if a problem requires an urgent resolution according to the categorization.

.. std_req:: SUP.9.BP4: Raise alert notifications
   :id:std_bp__aspice-40__SUP-9-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-13-07

   If according to the categorization the problem has a high impact on other systems or
   other affected parties, an alert notification needs to be raised accordingly.

.. std_req:: SUP.9.BP5: Initiate problem resolution
   :id:std_bp__aspice-40__SUP-9-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-13-07

   Initiate appropriate actions according to the categorization to resolve the problem long-term,
   including review of those actions or initiate a change request.
   This includes synchronization and consistency with short-term urgent resolution actions, if applicable.

.. std_req:: SUP.9.BP6: Track problems to closure
   :id:std_bp__aspice-40__SUP-9-BP6
   :status: valid
   :links:std_bp__aspice-40__iic-13-07,std_bp__aspice-40__iic-15-12

   Track the status of problems to closure including all related change requests.
   The closure of problems is accepted by relevant stakeholders.

.. std_req:: SUP.9.BP7: Report the status of problem resolution activities
   :id:std_bp__aspice-40__SUP-9-BP7
   :status: valid
   :links:std_bp__aspice-40__iic-15-12

   Collect and analyze problem resolution management data, identify trends, and initiate related actions.
   Regularly report the results of data analysis, the identified trends and the status of problem resolution
   activities to relevant stakeholders.

   .. note::

      Collected data may contain information about where the problems occurred,
      how and when they were found, what their impacts were, etc.


