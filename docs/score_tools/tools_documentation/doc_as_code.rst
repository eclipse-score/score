..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
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

.. doc_tool:: Doc-as-Code
   :id: doc_tool__doc_as_code
   :status: evaluated
   :version: 2
   :tool_version: v7.0.1
   :tcl: LOW
   :safety_affected: YES
   :security_affected: YES
   :realizes: wp__tool_verification_report[version==1]
   :tags: tool_management, tools_documentation

..
   Hint: S-CORE kind of inverts ISO 26262!
   TCL1 = HIGH and TCL2/3 = LOW
   See doc__platform_tool_management_plan

Doc-as-Code Verification Report
===============================

Introduction
------------

Scope and purpose
~~~~~~~~~~~~~~~~~
The S-CORE Docs-as-Code tool (Bazel module ``score_docs_as_code``) builds HTML
documentation from RST/Markdown sources — process description, requirements, and
traceability — and validates content against the S-CORE metamodel.

Inputs and outputs
~~~~~~~~~~~~~~~~~~
* **Inputs:** RST/Markdown sources, Sphinx configuration (``conf.py``), the S-CORE
  metamodel (``metamodel.yaml``), Bazel build files.
* **Outputs:** HTML documentation (``_build/``), needs/traceability data
  (``needs.json``), test/coverage reports.

Available information
~~~~~~~~~~~~~~~~~~~~~
* Repository: https://github.com/eclipse-score/docs-as-code
* Documentation: https://eclipse-score.github.io/docs-as-code/
* Bazel module name: ``score_docs_as_code``

Installation and integration
----------------------------

Installation
~~~~~~~~~~~~

The tool is consumed as a Bazel module. Declare the dependency in
``MODULE.bazel``::

    bazel_dep(name = "score_docs_as_code", version = "7.0.1")

and the S-CORE registry in ``.bazelrc``::

    common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
    common --registry=https://bcr.bazel.build

Invoke the ``docs()`` macro from the root ``BUILD`` file::

    load("@score_docs_as_code//:docs.bzl", "docs")
    docs(
        project = "My Project",
        project_url = "https://github.com/eclipse-score/my-project",
        source_dir = "docs",
    )

For local development, ``bazel run //:ide_support`` creates a Python virtual
environment (``.venv_docs``) with all Sphinx extensions pre-installed for IDE
support (Esbonio). The macro's build targets (``//:docs``, ``//:docs_check``,
``//:live_preview``, ``//:ide_support``) are documented in the docs-as-code
user guide.

Tool sources live in the ``docs-as-code`` repository under ``src/extensions/``
(Sphinx extensions) and ``docs.bzl`` (Bazel macros). The default metamodel is
bundled at
``@score_docs_as_code//src/extensions/score_metamodel:metamodel_yaml``
and may be overridden via the ``metamodel`` parameter.

Integration
~~~~~~~~~~~
The tool is the central documentation hub of the S-CORE Bazel toolchain, used
by all modules to build, check, and publish documentation.

Cross-module linking supports two modes:

- **External needs import:** reference another module's ``:needs_json`` target
  via the ``external_needs`` parameter of ``docs()`` to cross-reference need
  IDs across modules (e.g., ``:need:`gd_req__example_id```).
- **Bundle mounting:** mount another module's ``:docs_bundle`` target via the
  ``bundles`` parameter; the mounted sources join the consuming build, with
  placement controlled by ``mount_at`` (docname prefix) and ``attach_to``
  (toctree anchor).

Within a repository, Sphinx combines documentation sources (RST/Markdown),
needs JSON, source-code links (``sourcelinks_json``) and test metadata through
the S-CORE extensions (``score_metamodel``, ``score_metrics``, ``score_mounts``)
to produce HTML, ``needs.json`` and ``metrics.json``.

CI quality gates are provided by ``bazel run //:traceability_gate``, which reads
``metrics.json`` and enforces configurable thresholds (requirements-to-code,
requirements-to-test, fully-linked, tests-linked).

Environment
~~~~~~~~~~~
- **Operating system:** Linux — the S-CORE DevContainer (canonical,
  recommended), WSL2, or native.
- **Build system:** Bazel (``rules_python``, ``sphinxdocs``) fetches all
  toolchains and dependencies, including a remote JDK 17 for PlantUML diagrams
  when no local Java is present.

Safety evaluation
-----------------

Use cases were derived from the Documentation Management process
(:need:`doc_concept__documentation_process`, :need:`gd_req__doc_types`,
:need:`gd_req__doc_attributes_manual`) and the docs-as-code tool requirements
and capabilities.

All affected safety-relevant work products are ASIL-B in S-CORE, so every
safety-relevant harm chain ends in a systematic fault in the ASIL_B safety case.
The facts below are shared by use cases and only referenced in each
Malfunctions cell.

.. _basis-ci:

Build/CI behavior
   Builds run with ``-W``; any warning trips CI. The
   safety-relevant danger is the *silent* failure — a missing warning
   or a wrong output published undetected. A loud CI abort is not
   safety-relevant (TI0): no wrong output enters the baseline.

.. _basis-backstop:

Source of truth & backstop
   Documents reach ``valid`` only via source review
   (:need:`gd_req__doc_attr_status`). ``needs.json`` and module verification
   reports are the machine-readable verification evidence, with no automated
   re-derivation. For silent wrong outputs the gated CI stays green; only
   document review (:need:`gd_req__doc_attr_status`) and manual safety review
   catch the residual.

.. _basis-tcl:

TCL derivation rule
   Tool Impact = no (TI0) ⇒ **TCL HIGH**. Tool Impact = yes × Tool Error
   Detection = NO ⇒ **TCL LOW** (low because silent failures are not
   auto-detected — only document/manual review).

.. _basis-ti0:

TI0 derived-view rows (M1, M7)
   The rendered output (HTML, cross-repo links, PR previews) is a *derived
   view*; the authoritative safety artifacts are the source-controlled work
   products and machine-readable verification reports
   (:need:`gd_req__verification_reporting`). Safety classification and
   traceability are owned and enforced by M2–M6 at the source level.
   Rendering/preview defects affect reviewer convenience, not safety evidence.
   With no safety impact (TI0), the detection and further-measure columns are
   not applicable; they are recorded as ``n/a (TI0)``.


.. list-table:: S-CORE Docs-as-Code evaluation
   :header-rows: 1
   :widths: 1 2 8 2 6 4 2 2

   * - Malfunction identification
     - Use case description
     - Malfunctions
     - Impact on safety?
     - Impact safety measures available?
     - Impact safety detection sufficient?
     - Further additional safety measure required?
     - TCL (basis-tcl_)
   * - M1
     - | **Documentation generation** — build and publish HTML from
       | RST/Markdown sources.
       | See :need:`gd_req__doc_types`, :need:`gd_req__doc_attributes_manual`,
       | :need:`gd_req__doc_attr_status`.
     - | Incomplete, outdated, or mis-rendered HTML. TI0 derived-view row
       | (basis-ti0_).
     - no
     - no
     - n/a (TI0)
     - no
     - high
   * - M2
     - | **Document metamodel & attribute enforcement** — enforce document
       | types, mandatory attributes (id, status, security, safety, realizes),
       | the status lifecycle, and global need-ID uniqueness.
       | See :need:`gd_req__doc_types`, :need:`gd_req__doc_attributes_manual`,
       | :need:`gd_req__doc_attr_status`, :need:`gd_req__req_attr_uid`,
       | :need:`gd_req__req_check_mandatory`.
     - | Silent false-negative (basis-ci_): a too-permissive
       | ``metamodel.yaml`` regex (e.g. ``fault_id: ^.*$``, shipped as a
       | *mandatory* option on ``feat_saf_fmea``/``comp_saf_fmea``)
       | accepted with no guard, or a check bug skips a case.
       | (Duplicate IDs stay loud.)
       | *Harm chain:* ASIL_B element enters baseline misclassified (e.g. QM)
       | or with a broken lifecycle/missing link → its verification &
       | traceability (M4/M6) weakened.
       | *No backstop* for a permissive regex or check blind spot
       | (basis-backstop_).
     - yes
     - yes
     - no
     - yes (qualification)
     - low
   * - M3
     - | **Safety classification & safe-linking enforcement** — enforce the
       | ``safety`` attribute on documents/needs and safe linking of
       | safety-relevant elements.
       | See :need:`gd_req__req_attr_safety`, :need:`gd_req__arch_attr_safety`,
       | :need:`gd_req__req_check_mandatory`,
       | :need:`gd_req__req_linkage_safety`.
     - | Silent false-negative (basis-ci_). The tool enforces
       | *presence and format* of ``safety`` (mandatory on all safety-relevant
       | types — requirements, architecture elements, documents, verification
       | reports; optional only on ``tool_req``/``mod``) and *some*
       | safety-linking rules (graph checks on ``derived_from``, ``fulfils``,
       | and the safety variant of ``implements``). Residual *tool* gap:
       | safety links via relation types the graph checks do not cover
       | (``satisfied_by``, ``covers``, ``includes``, ``uses``,
       | ``belongs_to``, ``consists_of``).
       | *Operational context:* presence of ``safety`` is backstopped by M2's
       | mandatory-attribute check (basis-backstop_); the classification
       | *value* and safety-linking completeness across all relation types
       | have no automated backstop — only document review
       | (:need:`gd_req__doc_attr_status`) and manual safety review.
     - yes
     - yes
     - no
     - yes (qualification)
     - low
   * - M4
     - | **Requirements coverage statistics** — count, per requirement type, the
       | requirements carrying a ``source_code_link`` and/or a ``testlink``
       | (URLs to the implementing source / test), compute link-coverage
       | percentages, and write ``metrics.json`` consumed by the
       | ``traceability_gate`` CI quality gate (requirements-to-code,
       | requirements-to-test, fully-linked thresholds).
       | See :need:`gd_req__req_traceability`, :need:`gd_req__req_attr_impl`,
       | :need:`gd_req__req_attr_testlink`,
       | :need:`gd_req__verification_reporting`.
     - | Silent wrong-output (basis-ci_): a coverage statistic computed wrong.
       | A present ``source_code_link``/``testlink`` not counted (e.g.
       | ``is_non_empty`` rejects a valid value), or a requirement type dropped
       | by the type filter so its links vanish from ``metrics.json`` (and
       | ``safe_percent`` then reports the empty type as 100% by design).
       | *Harm chain:* ASIL_B requirement — or a whole requirement class —
       | reported code/test-linked, or dropped from the gate → CI quality gate
       | green → safety case believes implementation/test coverage exists where
       | it does not.
     - yes
     - yes
     - no
     - yes (qualification)
     - low
   * - M5
     - | **Architecture visualization & linkage validation** — generate
       | architecture diagrams (PlantUML/Mermaid) and validate architecture
       | linkage.
       | See :need:`gd_req__arch_viewpoints`,
       | :need:`gd_req__impl_diagram_check_id`,
       | :need:`gd_req__impl_diagram_linkage_id`,
       | :need:`gd_req__arch_attr_mandatory`.
     - | Silent wrong-output (basis-ci_): diagram misrepresents the
       | architecture or linkage validation misses a broken safety link.
       | *Harm chain:* ASIL_B architecture element mis-/un-linked → safety
       | architecture misrepresented, broken linkage hidden from review.
     - yes
     - yes
     - no
     - yes (qualification)
     - low
   * - M6
     - | **Test linkage & broken-reference detection** — for each ``testcase``
       | need, resolve its ``partially_verifies``/``fully_verifies``
       | references against the needs set, count tests linked to at least one
       | requirement (``tests-linked``), and list dangling references
       | (``broken_references``) in ``metrics.json`` for the
       | ``traceability_gate`` (tests-linked threshold).
       | See :need:`gd_req__req_attr_testlink`,
       | :need:`gd_req__verification_checks`,
       | :need:`gd_req__verification_reporting`.
     - | Silent wrong-output (basis-ci_): a ``partially_verifies``/
       | ``fully_verifies`` ref to an *absent* need not added to
       | ``broken_references`` (e.g. an ID-form mismatch in the
       | ``ref not in all_needs`` check) — a dangling test-to-requirement
       | reference silently dropped (and ``tests-linked`` still counts the
       | test, since it keys on ref presence, not resolution).
       | *Harm chain:* ASIL_B requirement's test coverage missing but the
       | broken reference unreported → safety case believes the requirement
       | is tested where it is not.
     - yes
     - yes
     - no
     - yes (qualification)
     - low
   * - M7
     - | **Cross-repository linking & PR preview generation** — link
       | documentation across repositories (versioned + latest) and generate
       | PR previews.
       | See :need:`gd_req__req_traceability` (cross-repository traceability).
     - | Versioned links resolve to the wrong revision, or PR previews built
       | from outdated sources. TI0 derived-view row (basis-ti0_).
       | Cross-repository traceability is owned and computed by M4 at the
       | source level.
     - no
     - no
     - n/a (TI0)
     - no
     - high

Security evaluation
-------------------
The threat model reduces to a single class: **source tampering**. The tool has
no runtime attack surface — it is a build-time Sphinx extension reading
source-controlled inputs and writing generated output.

.. list-table:: S-CORE Docs-as-Code security evaluation
   :header-rows: 1
   :widths: 1 2 8 2 6 4 2

   * - Threat identification
     - Use case description
     - Threats
     - Impact on security?
     - Impact security measures available?
     - Impact security detection sufficient?
     - Further additional security measure required?
   * - T1
     - | **Source tampering** — applies to all tool use cases: documentation
       | generation, metamodel/attribute enforcement, security classification
       | & linkage restriction, traceability & coverage, architecture
       | visualization & linkage validation, source/test traceability,
       | cross-repo linking & PR preview generation.
       | See :need:`gd_req__doc_types`, :need:`gd_req__req_attr_security`,
       | :need:`gd_req__arch_attr_security`, :need:`gd_req__req_linkage`,
       | :need:`gd_req__req_traceability`,
       | :need:`gd_req__arch_linkage_security_trace`,
       | :need:`gd_req__verification_reporting`.
     - | An attacker with write access tampers with sources, configuration, or
       | extension code to weaken/disable security checks or inject misleading
       | content into published output.
       | The attack always targets inputs, not the tool — whether the attacker
       | edits an RST/Markdown source, the ``metamodel.yaml`` regex, a graph-check rule,
       | or Python extension logic, it is one commit.
       | *Harm chain:* misleading content reaches published docs, or
       | security-relevant needs enter the baseline without a valid
       | ``security`` classification or with broken/disallowed links →
       | security argument incomplete, traceability/coverage falsely complete
       | → incorrect security decisions.
     - yes
     - | Git access control, mandatory PR review with reviewer
       |   (:need:`gd_req__doc_reviewer`) + approver
       |   (:need:`gd_req__doc_approver`), ``status=valid`` gate
       |   (:need:`gd_req__doc_attr_status`, :need:`gd_guidl__documentation`),
       |   known-provenance tenet (:need:`tenet__trust__tt-provenance`), plus
       |   structural metamodel enforcement (``security: ^(YES|NO)$``
       |   mandatory, security graph check) and the metamodel test suite
     - yes
     - no

Result
~~~~~~
The final Tool Confidence Level is TCL **LOW**,
the worst case across all use cases.

S-CORE Docs-as-Code requires qualification
for use in safety-related software development according to ISO 26262.

Recommended improvements for future versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The residual risk in M2–M6 (TCL LOW) stems from Tool Error Detection being
*low*: silent failures are not auto-detected, only caught by document/manual
review. The following improvements would raise Tool Error Detection and, once
verified, could raise the TCL to HIGH:

* **Extend safety/security graph checks to all relation types** (M3, M5). The
  metamodel defines five graph checks; the safety/security-relevant ones
  constrain only ``derived_from``, ``fulfils`` and the safety variant of
  ``implements`` (``complies`` covers the ASPICE-40 workproduct rule, not
  safety/security). ``satisfied_by``, ``covers``, ``includes``, ``uses``,
  ``belongs_to``, ``consists_of``, etc. remain unchecked. A safety-relevant
  element linked to a non-safety one via *any* relation should be flagged,
  closing the gap where a wrong classification or disallowed link enters the
  baseline undetected.

* **Add cross-contamination detection** (M3). Flag any need with
  ``safety: QM`` linked (via any relation) to one with ``safety: ASIL_B`` —
  and analogously for ``security``. This does not decide whether a single
  classification is semantically correct (still a review task) but catches the
  common case of an inconsistent classification across a link — the
  safety/security analog of the existing
  ``check_valid_only_links_to_valid`` status check, which is not yet present.

* **Negative-test fixtures for permissive-metamodel regressions** (M2, M3).
  The file-based framework (``test_rules_file_based.py``) with
  ``:expect:``/``:expect_not:`` already makes regressions that silence a
  missing-mandatory or disallowed-link check fail CI. The remaining gap is a
  fixture asserting that a deliberately over-permissive regex (e.g.
  ``status: ^.*$``) is *rejected* — coupled to the permissive-regex guard
  below (until that guard exists, there is nothing to assert).

* **Guard against permissive regexes in the metamodel** (M2). A linter
  rejecting ``^.*$`` or empty-accepting patterns for *mandatory* attribute
  definitions, so a misconfigured ``metamodel.yaml`` is caught at the
  metamodel level. The guard would catch real defects already in the shipped
  metamodel: ``feat_saf_fmea`` and ``comp_saf_fmea`` declare ``fault_id:
  ^.*$`` as a *mandatory* option — yet it carries the req-Id
  ``tool_req__docs_saf_attr_fmea_fault_id``, i.e. a genuine requirement it is
  meant to enforce, and the ``^.*$`` pattern accepts even the empty string.
  That it diverges from the sibling ``plat_saf_dfa.failure_id: ^.+$`` (non-empty)
  for the same concept shows these are not deliberate free-form fields but
  accidental permissive patterns. (``^.*$`` is also used legitimately on
  *optional* options such as ``author``/``approver``/``reviewer``/``hash``, so
  the guard must scope to mandatory definitions to avoid noise.)

* **Expected-output tests on ``metrics.json`` for the coverage/linkage
  computation** (M4, M6). M4 and M6 fail via *wrong computation* —
  ``score_metrics`` silently miscounts and writes the wrong ``metrics.json``
  with no warning: a present ``source_code_link``/``testlink`` not counted, a
  requirement type dropped by the filter so its links vanish, or a dangling
  ``testcase`` ``*_verifies`` ref not listed in ``broken_references``. The
  existing ``:expect:``/``:expect_not:`` framework checks build *warnings*,
  and ``score_metrics`` emits none on miscounts, so it cannot catch this class
  — the improvement is a new harness that rebuilds ``metrics.json`` on
  representative and deliberately broken RST/Markdown inputs and diffs it against a
  checked-in expected output, asserting the negative paths (a dropped type
  must not vanish from ``metrics.json``, a dangling ref must land in
  ``broken_references``) and the counting invariants (``fully_linked`` ≤
  ``with_code_link``/``with_test_link``, per-type totals sum to the overall).
  This raises Tool Error Detection for the wrong-computation class.

**Optional Section for Tool Qualification**
-------------------------------------------
Based on method: validation of the software tool

Requirements and testing aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tool requirements
   Defined in the docs-as-code internal documentation:
   `Tool Requirements <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/requirements/requirements.html>`_.
   Each ``tool_req`` specifies a mandatory attribute enforcement, linkage
   rule, or metamodel check implemented by the ``score_metamodel`` Sphinx
   extension. The full capability list is in
   `Capabilities <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/requirements/capabilities.html>`_.

Test cases
   Results and testcase metadata are published in
   `Tooling Verification <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/requirements/tooling_verification.html>`_;
   the extension's test infrastructure is described in
   `File-Based Testing <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/extensions/rst_filebased_testing.html>`_.

Requirements coverage
   Per-requirement test and code linkage is tracked in
   `Requirement Test Coverage <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/requirements/requirement_coverage.html>`_,
   using the same ``score_metrics`` calculations as the CI quality gates
   (``bazel run //:traceability_gate``, `the output metrics.json <https://eclipse-score.github.io/docs-as-code/v7.0.1/metrics.json>`__).

Analysis perspective
~~~~~~~~~~~~~~~~~~~~

Architectural design
   The internal architecture is described via its Sphinx extensions and Bazel
   macros:

   * `Extensions overview <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/extensions/index.html>`_
     — ``score_metamodel``, ``score_metrics``, ``score_source_code_linker``,
     ``score_mounts``, ``score_cross_module_compatibility`` and other
     extensions.
   * `score_metamodel design <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/extensions/metamodel.html>`_
     — metamodel definition, validation checks (local, graph-based,
     prohibited-word), and the check lifecycle.
   * `Bazel macros reference <https://eclipse-score.github.io/docs-as-code/v7.0.1/reference/bazel_macros.html>`_
     — the ``docs()`` macro and its generated targets.
   * `Build commands <https://eclipse-score.github.io/docs-as-code/v7.0.1/reference/commands.html>`_
     — public and internal Bazel targets.
