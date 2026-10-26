---
name: authoring-workflow
description: Workflow for authoring and changing S-CORE artifacts against the normative metamodel
applyTo: "**/*.rst"
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright (c) 2026 Contributors to the Eclipse Foundation -->

# S-CORE Authoring Workflow

After calling `initialize_session`, the first authoring step when changing an
S-CORE artifact is to identify its normative need type, options, links, and
graph constraints. The metamodel projection is normative; this workflow
guidance is not.

Do not invent need types or options. If the model does not express a required
concept, update the upstream metamodel through its normal review process before
authoring the artifact.
