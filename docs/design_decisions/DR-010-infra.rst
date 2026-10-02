..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-010-Infra: AI SDLC / SpecKit Tooling Evaluation for Eclipse S-CORE
======================================================================

- **Issue:** `#3115 <https://github.com/eclipse-score/score/issues/3115>`_ — Evaluate AI SDLC / SpecKit Tooling
- **Date:** 2026-07-31

.. dec_rec:: AI SDLC / SpecKit Tooling Evaluation
   :id: dec_rec__infra__ai_sdlc_tooling
   :status: proposed
   :version: 1
   :context: Infrastructure
   :decision: Do not adopt any evaluated framework wholesale; build an S-CORE-owned harness based on SpecKit + Sphinx-Needs traceability

**Decision driver:** Can a tool create a traceable chain from
**Requirements → Specifications → ADRs → Code → Tests → Documentation**
while enabling AI agents to participate in a **governed, reproducible, ASPICE-compatible** workflow?

1. Evaluation Method
--------------------

Each framework was evaluated against ten categories:

1. Requirements Engineering
2. Specification Management
3. Traceability
4. AI Agent Support
5. Governance
6. Reproducibility
7. Open Source Sustainability
8. S-CORE Integration
9. ASPICE Alignment
10. Long-Term Maintainability

**Scoring scale:**

.. list-table::
   :header-rows: 1
   :widths: 10 30

   * - Score
     - Meaning
   * - 1
     - Poor
   * - 2
     - Limited
   * - 3
     - Acceptable
   * - 4
     - Strong
   * - 5
     - Excellent

Evaluation prioritized **enterprise-scale collaborative engineering** and **compliance evidence**
over individual developer productivity. Evidence was drawn from each project's source repository
(README, license, package metadata, configuration) rather than marketing claims.

**Tools evaluated:**

.. list-table::
   :header-rows: 1
   :widths: 20 50

   * - Tool
     - Source
   * - Syspilot
     - https://github.com/enthali/syspilot
   * - BMAD Method
     - https://github.com/bmad-code-org/BMAD-METHOD
   * - SpecKit
     - https://github.com/github/spec-kit · https://speckit.org
   * - Pharaoh
     - https://github.com/useblocks/pharaoh-skills

2. Executive Summary
--------------------

**No single tool fully satisfies the S-CORE decision criterion.**
The strongest capabilities are distributed across the four frameworks:

- **SpecKit** provides the strongest structured **specification-first workflow** and the best open-source sustainability.
- **Syspilot** provides **AI-assisted Sphinx-Needs traceability** and focused change-impact context.
- **Pharaoh** provides the strongest **requirements-centric, ASPICE-aligned concepts** — but the repository is **archived**.
- **BMAD Method** provides broad **agent collaboration and agile workflows**, but is not traceability- or ASPICE-first.

Therefore, an **adaptation strategy** (combine strengths, own the governance in S-CORE) is preferred
over direct adoption of any single framework.

3. Why S-CORE Cannot Adopt One Tool Directly
--------------------------------------------

None of the evaluated frameworks fully satisfy all S-CORE requirements.
The strongest capabilities are distributed:

- **SpecKit** provides structured specification workflows, but no native Sphinx-Needs / ADR / ASPICE semantics.
- **Syspilot** provides AI-assisted traceability, but is an early research project bound to Copilot + Jarvis.
- **Pharaoh** provides the strongest requirements-centric, safety-aligned concepts, but its repository is archived and read-only.
- **BMAD** provides agent collaboration workflows, but lacks a traceability-first artifact model.

Because the required capabilities — specification workflow, traceability, ASPICE evidence, and
long-term maintainability — are **not present together in any one tool**, an adaptation strategy
is preferred over direct adoption.

4. Tool-by-Tool Analysis
------------------------

4.1 Syspilot
~~~~~~~~~~~~

Syspilot is built directly on **Sphinx-Needs**, making it the most naturally aligned with
S-CORE's documentation stack. Its core idea is strong: AI agents follow **deterministic requirement
links** rather than searching the whole repository probabilistically
("the map, not the flashlight").

**Strengths**

- Native Sphinx-Needs orientation.
- Strong traceability mindset: user story → requirements → design specs.
- Change-impact analysis producing focused AI context (``O(affected)``, not ``O(total)``).
- Manager/engineer agent roles cover PM, change management, quality, design, implementation,
  UAT, verification, documentation, MECE, trace, and release.

**Weaknesses**

- README explicitly labels it an **early research project** with possible breaking changes.
- Hard dependency on VS Code, GitHub Copilot, and the ``enthali.jarvis-core`` extension
  for multi-agent orchestration.
- Governance/reproducibility are promising but not yet enterprise-hardened.

**S-CORE view:** Good **pilot candidate** for the traceability layer; not mature enough
to be the sole adopted framework.

4.2 BMAD Method
~~~~~~~~~~~~~~~

BMAD is a broad AI-assisted agile development framework, rich in agents and workflows across
brainstorming, PRDs, architecture, UX, development, and testing. It is more about
**AI collaboration patterns** than regulated engineering evidence.

**Strengths**

- Mature open-source packaging (npm ``bmad-method`` v6.10.0), MIT license, active ecosystem.
- Large workflow surface (34+ workflows) and role-based agents.
- Strong CI-friendly tooling (lint, tests, validation scripts) and non-interactive install for CI/CD.
- Useful for product/architecture ideation and implementation support.

**Weaknesses**

- Not Sphinx-Needs native; not ASPICE native.
- Traceability is not the central artifact model.
- Requirement → design → code → test linkage is not provable without extra tooling.

**S-CORE view:** **Not recommended** as the core SDLC governance tool. Keep optional for
facilitation/ideation.

4.3 SpecKit
~~~~~~~~~~~

SpecKit is the strongest candidate for a **governed specification-first workflow**:
``constitution → specify → plan → tasks → analyze → implement``, with a CLI, templates,
presets, extensions, and project-local overrides.

**Strengths**

- Specification generation is the **core concept**; specs become versioned repo artifacts.
- Strong governance primitives: constitution, templates, checklists, phase gates.
- Good reproducibility via templates, deterministic commands, and CLI-managed structure.
- MIT license (GitHub, Inc.), broad agent support (30+), reducing vendor lock-in.
- Security-conscious build posture (ruff subprocess-shell lint locks).

**Weaknesses**

- Not built for Sphinx, Sphinx-Needs, Bazel, ADRs, or ASPICE.
- Traceability is workflow-level, not automatically ASPICE-grade.
- Requirement IDs, Sphinx-Needs links, ADR links, and test evidence require
  S-CORE-specific templates/extensions.

**S-CORE view:** **Best foundation** for the specification + AI workflow layer, if extended
with S-CORE templates and Sphinx-Needs integration.

4.4 Pharaoh
~~~~~~~~~~~

Pharaoh is conceptually the closest match to S-CORE's needs. Built for Sphinx-Needs projects,
it offers a full V-model skill chain: requirement/architecture/test/FMEA drafting and review,
traceability, MECE, change impact, codelinks, lifecycle checks, standard conformance, decisions,
quality gates, and reproducibility checks.

**Strengths**

- Strongest Sphinx-Needs alignment and traceability model.
- Explicit ASPICE 4.0 / ISO 26262-8 §6 / ISO/SAE 21434 conformance concepts.
- Advisory vs **enforcing** mode via ``pharaoh.toml``, with required-link rules and codelink support.
- Review metadata (``:reviewer:``, ``:approved_by:``), lifecycle/status gates, and
  reproducibility diff checks.

**Weaknesses**

- **The repository is archived (read-only since 2026-07-28) and no longer maintained** —
  verified directly on GitHub.
- Functionality has moved to commercial-adjacent **ubCode / ubTrace** (stated free for
  open-source), which changes the governance/adoption profile.
- "The AI is the runtime" — flexible, but harder to certify/stabilize.

**S-CORE view:** **Best reference design, risky direct adoption.**
Reuse its concepts; do not depend on the archived repo.

.. note::

   **Verified evidence:** ``useblocks/pharaoh-skills`` shows "This repository was archived by
   the owner on Jul 28, 2026. It is now read-only." (24 stars, 3 contributors, latest release
   v1.2.1). Skills are stated to have moved into ubCode and ubTrace.

5. Scoring Matrix
-----------------

Scores: 1 = Poor, 2 = Limited, 3 = Acceptable, 4 = Strong, 5 = Excellent.

.. list-table::
   :header-rows: 1
   :widths: 35 15 10 15 15

   * - Category
     - Syspilot
     - BMAD
     - SpecKit
     - Pharaoh
   * - Requirements Engineering
     - 4
     - 3
     - 4
     - 5
   * - Specification Management
     - 3
     - 3
     - 5
     - 4
   * - Traceability
     - 5
     - 2
     - 3
     - 5
   * - AI Agent Support
     - 4
     - 5
     - 4
     - 4
   * - Governance
     - 3
     - 3
     - 4
     - 4
   * - Reproducibility
     - 3
     - 2
     - 4
     - 4
   * - Open Source Sustainability
     - 2
     - 4
     - 5
     - 2
   * - S-CORE Integration
     - 5
     - 2
     - 3
     - 5
   * - ASPICE Alignment
     - 3
     - 2
     - 3
     - 5
   * - Long-Term Maintainability
     - 2
     - 4
     - 5
     - 2
   * - **Total**
     - **34**
     - **30**
     - **40**
     - **40**

**Interpretation:** SpecKit and Pharaoh tie numerically for different reasons — SpecKit is
maintainable and workflow-ready; Pharaoh is domain-aligned but archived. For the ADR, that
qualitative difference matters more than the raw total.

6. ASPICE Impact Assessment
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 15 15 15 15

   * - ASPICE Area
     - Syspilot
     - BMAD
     - SpecKit
     - Pharaoh
   * - SYS.1 Requirements elicitation
     - Medium
     - Medium
     - Medium/High
     - High
   * - SYS.2 System requirements
     - High
     - Low/Medium
     - Medium
     - High
   * - SYS.3 System architecture
     - Medium
     - Medium/High
     - Medium
     - High
   * - SWE.1 Software requirements
     - High
     - Low/Medium
     - Medium
     - High
   * - SWE.2 Software architecture
     - Medium
     - Medium/High
     - Medium
     - High
   * - SWE.3 Detailed design / unit construction
     - Medium
     - Medium
     - Medium
     - Medium/High
   * - SWE.4 Unit verification
     - Medium
     - Medium
     - Medium
     - High (if linked to needs/tests)
   * - SWE.5 Integration testing
     - Medium
     - Medium
     - Medium
     - Medium/High
   * - SWE.6 Qualification testing
     - Medium
     - Low/Medium
     - Medium
     - High

**Key point:** ASPICE alignment depends on **traceability evidence**, not just generated
documents. Pharaoh and Syspilot are closest because they start from Sphinx-Needs trace links.
SpecKit can support ASPICE only after S-CORE adds requirement IDs, link rules, review states,
approval metadata, and documentation-pipeline integration.

7. Integration Architecture
---------------------------

7.1 Workflow (data flow)
~~~~~~~~~~~~~~~~~~~~~~~~

.. mermaid::

   flowchart LR
       A[Sphinx-Needs Requirements] --> B[SpecKit Specification Layer]
       B --> C[Architecture / ADR Generation]
       C --> D[Implementation Tasks]
       D --> E[Code + Bazel Build]
       E --> F[Tests + CI Evidence]
       F --> G[Sphinx Documentation]
       G --> A

       A --> H[Traceability / Impact Analysis]
       C --> H
       D --> H
       E --> H
       F --> H

7.2 Target State (conceptual stack)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   +--------------------------------+
   | AI Agents                      |
   +--------------------------------+
   | SpecKit Workflow Layer         |
   +--------------------------------+
   | ADRs + Sphinx-Needs            |
   +--------------------------------+
   | Code + Bazel + CI/CD           |
   +--------------------------------+
   | S-CORE Repository              |
   +--------------------------------+

7.3 Capability Mapping
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 50

   * - S-CORE Need
     - Recommended Tooling Role
   * - Requirements as managed artifacts
     - Sphinx-Needs + Syspilot/Pharaoh-style skills
   * - Specification workflow
     - SpecKit
   * - ADR generation
     - S-CORE SpecKit extension or Pharaoh-style decision skill
   * - Traceability graph
     - Sphinx-Needs + codelinks / ``needs.json`` validation
   * - AI agent governance
     - Versioned prompts/templates in Git
   * - Reproducibility
     - SpecKit CLI/templates + CI validation
   * - ASPICE evidence
     - Sphinx-Needs reports, CI checks, review metadata
   * - Documentation output
     - Sphinx build pipeline

8. Risks and Mitigations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 15 45

   * - Risk
     - Impact
     - Mitigation
   * - Pharaoh repo archived (verified 2026-07-28)
     - High
     - Do not adopt directly; reuse concepts or evaluate ubCode/ubTrace separately
   * - Syspilot early research status
     - High
     - Pilot only; do not make it mandatory infrastructure
   * - SpecKit lacks ASPICE/Sphinx-Needs model
     - Medium
     - Build S-CORE templates/extensions for ASPICE work products
   * - BMAD lacks traceability core
     - Medium
     - Use only for facilitation, not compliance evidence
   * - AI output nondeterminism
     - High
     - Version prompts, templates, model settings, inputs, and generated outputs
   * - Weak auditability
     - High
     - Store all artifacts in Git; require review states and trace links
   * - Vendor/tool lock-in
     - Medium
     - Prefer repo-native Markdown/RST/YAML over IDE-only state

9. Recommendation
-----------------

Adopt a **S-CORE-owned AI SDLC harness** based on **SpecKit + Sphinx-Needs traceability**,
rather than adopting Syspilot, BMAD, SpecKit, or Pharaoh wholesale.

- **SpecKit — Adopt/adapt** as the base specification-driven workflow.
- **Syspilot — Pilot/adapt** for Sphinx-Needs traceability and focused AI context.
- **Pharaoh — Reference design only** (repo archived); reassess ubCode/ubTrace separately.
- **BMAD — Optional** for early ideation/planning where no compliance evidence is required.

10. Decision
------------

**Do not adopt any evaluated framework as mandatory S-CORE infrastructure.** Instead:

1. **Prototype SpecKit-based specification workflows** integrated with the S-CORE repository.
2. **Reuse Sphinx-Needs traceability patterns** from Syspilot and Pharaoh (concepts, not the archived repo).
3. **Keep BMAD optional** for developer productivity and facilitation only.
4. **Re-evaluate after pilot results**, including a separate assessment of ubCode/ubTrace
   as the maintained Pharaoh successor.

**Expected S-CORE outcome:** a repository-native, Sphinx-compatible AI SDLC process where
requirements, specs, ADRs, plans, code links, tests, reviews, and documentation are all
versioned, reviewable, and traceable — with AI agents participating only through governed
templates and reproducible workflows.

11. Evidence Sources
--------------------

Evidence is drawn from the **full local repositories** (agent/skill definitions, schemas,
templates, configuration), not only READMEs.

Syspilot (``syspilot-main/``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Claim
     - Concrete source in repo
   * - Sphinx-Needs based, US → REQ → SPEC traceability
     - ``syspilot/agents/syspilot.trace.agent.md`` (upward/downward tracing, link validation,
       orphan detection via ``get_need_links.py``)
   * - Multi-agent architecture (13 agents)
     - ``syspilot/agents/`` — ``pm``, ``cm``, ``qm``, ``design``, ``implement``, ``uat``,
       ``verify``, ``docu``, ``mece``, ``trace``, ``release``, ``setup``, ``installer``
   * - Copilot + Jarvis dependency; per-agent model pinning
     - Agent frontmatter (``model: Claude Haiku 4.5 (copilot)``), README requirements
       (``enthali.jarvis-core``)
   * - Early research status; MIT
     - ``README.md`` ("Early Research Project"), ``LICENSE`` (MIT, Copyright 2026 Georg)
   * - Install/bootstrap model
     - ``syspilot/bootstrap.json``, ``syspilot/{skills,sphinx,templates,prompts}/``

BMAD Method (``BMAD-METHOD-main/``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Claim
     - Concrete source in repo
   * - MIT + trademark notice; npm v6.10.0
     - ``LICENSE``, ``package.json`` (``"version": "6.10.0"``)
   * - CI tooling / quality gates
     - ``package.json`` scripts (``lint``, ``test:*``, ``validate:refs``, ``validate:skills``),
       ``test/`` suite
   * - Module ecosystem & workflow surface
     - ``bmad-modules.yaml``,
       ``src/bmm-skills/{1-analysis,2-plan-workflows,3-solutioning,4-implementation}/``
   * - Not traceability/ASPICE-first
     - No Sphinx-Needs schema or trace-link model present in ``src/`` skills

SpecKit (``spec-kit-main/``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Claim
     - Concrete source in repo
   * - MIT (GitHub, Inc.); spec-driven CLI
     - ``LICENSE``, ``pyproject.toml`` (``specify-cli``), ``spec-driven.md``
   * - Specification-first templates & gates
     - ``templates/{spec,plan,tasks,constitution,checklist}-template.md`` (prioritized user
       stories, acceptance scenarios, phase gates)
   * - Extensible / low lock-in; 30+ agents
     - ``extensions/``, ``presets/``, ``workflows/``, ``integrations/``, ``.specify/``
       override stack
   * - Security-conscious build posture
     - ``pyproject.toml`` ruff rules S602/S604/S605 (shell-injection lockdown)

Pharaoh (``pharaoh-skills-main/``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Claim
     - Concrete source in repo
   * - Sphinx-Needs V-model; 70+ atomic skills
     - ``skills/`` (e.g. ``pharaoh-req-draft``, ``pharaoh-arch-review``,
       ``pharaoh-vplan-draft``, ``pharaoh-fmea``, ``pharaoh-flow``, ``pharaoh-trace``)
   * - Explicit ASPICE/ISO conformance engine
     - ``skills/pharaoh-standard-conformance/SKILL.md``
       (``iso26262 | aspice40 | iso21434``, per-indicator pass/fail JSON)
   * - Advisory vs enforcing governance; required links
     - ``pharaoh.toml.example`` (``strictness``, ``require_verification``,
       ``required_links = ["req -> spec", "spec -> impl", "impl -> test"]``, codelinks)
   * - Schema-validated artifacts & IDs
     - ``schemas/`` (``artefact-catalog``, ``checklists-frontmatter``,
       ``id-conventions``, ``workflows``)
   * - Ships an S-CORE example project
     - ``examples/score/.pharaoh/project/``
   * - MIT license
     - ``LICENSE`` (MIT, Copyright 2026 useblocks GmbH)
   * - **Repository archived (read-only) since 2026-07-28**
     - GitHub — ``useblocks/pharaoh-skills`` (verified); README deprecation note
       points to ubCode/ubTrace
