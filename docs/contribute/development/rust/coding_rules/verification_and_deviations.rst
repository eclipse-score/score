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

.. _rust_coding_rules_verification:

Verification and Deviations
###########################

.. document:: Rust Coding Rules Verification and Deviations
   :id: doc__rust_coding_rules_verification
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan[version==1]

Coverage per rule
=================

For an adopted rulebook, maintain one coverage record per rule and delivered
configuration in the project's :need:`Verification Plan <wp__verification_plan>`
and associated reports. Record:

* Rule ID, rulebook revision and applicable component/profile.
* Compiler, Clippy and custom checker versions, exact flags and configured scope.
* Target, Rust edition, feature selection, dependency versions and generated inputs.
* Positive/negative checker tests, known false positives and missed cases.
* Full, partial or manual coverage, and the additional review/test evidence needed.
* Findings, their disposition, deviations and outstanding obligations.

A checker that did not run, failed to extract code, or analyzed a different
configuration provides no clean-result evidence. Suppressing a diagnostic does
not establish rule conformance. A rule with no automated checker still needs
its assigned review or verification evidence.

Selection and validation of checkers
====================================

Start with the existing compiler and Clippy checks that match the selected rule.
Confirm their behavior in the pinned toolchain and verify that both Cargo and
Bazel analysis actions receive the intended flags. ``clippy.toml`` configuration
alone does not establish that a lint is enabled.

The catalogue's checker mappings are candidates, not validated implementations.
For custom CodeQL checks, first establish extraction coverage and model the
relevant APIs, validators and effects. Compiler-based custom lints may be needed
when the rule relies on precise Rust compiler semantics. Tool selection follows
the adopted requirement rather than determining its meaning.

Use compliant and violating examples to validate each checker, including relevant
aliases, macros, trait calls, unsafe wrappers and conditional compilation. Include
examples that compile successfully but violate the adopted policy. Miri and other
runtime analysis provide evidence only for supported executed paths.

Tool configuration and checker implementations belong in ``score_rust_policies`` and
shared analysis tooling; this section owns the rule text. The coverage record identifies the exact
tooling revision associated with a rulebook revision.

Deviation records
=================

A proposed deviation records:

* The rule and rulebook revision, source locations and configurations affected.
* The reason conformance is impractical and the alternatives considered.
* Safety/security consequences, compensating measures and verification evidence.
* Accountable owner, reviewers, approval reference and review date or expiry.
* The exact suppression or configuration change, if one is needed.

Review deviations through the project's existing implementation/review process
and the responsibilities identified in its development and verification plans.
A technical suppression is not approval. Advisory nonconformances also receive
a documented disposition, even when a formal deviation is unnecessary.
No deviation can permit Rust undefined behavior.

Adoption and rollout
====================

#. Review the proposed rules and classification corrections; assign rule owners.
   Resolve component-specific allocation, recursion, panic, numerical precision
   and foreign-interface requirements.
#. Validate selected compiler/Clippy checks first, particularly
   :ref:`SCR-RUST-002 <scr-rust-002>`, :ref:`SCR-RUST-004 <scr-rust-004>`,
   :ref:`SCR-RUST-016 <scr-rust-016>`, :ref:`SCR-RUST-026 <scr-rust-026>`,
   :ref:`SCR-RUST-036 <scr-rust-036>` and :ref:`SCR-RUST-037 <scr-rust-037>`.
#. Inventory unsafe operations and foreign interfaces, including pointer operations
   expressed in safe code. Record dependency and generated-code assumptions.
#. Prototype custom analysis only for identified coverage gaps. Measure false
   positives and missed cases before using it as a blocking check.
#. Report existing findings, review their dispositions, then gate new violations
   of validated checks. Preserve manual obligations and unimplemented-check gaps.
#. Review coverage and deviations for the delivered configurations at release.

Acceptance is per rule and configuration. A clean lint/SARIF report is not a
functional-safety claim. Timing, crash consistency, protocol correctness and
system-level safety properties need their own requirements and verification.
