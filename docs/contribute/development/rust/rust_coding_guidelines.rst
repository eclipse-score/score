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

.. _rust_coding_guidelines:

Rust Coding Guidelines
######################

.. document:: Coding Guidelines Rust
   :id: doc__rust_coding_guidelines
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan[version==1]


Safety Rust
===========

For writing Rust code in S-CORE, especially for safety- and
security-relevant software, the following guidance and tooling references
apply.

This page provides the rationale, the guideline and tooling landscape, and a
project-wide set of practices for writing Rust in S-CORE. The concrete,
enforceable rules (the ``rustc`` / Clippy lint configuration and the release
profile) are maintained centrally in the ``score_rust_policies`` repository and
are referenced from the `Conclusions for S-CORE`_ section below.


Coding Guidelines
-----------------

The following coding guidelines and reference documents are relevant for
Rust development in S-CORE:

* A safety- and cybersecurity-oriented Rust baseline (referred to as "the
  baseline" throughout this document) is used as the primary reference for
  safety- and security-related development and for arguing safety according to
  ISO 26262 or RTCA DO-178C combined with RTCA DO-332. It provides a
  comprehensive set of recommendations for using Rust in safety-critical
  systems, including language features, coding practices, and tool usage.
* `Safety-Critical Rust Coding Guidelines <https://coding-guidelines.arewesafetycriticalyet.org/>`_
  are still under development and currently only define a subset of the
  desired rules.
* `Secure Rust Guidelines (unstable) <https://anssi-fr.github.io/rust-guide/>`_
  complement this baseline. ANSSI focuses more on process and architecture
  guidance, while the baseline is more concrete regarding tool usage and
  enforceable checks.
* `Linux Kernel Rules <https://www.kernel.org/doc/Documentation/rust/coding-guidelines.rst>`_
  mainly define formatting and documentation requirements for Rust in the
  Linux kernel and do not provide broader static code analysis rules.
* `MISRA C:2025 Addendum 6, Applicability of MISRA C:2025 to the Rust Programming Language <https://misra.org.uk/app/uploads/2025/03/MISRA-C-2025-ADD6.pdf>`_
  overlaps strongly with this baseline and is therefore primarily relevant as an
  additional cross-reference.


State of Rust Safety-Critical Tooling
-------------------------------------

The Safety-Critical Rust Consortium aims to make Rust suitable for use in
automotive and other safety-critical environments by building and maintaining a
set of essential tools that are vetted by the community for certification
purposes. They track the development status of these tools and document their
progress. The consortium is considering whether to develop specialized training
materials for safety-critical Rust, though this may require a separate group.
Their current activities include supporting a qualified compiler (with
Ferrocene available for some targets), developing a certified core library,
working on tools for coding style verification, and assessing the need for
static analysis and code metrics tools. Some tools, such as MC/DC coverage
reporting and code metrics generators, are still unavailable, and the
consortium is evaluating what further tooling and support are necessary to
enable certification and safe use of Rust in automotive applications.

The following external references provide context for the safety-critical Rust
tooling and guidelines:

* `Safety-Critical Coding Guidelines <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines>`_
* `Deployed version of Safety-Critical Coding Guidelines <https://coding-guidelines.arewesafetycriticalyet.org/>`_
* `Safety-Critical Rust Consortium <https://rustfoundation.org/safety-critical-rust-consortium>`_
* `Safety-Critical Rust Consortium Guidelines <https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines/>`_
* `Learn unsafe Rust <https://google.github.io/learn_unsafe_rust/>`_
* `Rust language <https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html>`_
* `Mission Statement - Safety-critical-rust-consortium <https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/blob/main/arewesafetycriticalyet.org/docs/coding_guidelines/1_mission.md>`_
  and `Tooling Mission Statement <https://arewesafetycriticalyet.org/tooling/statement/>`_

The goal is to have coding guidelines for Rust suitable for safety-critical
systems by the Safety-Critical Rust Consortium by the end of 2026. Until that,
please also use Slack score-rust-community channel for discussions and
participation in the SCRC.


MISRA vs CERT
-------------

MISRA and CERT represent two different approaches to safety- and
security-oriented coding standards. MISRA relies on restrictive language
subsetting and a formal compliance process, which can add effort without a
proportional safety or security benefit and is not always consistent across
languages. CERT focuses on practical, consensus-based rules that target real
security vulnerabilities in existing code. For Rust in SCORE the CERT-style
approach — practical, evidence-based and focused on real-world issues — is
preferred over rigid language subsetting, which is consistent with the Clippy-
and compiler-based enforcement used in this project.

The SCRC discussion `MISRA vs CERT <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/75/>`_
provides background on comparing the two approaches for Rust coding guidelines.

In 2026 the Coding Guidelines Subcommittee of the SCRC are aiming to have
MISRA C and CERT C mapped to Rust, with

* a bulk of the coding guidelines written
* a bulk of the Clippy lints necessary written to check the guidelines


Rust Tooling: Clippy
--------------------

Rust Clippy is a collection of lints (code style and correctness checks) for
the Rust programming language. It helps developers identify common mistakes,
improve code quality, and follow best practices by providing warnings and
suggestions as part of the Rust toolchain. Clippy can be run on Rust projects
to catch issues that the standard compiler might miss, making it an essential
tool for writing clean, idiomatic, and efficient Rust code.

`Link to Clippy <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/78/>`_


Rust Tooling: CodeQL
--------------------

CodeQL is a code analysis platform based on the QL query language and
associated tooling. It supports Rust (see
`CodeQL supported languages and frameworks <https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/>`_
and `CodeQL Rust CWE query help <https://codeql.github.com/codeql-query-help/rust-cwe/>`_).

Typical problem classes detected by CodeQL for Rust include:

* injection vulnerabilities (e.g., SQL injection, path traversal,
  regex injection, log injection, XSS)
* insecure communication and transport usage (e.g., non-HTTPS URLs,
  disabled TLS certificate checks)
* cryptographic weaknesses (e.g., hard-coded cryptographic values,
  weak algorithms or weak hashing)
* sensitive data exposure (e.g., cleartext logging, cleartext
  transmission or storage)
* request and input abuse patterns (e.g., SSRF, uncontrolled allocation
  size from untrusted input)
* unsafe memory-related patterns relevant at Rust unsafe boundaries
  (e.g., access-after-lifetime-ended, invalid pointer access,
  constructor initialization issues)

CodeQL's key strength is inter-procedural data-flow/taint tracking,
which complements compiler and lint checks.


Rust Tooling: Miri
------------------

Miri is an Undefined Behavior detection tool for Rust. It can run binaries
and test suites of cargo projects and detect unsafe code that fails to
uphold its safety requirements.

`Link to Miri <https://github.com/rust-lang/miri>`_


Conclusions for S-CORE
----------------------

The current baseline includes general Rust safety and security topics together
with related rules and recommendations. The results summarized below show how
each topic is captured in practice, including automated checks (by tool and tool option) and supporting
process measures. Where no automated check exists, coverage is captured
through manual review, process controls, or architecture decisions.

In general, fulfilling the required coverage for the safety and security topics
requires automated checks (CodeQL, Clippy, ``rustc`` and related tooling)
together with process controls (reviews, architecture records, and focused
tests).

Application of these guidelines follows the S-CORE software development,
verification, and change management processes; their requirements are not
repeated here.

Coverage status is summarized as follows:

* High coverage for automated coding checks and security checks, including lint
  profiles, CodeQL analysis, and S-CORE dependency and SBOM controls.
* High coverage for runtime robustness checks (panic policy, overflow checks,
  and ``Result``/``Option`` usage patterns).
* Medium to High coverage for tool confidence activities via TI/TD/TCL
  determination and qualification workflow where required.
* Medium coverage for topics that remain system-context dependent, in
  particular timing/WCET arguments and change-triggered re-validation scope.

The listed topics are covered at the level described in this document; complete
safety and security coverage remains dependent on the system context and the
applicable S-CORE processes.

Practical Traceability to Automated Checks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To keep the link from safety-oriented requirements to enforceable checks
explicit, S-CORE uses the following mapping from high level objective areas to
tool evidence:

* **Unsafe scope and API boundary robustness:**
  Clippy and CodeQL data-flow checks at unsafe/FFI boundaries.
* **Controlled runtime failure behavior:**
  Clippy, policy constraints on ``unwrap`` usage, and a Cargo release profile
  with overflow checks enabled.
* **Deterministic and reviewable interfaces:**
  Clippy and ``rustc``, together with documentation and review process
  controls.
* **Type and conversion correctness:**
  Clippy and project guidance to prefer explicit fallible or infallible
  conversions.
* **Concurrency and shared-state safety:**
  ``rustc`` checks for safe Rust, Clippy, and focused review and tests for
  synchronization, shared state, unsafe code, and FFI boundaries.
* **Input and resource robustness:**
  CodeQL data-flow analysis, explicit input validation, bounded resource use,
  and focused verification tests.
* **Cryptography and sensitive data:**
  CodeQL security analysis, dependency and SBOM controls, and security review
  for cryptographic use, secrets, logging, and data handling.
* **Security and supply-chain integrity:**
  CodeQL security queries, S-CORE dependency and SBOM controls, and configured
  Cargo profiles.
* **Change and qualification traceability:**
  TI/TD/TCL evaluation, Tool Verification Reports, and change-triggered
  re-validation via configuration management.

The topics listed above are addressed in S-CORE by the following tools and
practices. Within the S-CORE project, formatting and Clippy checks are enforced
by the central Rust policies. Miri is available for targeted undefined-behavior
analysis. The code should compile with zero warnings. Additional guidelines by
the Rust Community, the Rust Foundation and
the Safety-Critical Rust Consortium are applied where applicable but not
enforced. If possible the usage of `unsafe` is avoided. To keep the code
`panic`-free only APIs with a proper return value should be used.

Source usage note: normative decisions in this document are based on the
S-CORE process and MISRA references (including
`MISRA C:2025 Addendum 6 Applicability of MISRA C:2025 to the Rust Programming Language <https://misra.org.uk/app/uploads/2025/03/MISRA-C-2025-ADD6.pdf>`_).
Research sources such as
`MISRust (arXiv:2605.23490v1), Table 3 <https://arxiv.org/html/2605.23490v1>`_
are used as supporting rationale for topic prioritization, not as normative
compliance criteria.

The recommended ``[lints.rust]``, ``[lints.clippy]``, and ``[profile.release]``
settings are maintained centrally in the
`score_rust_policies repository <https://github.com/eclipse-score/score_rust_policies>`_:

CodeQL is handled separately from this repository; see *Rust Tooling: CodeQL*
above and :doc:`/platform_management_plan/software_verification`.

* `Practical baseline (relaxed) <https://github.com/eclipse-score/score_rust_policies/blob/main/clippy/relaxed/Cargo.toml>`_ —
  suitable for general SCORE components.
* `Strict / ASIL variant <https://github.com/eclipse-score/score_rust_policies/blob/main/clippy/strict/Cargo.toml>`_ —
  for safety-critical code requiring stricter enforcement.

Rust Tooling Configuration and Evidence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The settings below are thematically aligned with the Safety-Critical Rust
Coding Guidelines, especially their sections on errors, concurrency, unsafety,
FFI, compilation, and compliance.

The concrete ``rustc`` and Clippy lints, their levels, and the release profile
are project policy decisions maintained in ``score_rust_policies``. The
following external, authoritative sources document the semantics and effects of
those settings and can be used as technical evidence for the safety and
security argument (the CodeQL sources are already linked in the *Rust Tooling:
CodeQL* section above):

The following table maps every active option in the strict/ASIL policy to the
public guideline topics and to the condition described by its official tool
documentation. The relaxed policy uses the same active option set, with a
different policy intent for the compiler and Clippy levels where documented.
Commented-out, toolchain-dependent candidates are not active options and are
therefore excluded.

.. list-table:: Guideline topics and complete configured tool checks
   :header-rows: 1
   :widths: 20 32 27 28 10

   * - Guideline topic
     - Complete configured options
     - Detected condition or test
     - Safety/security relevance
     - Level
   * - Types, traits, generics, and conversions
     - ``elided_lifetimes_in_paths``; ``explicit_outlives_requirements``; ``redundant_lifetimes``; ``single_use_lifetimes``; ``cast_lossless``; ``cast_possible_truncation``; ``cast_possible_wrap``; ``cast_sign_loss``; ``cast_ptr_alignment``; ``as_conversions``
     - Hidden or redundant lifetime bounds, unnecessary casts, lossy conversions, pointer alignment risks, and conversion choices are diagnosed.
     - Prevents unclear lifetime contracts, data corruption, and invalid pointer access at safety- or FFI-relevant boundaries.
     - Warn/allow
   * - Patterns, expressions, values, and statements
     - ``unused``; ``unit_bindings``; ``trivial_numeric_casts``; ``redundant_type_annotations``; ``float_cmp``; ``lossy_float_literal``
     - Unused code and results, useless unit bindings, redundant annotations or casts, exact floating-point comparisons, and lossy literals are diagnosed.
     - Reduces unnoticed logic defects, incorrect comparisons, and numerical behavior that can affect deterministic safety functions.
     - Warn
   * - Functions, associated items, and implementations
     - ``missing_docs``; ``missing_errors_doc``; ``missing_docs_in_private_items``; ``missing_panics_doc``; ``panic_in_result_fn``; ``exit``; ``infinite_loop``; ``try_err``
     - Missing API documentation, panic-prone ``Result`` functions, process exits, unconditional loops, and suspicious error propagation are diagnosed.
     - Makes failure behavior reviewable and reduces uncontrolled termination, hangs, and undocumented safety assumptions.
     - Warn/deny
   * - Attributes, entities, and resolution
     - ``unreachable_pub``; ``unnameable_types``; ``macro_use_extern_crate``; ``meta_variable_misuse``; ``non_local_definitions``; ``shadow_reuse``; ``shadow_unrelated``; ``shadow_same``; ``allow_attributes``; ``implicit_return``
     - Unreachable or unnameable public interfaces, macro definition problems, non-local definitions, shadowing, and configured attribute or return-style policies are checked.
     - Prevents review gaps, unintended API behavior, and macro or name-resolution defects that can alter safety-relevant code.
     - Warn/allow
   * - Ownership and destruction
     - ``let_underscore_drop``; ``mem_forget``
     - Immediate destruction caused by non-binding ``let`` and bypassing destructors are diagnosed.
     - Prevents premature lock release, resource leaks, and skipped cleanup that can violate synchronization or resource-safety assumptions.
     - Warn
   * - Exceptions and errors
     - ``unused_results``; ``let_underscore_must_use``; ``missing_panics_doc``; ``panic_in_result_fn``; ``unwrap_used``; ``panicking_overflow_checks``
     - Ignored return values, undocumented panics, panic-prone ``Result`` functions, unwraps, and arithmetic overflow checks are applied.
     - Makes error handling explicit and prevents unchecked failures, silent arithmetic faults, and loss of diagnostic or safety information.
     - Warn/deny
   * - Concurrency and shared state
     - ``let_underscore_drop``; ``iter_over_hash_type``
     - Accidental early destruction of guards and nondeterministic hash iteration are diagnosed; synchronization correctness still requires tests and review.
     - Reduces lock-lifetime and nondeterminism hazards; data-race freedom cannot be established by these options alone.
     - Warn/partial
   * - Program structure and compilation
     - ``missing_abi``; ``variant_size_differences``; ``format_push_string``; ``invalid_upcast_comparisons``; ``ptr_cast_constness``; ``ref_as_ptr``; ``transmute_ptr_to_ptr``; ``as_underscore``
     - ABI omissions, excessive enum layout differences, string-building inefficiency, invalid comparisons, and pointer conversion hazards are diagnosed.
     - Prevents ABI mismatches, representation errors, and pointer misuse that can cause undefined behavior or unsafe interoperability.
     - Warn
   * - Unsafety
     - ``unsafe_op_in_unsafe_fn``; ``undocumented_unsafe_blocks``; ``as_ptr_cast_mut``; ``declare_interior_mutable_const``
     - Unsafe operations without explicit blocks, undocumented unsafe blocks, mutable pointer casts, and interior-mutable constants are diagnosed.
     - Restricts and exposes the highest-risk code where memory safety, aliasing, and undefined behavior must be justified.
     - Deny
   * - FFI
     - ``missing_abi``; ``ptr_cast_constness``; ``ref_as_ptr``; ``transmute_ptr_to_ptr``; ``cast_ptr_alignment``
     - Missing ABI declarations and selected pointer/interface hazards at foreign-function boundaries are diagnosed.
     - Prevents calling-convention, layout, lifetime, and pointer-contract violations across language boundaries.
     - Warn/partial
   * - Macros
     - ``meta_variable_misuse``; ``macro_use_extern_crate``
     - Possible macro metavariable errors and deprecated macro imports are diagnosed.
     - Reduces generated-code defects and hidden dependency behavior that may evade ordinary source review.
     - Warn
   * - Imports, interfaces, and reviewability
     - ``wildcard_imports``; ``wildcard_enum_match_arm``; ``missing_docs``; ``unreachable_pub``; ``unnameable_types``
     - Ambiguous or overly broad imports and matches, missing public documentation, and inconsistent public visibility are diagnosed.
     - Keeps interfaces and control flow explicit, improving reviewability of safety- and security-relevant behavior.
     - Warn/deny
   * - Inline assembly
     - No dedicated active option
     - The current policy has no configured inline-assembly check; target-specific review is required.
     - Incorrect registers, constraints, or memory effects can bypass Rust safety guarantees and require target-specific analysis.
     - Process
   * - Cargo release behavior
     - ``[profile.release] overflow-checks = true``
     - Runtime integer overflow in release builds causes a panic instead of wrapping silently.
     - Prevents silent numeric corruption in production safety calculations; the resulting panic still requires system-level handling.
     - Required
   * - Policy configuration
     - ``clippy.toml`` ``msrv = "1.90.0"``; strict ``check-private-items = true``
     - Clippy applies MSRV-aware suggestions and checks private items in the strict profile.
     - Keeps diagnostics reproducible and prevents undocumented private implementation defects from escaping the selected analysis scope.
     - Configuration
   * - Compliance and process
     - SCRC compliance categories; S-CORE review, verification, and change-management processes
     - Deviations, evidence, and changes are handled by process rather than by a compiler lint.
     - Provides the evidence, review, and deviation control needed for risks that static analysis cannot decide.
     - Process

The strict profile uses ``deny`` for selected hard safety or correctness
constraints, ``warn`` where migration effort or context requires review, and
``allow`` where a rule is too coarse or project context determines applicability.

The following list contains the official Rust and Clippy references and the options from above per tool:

* `Clippy lint index <https://rust-lang.github.io/rust-clippy/master/index.html>`_ —
  the complete, searchable catalogue of Clippy lints. Every Clippy lint selected
  in ``score_rust_policies`` (for example ``undocumented_unsafe_blocks``,
  ``missing_panics_doc``, ``wildcard_imports``, ``declare_interior_mutable_const``,
  ``unwrap_used``, ``panic_in_result_fn``, ``let_underscore_must_use``,
  ``wildcard_enum_match_arm`` and the ``cast_*``, ``shadow_*`` and pointer-cast
  families) is listed here with its lint group and default level.
* `Clippy configuration <https://doc.rust-lang.org/clippy/configuration.html>`_ —
  documents the ``clippy.toml`` options used by the policy, including ``msrv``
  and per-lint configuration, and how lint levels are applied.
* `rustc lint listing <https://doc.rust-lang.org/rustc/lints/listing/>`_ —
  the compiler's built-in lints, split into
  `allowed-by-default <https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html>`_
  and `warn-by-default <https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html>`_.
  This documents the ``rustc`` lints enabled by the policy, including
  ``unsafe_op_in_unsafe_fn`` (denied in the strict profile), ``unreachable_pub``,
  ``missing_docs``, ``unused_results``, ``let_underscore_drop``,
  ``elided_lifetimes_in_paths``, ``single_use_lifetimes``,
  ``trivial_numeric_casts``, ``unit_bindings``, ``unnameable_types``,
  ``variant_size_differences`` and the ``unused`` group.
* `Cargo manifest: the [lints] section <https://doc.rust-lang.org/cargo/reference/manifest.html#the-lints-section>`_ —
  documents the ``[lints.rust]`` and ``[lints.clippy]`` tables and the
  ``level`` / ``priority`` semantics used by the policy profiles.
* `Cargo profiles reference <https://doc.rust-lang.org/cargo/reference/profiles.html>`_ —
  documents the ``overflow-checks`` profile setting used in the policy's
  ``[profile.release]`` (``overflow-checks = true``). Note that Cargo's release
  profile defaults to ``overflow-checks = false``, so the policy sets it
  explicitly.

Explanation of ARA Applications in Rust
---------------------------------------

AUTOSAR also shares a publicly available document that explains how to use Rust
in ARA applications as Rust offers safety and performance advantages. While
ecosystem support is still maturing, Rust-based ARA applications can lead to
safer, more reliable automotive software, especially in safety-critical and
high-performance domains.

`AUTOSAR ARA Applications in Rust <https://www.autosar.org/fileadmin/standards/R24-11/AP/AUTOSAR_AP_EXP_ARARustApplications.pdf>`_
