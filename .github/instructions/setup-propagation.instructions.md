---
name: setup-propagation
description: Use the setup MCP server to initialize local APM package state
applyTo: "**"
---

<!--
*******************************************************************************
Copyright (c) 2026 Contributors to the Eclipse Foundation

SPDX-License-Identifier: Apache-2.0
*******************************************************************************
-->

# APM Setup Propagation

Use the `apm-setup` MCP tools explicitly when a repository needs local package
state.

- Call `verify_setup` before setup when status is unknown.
- Call `setup_graphify` before the first graph query when the graph is missing.
- Call `setup_context_discipline` before recording local observations.
- Run setup again after major repository changes when generated state is stale.

Installing the package registers its declared MCP server for the selected
target; installation still does not run setup tools. Setup operations are
repository-local and must be explicitly requested through the MCP tools.
