<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->
(DR-002-Arch-detailed-assessments)=
# DR-002-Arch: Detailed Assessments

                                                            
This page provides detailed evaluation assessments for the :ref:`Library Delivery Model <DR-002-Arch>` design decision.

## Update Granularity — Detailed Assessment

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

## Performance Differences — Indicative Values and Hardware Dependencies

Precise performance numbers cannot be stated universally because they depend heavily on target hardware characteristics (CPU microarchitecture, cache hierarchy, flash/storage type, MMU capabilities). However, published research and industry experience provide **order-of-magnitude orientation:**

### Per-Call Overhead (PLT/GOT Indirection)

| Hardware class | Overhead per cross-library call | Notes |
|----------------|:-------------------------------:|-------|
| ARM Cortex-A (with branch predictor) | ~1–5 ns | Branch prediction mitigates most of the indirect jump cost. GOT entry is typically in L1 cache for hot paths. |
| ARM Cortex-R (no/simple branch predictor) | ~5–20 ns | Indirect jumps are more expensive without speculative execution. Relevant for safety-critical real-time controllers. |
| x86-64 (modern) | ~1–3 ns | Highly optimized branch prediction. Negligible for most workloads. |

**Context:** For a middleware API that is called at kHz rates (e.g., logging, diagnostics polling), this overhead is immeasurable. For APIs called at MHz rates in tight loops (e.g., serialization of high-frequency sensor data), the cumulative cost can reach low single-digit percent — typically dominated by the inability to inline across the library boundary rather than the PLT jump itself.

### Link-Time Optimization (LTO) Benefit Lost

LTO across the entire binary (static case) vs. LTO only within each `.so` (dynamic case) can yield:

- **Typical improvement from full-binary LTO:** 5–20% for compute-bound code (published GCC/LLVM benchmarks).
- **For I/O-bound or event-driven middleware code:** Often <5%, as performance is dominated by system calls, IPC, and data copying rather than instruction efficiency.
- **S-CORE relevance:** Most middleware APIs are I/O-bound or event-driven (communication, diagnostics, logging). The LTO benefit of static linking is likely in the **low single-digit percent range** for typical middleware call patterns. Compute-intensive modules (e.g., cryptographic operations, data serialization) may see larger benefits.

### Startup Time (Symbol Resolution)

| Factor | Typical impact |
|--------|:--------------:|
| Per-symbol resolution (ELF hash lookup) | ~0.5–2 µs per symbol (ARM Cortex-A) |
| Library with ~500 exported symbols | ~0.5–1 ms relocation time |
| Library with ~5000 exported symbols | ~5–10 ms relocation time |
| `LD_BIND_NOW` (full eager binding) | Paid once at startup, zero cost afterwards |
| Lazy binding (default) | Startup faster, first call to each symbol slower |

**Context:** For a middleware with a well-designed API surface (hundreds, not thousands of exported symbols per `.so`), the startup overhead of dynamic linking is typically in the **low millisecond range per library** — negligible for most automotive boot sequences.

### System-Wide Startup (Multi-App, Flash I/O)

This is the most hardware-dependent factor:

| Storage type | Sequential read speed | Impact of N×static vs. 1×shared |
|-------------|:---------------------:|:---:|
| eMMC (typical automotive) | 100–300 MB/s | Significant: 10 apps × 5 MB middleware = 50 MB vs. 5 MB |
| NOR flash (direct-execute) | 50–100 MB/s | Most significant: I/O is the bottleneck |
| NVMe / UFS 3.x | 1–3 GB/s | Less significant: I/O cost is amortized by high bandwidth |

### Summary

| Performance aspect | Magnitude of impact | Hardware-dependent? | Measurable in S-CORE context? |
|-------------------|:-------------------:|:-------------------:|:-----------------------------:|
| PLT/GOT per-call overhead | Low (ns) | Moderate | Yes, via micro-benchmarks |
| LTO benefit lost | Low–moderate (%) | Low | Yes, via A/B benchmarks |
| Startup symbol resolution | Low (ms) | Moderate | Yes, via profiling |
| Multi-app flash I/O savings | Moderate–high (ms–s) | **High** | Requires target hardware |

**Recommendation:** The performance difference between static and dynamic linking is **not the dominant decision criterion** for a middleware platform. In most deployment scenarios, the per-call overhead is negligible for middleware APIs, and the startup difference depends on hardware that varies across targets. Code size, RAM sharing, update granularity, safety, and security should weigh more heavily in this decision. Projects with hard real-time requirements on specific hot paths can address those through targeted design (e.g., header-only interfaces, inlined critical paths) regardless of the general linking strategy.
