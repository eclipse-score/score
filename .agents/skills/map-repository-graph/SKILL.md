---
name: map-repository-graph
description: Skill for querying and exploring repository structure as a knowledge graph
---

<!--
*******************************************************************************
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
*******************************************************************************
-->

# Map Repository Graph Skill

Use this skill to understand your repository structure without exhausting context.

## Prerequisites: Graph Setup

Before using this skill, call the `apm-setup` MCP tools for the target repository:

```bash
verify_setup(repo_path)
setup_graphify(repo_path)
```

Verify that setup created `graphify-out/graph.json` before querying the graph.

## When to invoke

- Understanding what files/modules exist and how they relate
- Finding where a symbol (function, class, interface) is defined
- Tracing dependencies and call chains
- Identifying which files need to be modified for a task
- Understanding code organization and ownership

## How to use

1. **Define your query scope** (whole repo, specific directory, specific pattern?)
2. **Ask about the graph layer** you need (structure, symbols, dependencies, ownership?)
3. **Get back a map** (not source code—just relationships and metadata)
4. **Identify relevant nodes** from the map
5. **Read only what's relevant** using line-range file reads

## Example queries

```
Query scope: src/api/
Graph layer: symbols + dependencies
Question: Show me all functions in this directory and what they call
```

```
Query scope: entire repo
Graph layer: ownership
Question: What are the main module boundaries and who owns each?
```

```
Query scope: /utils/
Graph layer: structure + dependencies
Question: Map all files and show reverse dependencies (what imports these files?)
```

## What you get

- Repository structure overview (not source code)
- Symbol lists with signatures
- Dependency graphs or dependency matrices
- Ownership information
- File metadata (size, complexity metrics if available)

## Integration with Working Memory

When using context-discipline working memory:

```python
# Session starts with goal
wm.initialize_session(
    goal="Understand authentication flow",
    subgoals=["Find auth entry points", "Trace to database"],
)
# Returns {"session_id": "...", "setup": {"ok": ..., ...}}

# Query the graph via working memory
auth_nodes = wm.query_graph("All functions related to authentication")
# Returns {"query": "...", "matches": [...], "setup": {...}}
# ↓ Delegates to graphify-codegraph MCP
# ↓ Reads graphify-out/graph.json
# ↓ The matches entry contains relevant symbols + files

# Use results to guide file reads
wm.record_decision(
    decision="Read auth.py and api/login.py",
    reason=["Graph results identify the relevant files"],
)
```

## Refreshing the Graph

During development, refresh if code changes significantly:

```bash
cd /path/to/repo
rm -rf graphify-out/
graphify .
```

MCP automatically reads the new graph on next query—no restart needed.

## Pro tips

- **Narrow your scope** — Query specific directories, not everything
- **Layer by layer** — Start with structure, then dive into symbols you care about
- **Follow reverse deps** — Find what calls a function, then read those callers
- **Use ownership** — Find the maintainer of a module before making breaking changes
- **Refresh if stale** — If you find files missing, regenerate the graph

## Next step

Once you have the graph map, use targeted file reads (with line ranges) to examine only the relevant source code.
