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

Document Management Process Requirements
========================================

.. gd_req:: Document Management Process Requirement 1
   :id: gd_req__doc_author
   :status: valid
   :complies: std_req__iso26262__support_43

   Documents headers shall contain an "author" attribute, which is added during documentation build
   and contains the last PRs committer of the file containing the document.

.. gd_req:: Document Management Process Requirement 2
   :id: gd_req__doc_approver
   :status: valid
   :complies: std_req__iso26262__support_43

   Documents headers shall contain an "approver" attribute, which is added during documentation build
   and contains the last PRs CODEOWNER reviewer of the file containing the document.

.. gd_req:: Document Management Process Requirement 3
   :id: gd_req__doc_reviewer
   :status: valid
   :complies: std_req__iso26262__support_41

   Documents headers shall contain "reviewer" attribute, which is added during documentation build
   and contains the last PRs reviewers of the file containing the document, which were not covered by
   :need:`gd_req__doc_approver`.
