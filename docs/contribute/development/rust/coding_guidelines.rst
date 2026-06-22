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

* A safety- and cybersecurity-oriented Rust baseline is used as the primary
   reference for safety- and security-related development and for arguing
   safety according to ISO 26262 or RTCA DO-178C combined with RTCA DO-332.
   It provides a comprehensive set of recommendations for using Rust in
   safety-critical systems, including language features, coding practices, and
   tool usage.
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

The current baseline includes general Rust safety and security topics together
with related rules and recommendations. The following table shows how each
topic is captured in practice, including automated checks (by tool and tool option) and supporting
process measures. Where no automated check exists, coverage is captured
through manual review, process controls, or architecture decisions.

The classification follows a MISRA-style convention:

*   Required — Mandatory. Deviations need documented reasoning.
*   Advisory — Recommended. Deviations should be documented when practical.
*   Document — The decision and its reasoning must be documented regardless of outcome.

The matrix below summarizes overall coverage for these topics. The
`Cargo.toml` profiles further below provide a practical baseline and
intentionally contain a recommended subset of checks.

.. csv-table:: Overlap Summary Matrix (Baseline Measures)
   :header: "Name", "Type", "Automated (Baseline)", "CodeQL", "Clippy", "Rustc", "Other Tooling / Process", "Combined"
   :widths: 24, 14, 12, 10, 18, 18, 22, 8

   "Compiler qualification", "Document, Required", "-", "-", "-", "-", "Process/evidence", "M"
   "Dependency management", "Required", "-", "-", "-", "-", "cargo-audit, cargo-deny, cargo-vet, SBOM", "H"
   "async/await decision", "Document, Advisory", "-", "-", "-", "-", "Architecture decision record", "M"
   "Extension trait guidelines", "Document, Advisory", "-", "-", "-", "-", "Review guideline", "M"
   "Minimum Supported Rust Version", "Document, Advisory", "cargo plugin", "-", "-", "M (stable toolchain pinning, rust-version policy)", "Toolchain pinning in CI", "H"
   "Shadowing style", "Document, Advisory", "Partially, clippy", "-", "M (shadow_reuse/shadow_unrelated as warn, shadow_same as allow)", "-", "Review style guide", "M"
   "Code review environment", "Advisory", "-", "-", "-", "-", "Process/tooling setup", "M"
   "Macro review and testing strategy", "Document, Advisory", "-", "-", "-", "-", "Tests, trybuild, review", "M"
   "Module file naming", "Document, Advisory", "Partially", "-", "L (no strong built-in lint)", "-", "Custom checks", "M"
   "Default trait implementations", "Document, Advisory", "-", "-", "-", "-", "Design guideline", "M"
   "Usage of unwrap in mutex lock", "Document, Advisory", "-", "-", "M (unwrap_used with documented exception policy)", "-", "Review policy", "M"
   "Document undesirable but not unsafe hardware effects", "Advisory", "-", "-", "-", "-", "Safety documentation", "M"
   "FFI: Check values at boundary", "Required", "-", "-", "-", "-", "FFI tests, fuzzing, review", "M"
   "Safe wrapper for unsafe interfaces", "Required", "-", "-", "-", "-", "Design/review", "M"
   "Document unsafe assumptions in Safety: clause", "Required", "clippy", "-", "H (undocumented_unsafe_blocks)", "-", "-", "H"
   "Minimal scope for unsafe", "Required", "-", "-", "M (policy/review support, no single strong lint)", "-", "cargo-geiger, review", "M"
   "Unsafe block in unsafe function", "Required", "clippy", "-", "M (supporting only, project-dependent)", "H (unsafe_op_in_unsafe_fn)", "-", "H"
   "Safety documentation for unsafe functions", "Required", "clippy", "-", "M (manual documentation/review in profile baseline)", "-", "Rustdoc + review process", "M"
   "Panic documentation on functions", "Required", "clippy", "-", "H (missing_panics_doc)", "-", "-", "H"
   "Global mutable state with sound wrapper", "Required", "-", "-", "-", "-", "Review/design", "M"
   "FFI rules from ANSII", "Required", "-", "-", "-", "-", "FFI conformance process", "M"
   "Inline assembly rules from reference", "Required", "-", "-", "-", "-", "Manual asm review", "M"
   "Automated contract versioning", "Advisory", "symbols", "-", "-", "-", "Symbol/ABI diff tooling", "H"
   "Pointer to reference conversion", "Required", "-", "M", "M (cast_ptr_alignment, ptr_cast_constness, ref_as_ptr, transmute_ptr_to_ptr)", "M (invalid_reference_casting plus diagnostics)", "Review/tests", "M"
   "Define proper panic handling", "Document, Required", "-", "-", "M (panic_in_result_fn as warn; unwrap_used and panicking_overflow_checks evaluated for usefulness)", "M (panic strategy/profile settings)", "Panic strategy in CI/profile", "H"
   "catch_unwind only for controlled shutdown", "Required", "-", "-", "L (no direct strong lint)", "-", "Review policy", "M"
   "Deref misuse for inheritance", "Required", "-", "-", "L (no direct strong lint)", "-", "Review/style", "M"
   "Transitive interior mutability documentation", "Advisory", "-", "-", "-", "-", "Documentation process", "M"
   "No internal mutability in constants", "Required", "-", "-", "H (declare_interior_mutable_const)", "-", "-", "H"
   "Prefer cfg!() over #[cfg()]", "Required", "-", "-", "-", "-", "Review/custom linting", "M"
   "Features are additive, not exclusive", "Required", "-", "-", "-", "-", "Cargo feature CI checks", "H"
   "No deprecated interfaces from core/std", "Required", "-", "-", "M (deprecated in lint profile)", "H (deprecated)", "-", "H"
   "No nightly features", "Required", "rustc", "-", "-", "H (stable compiler policy; unstable_features on nightly)", "Stable toolchain enforcement", "H"
   "No wildcard in imports", "Required", "clippy", "-", "H (wildcard_imports)", "-", "-", "H"
   "Ensure formatting and lints (e.g., in CI)", "Advisory", "rustfmt + clippy", "-", "H (CI clippy gate)", "-", "rustfmt in CI", "H"
   "No raw identifiers", "Required", "grep", "-", "-", "-", "grep/custom check", "H"
   "Rustc linter", "Advisory", "rustc", "-", "-", "H (curated rustc baseline profile; extended edition/future lints enabled per toolchain support)", "-", "H"
   "Clippy linter", "Advisory", "clippy", "-", "H (curated warn/deny/allow clippy profile)", "-", "-", "H"
   "Strong typing for error detection at compile time", "Advisory", "-", "-", "-", "H (type system, borrow checker, trait bounds)", "-", "H"
   "Structures replace many arguments", "Advisory", "-", "-", "L (style/review guidance)", "-", "Review/style", "M"
   "Testing trait requirements on trait implementations", "Required", "-", "-", "-", "-", "Tests/property tests", "H"
   "Test coverage on generics", "Advisory", "coverage", "-", "-", "-", "Coverage tooling", "H"
   "Avoid as for conversions", "Required", "clippy", "-", "H (as_underscore, cast_lossless, cast_possible_truncation, cast_possible_wrap, cast_ptr_alignment, cast_sign_loss)", "-", "-", "H"
   "Error/Option instead of magic values", "Advisory", "-", "-", "M (partial style support)", "M (type checks support pattern, no direct rule)", "Review", "M"
   "Resource Acquisition Is Initialization", "Required", "-", "-", "-", "M (ownership and Drop semantics, no direct lint)", "Review/tests", "M"
   "Overflow checking", "Required", "rustc", "-", "-", "H (release overflow-checks enabled)", "Release profile setting", "H"
   "Dynamic memory design", "Required", "-", "-", "-", "-", "Allocator/system design checks", "M"
   "Stack checking", "Required", "rustc", "-", "-", "M (limited compiler support)", "cargo-call-stack, external analysis", "M"
   "Concurrency system design (timing constraints)", "Required", "-", "-", "-", "-", "loom, WCET, system analysis", "M"
   "Document cancellation safety of async functions", "Advisory", "-", "-", "-", "-", "Documentation/review", "M"
   "Explicit task dropping intention", "Advisory", "-", "-", "L (let_underscore_future as supporting signal)", "-", "Runtime policy/review", "M"
   "Planning ahead for Pin/Send", "Document, Advisory", "-", "-", "-", "M (Send and lifetime trait-bound checks)", "Design constraints review", "M"
   "Minimize duplicated dependencies because of versioning", "Required", "cargo", "-", "-", "-", "cargo tree, cargo-deny", "H"
   "Minimal scope for symbols", "Advisory", "(clippy)", "-", "M (redundant_pub_crate as supporting signal)", "M (unreachable_pub, visibility diagnostics)", "Visibility checks/review", "M"
   "Multi-crate design to minimize cyclic dependencies", "Advisory", "-", "-", "-", "-", "cargo graph, dependency analysis", "M"
   "Usize should only measure memory, not environment quantities", "Required", "-", "-", "L (no direct strong lint)", "-", "Review/style", "M"
   "Separation of download and build steps", "Advisory", "-", "-", "-", "-", "CI sandboxing/pipeline controls", "H"
   "Special protection of sensitive data", "Advisory", "-", "H", "-", "-", "Secret handling process", "H"
   "Marker traits for formal documentation", "Advisory", "-", "-", "-", "M (trait-bound enforcement mechanism)", "Review/formal method support", "M"
   "Lifetime and pointers", "Advisory", "-", "M", "-", "H (borrow checker, lifetime analysis)", "-", "H"
   "Atomic access modes", "Advisory", "-", "-", "L (no explicit lint in current baseline profile block)", "-", "Review for ordering rationale", "M"
   "Unintended matches", "Advisory", "-", "-", "M (wildcard_enum_match_arm)", "M (non_exhaustive_omitted_patterns)", "-", "M"
   "Logically significant return values should be #[must_use]", "Required", "-", "-", "M (let_underscore_must_use)", "M (unused_results in profile; must_use semantics by language)", "-", "M"
   "Complex drop logic should be called explicitly", "Required", "-", "-", "L (no direct strong lint)", "-", "Review/tests", "M"


During the S-CORE project formatting and clippy checks are enforced. Miri can
be used to detect undefined behaviors. Also the code should compile with zero
warnings. Additional guidelines by the Rust Community, the Rust Foundation and
the Safety-Critical Rust Consortium are applied where applicable but not
enforced. If possible the usage of `unsafe` is avoided. To keep the code
`panic`-free only APIs with a proper return value should be used. The goal is
to have coding guidelines for Rust suitable for safety-critical systems by the
Safety-Critical Rust Consortium by the end of 2026. Until that, please also
use Slack score-rust-community channel for discussions and participation in the
SCRC.

The adaption of these guidelines will be documented in the S-CORE project
documentation.

.. admonition:: Cargo.toml lint profile (safety-oriented, practical baseline)

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

      # Rustc lints recommended to evaluate as warn
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

      # Edition and compatibility lint groups (baseline intent)
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

      # Evaluate for helpfulness
      panicking_overflow_checks = "warn"
      unwrap_used = "warn"

      # Recommended against because too coarse
      as_conversions = "allow"

      # Release profile requirement
      [profile.release]
      overflow-checks = true   # Required for safety-oriented integer checks

      # Checking of documentation on private items (in clippy.toml)
      # check-private-items = true


.. admonition:: Cargo.toml lint profile (safety-oriented, strict/ASIL variant)

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

      # Rustc lints recommended to evaluate as warn
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

      # Edition and compatibility lint groups (baseline intent)
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

      # Evaluate for helpfulness
      panicking_overflow_checks = "warn"
      unwrap_used = "warn"

      # Recommended against because too coarse
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
