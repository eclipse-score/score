..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-010-Infra: AI SDLC Tooling Evaluation and S-CORE Harness Direction
=====================================================================

- **Issue:** `#3115 <https://github.com/eclipse-score/score/issues/3115>`_ — Evaluate AI SDLC / SpecKit Tooling
- **Date:** 2026-07-31 (rev. 2)

.. dec_rec:: AI SDLC Tooling Evaluation and S-CORE Harness Direction
   :id: dec_rec__infra__ai_sdlc_tooling
   :status: proposed
   :version: 2
   :context: Infrastructure
   :decision: Build a thin, S-CORE-owned layer of reference agents/skills and MCP
      automation that drives the existing S-CORE process and Sphinx-Needs
      traceability, operating entirely within the current process metamodel and
      its established artifact types. Reuse concepts from SpecKit, Syspilot and
      Pharaoh rather than adopting any framework wholesale. Tool qualification and
      operational rollout are handled separately.

1. Context and Problem Statement
--------------------------------

S-CORE already has a complete development and design process, with its
associated artifacts defined in the process model, Sphinx-Needs traceability as
the artifact backbone, and governance enforced through contribution rules, code
owners and CI. **This record builds on that process; it does not replace it.**

The gap this record addresses is narrower: S-CORE has **no defined, governed way
for AI agents to participate in that process** while preserving its traceability
and reviewability. The decision to make is:

   Should S-CORE **adopt** one external AI-SDLC framework, **depend on several**,
   or **build and own** a thin automation layer that drives the existing process?

This is a tooling/integration decision, not a process-definition decision.

2. Scope and Non-Goals
----------------------

**In scope**

- Decide the evaluation outcome and the prototyping direction for AI-SDLC tooling.

**Explicit non-goals**

- This record keeps any harness **outside** the S-CORE toolchain used to produce
  release artifacts, pending a separate qualification decision.
- This record makes **no ASIL-B / tool-qualification claim**. Qualification
  (confidence in the use of software tools, ISO 26262-8) is a **separate, later
  decision** and a precondition before any such tooling could touch qualified
  work products.
- The automation layer **works entirely within the existing process metamodel
  and its established artifact (need) types**, keeping that model authoritative
  and unchanged. Agents consume it and extend its *coverage*, not its definition.
- Operational rollout, enforcement, and agent granularity are tracked as
  follow-ups (Section 11).

   *Rationale:* several reviewers correctly noted that making AI tooling part of
   the toolchain raises a qualification question that must be answered with a
   clear "yes" before adoption. This record is deliberately scoped below that
   line so the evaluation can land without pre-empting qualification.

3. Evaluation Method and Evidence Basis
---------------------------------------

The evaluation draws on three distinct, separately-labelled evidence sources, so
reviewers can weigh each appropriately:

1. **Desk scan (repository evidence).** Each framework was assessed against ten
   categories from its own source repository (agents/skills, schemas, templates,
   license, configuration) — Section 4 and Section 12. This is a structured
   comparison, **not** a claim of hands-on operation on the S-CORE codebase.
2. **Field evidence.** Hands-on PoC findings contributed during review — notably
   on OpenSpec and BMAD — are incorporated where they sharpen the desk scan (see
   Section 4.5 and the loopback finding in 8.3).
3. **Prototype evidence.** The direction in Section 7 is grounded in the in-flight
   S-CORE prototype in ``eclipse-score/mcp-servers`` (``metamodel-flow``), which
   is hands-on experience on S-CORE's own model rather than a third-party demo.

**Scoring scale:** 1 Poor · 2 Limited · 3 Acceptable · 4 Strong · 5 Excellent.
Evaluation prioritized enterprise-scale collaborative engineering and compliance
evidence over individual developer productivity.

**Tools evaluated:**

.. list-table::
   :header-rows: 1
   :widths: 20 50

   * - Tool
     - Source / evidence
   * - Syspilot
     - https://github.com/enthali/syspilot (desk scan)
   * - BMAD Method
     - https://github.com/bmad-code-org/BMAD-METHOD (desk scan + field PoC)
   * - SpecKit
     - https://github.com/github/spec-kit · https://speckit.org (desk scan)
   * - OpenSpec
     - Field PoC during review (concurrent-development evaluation)
   * - Pharaoh
     - https://github.com/useblocks/pharaoh-skills (desk scan; repo archived)

4. Tool-by-Tool Analysis
------------------------

4.1 Syspilot
~~~~~~~~~~~~

Built directly on Sphinx-Needs; agents follow deterministic requirement links
("the map, not the flashlight"), with change-impact producing focused context
(``O(affected)``, not ``O(total)``).

- **Strengths:** native Sphinx-Needs orientation; strong traceability mindset;
  manager/engineer agent roles across the lifecycle.
- **Weaknesses:** README labels it an early research project; hard dependency on
  VS Code, Copilot and ``enthali.jarvis-core``; governance not enterprise-hardened.
- **S-CORE view:** valuable source of **concepts** for the traceability layer.

4.2 BMAD Method
~~~~~~~~~~~~~~~

Broad AI-assisted agile framework (34+ workflows, role agents); about
collaboration patterns rather than regulated engineering evidence.

- **Strengths:** mature packaging (npm v6.10.0, MIT), CI-friendly tooling.
- **Weaknesses:** not Sphinx-Needs or ASPICE native; traceability is not the
  central artifact model.
- **S-CORE view:** best kept for ideation/facilitation; not compliance evidence.

4.3 SpecKit
~~~~~~~~~~~

Strongest **specification-first workflow**:
``constitution → specify → plan → tasks → analyze → implement``, with CLI,
templates and phase gates.

- **Strengths:** specs as versioned artifacts; governance primitives; broad agent
  support (30+); MIT.
- **Weaknesses:** not built for Sphinx-Needs, Bazel, ADRs or ASPICE; traceability
  is workflow-level; requirement IDs, Needs links and test evidence require
  S-CORE-specific integration.
- **S-CORE view:** best reused as a **phase shell** (Section 8) whose outputs are
  S-CORE needs.

4.4 Pharaoh
~~~~~~~~~~~

Conceptually the closest match: Sphinx-Needs V-model skill chain with explicit
ASPICE 4.0 / ISO 26262-8 / ISO 21434 conformance concepts, enforcing mode, review
metadata and reproducibility checks.

- **Weaknesses:** repository **archived (read-only since 2026-07-28)**; skills
  moved to commercial-adjacent ubCode/ubTrace; "AI is the runtime" is hard to
  certify/stabilize.
- **S-CORE view:** best **reference design**; reuse concepts rather than depend on
  the archived repo.

.. note::

   **Verified:** ``useblocks/pharaoh-skills`` is archived (read-only) as of
   2026-07-28 (latest release v1.2.1). Functionality is stated to have moved into
   ubCode / ubTrace.

4.5 OpenSpec
~~~~~~~~~~~~

Added following review feedback; assessed primarily from **field PoC** (a
concurrent-development evaluation) rather than desk scan.

- **Strengths:** simple, lightweight SDD workflow; maintained; low adoption cost.
- **Weaknesses (field-observed):** not Sphinx-Needs or ASPICE native; **no
  loopbacks within an ongoing change** — once tasks are derived, agents implement
  and iterate but are never returned to re-check that implementation still matches
  the original specification, or to raise requirements discovered late (e.g.
  non-functional/test requirements). Holding even its own simple process requires
  constant supervision or supporting tooling.
- **S-CORE view:** reinforces the core finding (Section 8.3): keeping S-CORE's own
  process and artifact types authoritative — and driving them with automation —
  is more robust than replacing them with a tool's defaults.

5. Scoring Matrix
-----------------

Scores 1–5. OpenSpec scores are field-informed rather than desk-scan.

.. list-table::
   :header-rows: 1
   :widths: 30 12 10 12 12 12

   * - Category
     - Syspilot
     - BMAD
     - SpecKit
     - OpenSpec
     - Pharaoh
   * - Requirements Engineering
     - 4
     - 3
     - 4
     - 3
     - 5
   * - Specification Management
     - 3
     - 3
     - 5
     - 4
     - 4
   * - Traceability
     - 5
     - 2
     - 3
     - 2
     - 5
   * - AI Agent Support
     - 4
     - 5
     - 4
     - 4
     - 4
   * - Governance
     - 3
     - 3
     - 4
     - 2
     - 4
   * - Reproducibility
     - 3
     - 2
     - 4
     - 3
     - 4
   * - Open Source Sustainability
     - 2
     - 4
     - 5
     - 4
     - 2
   * - S-CORE Integration
     - 5
     - 2
     - 3
     - 2
     - 5
   * - ASPICE Alignment
     - 3
     - 2
     - 3
     - 2
     - 5
   * - Long-Term Maintainability
     - 2
     - 4
     - 5
     - 4
     - 2
   * - **Total**
     - **34**
     - **30**
     - **40**
     - **30**
     - **40**

**Interpretation:** the totals are secondary. No tool scores well on *both*
S-CORE Integration/ASPICE *and* Maintainability — the maintained tools are not
domain-aligned, and the domain-aligned tool is archived. That split is what
favours a build-and-own direction that keeps S-CORE's model central.

6. ASPICE Impact Assessment
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 10 12 12 12

   * - ASPICE Area
     - Syspilot
     - BMAD
     - SpecKit
     - OpenSpec
     - Pharaoh
   * - SYS.1 Requirements elicitation
     - Medium
     - Medium
     - Med/High
     - Medium
     - High
   * - SYS.2 System requirements
     - High
     - Low/Med
     - Medium
     - Low/Med
     - High
   * - SYS.3 System architecture
     - Medium
     - Med/High
     - Medium
     - Low/Med
     - High
   * - SWE.1 Software requirements
     - High
     - Low/Med
     - Medium
     - Low/Med
     - High
   * - SWE.2 Software architecture
     - Medium
     - Med/High
     - Medium
     - Low/Med
     - High
   * - SWE.3 Detailed design
     - Medium
     - Medium
     - Medium
     - Medium
     - Med/High
   * - SWE.4 Unit verification
     - Medium
     - Medium
     - Medium
     - Low/Med
     - High
   * - SWE.5 Integration testing
     - Medium
     - Medium
     - Medium
     - Low/Med
     - Med/High
   * - SWE.6 Qualification testing
     - Medium
     - Low/Med
     - Medium
     - Low/Med
     - High

**Key point:** ASPICE alignment depends on **traceability evidence**, not
generated documents. The strongest alignment comes from driving the S-CORE model
that already produces that evidence — which is the direction this record takes.

7. Decision
-----------

Build and own a thin S-CORE layer — reference agents/skills plus MCP automation —
that drives the **existing** S-CORE process and Sphinx-Needs traceability, reusing
proven concepts rather than adopting any framework wholesale.

- **Reuses the existing model as-is.** Agents read the current process metamodel
  and its defined artifact (need) types via the cached sidecar graph
  (``metamodel-flow``, ``process_graph.json``), keeping it the single source of
  truth.
- **SpecKit — adapt as a phase shell.** Reuse its phase structure; every output is
  an existing S-CORE need.
- **Syspilot / Pharaoh — concepts.** Requirement-driven traceability and
  change-impact (Syspilot); lifecycle governance and conformance (Pharaoh).
- **BMAD / OpenSpec — reference only.** Useful for ideation; field evidence shows
  S-CORE's own process is the more robust backbone to automate against.

8. Integration Architecture
---------------------------

8.1 Principle
~~~~~~~~~~~~~

The layer adds **automation that drives the existing process**. Every phase output
is an existing S-CORE need, so the established artifact types remain the backbone
and the generated chain stays native to S-CORE.

8.2 Phase → Artifact → Process → Tool mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Need-type IDs below are representative — bind each to the actual IDs in
``metamodel.yaml`` / ``process_graph.json`` before merge.

.. list-table::
   :header-rows: 1
   :widths: 14 22 20 24 20

   * - SpecKit phase
     - S-CORE artifact (need)
     - Process area
     - Backing MCP tool
     - Gate / loopback
   * - constitution
     - *(reuses existing rules)*
     - Process model (source of truth)
     - ``metamodel-flow`` sidecar loader
     - read-only; existing metamodel stays authoritative
   * - specify
     - ``stkh_req``, ``feat_req``
     - Requirements Eng. (SYS.1/2, SWE.1)
     - requirement validation + normalization; SpecKit→Needs conversion
     - human review before needs enter the graph
   * - plan
     - ``feat_arc_*``, ``comp_arc_*``, ``dec_rec``
     - Architecture (SYS.3, SWE.2)
     - traceability query + change-impact
     - architecture review; ADR sign-off
   * - tasks
     - ``comp_req``, ``dd`` + task breakdown
     - Detailed design (SWE.3)
     - task derivation with trace links
     - requirement→task completeness check
   * - analyze
     - *(validation only)* — MECE, orphans, ``needs.json``
     - Verification planning / Change Mgmt
     - change-impact + **lifecycle loopback**
     - **loopback: re-check spec↔impl↔test; block on drift**
   * - implement
     - code, ``*_test``, ``mod_ver_report``
     - Implementation + Verification (SWE.4–6)
     - evidence collection; progress/reporting
     - test evidence + trace breadcrumb; human sign-off

8.3 The loopback
~~~~~~~~~~~~~~~~

Field evaluation of SDD tools (OpenSpec, BMAD) found their decisive weakness:
**no loopback within an ongoing change.** Agents implement and iterate but are
never returned to confirm the implementation still matches the specification, or
to raise requirements discovered late. The S-CORE layer makes this loopback a
**first-class, enforced gate** (``analyze → specify``) rather than relying on a
human to notice drift.

.. mermaid::

   flowchart LR
       A[Sphinx-Needs Requirements] --> B[specify]
       B --> C[plan: architecture / ADR]
       C --> D[tasks: detailed design]
       D --> E[implement: code + Bazel]
       E --> F[tests + evidence]
       F --> G[Sphinx documentation]
       G --> A
       F -->|loopback: drift detected| H{analyze: spec↔impl↔test aligned?}
       H -->|no| B
       H -->|yes| I[human sign-off]

9. Governance and Safety Principles
-----------------------------------

- **One process step per agent.** Agents are scoped narrowly and defer to skills,
  keeping context and review tractable.
- **Human sign-off at every gate.** No artifact — requirement, design, code or
  test — enters the graph or merges without human approval.
- **Everything reviewable.** Everything-as-code, including requirements and
  generated code, stays human-understandable and reviewable by the person signing
  it off.
- **Reproducible by construction.** Prompts, templates, model settings, inputs and
  generated outputs are versioned in Git so every run is auditable and repeatable.

10. Risks and Mitigations
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 42 15 43

   * - Risk
     - Impact
     - Mitigation
   * - Qualification (ASIL-B) not yet demonstrated
     - High
     - Kept outside the toolchain; no canon status until a separate qualification
       decision gives a clear "yes"
   * - Generated chain diverging from S-CORE artifacts
     - High
     - Phase-shell only; every output is an existing S-CORE need
   * - Model drift between harness and process
     - Medium
     - Agents read the cached sidecar ``process_graph.json``; the metamodel stays
       the single source of truth
   * - AI output nondeterminism
     - High
     - Version prompts, templates, model settings, inputs and outputs
   * - Pharaoh repo archived
     - High
     - Reuse concepts; reassess ubCode/ubTrace separately
   * - Reviewer/sign-off burden from agent output
     - Medium
     - Narrow agents + enforced gates + trace evidence to keep review tractable

11. Open Questions / Follow-ups
-------------------------------

- **Qualification assessment** — can this tooling meet ISO 26262-8 tool-use
  confidence before any toolchain role? (precondition, separate DR)
- **Agent granularity** — e.g. a process-engineer agent deferring to per-step
  skills vs. role-specific agents. (separate design DR)
- **Relationship to** ``mcp-servers`` ``metamodel-flow`` — this record sets the
  direction the prototype already pursues; keep the two in sync.
- **ubCode / ubTrace** — reassess as the maintained Pharaoh successor.

12. Evidence Sources
--------------------

Desk-scan evidence is drawn from the full repositories (agents/skills, schemas,
templates, configuration), not only READMEs. Field evidence (OpenSpec, BMAD) is
from reviewer PoC work and labelled as such.

*(Retain the per-tool evidence tables for Syspilot, BMAD, SpecKit and Pharaoh
from version 1 here; add an OpenSpec row pointing to the field-PoC findings
summarized in Section 4.5.)*
