..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

DR-010-Infra: Select AI tooling for S-CORE integration and evaluation
=====================================================================

.. dec_rec:: Select AI tooling for S-CORE integration and evaluation
   :id: dec_rec__infra__ai_sdlc_tooling
   :status: proposed
   :version: 3
   :context: Infrastructure; integrate AI assistance within the existing S-CORE engineering process
   :decision: Recommend APM for packaging, Spec Kit for integration development and Harbor for evaluation; retain the native S-CORE engineering workflow
   :tracking: https://github.com/eclipse-score/score/issues/3115
   :consequences: Retain native artifact authority and human accountability; require compatibility and comparative pilot evidence

This is the proposed evaluation outcome for
`issue #3115 <https://github.com/eclipse-score/score/issues/3115>`_, replacing
the same-ID candidate in `PR #3140 <https://github.com/eclipse-score/score/pull/3140>`_.
Version 3 makes the recommendation explicit. Maintainer acceptance is pending.
The recommendation selects tools for the roles below; operational rollout and
qualification are separate implementation decisions.

Context
-------

S-CORE already defines its engineering process, work products, metamodel,
traceability and review responsibilities. The problem is how AI assistance can
operate within those rules while retaining understandable artifacts, measured
verification and human accountability. Another authoritative requirements or
process store would introduce synchronization work and obscure ownership.

The review of PR #3140 requests real experience on S-CORE artifacts, lifecycle
loopbacks when requirements change, manageable agent context, technical
feasibility and clear qualification limits. The ``s-core_sw_fabric`` pilot
provides one exploratory implementation and historical measurements against
pinned S-CORE artifacts. It is not a head-to-head benchmark of every candidate
or an organization-scale deployment.

The scope of this evaluation is the eight options listed in
`issue #3115 <https://github.com/eclipse-score/score/issues/3115>`_: APM, Lola
and OKIT for packaging; Syspilot, BMAD, Spec Kit and Pharaoh for SDLC/harness;
Harbor for evaluation. Their different responsibilities require separate
assessments. A packaging manager does not establish workflow correctness, and
an agent benchmark does not establish engineering acceptance.

Decision
--------

Recommend the following combination on the available evidence:

* **APM for distributing agent context.** Its captured documentation explicitly
  describes resolved-source/content locks, installation policy, drift checks and
  SBOM export. These capabilities match reproducibility, provenance and bounded
  destinations. This supports the issue assignee's packaging recommendation.
  Organization-wide installation behavior remains to be validated.
* **Spec Kit for developing the integration and supporting tools.** This is the
  SDLC option with retained implementation experience in this packet. Keep the
  existing S-CORE workflow and native work products for target engineering;
  translate selected procedures rather than replacing the native metamodel.
* **Harbor for comparative agent evaluation.** Its documented custom benchmark
  environments fit an independently reviewed S-CORE task corpus. Native outcome
  checks and human engineering review remain the acceptance authority. No Harbor
  benchmark result or execution is claimed here.

This recommendation is a qualitative engineering inference from the captured
sources and the labelled implementation evidence. It is not a numerical ranking
or a measured claim of comparative performance. The rejected/deferred options
and conditions for reconsideration are recorded below.

Apply these integration constraints:

#. Keep native S-CORE artifacts, identifiers, metamodel and accepted tailoring
   authoritative. Generate or derive agent context from pinned native sources.
   Sidecar graphs must remain rebuildable views, not another requirements store.
#. Use Spec Kit for developing the integration itself. Evaluate adapted
   procedures for native tasks without requiring S-CORE work products to become
   Spec Kit documents or creating duplicate mandatory artifacts.
#. Evaluate packaging separately from execution. APM remains a candidate,
   consistent with the issue's existing packaging proposal. Test distribution,
   upgrades, drift and destination controls before selecting a packaging tool.
#. Use deterministic tools to measure required checks. Agents may draft and
   critique. Required engineering judgments remain with authorized humans;
   unattended runs export evidence and terminate at the human boundary.
#. Admit source-bound tasks with explicit write paths, check scope, context,
   tools, attempts and budgets. Changed requirements or subjects must trigger
   renewed impact and evidence assessment. Preserve missing checks and failures.
#. Retain portable evidence and understandable source. Successful orchestration
   must not hide failed compilation, missing quality evidence, unsupported
   platforms or pending engineering review.

Fabro is the fabric pilot's pinned execution candidate. It is not one of the
eight issue-listed options, and this proposal does not select it for S-CORE.
The observed resume limitation is included in the assessment.

Selection Criteria
------------------

The comparison prioritizes native Sphinx-Needs/metamodel compatibility,
reproducible context and destination control, requirement-change loopbacks,
independent deterministic verification, portable evidence, supported developer
clients, and maintenance/integration effort. These priorities derive from the
S-CORE ownership and review concerns in PR #3140 and the retained native pilot.
They are evaluation criteria for this decision, not newly accepted requirements.

APM is the strongest documented match for governed packaging in this survey;
Lola remains a credible distribution alternative. OKIT's recorded source commits
are useful provenance, so the evaluation does not repeat the earlier assertion
that it has no version tracking. Its automatic provider enablement is a concrete
reason to require destination checks for wider use. No undocumented absence of
security or governance features is treated as a proven defect.

Spec Kit is selected for the role actually exercised by this packet. Syspilot's
Sphinx-Needs focus makes it a preferred next native-context experiment, while its
stated early research status, client/license dependencies and silent loss of
handoff capability when its extension is disabled prevent an unqualified default
rollout recommendation. BMAD documents adaptable workflows, but this packet does
not establish its native S-CORE adaptation. Pharaoh supplies relevant native
analysis concepts, yet its archived repository cannot establish maintained
support. Harbor fits the evaluation role; its score never replaces native review.

Alternatives Considered
-----------------------

All repository descriptions below are primary-source observations captured on
2026-10-07. Documentation support is not proof of executed behavior. Exact
source commits, original README bytes, redirects and available licenses are
retained in the `candidate inventory
<https://github.com/Eclipse-SDV-Hackathon-Chapter-Four/Thinking_CAPs/blob/contrib/score-ai-sdlc-3115-evidence/contributions/issues/eclipse-score/score/3115/evidence/candidates/index.json>`_.
No numeric ranking is assigned to an untested tool.

.. list-table:: Issue-listed options and evidence levels
   :header-rows: 1
   :widths: 15 30 25 30

   * - Candidate
     - Documented purpose
     - Experience in this packet
     - Selection and reason
   * - `APM <https://github.com/microsoft/apm>`_
     - Manifest-based agent context packaging, locks, policy and MCP integration
     - S-CORE package inspection and disposable MCP probes; no APM CLI distribution pilot
     - Recommend as primary packaging tool: documented locks, policy, drift and inventory directly match provenance needs
   * - `Lola <https://github.com/LobsterTrap/lola>`_
     - Cross-assistant skill/context packages and declarative installation
     - Primary-source research; not executed
     - Retain as packaging fallback when supported clients and the same installation/upgrade cases are demonstrated
   * - `OKIT <https://github.com/Mumme-IT/okit>`_
     - Installs skills/agents to providers and records source commits
     - Primary-source research; not executed
     - Restrict to isolated personal prototyping; documented auto-enabling of detected providers needs explicit destination control before shared rollout
   * - `Syspilot <https://github.com/enthali/syspilot>`_
     - Sphinx-Needs links and focused change context; labelled early research
     - Primary-source research; not executed
     - Prefer for a subsequent native-context prototype; defer baseline adoption because early breaking changes and VS Code/Copilot/jarvis-core requirements need compatibility checks
   * - `BMAD <https://github.com/bmad-code-org/BMAD-METHOD>`_
     - Skills and workflows for explicit planning, implementation and learning loops
     - Primary-source research; not executed
     - Keep as an alternative; adaptive planning is useful, but native artifact/loopback adaptation is unmeasured here and Spec Kit has retained integration experience
   * - `Spec Kit <https://github.com/github/spec-kit>`_
     - Specification-driven development workflow
     - Used to develop the fabric at pinned v1.0.12 / e77daa9021d20db26b878f7dfa5640fe5a42d04e
     - Recommend for integration development on measured experience; adapt native tasks without imposing duplicate Spec Kit work products
   * - `Pharaoh <https://github.com/useblocks/pharaoh-skills>`_
     - Sphinx-Needs analysis encoded in skills and agent instructions
     - Primary-source research; requested URL redirects to an archived repository
     - Do not add the archived repository as a maintained dependency; reuse reviewed native-trace concepts and assess successors separately
   * - `Harbor <https://github.com/harbor-framework/harbor>`_
     - Agent benchmarks and evaluation environments
     - Primary-source research; not executed
     - Recommend as the comparative benchmark driver: custom environments and arbitrary agents match a shared native task corpus

Current README capabilities are not transferred to historically measured
versions. The fabric's source and tool locks remain distinct from this dated
repository survey. This pilot cannot establish comparative superiority over
the seven alternatives that were not executed.

Pilot Evidence
--------------

The `portable evaluation packet
<https://github.com/Eclipse-SDV-Hackathon-Chapter-Four/Thinking_CAPs/tree/contrib/score-ai-sdlc-3115-evidence/contributions/issues/eclipse-score/score/3115>`_
contains a source snapshot, per-file hashes, original command records,
historical logs and acceptance limitations. Its `evidence map
<https://github.com/Eclipse-SDV-Hackathon-Chapter-Four/Thinking_CAPs/blob/contrib/score-ai-sdlc-3115-evidence/contributions/issues/eclipse-score/score/3115/evidence-map.md>`_
identifies supplied bytes, existing native packets and omitted deep history.

The fabric baseline is ``7e24a43c258f1dcaa2b27e02b501964847bc8714`` plus a
captured dirty working tree, including selected untracked development files.
A commit identifier alone does not describe that snapshot. Historical test
results belong to their recorded subjects; they are not rebound to the current
snapshot or treated as fresh qualification evidence.

.. list-table:: Measured experience and practical limits
   :header-rows: 1
   :widths: 20 45 35

   * - Question
     - Retained experience
     - Limit
   * - Native ownership and traceability
     - Locked process/docs sources, native export/import, artifact indexing, expected-set trace, drift and impact implementations
     - Production mappings, profile review and broader native compatibility remain open
   * - Lifecycle loopbacks
     - Old/new reverse impact, stale-subject rejection, changed-relation regression and bounded correction/evidence-refresh modes
     - Implementation checks do not establish complete B1-B5 engineering qualification
   * - Agent context and procedures
     - Pinned MCP discovery/probes, baseline-bound manifests, selected skills, bounded summaries/retrieval and call limits
     - Unsupported tools or unknown usage block relevant stages; APM rollout is untested
   * - Deterministic development validation
     - Historical 011 full regression: 2,056 passed and 22 skipped; affected scope: 139 passed; initial failing run retained
     - Logs apply to historical subjects; no current dirty-worktree pass or complete native readiness claim
   * - Context measurement
     - Synthetic byte estimates: 86.94-95.12%; first live rendering proxies: 30.46-30.63%; later tool-projection proxies: 66.32-66.60%
     - Controlled rendering fixtures; real-task savings, semantic quality, billing and runtime advantage remain unestablished
   * - Native use
     - Lifecycle #704 retains a scoped implementation and 113 passing native cases
     - Selected revision/check scope applies; native review and qualification remain distinct
   * - Failure transparency
     - Historical DeepSeek communication #1261 attempt failed compilation with 0/5 tests executed despite orchestration completion; a later Claude correction passed selected Linux checks
     - Failed history and later corrections remain distinct; native acceptance stays pending
   * - Trust and review
     - Fixture assurance gates, stale/unauthorized refusal cases and explicit offline engineering review records
     - Protected production trust roots and acceptance authority are not provisioned; no ASIL-B qualification
   * - Runtime suitability
     - Pinned Fabro disposable register/run/status/cancel/export probes
     - Same-run checkpoint resume was unavailable on the candidate; no runtime selection

The token observations distinguish synthetic context estimates from actual
provider usage on controlled rendering fixtures. Equal expected fixture
outputs do not establish equal engineering adequacy. Neither experiment
establishes the fabric's intended 60-80% real routine-task savings target.

Raw development/JUnit logs and rendering request/response records travel in
the packet. Native implementation packets are retained separately in the
same repository. Some deep source/build/tool payloads are only inventoried;
full replay requires those original bytes. The byte-integrity verifier does
not execute tests, qualify tools or authenticate engineering decisions.

Consequences
------------

The proposal retains one native engineering authority and makes tool choices
separable. It adds compatibility, integration, evidence retention and review
work. Spec Kit artifacts used to develop the fabric must not become duplicate
mandatory artifacts for all S-CORE development.

Native-version drift, platform applicability and complete check denominators
require explicit treatment. Generated artifacts and code must remain
understandable to the people accountable for their review. Neither tests nor
agent judgments replace the required engineering review or qualification.

Justification for the Decision
------------------------------

The fabric supplies implementation experience for architectural boundaries,
selective context, negative outcomes and native verification. It supports
piloting those patterns, rather than adopting a framework wholesale. It does
not demonstrate comparative tool superiority, community-scale behavior or
qualification of tools for a safety-related use.

This record supplies an evaluation outcome for all eight issue-listed options
and the rationale for the recommended combination. Acceptance of this decision
record is the requested completion of issue #3115. It does not assert completed
rollout, comparative benchmarks or qualification. Maintainers decide whether the
available evidence supports this recommendation and may require additional
comparison before accepting it. No accepting person, date or approval is inferred.

Reconciliation and Implementation Handoff
-----------------------------------------

PR #3307 offers this version as a replacement for the DR-010 candidate in #3140.
Both use ``dec_rec__infra__ai_sdlc_tooling``. Merge one representation of that ID
at ``docs/design_decisions/infrastructure/DR-010-infra.rst``. If #3307 is accepted,
the owner of #3140 can close or supersede its same-ID proposal. If #3140 is the
preferred vehicle, incorporate this record there and supersede #3307. Do not
merge both records or recreate the removed legacy directory. This PR does not
modify another contributor's branch or infer their acceptance.

Follow-on rollout work should retain a reviewed public task corpus and immutable
source pins. Check repeated installation output, allowed provider destinations,
content/source integrity, upgrades, drift and rollback for packaging. Check native
IDs/link directions, requirement-change loopbacks, stale-evidence refusal and
required artifact coverage for procedures. Evaluate agents on native build/test
and review outcomes, recording retries, failures, usage and environment; fixture
rendering proxies do not establish task savings. Disposition unsupported clients,
unknown usage and missing checks before unattended use. Provision trust and
qualified human review for any claimed safety-related application.

These are explicit follow-on validation needs for implementation and adoption.
They are not reported as executed work or automatically added to #3115's DoD.
Tool licensing, native tailoring and qualification applicability remain subject
to the selected versions, use cases and authorized engineering decisions.
