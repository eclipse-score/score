<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-002-Arch: Considerations


This page provides detailed considerations for the :ref:`Library Delivery Model <DR-002-Arch>` design decision

## Architectural Note: Internal Composition of Shared Libraries

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

### API Encapsulation: Shared Library vs. Merged Static Library

A shared library with `-fvisibility=hidden` and explicit exports provides **hard API encapsulation**: internal symbols are physically absent from the dynamic symbol table. Applications cannot accidentally (or intentionally) call internal functions — the linker will reject such references.

Could the same encapsulation be achieved by merging smaller static libraries into a single larger static archive (`.a`) before delivery? **No — a static library offers no symbol hiding:**

| Delivery form | Internal symbols visible to consumers? | Accidental use preventable? |
|---------------|:--------------------------------------:|:---------------------------:|
| Shared library (`-fvisibility=hidden`) | No — not in dynamic symbol table | Yes — linker rejects unknown symbols |
| Merged static archive (`.a`) | **Yes** — all `.o` symbols remain linkable | **No** — linker can resolve any symbol from the archive |
| Partial link (`ld -r`) + symbol localization | Partially — requires manual version scripts or `objcopy --localize` | Complex workaround, fragile to maintain |

A static archive is simply a collection of object files. Merging multiple `.a` into one still exposes every symbol from every `.o` to the consuming linker. There is no standard mechanism in the archive format to mark symbols as "internal". Workarounds exist (partial linking with `ld -r` followed by `objcopy --localize-hidden` or linker version scripts), but these are fragile, non-portable, and not natively supported by Bazel.

**Conclusion:** The shared library model provides a natural and robust API boundary that physically prevents accidental use of internal interfaces. This is an additional architectural advantage of delivering modules as shared libraries beyond the commonly cited memory/update benefits.

This composition model applies to all options that involve shared libraries (Options 2, 3, and 4). The term "shared library" in this document always refers to such a composed unit with a controlled export surface, not to individually shared internal components.

## Cross-Language Interoperability (C++ ↔ Rust)

:ref:`Library Delivery Model <DR-002-Arch>`).
S-CORE uses both C++ and Rust (see :ref:`<DR-001-arch>`). Modules written in one language may need to be consumed by applications or other modules written in the other. The library delivery model affects cross-language interoperability (FFI):

### The Common Denominator: C ABI

Neither C++ nor Rust has a stable, cross-language ABI of its own. Cross-language calls require an intermediate **C ABI** (`extern "C"` in both languages). This applies equally to static and dynamic linking:

| Aspect | Static library | Shared library |
|--------|:--------------:|:--------------:|
| C ABI functions callable cross-language? | Yes | Yes |
| Native C++ classes/templates usable from Rust? | No (no stable C++ ABI) | No (same limitation) |
| Native Rust types usable from C++? | No (no stable Rust ABI) | No (same limitation) |
| Requires wrapper/binding layer? | Yes | Yes |

### How the Linking Model Affects FFI in Practice

| Concern | Static Linking | Dynamic Linking |
|---------|:--------------:|:---------------:|
| **Symbol resolution** | Resolved at build time — link errors caught early | Resolved at load time — missing symbols may cause runtime failures |
| **ABI stability requirement** | None — caller and callee are compiled together | C ABI must remain stable across independent builds/releases |
| **Tooling (bindgen, cxx, cbindgen)** | Generated bindings compiled directly into the binary | Same bindings, but ABI compatibility must be maintained across versions |
| **Language runtime coupling** | Both runtimes (C++ stdlib, Rust libstd) linked into one binary — potential conflicts (e.g., dual allocators, duplicate panic handlers) | Each `.so` can encapsulate its own runtime internally; only C ABI is exposed across the boundary |
| **Versioning** | No versioning concern — single build | ABI version of the C interface must be tracked; breaking changes require soname bumps |

### Practical Approaches for S-CORE

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

### Bazel Integration for Cross-Language FFI

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

## Debugging Considerations

The library delivery model has practical implications for debugging during development and for post-mortem analysis of field issues.

### Comparison

| Aspect | Static Libraries | Shared Libraries |
|--------|:----------------:|:----------------:|
| **Symbol availability in debugger** | All symbols in one binary — single symbol table, all addresses known at load | Debugger must discover `.so` files at runtime; symbols loaded per library as each `.so` is mapped |
| **Breakpoints** | Straightforward — all code addresses fixed at link time | Works, but lazy-bound PLT entries may require `set breakpoint pending on` or break on the resolved target |
| **Source-level stepping** | Seamless if debug info (`-g`) is included | Seamless if debug info is available per `.so` — identical experience once symbols are loaded |
| **Core dump analysis** | Self-contained — the single binary plus the core file is sufficient to reconstruct the full state | Requires the **exact matching `.so` versions** alongside the core file. If `.so` files have been updated since the crash, stack traces may be incorrect |
| **Stripped production binaries** | External debug info (`.debug` file) must match the deployed binary | External debug info must match **per `.so`** — requires tracking debug symbols for each library version independently |
| **Hot code reload during development** | Not possible — must relink and restart the entire binary | Possible in principle (`dlclose` / `dlopen`) — useful for rapid iteration on a single module without full restart. **Warning:** `dlclose()` must never be used when objects from the `.so` are still alive — for C++ shared libraries with virtual interfaces, `dlclose` unmaps code pages and any live objects with vtable pointers into that `.so` become use-after-free; subsequent virtual calls jump to unmapped memory. |
| **Address Space Layout Randomization (ASLR)** | Single base address randomized; relative offsets stable | Each `.so` is independently randomized — debugger handles this transparently, but manual address calculations are more complex |
| **Debug build size** | One large binary with all debug info embedded | Smaller per-library debug files; total may be similar but more manageable for partial debugging |

### Practical Impact for S-CORE

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

**Conclusion:** Static linking has a clear advantage for **post-mortem debugging and field issue analysis** due to its self-contained nature. Dynamic linking adds operational complexity for maintaining debug symbol archives and matching `.so` versions to core dumps. For development-time debugging, both models are equivalent.

## Operating System Support (Linux and QNX)

S-CORE targets both Linux and QNX as deployment platforms. Both operating systems support static and dynamic linking, but with differences in maturity, tooling, and behavior that are relevant to this decision.

### Feature Comparison

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

### Linux-Specific Considerations

- **Mature ecosystem:** Dynamic linking is the dominant model on Linux. The toolchain (GCC, LLVM, ld, ldd, ldconfig) is highly optimized for shared libraries. Package managers, distribution models, and most middleware on Linux assume dynamic linking.
- **musl libc and static linking:** For fully static binaries on Linux, `musl` (as alternative to glibc) provides clean static linking without hidden dynamic dependencies. Bazel supports musl-based static toolchains. This can simplify deployment on embedded Linux targets.
- **glibc and `dlopen` within static binaries:** glibc uses `dlopen` internally (e.g., for NSS, iconv). Fully static binaries with glibc may behave unexpectedly. This is a known limitation — not a concern for QNX.
- **ASLR:** Both PIE (static) and PIC (shared) binaries support full ASLR on Linux. No security difference between the models regarding address randomization.

### QNX-Specific Considerations

- **Microkernel + process model:** QNX's microkernel architecture results in many small processes (resource managers, drivers). Shared libraries are particularly beneficial here because many processes share common infrastructure code (libc, libsocket, etc.). S-CORE middleware modules fit naturally into this pattern.
- **Startup behavior:** QNX's `ldqnx.so` dynamic linker is leaner than Linux's, with lower symbol resolution overhead. Startup cost of dynamic linking is generally lower on QNX than on comparable Linux deployments.
- **Filesystem considerations:** QNX targets often use read-only filesystems (IFS / image filesystem). Shared libraries in the image are XIP-capable (execute-in-place) on some flash configurations — reducing RAM usage further.
- **Safety-certified configuration:** For ASIL-qualified QNX deployments, the OS vendor (BlackBerry QNX) provides guidance on certified library configurations. Static linking simplifies the certified configuration (fewer deployment artifacts), but QNX's safety documentation also covers dynamically linked configurations.
- **Toolchain:** QNX SDP provides both static and shared library support via its GCC/LLVM toolchain. Bazel cross-compilation for QNX requires a custom toolchain definition; both `cc_library` and `cc_shared_library` work with the QNX toolchain.
- **Secure execution policies:** QNX supports `procnto` security policies that restrict library loading to specific paths, mitigating `LD_PRELOAD`-style attacks. This partially addresses the security concerns of dynamic linking.

### Cross-Platform Implications for S-CORE

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

## License and FOSS Compliance

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

## ABI Stability and Versioning

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
5. **C++ interfaces:** ABI compliance is only ensured for C interfaces. If a library exposes a C++ interface, the C++ ABI is not standardized across compilers (GCC, Clang) or compiler versions. Therefore, either the library must provide a pure C interface at the `.so` boundary, or the build infrastructure must guarantee that the entire product (all `.so` files and their consumers) is built with the identical toolchain (same compiler, same version, same standard library).

**For static-only delivery**, this entire concern disappears — the consumer always builds against the exact source/headers they received. But the tradeoff is the loss of independent updateability.

## Testing Strategy

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

## Build Reproducibility and Deployment Hermeticity

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

## Library Initialization Order

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
- `.so` constructors must not call into the host module, must not modify global process state, and must not spawn threads.
- Provide explicit `score_<module>_init()` functions that applications call in a defined order.
- Document initialization dependencies between modules.

## Thread Safety and Lazy Binding

The default ELF dynamic linker behavior uses **lazy binding**: symbols are resolved on first call rather than at load time. This interacts with multi-threading:

| Scenario | Behavior |
|----------|----------|
| Single-threaded first call | Lazy resolution triggers linker code → safe |
| Multi-threaded first call to same symbol | Multiple threads may trigger resolution simultaneously → implementation-dependent |
| `LD_BIND_NOW` / `-Wl,-z,now` (eager binding) | All symbols resolved at load time before any application thread runs → fully deterministic |

To open a shared library at runtime, `dlopen()` can be used instead of `LD_BIND_NOW` (which resolves all symbols at program start). This is useful for plugin systems where libraries are loaded on demand. In such cases, the combination `RTLD_NOW | RTLD_LOCAL` shall be used — `RTLD_NOW` ensures all symbols are resolved immediately (no deferred failures), and `RTLD_LOCAL` prevents the loaded library's symbols from polluting the global namespace. However, `dlopen()` with these flags is not 100% thread-safe in all scenarios: if `dlopen()` is called from library constructors executing in parallel, or if combined with `fork()`, deadlocks or undefined behavior can occur.

**Linux:** glibc's dynamic linker is thread-safe for lazy binding (uses internal locks). The concern is largely historical but adds latency jitter — the first call to a symbol has unpredictable latency.

**QNX:** `ldqnx.so` is thread-safe for lazy binding. Same jitter concern applies.

**Impact on real-time systems:**
- Lazy binding introduces **latency non-determinism** — the first call to each function through the PLT may take microseconds longer than subsequent calls. For hard real-time applications (e.g., safety-critical control loops), this jitter is unacceptable.
- **Mitigation:** Use `LD_BIND_NOW` (or `-Wl,-z,now` at link time) to force eager binding. All symbols are resolved at startup, eliminating runtime jitter. Tradeoff: slightly increased startup time.
- For S-CORE, `LD_BIND_NOW` should be the **mandatory default** for any dynamically linked deployment in automotive/safety-critical contexts. This eliminates the thread-safety and latency-jitter concern entirely.

**Bazel integration:** The linker flag `-Wl,-z,now` can be added to the shared library's `linkopts` or to the consumer's link options to enforce eager binding. Bazel toolchain configuration can make this the default for all targets.

## Multi-Repository Architecture

S-CORE follows a multi-repository approach: each module (or group of related modules) lives in its own Git repository and is developed independently. These modules are integrated into the **reference integration repository** (`score_platform`) which composes them into a coherent platform. This architecture has significant implications for the linking model.

### Repository Structure

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

### Impact on Static Linking

| Concern | Assessment |
|---------|-----------|
| **Cross-repo dependency resolution** | Bazel handles this transparently — `bazel_dep()` fetches the source, and all code is compiled together in one build graph. Static linking works across repo boundaries as if the code were in a single repo. |
| **Diamond dependencies** | Bazel resolves to exactly one version of each dependency (MVS — Minimum Version Selection). No duplication in the final binary. |
| **Build reproducibility** | Fully hermetic — the `MODULE.bazel.lock` pins all transitive versions. The same build graph produces the same binary regardless of when it is built. |
| **Module independence** | Limited — a module's CI can build and test its own static library, but cannot produce a deployable artifact without the consumer. The module repo delivers source or `.a` files; the integration repo produces the final binary. |

**Consequence:** Static linking is **well-suited** for a multi-repo approach with Bazel. The integration repo builds everything from source (or from cached artifacts), and Bazel's dependency resolution eliminates version conflicts at build time.

### Integration Challenges Apply to Both Models

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

### Impact on Dynamic Linking

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

### Diamond Dependency Problem — Detailed Example

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

### Multi-Repo and the Opt-In Model (Option 4)

The opt-in model interacts favorably with the multi-repository approach:

| Pattern | How it works |
|---------|-------------|
| **Module repo delivers static library** (default) | The module publishes a Bazel module (`bazel_dep`) that exposes `cc_library` targets. The integration repo links everything statically. Simple, no ABI concerns across repos. |
| **Module repo delivers shared library** (opt-in) | The module additionally publishes a pre-built `.so` with a stable C ABI and Soname versioning. The module's CI tests the `.so` independently. The integration repo can consume either the source (for static) or the `.so` (for dynamic). |
| **Internal dependencies within a `.so`** | When a module opts into `.so` delivery, its transitive in-repo dependencies are statically linked into the `.so`. Only the public API is exposed. This eliminates cross-repo diamond dependency problems for internal code. |
| **Shared infrastructure libraries** | Widely-used infrastructure (e.g., serialization, logging) can be delivered as `.so` with strict ABI guarantees. These require the most rigorous versioning and compatibility testing across repos. |

### Bazel Integration for Multi-Repo

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
