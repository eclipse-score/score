---
name: context-compression
description: Guidelines for compressing and summarizing information before returning to context
applyTo: "**"
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

# Context Compression Guidelines

Every tool output risks exhausting your context window. Compress before re-inserting.

## The Rule

**Never paste raw tool output into working memory.**

Always: Query → Compress → Summarize → Re-insert compressed summary

## Compression patterns by tool type

### File reads

```
BEFORE (raw output):
[200 lines of source code]

AFTER (compressed):
- File: lib/auth.py (lines 50-75)
- Purpose: authenticate() function
- Key finding: Uses synchronous time.sleep() for backoff; needs async conversion
- Related: Called by api/handlers.py:87, cli/commands.py:42
- Status: Ready for refactoring
```

### Graph queries

```
BEFORE (raw output):
[Large dependency matrix with 50+ files]

AFTER (compressed):
- Scope: src/api/ directory
- 12 files total
- Internal dependencies: handlers.py → services.py → models.py (clean chain)
- External imports: 3 files import external libraries
- Ownership: team/backend owns all
- Key insight: Single dependency chain, no circular deps
```

### API/docs queries

```
BEFORE (raw output):
[10 pages of FastAPI documentation]

AFTER (compressed):
- Query: FastAPI dependency injection pattern
- Key: Use Depends() function to inject dependencies
- Signature: async def handler(db: Session = Depends(get_db))
- Example: [minimal working example, 5 lines max]
- Note: Dependency is evaluated per-request
- Version: FastAPI 0.104+
```

### Error messages

```
BEFORE (raw output):
[Full stack trace with 20+ frames]

AFTER (compressed):
- Error: TypeError: cannot index into None type
- Location: models.py:42 in User.get_email()
- Cause: user.profile can be None; code assumes it's always set
- Context: Happens when user record incomplete
- Fix strategy: Add defensive check or update schema requirement
```

## Compression checklist

- [ ] **Removed noise** — Eliminated irrelevant details, boilerplate, examples I don't need
- [ ] **Extracted signal** — Pulled out 3-5 key facts that matter for the task
- [ ] **Noted the source** — Can I reference the original if the model needs full details?
- [ ] **Fit in 3-4 lines** — Can I state this compressed finding in 3-4 bullets?
- [ ] **Actionable** — Does this compression give me enough info to proceed?

## When to break the rule

You can include more detail if:

1. The information is **highly relevant** to an immediate decision
2. The **model has context budget** available
3. The information is **impossible to summarize further** without losing essential meaning
4. You're in an **early exploration phase** (before you've narrowed scope)

Even then: compress 50% and provide a reference link/path to full details.

## Update compressed findings as you learn

```yaml
findings:
  from_tools:
    - tool: file-read
      query: "lib/auth.py:50-75"
      result: "authenticate() uses sync time.sleep(); needs async conversion"
      timestamp: "2026-08-13T10:40:00Z"
    # Later, you read related code:
    - tool: file-read
      query: "cli/commands.py:42 (caller of authenticate)"
      result: "CLI also uses sync auth; async conversion requires new CLI event loop"
      timestamp: "2026-08-13T10:50:00Z"
      dependency: "Blocks authenticate() conversion; must handle together"
```

Track dependencies between compressed findings. This prevents forgotten blockers.
