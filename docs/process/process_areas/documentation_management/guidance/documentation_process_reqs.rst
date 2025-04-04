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

.. _documentation_process_requirements:

Document Management Process Requirements
========================================

.. gd_req:: Document Author
   :id: gd_req__doc_author
   :status: valid
   :complies: std_req__iso26262__support_1045

   Documents headers shall contain an "author" attribute. Every committer who adds more than 50%
   of the content shall put his name.

   Note: In the future this may also be automated based on an analysis of content during the
   documentation build for every commit of the file containing the document.

.. gd_req:: Document Approver
   :id: gd_req__doc_approver
   :status: valid
   :complies: std_req__iso26262__support_1045

   Documents headers shall contain an "approver" attribute, which is added during documentation build
   and contains the last PR CODEOWNER reviewer of the file containing the document.

.. gd_req:: Document Reviewer
   :id: gd_req__doc_reviewer
   :status: valid
   :complies: std_req__iso26262__support_1043

   Documents headers shall contain "reviewer" attribute, which is added during documentation build
   and contains the last PR reviewers of the file containing the document, which were not covered by
   :need:`gd_req__doc_approver`.
