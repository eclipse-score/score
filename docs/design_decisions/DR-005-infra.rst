..
   Copyright (c) 2025 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-005-Infra: Hosting Strategy for Module Documentation
=======================================================

.. dec_rec:: Hosting strategy for module webspaces
   :id: dec_rec__infra__webspace
   :status: proposed
   :context: Infrastructure
   :decision: tbd

Context / Problem
-----------------

We host site content for modules using GitHub Pages (per-repo webspaces).
While this works so far, the storage and site limits are becoming noticeable.
More diagrams, pull-requests, and versions will exacerbate the problem.

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

1. Provide sufficient storage and bandwidth for released documentation and static assets.
2. Keep a consistent site/URL structure and navigation across modules.
3. Keep hosting and maintenance costs predictable and low.
4. Dedicated space for releases?

Options Considered
------------------

Option G: Continue with per-repo GitHub Pages (status quo)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Keep publishing module webspaces to GitHub Pages.
Invest efforts to keep space needs low as we only have 1GiB per repository.

😡  Effort: Increasing.


Option C: Centralized hosting under the Eclipse webspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Host module webspaces in sub-folders of https://eclipse.dev/score/
The site would be the canonical public landing page,
while modules may still publish artifact outputs to GitHub or to an internal storage bucket.

😡  Effort: Infrastructure and migration needed.

Option X: ...
^^^^^^^^^^^^^

Use an external hosting provider?
Pay GitHub for more space?


Evaluation
----------

.. csv-table::
   :header: Criteria, Option G, Option C, Option X
   :widths: 20, 10, 10, 10

   Effort, 💚, 😡, ?

decision tbd
