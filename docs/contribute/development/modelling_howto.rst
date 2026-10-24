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

.. document:: Feature & Component Modelling How-To
   :id: doc__modelling_howto
   :status: valid
   :safety: QM
   :security: NO
   :realizes: wp__requirements_proc_tool

Feature & Component Modelling How-To
####################################

This guide walks you, step by step, through **what to model at the
feature level and at the component / module level**, **in which
repository**, **with which sphinx-needs directives**, and **how the
elements must be linked** so that the docs-as-code build, the safety /
security graph checks and the verification dashboard accept the result.

The canonical reference for this how-to is the **baselibs** feature
and its modules (``docs/features/baselibs/`` and
``docs/modules/baselibs/`` in the build). All other features /
modules should follow the same pattern.

Key rule for the repository split:

- The **score repository owns the contract** of a feature --
  ``stkh_req``, ``feat_req``, ``feat`` and ``logic_arc_int(_op)``.
- The **module repository owns the realisation** of the feature --
  ``feat_arc_sta`` / ``feat_arc_dyn``, ``mod`` / ``mod_view_sta``,
  ``comp`` / ``comp_arc_sta``, ``comp_req`` and all component
  inspections.

Scope -- the reduced metamodel actually in use today:

- **Feature side:** ``feat``, ``feat_req``, ``feat_arc_sta``,
  ``feat_arc_dyn``, ``logic_arc_int``, ``logic_arc_int_op``.
- **Component / module side:** ``mod``, ``mod_view_sta``, ``comp``,
  ``comp_req``, ``comp_arc_sta``.
- **Roots / side inputs:** ``stkh_req``, ``aou_req``.
- **Verification:** ``testcase`` (auto-generated from JUnit XML).
- **Inspections:** ``chklst_req_inspection``, ``chklst_arc_inspection``,
  ``chklst_impl_inspection`` -- one per layer / per file.

Dormant element types
(``dd_sta``, ``dd_dyn``, ``sw_unit*``,
``real_arc_int*``, ``comp_arc_dyn``, ``*_saf_*``,
``mod_view_dyn``, ``plat_saf_dfa``) are mentioned only where you may
need to add them later.

.. contents::
   :local:
   :depth: 2


Where things live (repository map)
**********************************

Two repository tiers are involved.

**score** (this repo)
   Owns the **feature contract**, i.e. everything that a downstream
   consumer must be able to rely on without knowing the realisation:

   - stakeholder requirements (``stkh_req``),
   - platform-level assumptions (``aou_req``),
   - per-feature ``feat_req``,
   - the feature handle ``feat`` and its published interfaces
     ``logic_arc_int`` / ``logic_arc_int_op``,
   - the feature requirements-inspection checklist
     (``chklst_req_inspection`` for the feature).

**process_description** (imported)
   Pulled in via sphinx-needs ``[[needs.external_needs]]`` in
   ``docs/ubproject.toml``. Owns ``wp__*``, ``gd_*``, ``tool_req__*``.
   You only *link* to them, never edit them from score.

**module repositories** (e.g. ``baselibs``, ``logging``, ``feo``, ``persistency``, …)
   Each module repository owns the **realisation** of the feature(s)
   it builds:

   - the architectural views of the feature
     (``feat_arc_sta`` and ``feat_arc_dyn``) plus the architecture
     inspection (``chklst_arc_inspection``) for the feature -- these
     diagrams describe *how this module realises the feature*, so
     they belong to the module, not to score,
   - the **module documentation** (``mod``, ``mod_view_sta``,
     module safety plan / package, release note, manual,
     verification report),
   - one folder per **component** with its requirements
     (``comp_req``), architecture (``comp``, ``comp_arc_sta``),
     optional safety analyses and the detailed-design checklist,
   - all **component-level inspection checklists**
     (``chklst_req_inspection``, ``chklst_arc_inspection``,
     ``chklst_impl_inspection``).

   The module repo **never** redefines ``feat``, ``feat_req`` or
   ``logic_arc_int*`` -- it only *links to them* through
   ``belongs_to`` (``feat_arc_*`` → ``feat``,
   ``comp`` → ``feat``), ``fulfils`` (``feat_arc_*`` → ``feat_req``),
   ``satisfies`` (``comp_req`` → ``feat_req``) and
   ``implements`` / ``uses`` (``comp`` → ``logic_arc_int``).

.. note::

   Multi-repository docs **are** supported. ``baselibs``,
   ``logging``, ``feo``, … are pulled into the score build through
   the bzlmod dependency graph and sphinx-needs
   ``[[needs.external_needs]]`` (see ``docs/ubproject.toml`` for the
   ``score_process`` entry; module repos are wired up the same way).
   The cross-repo links (``belongs_to``, ``fulfils``, ``satisfies``,
   ``implements``) resolve by need ID across the aggregated graph.
   The trees shown below therefore live in their respective
   repositories *for real* -- they are not mirrored copies.

File-system layout (the baselibs pattern -- mandatory):

.. code-block:: text

   score/                                                 # SCORE REPO
   └── docs/
       ├── requirements/
       │   └── stakeholder/index.rst                      # .. stkh_req::
       ├── platform_assumptions/index.rst                 # platform aou_req
       └── features/<feature>/                            # feature contract
           ├── index.rst                                  # .. document:: + abstract / motivation
           └── docs/
               ├── requirements/
               │   ├── index.rst                          # .. feat_req::
               │   └── chklst_req_inspection.rst
               └── architecture/
                   └── index.rst                          # .. feat::,
                                                          # .. logic_arc_int(_op)::

   <module-repo>/                                         # MODULE REPO
   ├── docs/features/<feature>/                           # feature realisation views
   │   └── docs/
   │       └── architecture/
   │           ├── index.rst                              # .. feat_arc_sta::,
   │           │                                          # .. feat_arc_dyn::
   │           └── chklst_arc_inspection.rst
   │
   ├── docs/features/<feature>/docs/safety_analysis/      # optional, ASIL only
   │   ├── fmea.rst                                       # .. feat_saf_fmea::
   │   └── dfa.rst                                        # .. feat_saf_dfa::
   │
   └── docs/modules/<module>/                             # module + components
       ├── index.rst                                      # toctree for module + components
       ├── docs/
       │   ├── index.rst                                  # .. mod::, .. mod_view_sta::
       │   ├── release/release_note.rst
       │   ├── safety_mgt/{index,module_safety_plan,
       │   │                module_safety_package_fdr,
       │   │                module_safety_plan_fdr,
       │   │                module_codeowners,
       │   │                module_safety_analysis_fdr}.rst
       │   ├── manual/safety_manual.rst
       │   └── verification/module_verification_report.rst
       │
       └── <component>/docs/                              # one folder per component
           ├── index.rst                                  # component toctree
           ├── requirements/
           │   ├── index.rst                              # .. comp_req::
           │   └── chklst_req_inspection.rst
           ├── architecture/
           │   ├── index.rst                              # .. comp::, .. comp_arc_sta::
           │   └── chklst_arc_inspection.rst
           ├── safety_analysis/                           # optional, ASIL only
           │   ├── fmea.rst                               # .. comp_saf_fmea::
           │   └── dfa.rst                                # .. comp_saf_dfa::
           └── detailed_design/
               └── chklst_impl_inspection.rst

.. note::

   Every directive sits inside a ``.. document::`` block at the top of
   the file (``:realizes: wp__feature_arch``,
   ``wp__requirements_feat``, ``wp__component_arch``, …). The
   ``document`` need carries the safety / security tags of the *file*
   and is what the inspection checklists fulfil.


Step-by-step at the feature level
*********************************

Goal: from a stakeholder need to a feature that publishes one or more
**logical interfaces** for downstream components to consume.

Step 1 -- Anchor in the stakeholder requirements (score repo)
=============================================================

If the user need is not yet captured, add it once in
``score/docs/requirements/stakeholder/index.rst``:

.. code-block:: rst

   .. stkh_req:: Base libraries
      :id: stkh_req__functional_req__base_libraries
      :reqtype: Functional
      :security: NO
      :safety: QM
      :status: valid

      The platform shall provide reusable base libraries.

Rules:

- One ``stkh_req`` per user concern, never per implementation detail.
- No outgoing links -- this is a root.
- ``:safety:`` may be ``QM`` even if a downstream feature is ``ASIL_B``;
  the graph check only forbids ``QM → ASIL`` *into* the safety chain,
  not the other way around.

Step 2 -- Create the feature directory in the score repo
========================================================

The **feature contract** (requirements + published interfaces) is
owned by score. In the **score repo** create:

.. code-block:: text

   score/docs/features/<feature>/
   ├── index.rst                                # document + toctree
   └── docs/
       ├── requirements/
       │   ├── index.rst                        # feat_req
       │   └── chklst_req_inspection.rst
       └── architecture/
           └── index.rst                        # feat, logic_arc_int(_op)

Note what is **not** here: ``feat_arc_sta`` / ``feat_arc_dyn`` and
the architecture inspection do **not** live in score -- they belong
to the realising module (Step 6).

``index.rst`` declares the feature *document*, abstract, motivation
and the toctree -- not the ``feat`` directive itself (which goes in
``docs/architecture/index.rst`` in Step 4). The baselibs file does it
like this:

.. code-block:: rst

   .. _<feature>_feature:

   <Feature Title>
   ###############

   .. document:: <Feature>
      :id: doc__<feature>
      :status: valid
      :safety: ASIL_B
      :tags: feature_request
      :security: YES
      :realizes: wp__feat_request

   .. toctree::
      :hidden:

      docs/requirements/index.rst
      docs/requirements/chklst_req_inspection.rst
      docs/architecture/index.rst

   Abstract / Motivation / Rationale / Safety Impact / …
   =====================================================

Step 3 -- Write the feature requirements (``feat_req``)
=======================================================

In ``docs/features/<feature>/docs/requirements/index.rst``:

.. code-block:: rst

   .. document:: <Feature> Requirements
      :id: doc__<feature>_requirements
      :status: valid
      :safety: ASIL_B
      :security: YES
      :realizes: wp__requirements_feat

   .. feat_req:: Multi-Language APIs
      :id: feat_req__<feature>__multi_language_apis
      :reqtype: Functional
      :security: NO
      :safety: ASIL_B
      :satisfies: stkh_req__functional_req__base_libraries
      :status: valid

      The feature shall provide APIs for C++, Rust, or both.

   .. needextend:: is_external == False and "__<feature>" in id
      :+tags: <feature>

Mandatory links:

- ``:satisfies:`` |to| at least one ``stkh_req``
  (schema: ``mandatory_links: satisfies: stkh_req``).

Optional links you will need in practice:

- ``:covers:`` |to| ``aou_req`` if the requirement is rooted in an
  assumption of use rather than a stakeholder requirement.

Graph rule to remember:

- A ``feat_req`` with ``:safety: ASIL_B`` may not link to a stakeholder
  need that breaks the safety propagation. The check is
  ``tool_req__docs_common_attr_safety_link_check``.

Tag the requirements file in
``docs/features/<feature>/docs/requirements/chklst_req_inspection.rst``
with a ``.. chklst_req_inspection::`` need (same id pattern as
``baselibs``).

Step 4 -- Declare the feature node and the logical interfaces
=============================================================

In the **score** repo, in
``docs/features/<feature>/docs/architecture/index.rst``:

.. code-block:: rst

   .. _<feature>_architecture:

   Architecture
   ============

   .. document:: <Feature> Architecture
      :id: doc__<feature>_architecture
      :status: valid
      :safety: ASIL_B
      :security: YES
      :realizes: wp__feature_arch

   .. feat:: <Feature>
      :id: feat__<feature>
      :security: YES
      :safety: ASIL_B
      :status: valid
      :provides: logic_arc_int__<feature>__<iface_a>,
                 logic_arc_int__<feature>__<iface_b>

   Interfaces
   ----------

   .. logic_arc_int:: <iface_a>
      :id: logic_arc_int__<feature>__<iface_a>
      :security: YES
      :safety: ASIL_B
      :status: valid

   .. logic_arc_int_op:: open
      :id: logic_arc_int_op__<feature>__open
      :security: YES
      :safety: ASIL_B
      :status: valid
      :included_by: logic_arc_int__<feature>__<iface_a>

The ``feat`` node is the *blackbox handle* of the feature; the only
links it carries are interface declarations:

- ``:provides:`` -- the logical interfaces this feature exposes.
- ``:uses:`` -- the logical interfaces of other features this one
  depends on (use sparingly at the feature node; ``:uses:`` is mostly
  carried by the components in Step 8).
- ``:includes:`` -- only when grouping sub-interfaces.

Rules:

- ``logic_arc_int_op.included_by`` is **mandatory**.
- Match the safety / security level of the providing feature; the
  graph check ``tool_req__docs_arch_link_qm_to_safety_req`` will fail
  the build otherwise.
- No ``feat_arc_sta`` / ``feat_arc_dyn`` here -- those views describe
  *how a particular module realises the feature* and therefore live
  in the module repository (Step 6).

Step 5 -- File the feature requirements inspection
==================================================

In the **score** repo, next to the requirements file:
``docs/features/<feature>/docs/requirements/chklst_req_inspection.rst``
-- realises ``wp__requirements_feat_inspection``.

Do **not** hand-write this file. Use the **Requirements Inspection**
agent described in the sub-section below -- it scaffolds the file
from the baselibs template, runs the per-item analysis recipes
bundled in the ``req-inspection-checklist`` skill and fills the
``Passed`` column where the evidence is automatable.

.. _modelling_howto_inspection_agent:

Generating inspection checklists with the Requirements Inspection agent
-----------------------------------------------------------------------

Don't hand-write ``chklst_req_inspection.rst`` (and, once the agent
grows the same recipe for architecture and implementation, the other
two checklist files either). Use the **Requirements Inspection**
agent shipped in this repo:

- Agent definition: ``.github/agents/req-inspection.agent.md``
- Skill (templates, per-item grep recipes, verdict rules):
  ``.github/skills/req-inspection-checklist/``

The agent operates on the patterns established by ``baselibs`` and
``persistency`` and follows a fixed approach: load the skill, locate
the feature's ``requirements/`` directory, read ``:safety:`` /
``:security:`` from ``index.rst``, create or fill the checklist,
run every per-item analysis, register the file in the toctree if
it was new, look up the tracking issue, and flip ``:status: draft``
to ``valid`` only when every row has a verdict.

How to start the agent
^^^^^^^^^^^^^^^^^^^^^^

Use the GitHub Copilot CLI:

.. code-block:: bash

   copilot --allow-all-tools --agent "Requirements Inspection" -p "<feature-name>"

Example:

.. code-block:: bash

   copilot --allow-all-tools --agent "Requirements Inspection" -p "lifecycle"

The argument to ``-p`` is the **feature name only** (not a path,
not the full ``stkh_req`` ID). The agent works on a single
feature per run -- do not pass several at once.

.. note::

   Today the agent only handles **feature-level** requirements
   inspections (``feat_req`` under ``docs/features/<feature>/`` in
   the score repo). Component-level ``comp_req`` inspections under
   ``docs/modules/<module>/<component>/`` in module repositories
   are **not** yet supported -- those checklists still have to be
   written by hand from the
   `folder template <https://github.com/eclipse-score/process_description/blob/v1.5.4/process/folder_templates/modules/module_name/component_name/docs/requirements/chklst_req_inspection.rst>`_.

What the agent will not do
^^^^^^^^^^^^^^^^^^^^^^^^^^

The constraints baked into the agent (see
``.github/agents/req-inspection.agent.md``):

- It does **not** invent or alter the standard checklist item IDs or
  acceptance criteria -- those live in the skill.
- It does **not** flip ``:status: draft`` → ``:status: valid`` until
  every ``Passed`` cell is ``Yes`` / ``No`` / ``N/A`` (with a
  remark) or explicitly empty with a documented expert-review
  remark.
- It does **not** mark items as ``Yes`` when the evidence requires a
  human role (safety expert, test expert, TARA) and that evidence
  is not present -- it leaves the cell empty and records the gap in
  ``Remarks``.
- It does **not** modify unrelated features in the same run.

If you need the same automation for the **architecture** or
**implementation** inspections, file an issue against the agent --
the skill's per-item recipes are extensible to those two checklist
flavours, but they are not implemented yet. Until then,
``chklst_arc_inspection.rst`` and ``chklst_impl_inspection.rst`` are
still hand-written from the baselibs template.

When to invoke the agent
^^^^^^^^^^^^^^^^^^^^^^^^

- New feature: as soon as ``feat_req`` has at least one valid entry.
- New component: as soon as ``comp_req`` has at least one valid
  entry (and once the agent supports it -- see above).
- Existing feature with ``:status: draft`` and empty ``Passed``
  cells: re-run; the agent re-reads the analysis and only fills
  what changed.
- Verifying coverage of an existing checklist: invoke and read the
  agent's status report; if it reports ``:status: valid``, no rows
  were touched.

What you do *not* do in the score repo
======================================

- No ``feat_arc_sta`` / ``feat_arc_dyn`` -- they live in the module
  repo (Step 6).
- No ``chklst_arc_inspection`` for the feature -- same reason.
- No ``comp``, no ``comp_req``, no ``comp_arc_*``, no ``mod*``.
- No FMEA / DFA if you are pre-ASIL. ``feat_saf_fmea`` /
  ``feat_saf_dfa`` only land once the safety plan calls for them,
  and they live in the module repo.


Step-by-step at the module / component level
********************************************

Goal: realise the feature in one or more components, group them under
a module and trace every ``comp_req`` back to the score-owned
``feat_req``. **All artefacts in this section live in the module
repository**, including the architectural views of the feature.

Step 6 -- Add the feature architecture views in the module repo
===============================================================

The architectural views describe *how this module realises the
feature*, so they live in the module repo at exactly the same
file-system path the score side uses:
``docs/features/<feature>/docs/architecture/index.rst`` (module repo).

.. code-block:: rst

   .. document:: <Feature> Realisation
      :id: doc__<feature>_arch_realisation
      :status: valid
      :safety: ASIL_B
      :security: YES
      :realizes: wp__feature_arch

   .. feat_arc_sta:: Static Architecture
      :id: feat_arc_sta__<feature>__static
      :security: YES
      :safety: ASIL_B
      :status: valid
      :belongs_to: feat__<feature>
      :includes: logic_arc_int__<feature>__<iface_a>
      :fulfils: feat_req__<feature>__multi_language_apis

      .. uml:: _assets/static_view.puml

   .. feat_arc_dyn:: Open / Close sequence
      :id: feat_arc_dyn__<feature>__open_close
      :security: YES
      :safety: ASIL_B
      :status: valid
      :belongs_to: feat__<feature>
      :fulfils: feat_req__<feature>__multi_language_apis

      .. uml:: _assets/open_close_seq.puml

Mandatory links:

- ``feat_arc_sta``: ``belongs_to: feat``,
  ``fulfils: feat_req | aou_req``, ``includes: logic_arc_int(_op)``.
- ``feat_arc_dyn``: ``belongs_to: feat``, ``fulfils: feat_req``.

Note: ``belongs_to`` / ``fulfils`` / ``includes`` cross the
repository boundary by ID -- they resolve to the score-owned
``feat``, ``feat_req`` and ``logic_arc_int`` because the score build
is the consumer of both trees.

File the feature architecture inspection
----------------------------------------

In the **module** repo, next to the architecture file:
``docs/features/<feature>/docs/architecture/chklst_arc_inspection.rst``
-- realises ``wp__feature_arch_inspection``.

The Requirements Inspection agent does not generate this file yet
(see :ref:`modelling_howto_inspection_agent`). Copy it from the
`feature architecture checklist folder template <https://github.com/eclipse-score/process_description/blob/v1.5.4/process/folder_templates/features/feature_name/architecture/chklst_arc_inspection.rst>`_
and adapt the ``:id:`` to
``chklst_arc_inspection__<feature>``.

Step 7 -- Create the module directory
=====================================

In your module repo at ``docs/modules/<module>/``:

.. code-block:: text

   docs/modules/<module>/
   ├── index.rst                          # toctree only
   ├── docs/                              # module-level docs
   │   ├── index.rst                      # mod, mod_view_sta
   │   ├── release/release_note.rst
   │   ├── safety_mgt/…
   │   ├── manual/safety_manual.rst
   │   └── verification/module_verification_report.rst
   └── <component>/docs/                  # one folder per component
       ├── index.rst                      # component toctree
       ├── requirements/{index, chklst_req_inspection}.rst
       ├── architecture/{index, chklst_arc_inspection}.rst
       ├── safety_analysis/{fmea, dfa}.rst              # ASIL only
       └── detailed_design/chklst_impl_inspection.rst

``docs/modules/<module>/index.rst`` is just navigation
(baselibs / logging pattern):

.. code-block:: rst

   <Module> Module
   ###############

   .. toctree::
      :titlesonly:
      :maxdepth: 2

      ./docs/index

   Components
   ==========

   .. toctree::
      :titlesonly:
      :maxdepth: 1
      :glob:

      ./*/docs/index

Step 8 -- Declare the module (``mod`` / ``mod_view_sta``)
=========================================================

In ``docs/modules/<module>/docs/index.rst``:

.. code-block:: rst

   .. mod:: <Module>
      :id: mod__<module>
      :status: valid
      :safety: ASIL_B
      :security: YES
      :includes: comp__<module>__<comp_a>, comp__<module>__<comp_b>

   .. mod_view_sta:: <Module>
      :id: mod_view_sta__<module>__<module>
      :includes: comp__<module>__<comp_a>, comp__<module>__<comp_b>
      :belongs_to: mod__<module>

      .. needarch::
         :scale: 50
         :align: center

         {{ draw_module(need(), needs) }}

   Module Documents
   ================

   .. toctree::
      :maxdepth: 2
      :titlesonly:

      release/release_note
      safety_mgt/index
      manual/safety_manual
      verification/module_verification_report

Rules:

- ``mod.includes`` is mandatory and must list every ``comp`` of the
  module.
- ``mod_view_sta`` carries the diagram; ``mod`` carries the data.
- The ``draw_module`` Jinja helper from
  ``score_sphinx_bundle`` renders the static view automatically from
  the linked components -- prefer it over a hand-drawn PlantUML where
  possible (this is what baselibs / logging / feo use).

Step 9 -- Declare the component (``comp`` / ``comp_arc_sta``)
=============================================================

In ``docs/modules/<module>/<component>/docs/architecture/index.rst``:

.. code-block:: rst

   .. document:: <Component> Architecture
      :id: doc__<module>_<component>_architecture
      :status: valid
      :safety: ASIL_B
      :security: YES
      :realizes: wp__component_arch

   Component Architecture
   **********************

   .. comp:: <module>::<component>
      :id: comp__<module>__<component>
      :security: YES
      :safety: ASIL_B
      :status: valid
      :belongs_to: feat__<feature>
      :implements: logic_arc_int__<feature>__<iface_a>
      :uses: logic_arc_int__logging__logging,
             logic_arc_int__baselibs__json

      .. needarch::
         :scale: 50
         :align: center

         {{ draw_component(need(), needs) }}

   .. comp_arc_sta:: Static Architecture
      :id: comp_arc_sta__<module>__<component>__static
      :security: YES
      :safety: ASIL_B
      :status: valid
      :belongs_to: comp__<module>__<component>
      :fulfils: comp_req__<module>__<component>__store_read

      .. uml:: _assets/comp_static.puml

If your component **owns** a logical interface (rather than just
implements one declared at the feature level -- this is how the
``logging`` and several baselibs components do it), declare the
``logic_arc_int`` / ``logic_arc_int_op`` in the **same** file:

.. code-block:: rst

   .. logic_arc_int:: <component>
      :id: logic_arc_int__<feature>__<component>
      :security: YES
      :safety: ASIL_B
      :status: valid

   .. logic_arc_int_op:: <op>
      :id: logic_arc_int_op__<feature>__<op>
      :security: YES
      :safety: QM
      :status: valid
      :included_by: logic_arc_int__<feature>__<component>

Mandatory links on the ``comp``:

- ``:belongs_to:`` |to| ``feat`` -- the component declares which
  **feature** it realises.

Typical optional links:

- ``:implements:`` |to| one or more ``logic_arc_int`` provided at
  runtime.
- ``:uses:`` |to| logical interfaces of other features
  (``logging``, ``tracing``, ``baselibs`` are the dominant
  consumers).
- ``:consists_of:`` |to| sub-components if you decompose further.

Graph rules:

- A ``QM`` component may not implement an ``ASIL_B`` logical interface
  (``tool_req__docs_arch_link_qm_to_safety_req``).
- A security component (``security: YES``) may only link to security
  needs (``tool_req__docs_arch_link_security``).

Step 10 -- Write the component requirements (``comp_req``)
==========================================================

In ``docs/modules/<module>/<component>/docs/requirements/index.rst``:

.. code-block:: rst

   .. document:: <Component> Requirements
      :id: doc__<module>_<component>_requirements
      :status: valid
      :safety: ASIL_B
      :security: YES
      :realizes: wp__requirements_comp

   .. comp_req:: Persist value round-trip
      :id: comp_req__<module>__<component>__store_read
      :reqtype: Functional
      :security: NO
      :safety: ASIL_B
      :status: valid
      :belongs_to: comp__<module>__<component>
      :satisfies: feat_req__<feature>__store_data

Mandatory links:

- ``:satisfies:`` |to| at least one ``feat_req``.
- ``:belongs_to:`` |to| the parent ``comp``.

Optional:

- ``:covers:`` |to| an ``aou_req`` (platform or component-local).

ASIL completeness:

- For each ``comp_req`` with ``:safety: ASIL_B`` set the
  ``complete test coverage`` attribute once the test set is judged
  sufficient.

Step 11 -- File the component inspections
=========================================

Three checklist files, one per artefact:

- ``…/<component>/docs/requirements/chklst_req_inspection.rst``
  realises ``wp__requirements_comp_inspection``.
- ``…/<component>/docs/architecture/chklst_arc_inspection.rst``
  realises ``wp__component_arch_inspection``.
- ``…/<component>/docs/detailed_design/chklst_impl_inspection.rst``
  realises ``wp__sw_implementation_inspection``.

All three use the same ``.. chklst_<…>_inspection::`` directive
declared in the metamodel. Copy the official folder templates from
``process_description`` (pinned to the version score consumes via
``bazel_dep(name = "score_process", …)`` in ``MODULE.bazel`` -- at
the time of writing, ``v1.5.4``) and adapt the ``:id:`` to
``chklst_<…>_inspection__<module>_<component>``:

- `chklst_req_inspection.rst <https://github.com/eclipse-score/process_description/blob/v1.5.4/process/folder_templates/modules/module_name/component_name/docs/requirements/chklst_req_inspection.rst>`_
- `chklst_arc_inspection.rst <https://github.com/eclipse-score/process_description/blob/v1.5.4/process/folder_templates/modules/module_name/component_name/docs/architecture/chklst_arc_inspection.rst>`_
- `chklst_impl_inspection.rst <https://github.com/eclipse-score/process_description/blob/v1.5.4/process/folder_templates/modules/module_name/component_name/docs/detailed_design/chklst_impl_inspection.rst>`_

The full template tree (per-feature and per-component skeletons,
including safety / security planning, module safety plan, etc.) is
browsable in the source under
`process/folder_templates/ <https://github.com/eclipse-score/process_description/tree/v1.5.4/process/folder_templates>`_.

Safety analyses (``…/<component>/docs/safety_analysis/{fmea,dfa}.rst``)
are added only when the module safety plan calls for them
(``comp_saf_fmea`` / ``comp_saf_dfa``).

Step 12 -- Link source code back to the requirement
===================================================

Source code is linked back to requirements (typically ``comp_req``) by
the **docs-as-code source-code linker** (see
:doc:`/contribute/development/traceability_tooling`). Add a comment
containing one of these template strings on the line(s) of the
implementing function/method:

.. code-block:: cpp

   // # req-Id: comp_req__containers_rust__fixed_vector
   int your_function() { ... }

.. code-block:: rust

   /// # req-Id: comp_req__feo__activity
   impl Activity { ... }

.. code-block:: python

   # req-Id: tool_req__docs_common_attr_title
   # req-Id: tool_req__docs_common_attr_status
   def your_function(args): ...

The linker scans every file (skipping ``.pyc``, ``.so``, ``.exe``,
``.bin``, ``.rst``, ``.md`` and dot-prefixed paths) and produces a
``source_code_link`` extra field on the linked need, surfaced in the
rendered page.

Step 13 -- Add the verification (``testcase``)
==============================================

You do **not** write ``testcase`` directives by hand. You tag the test
in its source, the framework emits a JUnit XML and the docs-as-code
test-result linker synthesises the need. The metadata you must set:

.. code-block:: cpp

   class StoreReadTest : public ::testing::Test {
     public:
       void SetUp() override {
           RecordProperty("TestType",            "requirements-based");
           RecordProperty("DerivationTechnique", "boundary-values");
       }
   };

   TEST_F(StoreReadTest, RoundTrip) {
       RecordProperty("FullyVerifies",
                      "comp_req__<module>__<component>__store_read");
       RecordProperty("Description", "Round-trip of an arbitrary blob.");
       /* ... */
   }

Rules (from ``gd_req__verification_checks``):

- Unit Test or Component Integration Test may only ``FullyVerifies`` /
  ``PartiallyVerifies`` a ``comp_req``.
- Feature Integration Test may only link to ``feat_req``.
- Platform Integration Test may only link to ``stkh_req``.

Use ``PartiallyVerifies`` on each test when more than one test together
covers the requirement, then set the ``complete test coverage``
attribute on the ``comp_req`` (ASIL only).


Cross-layer link cheat sheet
****************************

When in doubt, this is the only set of cross-layer links you need
today:

.. list-table::
   :header-rows: 1
   :widths: 22 22 26 30

   * - From (component side)
     - Link
     - To (feature side)
     - Mandatory?
   * - ``comp_req``
     - ``satisfies``
     - ``feat_req``
     - mandatory
   * - ``comp``
     - ``belongs_to``
     - ``feat``
     - mandatory
   * - ``comp``
     - ``implements``
     - ``logic_arc_int``, ``real_arc_int_op``
     - optional (mandatory when ``feat`` ``:provides:`` the iface)
   * - ``comp`` / ``comp_arc_sta``
     - ``uses``
     - ``logic_arc_int``, ``real_arc_int_op``
     - optional
   * - ``feat``
     - ``provides`` / ``uses``
     - ``logic_arc_int(_op)``
     - optional, but expected when any component implements it

Everything else (``includes``, ``fulfils``, ``belongs_to`` inside a
layer) stays *within* its layer.


Validation before opening a PR
******************************

Run the live build and the metamodel checks locally:

.. code-block:: bash

   bazel run //:run live_preview

What the build will reject:

- Missing mandatory option (``status``, ``safety``, ``security``,
  ``reqtype`` for requirements).
- Missing mandatory link (``comp.belongs_to``,
  ``comp_req.satisfies`` / ``belongs_to``,
  ``feat_arc_*.belongs_to`` / ``fulfils``, …).
- Dead link (``has_forbidden_dead_links`` in ``needs.json``): the
  target ID does not exist.
- Graph check violations: QM → ASIL escalation; security mismatch;
  safety analysis pointing to QM elements.

What the build will *warn* about (but accept today):

- ``testcase.fully_verifies`` pointing at the wrong layer (e.g. a unit
  test linking to ``stkh_req__…``). The corresponding tool
  requirement ``tool_req__docs_test_metadata_link_levels`` is still
  ``:implemented: NO``.
- ``feat`` without ``:provides:`` even though it has ``logic_arc_int``
  ``includes`` from a ``feat_arc_sta``.
- Missing ``complete test coverage`` attribute on an ``ASIL_B``
  ``comp_req``.


Dormant elements (add only when needed)
***************************************

The following schema types are *registered* in
``metamodel.yaml`` but have **zero** declarations in ``docs/`` today.
Do not introduce them speculatively; add them when the safety plan or
a release rule starts requiring them:

- ``dd_sta`` / ``dd_dyn`` -- detailed design. Today components jump
  from ``comp_req`` straight to source code via ``# req-Id:``. Add DD
  needs once ``wp__sw_implementation_inspection`` becomes mandatory
  for your module.
- ``sw_unit``, ``sw_unit_int`` -- only useful once a module starts to
  publish sw-unit interfaces formally.
- ``real_arc_int``, ``real_arc_int_op`` -- realised interface
  refinement. Currently every cross-layer ``implements`` / ``uses``
  targets ``logic_arc_int``; switch to ``real_arc_int_op`` when API
  qualification needs the realised signature.
- ``comp_arc_dyn`` -- component sequence diagrams (only one usage in
  the entire ``docs/`` today, in ``feo``).
- ``feat_saf_fmea`` / ``feat_saf_dfa`` / ``comp_saf_fmea`` /
  ``comp_saf_dfa`` / ``plat_saf_dfa`` -- safety analyses. Add once
  your module enters the ASIL safety case (the module safety plan
  prescribes which analyses are required).
- ``mod_view_dyn`` -- module sequence diagrams.

When you do introduce a dormant type, the link contract is already in
``metamodel.yaml``; re-read it before writing the directive to be sure
of mandatory vs. optional links and the safety-propagation graph
checks.


Worked example: ``baselibs`` feature + ``bitmanipulation`` component
********************************************************************

The smallest end-to-end excerpt that matches the baselibs sources.
Each file is annotated with the repository that owns it.

**[score repo]** ``docs/features/baselibs/index.rst``:

.. code-block:: rst

   .. _baselibs_feature:

   Base Libraries
   ###############

   .. document:: Base Libraries
      :id: doc__baselibs
      :status: valid
      :safety: ASIL_B
      :tags: feature_request
      :security: YES
      :realizes: wp__feat_request

   .. toctree::
      :hidden:

      docs/requirements/index.rst
      docs/requirements/chklst_req_inspection.rst
      docs/architecture/index.rst

   Abstract
   ========
   …

**[score repo]**
``docs/features/baselibs/docs/requirements/index.rst``:

.. code-block:: rst

   .. document:: Baselibs Requirements
      :id: doc__baselibs_requirements
      :status: draft
      :safety: ASIL_B
      :security: YES
      :realizes: wp__requirements_feat

   .. feat_req:: Bit Manipulation Library
      :id: feat_req__baselibs__bitmanipulation
      :reqtype: Functional
      :security: NO
      :safety: ASIL_B
      :satisfies: stkh_req__functional_req__base_libraries
      :status: valid

      The base libraries shall provide bit manipulation utilities for
      low-level operations on integral types.

   .. needextend:: is_external == False and "__baselibs" in id
      :+tags: baselibs

**[score repo]**
``docs/features/baselibs/docs/architecture/index.rst``
(only the contract: ``feat`` + ``logic_arc_int``):

.. code-block:: rst

   .. document:: Baselibs Architecture
      :id: doc__baselibs_architecture
      :status: valid
      :safety: ASIL_B
      :security: YES
      :realizes: wp__feature_arch

   .. feat:: Baselibs
      :id: feat__baselibs
      :security: YES
      :safety: ASIL_B
      :status: valid
      :provides: logic_arc_int__baselibs__bit_manipulation,
                 logic_arc_int__baselibs__json,
                 logic_arc_int__baselibs__memory_shared

   .. logic_arc_int:: Bit Manipulation
      :id: logic_arc_int__baselibs__bit_manipulation
      :security: NO
      :safety: ASIL_B
      :status: valid

**[baselibs module repo]**
``docs/features/baselibs/docs/architecture/index.rst``
(realisation views -- merged into the same page by the build):

.. code-block:: rst

   .. feat_arc_sta:: Baselibs Static Architecture
      :id: feat_arc_sta__baselibs__static
      :security: YES
      :safety: ASIL_B
      :status: valid
      :belongs_to: feat__baselibs
      :includes: logic_arc_int__baselibs__bit_manipulation,
                 logic_arc_int__baselibs__json,
                 logic_arc_int__baselibs__memory_shared
      :fulfils: feat_req__baselibs__bitmanipulation,
                feat_req__baselibs__json_library,
                feat_req__baselibs__memory_library

      .. uml:: _assets/baselibs_static.puml

**[baselibs module repo]** ``docs/modules/baselibs/index.rst``:

.. code-block:: rst

   Baselibs Module
   ###############

   .. toctree::
      :titlesonly:
      :maxdepth: 2

      ./docs/index

   Components
   ==========

   .. toctree::
      :titlesonly:
      :maxdepth: 1
      :glob:

      ./*/docs/index

**[baselibs module repo]** ``docs/modules/baselibs/docs/index.rst``:

.. code-block:: rst

   .. mod:: Baselibs
      :id: mod__baselibs
      :status: valid
      :safety: ASIL_B
      :security: YES
      :includes: comp__baselibs__bitmanipulation,
                 comp__baselibs__json,
                 comp__baselibs__memory_shared

   .. mod_view_sta:: Baselibs
      :id: mod_view_sta__baselibs__baselibs
      :belongs_to: mod__baselibs
      :includes: comp__baselibs__bitmanipulation,
                 comp__baselibs__json,
                 comp__baselibs__memory_shared

      .. needarch::

         {{ draw_module(need(), needs) }}

**[baselibs module repo]**
``docs/modules/baselibs/bitmanipulation/docs/architecture/index.rst``:

.. code-block:: rst

   .. document:: BitManipulation Architecture
      :id: doc__baselibs_bitmanipulation_architecture
      :status: valid
      :safety: ASIL_B
      :security: NO
      :realizes: wp__component_arch

   Component Architecture
   **********************

   .. comp:: baselibs::bitmanipulation
      :id: comp__baselibs__bitmanipulation
      :security: NO
      :safety: ASIL_B
      :status: valid
      :belongs_to: feat__baselibs
      :implements: logic_arc_int__baselibs__bit_manipulation

      .. needarch::

         {{ draw_component(need(), needs) }}

   .. comp_arc_sta:: Static Architecture
      :id: comp_arc_sta__baselibs__bitmanipulation__static
      :security: NO
      :safety: ASIL_B
      :status: valid
      :belongs_to: comp__baselibs__bitmanipulation
      :fulfils: comp_req__baselibs__bitmanipulation__count_set_bits

      .. uml:: _assets/bit_static.puml

**[baselibs module repo]**
``docs/modules/baselibs/bitmanipulation/docs/requirements/index.rst``:

.. code-block:: rst

   .. document:: BitManipulation Requirements
      :id: doc__baselibs_bitmanipulation_requirements
      :status: valid
      :safety: ASIL_B
      :security: NO
      :realizes: wp__requirements_comp

   .. comp_req:: Count set bits
      :id: comp_req__baselibs__bitmanipulation__count_set_bits
      :reqtype: Functional
      :security: NO
      :safety: ASIL_B
      :status: valid
      :belongs_to: comp__baselibs__bitmanipulation
      :satisfies: feat_req__baselibs__bitmanipulation

**[baselibs module repo]** in the C++ implementation file:

.. code-block:: cpp

   // # req-Id: comp_req__baselibs__bitmanipulation__count_set_bits
   std::size_t count_set_bits(std::uint64_t v) { ... }

**[baselibs module repo]** in the gtest file:

.. code-block:: cpp

   TEST(BitManipulation, CountSetBits) {
       RecordProperty("TestType",            "requirements-based");
       RecordProperty("DerivationTechnique", "boundary-values");
       RecordProperty("FullyVerifies",
           "comp_req__baselibs__bitmanipulation__count_set_bits");
       RecordProperty("Description", "Set-bit count for boundary values.");
       /* ... */
   }

Rendered result:

- The ``feat_req__baselibs__bitmanipulation`` page shows a
  ``satisfied_by`` backlink to the ``comp_req``.
- The ``comp_req`` page shows a ``fully_verified_by`` backlink to the
  testcase, a ``source_code_link`` to the C++ function and a
  ``satisfies`` forward link up to the ``feat_req``.
- The ``feat__baselibs`` page shows a ``provided_by`` backlink from
  ``logic_arc_int__baselibs__bit_manipulation`` and an
  ``implemented_by`` backlink from
  ``comp__baselibs__bitmanipulation``.
- The ``mod__baselibs`` page (with ``draw_module``) shows the
  rendered static module view aggregating all included components.


Quick checklist before merging
******************************

1. Every ``feat_req`` ``:satisfies:`` at least one ``stkh_req``.
2. Every ``comp_req`` ``:satisfies:`` at least one ``feat_req`` and
   ``:belongs_to:`` a ``comp``.
3. Every ``comp`` ``:belongs_to:`` a ``feat``.
4. Every ``feat_arc_sta`` / ``feat_arc_dyn`` ``:belongs_to:`` a
   ``feat`` and ``:fulfils:`` at least one ``feat_req``.
5. Every ``feat_arc_sta`` ``:includes:`` the ``logic_arc_int`` the
   feature ``:provides:``.
6. Every ``logic_arc_int_op`` is ``:included_by:`` exactly one
   ``logic_arc_int``.
7. ``mod.includes`` lists every ``comp`` of the module;
   ``mod_view_sta.belongs_to`` points to that ``mod``.
8. Safety / security levels propagate consistently
   (``QM → QM`` only, ``ASIL_B → ASIL_B``,
   ``security YES → security YES``).
9. Every implementing function carries a ``# req-Id: comp_req__…``
   comment.
10. Every test sets ``TestType`` + ``DerivationTechnique`` +
    ``FullyVerifies`` / ``PartiallyVerifies`` and -- for ASIL --
    the ``comp_req`` has ``complete test coverage = yes``.
11. The four inspection checklists exist:

    - feature: ``…/docs/requirements/chklst_req_inspection.rst``,
      ``…/docs/architecture/chklst_arc_inspection.rst``,
    - component: ``…/docs/requirements/chklst_req_inspection.rst``,
      ``…/docs/architecture/chklst_arc_inspection.rst``,
      ``…/docs/detailed_design/chklst_impl_inspection.rst``.

12. ``bazel run //:run live_preview`` is green and ``needs.json``
    contains no ``has_forbidden_dead_links``.


.. |to| unicode:: U+2192 .. RIGHTWARDS ARROW

See also
********

- :doc:`/contribute/development/traceability_tooling` -- how to render
  dashboards (``needtable``, ``needpie``) from the linked data.
- :doc:`/platform_management_plan/software_verification` -- allowed
  ``TestType`` / ``DerivationTechnique`` values and release-time
  quality goals.
- ``docs/features/baselibs/`` and ``docs/modules/baselibs/`` -- the
  canonical sources this how-to mirrors.
