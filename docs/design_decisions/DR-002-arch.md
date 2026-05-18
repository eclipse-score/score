<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-002-Arch: Library Delivery Model (Static vs. Dynamic)

* **Date:** 2026-05-15

```{dec_rec} Library Delivery Model for Platform Modules
:id: dec_rec__arch__library_delivery_model
:status: proposed
:context: Architecture
:decision: Proposal: Opt-in per module — static by default, dynamic where justified
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

### Architectural Note: Internal Composition of Shared Libraries

When a module (feature) is delivered as a shared library, this does **not** imply that every internal component of that module is itself a separate `.so`. The standard and recommended pattern is:

- The module (feature) exposes a **single shared library** (or a reasonable number of shared libraries) with a well-defined public API (exported symbols).
- Internally, the module is composed of multiple static libraries (internal components, helpers, data structures) that are **statically linked into the shared library** at build time.
- Only the explicitly exported API surface is visible to consumers; all internal symbols remain hidden (`-fvisibility=hidden` / `#[doc(hidden)]`).

This pattern has several important consequences:

| Aspect | Implication |
|--------|-------------|
| **ABI surface** | Minimized — only the public API constitutes the ABI contract. Internal refactoring does not break consumers. |
| **LTO within the library** | The compiler can apply full link-time optimization across all internal static libraries within the shared library boundary. Cross-module inlining and dead code elimination work as expected inside the `.so`. |
| **Security** | Hidden internal symbols cannot be interposed or called externally. The attack surface is limited to exported functions. |
| **Safety** | The certification boundary is the shared library as a unit. Internal decomposition is an implementation detail that does not affect the external safety interface. |
| **Bazel build graph** | Internal components are regular `cc_library` / `rust_library` targets. The final `cc_shared_library` target aggregates them. Visibility rules ensure internal targets are not directly depended upon by external consumers. |

```
# Example Bazel structure for a module delivered as shared library
cc_library(
    name = "internal_serialization",
    visibility = ["//visibility:private"],
    ...
)

cc_library(
    name = "internal_transport",
    visibility = ["//visibility:private"],
    deps = [":internal_serialization"],
    ...
)

cc_shared_library(
    name = "score_comm",
    deps = [":internal_transport"],
    exports_filter = ["//comm:public_api"],
    ...
)
```

#### API Encapsulation: Shared Library vs. Merged Static Library

A shared library with `-fvisibility=hidden` and explicit exports provides **hard API encapsulation**: internal symbols are physically absent from the dynamic symbol table. Applications cannot accidentally (or intentionally) call internal functions — the linker will reject such references.

Could the same encapsulation be achieved by merging smaller static libraries into a single larger static archive (`.a`) before delivery? **No — a static library offers no symbol hiding:**

| Delivery form | Internal symbols visible to consumers? | Accidental use preventable? |
|---------------|:--------------------------------------:|:---------------------------:|
| Shared library (`-fvisibility=hidden`) | No — not in dynamic symbol table | Yes — linker rejects unknown symbols |
| Merged static archive (`.a`) | **Yes** — all `.o` symbols remain linkable | **No** — linker can resolve any symbol from the archive |
| Partial link (`ld -r`) + symbol localization | Partially — requires manual version scripts or `objcopy --localize` | Complex workaround, fragile to maintain |

A static archive is simply a collection of object files. Merging multiple `.a` into one still exposes every symbol from every `.o` to the consuming linker. There is no standard mechanism in the archive format to mark symbols as "internal". Workarounds exist (partial linking with `ld -r` followed by `objcopy --localize-hidden` or linker version scripts), but these are fragile, non-portable, and not natively supported by Bazel.

**Conclusion:** The shared library model provides a natural and robust API boundary that physically prevents accidental use of internal interfaces. This is an additional architectural advantage of delivering modules as shared libraries beyond the commonly cited memory/update benefits.

This composition model applies to all options below that involve shared libraries (Options 2, 3, and 4). The term "shared library" in this document always refers to such a composed unit with a controlled export surface, not to individually shared internal components.

### Cross-Language Interoperability (C++ ↔ Rust)

S-CORE uses both C++ and Rust (see [DR-001-Arch](DR-001-arch.md)). Modules written in one language may need to be consumed by applications or other modules written in the other. The library delivery model affects cross-language interoperability (FFI):

#### The Common Denominator: C ABI

Neither C++ nor Rust has a stable, cross-language ABI of its own. Cross-language calls require an intermediate **C ABI** (`extern "C"` in both languages). This applies equally to static and dynamic linking:

| Aspect | Static library | Shared library |
|--------|:--------------:|:--------------:|
| C ABI functions callable cross-language? | Yes | Yes |
| Native C++ classes/templates usable from Rust? | No (no stable C++ ABI) | No (same limitation) |
| Native Rust types usable from C++? | No (no stable Rust ABI) | No (same limitation) |
| Requires wrapper/binding layer? | Yes | Yes |

#### How the Linking Model Affects FFI in Practice

| Concern | Static Linking | Dynamic Linking |
|---------|:--------------:|:---------------:|
| **Symbol resolution** | Resolved at build time — link errors caught early | Resolved at load time — missing symbols may cause runtime failures |
| **ABI stability requirement** | None — caller and callee are compiled together | C ABI must remain stable across independent builds/releases |
| **Tooling (bindgen, cxx, cbindgen)** | Generated bindings compiled directly into the binary | Same bindings, but ABI compatibility must be maintained across versions |
| **Language runtime coupling** | Both runtimes (C++ stdlib, Rust libstd) linked into one binary — potential conflicts (e.g., dual allocators, duplicate panic handlers) | Each `.so` can encapsulate its own runtime internally; only C ABI is exposed across the boundary |
| **Versioning** | No versioning concern — single build | ABI version of the C interface must be tracked; breaking changes require soname bumps |

#### Practical Approaches for S-CORE

1. **`extern "C"` wrappers:** Each module exposes a C-ABI header regardless of implementation language. This works identically for static and dynamic linking.

2. **Binding generators (cxx, bindgen, cbindgen):**
   - `cxx` generates safe Rust↔C++ bridges with compile-time checks. Works best with static linking (caller and callee built together).
   - `bindgen`/`cbindgen` generate raw C FFI bindings. Work with both static and dynamic, but dynamic requires ABI discipline.

3. **Shared library as language isolation boundary:** A shared library is particularly well-suited for cross-language delivery because:
   - The `.so` fully encapsulates the implementation language and its runtime.
   - Consumers see only the C ABI surface — they need not know (or link against) the implementation language's standard library.
   - A Rust `.so` can be consumed by a C++ application without the C++ build system needing any Rust toolchain.
   - A C++ `.so` can be consumed by a Rust application without pulling in libstdc++/libc++ into the Rust binary's static link.

4. **Static library cross-language challenges:**
   - A Rust `.rlib` cannot be directly linked into a C++ binary — it requires the Rust runtime (libstd, allocator, panic infrastructure).
   - A C++ `.a` can be linked into a Rust binary via `cc` crate / `build.rs`, but the C++ standard library must be explicitly linked.
   - When both languages coexist in one binary, care must be taken to avoid conflicting allocators, exception/panic mechanisms, and thread-local storage.

#### Bazel Integration for Cross-Language FFI

```
# Rust module exposing C ABI for C++ consumers
rust_shared_library(
    name = "score_crypto_ffi",
    crate_name = "score_crypto_ffi",
    srcs = ["src/ffi.rs"],
    deps = [":score_crypto_internal"],
)

# C++ application consuming the Rust shared library
cc_binary(
    name = "app",
    srcs = ["main.cpp"],
    deps = [":score_crypto_ffi"],  # links against the .so
)
```

**Conclusion for this decision:** Shared libraries provide a cleaner cross-language boundary because they fully encapsulate the implementation language's runtime and expose only a C ABI contract. Static linking requires the consumer's build system to understand and manage the foreign language's runtime dependencies, increasing coupling and build complexity. This is an additional argument favoring dynamic delivery for modules that are consumed cross-language.

### Debugging Considerations

The library delivery model has practical implications for debugging during development and for post-mortem analysis of field issues.

#### Comparison

| Aspect | Static Libraries | Shared Libraries |
|--------|:----------------:|:----------------:|
| **Symbol availability in debugger** | All symbols in one binary — single symbol table, all addresses known at load | Debugger must discover `.so` files at runtime; symbols loaded per library as each `.so` is mapped |
| **Breakpoints** | Straightforward — all code addresses fixed at link time | Works, but lazy-bound PLT entries may require `set breakpoint pending on` or break on the resolved target |
| **Source-level stepping** | Seamless if debug info (`-g`) is included | Seamless if debug info is available per `.so` — identical experience once symbols are loaded |
| **Core dump analysis** | Self-contained — the single binary plus the core file is sufficient to reconstruct the full state | Requires the **exact matching `.so` versions** alongside the core file. If `.so` files have been updated since the crash, stack traces may be incorrect |
| **Stripped production binaries** | External debug info (`.debug` file) must match the deployed binary | External debug info must match **per `.so`** — requires tracking debug symbols for each library version independently |
| **Hot code reload during development** | Not possible — must relink and restart the entire binary | Possible in principle (`dlclose` / `dlopen`) — useful for rapid iteration on a single module without full restart |
| **Address Space Layout Randomization (ASLR)** | Single base address randomized; relative offsets stable | Each `.so` is independently randomized — debugger handles this transparently, but manual address calculations are more complex |
| **Debug build size** | One large binary with all debug info embedded | Smaller per-library debug files; total may be similar but more manageable for partial debugging |

#### Practical Impact for S-CORE

1. **Development debugging:** Both models provide equivalent source-level debugging experience with modern toolchains (GDB, LLDB). No practical disadvantage for either approach during active development.

2. **Field issue analysis (core dumps):** This is where the models diverge significantly:
   - **Static:** A core dump + the binary = full debuggability. Simple to collect, simple to analyze. No dependency on matching library versions.
   - **Dynamic:** A core dump requires the exact set of `.so` files (at the correct versions) that were loaded at crash time. In a middleware deployment with independent update cadences, this means:
     - The OEM must archive every deployed `.so` version with its corresponding debug symbols.
     - Core dump analysis tooling must resolve the correct `.so` set based on build-ID or version metadata embedded in the core.
     - If a middleware update was applied between the crash and the analysis, the wrong `.so` versions may be used, producing misleading stack traces.

3. **Bazel integration for debug symbols:**
   - Static: Bazel produces a single binary; `--strip=never` or `--fission` controls debug info.
   - Dynamic: Each `cc_shared_library` produces a separate `.so` + optional `.debug` file. Debug symbol archives must be maintained per target per version.

4. **Safety implications of debugging:** For certified components, the ability to reproduce and analyze failures deterministically is a safety requirement. Static linking simplifies this because the deployed binary is fully self-contained. Dynamic linking requires a robust configuration management process to ensure that the exact library combination of a field deployment can be reconstructed for analysis.

**Conclusion:** Static linking has a clear advantage for **post-mortem debugging and field issue analysis** due to its self-contained nature. Dynamic linking adds operational complexity for maintaining debug symbol archives and matching `.so` versions to core dumps. For development-time debugging, both models are equivalent. This is an additional argument for the opt-in model (Option 4): frequently updated modules benefit from dynamic delivery, but the debugging complexity is limited to those opted-in modules rather than the entire stack.

### Operating System Support (Linux and QNX)

S-CORE targets both Linux and QNX as deployment platforms. Both operating systems support static and dynamic linking, but with differences in maturity, tooling, and behavior that are relevant to this decision.

#### Feature Comparison

| Capability | Linux (glibc / musl) | QNX (Neutrino RTOS) |
|-----------|:--------------------:|:--------------------:|
| Static linking | Fully supported | Fully supported |
| Shared libraries (`.so`) | Fully supported (ELF, `ld-linux.so`) | Fully supported (ELF, `ldqnx.so`) |
| `dlopen` / `dlclose` (runtime loading) | Fully supported | Supported |
| Page sharing of `.text` across processes | Yes (kernel maps shared `.so` pages) | Yes (procnto shares mapped pages) |
| Position-Independent Code (PIC) required for `.so` | Yes | Yes |
| `LD_PRELOAD` / library interposition | Yes — potential security concern | Limited — QNX restricts in secure configurations |
| Full RELRO hardening | Supported (`-Wl,-z,relro,-z,now`) | Supported |
| Symbol versioning (ELF version scripts) | Fully supported | Supported (limited ecosystem tooling) |
| `DT_RUNPATH` / `DT_RPATH` | Fully supported | Supported |
| Core dump with `.so` build-IDs | Yes (well-supported by GDB, coredumpctl) | Supported (QNX crash dump system) |

#### Linux-Specific Considerations

- **Mature ecosystem:** Dynamic linking is the dominant model on Linux. The toolchain (GCC, LLVM, ld, ldd, ldconfig) is highly optimized for shared libraries. Package managers, distribution models, and most middleware on Linux assume dynamic linking.
- **musl libc and static linking:** For fully static binaries on Linux, `musl` (as alternative to glibc) provides clean static linking without hidden dynamic dependencies. Bazel supports musl-based static toolchains. This can simplify deployment on embedded Linux targets.
- **glibc and `dlopen` within static binaries:** glibc uses `dlopen` internally (e.g., for NSS, iconv). Fully static binaries with glibc may behave unexpectedly. This is a known limitation — not a concern for QNX.
- **ASLR:** Both PIE (static) and PIC (shared) binaries support full ASLR on Linux. No security difference between the models regarding address randomization.

#### QNX-Specific Considerations

- **Microkernel + process model:** QNX's microkernel architecture results in many small processes (resource managers, drivers). Shared libraries are particularly beneficial here because many processes share common infrastructure code (libc, libsocket, etc.). S-CORE middleware modules fit naturally into this pattern.
- **Startup behavior:** QNX's `ldqnx.so` dynamic linker is leaner than Linux's, with lower symbol resolution overhead. Startup cost of dynamic linking is generally lower on QNX than on comparable Linux deployments.
- **Filesystem considerations:** QNX targets often use read-only filesystems (IFS / image filesystem). Shared libraries in the image are XIP-capable (execute-in-place) on some flash configurations — reducing RAM usage further.
- **Safety-certified configuration:** For ASIL-qualified QNX deployments, the OS vendor (BlackBerry QNX) provides guidance on certified library configurations. Static linking simplifies the certified configuration (fewer deployment artifacts), but QNX's safety documentation also covers dynamically linked configurations.
- **Toolchain:** QNX SDP provides both static and shared library support via its GCC/LLVM toolchain. Bazel cross-compilation for QNX requires a custom toolchain definition; both `cc_library` and `cc_shared_library` work with the QNX toolchain.
- **Secure execution policies:** QNX supports `procnto` security policies that restrict library loading to specific paths, mitigating `LD_PRELOAD`-style attacks. This partially addresses the security concerns of dynamic linking.

#### Cross-Platform Implications for S-CORE

| Decision factor | Linux | QNX | Impact on linking choice |
|----------------|:-----:|:---:|:------------------------:|
| Dynamic linking ecosystem maturity | Excellent | Good | Both platforms fully support shared libraries |
| Static linking cleanness | Good (musl) / Problematic (glibc) | Clean | Static is simpler on QNX than on glibc-Linux |
| Security hardening for `.so` | RELRO + ASLR + seccomp | RELRO + ASLR + procnto policies | Both can harden shared libraries adequately |
| Page sharing benefit | High (many userspace processes) | Very high (microkernel = many small processes) | Shared libraries more beneficial on QNX |
| Safety certification documentation | N/A (Linux not safety-certified) | Available from QNX vendor | Static simplifies, but dynamic is certifiable |
| XIP (execute-in-place) support | Limited | Available on some flash configurations | Additional memory advantage for `.so` on QNX |

**Conclusion:** Both Linux and QNX fully support static and dynamic linking. Neither OS forces a specific model. However:
- On **QNX**, the microkernel architecture with many small processes makes shared libraries particularly attractive for memory efficiency, and the OS vendor provides safety-certified configurations for both models.
- On **Linux**, dynamic linking is the ecosystem default with excellent tooling, while clean fully-static linking requires a musl-based toolchain (glibc is problematic for fully static binaries).
- The decision between static and dynamic linking is **not constrained by OS capabilities** on either platform. Both options are viable, and the choice should be driven by the architectural criteria discussed in this document (update granularity, safety, security, performance) rather than OS limitations.

### License and FOSS Compliance

The linking model has direct implications for open-source license compliance, particularly for copyleft licenses:

| License type | Static linking | Dynamic linking |
|-------------|:--------------:|:---------------:|
| **Apache-2.0, MIT, BSD** (permissive) | No restriction | No restriction |
| **LGPL-2.1 / LGPL-3.0** | Problematic — the resulting binary may be considered a "combined work" requiring release of the entire binary's source or providing re-linking capability | Compliant — the application uses the library "as a shared library", satisfying LGPL requirements |
| **GPL** (without linking exception) | Copyleft applies to entire binary | Copyleft applies to entire binary (linking model irrelevant for GPL) |

**Relevance for S-CORE:**
- S-CORE itself is Apache-2.0 licensed — no restriction on either model for S-CORE's own code.
- However, S-CORE depends on **third-party libraries** that may be LGPL-licensed (e.g., system libraries, codec libraries, protocol implementations). If such a dependency is statically linked into S-CORE's delivery artifacts, downstream consumers inherit the LGPL obligation — they must be able to re-link against a modified version of the LGPL library.
- The **safest compliance strategy** for LGPL dependencies is to deliver them as shared libraries (or to deliver S-CORE modules that use LGPL code as shared libraries), ensuring clear separation between the LGPL component and the proprietary application code.
- For the opt-in model (Option 4), any module with LGPL transitive dependencies should be a strong candidate for dynamic delivery.

### ABI Stability and Versioning

Shared libraries introduce an explicit **ABI contract** between the library provider (S-CORE) and its consumers (applications). This contract must be managed:

| Concern | Static (no ABI contract) | Dynamic (ABI contract required) |
|---------|:------------------------:|:-------------------------------:|
| Breaking API change | Consumer recompiles — detected at build time | Consumer may crash at runtime if `.so` is updated without recompile |
| ABI versioning | Not applicable | Soname versioning required (e.g., `libscore_comm.so.1` → `.so.2`) |
| Backward compatibility | Not required | Must be maintained within a major version |
| Support lifetime | Per release | Per ABI version — may span multiple releases |

**Key questions for S-CORE:**
1. **How long is an ABI version supported?** If S-CORE guarantees ABI stability for 2 years, consumers can update middleware `.so` files without rebuilding. If ABI stability is not guaranteed, the benefit of independent updateability is reduced.
2. **How are breaking changes communicated?** Soname bumps signal ABI breaks. Consumers linking against `libscore_comm.so.1` will not accidentally load `libscore_comm.so.2` — the dynamic linker rejects the mismatch.
3. **Tooling:** ABI compliance checking tools (`abidiff`, `abi-compliance-checker`) can be integrated into CI to detect unintentional ABI breaks before release. Bazel can be configured to run these checks as part of the build.
4. **Semantic versioning:** S-CORE should align Soname major versions with semantic versioning major versions. Minor/patch updates preserve ABI.

**For static-only delivery**, this entire concern disappears — the consumer always builds against the exact source/headers they received. But the tradeoff is the loss of independent updateability.

### Testing Strategy

The linking model affects what constitutes a "tested configuration" and who is responsible for testing which combinations:

| Aspect | Static | Dynamic |
|--------|:------:|:-------:|
| **Unit/module test artifact** | Static library tested in isolation (test binary links statically) | Same — module tests are independent of delivery form |
| **Integration test artifact** | The final linked binary = test subject | The `.so` + a test harness binary = test subject |
| **Deployment configuration tested** | Binary is self-contained — no deployment variability | Specific combination of `.so` versions must be tested together |
| **Combinatorial explosion** | Each consumer binary is one test configuration | Each combination of consumer × `.so` versions is a configuration |
| **Who tests?** | Consumer is responsible for their binary | Middleware provider tests the `.so` in reference configurations; consumer tests their specific integration |

**Implications for S-CORE:**
- **Static:** S-CORE delivers tested library code, but each consumer must test their final linked binary. S-CORE cannot guarantee system behavior because the final binary is consumer-specific.
- **Dynamic:** S-CORE can deliver a **tested `.so` set** that represents a validated middleware configuration. Consumers test only the integration of their application with the validated `.so` set. This can reduce redundant testing effort across multiple consumer teams — if S-CORE certifies `libscore_comm.so v2.3.1`, all consumers benefit from that certification without re-testing the communication stack.
- **Safety testing:** For ISO 26262, the "software unit" under test must correspond to the deployed artifact. With shared libraries, the `.so` itself can be the qualified unit — reusable across multiple consumer products without re-qualification (assuming no configuration changes).

### Build Reproducibility and Deployment Hermeticity

Bazel provides hermetic, reproducible builds. However, build-time hermeticity does not automatically ensure deployment-time hermeticity:

| Concern | Static | Dynamic |
|---------|:------:|:-------:|
| **Build reproducibility** | Bazel guarantees identical binary for identical inputs | Bazel guarantees identical `.so` for identical inputs |
| **Deployment reproducibility** | Binary = deployment artifact. Fully determined at build time. | Deployment = binary + set of `.so` files. The **combination** must be documented and reproducible. |
| **Configuration drift** | Impossible — binary is immutable | Possible — a `.so` may be updated independently, creating a combination that was never built or tested together |
| **Lock file / manifest** | Not needed | Required — a deployment manifest must record the exact versions of all `.so` files comprising a valid configuration |

**Mitigation for dynamic linking:**
- Introduce a **deployment manifest** (e.g., a JSON/TOML file) that records the exact `.so` versions, checksums, and build-IDs for a validated configuration.
- Bazel can generate this manifest as a build output alongside the `.so` artifacts.
- Runtime verification: On system startup, a component can validate that all loaded `.so` files match the expected manifest (build-ID comparison). This provides determinism guarantees approaching those of static linking.

### Library Initialization Order

Shared libraries may contain initialization code (`__attribute__((constructor))` in C/C++, `#[ctor]` in Rust) that runs when the library is loaded. The execution order of these constructors is **not fully deterministic:**

| Behavior | Static | Dynamic |
|----------|:------:|:-------:|
| Initialization order | Determined by link order — well-defined within one binary | Determined by dependency graph + load order — may vary across runs or platform versions |
| Circular dependencies | Detected at link time (error) | May cause undefined initialization order or `dlopen` failures |
| Global state in constructors | Executes once in binary startup — predictable | May execute at different times relative to other libraries |

**Risks:**
- If S-CORE module A's constructor depends on module B being initialized first, the dynamic linker must respect this dependency order. ELF `DT_NEEDED` entries establish this, but complex graphs may lead to surprising behavior.
- Constructor-heavy designs are fragile with dynamic linking. Best practice: minimize constructor logic, use explicit initialization functions called by the application.

**Recommendation for S-CORE:**
- Avoid reliance on `__attribute__((constructor))` for critical initialization.
- Provide explicit `score_<module>_init()` functions that applications call in a defined order.
- Document initialization dependencies between modules.

### Thread Safety and Lazy Binding

The default ELF dynamic linker behavior uses **lazy binding**: symbols are resolved on first call rather than at load time. This interacts with multi-threading:

| Scenario | Behavior |
|----------|----------|
| Single-threaded first call | Lazy resolution triggers linker code → safe |
| Multi-threaded first call to same symbol | Multiple threads may trigger resolution simultaneously → implementation-dependent |
| `LD_BIND_NOW` / `-Wl,-z,now` (eager binding) | All symbols resolved at load time before any application thread runs → fully deterministic |

**Linux:** glibc's dynamic linker is thread-safe for lazy binding (uses internal locks). The concern is largely historical but adds latency jitter — the first call to a symbol has unpredictable latency.

**QNX:** `ldqnx.so` is thread-safe for lazy binding. Same jitter concern applies.

**Impact on real-time systems:**
- Lazy binding introduces **latency non-determinism** — the first call to each function through the PLT may take microseconds longer than subsequent calls. For hard real-time applications (e.g., safety-critical control loops), this jitter is unacceptable.
- **Mitigation:** Use `LD_BIND_NOW` (or `-Wl,-z,now` at link time) to force eager binding. All symbols are resolved at startup, eliminating runtime jitter. Tradeoff: slightly increased startup time.
- For S-CORE, `LD_BIND_NOW` should be the **mandatory default** for any dynamically linked deployment in automotive/safety-critical contexts. This eliminates the thread-safety and latency-jitter concern entirely.

**Bazel integration:** The linker flag `-Wl,-z,now` can be added to the shared library's `linkopts` or to the consumer's link options to enforce eager binding. Bazel toolchain configuration can make this the default for all targets.

### Multi-Repository Architecture

S-CORE follows a multi-repository approach: each module (or group of related modules) lives in its own Git repository and is developed independently. These modules are integrated into the **reference integration repository** (`score_platform`) which composes them into a coherent platform. This architecture has significant implications for the linking model.

#### Repository Structure

```
score_platform (reference integration repo)
├── MODULE.bazel          # bzlmod: declares dependencies on module repos
├── module_comm/          # or: fetched via bazel_dep()
├── module_diag/
├── module_logging/
└── ...

score_comm (separate repo)     ← independent development, own CI
score_diag (separate repo)     ← independent development, own CI
score_logging (separate repo)  ← independent development, own CI
```

Bazel's module system (`bzlmod`) resolves inter-repository dependencies at build time. Each module declares its dependencies in its own `MODULE.bazel`, and the integration repo pins the compatible versions.

#### Impact on Static Linking

| Concern | Assessment |
|---------|-----------|
| **Cross-repo dependency resolution** | Bazel handles this transparently — `bazel_dep()` fetches the source, and all code is compiled together in one build graph. Static linking works across repo boundaries as if the code were in a single repo. |
| **Diamond dependencies** | Bazel resolves to exactly one version of each dependency (MVS — Minimum Version Selection). No duplication in the final binary. |
| **Build reproducibility** | Fully hermetic — the `MODULE.bazel.lock` pins all transitive versions. The same build graph produces the same binary regardless of when it is built. |
| **Module independence** | Limited — a module's CI can build and test its own static library, but cannot produce a deployable artifact without the consumer. The module repo delivers source or `.a` files; the integration repo produces the final binary. |

**Consequence:** Static linking is **well-suited** for a multi-repo approach with Bazel. The integration repo builds everything from source (or from cached artifacts), and Bazel's dependency resolution eliminates version conflicts at build time.

#### Integration Challenges Apply to Both Models

It is important to note that **independent module development without integration testing causes problems regardless of the linking model.** If modules are developed in separate repos and only integrated late, incompatibilities will arise in both cases:

| Type of incompatibility | Static linking | Dynamic linking (built from source) | Dynamic linking (pre-built `.so`) |
|--------------------------|:--------------:|:-----------------------------------:|:---------------------------------:|
| API change (function signature, header) | **Compile error** in integration repo — caught immediately | **Compile error** in integration repo — same as static | **Runtime crash** — `.so` was built against old headers |
| Semantic change (same API, different behavior) | Silent — not caught by compiler | Silent — not caught by compiler | Silent — not caught by compiler |
| Dependency version mismatch | Bazel resolves at build time — one version | Bazel resolves at build time — same as static | May produce conflicting versions at deploy time |
| ABI change (struct layout, enum values) | Recompiled together — no ABI concept | Recompiled together — no ABI concept | **Silent data corruption** — binary layout mismatch not detectable by linker |

**Key insight:** The difference is **not** that dynamic linking creates more integration problems. The problems (API drift, semantic changes, version mismatches) are identical. The difference is **when incompatibilities are detected:**

1. **Static linking** and **dynamic linking built from source** both detect API/signature breaks at **compile time** in the integration repo. Bazel's build graph forces recompilation of all dependents when a dependency changes.
2. **Pre-built `.so` artifacts** shift some error detection from **compile time to runtime** — specifically, ABI-level breaks that the compiler would catch if it saw the updated headers are invisible when linking against a pre-built binary.
3. **Semantic incompatibilities** (same API, changed behavior) are undetectable by either model and require integration tests regardless.

**Therefore:** The real risk factor is not "static vs. dynamic" but **"build from source vs. consume pre-built artifacts."** If the integration repo always builds all shared libraries from source, the compile-time safety guarantees are identical to static linking.

The **additional risk unique to dynamic linking** arises only **after deployment:** the ability to update a single `.so` in the field without rebuilding its consumers introduces a runtime compatibility dimension that does not exist with statically linked binaries. This is simultaneously the greatest advantage (independent updateability) and the greatest risk (unvalidated combinations) of dynamic linking.

#### Impact on Dynamic Linking

Given the above distinction, the dynamic linking assessment differentiates between two consumption modes:

**Mode A — Integration repo builds `.so` from source (via Bazel):**

| Concern | Assessment |
|---------|-----------|
| **Compile-time safety** | Identical to static linking — Bazel recompiles all targets when a dependency changes. |
| **Diamond dependencies** | Resolved by Bazel at build time — same as static. |
| **Independent release cadences** | Not achieved — all modules are still built together. The `.so` boundary exists at runtime but not at build time. |
| **Benefit over static** | Runtime benefits (page sharing, update granularity) are preserved. Build-time safety is not sacrificed. |

**Mode B — Module repos publish pre-built `.so` artifacts:**

| Concern | Assessment |
|---------|-----------|
| **Compile-time safety** | Reduced — the integration repo links against pre-built `.so` files. ABI compatibility is not verified by the compiler. |
| **ABI compatibility across repos** | Must be guaranteed by convention and tooling (`abidiff`, ABI compliance checks in CI). |
| **Diamond dependencies** | Real risk — modules built independently against different versions of a shared dependency may be incompatible. |
| **Independent release cadences** | Achieved — modules can publish `.so` artifacts on their own schedule. |
| **Benefit over static** | Full independence, but requires disciplined ABI management. |

**Recommendation:** For S-CORE, **Mode A** (build from source in the integration repo) should be the default. This preserves compile-time safety while gaining the runtime benefits of shared libraries. **Mode B** (pre-built `.so`) should only be used for modules where true release independence is required, and only with strict ABI versioning, Soname management, and CI-integrated ABI compliance checking.

#### Diamond Dependency Problem — Detailed Example

This problem is specific to **Mode B** (pre-built `.so` artifacts) and does not apply when building from source:

```
Application
├── links: score_comm.so (pre-built in score_comm repo)
│   └── was built against: score_serialization v2.0 headers
└── links: score_diag.so (pre-built in score_diag repo)
    └── was built against: score_serialization v2.1 headers

Deployed: score_serialization.so v2.1
→ score_comm.so may be incompatible if ABI changed between v2.0 and v2.1
```

- **Static linking (integration repo builds all from source):** Bazel resolves `score_serialization` to one version (e.g., 2.1) and compiles everything together. Incompatibilities are caught at compile time.
- **Dynamic linking from source (Mode A):** Same as static — Bazel resolves one version and builds all `.so` files in one graph. No diamond problem.
- **Dynamic linking pre-built (Mode B):** `score_comm.so` was built against v2.0 headers. If the deployed `score_serialization.so` is v2.1 and the ABI changed, `score_comm.so` may crash or silently corrupt data at runtime. The linker cannot detect this.
- Mitigation (for Mode B only): The integration repo must define a **compatible version set** and either:
  - Rebuild all `.so` files from source in one build (losing the independent release advantage), or
  - Enforce strict ABI compatibility rules and Soname versioning across repos, or
  - Use the opt-in model (Option 4): only modules at the "API boundary" are shared libraries; internal transitive dependencies are statically linked into each `.so`, eliminating the diamond problem for internal code.

#### Multi-Repo and the Opt-In Model (Option 4)

The opt-in model interacts favorably with the multi-repository approach:

| Pattern | How it works |
|---------|-------------|
| **Module repo delivers static library** (default) | The module publishes a Bazel module (`bazel_dep`) that exposes `cc_library` targets. The integration repo links everything statically. Simple, no ABI concerns across repos. |
| **Module repo delivers shared library** (opt-in) | The module additionally publishes a pre-built `.so` with a stable C ABI and Soname versioning. The module's CI tests the `.so` independently. The integration repo can consume either the source (for static) or the `.so` (for dynamic). |
| **Internal dependencies within a `.so`** | When a module opts into `.so` delivery, its transitive in-repo dependencies are statically linked into the `.so`. Only the public API is exposed. This eliminates cross-repo diamond dependency problems for internal code. |
| **Shared infrastructure libraries** | Widely-used infrastructure (e.g., serialization, logging) can be delivered as `.so` with strict ABI guarantees. These require the most rigorous versioning and compatibility testing across repos. |

#### Bazel Integration for Multi-Repo

```
# In the integration repo's MODULE.bazel:
bazel_dep(name = "score_comm", version = "2.4.0")
bazel_dep(name = "score_diag", version = "1.7.0")
bazel_dep(name = "score_logging", version = "1.5.0")

# Static integration (default): all built from source
cc_binary(
    name = "app",
    deps = [
        "@score_comm//:comm",       # cc_library → static
        "@score_diag//:diag",       # cc_library → static
        "@score_logging//:logging", # cc_library → static
    ],
)

# Dynamic integration (opt-in modules):
# score_comm publishes a cc_shared_library target
cc_binary(
    name = "app_dynamic",
    deps = [
        "@score_comm//:comm_so",    # cc_shared_library → .so
        "@score_diag//:diag",       # cc_library → static
        "@score_logging//:logging_so", # cc_shared_library → .so
    ],
)
```

**Conclusion:** The multi-repository architecture is compatible with both linking models. The integration challenges of independent module development (API drift, semantic changes) are **identical** for both models and require integration testing regardless. The key differences are:
- **Static linking** and **dynamic linking built from source** (Mode A) provide the same compile-time safety guarantees. Multi-repo is transparent thanks to Bazel's dependency resolution.
- **Pre-built `.so` artifacts** (Mode B) introduce cross-repo ABI coordination as a new concern. This is the price for true independent release cadences.
- The **additional risk unique to dynamic linking** exists only at deployment time: the possibility of updating a `.so` independently creates combinations that were never built or tested together. This risk does not exist with static linking.
- The **opt-in model (Option 4)** is the best fit for multi-repo: static by default (simple cross-repo integration), with `.so` delivery (preferably Mode A, Mode B only where justified) for modules where independent updateability is worth the additional ABI management overhead. Internal dependencies are statically linked into the `.so`, isolating the ABI surface to the module's public API.

---

## Options Considered


### Option 1: Static Libraries Only

All platform modules and features are delivered exclusively as static libraries (`.a` / `.rlib`). Consumers link all dependencies at build time into a single binary.

#### Advantages

- **Performance:** No dynamic linking overhead at startup or runtime. Function calls are direct, enabling full link-time optimization (LTO) across the entire binary. For a **single application in isolation**, this is the fastest option with optimal per-call performance (no PLT/GOT indirection). Note: In multi-application deployments, this advantage is partially offset by increased startup I/O (see Disadvantages).
- **Determinism:** The resulting binary is fully self-contained. No runtime dependency resolution, no version conflicts, no missing `.so` files at deployment.
- **Safety:** The binary under certification is exactly the binary that was tested and verified. No risk of library substitution at runtime. Simplifies the safety case and traceability from source to deployed artifact.
- **Security:** Reduced attack surface — no `LD_PRELOAD` injection, no symbol interposition, no writable GOT/PLT entries. The binary can be fully hardened with RELRO and stripped of dynamic linking infrastructure.
- **Bazel integration:** Static linking is the natural default in Bazel's `cc_library` / `rust_library` rules. No need for `linkshared` attributes or `cc_shared_library` targets. Dependency resolution is fully handled at analysis time.

#### Disadvantages

- **Code size:** Each binary includes its own copy of all library code. If multiple binaries on the same target share modules, total flash/storage consumption increases significantly. In a middleware scenario with 10+ applications sharing S-CORE, this means 10+ copies of each module in flash.
- **Memory consumption:** Each process loads its own copy of all statically linked library code into RAM. The `.text` segments cannot be shared across processes by the OS kernel. In a deployment with N applications using S-CORE, the middleware code occupies N × (library size) in physical RAM rather than 1 × (library size). On memory-constrained ECUs, this can be a critical limitation.
- **Startup performance in multi-app deployments:** While per-call performance is optimal, the system-wide startup cost increases in middleware scenarios with many applications:
  - Each of the N applications must independently load its own copy of the middleware code from flash — there is no sharing of already-resident pages across processes.
  - N applications each trigger cold page faults for the same library code (at different virtual addresses within their respective binaries).
  - Total flash I/O for loading middleware code scales linearly with the number of applications (N × library size read from flash), whereas with shared libraries the code is read once and reused from page cache.
  - The cumulative system startup time (all applications) can exceed the dynamic linking alternative, where only the first application pays the full I/O cost.
- **Update granularity:** Any change in any S-CORE module requires re-linking and re-deploying **every application binary** that uses it. A single bug fix in the middleware forces a full rebuild and OTA update of all dependent applications. In a typical deployment with many consumer applications, this means:
  - OTA update packages grow to include all application binaries, not just the changed middleware component.
  - Update duration and bandwidth consumption scale with the number of applications, not with the size of the change.
  - Rollback becomes an all-or-nothing operation across the entire software stack.
  - Security patches cannot be deployed to the middleware independently — the OEM must coordinate a synchronized release of all applications.
  - Time-to-field for critical fixes is extended by the rebuild and re-test cycle of all consumer applications.
- **Re-certification:** A change in one module may require re-testing the entire linked binary, depending on the safety argumentation strategy (impact analysis vs. full re-test). With multiple applications, this effort multiplies per binary.

---

### Option 2: Dynamic/Shared Libraries Only

All platform modules and features are delivered exclusively as shared libraries (`.so` / `.dylib`). Consumers link against them at runtime via the dynamic linker.

#### Advantages

- **Code size:** Shared libraries are stored once on flash regardless of how many binaries use them. Reduced flash/storage footprint in the middleware scenario — a single copy of each S-CORE `.so` serves all applications on the ECU.
- **Memory consumption:** The OS kernel maps shared library `.text` segments into physical RAM exactly once and shares them across all processes via virtual memory. If 10 applications use `libscore_comm.so`, the code pages exist only once in physical RAM. This can reduce total RAM usage by an order of magnitude for the middleware portion. Additionally, shared pages that are already loaded for one application incur zero additional page-fault cost when another application starts.
- **Update granularity:** This is the strongest advantage of dynamic linking in a middleware context:
  - A bug fix or security patch in an S-CORE module can be deployed as a single `.so` replacement without touching any application binary.
  - OTA update size is proportional to the actual change, not to the number of consumers.
  - Applications and middleware can follow independent release cadences — the OEM can update customer applications without waiting for a new S-CORE release, and vice versa.
  - Rollback granularity improves: a faulty middleware update can be reverted independently of application state.
  - Security response time is minimized: a CVE in a shared module can be patched once, deployed once, and immediately effective for all applications.
- **Decoupled build and deployment:** Modules can be built, versioned, and deployed independently of their consumers. This is particularly valuable when S-CORE is delivered by a different organization than the applications consuming it.

#### Performance: First Load vs. Subsequent Use

The runtime performance of a shared library differs significantly depending on whether it is loaded for the first time or is already resident in memory:

| Aspect | First application (cold) | Subsequent applications (warm) |
|--------|--------------------------|-------------------------------|
| File mapping | `.so` must be read from flash/disk and mapped into page cache | Kernel reuses existing page cache — no flash I/O |
| Page faults | `.text` pages are demand-paged on first access (cold page faults) | Pages already in physical RAM — zero page faults for code |
| Symbol resolution | Dynamic linker resolves all symbols, fills GOT/PLT (per-process) | Still required per-process — same cost |
| Library constructors | Run once in first process | Run again in each subsequent process |
| Steady-state call overhead | PLT/GOT indirection per call (same for all) | Identical — no improvement after initial resolution |

**Summary:** The first application to load a shared library pays a startup penalty (flash I/O + page faults + relocation). All subsequent applications benefit from the fact that the library's code pages are already in the kernel page cache and physical RAM. In a middleware deployment where S-CORE libraries are loaded by many applications, the cold-start cost is paid only once (typically by the first application to start), and all later consumers start faster. However, the per-call PLT/GOT indirection remains constant regardless of how many consumers exist — it is inherent to the dynamic linking mechanism and does not amortize with use.

This warm-cache behavior further strengthens the case for dynamic linking in multi-application middleware scenarios: the performance penalty is highest for a single consumer and decreases (in relative terms) as the number of consumers sharing the library grows.

#### Disadvantages

- **Performance:** Dynamic linking introduces a per-call overhead (PLT/GOT indirection) that is constant regardless of the number of consumers. Additionally, the first load of a library incurs flash I/O and page fault costs (see above). LTO cannot optimize across library boundaries, potentially leaving cross-module call patterns and inlining opportunities unexploited.
- **Determinism:** Runtime behavior depends on which `.so` versions are present on the target. ABI compatibility must be maintained or explicitly managed. Risk of version mismatches.
- **Safety:** The certified binary configuration includes the combination of consumer + all shared libraries at specific versions. Runtime substitution of libraries must be prevented or explicitly controlled. Symbol resolution is a runtime-variable process, complicating traceability. Safety standards (ISO 26262) require demonstrating that the tested configuration matches the deployed configuration — dynamic linking adds complexity to this argument.
- **Security:** Expanded attack surface — `LD_PRELOAD` injection, symbol interposition, writable GOT/PLT (unless full RELRO), potential for loading malicious `.so` files if library paths are not locked down.
- **Bazel integration:** Requires explicit `cc_shared_library` targets or `linkshared = True`. Shared library versioning (sonames) must be managed manually. Bazel's default dependency model assumes static linking; shared library boundaries must be explicitly designed and maintained.

---

### Option 3: Both Static and Dynamic Libraries Simultaneously

Every module is always built and delivered in both static and dynamic form. Consumers choose per integration context.

#### Advantages

- **Flexibility:** Downstream projects can choose the linking model that fits their deployment scenario (e.g., static for deeply embedded ECUs, dynamic for high-performance compute platforms).
- **Broad compatibility:** Supports diverse integration targets without constraining the platform delivery.
- **Memory / code size optimization:** Customers on memory-constrained hardware with many applications can use the dynamic variant to share code pages in RAM. Customers with single-binary deployments can use the static variant to avoid dynamic linking overhead.
- **Update granularity:** Customers deploying S-CORE as shared middleware for many applications can use the dynamic variant and benefit from independent updateability. Customers with single-binary deployments can use the static variant for maximum performance.

#### Disadvantages

- **Build complexity:** Every module must be built twice. CI/CD pipelines, testing, and release processes double in scope for library artifacts.
- **Safety / Certification:** Both delivery forms must be tested and qualified separately. The safety case must cover both linking scenarios, increasing documentation and verification effort.
- **Security:** Both forms must be independently hardened and analyzed.
- **Bazel integration:** Requires maintaining parallel build targets (`cc_library` + `cc_shared_library`) for each module. Increases BUILD file complexity and the risk of configuration drift between the two variants.
- **Maintenance cost:** Any API change must be verified for both static and dynamic ABI compatibility.

---

### Option 4: Opt-In Per Module

The default delivery model is static libraries. Individual modules may opt in to additionally provide a shared library variant if there is a justified need (e.g., large shared libraries used by many consumers, or modules requiring independent updateability).

#### Advantages

- **Pragmatic default:** Static linking provides the best safety, security, and performance properties by default.
- **Targeted flexibility:** Modules with genuine dynamic linking requirements (e.g., plugin architectures, large shared codebases, independently updatable components) can provide a shared variant without forcing the overhead on all modules.
- **Memory efficiency where it matters:** Large modules used by many applications (e.g., communication stack, serialization framework) can opt into dynamic delivery to enable RAM sharing across processes. Smaller utility modules remain static with negligible memory impact.
- **Controlled complexity:** Build system complexity only increases for modules that explicitly opt in. The default case remains simple.
- **Update granularity:** Modules that are most critical for independent updateability in the middleware scenario (e.g., communication stacks, security-relevant components, frequently patched modules) can opt into dynamic delivery. This enables targeted partial OTA updates for the components that benefit most, while keeping the simpler static model for stable, rarely-changed modules. The middleware can define a "shared core" set of modules delivered as `.so` for update efficiency, while less critical or rarely-changing modules remain static.
- **Safety:** The default safety argument remains simple (static binary = tested binary). Modules opting into dynamic delivery explicitly take responsibility for the additional safety argumentation (ABI stability, version control, deployment configuration management).
- **Security:** The default case has the smallest attack surface. Dynamic variants are individually assessed. Security-critical modules that require rapid patching can opt into dynamic delivery to minimize time-to-field.
- **Bazel integration:** The default `cc_library` / `rust_library` pattern works without modification. Modules opting in add a `cc_shared_library` target alongside their static target. Bazel's visibility and dependency mechanisms can enforce that only approved modules provide shared libraries.

#### Disadvantages

- **Inconsistency:** Not all modules are delivered in the same way. Downstream integrators must understand which modules offer which variants.
- **Governance overhead:** Requires a decision process for when a module qualifies for dynamic delivery. Criteria must be defined and maintained.
- **Partial duplication:** Opted-in modules still face the dual-build and dual-test cost from Option 3, albeit only for a subset.

---

## Evaluation Criteria

| Criterion | Static Only | Dynamic Only | Both | Opt-In per Module |
|-----------|:-----------:|:------------:|:----:|:-----------------:|
| Runtime performance | ++ | - | +/- | + |
| Code size on flash (multi-app) | -- | ++ | +/- | + |
| RAM consumption (multi-app) | -- | ++ | +/- | + |
| Middleware update independence | -- | ++ | ++ | + |
| OTA update size | -- | ++ | ++ | + |
| Security patch response time | -- | ++ | ++ | + |
| Safety argumentation | ++ | - | - | + |
| Security posture (hardening) | ++ | - | +/- | + |
| Build system simplicity | ++ | + | -- | + |
| Downstream flexibility | - | - | ++ | + |
| Maintenance effort | ++ | + | -- | + |

### Update Granularity — Detailed Assessment

Given S-CORE's role as middleware shared by multiple applications, update granularity is a decisive evaluation criterion:

| Scenario | Static Only | Dynamic Only | Opt-In per Module |
|----------|:-----------:|:------------:|:-----------------:|
| Security patch in comm module | Rebuild + redeploy all apps | Replace one `.so` | Replace one `.so` (if opted in) |
| Bug fix in logging module | Rebuild + redeploy all apps | Replace one `.so` | Static rebuild (if not opted in) |
| New middleware release | Rebuild + redeploy all apps | Replace middleware `.so` set | Replace opted-in `.so`s + rebuild static consumers |
| Application-only update | Rebuild app binary | Replace app binary only | Replace app binary only |
| Rollback middleware change | Rollback all app binaries | Rollback middleware `.so`s | Partial rollback possible |
| Typical OTA size (middleware patch) | ~All app binaries (tens of MB) | ~Changed `.so` only (KB–MB) | ~Changed opted-in `.so` (KB–MB) |

For deployments where S-CORE serves as the shared foundation for many applications, the **inability to update the middleware independently** (static-only model) represents a significant operational constraint that increases OTA costs, extends security patch timelines, and complicates release coordination between middleware provider and application teams.

### Performance Differences — Indicative Values and Hardware Dependencies

Precise performance numbers cannot be stated universally because they depend heavily on target hardware characteristics (CPU microarchitecture, cache hierarchy, flash/storage type, MMU capabilities). However, published research and industry experience provide **order-of-magnitude orientation:**

#### Per-Call Overhead (PLT/GOT Indirection)

| Hardware class | Overhead per cross-library call | Notes |
|----------------|:-------------------------------:|-------|
| ARM Cortex-A (with branch predictor) | ~1–5 ns | Branch prediction mitigates most of the indirect jump cost. GOT entry is typically in L1 cache for hot paths. |
| ARM Cortex-R (no/simple branch predictor) | ~5–20 ns | Indirect jumps are more expensive without speculative execution. Relevant for safety-critical real-time controllers. |
| x86-64 (modern) | ~1–3 ns | Highly optimized branch prediction. Negligible for most workloads. |

**Context:** For a middleware API that is called at kHz rates (e.g., logging, diagnostics polling), this overhead is immeasurable. For APIs called at MHz rates in tight loops (e.g., serialization of high-frequency sensor data), the cumulative cost can reach low single-digit percent — typically dominated by the inability to inline across the library boundary rather than the PLT jump itself.

#### Link-Time Optimization (LTO) Benefit Lost

LTO across the entire binary (static case) vs. LTO only within each `.so` (dynamic case) can yield:

- **Typical improvement from full-binary LTO:** 5–20% for compute-bound code (published GCC/LLVM benchmarks).
- **For I/O-bound or event-driven middleware code:** Often <5%, as performance is dominated by system calls, IPC, and data copying rather than instruction efficiency.
- **S-CORE relevance:** Most middleware APIs are I/O-bound or event-driven (communication, diagnostics, logging). The LTO benefit of static linking is likely in the **low single-digit percent range** for typical middleware call patterns. Compute-intensive modules (e.g., cryptographic operations, data serialization) may see larger benefits.

#### Startup Time (Symbol Resolution)

| Factor | Typical impact |
|--------|:--------------:|
| Per-symbol resolution (ELF hash lookup) | ~0.5–2 µs per symbol (ARM Cortex-A) |
| Library with ~500 exported symbols | ~0.5–1 ms relocation time |
| Library with ~5000 exported symbols | ~5–10 ms relocation time |
| `LD_BIND_NOW` (full eager binding) | Paid once at startup, zero cost afterwards |
| Lazy binding (default) | Startup faster, first call to each symbol slower |

**Context:** For a middleware with a well-designed API surface (hundreds, not thousands of exported symbols per `.so`), the startup overhead of dynamic linking is typically in the **low millisecond range per library** — negligible for most automotive boot sequences.

#### System-Wide Startup (Multi-App, Flash I/O)

This is the most hardware-dependent factor:

| Storage type | Sequential read speed | Impact of N×static vs. 1×shared |
|-------------|:---------------------:|:---:|
| eMMC (typical automotive) | 100–300 MB/s | Significant: 10 apps × 5 MB middleware = 50 MB vs. 5 MB |
| NOR flash (direct-execute) | 50–100 MB/s | Most significant: I/O is the bottleneck |
| NVMe / UFS 3.x | 1–3 GB/s | Less significant: I/O cost is amortized by high bandwidth |

#### Summary

| Performance aspect | Magnitude of impact | Hardware-dependent? | Measurable in S-CORE context? |
|-------------------|:-------------------:|:-------------------:|:-----------------------------:|
| PLT/GOT per-call overhead | Low (ns) | Moderate | Yes, via micro-benchmarks |
| LTO benefit lost | Low–moderate (%) | Low | Yes, via A/B benchmarks |
| Startup symbol resolution | Low (ms) | Moderate | Yes, via profiling |
| Multi-app flash I/O savings | Moderate–high (ms–s) | **High** | Requires target hardware |

**Recommendation:** The performance difference between static and dynamic linking is **not the dominant decision criterion** for a middleware platform. In most deployment scenarios, the per-call overhead is negligible for middleware APIs, and the startup difference depends on hardware that varies across targets. Code size, RAM sharing, update granularity, safety, and security should weigh more heavily in this decision. Projects with hard real-time requirements on specific hot paths can address those through targeted design (e.g., header-only interfaces, inlined critical paths) regardless of the general linking strategy.

## Decision Proposal

**Option 4: Opt-In Per Module** — Static libraries as the default delivery model, with individual modules opting in to additionally provide shared library variants where justified.

### Rationale

The analysis of all relevant criteria — performance, code size, RAM consumption, update granularity, safety, security, licensing, debugging, cross-language interoperability, OS support, multi-repository integration, ABI management, and build system complexity — consistently points to Option 4 as the best balance for S-CORE's middleware role:

1. **Static by default** provides the strongest guarantees for safety (tested binary = deployed binary), security (no dynamic attack surface), and build simplicity (Bazel's natural model). For modules that are stable, rarely patched, and used by few consumers, static linking is optimal.

2. **Dynamic opt-in** addresses the real-world needs of a middleware platform serving multiple applications on the same hardware:
   - **Update granularity:** Security patches and bug fixes in frequently-updated modules can be deployed without rebuilding all consumer applications.
   - **Memory efficiency:** Large modules shared by many applications benefit from kernel-level page sharing (RAM) and single-copy storage (flash).
   - **Cross-language delivery:** Modules consumed across language boundaries (C++ ↔ Rust) benefit from the clean encapsulation of a shared library.
   - **License compliance:** Modules with LGPL transitive dependencies can satisfy license requirements through shared library delivery.

3. **Mode A (build from source)** should be the standard for shared libraries in the integration repo, preserving compile-time safety. **Mode B (pre-built `.so`)** should be used only where true release independence is required, accompanied by strict ABI versioning and CI-integrated compatibility checks.

### Criteria for Opting In to Dynamic Delivery

The opt-in decision involves two distinct perspectives:

#### Platform Perspective (S-CORE decides)

As a platform provider, S-CORE does **not** know how many applications will consume a given module in any specific downstream deployment. The number of consumers (5, 10, 20+) is a deployment decision made by the OEM/integrator. Therefore, S-CORE's opt-in criteria must be based on properties **intrinsic to the module**, not on assumed deployment topology:

A module should opt in to **additionally provide** a shared library variant if **at least one** of the following applies:

- The module is **large in code size** (e.g., communication stacks, serialization frameworks, crypto libraries) and is architecturally expected to be shared across applications — making RAM/flash duplication costly in typical middleware deployments.
- The module requires **independent updateability** (e.g., frequent security patches, regulatory-driven updates, rapid CVE response).
- The module is consumed **cross-language** (Rust ↔ C++) and benefits from runtime encapsulation of its language runtime.
- The module has **LGPL-licensed transitive dependencies**.
- The module implements a **plugin or extension interface** that requires runtime loading.

The decision to opt in must be documented in the module's architecture documentation and approved as part of the module's design review.

#### Integrator Perspective (OEM/customer decides)

The downstream integrator knows their actual deployment topology — how many applications run on the target, which modules they consume, and what their update and certification strategy is. For opted-in modules that provide both variants, the **integrator decides which variant to use** based on their specific deployment:

| Integrator scenario | Recommended variant |
|---------------------|:-------------------:|
| Single application on ECU | Static — no sharing benefit, simpler safety case |
| 2–5 applications sharing the module | Dynamic may be beneficial — evaluate RAM/flash savings vs. ABI management cost |
| 5–20+ applications sharing the module | Dynamic strongly recommended — significant memory/flash/update benefits |
| Hard real-time single-purpose controller | Static — maximum determinism, no dynamic linking overhead |
| High-performance compute with OTA requirements | Dynamic — update granularity and memory sharing outweigh the overhead |

S-CORE provides both variants for opted-in modules. The integrator's deployment configuration (which variant to link) is outside S-CORE's scope but should be documented in S-CORE's integration guide with guidance for typical scenarios.

### Special Case: Infrastructure Libraries (baselibs)

The S-CORE [baselibs](https://github.com/eclipse-score/baselibs) module deserves special consideration. It provides foundational utilities (concurrency, containers, filesystem, serialization, OS abstraction, memory handling, error handling, etc.) that are consumed by **virtually every other S-CORE module** as well as by downstream applications. This creates a unique situation:

```
Application A ─┬─→ score_comm ──────→ baselibs (containers, serialization, os)
               ├─→ score_logging ───→ baselibs (json, filesystem)
               └─→ score_diag ─────→ baselibs (result, utils)

Application B ─┬─→ score_comm ──────→ baselibs (containers, serialization, os)
               └─→ score_lifecycle ─→ baselibs (json)
```

#### The Decision: Should baselibs Be Delivered as a Shared Library?

This is **not** a straightforward opt-in case. The arguments differ from typical application-facing modules:

**Arguments for delivering baselibs as shared library:**

- **Maximum deduplication:** baselibs code appears in every module and every application. If all modules are static, baselibs code is duplicated N×M times (N applications × M modules). As a single `.so`, it exists once in RAM and flash.
- **Single point of update:** A bug fix in `baselibs::containers` or a security patch in `baselibs::os` would be deployed once, effective for all modules and applications immediately.

**Arguments against delivering baselibs as a shared library:**

- **Massive ABI surface:** baselibs exposes many fine-grained utilities (containers, result types, language extensions). Stabilizing the ABI across all of these is extremely difficult — much harder than for a focused API like a communication stack.
- **Template-heavy / header-only code:** Many baselibs components (containers, result types, `safecpp` language extensions) are likely template-heavy or header-only. These are compiled **into the consumer** at build time and cannot be shared via `.so` — they will be duplicated regardless of the linking model.
- **Tight coupling:** Modules use baselibs types in their own APIs (e.g., returning `score::Result<T>`, accepting `score::DynamicArray<T>`). If baselibs were a separate `.so`, its types would cross library boundaries — requiring ABI stability for every type, not just for function signatures.
- **Fragile base class / type problem:** A layout change in `score::DynamicArray` would break the ABI of **every module** that uses it in its interface. This makes the ABI contract transitively fragile.

#### Recommended Approach for baselibs

Given the above analysis, baselibs should follow a **differentiated strategy:**

| baselibs component type | Delivery model | Rationale |
|------------------------|:--------------:|-----------|
| **Template / header-only** (containers, result, language extensions, safecpp) | **Static only** | Cannot be shared via `.so` — templates are instantiated in the consumer. No benefit from dynamic linking. |
| **Compiled utilities with stable C ABI** (OS abstraction, filesystem, shared memory) | **Opt-in for `.so`** | These have well-defined function-call APIs that can be stabilized. OS-level abstractions are natural candidates for shared delivery. |
| **Serialization (flatbuffers, JSON)** | **Case-by-case** | If the API is C-ABI-friendly (opaque handles, C function calls), it can be shared. If the API exposes C++ templates or types, it must remain static. |

**Key insight:** For a utility library like baselibs, the decision is not "the whole module is static or dynamic" but rather **which sub-components can technically and practically be delivered as shared libraries.** The architectural note on internal composition (see above) applies here: even if some baselibs components are delivered as `.so`, others will necessarily remain header-only/static and be compiled into each consumer.

**Implication for other modules:** When a module like `score_comm` is delivered as a `.so`, it **statically links** the baselibs components it uses internally. The baselibs types that appear in `score_comm`'s **public API** must be part of the ABI contract. This is another reason to minimize the use of complex baselibs types (templates, containers) in public module APIs and prefer simple C-ABI-compatible types at the shared library boundary.

### Mandatory Requirements for Opted-In Modules

- Expose a **C ABI surface** with `-fvisibility=hidden` and explicit exports.
- Maintain **Soname versioning** aligned with semantic versioning.
- Use **`-Wl,-z,now` (eager binding)** as mandatory linker flag.
- Provide **explicit initialization functions** (`score_<module>_init()`) rather than relying on `__attribute__((constructor))`.
- Include **ABI compliance checks** (`abidiff` or equivalent) in the module's CI pipeline.
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

- Opted-in modules carry additional overhead: dual build targets, ABI management, Soname versioning, ABI compliance CI checks, and deployment manifest generation.
- Downstream integrators must understand which modules offer which variants and choose accordingly.
- A governance process for opt-in decisions must be established and maintained.
- Debug symbol archives must be maintained per `.so` version for opted-in modules.

### Follow-Up Actions

- Define the initial set of modules that should opt in (candidates: communication stack, logging, diagnostics, crypto/security).
- Establish Bazel toolchain defaults for shared libraries (`-Wl,-z,now`, `-fvisibility=hidden`).
- Integrate `abidiff` or equivalent into the CI pipeline for opted-in module repos.
- Define the deployment manifest format and tooling.
- Document the opt-in process in the S-CORE contribution guidelines.
