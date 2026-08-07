..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-009-Infra: AI Agent Context Packaging Tooling Selection
==========================================================

- **Date:** 2026-07-31
- **Issue:** `#3115 <https://github.com/eclipse-score/score/issues/3115>`_

.. dec_rec:: AI Agent Context Packaging Tooling Selection
   :id: dec_rec__infra__ai_packaging_tooling
   :status: proposed
   :version: 1
   :context: Infrastructure
   :decision: APM is the primary AI agent context packaging tool; Lola is the fallback; OKIT is not recommended

Context / Problem
-----------------

S-CORE contributors use multiple AI coding assistants (GitHub Copilot, Claude Code, Cursor, etc.).
Agent context — skills, instructions, prompts, MCP server references — is today copy-pasted per
repository and per tool, unversioned and unaudited.

A packaging layer is needed that:

- Distributes agent context declaratively and reproducibly across all contributors regardless of IDE.
- Provides supply-chain controls (lockfile integrity, SBOM, policy allow-lists) consistent with
  S-CORE's existing ``sbom-tool`` and safety-oriented process.
- Integrates with CI as a merge gate (audit, drift detection).

Visual Overview
~~~~~~~~~~~~~~~

.. mermaid::

   flowchart LR
       subgraph Sources["Package Sources (git / marketplace)"]
           R1[eclipse-score/mcp-servers]
           R2[eclipse-score/tooling]
           R3[community skills repos]
       end

       subgraph PM["Package Manager (one of three)"]
           APM["APM\napm.yml + apm.lock.yaml\npolicy · SBOM · hashes"]
           Lola["Lola\n.lola-req\nno lockfile hashes"]
           OKIT["OKIT\nflat copy\nno versioning"]
       end

       subgraph Out["Per-Contributor Output"]
           C1[".github/copilot-instructions.md"]
           C2["CLAUDE.md"]
           C3[".cursor/rules"]
           C4["...other IDE configs"]
       end

       Sources --> APM
       Sources --> Lola
       Sources --> OKIT
       APM --> Out
       Lola --> Out
       OKIT --> Out

Options Considered
------------------

APM — ``microsoft/apm``
~~~~~~~~~~~~~~~~~~~~~~~

Manifest + lockfile package manager for AI agent context (instructions, skills, prompts, hooks,
plugins, MCP servers) across 8 coding assistants. Uses ``apm.yml`` manifest and ``apm.lock.yaml``
lockfile with content hashes.

**Pros:**

- Policy engine (``apm-policy.yml``): org-level allow-lists, tighten-only inheritance, CI audit gates.
- Lockfile with content hashes; ``apm.lock export --format cyclonedx|spdx`` SBOM export.
- Content-security scanning (hidden-Unicode / prompt-injection detection on install).
- Broadest agent coverage: 8 assistants (Copilot, Claude Code, Cursor, OpenCode, Codex, Gemini, Windsurf, Kiro).
- Drift detection; active Microsoft-org project (3.3k stars, 71 releases).
- Directly complements ``eclipse-score/mcp-servers`` and ``sbom-tool``.

**Cons:**

- Newest governance/policy features are the least battle-tested part of the tool.
- Single-vendor stewardship (Microsoft) even though built on open standards.
- Adds a new onboarding step for contributors.

Lola — ``LobsterTrap/lola``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lighter, community-governed AI skill/context package manager (Go+Python) with marketplace-based
distribution. Declarative ``.lola-req`` file (pip-requirements style).

**Pros:**

- Simpler mental model; lower adoption barrier.
- Vendor-neutral governance (GOVERNANCE.md, OpenSSF Best Practices badge).
- Covers 6 assistants (Claude Code, Copilot CLI, Copilot VS Code, Cursor, Gemini CLI, OpenCode).

**Cons:**

- No lockfile content-hash integrity, no policy enforcement, no SBOM, no content-security scanning.
- Narrower agent coverage than APM (6 vs. 8).
- Smaller community (109 stars, 8 releases); missing enterprise governance features.

OKIT — ``Mumme-IT/okit``
~~~~~~~~~~~~~~~~~~~~~~~~

Minimal, dependency-free (stdlib-only) Python CLI: clones a repo, copies ``skills/`` and ``agents/``
files into whichever tool directories are detected on ``PATH``.

**Pros:**

- Zero dependencies; trivially auditable codebase.
- Very low learning curve (three commands).

**Cons:**

- No dependency resolution, versioning, lockfile, policy enforcement, or content-security scanning.
- Single contributor (1 star, 1 fork, 40 commits, no releases); bus factor of one.
- Not defensible as shared infrastructure for a multi-org Eclipse project.

Conclusion
----------

**Primary: APM.** It is the only candidate with an actual governance and supply-chain-security
model (policy enforcement, lockfile integrity hashes, SBOM export, drift detection, content-security
scanning) — essential when agent context is executable-in-effect and S-CORE is a safety-relevant
open-source project accepting third-party contributions.

**Fallback: Lola.** Kept on the radar as a lighter-weight, vendor-neutral alternative if APM's
Microsoft stewardship or scope becomes a concern for Eclipse Foundation governance.

**Not recommended: OKIT.** Pre-production maturity (bus factor 1, no governance). Revisit if the
project matures significantly.

.. list-table::
   :header-rows: 1
   :widths: 10 15 30

   * - Tool
     - S-CORE Fit
     - Recommendation
   * - APM
     - High
     - **USE** — primary packaging tool
   * - Lola
     - Medium
     - **WATCH** — fallback only
   * - OKIT
     - Low
     - **DO NOT USE** at this maturity

.. note::

   Status remains **proposed** until a proof-of-concept pilot validates integration with
   S-CORE's Bazel/Sphinx/sphinx-needs infrastructure and CI pipeline.
