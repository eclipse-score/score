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

Writing Rust Code
#################

.. document:: Coding Guidelines Rust
   :id: doc__rust_coding_guidelines
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan


Coding Guidelines
=================

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

`Safety-Critical Rust Consortium <https://rustfoundation.org/safety-critical-rust-consortium>`_

`Safety-Critical Rust Consortium Guidelines <https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines/>`_

`Learn unsafe Rust <https://google.github.io/learn_unsafe_rust/>`_

`Rust language <https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html>`_


State of Rust Safety-Critical Tooling
#####################################

The linked document provides a current overview of the tooling landscape for
certifying Rust in safety-critical applications, presenting a
community-approved list of essential tools and tracking their development
status. It also explores whether developing specialized training curricula for
safety-critical Rust is necessary, potentially requiring a separate
subcommittee. The document details the state of specific tools—such as
compilers and analysis utilities—by outlining their intended purposes,
certification requirements, and their availability or progress. While some
tools, such as the Ferrocene compiler, are already available or being actively
developed, others remain under evaluation or are not yet accessible.

`Mission Statement - Tooling Subcommittee <https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/tooling/mission-statement.md>`_


Explanation of ARA Applications in Rust
#######################################

AUTOSAR also shares a public available document that explains how to use Rust in
ARA applications as Rust is offering safety and performance advantages. While
ecosystem support is still maturing, Rust-based ARA applications can lead to
safer, more reliable automotive software, especially in safety-critical and
high-performance domains.

`AUTOSAR ARA Applications in Rust <https://www.autosar.org/fileadmin/standards/R24-11/AP/AUTOSAR_AP_EXP_ARARustApplications.pdf>`_


MISRA vs Cert
#############

This issue contrasts the MISRA and CERT coding standards, highlighting their
different approaches to software safety and security. MISRA is noted for its
restrictive language subsetting and complex compliance process, often imposing
outdated or ineffective rules that do not guarantee improved safety or
security. This can create unnecessary work for developers without clear
benefits and is sometimes inconsistent across languages. CERT, on the other
hand, is praised for its focus on practical, consensus-based rules that target
real security vulnerabilities in existing code, avoiding excessive constraints.
The overall recommendation is to favor guidelines like CERT’s—practical,
evidence-based, and focused on real-world issues—over rigid, untested standards
that hinder adoption and developer productivity.

`MISRA vs Cert <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/75/>`_


Link to Clippy
##############

Rust Clippy is a collection of lints (code style and correctness checks) for
the Rust programming language. It helps developers identify common mistakes,
improve code quality, and follow best practices by providing warnings and
suggestions as part of the Rust toolchain. Clippy can be run on Rust projects
to catch issues that the standard compiler might miss, making it an essential
tool for writing clean, idiomatic, and efficient Rust code.

`Link to Clippy <https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/78/>`_


Link to Miri
############

Miri is an Undefined Behavior detection tool for Rust. It can run binaries
and test suites of cargo projects and detect unsafe code that fails to
uphold its safety requirements.

`Link to Miri <https://github.com/rust-lang/miri>`_

Conclusions for S-CORE
######################

During the S-CORE project formatting and clippy checks are enforced. Miri can
be used to detect undefined behaviors. Also the code should compile with zero warnings.
Additional guidelines by the Rust Community, the Rust Foundation and the Safety-Critical
Rust Consortium are applied where applicable but not enforced. If possible the usage
of `unsafe` is avoided. To keep the code `panic`-free only APIs with a proper return value
should be used.

The adaption of these guidelines will be documented in the S-CORE project
documentation.
