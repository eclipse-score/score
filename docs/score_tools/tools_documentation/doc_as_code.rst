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
   TCL1 = HIGH confidence here
   TCL2/3 = LOW confidence here
   See doc__platform_tool_management_plan

Doc-as-Code Tool Verification Report
====================================

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
  metamodel (``metamodel.yaml``), Bazel build files, source-code links
  (``sourcelinks_json``) and test results (``testlinks``).
* **Outputs:** HTML documentation (``_build/``), needs/traceability data
  (``needs.json``), coverage/linkage statistics (``metrics.json``).

.. mermaid::

   graph LR
      src@{ shape: docs, label: "RST/Markdown sources (+ assets)" }
      code@{ shape: docs, label: "C++/Rust/Python sources" }
      srclinks@{ shape: doc, label: "sourcelinks" }
      cfg@{ shape: docs, label: "Config (conf.py, metamodel.yaml, Bazel)" }
      tests@{ shape: docs, label: "Test results" }
      dac@{ shape: subproc, label: "Doc-as-Code" }
      html@{ shape: docs, label: "HTML docs" }
      needs@{ shape: doc, label: "needs.json" }
      metrics@{ shape: docs, label: "metrics.json" }
      gate@{ shape: subproc, label: "traceability_gate" }

      src --> dac
      code --> srclinks --> dac
      cfg --> dac
      tests --> dac
      dac --> html
      dac --> needs
      dac --> metrics
      metrics --> gate

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

Use cases were derived from the process requirements
and the docs-as-code
`Tool Requirements <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/requirements/requirements.html>`_.

The facts below are shared by use cases and only referenced in each
Malfunctions cell.

.. _basis-ci:

Build/CI behavior
   Builds run with ``-W``; any warning trips CI. The
   safety-relevant danger is the *silent* failure — a missing warning
   or a wrong output published undetected.
   A loud CI abort is safe: no wrong output enters the baseline.

.. _pr_review:

PR Review
   Repository contents are the source of truth
   and every change is reviewed by a committer
   (:need:`rl__contributor`, :need:`rl__committer`, :need:`doc_concept__wp_inspections`).
   Still, for silent wrong outputs the gated CI stays green.

.. _basis-ti1:

Derived-view
   The rendered output (HTML, architecture diagrams, cross-repo links, PR
   previews) is a derived view; the authoritative safety artifacts are the source-controlled work products.
   Traceability is enforced at the source level.
   Rendering/preview defects affect reviewer convenience, not safety evidence.


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
     - Confidence (automatic calculation)
   * - M1
     - | **Document metamodel enforcement** — enforce document types, mandatory attributes (id, status, security, safety, realizes), etc.
       | See, for example, :need:`gd_req__doc_attr_status`, :need:`gd_req__req_attr_uid`, :need:`gd_req__req_attr_safety`, :need:`gd_req__arch_attr_safety`, :need:`gd_req__req_check_mandatory`.
     - | `Silent false-negative <basis-ci_>`_, too-permissive
       | ``metamodel.yaml`` regex accepted with no guard, or a check bug skips a case.
     - yes
     - yes: `PR review <pr_review_>`_
     - | no: Qualify metamodel enforcement.
       |
       | No check against a permissive regex or check blind spot
       | (e.g. ``fault_id: ^.*$``, shipped as a *mandatory* option on ``feat_saf_fmea``/``comp_saf_fmea``).
     - yes (qualification)
     - low
   * - M2
     - | **Safety-critical linking enforcement**.
       | See :need:`gd_req__req_linkage_safety`.
     - | `Silent false-negative <basis-ci_>`_: Allow links which cannot be safe derivations.
     - yes
     - yes: `PR review <pr_review_>`_
     - | no: Qualify graph checks.
       |
       | The clearest gap is ``satisfied_by`` (and arguably ``covers``), which carry the same "target at least as safe" obligation as the checked ``fulfils``/``implements`` yet are unconstrained.
     - yes (qualification)
     - low
   * - M3
     - | **Requirements coverage statistics** — count, per requirement type, the requirements carrying a ``testlink``, compute link-coverage percentages.
       | See :need:`gd_req__verification_reporting`.
     - | `Silent wrong-output <basis-ci_>`_: a coverage statistic computed wrong.
     - yes
     - no
     - no: Qualify coverage statistics.
     - yes (qualification)
     - low
   * - M4
     - | **Architecture visualization** — generate architecture diagrams (PlantUML/Mermaid).
       | See :need:`gd_req__arch_viewpoints`.
     - | `Silent wrong-output <basis-ci_>`_: a diagram misrepresents the architecture.
     - yes
     - no
     - no: Qualify diagram generation.
     - yes (qualification)
     - low
   * - M5
     - | **Test linkage** — for each ``testcase`` need, resolve its ``partially_verifies``/``fully_verifies`` references against the needs set.
       | See :need:`gd_req__req_attr_testlink`, :need:`gd_req__verification_reporting`.
     - | `Silent wrong-output <basis-ci_>`_:
       | Safety case believes the requirement is tested where it is not.
     - yes
     - no
     - no: Qualify linkage statistics
     - yes (qualification)
     - low
   * - M6
     - | **Test reference check**.
       | See :need:`gd_req__req_attr_testlink`.
     - | `Silent wrong-output <basis-ci_>`_:
       | Test references an outdated/missing requirement.
     - yes
     - yes: `PR review <pr_review_>`_
     - no: Qualify test reference check
     - yes (qualification)
     - low
   * - M7
     - | **Documentation generation** — apart from the aspects **not covered by previous malfunctions**.
       | See :need:`gd_req__doc_attributes_manual`, :need:`gd_req__doc_attr_status`.
     - | Incomplete, outdated, or mis-rendered HTML.
     - no: `Derived-view <basis-ti1_>`_
     - no
     - n/a (TI1)
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
     - | **Source tampering** — applies to all tool use cases.
       | See :need:`gd_req__req_attr_security`, :need:`gd_req__arch_attr_security`, :need:`gd_req__req_linkage`,
       | :need:`gd_req__req_traceability`, :need:`gd_req__arch_linkage_security_trace`.
     - | An attacker with write access tampers with sources, configuration, or
       | extension code to weaken/disable security checks or inject misleading
       | content into published output.
     - yes
     - yes: `PR review <pr_review_>`_.
     - yes
     - no

Result
------
The final Tool Confidence Level is **LOW**,
the worst case across all use cases.

S-CORE Docs-as-Code requires qualification
for use in safety-related software development according to ISO 26262.


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
   extension.

Test cases
   Results and testcase metadata are published in
   `Tooling Verification <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/requirements/tooling_verification.html>`_.
   There is additional description about
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
     — ``score_metamodel``, ``score_metrics``,
     ``score_mounts``, ``score_cross_module_compatibility`` and other
     extensions.
   * `score_metamodel design <https://eclipse-score.github.io/docs-as-code/v7.0.1/internals/extensions/metamodel.html>`_
     — metamodel definition, validation checks (local, graph-based,
     prohibited-word), and the check lifecycle.
   * `Bazel macros reference <https://eclipse-score.github.io/docs-as-code/v7.0.1/reference/bazel_macros.html>`_
     — the ``docs()`` macro and its generated targets.
   * `Build commands <https://eclipse-score.github.io/docs-as-code/v7.0.1/reference/commands.html>`_
     — public and internal Bazel targets.
