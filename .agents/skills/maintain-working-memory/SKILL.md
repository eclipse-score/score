---
name: maintain-working-memory
description: Use context-discipline MCP tools to track goals, assumptions, and decisions during agentic sessions
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

# Maintain Working Memory Skill

Use the `context-discipline` MCP tools to track your session explicitly without custom YAML maintenance.

Simple, self-contained implementation. Works standalone. Session records and
durable context overlays are stored locally.

## When to invoke

- **Starting a session** — Initialize working memory with goals
- **After tool calls** — Record compressed findings (1-2 sentences)
- **Before major decisions** — Check unverified assumptions and stale artifacts
- **When making decisions** — Record with reversibility tracking
- **Regularly** — Update plan and coverage as you learn

## How to use

### Setup: Initialize working memory

```python
wm.initialize_session(
    goal="Refactor auth module to async",
    subgoals=[
        "Identify all auth functions",
        "Map dependencies on sync calls",
        "Implement async versions",
        "Update call sites",
    ],
    assumptions=["auth.py is the only auth module"],
)
# Returns {"session_id": "...", "setup": {"ok": ..., ...}}
```

### Record compressed findings

```python
# After each tool call, record (COMPRESS to 1-2 sentences)
graph_result = wm.query_graph("All functions in lib/auth.py")
# Returns {"query": "...", "matches": [...], "setup": {...}}
```

### Track assumptions

```python
# Add assumptions (especially ones to verify)
wm.initialize_session(
    goal="Track assumptions",
    subgoals=[],
    assumptions={
        "auth.py is only auth module": "high",
        "No external code imports auth": "medium",
    },
)

# Before risky decisions, check for unverified ones
unverified = wm.get_unverified_assumptions()
if unverified:
    print(f"WARNING: {len(unverified)} unverified assumptions")
    for a in unverified:
        if a.confidence in ["low", "medium"]:
            print(
                f"  - {a.key} (confidence: {a.confidence}) - VERIFY BEFORE PROCEEDING"
            )
```

### Record decisions

```python
# Document what you decide and why (with reversibility)
decision_result = wm.record_decision(
    decision="Implement async in auth.py first, then update callers",
    reason=[
        "Minimizes risk of partial refactoring",
        "Only 3 call sites to update",
        "Can test refactored functions independently",
    ],
    reversible=True,
    grounded_nodes=["auth.py", "auth_module"],
)
# Returns {"unresolved_nodes": []}
# Grounded nodes accept repo-relative source paths or canonical graph node IDs.
# Non-empty unresolved_nodes entries do not contribute to retrieval; restate
# them as real paths or graph IDs.
```

### Update progress

```python
# After each major step, update your plan
wm.record_outcome(
    task="Map all call sites of authenticate()",
    verdict="pass",
    coverage=0.35,
    surfaced_nodes=["authenticate"],
    missing_nodes=[],
)
```

### Review before major decisions

```python
# Get current state
state = wm.get_working_memory()
print(f"Entries: {len(state)}")

# Check for potential issues
unverified = wm.get_unverified_assumptions()

if unverified:
    print(f"WARNING: {len(unverified)} unverified assumptions")
```

## Current API

The six MCP tools are the complete current API: `initialize_session`,
`query_graph`, `record_decision`, `record_outcome`, `get_working_memory`, and
`get_unverified_assumptions`. Working memory is held for the running server
session; collaboration records are persisted to `.score-local/sessions.jsonl`.

## Automatic Benefits

- ✅ **Zero custom guardrail code** — Reuses tested infrastructure
- ✅ **Immutable audit trail** — JSONL append-only logs
- ✅ **Fast queries** — O(1) lookups via session index
- ✅ **Importance/coverage filtering** — Automatic signal vs. noise detection
- ✅ **No maintenance burden** — Simple Python class, no YAML to maintain
- ✅ **Intersession retrieval** — Reuses relevant reasoning from prior sessions
