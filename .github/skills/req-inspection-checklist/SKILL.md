---
name: req-inspection-checklist
description: 'Reference assets for creating and filling a feature requirements inspection checklist (chklst_req_inspection.rst) for an S-CORE feature: file location patterns, RST template, standard checklist items, per-item analysis commands, and toctree/needtable snippets. Used by the Requirements Inspection agent. Follows the pattern from baselibs and persistency features. Scope is limited to feature-level `feat_req` inspections in the score repo; component-level `comp_req` inspections in module repos are not yet supported.'
argument-hint: 'Feature name (e.g. "communication", "baselibs", "persistency")'
---

# Requirements Inspection Checklist — Reference

Reference assets for the `chklst_req_inspection.rst` file used by S-CORE features. The end-to-end workflow (locate file, decide create vs. fill, set status, report) lives in the `req-inspection` agent — this skill provides the concrete templates, patterns and per-item analysis recipes the agent applies.

**Scope:** feature-level requirements inspections only (`feat_req` under `docs/features/<feature>/`). Component-level `comp_req` inspections in module repositories (`baselibs`, `logging`, `feo`, `persistency`, …) are out of scope for this skill.

## Checklist File Location Patterns

Features follow one of two directory structures:

| Pattern | Example |
|---|---|
| `docs/features/<feature>/docs/requirements/` | baselibs, communication |
| `docs/features/<feature>/requirements/` | persistency |

Always check which pattern the target feature uses before creating the file.

## Document Directive Pattern

```rst
.. document:: <Feature> Requirements Inspection Checklist
   :id: doc__<feature>_req_inspection
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_inspect
```

- `:id:` must be unique across the project — use `doc__<feature>_req_inspection`
- `:status:` starts as `draft`
- `:safety:` matches the safety level of the feature requirements document
- `:security:` matches the security attribute of the feature requirements document
- `:realizes: wp__requirements_inspect` is always required

## Checklist Items (standard, never change)

| ID | Acceptance Criteria |
|---|---|
| REQ_01_01 | Is the requirement sentence template used? |
| REQ_02_01 | Is the requirement description *comprehensible*? |
| REQ_02_02 | Is the requirement description *unambiguous*? |
| REQ_02_03 | Is the requirement description *atomic*? |
| REQ_02_04 | Is the requirement description *feasible*? |
| REQ_02_05 | Is the requirement description *independent from implementation*? |
| REQ_03_01 | For stakeholder requirements: Is the *rationale* correct? |
| REQ_03_02 | For other requirements: Is the *linkage to the parent requirement* correct? |
| REQ_04_01 | Is the requirement *internally and externally consistent*? |
| REQ_05_01 | Do the software requirements consider *timing constraints of the parent requirement*? |
| REQ_06_01 | Does the requirement consider *external interfaces*? |
| REQ_07_01 | Is the *ASIL Attribute* set correctly? |
| REQ_07_02 | Is the attribute *security* set correctly? |
| REQ_08_01 | Is the requirement *verifiable*? |
| REQ_09_01 | For stakeholder requirements: Do those cover assumed safety mechanisms needed by the hardware and system? |
| REQ_09_02 | For feature/component requirements: Do the requirements defining a safety mechanism contain the error reaction leading to a safe state? |

## Needtable Filter at End of File

Always append two `needtable` directives at the end — one for `feat_req`, one for `aou_req`:

```rst
.. needtable::
   :filter: "features/<feature>" in docname and "requirements" in docname and docname is not None and status == "valid"
   :style: table
   :types: feat_req
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

.. needtable::
   :filter: "features/<feature>" in docname and "requirements" in docname and docname is not None and status == "valid"
   :style: table
   :types: aou_req
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
```

## Toctree Registration

After creating the file, add it to the feature's top-level `index.rst` toctree:

- For `docs/features/<feature>/docs/requirements/` layout → add to `docs/features/<feature>/index.rst`
- Entry: `docs/requirements/chklst_req_inspection.rst` (or without `.rst` extension as preferred in the file)

**Important:** If the toctree uses a `:glob:` pattern like `docs/**/index`, the checklist will NOT be picked up automatically — it must be added explicitly.

## Filling the Checklist (Conducting the Inspection)

After the file is created — or if it already exists but is still `draft` with empty `Passed` columns — perform the following analysis on the feature's `requirements/index.rst` (and any sub-requirement files) to compute the actual verdict for each row.

### Analysis Steps per Checklist Item

#### REQ_01_01 — "shall" template used?

```bash
grep -n "shall" docs/features/<feature>/**/requirements/index.rst \
  | grep -v "^.*:id:\|:reqtype:\|:security:\|:safety:\|:satisfies:\|:status:"
```

- **Yes** if every `feat_req` / `aou_req` body contains at least one "shall".
- **No** if any requirement body is missing "shall" — list the failing IDs in Remarks.

#### REQ_02_01 — Comprehensible?

Read each requirement body. **No** = any requirement that is hard to understand without domain knowledge. List the IDs in Remarks.

#### REQ_02_02 — Unambiguous?

```bash
grep -n "whenever possible\|if possible\|as needed\|as required\|appropriate\|suitable\|sufficient\|adequate\|reasonable\|about\b\|etc\.\|relevant\b\|may be\|might be\|could be\|should be" \
  docs/features/<feature>/**/requirements/index.rst
```

- **Yes** if none found in requirement bodies (notes are excluded).
- **No** — list the weak words and the requirement IDs in Remarks.
- Note: occurrences only in `.. note::` blocks are acceptable.

#### REQ_02_03 — Atomic?

```bash
grep -c "shall" <each requirement body>
```

- **No** if any single requirement body contains more than one "shall" statement (covering distinct obligations) — list the IDs.
- **Yes** if each requirement body has exactly one "shall" obligation.

#### REQ_02_04 — Feasible?

```bash
grep -n ":impl:" docs/features/<feature>/**/requirements/index.rst
```

- **Yes** if `:impl:` traces are present for the requirements.
- **Leave empty** and write in Remarks "No :impl: traces present — needs verification by development expert." if none found.

#### REQ_02_05 — Independent from implementation?

Read each requirement body. **No** = any requirement that dictates the "how" (algorithms, data structures, specific library names) in the body (not only in notes). Notes may contain implementation hints.

#### REQ_03_01 — Stakeholder requirement rationale correct?

```bash
grep -n "^.. stkh_req::" docs/features/<feature>/**/requirements/index.rst
```

- **N/A** with remark "No stakeholder requirements in scope of this inspection." if no `stkh_req` directives are found in the requirements file.
  Note: `:satisfies: stkh_req__...` links do **not** make an `feat_req` a stakeholder requirement.
- **Yes/No** otherwise — check rationale text.

#### REQ_03_02 — Linkage to parent correct?

```bash
grep -n ":satisfies:" docs/features/<feature>/**/requirements/index.rst
```

- **Yes** if every `feat_req` / `aou_req` has a `:satisfies:` pointing to an appropriate parent.
- **No** if any requirement is missing `:satisfies:` or points to an unrelated parent — list IDs.

#### REQ_04_01 — Internally and externally consistent?

Read all requirements. Check for contradictions within the feature and against other features that share components. **Yes/No** with list of contradicting pairs if found.

#### REQ_05_01 — Timing constraints considered?

Check parent stkh_req for timing requirements. Verify that `feat_req` with ASIL_B `:safety:` address timing where needed. **Yes/No**.

#### REQ_06_01 — External interfaces considered?

Check whether the requirements define the API elements (inputs, outputs, error codes). **Yes** if interfaces are specified; **No** with list of gaps.

#### REQ_07_01 — ASIL Attribute correct?

```bash
grep -n ":safety:" docs/features/<feature>/**/requirements/index.rst
```

- Automated checks handle derived requirements.
- For top-level and AoU requirements: manual check by safety expert needed.
- **Leave empty** and note "Needs verification by safety expert." if top-level ASIL allocation cannot be verified from documentation alone.

#### REQ_07_02 — Security attribute correct?

```bash
grep -n ":security:" docs/features/<feature>/**/requirements/index.rst
```

- Automated check covers inheritance from security=YES parents.
- For top-level: requires TARA.
- **Leave empty** and note "Needs TARA verification." if TARA results are not available.

#### REQ_08_01 — Verifiable?

```bash
grep -rn ":covers:.*<req_id_prefix>" /workspaces/score --include="*.rst"
grep -rn ":covers:.*<req_id_prefix>" /workspaces/score --include="*.py" --include="*.cpp"
```

- **Yes** if `:covers:` traces from test specifications back to the feature requirements exist.
- **Leave empty** and note "No :covers: traces from tests found — needs test expert." if none found.

#### REQ_09_01 — Stakeholder requirements cover assumed safety mechanisms?

```bash
grep -n "^.. stkh_req::" docs/features/<feature>/**/requirements/index.rst
```

- **N/A** with remark "No stakeholder requirements in scope of this inspection." if no `stkh_req` directives are present.
- **Yes/No** otherwise — check that stakeholder rationales address safety mechanisms expected from hardware and system level.

#### REQ_09_02 — Feature/component safety mechanism error reaction?

```bash
grep -n "safe state\|error reaction\|safety mechanism\|fail.safe\|fail_safe" \
  docs/features/<feature>/**/requirements/index.rst
```

- **N/A** with remark "No feature requirements defining a safety mechanism with an error reaction are present." if no safety mechanisms found.
- **Yes/No** otherwise — check that error reactions leading to safe state are described.

### Column Values

| Column | Values | Notes |
|---|---|---|
| `Passed` | `Yes`, `No`, `N/A`, or empty | Empty = cannot be assessed from documentation alone |
| `Remarks` | Explanation | Always explain `N/A`, `No`, and empty verdicts; list failing requirement IDs |
| `Issue link` | GitHub issue URL or empty | Use the feature's inspection tracking issue for all rows |

### Completing the Inspection

Only change `:status: draft` → `:status: valid` when **all** `Passed` cells are filled (no empties remain). Rows that needed expert input must be resolved first.

### Issue Link Reference

- Search GitHub for an existing **inspections tracking issue** for the feature:
  `gh issue list --label ft:<feature> --search "inspection"` or check the feature epic.
- Use the same URL for all rows.
- Example for baselibs: `https://github.com/eclipse-score/score/issues/2479`
- Example for persistency: `https://github.com/eclipse-score/score/issues/960`

## Full File Template

```rst
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

<Feature> Requirements Inspection Checklist
###########################################

.. document:: <Feature> Requirements Inspection Checklist
   :id: doc__<feature>_req_inspection
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_inspect

**Purpose**

The purpose of this requirement inspection checklist is to collect the topics to be
checked during requirements inspection.

**Conduct**

As described in the concept :need:`doc_concept__wp_inspections` the following
"inspection roles" are expected to be filled:

- author: persons who did the last commits on the requirements in scope
- reviewer: persons committing into this inspection document or giving a PR verdict
- moderator: only needed for conflict resolution; is the safety/security/quality manager
- test expert: <one of the reviewers explicitly named here, to cover REQ_08_01>

**Checklist**

.. list-table:: <Feature> Requirements Inspection Checklist
   :header-rows: 1
   :widths: 10,30,50,6,6,8

   * - Review ID
     - Acceptance Criteria
     - Guidance
     - Passed
     - Remarks
     - Issue link
   * - REQ_01_01
     - Is the requirement sentence template used?
     - see :need:`gd_temp__req_formulation`, this includes the use of "shall".
     -
     -
     -
   * - REQ_02_01
     - Is the requirement description *comprehensible* ?
     - If you think the requirement is hard to understand, comment here.
     -
     -
     -
   * - REQ_02_02
     - Is the requirement description *unambiguous* ?
     - Especially search for "weak words" like "about", "etc.", "relevant" and others.
     -
     -
     -
   * - REQ_02_03
     - Is the requirement description *atomic* ?
     - Consider if the requirement may be tested by one positive test case or needs more.
     -
     -
     -
   * - REQ_02_04
     - Is the requirement description *feasible* ?
     - Expectation is that at the time of inspection the requirement has some implementation.
       This can be checked via traces, see also :need:`gd_req__req_attr_impl`.
     -
     -
     -
   * - REQ_02_05
     - Is the requirement description *independent from implementation* ?
     - The "what" should be described, not the "how".
     -
     -
     -
   * - REQ_03_01
     - For stakeholder requirements: Is the *rationale* correct?
     - Rationales explain why the top level requirements were created.
     -
     -
     -
   * - REQ_03_02
     - For other requirements: Is the *linkage to the parent requirement* correct?
     - Linkage to correct levels and ASIL attributes is checked automatically, but
       correctness of the child implementing the parent must be checked manually.
     -
     -
     -
   * - REQ_04_01
     - Is the requirement *internally and externally consistent*?
     - Does the requirement contradict other requirements within the same or higher levels?
     -
     -
     -
   * - REQ_05_01
     - Do the software requirements consider *timing constraints of the parent requirement*?
     - Think about timing constraints even if those are not explicitly mentioned in the parent.
     -
     -
     -
   * - REQ_06_01
     - Does the requirement consider *external interfaces*?
     - Feature and Component Requirements should determine the data consumed and set on interfaces.
     -
     -
     -
   * - REQ_07_01
     - Is the *ASIL Attribute* set correctly?
     - Derived requirements are checked automatically, see :need:`gd_req__req_linkage_safety`.
       Top level requirements and AoUs must be checked manually.
     -
     -
     -
   * - REQ_07_02
     - Is the attribute *security* set correctly?
     - Stakeholder requirements security attribute should be set based on TARA.
       Automated check: every requirement satisfying a security=YES requirement inherits it.
     -
     -
     -
   * - REQ_08_01
     - Is the requirement *verifiable*?
     - Expectation is that at the time of inspection tests are created for the requirement.
       See :need:`gd_req__req_attr_test_covered`. Missing test cases → invite a test expert.
     -
     -
     -
   * - REQ_09_01
     - For stakeholder requirements: Do those cover assumed safety mechanisms needed by the
       hardware and system?
     - Stakeholder requirements covering safety mechanisms come from rationales, whereas
       feature/component requirements are covering safety mechanisms coming from
       :need:`gd_chklst__safety_analysis`.
     -
     -
     -
   * - REQ_09_02
     - For feature/component requirements: Do the requirements defining a safety mechanism
       contain the error reaction leading to a safe state?
     - Alternatively there could be "repair" mechanisms. Also consider REQ_05_01 for these.
     -
     -
     -

Note: If a Review ID is not applicable, state "n/a" in Passed and comment in Remarks.
For example "no stakeholder requirement (no rationale needed)".

The following requirements in "valid" state are in scope of this inspection:

.. needtable::
   :filter: "features/<feature>" in docname and "requirements" in docname and docname is not None and status == "valid"
   :style: table
   :types: feat_req
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

And also the following AoUs in "valid" state (answer the questions above as if they are
requirements, except REQ_03_01 and REQ_03_02):

.. needtable::
   :filter: "features/<feature>" in docname and "requirements" in docname and docname is not None and status == "valid"
   :style: table
   :types: aou_req
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
```
