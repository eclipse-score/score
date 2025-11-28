DR-005-infra: Directory Structure for S-CORE Bazel C++ Toolchain Configuration Repository
====================================================================================

Overview
--------

This repository acts as a **pure configuration layer** for C++ toolchains used in Bazel builds.
It contains **only configuration files** (``BUILD.bazel``, ``.bzl``), while all **toolchain
binaries** are downloaded from external repositories via ``http_archive``.

Platform definitions are **not** part of this repository—they are provided separately by the
S-CORE Bazel Platforms module.

This structure supports:

- Multiple compiler versions
- Multiple OS/CPU combinations
- Clean layering following Bazel best practices
- Bzlmod-compatible module extensions
- Reusability and long-term maintainability

----

High-Level Goals
----------------

- Provide a **central place** for all C++ toolchain configuration logic.
- Separate toolchain **binaries** from **configurations**.
- Provide scalable support for:

  - Linux (x86_64, arm64)
  - QNX (x86_64, arm64)
  - Multiple compiler variants (GCC, Clang, QCC)
  - Multiple versions per compiler

- Allow all consuming repositories to pull toolchains via **Bzlmod** with simple configuration.

----

Proposed Directory Structure
----------------------------

.. code-block:: text

    <repo_root>/
    ├── MODULE.bazel
    ├── BUILD.bazel
    │
    ├── toolchains/
    │   ├── linux/
    │   │   ├── x86_64/
    │   │   │   ├── gcc/
    │   │   │   │   ├── 12.2.0/
    │   │   │   │   │   ├── BUILD.bazel
    │   │   │   │   │   ├── cc_toolchain_config.bzl
    │   │   │   │   │   └── third_party/
    │   │   │   │   │       └── gcc.BUILD
    │   │   │   │   └── ...
    │   │   │   └── llvm/
    │   │   │       ├── 16/
    │   │   │       └── ...
    │   │   │
    │   │   └── arm64/
    │   │       ├── gcc/
    │   │       │   ├── 12.2.0/
    │   │       │   └── ...
    │   │       └── llvm/
    │   │           ├── 16/
    │   │           └── ...
    │   │
    │   ├── qnx/
    │   │   ├── x86_64/
    │   │   └── arm64/
    │   │       └── qcc/
    │   │           ├── 7.1/
    │   │           ├── 8.0/
    │   │           └── ...
    │   │
    │   ├── rules/
    │   │   ├── BUILD.bazel
    │   │   ├── gcc.bzl
    │   │   ├── llvm.bzl
    │   │   └── qcc.bzl
    │   │
    │   ├── extentions/
    │   │   ├── BUILD.bazel
    │   │   ├── gcc.bzl
    │   │   ├── llvm.bzl
    │   │   └── qcc.bzl
    │   │
    │   └── common/
    │       ├── cc_config_common.bzl
    │       ├── toolchain_features.bzl
    │       └── version_matrix.bzl
    │
    ├── tests/
    │   └── ...
    │
    └── docs/
        ├── repo_overview.md
        ├── naming_convention.md
        ├── how_to_add_toolchain.md
        └── version_policy.md

----

Structure Rationale
-------------------

1. OS → Architecture → Compiler → Version Hierarchy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This structure provides:

- Clear separation of toolchains
- Easy extension when adding:

  - New compilers
  - New versions
  - New platforms

Example:

.. code-block:: text

    toolchains/linux/x86_64/gcc/13.1.0/

----

2. Clean Separation from Binaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All binaries remain outside:

- Toolchain binaries provided by vendor archives  
- Retrieved via ``http_archive``
- Only configuration logic lives here

Each versioned toolchain directory pulls paths from package repository
``toolchain_cpp_packages`` (full name: ``S-CORE Bazel CPP Toolchain packages``) such as:

::

    @score_toolchain_linux_x86_64_gcc12_2_0

or:

::

    @score_toolchain_linux_arm64_gcc13_1_0

This ensures the configuration repo remains lightweight and portable.

----

3. Shared Common Logic
~~~~~~~~~~~~~~~~~~~~~~

All shared logic lives under:

::

    toolchains/common/

Contained files:

+------------------------------+-----------------------------------------------+
| File                         | Purpose                                       |
+==============================+===============================================+
| ``cc_config_common.bzl``     | Common flags and default configurations       |
+------------------------------+-----------------------------------------------+
| ``toolchain_features.bzl``   | Helper functions for constructing features    |
+------------------------------+-----------------------------------------------+
| ``version_matrix.bzl``       | Single source of truth for supported versions |
+------------------------------+-----------------------------------------------+

This avoids duplication across the full matrix of platform/compiler/version combinations.

----

4. Bzlmod Extension
~~~~~~~~~~~~~~~~~~~

The repository exposes module extensions defined in the ``extentions`` directory.

Example:

::

    module_extension(
        name = "gcc",
        extension_file = "//toolchains/extentions:gcc.bzl",
    )

or:

::

    module_extension(
        name = "llvm",
        extension_file = "//toolchains/extentions:llvm.bzl",
    )

The extension:

- Loads toolchain definitions
- Provides interface for root module to set desired version and options
- Maps toolchains to the Bazel Platforms module

----

5. Documentation
~~~~~~~~~~~~~~~~

A dedicated ``docs/`` directory ensures maintainability:

- **repo_overview.md** — high-level purpose
- **naming_convention.md** — toolchain naming scheme
- **how_to_add_toolchain.md** — step-by-step contributor guide
- **toolchain_testing_and_validation** — integration-gate validation specification
- **version_policy.md** — rules for adding/deprecating versions

----

Benefits Summary
----------------

+-------------------+--------------------------------------------------------------+
| **Benefit**       | **Explanation**                                              |
+===================+==============================================================+
| Scalable          | Clean hierarchy allows adding platforms and compilers        |
|                   | easily.                                                      |
+-------------------+--------------------------------------------------------------+
| Modular           | Fully compatible with Bzlmod.                                |
+-------------------+--------------------------------------------------------------+
| Lightweight       | No binaries stored in the repository.                        |
+-------------------+--------------------------------------------------------------+
| Consistent        | Shared logic centralized under ``toolchains/common``.        |
+-------------------+--------------------------------------------------------------+
| Traceable         | Version matrix gives a clear overview of supported versions. |
+-------------------+--------------------------------------------------------------+

