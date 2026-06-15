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

Writing Rust Code incl. Coding Guidelines
#########################################

.. document:: Coding Guidelines Rust
   :id: doc__rust_coding_guidelines
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan


Safety Rust
===========

For writing Rust code in SCORE, especially for safety- and
security-relevant software, the following guidance and tooling references
apply.


Coding Guidelines
-----------------

The following coding guidelines and reference documents are relevant for
Rust development in SCORE:

* `JA1020_202603: Safety and Cybersecurity Recommendations for the Use of the Rust Language in Critical Systems <https://saemobilus.sae.org/standards/ja1020_202603-safety-cybersecurity-recommendations-use-rust-language-critical-systems#view>`_
   is the primary baseline for safety- and security-related Rust development and in arguing safety according to ISO 26262 or RTCA DO-178C combined with RTCA DO-332. The current version of JA1020 is from March 2026 and is expected to be updated in the future, with the next version planned for late 2026. It provides a comprehensive set of recommendations for using Rust in safety-critical systems, covering topics such as language features, coding practices, and tool usage.
* `Safety-Critical Rust Coding Guidelines <https://coding-guidelines.arewesafetycriticalyet.org/>`_
   are still under development and currently only define a subset of the
   desired rules.
* `Secure Rust Guidelines (unstable) <https://anssi-fr.github.io/rust-guide/>`_
   complement JA1020. ANSSI focuses more on process and architecture
   guidance, while JA1020 is more concrete regarding tool usage and
   enforceable checks.
* `Linux Kernel Rules <https://www.kernel.org/doc/Documentation/rust/coding-guidelines.rst>`_
   mainly define formatting and documentation requirements for Rust in the
   Linux kernel and do not provide broader static code analysis rules.
* `MISRA C:2025 Addendum 6, Applicability of MISRA C:2025 to the Rust Programming Language <https://misra.org.uk/app/uploads/2025/03/MISRA-C-2025-ADD6.pdf>`_
   overlaps strongly with JA1020 and is therefore primarily relevant as an
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

`Safety-Critical Coding Guidelines <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines>`_

`Deployed version of Safety-Critical Coding Guidelines <https://coding-guidelines.arewesafetycriticalyet.org/>`_

`Safety-Critical Rust Consortium <https://rustfoundation.org/safety-critical-rust-consortium>`_

`Safety-Critical Rust Consortium Guidelines <https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines/>`_

`Learn unsafe Rust <https://google.github.io/learn_unsafe_rust/>`_

`Rust language <https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html>`_

The linked document provides a current overview of the tooling landscape for
certifying Rust in safety-critical applications, presenting a
community-approved list of essential tools and tracking their development
status. It also explores whether developing specialized training curricula for
safety-critical Rust is necessary, potentially requiring a separate
subcommittee. The document details the state of specific tools, such as
compilers and analysis utilities, by outlining their intended purposes,
certification requirements, and their availability or progress. While some
tools, such as the Ferrocene compiler, are already available or being actively
developed, others remain under evaluation or are not yet accessible.

`Mission Statement - Tooling Subcommittee <https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/tooling/mission-statement.md>`_


MISRA vs CERT
-------------

This issue contrasts the MISRA and CERT coding standards, highlighting their
different approaches to software safety and security. MISRA is noted for its
restrictive language subsetting and complex compliance process, often imposing
outdated or ineffective rules that do not guarantee improved safety or
security. This can create unnecessary work for developers without clear
benefits and is sometimes inconsistent across languages. CERT, on the other
hand, is praised for its focus on practical, consensus-based rules that target
real security vulnerabilities in existing code, avoiding excessive constraints.
The overall recommendation is to favor guidelines like CERT's: practical,
evidence-based, and focused on real-world issues, over rigid, untested
standards that hinder adoption and developer productivity.

`MISRA vs Cert <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/75/>`_

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
https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
and https://codeql.github.com/codeql-query-help/rust-cwe/).

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

The SAE JA1020 Appendix A.2 contains some rules and recommendations related to the automated tools that support its enforcement. The following table summarizes the coverage of these tools. Where no automated tool exists, the coverage column reflects the need for manual review, process controls, or architecture decisions.

The classification follows the MISRA convention used by SAE JA1020:

    Required — Mandatory. Deviations need documented reasoning.
    Advisory — Recommended. Deviations should be documented when practical.
    Document — The decision and its reasoning must be documented regardless of outcome.

The matrix below summarizes overall coverage per topic. The `Cargo.toml`
profiles further below are practical baseline and intentionally
contains the by JA1020 recommended subset of checks.


.. csv-table:: Overlap Summary Matrix (JA1020_202603 Measures)
   :header: "Name", "Type", "Automated (JA1020)", "Section", "CodeQL", "Clippy", "Rustc", "Other Tooling / Process", "Combined"
   :widths: 24, 14, 12, 10, 10, 18, 18, 22, 8

   "Compiler qualification", "Document, Required", "-", "6.1, 13.1", "-", "-", "-", "Process/evidence", "M"
   "Dependency management", "Required", "-", "6.1.1, 6.2.8, 6.4.18, 13.1", "-", "-", "-", "cargo-audit, cargo-deny, cargo-vet, SBOM", "H"
   "async/await decision", "Document, Advisory", "-", "6.2.1", "-", "-", "-", "Architecture decision record", "M"
   "Extension trait guidelines", "Document, Advisory", "-", "6.2.2", "-", "-", "-", "Review guideline", "M"
   "Minimum Supported Rust Version", "Document, Advisory", "cargo plugin", "6.2.3", "-", "-", "M (stable toolchain pinning, rust-version policy)", "Toolchain pinning in CI", "H"
   "Shadowing style", "Document, Advisory", "Partially, clippy", "6.2.4, 6.3.4", "-", "M (shadow_reuse/shadow_unrelated as warn, shadow_same as allow)", "-", "Review style guide", "M"
   "Code review environment", "Advisory", "-", "6.2.5", "-", "-", "-", "Process/tooling setup", "M"
   "Macro review and testing strategy", "Document, Advisory", "-", "6.2.6", "-", "-", "-", "Tests, trybuild, review", "M"
   "Module file naming", "Document, Advisory", "Partially", "6.2.7", "-", "L (no strong built-in lint)", "-", "Custom checks", "M"
   "Default trait implementations", "Document, Advisory", "-", "6.2.9", "-", "-", "-", "Design guideline", "M"
   "Usage of unwrap in mutex lock", "Document, Advisory", "-", "6.2.10.1", "-", "M (unwrap_used with documented exception policy)", "-", "Review policy", "M"
   "Document undesirable but not unsafe hardware effects", "Advisory", "-", "6.2.10.2", "-", "-", "-", "Safety documentation", "M"
   "FFI: Check values at boundary", "Required", "-", "6.3.1, 6.3.1.3", "-", "-", "-", "FFI tests, fuzzing, review", "M"
   "Safe wrapper for unsafe interfaces", "Required", "-", "6.3.1", "-", "-", "-", "Design/review", "M"
   "Document unsafe assumptions in Safety: clause", "Required", "clippy", "6.3.1", "-", "H (undocumented_unsafe_blocks)", "-", "-", "H"
   "Minimal scope for unsafe", "Required", "-", "6.3.1", "-", "M (policy/review support, no single strong lint)", "-", "cargo-geiger, review", "M"
   "Unsafe block in unsafe function", "Required", "clippy", "6.3.1", "-", "M (supporting only, project-dependent)", "H (unsafe_op_in_unsafe_fn)", "-", "H"
   "Safety documentation for unsafe functions", "Required", "clippy", "6.3.1", "-", "M (manual documentation/review in profile baseline)", "-", "Rustdoc + review process", "M"
   "Panic documentation on functions", "Required", "clippy", "6.3.1", "-", "H (missing_panics_doc)", "-", "-", "H"
   "Global mutable state with sound wrapper", "Required", "-", "6.3.1.1", "-", "-", "-", "Review/design", "M"
   "FFI rules from ANSII", "Required", "-", "6.3.1.2", "-", "-", "-", "FFI conformance process", "M"
   "Inline assembly rules from reference", "Required", "-", "6.3.1.4", "-", "-", "-", "Manual asm review", "M"
   "Automated contract versioning", "Advisory", "symbols", "6.3.1.5", "-", "-", "-", "Symbol/ABI diff tooling", "H"
   "Pointer to reference conversion", "Required", "-", "6.3.1.6", "M", "M (cast_ptr_alignment, ptr_cast_constness, ref_as_ptr, transmute_ptr_to_ptr)", "M (invalid_reference_casting plus diagnostics)", "Review/tests", "M"
   "Define proper panic handling", "Document, Required", "-", "6.3.2, 6.4.12", "-", "M (panic_in_result_fn as warn; unwrap_used and panicking_overflow_checks evaluated for usefulness)", "M (panic strategy/profile settings)", "Panic strategy in CI/profile", "H"
   "catch_unwind only for controlled shutdown", "Required", "-", "6.3.2", "-", "L (no direct strong lint)", "-", "Review policy", "M"
   "Deref misuse for inheritance", "Required", "-", "6.3.3", "-", "L (no direct strong lint)", "-", "Review/style", "M"
   "Transitive interior mutability documentation", "Advisory", "-", "6.3.5", "-", "-", "-", "Documentation process", "M"
   "No internal mutability in constants", "Required", "-", "6.3.5", "-", "H (declare_interior_mutable_const)", "-", "-", "H"
   "Prefer cfg!() over #[cfg()]", "Required", "-", "6.3.6", "-", "-", "-", "Review/custom linting", "M"
   "Features are additive, not exclusive", "Required", "-", "6.3.6", "-", "-", "-", "Cargo feature CI checks", "H"
   "No deprecated interfaces from core/std", "Required", "-", "6.3.7", "-", "M (deprecated in lint profile)", "H (deprecated)", "-", "H"
   "No nightly features", "Required", "rustc", "6.3.8", "-", "-", "H (stable compiler policy; unstable_features on nightly)", "Stable toolchain enforcement", "H"
   "No wildcard in imports", "Required", "clippy", "6.3.9", "-", "H (wildcard_imports)", "-", "-", "H"
   "Ensure formatting and lints (e.g., in CI)", "Advisory", "rustfmt + clippy", "6.4.1", "-", "H (CI clippy gate)", "-", "rustfmt in CI", "H"
   "No raw identifiers", "Required", "grep", "6.4.1", "-", "-", "-", "grep/custom check", "H"
   "Rustc linter", "Advisory", "rustc", "6.4.2", "-", "-", "H (JA1020-curated rustc baseline profile; extended edition/future lints enabled per toolchain support)", "-", "H"
   "Clippy linter", "Advisory", "clippy", "6.4.3", "-", "H (JA1020 curated warn/deny/allow clippy profile)", "-", "-", "H"
   "Strong typing for error detection at compile time", "Advisory", "-", "6.4.5", "-", "-", "H (type system, borrow checker, trait bounds)", "-", "H"
   "Structures replace many arguments", "Advisory", "-", "6.4.5.2", "-", "L (style/review guidance)", "-", "Review/style", "M"
   "Testing trait requirements on trait implementations", "Required", "-", "6.4.6", "-", "-", "-", "Tests/property tests", "H"
   "Test coverage on generics", "Advisory", "coverage", "6.4.7, 10.1", "-", "-", "-", "Coverage tooling", "H"
   "Avoid as for conversions", "Required", "clippy", "6.4.9", "-", "H (as_underscore, cast_lossless, cast_possible_truncation, cast_possible_wrap, cast_ptr_alignment, cast_sign_loss)", "-", "-", "H"
   "Error/Option instead of magic values", "Advisory", "-", "6.4.10", "-", "M (partial style support)", "M (type checks support pattern, no direct rule)", "Review", "M"
   "Resource Acquisition Is Initialization", "Required", "-", "6.4.11", "-", "-", "M (ownership and Drop semantics, no direct lint)", "Review/tests", "M"
   "Overflow checking", "Required", "rustc", "6.4.12", "-", "-", "H (release overflow-checks enabled)", "Release profile setting", "H"
   "Dynamic memory design", "Required", "-", "6.4.13", "-", "-", "-", "Allocator/system design checks", "M"
   "Stack checking", "Required", "rustc", "6.4.13", "-", "-", "M (limited compiler support)", "cargo-call-stack, external analysis", "M"
   "Concurrency system design (timing constraints)", "Required", "-", "6.4.14, 6.4.15.4", "-", "-", "-", "loom, WCET, system analysis", "M"
   "Document cancellation safety of async functions", "Advisory", "-", "6.4.15.1", "-", "-", "-", "Documentation/review", "M"
   "Explicit task dropping intention", "Advisory", "-", "6.4.15.3", "-", "L (let_underscore_future as supporting signal)", "-", "Runtime policy/review", "M"
   "Planning ahead for Pin/Send", "Document, Advisory", "-", "6.4.15.5", "-", "-", "M (Send and lifetime trait-bound checks)", "Design constraints review", "M"
   "Minimize duplicated dependencies because of versioning", "Required", "cargo", "6.4.16", "-", "-", "-", "cargo tree, cargo-deny", "H"
   "Minimal scope for symbols", "Advisory", "(clippy)", "6.4.16", "-", "M (redundant_pub_crate as supporting signal)", "M (unreachable_pub, visibility diagnostics)", "Visibility checks/review", "M"
   "Multi-crate design to minimize cyclic dependencies", "Advisory", "-", "6.4.16", "-", "-", "-", "cargo graph, dependency analysis", "M"
   "Usize should only measure memory, not environment quantities", "Required", "-", "6.4.17", "-", "L (no direct strong lint)", "-", "Review/style", "M"
   "Separation of download and build steps", "Advisory", "-", "6.4.18", "-", "-", "-", "CI sandboxing/pipeline controls", "H"
   "Special protection of sensitive data", "Advisory", "-", "6.4.19", "H", "-", "-", "Secret handling process", "H"
   "Marker traits for formal documentation", "Advisory", "-", "6.4.21", "-", "-", "M (trait-bound enforcement mechanism)", "Review/formal method support", "M"
   "Lifetime and pointers", "Advisory", "-", "6.4.23.1", "M", "-", "H (borrow checker, lifetime analysis)", "-", "H"
   "Atomic access modes", "Advisory", "-", "6.4.23.2", "-", "L (no explicit lint in current JA1020 profile block)", "-", "Review for ordering rationale", "M"
   "Unintended matches", "Advisory", "-", "6.4.23.3", "-", "M (wildcard_enum_match_arm)", "M (non_exhaustive_omitted_patterns)", "-", "M"
   "Logically significant return values should be #[must_use]", "Required", "-", "9.1", "-", "M (let_underscore_must_use)", "M (unused_results in profile; must_use semantics by language)", "-", "M"
   "Complex drop logic should be called explicitly", "Required", "-", "9.2", "-", "L (no direct strong lint)", "-", "Review/tests", "M"


During the S-CORE project formatting and clippy checks are enforced. Miri can
be used to detect undefined behaviors. Also the code should compile with zero
warnings. Additional guidelines by the Rust Community, the Rust Foundation and
the Safety-Critical Rust Consortium are applied where applicable but not
enforced. If possible the usage of `unsafe` is avoided. To keep the code
`panic`-free only APIs with a proper return value should be used. The goal is
to have coding guidelines for Rust suitable for safety-critial systems by the
Safety-Critical Rust Consortium by the end of 2026. Until that, please also
use Slack score-rust-community channel for discussions and participation in the
SCRC.

The adaption of these guidelines will be documented in the S-CORE project
documentation.

.. admonition:: Cargo.toml lint profile (JA1020-oriented, practical baseline)

   .. code-block:: toml

      # Cargo.toml

      # Rust compiler lints (rustc)
      [lints.rust]
      unsafe_op_in_unsafe_fn = "deny"
      missing_abi = "warn"
      unreachable_pub = "warn"
      missing_docs = "warn"
      unused_results = "warn"
      let_underscore_drop = "warn"
      non_exhaustive_omitted_patterns = "warn"

      # Rustc lints recommended to evaluate as warn (JA1020)
      elided_lifetimes_in_paths = "warn"
      explicit_outlives_requirements = "warn"
      macro_use_extern_crate = "warn"
      meta_variable_misuse = "warn"
      non_local_definitions = "warn"
      redundant_lifetimes = "warn"
      single_use_lifetimes = "warn"
      trivial_numeric_casts = "warn"
      unit_bindings = "warn"
      unnameable_types = "warn"
      variant_size_differences = "warn"

      # Edition and compatibility lint groups (JA1020 intent)
      # Enable rust-<YEAR>-* and keyword-idents-<YEAR> lints supported by the
      # pinned compiler version.
      unused = { level = "warn", priority = -1 }

      # Future/availability-dependent rustc lints (enable when available in
      # the selected toolchain)
      # must_not_suspend = "warn"
      # fuzzy_provenance_casts = "warn"
      # lossy_provenance_casts = "warn"

      # Clippy lints
      [lints.clippy]
      # Warn
      as_underscore = "warn"
      cast_lossless = "warn"
      cast_possible_truncation = "warn"
      cast_possible_wrap = "warn"
      cast_sign_loss = "warn"
      cast_ptr_alignment = "warn"
      exit = "warn"
      format_push_string = "warn"
      infinite_loop = "warn"
      iter_over_hash_type = "warn"
      invalid_upcast_comparisons = "warn"
      lossy_float_literal = "warn"
      missing_errors_doc = "warn"
      missing_docs_in_private_items = "warn"
      panic_in_result_fn = "warn"
      ptr_cast_constness = "warn"
      ref_as_ptr = "warn"
      transmute_ptr_to_ptr = "warn"
      redundant_type_annotations = "warn"
      shadow_reuse = "warn"
      shadow_unrelated = "warn"
      try_err = "warn"
      wildcard_enum_match_arm = "warn"

      # Deny
      as_ptr_cast_mut = "deny"
      let_underscore_must_use = "deny"
      missing_panics_doc = "deny"
      undocumented_unsafe_blocks = "deny"
      wildcard_imports = "deny"
      declare_interior_mutable_const = "deny"

      # Allow
      shadow_same = "allow"
      implicit_return = "allow"
      allow_attributes = "allow"

      # Evaluate for helpfulness (JA1020)
      panicking_overflow_checks = "warn"
      unwrap_used = "warn"

      # Recommended against because too coarse (JA1020)
      as_conversions = "allow"

      # Release profile requirement
      [profile.release]
      overflow-checks = true   # Required for safety-oriented integer checks

      # Checking of documentation on private items (in clippy.toml)
      # check-private-items = true


.. admonition:: Cargo.toml lint profile (JA1020-oriented, strict/ASIL variant)

   .. code-block:: toml

      # Cargo.toml

      # Rust compiler lints (strict)
      [lints.rust]
      unsafe_op_in_unsafe_fn = "deny"
      missing_abi = "warn"
      unreachable_pub = "warn"
      missing_docs = "warn"
      unused_results = "warn"
      let_underscore_drop = "warn"
      non_exhaustive_omitted_patterns = "warn"

      # Rustc lints recommended to evaluate as warn (JA1020)
      elided_lifetimes_in_paths = "warn"
      explicit_outlives_requirements = "warn"
      macro_use_extern_crate = "warn"
      meta_variable_misuse = "warn"
      non_local_definitions = "warn"
      redundant_lifetimes = "warn"
      single_use_lifetimes = "warn"
      trivial_numeric_casts = "warn"
      unit_bindings = "warn"
      unnameable_types = "warn"
      variant_size_differences = "warn"

      # Edition and compatibility lint groups (JA1020 intent)
      unused = { level = "warn", priority = -1 }

      # Clippy lints (strict)
      [lints.clippy]
      # Warn
      as_underscore = "warn"
      cast_lossless = "warn"
      cast_possible_truncation = "warn"
      cast_possible_wrap = "warn"
      cast_sign_loss = "warn"
      cast_ptr_alignment = "warn"
      exit = "warn"
      format_push_string = "warn"
      infinite_loop = "warn"
      iter_over_hash_type = "warn"
      invalid_upcast_comparisons = "warn"
      lossy_float_literal = "warn"
      missing_errors_doc = "warn"
      missing_docs_in_private_items = "warn"
      panic_in_result_fn = "warn"
      ptr_cast_constness = "warn"
      ref_as_ptr = "warn"
      transmute_ptr_to_ptr = "warn"
      redundant_type_annotations = "warn"
      shadow_reuse = "warn"
      shadow_unrelated = "warn"
      try_err = "warn"
      wildcard_enum_match_arm = "warn"

      # Deny
      as_ptr_cast_mut = "deny"
      let_underscore_must_use = "deny"
      missing_panics_doc = "deny"
      undocumented_unsafe_blocks = "deny"
      wildcard_imports = "deny"
      declare_interior_mutable_const = "deny"

      # Allow
      shadow_same = "allow"
      implicit_return = "allow"
      allow_attributes = "allow"

      # Evaluate for helpfulness (JA1020)
      panicking_overflow_checks = "warn"
      unwrap_used = "warn"

      # Recommended against because too coarse (JA1020)
      as_conversions = "allow"

      # Release profile requirement
      [profile.release]
      overflow-checks = true

      # clippy.toml
      # check-private-items = true


Explanation of ARA Applications in Rust
=======================================

AUTOSAR also shares a public available document that explains how to use Rust in
ARA applications as Rust is offering safety and performance advantages. While
ecosystem support is still maturing, Rust-based ARA applications can lead to
safer, more reliable automotive software, especially in safety-critical and
high-performance domains.

`AUTOSAR ARA Applications in Rust <https://www.autosar.org/fileadmin/standards/R24-11/AP/AUTOSAR_AP_EXP_ARARustApplications.pdf>`_
