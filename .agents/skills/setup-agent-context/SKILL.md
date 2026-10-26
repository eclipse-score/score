---
name: setup-agent-context
description: Initialize local graph and working-memory state for APM packages
---

<!--
*******************************************************************************
Copyright (c) 2026 Contributors to the Eclipse Foundation

SPDX-License-Identifier: Apache-2.0
*******************************************************************************
-->

# Setup Agent Context

Use the registered `apm-setup` MCP server for all setup actions.

Before using graph or working-memory tools:

1. Call `verify_setup` for the target repository.
2. Call `setup_graphify` if `graphify-out/graph.json` is missing or stale.
3. Call `setup_context_discipline` if `.score-local/` is missing.
4. Continue only after setup reports success.

Do not assume that `apm install` or `apm compile` generated repository state.
