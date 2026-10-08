..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-009-Int: Portable safety traceability and SBOM exchange
==========================================================

- **Date:** 2026-10-08

.. dec_rec:: Portable safety traceability and SBOM exchange
   :id: dec_rec__int__portable_safety_traceability
   :status: proposed
   :version: 1
   :context: Integration
   :decision: Option 3 (proposed)

Context / Problem
-----------------

S-CORE safety lifecycle information is created and reviewed in engineering
systems such as Sphinx-Needs and emerging Dependable Element or graph-based
tooling. Downstream consumers, including product integrators, OEMs and
independent assessors, also need to discover the safety context associated
with delivered software and its SBOM components.

Copying classification, rationale, requirements, evidence and approval state
into a hand-authored sidecar would create a second source of truth. Exporting
directly from every authoring tool into every receiving format would instead
create tool-specific coupling and inconsistent semantics. Waiting for future
native SPDX and CycloneDX safety models would leave current S-CORE delivery and
evaluation use cases unaddressed.

The integration therefore needs a source-neutral mapping boundary that:

* preserves the authoritative lifecycle records and their identifiers;
* supports more than one S-CORE authoring and traceability approach;
* transports selected safety context with software and SBOM deliveries;
* allows deterministic validation and correlation by receiving tools;
* distinguishes artifact integrity from analysis completeness and truth; and
* never lets an exporter or receiving tool create or approve a safety decision.

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

* **Single source of truth:** Requirements, architecture, safety
  classification, evidence, verification and approval remain authoritative in
  their lifecycle systems.
* **Tool independence:** Sphinx-Needs, Dependable Element, TRLC/Lobster and
  future sources can map into the same portable semantics without making one
  tool mandatory for all producers.
* **Traceability:** Stable identifiers preserve the paths from requirement to
  design, implementation, test, evidence, analysis and approval.
* **Context:** Safety relevance is expressed for a product-component or
  system-element context, not as an intrinsic global property of a package.
* **Fail-closed behavior:** Missing, contradictory, ambiguous, stale or
  integrity-invalid records remain explicit and cannot be silently promoted to
  an approved state.
* **Exchange:** Current SPDX 2.3 and CycloneDX 1.x deliveries can discover an
  external safety artifact. Future native SPDX or CycloneDX representations can
  map into the same receiving model.
* **Provenance:** Exports carry source identity, source revision, policy and
  tool versions, record identities, review state and content digests.
* **Human authority:** Automated tooling may validate, correlate and propose
  findings. Authorized people remain responsible for classification, impact
  decisions, approvals and safety-case acceptance.

Non-Goals
~~~~~~~~~

* Replacing the S-CORE lifecycle model, safety case or review workflow.
* Defining a new safety classification or integrity-level vocabulary.
* Treating functional-safety relevance as vulnerability exploitability or a
  VEX ``not affected`` justification.
* Automatically determining legal applicability, safety relevance, impact or
  approval.
* Claiming that a digest alone proves authorship, authority or correctness.
* Requiring receiving tools to support the experimental transport before the
  corresponding governance and implementation decisions are accepted.

Primary Use Cases
-----------------

Supplier, OEM and independent-assessment handover
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Tier 1 or internal component team delivers software, an SBOM and available
safety lifecycle metadata. The OEM or system integrator checks the package
against its product context and applicable policies, records its own decisions
with identity and provenance, and prepares a safety-case or assessment evidence
package for an independent assessor or approval authority.

Internal feature development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A code, dependency, requirement, architecture, vulnerability or policy change
opens an impact analysis. The traceability graph identifies the potentially
affected requirements, tests, evidence and approval records. Routine changes
may pass automated checks; defined checkpoints require human review. Incremental
evaluation is supplemented by periodic or baseline-triggered full evaluation so
that an incomplete impact boundary cannot silently omit transitive effects.

Responsibility or jurisdiction transfer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When software responsibility moves between legal entities, organizations or
countries, tooling proposes candidate policy changes for legal and compliance
confirmation. The accountable organization records the confirmed policy set,
required checks and human approvals before accepting the package.

Open-source intake
^^^^^^^^^^^^^^^^^^

An open-source project may publish useful component metadata but is not a
contractual supplier or responsible party. The adopting OEM or integrator
retains responsibility for classification, applicability, missing evidence and
approval. Missing safety metadata is represented as an undetermined upstream
state, not as evidence that the component is not safety-relevant.

Options Considered
------------------

Option 1: Hand-authored SRAC record as an independent source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teams manually maintain a portable safety assertion alongside the lifecycle
model.

Pros:

* Simple for an initial demonstration.
* Independent of a specific lifecycle tool.

Cons:

* Duplicates safety decisions and evidence.
* Allows the portable record and authoritative lifecycle state to drift.
* Adds a second review and maintenance workflow.

Option 2: Direct authoring-tool exporters for every target format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each lifecycle tool exports its records directly into SPDX, CycloneDX and
receiving-tool-specific representations.

Pros:

* Avoids a separately authored safety file.
* Can exploit source-tool-specific information.

Cons:

* Couples each source to every transport and receiver.
* Repeats mapping and validation logic.
* Makes semantic consistency and migration difficult.

Option 3: Canonical projection with mapping overlays and portable transport
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Authoritative source records are mapped read-only into a source-neutral safety
traceability projection. A validated exporter packages the selected projection
as an integrity-bound SRAC artifact and references it from the delivered SPDX or
CycloneDX SBOM. Receivers verify and correlate the artifact without becoming an
authority for its safety decisions.

Pros:

* Preserves one authoritative authoring source.
* Supports multiple S-CORE metamodel and tooling approaches through adapters.
* Separates lifecycle semantics, exchange transport and receiving-tool storage.
* Provides a migration path to native SPDX and CycloneDX safety models.
* Allows deterministic positive and negative testing.

Cons:

* Requires governance of the canonical projection and mappings.
* Requires versioning and compatibility rules.
* Adds exporter, validation and packaging work.
* Does not itself prove the truth or completeness of a safety claim.

Option 4: Wait for native standards support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No portable safety metadata is emitted until released SPDX and CycloneDX
formats provide all required native concepts.

Pros:

* Avoids an interim transport convention.
* Reduces near-term implementation work.

Cons:

* Provides no present-day exchange path.
* Delays validation of S-CORE requirements against the developing standards.
* Does not solve the mapping between multiple authoritative source models.

Proposed Decision
-----------------

Adopt **Option 3** as the direction for evaluation and staged implementation.

The portable representation is a generated projection, not a second authoring
system. Mapping overlays translate authoritative S-CORE source concepts into a
canonical safety traceability model. The initial Sphinx-Needs adapter reads
``needs.json``; additional adapters may support Dependable Element,
TRLC/Lobster or graph-based sources after their mappings are reviewed.

The canonical projection shall cover, at minimum:

* subject and product/system context;
* requirements and architecture elements;
* domain-specific safety classification and relevance;
* analysis triggers, impacted elements and impact levels;
* decisions, responsible agents and lifecycle state;
* verification, evidence and approval records;
* assumptions of use and applicability where supplied by the source;
* source, policy and tool provenance; and
* publication roots and analysis-closure state.

The projection shall not invent a missing relationship, classification,
decision, approval or policy conclusion.

Architecture and Packaging Boundary
-----------------------------------

The intended flow is:

.. code-block:: text

   authoritative lifecycle sources
       Sphinx-Needs | Dependable Element | TRLC/Lobster | future sources
                              |
                       reviewed mappings
                              v
              canonical safety traceability projection
                              |
             producer validation and package generation
                              v
               integrity-bound SRAC exchange artifact
                              |
             SPDX/CycloneDX external reference and digest
                              v
               receiver verification and correlation

For current formats, the CycloneDX 1.x path uses an ``externalReference`` and
native hash field. The SPDX 2.3 path uses a package ``ExternalRef`` in category
``OTHER`` and carries the digest by a documented convention, such as the
comment or an annotation; SPDX 2.3 does not provide a native checksum field on
``ExternalRef``. A signed in-toto/DSSE statement may strengthen identity and
provenance where available, but signatures do not replace semantic completeness
validation.

Native future SPDX or CycloneDX safety data shall enter the same canonical
receiver model rather than creating a separate UI, query or policy path.

Validation and Trust Boundaries
-------------------------------

Producer-side validation checks:

* schema and vocabulary conformance;
* identifier uniqueness and referential integrity;
* requirement-to-evidence and decision traceability;
* consistency between related classification fields;
* required lifecycle and closure state;
* source revision and artifact digests; and
* deterministic regeneration of derived artifacts.

Receiver-side validation repeats schema, reference, digest and correlation
checks. It exposes matched, unmatched, ambiguous, invalid and stale states and
preserves the original provenance. A receiver must not convert any of those
states into an approved safety decision.

Artifact integrity, claim completeness and claim truth are separate properties:

* a digest proves that retrieved bytes match the referenced bytes;
* a signature or attestation can bind bytes and subject to an identity;
* closure validation can show whether required graph branches are present; and
* engineering review determines whether the underlying claim is acceptable.

Policies and Human Checkpoints
------------------------------

Policy evaluation may automate objective checks and propose applicable policy,
but human confirmation is required when at least one of the following applies:

* safety relevance, integrity level or an assumption of use changes;
* a requirement, verification result, evidence link or approval becomes stale;
* a vulnerability or security finding affects a safety-relevant component;
* the calculated impact boundary is incomplete or ambiguous;
* software responsibility crosses an organization, legal entity or country;
* legal or regulatory applicability changes; or
* an analysis contains an unresolved required decision or evidence branch.

OEM or integrator decisions are recorded with responsible identity, policy
version, timestamp and digest before packaging.

Tool Confidence
---------------

Generated evidence records the exporter, validator and mapping versions. Each
adopter remains responsible for assessing the confidence or qualification needs
of tools whose output is used in a safety case, including the considerations in
ISO 26262-8 clause 11 where applicable.

Consequences
------------

* S-CORE keeps lifecycle rules and safety decisions in authoritative models.
* SRAC becomes a derived portability and packaging layer.
* Competing authoring approaches can be evaluated through explicit mappings
  rather than parallel exchange formats.
* SPDX and CycloneDX remain transport and standardization targets, not the
  original authority for an S-CORE engineering decision.
* Downstream tools can implement read-only correlation before native safety
  models are released, while retaining a migration path.
* A governance owner is required for the canonical projection, mappings,
  versioning rules and compatibility tests.

Staged Implementation
---------------------

Following acceptance of this decision record, implementation should be split
into independently reviewable changes:

#. Define and test the canonical projection and mapping contract.
#. Add the Sphinx-Needs ``needs.json`` adapter without changing source records.
#. Add producer-side validation and deterministic SRAC generation.
#. Add current SPDX 2.3 and CycloneDX 1.x reference mappings.
#. Add receiving-side integrity verification and deterministic correlation.
#. Add packaging, provenance and optional attestation integration.
#. Add further source adapters only after their mappings and ownership are
   agreed.

Acceptance Criteria
-------------------

A demonstrator is accepted only when it proves all of the following:

#. The same source revision produces byte-identical portable output.
#. A product-specific assertion correlates only by an approved stable identity,
   such as PURL and version, digest or an explicit SBOM reference; name-only
   matching is rejected.
#. Requirement, evidence, decision and approval references resolve.
#. An unmatched or ambiguous component fails closed without creating a safety
   conclusion.
#. A tampered artifact or mismatched digest is rejected.
#. Removing a required decision or evidence edge leaves signature verification
   unaffected but causes completeness validation to fail.
#. A source update marks dependent exported information stale until it is
   regenerated and reviewed.
#. Tool and policy versions are present in generated provenance.
#. Incremental evaluation is backed by a periodic or baseline-triggered full
   evaluation.

Related Work
------------

* `S-CORE safety relevance proposal issue #3282 <https://github.com/eclipse-score/score/issues/3282>`_
* `S-CORE SRAC proof of concept PR #370 <https://github.com/eclipse-score/reference_integration/pull/370>`_
* `Policy-aware use-case documentation PR #393 <https://github.com/eclipse-score/reference_integration/pull/393>`_
* `S-CORE tooling mapping overlay PR #502 <https://github.com/eclipse-score/tooling/pull/502>`_
* `S-CORE metamodel flow PR #22 <https://github.com/eclipse-score/mcp-servers/pull/22>`_
* `SPDX 3.1-dev FunctionalSafety work <https://github.com/spdx/spdx-3-model/pulls?q=is%3Apr+1436+1442+1443+1458>`_
* `CycloneDX safety-model proposal PR #1120 <https://github.com/CycloneDX/specification/pull/1120>`_


