<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright (c) 2026 Contributors to the Eclipse Foundation -->

# Detect Loopback

## Trigger

Use this skill when implementation disproves an assumption in a requirement, specification, architecture, plan, or task.

## Workflow

1. State the discovered fact in one sentence.
2. Identify the earliest lifecycle stage whose decision is invalid or incomplete. If multiple stages are invalidated, call `record_loopback` once for the earliest stage only; downstream stages will be re-evaluated after that artifact is corrected.
3. Call `record_loopback` with that stage and the affected artifact. If `record_loopback` is unavailable or returns an error, stop and notify the user before proceeding to step 4.
4. Update the artifact passed to `record_loopback` in step 3 before resuming any work that depends on it.
5. Record fresh test evidence after the corrective change.