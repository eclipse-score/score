<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->
(DR-002-Arch)=
# DR-002-Arch: Library Delivery Model (Static vs. Dynamic)

* **Date:** 2026-05-15

```{dec_rec} Library Delivery Model for Platform Modules
:id: dec_rec__arch__library_delivery_model
:status: accepted
:context: Architecture
:decision: Opt-in per module — static by default, dynamic where justified
```

---

## Context / Problem

The S-CORE platform delivers features and modules as compiled libraries that are integrated into downstream products. A fundamental architectural question is whether these libraries should be delivered as static libraries, dynamic/shared libraries, or a combination thereof.

This decision affects code size, runtime performance, memory usage, updateability, safety certification, security posture, and build system complexity. The choice also directly impacts how modules are built and packaged using the Bazel build system.

### Middleware Deployment Context

S-CORE is a middleware platform. In a typical deployment, S-CORE serves as the shared foundation layer upon which **multiple customer applications** run on the same target hardware (ECU / high-performance compute unit). This has critical implications for the library delivery model:

- **Multiple consumers per target:** A single ECU may host 5–20+ application binaries that all depend on S-CORE modules (e.g., communication, diagnostics, logging, execution management). The exact number is a downstream deployment decision outside S-CORE's control, but the linking model determines whether each application carries its own copy of S-CORE code or shares a single instance.
- **Independent lifecycles:** The middleware and the applications above it typically follow different release cadences. A security patch in S-CORE's communication stack should ideally not require rebuilding and re-deploying all customer applications.
- **OTA update cost:** In automotive deployments, OTA update bandwidth is constrained and update windows are limited. The ability to update the middleware layer independently of applications — or vice versa — directly affects update size, duration, and rollback complexity.
- **Variant management:** Different vehicle lines or ECU configurations may use different subsets of S-CORE modules. The linking model affects how efficiently variants can be managed and updated.

The update granularity question is therefore not merely a convenience concern but a **deployment architecture decision** that affects field serviceability, security response time, and total cost of ownership for OEMs.

## Considerations

Detailed considerations covering all relevant aspects of this decision are documented in a separate page:

```{toctree}
:maxdepth: 1

DR-002-arch/considerations
DR-002-arch/detailed_assessments
```

The considerations cover:
- Internal composition of shared libraries and API encapsulation
- Cross-language interoperability (C++ ↔ Rust)
- Debugging considerations
- Operating system support (Linux and QNX)
- License and FOSS compliance
- ABI stability and versioning
- Testing strategy
- Build reproducibility and deployment hermeticity
- Library initialization order
- Thread safety and lazy binding
- Multi-repository architecture

---

## Options Considered


### Option 1: Static Libraries Only

All platform modules and features are delivered exclusively as static libraries (`.a` / `.rlib`). Consumers link all dependencies at build time into a single binary.

#### Advantages

- **Performance:** No dynamic linking overhead at startup or runtime. Full link-time optimization (LTO) across the entire binary.
- **Determinism:** The resulting binary is fully self-contained. No runtime dependency resolution, no version conflicts.
- **Safety:** The binary under certification is exactly the binary that was tested and verified. No risk of library substitution at runtime.
- **Security:** Reduced attack surface — no `LD_PRELOAD` injection, no symbol interposition, no writable GOT/PLT entries.
- **Bazel integration:** Static linking is the natural default in Bazel's `cc_library` / `rust_library` rules.

#### Disadvantages

- **Code size:** Each binary includes its own copy of all library code. With 10+ applications sharing S-CORE, this means 10+ copies of each module in flash.
- **Memory consumption:** Each process loads its own copy of all statically linked library code into RAM. The `.text` segments cannot be shared across processes by the OS kernel.
- **Startup performance in multi-app deployments:** Total flash I/O for loading middleware code scales linearly with the number of applications.
- **Update granularity:** Any change in any S-CORE module requires re-linking and re-deploying **every application binary** that uses it. Security patches cannot be deployed to the middleware independently.
- **Re-certification:** A change in one module may require re-testing the entire linked binary.

---

### Option 2: Dynamic/Shared Libraries Only

All platform modules and features are delivered exclusively as shared libraries (`.so` / `.dylib`). Consumers link against them at runtime via the dynamic linker.

#### Advantages

- **Code size:** Shared libraries are stored once on flash regardless of how many binaries use them.
- **Memory consumption:** The OS kernel maps shared library `.text` segments into physical RAM exactly once and shares them across all processes.
- **Update granularity:** A bug fix or security patch can be deployed as a single `.so` replacement without touching any application binary. Applications and middleware can follow independent release cadences.
- **Decoupled build and deployment:** Modules can be built, versioned, and deployed independently of their consumers.

#### Disadvantages

- **Performance:** Dynamic linking introduces per-call overhead (PLT/GOT indirection). LTO cannot optimize across library boundaries.
- **Determinism:** Runtime behavior depends on which `.so` versions are present on the target.
- **Safety:** Runtime substitution of libraries must be prevented or explicitly controlled. Complicates traceability.
- **Security:** Expanded attack surface — `LD_PRELOAD` injection, symbol interposition, writable GOT/PLT (unless full RELRO).
- **Bazel integration:** Requires explicit `cc_shared_library` targets. Shared library versioning must be managed manually.

---

### Option 3: Both Static and Dynamic Libraries Simultaneously

Every module is always built and delivered in both static and dynamic form. Consumers choose per integration context.

#### Advantages

- **Flexibility:** Downstream projects can choose the linking model that fits their deployment scenario.
- **Broad compatibility:** Supports diverse integration targets without constraining the platform delivery.

#### Disadvantages

- **Build complexity:** Every module must be built twice. CI/CD pipelines, testing, and release processes double in scope.
- **Safety / Certification:** Both delivery forms must be tested and qualified separately.
- **Bazel integration:** Requires maintaining parallel build targets for each module.
- **Maintenance cost:** Any API change must be verified for both static and dynamic ABI compatibility.

---

### Option 4: Opt-In Per Module

The default delivery model is static libraries. Individual modules may opt in to additionally provide a shared library variant if there is a justified need (e.g., large shared libraries used by many consumers, or modules requiring independent updateability).

#### Advantages

- **Pragmatic default:** Static linking provides the best safety, security, and performance properties by default.
- **Targeted flexibility:** Modules with genuine dynamic linking requirements can provide a shared variant without forcing the overhead on all modules.
- **Memory efficiency where it matters:** Large modules used by many applications can opt into dynamic delivery to enable RAM sharing across processes.
- **Controlled complexity:** Build system complexity only increases for modules that explicitly opt in.
- **Update granularity:** Modules most critical for independent updateability can opt into dynamic delivery, enabling targeted partial OTA updates.
- **Safety:** The default safety argument remains simple. Modules opting into dynamic delivery explicitly take responsibility for the additional safety argumentation.
- **Security:** The default case has the smallest attack surface. Security-critical modules that require rapid patching can opt into dynamic delivery.

#### Disadvantages

- **Inconsistency:** Not all modules are delivered in the same way.
- **Governance overhead:** Requires a decision process for when a module qualifies for dynamic delivery.
- **Partial duplication:** Opted-in modules still face the dual-build and dual-test cost, albeit only for a subset.

---

## Evaluation Criteria

| Criterion                      | Static Only | Dynamic Only | Both | Opt-In per Module |
|--------------------------------|:-----------:|:------------:|:----:|:-----------------:|
| Runtime performance            |     ++      |      -       | +/-  |         +         |
| Code size on flash (multi-app) |     --      |      ++      | +/-  |         +         |
| RAM consumption (multi-app)    |     --      |      ++      | +/-  |         +         |
| Middleware update independence |     --      |      ++      |  ++  |        +/-        |
| OTA update size                |     --      |      ++      |  ++  |         +         |
| Security patch response time   |     --      |      ++      |  ++  |         +         |
| Safety argumentation           |     ++      |      -       |  -   |         +         |
| Security posture (hardening)   |     ++      |      -       | +/-  |         +         |
| Build system simplicity        |     ++      |      +       |  --  |        +/-        |
| Downstream flexibility         |      -      |      -       |  ++  |         +         |
| Integrator usability           |      +      |      +       |  ++  |         +         |
| Maintenance effort             |     ++      |      +       |  --  |         +         |

For detailed update granularity and performance assessments, see [Detailed Assessments](DR-002-arch/detailed_assessments.md).

## Decision Proposal

**Option 4: Opt-In Per Module** — Static libraries as the default delivery model, with individual modules opting in to additionally provide shared library variants where justified.

### Rationale

The analysis of all relevant criteria consistently points to Option 4 as the best balance for S-CORE's middleware role:

1. **Static by default** provides the strongest guarantees for safety (tested binary = deployed binary), security (no dynamic attack surface), and build simplicity (Bazel's natural model). For modules that are stable, rarely patched, and used by few consumers, static linking is optimal.

2. **Dynamic opt-in** addresses the real-world needs of a middleware platform serving multiple applications on the same hardware:
   - **Update granularity:** Security patches and bug fixes can be deployed without rebuilding all consumer applications.
   - **Memory efficiency:** Large modules shared by many applications benefit from kernel-level page sharing.
   - **Cross-language delivery:** Modules consumed across language boundaries benefit from shared library encapsulation.
   - **License compliance:** Modules with LGPL transitive dependencies can satisfy license requirements through shared library delivery.

3. **Mode A (build from source)** should be the standard for shared libraries in the integration repo, preserving compile-time safety. **Mode B (pre-built `.so`)** should be used only where true release independence is required, accompanied by strict ABI versioning and CI-integrated compatibility checks.

### Criteria for Opting In to Dynamic Delivery

The opt-in decision involves two distinct perspectives:

#### Platform Perspective (S-CORE decides)

A module should opt in to **additionally provide** a shared library variant if **at least one** of the following applies:

- The module is **large in code size** (e.g., communication stacks, serialization frameworks, crypto libraries) and is architecturally expected to be shared across applications.
- The module requires **independent updateability** (e.g., frequent security patches, regulatory-driven updates, rapid CVE response).
- The module is consumed **cross-language** (Rust ↔ C++) and benefits from runtime encapsulation of its language runtime.
- The module has **LGPL-licensed transitive dependencies**.
- The module implements a **plugin or extension interface** that requires runtime loading.

The decision to opt in must be documented in the module's architecture documentation and approved as part of the module's design review.

#### Integrator Perspective (OEM/customer decides)

For opted-in modules that provide both variants, the **integrator decides which variant to use** based on their specific deployment:

| Integrator scenario | Recommended variant |
|---------------------|:-------------------:|
| Single application on ECU | Static — no sharing benefit, simpler safety case |
| 2–5 applications sharing the module | Dynamic may be beneficial — evaluate RAM/flash savings vs. ABI management cost |
| 5–20+ applications sharing the module | Dynamic strongly recommended — significant memory/flash/update benefits |
| Hard real-time single-purpose controller | Static — maximum determinism, no dynamic linking overhead |
| High-performance compute with OTA requirements | Dynamic — update granularity and memory sharing outweigh the overhead |

### Special Case: Infrastructure Libraries (baselibs)

The S-CORE [baselibs](https://github.com/eclipse-score/baselibs) module provides foundational utilities consumed by **virtually every other S-CORE module**. Given its nature, baselibs should follow a **differentiated strategy:**

| baselibs component type | Delivery model | Rationale |
|------------------------|:--------------:|-----------|
| **Template / header-only** (containers, result, language extensions, safecpp) | **Static only** | Cannot be shared via `.so` — templates are instantiated in the consumer. |
| **Compiled utilities with stable C ABI** (OS abstraction, filesystem, shared memory) | **Opt-in for `.so`** | Well-defined function-call APIs that can be stabilized. |
| **Serialization (flatbuffers, JSON)** | **Case-by-case** | If the API is C-ABI-friendly, it can be shared. If it exposes C++ templates, it must remain static. |

**Key insight:** For a utility library like baselibs, the decision is not "the whole module is static or dynamic" but rather **which sub-components can technically and practically be delivered as shared libraries.**

### Mandatory Requirements for Opted-In Modules

- Expose a **C ABI surface** with `-fvisibility=hidden` and explicit exports.
- Maintain **Soname versioning** aligned with semantic versioning.
- Use **`-Wl,-z,now` (eager binding)** as mandatory linker flag.
- Provide **explicit initialization functions** (`score_<module>_init()`) rather than relying on `__attribute__((constructor))`.
- Include **ABI compliance checks** (`abidiff` or equivalent) in the module's CI pipeline.
- Enforce a **toolchain identity CI gate**: verify that all shared libraries and their consumers are built with the same compiler and compiler version.
- Use **`RPATH`** (not `RUNPATH`) for library search paths. Set via `-Wl,--disable-new-dtags`.
- Apply **security hardening flags** for all shared library builds:
  - Full RELRO: `-Wl,-z,relro,-z,now`
  - Stack protection: `-fstack-protector-strong`
  - Position-Independent Code: `-fPIC`
  - Fortify source: `-D_FORTIFY_SOURCE=2`
  - No executable stack: `-Wl,-z,noexecstack`
  - Restrict library search paths to platform-controlled directories only
- Statically link all **internal dependencies** into the `.so` — do not expose internal sub-libraries as separate shared objects.
- Generate a **deployment manifest** with `.so` versions, checksums, and build-IDs as part of the release.

## Consequences

### Positive

- The default case (static) remains simple for safety argumentation, build system, debugging, and multi-repo integration.
- Modules that benefit from dynamic delivery can opt in without forcing complexity on the rest of the platform.
- OEMs gain targeted update granularity for the most critical middleware components while maintaining deterministic behavior for the rest.
- Cross-language module delivery is cleanly supported where needed.
- LGPL compliance is addressed structurally rather than through workarounds.

### Negative / Costs

- Opted-in modules carry additional overhead: dual build targets, ABI management, Soname versioning, ABI compliance CI checks, toolchain identity verification, CI/CD toolchain workflow for ABI diff check, and deployment manifest generation.
- Downstream integrators must understand which modules offer which variants and choose accordingly.
- A governance process for opt-in decisions must be established and maintained.
- Debug symbol archives must be maintained per `.so` version for opted-in modules.

### Follow-Up Actions

- Define the initial set of modules that should opt in (candidates: communication stack, logging, diagnostics, crypto/security).
- Establish Bazel toolchain defaults for shared libraries (`-Wl,-z,now`, `-fvisibility=hidden`).
- Integrate `abidiff` or equivalent into the CI pipeline for opted-in module repos.
- Define the deployment manifest format and tooling.
- Document the opt-in process in the S-CORE contribution guidelines.
