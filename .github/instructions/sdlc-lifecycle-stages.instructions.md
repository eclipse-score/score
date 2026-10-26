---
description: "Use when: a user gives a new requirement, asks to create SDLC artifacts, or asks to implement a staged change."
applyTo: "**"
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright (c) 2026 Contributors to the Eclipse Foundation -->

# SDLC Lifecycle Stages

Use `.stage/ISSUE-N/` to make the decision trail for a change inspectable. Before calling `bootstrap_sdlc_issue`, check whether a `.stage/ISSUE-N/` directory already exists for this requirement; if so, resume work there instead of creating a new one. When the user supplies a new requirement, call `bootstrap_sdlc_issue` once. It creates a complete review-marked draft: requirement, specification, architecture, plan, and three tasks.

Then inspect the repository and replace every `[DRAFT]` section with evidence-based content before changing production code. The MCP server creates files; it does not contain an LLM and cannot make repository-specific design decisions itself.

Complete steps 1-4 and remove all `[DRAFT]` markers before writing any production code. Step 5 (storing implementation evidence) occurs after code changes are made, during the review preparation phase:
1. Turn the requirement into verifiable behavior in `02-specification.md`.
2. Explain system boundaries and significant technical choices in `03-architecture.md`.
3. Convert the architecture into ordered work in `04-plan.yaml` and `05-tasks/`.
4. Remove draft/review markers only after the artifacts are consistent and reviewed.
5. Store actual implementation evidence in `harness/implementation-evidence.json` before review.

## End-to-End Workflow Checklist

Follow this ordered workflow and gating conditions:
1. `bootstrap_sdlc_issue` (or resume existing `.stage/ISSUE-N/`)
2. Fill draft artifacts with evidence
3. `assess_sdlc_issue` (resolve all findings before code changes)
4. Implement changes in code
5. `record_implementation_evidence` (record test statuses and task progress)
6. `assess_implementation_progress` (verify completion)
7. `check_stage_completeness` (validate artifact presence)

Call `assess_sdlc_issue` after filling the draft artifacts. Address every finding before production changes: it detects unresolved `[DRAFT]` content, requirement dependencies such as `#179` that lack a `## Dependency analysis` section, and missing `## Repository evidence` sections. Repository evidence must name inspected files, symbols, and test targets. If a finding cannot be resolved because required evidence does not exist in the repository, document this explicitly in the artifact and flag it for human review rather than proceeding.

After each implementation task, call `record_implementation_evidence` with the task filename, requirement/need IDs, changed source files, actual test commands, test statuses, and an honest task status. If test statuses indicate failure, do not mark the task status as complete; instead mark it as blocked or in-progress and do not proceed to the next task until resolved. Call `assess_implementation_progress` before review to check completed-task percentage and unverified work. Call `write_progress_report` into the documentation source tree to publish an RST progress report.

Call `check_stage_completeness` before entering a later stage. It validates file presence only; it does not validate semantic consistency. Never treat a passing completeness check as proof that an agent followed the plan.