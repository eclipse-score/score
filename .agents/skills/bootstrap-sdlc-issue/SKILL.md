<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright (c) 2026 Contributors to the Eclipse Foundation -->

# Bootstrap SDLC Issue

## Trigger

Use this skill when the user provides a new requirement and wants the complete SDLC record created from that single input.

## Workflow

1. Derive a concise issue ID and title from the user request.
2. Call `bootstrap_sdlc_issue` once with the issue ID, title, and requirement text.
3. Read the generated artifacts and inspect the repository before replacing any `[DRAFT]` content.
4. Update specification, architecture, plan, and tasks with repository-grounded decisions.
5. Do not write `harness/implementation-evidence.json` until real implementation tests have run.

## Important

MCP tools execute local code; they do not run instruction files or invoke an LLM. This skill must be installed or compiled into the active agent context. A direct `.vscode/mcp.json` server registration makes the tools available but does not automatically load this workflow guidance.