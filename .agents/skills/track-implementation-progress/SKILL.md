---
name: track-implementation-progress
description: Record implementation evidence, assess task completion, and publish implementation progress reports while implementing a staged issue
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright (c) 2026 Contributors to the Eclipse Foundation -->

# Track Implementation Progress

## Trigger

Use this skill while implementing a staged issue, after a task changes source files, runs tests, or becomes blocked.

## Workflow

1. Call `record_implementation_evidence` for the task with requirement/need IDs, changed source files, real test command outcomes, and task status. If need IDs or test results are not yet available, record the fields that are known and set the missing fields to null; do not skip the call entirely.
2. Never mark a task `completed` when its tests are blocked or failed. If a task has any failed or blocked tests alongside passing ones, mark the task status as `in_progress` and record each test result individually.
3. Call `assess_implementation_progress` before review to report task completion percentage, linked source files, need IDs, and test results.
4. Call `write_progress_report` into the documentation source directory after every `assess_implementation_progress` call, or when explicitly requested by the user.

## Evidence Format

Use exact repository-relative source paths and actual commands. Test entries contain at least `command` and `status`, where `status` is `passed`, `failed`, or `blocked`.