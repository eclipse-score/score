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

SUP.10 Change Request Management
--------------------------------

The purpose of the Change Request Management Process is to ensure that change requests are
recorded, analyzed, tracked, approved, and implemented.

Process outcomes
~~~~~~~~~~~~~~~~

1. Requests for changes are recorded and identified.
2. Change requests are analyzed, dependencies and relationships to other change requests
   are identified, and the impact is estimated.
3. Change requests are approved before implementation and prioritized accordingly.
4. Bidirectional traceability is established between change requests and affected work products.
5. Implementation of change requests is confirmed.
6. Change requests are tracked to closure and status of change requests is communicated to affected parties.

Base practices
~~~~~~~~~~~~~~

.. std_req:: SUP.10.BP1: Identify and record the change requests
   :id:std_bp__aspice-40__SUP-10-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-13-16

   The scope for application of change requests is identified.
   Each change request is uniquely identified, described, and recorded, including the initiator and reason of the change request.
   A status is assigned to each change request to facilitate tracking.

   .. note::

      Change requests may be used for changes related to e.g., product, process, methods.

   .. note::

      Example values for the change request status are “open”, “under investigation”, “implemented”, etc.

   .. note::

      The change request handling may differ across the product life cycle e.g., during prototype

.. std_req:: SUP.10.BP2: Analyze and assess change requests
   :id:std_bp__aspice-40__SUP-10-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-18-57,std_bp__aspice-40__iic-13-16

   Change requests are analyzed by relevant parties according to analysis criteria.
   Work products affected by the change request and dependencies to other change requests are determined.
   The impact of the change requests is assessed.

   .. note::

      Examples for analysis criteria are: resource requirements, scheduling issues, risks, benefits, etc.

.. std_req:: SUP.10.BP3: Approve change requests before implementation
   :id:std_bp__aspice-40__SUP-10-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-13-16

   Change requests are prioritized and approved for implementation based on analysis results and availability of resources.

   .. note::

      A Change Control Board (CCB) is an example mechanism used to approve change requests.

   .. note::

      Prioritization of change requests may be done by allocation to releases.

.. std_req:: SUP.10.BP4: Establish bidirectional traceability
   :id:std_bp__aspice-40__SUP-10-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-13-51

   Establish bidirectional traceability between change requests and work products affected by the change requests.
   In case that the change request is initiated by a problem, establish bidirectional traceability between change requests
   and the corresponding problem reports.

.. std_req:: SUP.10.BP5: Confirm the implementation of change requests
   :id:std_bp__aspice-40__SUP-10-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-13-16

   The implementation of change requests is confirmed before closure by relevant stakeholders.

.. std_req:: SUP.10.BP6: Track change requests to closure
   :id:std_bp__aspice-40__SUP-10-BP6
   :status: valid
   :links:std_bp__aspice-40__iic-13-16

   Change requests are tracked to closure. The status of change requests is communicated to all affected parties.

      .. note::

         Examples for informing affected parties can be daily standup meetings or tool-supported workflows.


