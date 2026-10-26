---
description: "Use when: implementation exposes a missing requirement, ambiguous specification, or invalid architecture decision."
applyTo: "**/.stage/**"
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright (c) 2026 Contributors to the Eclipse Foundation -->

# Loopback Detection

Implementation can reveal missing constraints, ambiguous acceptance criteria, or an architecture that cannot meet a stated requirement. Treat these as lifecycle loopbacks rather than patching around them.

Call `record_loopback` with the discovery, the earliest stage that must be reconsidered, and the affected artifact. The tool appends a durable log entry and adds a review marker to an existing affected file. Update that stage artifact and then rerun the applicable implementation evidence.