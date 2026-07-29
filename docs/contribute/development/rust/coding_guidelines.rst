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

This page provides the rationale, the guideline and tooling landscape, and a
project-wide set of practices for writing Rust in SCORE. The concrete,
enforceable rules (the ``rustc`` / Clippy lint configuration and the release
profile) are maintained centrally in the ``score_rust_policies`` repository and
are referenced from the `Conclusions for S-CORE`_ section below.


Coding Guidelines
-----------------

The following coding guidelines and reference documents are relevant for
Rust development in SCORE:

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

`Safety-Critical Coding Guidelines <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines>`_

`Deployed version of Safety-Critical Coding Guidelines <https://coding-guidelines.arewesafetycriticalyet.org/>`_

`Safety-Critical Rust Consortium <https://rustfoundation.org/safety-critical-rust-consortium>`_

`Safety-Critical Rust Consortium Guidelines <https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines/>`_

`Learn unsafe Rust <https://google.github.io/learn_unsafe_rust/>`_

`Rust language <https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html>`_

`Mission Statement - Tooling Subcommittee <https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/tooling/mission-statement.md>`_


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
with related rules and recommendations. The results summarized below show how
each topic is captured in practice, including automated checks (by tool and tool option) and supporting
process measures. Where no automated check exists, coverage is captured
through manual review, process controls, or architecture decisions.

The classification follows a MISRA-style convention:

* Required — Mandatory. Deviations need documented reasoning.
* Advisory — Recommended. Deviations should be documented when practical.
* Document — The decision and its reasoning must be documented regardless of outcome.

The summary below aggregates the overall coverage for these topics. The
`Cargo.toml` profiles further below provide a practical baseline and
intentionally contain a recommended subset of checks.

Summary of Results
~~~~~~~~~~~~~~~~~~~

The assessment covers different safety- and security-relevant topics from the
Rust baseline. For each topic the available automated checks (CodeQL, Clippy,
``rustc`` and other tooling) together with the supporting process measures were
rated for their combined overall coverage as High (H), Medium (M) or Low (L).

The topics group into the clusters below. None of them falls into the Low
category, so every topic is addressed by at least a solid combination of
tooling and process:

* **Unsafe code and FFI boundaries** — documenting and scoping ``unsafe``,
  safe wrappers, FFI value checks, inline assembly and raw-pointer/reference
  conversions. The enforceable parts reach High coverage through Clippy
  (``undocumented_unsafe_blocks``) and ``rustc`` (``unsafe_op_in_unsafe_fn``),
  with CodeQL adding data-flow checks at pointer/reference boundaries; the
  remaining boundary checks rely on FFI tests, fuzzing and review (Medium).
* **Panic, error and overflow handling** — panic documentation and strategy,
  ``catch_unwind`` usage, ``unwrap`` policy, overflow checks, ``Result`` /
  ``Option`` over magic values and ``#[must_use]`` return values. Largely High
  via Clippy (``missing_panics_doc``) and compiler/profile settings (release
  ``overflow-checks``), complemented by review.
* **Lint and language hygiene** — import, style and edition rules (no wildcard
  imports, no raw identifiers, no nightly, no deprecated, ``cfg!``, ``as``
  casts, shadowing), formatting and the curated Clippy/``rustc`` profiles, and
  strong typing. This cluster has the strongest automation and is almost
  entirely High through Clippy and ``rustc``.
* **Concurrency and async** — async/await decision, timing/concurrency design,
  cancellation safety, explicit task dropping and ``Pin`` / ``Send`` planning.
  Predominantly Medium and process-driven (``loom``, WCET analysis,
  architecture decision records and review).
* **Memory and resource management** — dynamic-memory design, stack checking,
  RAII and ``usize`` usage. Medium, driven by design rules and dedicated
  tooling (allocator/system checks, ``cargo-call-stack``).
* **Dependencies, features and supply chain** — dependency and duplicate
  management, additive features, download/build separation, contract/ABI
  versioning and protection of sensitive data. Mostly High via ``cargo-audit``
  / ``cargo-deny`` / ``cargo-vet``, SBOM, CI feature checks and symbol/ABI
  diffing, with CodeQL adding security-focused checks.
* **Process, documentation and qualification** — compiler qualification, MSRV,
  review environment, macro/testing strategy, trait/design guidelines, test
  coverage on generics, symbol visibility and lifetimes. Medium, argued through
  review, architecture decision records, rustdoc and tests.
* **Classification:** about half of the topics are *Required* and about half
  are *Advisory* / *Document*. The *Required* items concentrate on ``unsafe``
  usage, FFI boundaries, panic and overflow behavior, and dependency
  management.

In summary, enforceable coding-style and correctness topics are well covered by
automated tooling (primarily Clippy and ``rustc``), while safety-argument,
design and process topics rely on documented review and supporting tools.


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

The recommended ``[lints.rust]``, ``[lints.clippy]``, and ``[profile.release]``
settings are maintained centrally in the
`score_rust_policies repository <https://github.com/eclipse-score/score_rust_policies>`_:

* `Practical baseline (relaxed) <https://github.com/eclipse-score/score_rust_policies/blob/main/clippy/relaxed/Cargo.toml>`_ —
  suitable for general SCORE components.
* `Strict / ASIL variant <https://github.com/eclipse-score/score_rust_policies/blob/main/clippy/strict/Cargo.toml>`_ —
  for safety-critical code requiring stricter enforcement.


Tooling Evidence and References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``rustc`` and Clippy lints, the Clippy configuration and the release
profile selected in ``score_rust_policies`` all correspond to documented,
upstream features. The following authoritative, openly available sources back
those choices and can be used as evidence for the safety and security argument
(the CodeQL sources are already linked in the *Rust Tooling: CodeQL* section
above):

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
