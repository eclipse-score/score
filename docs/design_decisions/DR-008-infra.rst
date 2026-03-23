..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-008-Infra: Docs Modularity
================================================================

.. dec_rec:: Modularize docs
   :id: dec_rec__infra__docs_modularity
   :status: proposed
   :context: Infrastructure
   :decision: tbd

Context / Problem
-----------------

There is a proof-of-concept for an alternative documentation build concept introduced in
`tooling PR 95 <https://github.com/eclipse-score/tooling/pull/95>`_.
It improves the modularity of documentation but drops features of the existing documentation concept.

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

- **Implementation Effort**: Don't spend much one-time effort to implement the change proposed here.
- **Maintenance Effort**: Don't spend much ongoing effort due to increased complexity.
- **Ease of use**: Developers don't like working on documentation, so we should make it easy on them.

Options Considered
------------------

Option S: Single docs() only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We keep the current docs-as-code concept and drop the PoC proposal.

Implementation Effort 💚 No additional effort.

Maintenance Effort 🤔 unclear in relation to PoC.

Ease of use 💚 No change for developers.

Option M: Module API - Many Bazel targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We drop the current approach and switch to the PoC approach.

Implementation Effort 😡 Requires restructuring all documentation.

Maintenance Effort 🤔 unclear

Ease of use 😡 Requires developers to adapt to new workflow. No VSCode LSP integration.

Option C: Combine the Best of Both
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We integrated the advantages of the PoC into the existing solution maintaining all benefits.

Implementation Effort 😡 Certainly the most effort

Maintenance Effort 😡 Certainly the most effort

Ease of use 💚 No mandatory change for developers at first but extensions?

Evaluation
----------

Here is the summary, how well each option achieves the goals in order of goal importance:

.. csv-table::
   :header: Goals, Option S, Option M, Option C
   :widths: 15, 10, 10, 10

   Implementation Effort,      💚, 😡, 😡
   Maintenance Effort,         🤔, 🤔, 😡
   Ease of use,                💚, 😡, 💚

**Decision:** Option S has no downsides while the alternatives do.
