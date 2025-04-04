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

Concept
-------

.. doc_concept:: Documentation Management Concept
   :id: doc_concept__documentation__process
   :status: valid

In this section a concept for the documentation management will be discussed.
Inputs for this concepts are mainly the requirements of ISO26262 "Part 2: Management of functional safety"
and "Part 8: Supporting processes".

Key concept
^^^^^^^^^^^
The Documentation Management Plan should define the strategy to manage the identifed documentations
in an effective and repeatable way for the project life cycle.


Inputs
^^^^^^

#. Stakeholders for the documentation work products?
#. What tooling do we need?
#. Which guidance for the work products do we have?

Stakeholders
^^^^^^^^^^^^

#. :need:`Contributor <rl__contributor>`
#. :need:`Committer <rl__committer>`

   * contributing and approving documents

#. :need:`Technical Lead <rl__technical_lead>`

   * planning and status reporting of work products and their documentation for the platform

#. :need:`Module Lead <rl__module_lead>`

   * planning and status reporting of work products and their documentation for modules

#. :need:`Safety Manager <rl__safety_manager>`

   * wants to know when the safety related documents are ready for a release
   * wants to know who was the author and approver of a document in case of safety issues

#. :need:`Security Manager <rl__security_manager>`

   * wants to know when the security related documents are ready for a release
   * wants to know who was the author and approver of a document in case of security issues

#. :need:`Quality Manager <rl__quality_manager>`

   * wants to know when the quality related documents are ready for a release
   * wants to know who was the author and approver of a document in case of quality issues

Document Management Tooling
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the document attributes to be manually set, `sphinx-needs <https://www.sphinx-needs.com/>`_ will be used.

For the versioning and version history `github <https://github.com/>`_ is used.

For the automated attributes additional tooling is created (see :doc:`guidance/documentation_process_reqs`)


Guidance
--------

The document management guideline can be found here :need:`gd_guidl__documentation`.

Some process requirements to be automated are available here :ref:`documentation_process_requirements`.
