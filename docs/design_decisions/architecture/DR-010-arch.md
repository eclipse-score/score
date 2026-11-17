<!-- ----------------------------------------------------------------------------
  Copyright (c) 2026 Contributors to the Eclipse Foundation

  See the NOTICE file(s) distributed with this work for additional
  information regarding copyright ownership.

  This program and the accompanying materials are made available under the
  terms of the Apache License Version 2.0 which is available at
  https://www.apache.org/licenses/LICENSE-2.0

  SPDX-License-Identifier: Apache-2.0
----------------------------------------------------------------------------- -->

# DR-010-arch: Target architecture for SOME/IP and DDS on mw::com

- **Date:** 2026-11-17

```{dec_rec} Target architecture for SOME/IP and DDS on mw::com
:id: dec_rec__arch__target_someip_dds_on_mwcom
:status: proposed
:version: 1
:tracking: TBD
:context: SOME/IP and DDS support is split across three repositories with two gateway forwarding paths, a socom layer that duplicates mw::com, and a prototype that bypasses both. S-CORE needs one target picture for the communication stack.
:decision: Applications use mw::com only. Same-host communication uses LoLa. Remote communication uses SOME/IP or DDS bindings, each implemented in the repository of its protocol owner against the binding interface in communication, placed in the application or in gatewayd. One stack daemon per protocol per host holds the wire protocol. Forwarding exists once, in communication. socom is retired in favour of mw::com services.
```

---

## Summary

- **Today:** SOME/IP and DDS support is split over three repositories. Forwarding
  and the service model exist twice, `socom` duplicates `mw::com`, and a prototype
  bypasses both.
- **Target:** applications use `mw::com` only. Same-host traffic uses LoLa. Remote
  traffic uses a SOME/IP or DDS binding, which lives in its protocol's repository
  and is built into the application or into `gatewayd`. Each protocol has one
  daemon per host that holds the wire protocol. Forwarding exists once, in
  `communication`. `socom` is retired.
- **Decided by this record:** the target picture (D1 to D7), who owns what
  (Responsibilities) and the order of work (Implementation Plan).
- **Not decided here:** the SOME/IP stack for `someipd` (lg-someip or opensomeip,
  Q1) and the io-sock fast path (Q2). The measurements in Evidence Required decide
  them.
- **Safety boundary:** QM daemons and the io-sock path never sit in an ASIL data
  path. `gatewayd` and ASIL bindings run in ASIL-B processes.

---

## Glossary

| Term | Meaning in this record |
|---|---|
| `mw::com` | S-CORE's service-oriented communication API, in the `communication` repository |
| LoLa | The `mw::com` binding for zero-copy shared memory on one host |
| Binding | The part of `mw::com` that moves data for one transport or protocol (LoLa, SOME/IP, DDS) |
| Binding interface (SPI) | The interface every binding implements, owned by `communication` |
| Daemon service interface | The `mw::com` services between a binding and a stack daemon |
| SOME/IP | Automotive service protocol over IP networks; SD is its service discovery |
| DDS | Data Distribution Service, a data-centric publish/subscribe standard |
| `someipd`, `ddsd` | Stack daemons, one per protocol per host, holding the wire protocol |
| `gatewayd` | The gateway process on the ASIL-B side; hosts bindings for applications that cannot use `mw::com` directly |
| QM, ASIL-B | Safety levels: QM is no safety requirement, ASIL-B is a safety requirement of the automotive standard ISO 26262 |
| E2E | End-to-end protection of a message (counter, CRC, identifier) checked by the receiver |
| io-sock | The QNX network stack process into which the prototype's kernel module is loaded |
| socom | The gateway's current service layer, retired by this record |
| TC8 | The SOME/IP conformance test suite that the gateway runs |
| Direct placement | The binding runs inside the application |
| Gateway placement | The binding runs inside `gatewayd` |
| FEP, FCP, Shepherd | The feature proposal process: an author's proposal, a 10-day final comment period, and the Architecture Community member who guides it (DR-002-Proc) |

## Context / Problem

S-CORE applications use `mw::com` as their service-oriented API. LoLa provides
zero-copy shared-memory communication on the same host. Remote communication
needs a SOME/IP binding (for ECUs running SOME/IP) and, per DR-009, a DDS
binding (for DDS domains).

Today the implementation is spread over three repositories and does not yet
form one picture:

- **`eclipse-score/communication`** holds the `mw::com` core. Its SOME/IP
  binding is a skeleton without a transport: service discovery returns
  `kInvalidBindingInformation` with TODOs, and event sending returns
  `kBindingFailure` ("unsupported without a transport"). The binding list is a
  closed enum (`BindingType`) and the runtime factory creates runtimes from a
  fixed list, so a new binding requires a code change and a rebuild. It also
  contains a LoLa-to-LoLa gateway (`score/mw/com/gateway`) that forwards events
  between domains with a `GenericProxy`, a `Transport` interface and a
  `GenericSkeleton` on the destination side.
- **`eclipse-score/inc_someip_gateway`** holds `gatewayd` (ASIL-B),
  `someipd` (QM), `socom`, `gateway_ipc_binding` and a serializer. The
  `gateway_ipc_binding` package forwards events across the `gatewayd`/`someipd`
  process boundary with the same `GenericProxy`/`GenericSkeleton` pattern as the
  communication gateway. `socom` is documented as intra-process only; it is
  bridged across processes by `gateway_ipc_binding`. The forwarding pattern and
  the service model are therefore implemented twice. `gatewayd` does not yet
  implement E2E protection; the code has only comments.
- **Prototype** (`communication/experimental/someip_sd`) adds an SD-only daemon,
  a custom control protocol over `score::message_passing`, and an io-sock kernel
  module that moves SOME/IP event payloads outside the daemon. The module is
  declared QM, has no E2E, runs the LoLa runtime inside the io-sock process, and
  cannot be unloaded.

The gateway is still in active use and is the only place where ASIL-B
processing is planned. The gap is not a missing gateway; it is that the
gateway duplicates forwarding and a service model that `mw::com` already
provides, and that the stack and binding boundaries are not defined.

Methods are not covered by the current `mw::com` generic proxy and skeleton
(events only). `socom` is the only layer in the gateway that supports methods
today, and generic methods in `mw::com` are not scheduled
(`eclipse-score/communication#767`).

## Decision

S-CORE adopts the following target architecture for SOME/IP and DDS on
`mw::com`. The component view is shown below and the source is kept next to
this record as `_assets/DR-010-arch-target_component.puml`.

![Target architecture](_assets/DR-010-arch-target_component.png)

**D1 — `mw::com` first.** Applications use the `mw::com` API only. Applications
on the same host communicate through the LoLa binding. Applications on another
ECU communicate through a SOME/IP or DDS binding. The binding is implemented in
the repository of its protocol owner (see Responsibilities) and runs either in
the application (direct placement) or in `gatewayd` (gateway placement).

**D2 — One forwarding path.** Forwarding between a local `mw::com` service and a
remote binding is implemented once, in `communication`, generalised from the
existing LoLa gateway. The forwarding code in `gateway_ipc_binding` is retired.

**D3 — `socom` is retired.** The daemon contract between a binding and a stack
daemon is defined as `mw::com` services (the daemon service interface). `socom`
is removed once `mw::com` provides generic methods. Until then, methods are the
only blocking item.

**D4 — `gatewayd` has a narrow role.** `gatewayd` is used for applications that
cannot use `mw::com` directly (legacy LoLa applications, native DDS peers) and
for functions that need an ASIL-B host: E2E protection, policy and access
control. `gatewayd` contains no forwarding code of its own.

**D5 — One stack daemon per protocol per host.** `someipd` holds the SOME/IP
protocol and service discovery. `ddsd` holds the DDS participant and DDS
transport. Protocol logic lives only in these daemons. The bindings talk to a
daemon through the daemon service interface and never link a protocol stack.

**D6 — The serializer is a shared plugin.** A serializer plugin interface per
service type is used by all bindings and by `gatewayd`. A null serializer passes
pre-serialized payloads through unchanged. The location of the implementation
is decided in a follow-up record.

**D7 — The io-sock fast path is optional.** A kernel-side transport can be added
as a transport plugin of `someipd`, behind the same interface. It is not part
of any ASIL data path. It is enabled only if a measurement shows a material gain
over the daemon path on target hardware.

The following are not part of the target:

- a kernel module in an ASIL data path;
- an `mw::com` runtime inside a kernel module or inside the io-sock process;
- a second SOME/IP daemon, or a second SOME/IP stack in applications;
- a new gateway repository.

The choice of SOME/IP stack for `someipd` (lg-someip, or opensomeip hosted inside
`someipd`) is not decided here. It is decided on the measurements
in the Evidence Required section. The location of the stack source (dependency
or in-tree) is decided with it.

## Responsibilities

### Principles

**P1 — The core and the contract live in `communication`.** `communication` holds
the `mw::com` API, the LoLa binding, the binding interface (SPI), the build-time
binding table, the forwarding API, the serializer plugin API and the definition
of the daemon service interface. It holds no protocol implementation and no
protocol daemon.

**P2 — One repository per protocol family, not per binding or per stack.** The
number of bindings grows with the number of protocols (SOME/IP, DDS, and any
future protocol), not with the number of stack variants. Stack variants
(lg-someip, opensomeip, Cyclone DDS) sit behind a daemon (D5) and never
add a binding. This keeps the number of repositories and bindings bounded.

**P3 — The owner of a protocol owns its binding, daemon and tests.** The protocol
owner maintains the binding, the daemon, the stack integration, the protocol
conformance tests and the safety analysis of the protocol path.

**P4 — Shared interfaces change through a FEP.** The binding interface, the
daemon service interface, the serializer plugin API and the forwarding API are
shared across feature teams. A change to any of them is cross-team and requires
a FEP with a Shepherd and a final comment period, as defined in DR-002-Proc.

**P5 — Dependencies point one way.** A binding depends only on the interfaces
published by `communication`. `communication` never depends on a protocol
repository and lists no binding as a dependency. A protocol repository never
depends on another protocol repository. A binding is a build-time dependency of
the binary that uses it (an application, `gatewayd` or a test), not of
`communication`.

**P6 — ASIL-B logic runs only where the safety concept places it.** `gatewayd`
and ASIL-classified bindings run in ASIL-B processes. A QM daemon never links
ASIL-B code, and an ASIL-B process never links a protocol stack (D5).

### Ownership

| Area | Owner | Repository | Owns | Does not own |
|---|---|---|---|---|
| `mw::com` core, LoLa binding, binding interface, build-time binding table, forwarding API, serializer plugin API, daemon service interface definition | Communication FT | `eclipse-score/communication` | The interfaces and their conformance tests | Protocol logic, daemons, stacks |
| SOME/IP protocol: `someipd`, SOME/IP binding, stack integration, TC8 conformance | SOME/IP gateway FT | `eclipse-score/inc_someip_gateway` (repository may change, see open points) | The SOME/IP protocol path end to end | The binding interface |
| `gatewayd` (ASIL-B host): E2E, policy, access control, configuration | SOME/IP gateway FT | `eclipse-score/inc_someip_gateway` | ASIL-B processing of routes | Forwarding logic (in `communication`) |
| DDS protocol: `ddsd`, DDS binding, DDS integration | DDS FT, to be created | DDS repository, to be decided | The DDS protocol path end to end | The binding interface |
| Serializer implementations for each service type | To be assigned | To be decided | Generated or hand-written payload serializers | The serializer plugin API |
| External stacks: lg-someip, opensomeip, Cyclone DDS | Owner of the daemon that uses them | Dependency, not a repository of S-CORE | Version pinning, licence review, updates | Anything else |
| Performance evidence (T1 to T8) | SOME/IP FT for the protocol path; Communication FT for `mw::com`-level figures | Both | The results of tests T1 to T8 | — |
| Decision records | Architecture Community, with the leads of the affected feature teams | `eclipse-score/score` | The records | — |

### Rules for a new binding

1. A binding is added per protocol family, never per stack variant. Stack
   variants of an existing protocol are integrated in its daemon.
2. A new protocol gets one owner (a feature team), one repository, and a
   binding that passes the binding conformance tests from `communication`.
3. The repository is created through a FEP, because it is a platform-level
   change.
4. The set of bindings in a binary is fixed at build time. The binding is linked
   into the binary that uses it, and a generated table lists the bindings that
   binary contains. At startup, the binding runtimes are created only for bindings
   in that table, selected by the deployment configuration. Adding a binding
   needs no change to the `mw::com` core. Nothing is registered, loaded or
   allocated for a binding after startup (allocation is allowed at startup and
   shutdown only, as agreed in the SOME/IP gateway meeting minutes of 2026-03-31). Today
   the binding type is a closed enum and the runtime factory a fixed list (see the
   binding selection row in the inventory); Phase 2 replaces both with the
   build-time table.

### Future feature team structure

- **Now:** two feature teams: Communication (core and interfaces) and the
  SOME/IP gateway (protocol path, `gatewayd`).
- **Next:** a DDS feature team owning the DDS repository, the DDS binding and
  `ddsd`. Until it exists, the DDS feature request authors coordinate the DDS
  work, and the DDS binding stays out of `communication`.
- **Rule:** one feature team per protocol family, plus the core team. The number
  of feature teams therefore grows with protocols, not with bindings or stacks.

### Open points

- Owner and repository of the DDS protocol path.
- Repository of the SOME/IP protocol path: the incubation repository
  `inc_someip_gateway`, or a repository of its own after promotion.
- Owner of serializer implementations, and their relation to the code generation
  feature.
- Where the SOME/IP binding is built. It is needed by the gateway and, for direct
  placement, by applications. If it is part of the `inc_someip_gateway`
  repository, applications depend on the gateway repository; a package of its own
  avoids that.
- How a binding proves conformance to the binding interface: a test suite in
  `communication` that each protocol repository runs in its own CI.

## Implementation Plan

The work follows six phases. Each phase ends with an exit check, and a later
phase does not start until the earlier exit check is met.

**Phase 0 — Decide.** The Architecture Community accepts this record and the
follow-up records (stack choice, fast path, serializer location, DDS daemon
repository, SOME/IP binding location, conformance test suite). The record supersedes DR-001 in `inc_someip_gateway`.
Exit: decision records accepted.

**Phase 1 — Evidence.** Run the verification tests (T1 to T8, defined in Evidence
Required) for lg-someip
and opensomeip, each hosted inside `someipd`, on the same hardware, and the
fast-path test T5.
Exit: results published; Q1 and Q2 decided from them.

**Phase 2 — Foundation in `communication`.** A build-time binding table, so that
a binding can be added without a change to the `mw::com` core; generic methods in `mw::com`
(`communication#767`); forwarding generalised from the LoLa gateway; the
serializer plugin interface; the daemon service interface as `mw::com`
services. Exit: a test binding is added without changing the `mw::com` core,
and forwarding passes its tests with one transport.

**Phase 3 — SOME/IP path.** `someipd` runs on the chosen stack and offers the
daemon service interface. The SOME/IP binding uses it as transport.
`gateway_ipc_binding` forwarding is replaced by the shared path. `socom` is
removed once methods work on `mw::com`. Exit: the gateway path with E2E (T4) and
TC8 conformance (T1) pass on the new path.

**Phase 4 — Gateway safety and direct placement.** E2E protection implemented
in `gatewayd`. Direct placement: the same E2E check runs in the application's
binding for ASIL applications. Safety review of the QM/ASIL boundary and of the
daemon interface. Exit: safety review passed; fault-injection test T6 passed.

**Phase 5 — DDS.** `ddsd` and the DDS binding, using the same daemon service
interface and serializer. Exit: a native DDS peer interoperates with an `mw::com`
application through the gateway.

**Phase 6 — Optional fast path.** Only if Q2 is positive. Lives in `someipd` as
a transport plugin, never in an ASIL data path.

### Dependencies

- Build-time binding table in `mw::com` (Phase 2): needed before a new binding
  can be added without a core change.
- Generic methods in `mw::com` (`communication#767`, no timeline): needed before
  `socom` can be removed.
- Decision on the repository for the stack source and the DDS daemon: needed in
  Phase 0.
- Safety evidence for lg-someip: LG reports a qualification for its AUTOSAR
  variant, not for the open-sourced code (Phase 4). The record makes no
  compliance claim for any stack.

### Risks

| Risk | Mitigation |
|---|---|
| Generic methods in `mw::com` take longer | Keep `socom` for methods only until they land; do not block events on it |
| lg-someip open-source code is not safety-qualified | Qualification plan in Phase 4; keep both candidates under evaluation until the qualification path of the chosen stack is known |
| opensomeip gaps (port sharing, SD for several applications, event fan-out) must be closed inside `someipd` | Estimate the work in `someipd` before Q1 is decided; the gaps are the proponent's list, not ours |
| Defects found late in the open-sourced stack (undefined behaviour and framing bugs were fixed after its public release) | Sanitizer runs in Phase 1 (T7) |
| Two teams own parts of one path (`communication` and `inc_someip_gateway`) | Interfaces fixed in Phase 2 before implementation |
| Benchmark numbers come from the stack proponent | Phase 1 measures on our hardware |

### Not part of the target

- A kernel module in an ASIL data path.
- An `mw::com` runtime inside a kernel module or the io-sock process.
- A second SOME/IP daemon.
- A new gateway repository.
- Changes to application code for SOME/IP or DDS.

## Evidence Required

Two decisions depend on measurements: Q1, the stack for `someipd`, and Q2, the
io-sock fast path. The LG slides are hypotheses to check, not evidence: they
measure opensomeip without SD and daemon on Raspberry Pi 4, and nothing in them
has been reproduced on our hardware.

| ID | Question | Decides |
|---|---|---|
| Q1 | Which stack runs in `someipd`: lg-someip or opensomeip? | Follow-up record 1 |
| Q2 | Is the io-sock fast path worth a second data path next to the daemon? | Decision D7 |

Q2 depends on Q1: the fast path must beat the daemon path of the stack that is
chosen.

### Verification tests

| Test | Covers | Measured by |
|---|---|---|
| T1 | TC8 conformance of each candidate | `tests/tc8_conformance` |
| T2 | Multi-application host: port sharing, SD visibility, fan-out | Functional test, run set R5 |
| T3 | Target performance of the candidates | Run matrix R1 to R4 |
| T4 | Gateway path with E2E checked on the ASIL side | `tests/integration_test` |
| T5 | Fast path against the daemon path | Run sets R1 and R2, variant A against B or C |
| T6 | Fault injection on the QM/ASIL boundary: stack process killed, corrupted payloads, flooding | Fault-injection test, to be built |
| T7 | Sanitizer runs (ASan, UBSan, TSan) of each candidate stack | Sanitizer build of each candidate |
| T8 | Build and maintenance: QNX SDP build, dependencies, licence obligations | Build and licence review |

### What exists

The benchmark harness in `communication/experimental/someip_sd/benchmark`
already measures:

- **Round trip** over the io-sock path: `someip_bench_lola`, with the reflector
  on lg-someip. Output per run: p50, p90, p99, p999, loss and duplicates.
- **Mixed load** from a realistic event mix (`someip_event_workload.csv`):
  `someip_load_lola` and `someip_load_peer`, with `LOAD_RESULT` and `CPU_RESULT`
  and `load_report.py --compare` for two runs.
- **Hardware scripts:** `run_hw_load.sh` runs the whole flow on IPNext hardware,
  with `--stack iosock`.

What does not exist: a benchmarked side for lg-someip inside `someipd`, or for
opensomeip inside `someipd`. The wire contract (`bench_protocol.h`) is independent of
the stack, so these are new applications with the same options and output
format.

### Fairness problems to fix first

1. **Polling.** The module polls every ~10 ms, so its latency is dominated by
   polling (p50 about 17 ms on QEMU). A daemon path with event-driven wake-ups
   would look worse for a reason that is not the architecture. Fix:
   event-driven wake-ups (the `iosock_wakeup_spike` is the starting point) before
   the Q2 runs. If that is not possible in time, report the polling penalty
   separately and do not decide Q2 from latency.
2. **Zero-copy threshold.** TX copies payloads up to 2 KB; above that the mbuf
   keeps the LoLa sample until the driver frees it. Report 16 B and 1400 B
   separately.
3. **Peer.** The round-trip reflector is lg-someip for every candidate. The peer
   stays fixed for all candidates, and the results say so.
4. **Unloadable module.** The io-sock module cannot be unloaded. Restart io-sock
   or the target before each io-sock variant, and never run two bundles in one
   boot.
5. **CPU definition.** CPU per event or request is the CPU of all target
   processes on the path (module, daemon, application), divided by the number of
   events. The same definition is used for every candidate. The sampler needs
   root and read access to `/proc/<pid>/as` of io-sock.
6. **Environment.** Same hardware, CPU governor `performance`, same SD settings
   and ports, same payloads, same workload file. QEMU results are functional
   checks only.

### Variants measured

The candidates for `someipd` are B (lg-someip) and C (opensomeip). Both run
inside `someipd`, behind the same daemon interface and the same host coordinator,
so they are measured on the same path. Variant D (opensomeip as a library in each
application, without a daemon) is an optional reference for the best case that
the stack proponent reports for small messages; it is not a candidate, because it
has no host-wide coordination (test T2).

| Variant | Path measured | Status | Used for |
|---|---|---|---|
| A. io-sock | app → LoLa → io-sock module → network | exists | Q2 |
| B. lg-someip in `someipd` | app → binding → `someipd` (lg-someip) → network | to build | Q1, Q2 |
| C. opensomeip in `someipd` | app → binding → `someipd` (opensomeip, from PR `#435`) → network | to build | Q1, Q2 |
| D. opensomeip library, no daemon (optional reference) | app → opensomeip → network | to build, optional | reference only |

### Build list

1. Fairness fix for variant A (item 1 above), or the reporting rule for it.
2. Two benchmark applications, B and C, that run through `someipd`, and the
   optional reference D. Each reads the same options as `someip_bench_lola`, uses
   the same wire contract and output format, and reuses `gen_load_workload.py`
   for the mixed load.
3. One QNX target bundle per stack (Bazel), with the stack's configuration.
4. Extend `run_hw_load.sh` with `--stack lgsomeip` and `--stack opensomeip`, with
   the same arguments for both.
5. Calibration: run the same variant twice under the same setup. The two results
   must agree within the spread of the repetitions; otherwise the setup is not
   comparable.

### Run matrix

Each cell is run five times, with the variant order rotated between repetitions.
The target is restarted between variants. Results are reported as median and
spread (min and max).

| Run set | Scenario | Variants | Measure |
|---|---|---|---|
| R1 | Round trip, 16 B and 1400 B, 100 Hz, 300 pings | A, B, C, D | p50, p99, loss |
| R2 | Mixed load, scales 0.25, 0.5, 1.0 | A, B, C | CPU per event, delivery, latency per class |
| R3 | Fan-out: 1, 2 and 8 subscribers on the target, 1 KB events | A, B, C, D | CPU per event, bytes on link |
| R4 | Footprint: peak RSS per process, stripped size | A, B, C, D | MB, KB |
| R5 | Multi-application host: three applications offer and consume on one host | B, C | Functional only: port sharing, SD visibility, fan-out (test T2) |

### Decision rules (proposals, to be confirmed by the Communication FT)

**Q1 — stack for `someipd`**

1. Eligibility, all required: TC8 conformance (T1) reported for each candidate and
   accepted by the Communication FT; host coordination passes (R5); no open
   undefined-behaviour or memory findings in sanitizer runs (T7).
2. Among eligible stacks, choose the lower p99 round-trip time at 16 B and 1400 B
   (R1), and the lower CPU per event in R2 at scale 1.0.
3. If the difference is below 10 % on all of these, the tie is decided by the
   qualification path and the maintenance cost. The proponent describes
   opensomeip as pre-1.0 with safety alignment ongoing and not certified, and
   reports a qualification for the AUTOSAR variant of lg-someip only. The record
   makes no compliance claim for either.

**Q2 — io-sock fast path**

Accept the fast path only if, compared with the daemon path of the stack chosen
in Q1 (B or C):

- p99 round-trip time improves by at least 20 % at 16 B and at 1400 B (R1), and
- CPU per event improves by at least 20 % in R2 at scales 0.5 and 1.0, and
- both improvements are larger than the spread of the repetitions, and
- the latency comparison was made with event-driven wake-ups (item 1 above).

If any condition fails, the fast path is dropped (D7).

### Commands

Existing, on QEMU (functional check only):

```sh
bazel test --config=qnx_x86_64 //experimental/someip_sd/benchmark:someip_bench_dual_qemu_test \
    --test_output=all --nocache_test_results
```

Existing, on IPNext hardware:

```sh
./run_hw_load.sh --stack iosock      # variant A
```

Compare two runs:

```sh
python3 load_report.py --compare <A target results.txt> <A peer results.txt> \
    <B target results.txt> <B peer results.txt>
```

Variants B, C and D follow once their bundles and `--stack` options exist.

### Outputs and versions

- Raw results per variant, repetition and run set, in one directory per run.
- A table per decision: median, spread, and the decision rule applied.
- Versions of every component: this repository's commit, the lg-someip commit
  `d09656e`, the opensomeip version or commit (PR `#435`) and the QNX SDP version.
- Results are attached to the follow-up records for Q1 and Q2.

### Risks and open points

- The io-sock module cannot be unloaded, so each io-sock variant needs a restart,
  which makes the runs slow.
- The secpol rules for io-sock hosting LoLa are not defined yet. The secpol
  violations printed by `run_target.sh` must be empty before the measurements
  count.
- Owners and dates are not set here. The Communication FT assigns them.

## Component Inventory

Every component found while preparing this record, with its current location,
its disposition and its target location. Sub-components of a listed directory
share its disposition unless listed separately.

Dispositions:

- **Stay**: kept as it is.
- **Rework**: kept, changed as described in Decision.
- **Move**: kept, moved to another repository or directory.
- **Replace**: removed and replaced by a new component.
- **Retire**: removed once its replacement exists (see D3).
- **Drop**: deleted; not carried forward.
- **Optional**: kept only if the stated condition is met.
- **Open**: depends on a decision in Follow-up records.
- **New**: does not exist yet.
- **External**: third-party dependency, not owned by S-CORE.

### Communication (`eclipse-score/communication`)

| Component | Current location | Disposition | Target location and note |
|---|---|---|---|
| LoLa binding | `score/mw/com/impl/bindings/lola` | Stay | Same-host zero-copy path (D1) |
| SOME/IP binding (stub) | `score/mw/com/impl/bindings/someip` | Move | Moves to the SOME/IP protocol repository; gets a transport through the daemon service interface (D1, D5). The binding interface stays in communication |
| Binding selection | `score/mw/com/impl/binding_type.h`, `plumbing/binding_runtime_factory.cpp` | Rework | Bindings listed in a build-time table; no core change to add one |
| LoLa gateway (inter-domain) | `score/mw/com/gateway/gateway_application` | Rework | Generalised into the shared forwarding path (D2) |
| Gateway transport interface and factory | `score/mw/com/gateway/transport_layer` | Stay | Basis for the forwarding transport; hypervisor transports stay with the LoLa gateway |
| Gateway README | `score/mw/com/gateway/README.md` | Rework | Updated for the shared forwarding path |
| `error_serializer` | `score/mw/com/impl` | Stay | Not affected |
| Serializer plugin API | `inc_someip_gateway/score/serializer` | Move | The plugin interface moves to communication (D6) |
| Serializer implementations, including the null serializer | `inc_someip_gateway/score/serializer` | Open | Location decided by follow-up 3 (D6) |
| Daemon service interface | none | New | `mw::com` services between a binding and a stack daemon (D3) |
| Shared forwarding | partly in the LoLa gateway and in `gateway_ipc_binding` | New | One path in communication (D2) |
| DDS binding | none | New | In the DDS protocol repository, against the binding interface in communication (DR-009, Option B) |

### Gateway (`eclipse-score/inc_someip_gateway`)

| Component | Current location | Disposition | Target location and note |
|---|---|---|---|
| `gatewayd` | `score/gatewayd` | Rework | Uses the shared forwarding path; no forwarding code of its own; ASIL-B host (D4) |
| E2E in `gatewayd` | not implemented (comments only) | New | Implemented in `gatewayd` (Phase 4) |
| `someipd` | `score/someipd` | Rework | Offers the daemon service interface; stack behind an interface (D5) |
| SOME/IP stack in `someipd` | `@vsomeip` (`score/someipd` BUILD) | Replace | Replaced by the chosen stack, lg-someip or opensomeip (follow-up 1); vsomeip is out of the candidate set |
| `socom` | `score/socom` (about 34 files, mocks, tests, docs) | Retire | Removed once generic methods exist in `mw::com` (D3) |
| `gateway_ipc_binding` | `score/gateway_ipc_binding` (about 22 files) | Replace | Forwarding moves to communication; per-service logic replaced by the daemon service interface (D2) |
| `bridged_services` | `score/bridged_services` | Rework | Bridge configuration taken from the `mw::com` deployment |
| SOME/IP constants and types | `score/someip` | Stay | Used by the daemon |
| Gateway configuration schema | `score/config` | Stay | Gateway configuration |
| Deployment | `deployment/` | Stay | Packaging |
| Integration tests | `tests/integration_test` | Stay | Adapted to the new path |
| TC8 conformance tests | `tests/tc8_conformance` | Stay | Verification T1 |
| Benchmarks | `tests/benchmarks` | Stay | Verification T3 and T5 |
| Component requirements `socom.rst` | `docs/requirements/component` | Retire | With `socom` |
| Component requirements `gateway_ipc_binding.rst` | `docs/requirements/component` | Replace | Requirements for the shared forwarding path |
| DR-001 (socom as abstraction) | `docs/architecture/dec_someip_api_abstraction.rst` | Rework | Status changed to superseded by this record |
| DR-002 (`mw::com` as IPC) | `docs/architecture/dec_ipc_implementation.rst` | Stay | Consistent with this record |
| Migration sequence PR `#358` | open PR | Replace | Withdrawn or re-scoped to this record |
| `socom` work PRs `#322`, `#409`, `#417`, `#421` | open PRs | Drop | Stopped once this record is accepted |
| Feature integration test PR `#439` | open PR | Stay | Adapted to the new path |
| opensomeip in-process PR `#435` | open PR | Rework | Basis of candidate C; rebuilt behind the stack interface, not merged as a build switch |

### Prototype (`communication/experimental/someip_sd`)

| Component | Current location | Disposition | Target location and note |
|---|---|---|---|
| SD-only daemon (`SdFacade`, `SdOnlyRouter`) | `daemon/` | Drop | SD moves into `someipd` (D5) |
| Daemon protocol `sd_protocol.h` | `protocol/` | Drop | Replaced by the daemon service interface |
| Event module protocol `event_module_protocol.h` | `protocol/` | Drop | Replaced by the transport interface inside `someipd` |
| SD client library | `client/` | Drop | Replaced by bindings |
| POSIX event module (user-space stand-in) | `event_module/` | Drop | Not needed in the target |
| io-sock kernel module | `iosock_event_module/` | Optional | Transport plugin of `someipd` only if test T5 shows a material gain (D7); otherwise dropped |
| io-sock feasibility spike | `iosock_poc/` | Drop | Findings recorded in this record |
| io-sock wake-up spike | `iosock_wakeup_spike/` | Drop | Findings recorded in this record |
| Benchmark harness | `benchmark/` | Move | `tests/benchmarks` in the gateway repository |
| Dual-QEMU integration test | `test/` | Move | `tests/integration_test` in the gateway repository |
| Prototype diagrams and notes | `doc/`, `README.md` | Drop | Target diagram kept in this record |
| lg-someip third-party files and http_archive | `third_party/lg_someip`, `MODULE.bazel` | Open | Follows the stack decision (follow-up 1) |

### Other repositories, documents and proposals

| Component | Current location | Disposition | Target location and note |
|---|---|---|---|
| lg-someip in-tree proposal | communication PR `#1498` | Open | Follows the stack decision (follow-up 1) |
| lg-someip contribution proposal | score issue `#2807` | Open | Input to the stack decision |
| LIBERSOM (opensomeip) proposal | score issue `#3456` | Open | Input to the stack decision |
| TC8 and SOME/IP test suite proposal | score issue `#3464` | Open | Input to the verification plan |
| DDS daemon `ddsd` | none | New | DDS repository, to be decided (follow-up 4) |
| Cyclone DDS | external | External | Stack used by `ddsd` |
| DR-009 (DDS communication) | `score/docs/design_decisions/architecture` | Stay | Consistent with this record |
| DDS feature request | score PR `#2997` (fork) | Rework | Aligned with the daemon, binding and serializer decisions here |
| SOME/IP gateway feature page | `score/docs/features/communication/some_ip_gateway` | Rework | Refers to this record |

## Backwards Compatibility

The SOME/IP gateway has no released product. The SOME/IP gateway feature
page states that there is no previous gateway solution in S-CORE, so no
backwards compatibility is required for it. `socom` is internal to the gateway
repository and is not an application-facing API: `socom` appears only in
`gatewayd`, `someipd`, `gateway_ipc_binding` and `bridged_services`.

Applications are not affected. They continue to use `mw::com`, and their
deployment configuration changes only when a SOME/IP or DDS route is added.

In `communication`, the changes are additive: a build-time binding table without a
core change, generic methods, and a shared forwarding path. The existing LoLa
gateway keeps its behaviour and is generalised rather than replaced.

## Alternatives Considered

**Keep `socom` and finish the migration in progress** (`inc_someip_gateway#358`,
open PRs #322, #409, #417, #421). This keeps two service models and two
forwarding paths. Rejected because it keeps the duplication this record removes.

**Keep the current split** (`socom` over `gateway_ipc_binding` over `mw::com`).
This works today, but the duplication stays and the binding is not usable by
applications directly. Rejected.

**`mw::com` only, without `gatewayd`.** Not sufficient: legacy LoLa applications,
native DDS peers, policy and access control, and ASIL-side E2E placement need an
ASIL-B host. Rejected as the whole answer; kept as the default path (D1).

**A stack per application, without a host daemon** (the opensomeip library as
used in the proponent's comparison). This gives the lowest latency for small messages,
but each application then holds its own SD, ports and event fan-out, and port
sharing across services is not provided. Rejected for the host-wide
coordination the target needs; the measured latency gain is recorded as an
input to the stack decision.

**The io-sock kernel module as the main SOME/IP data path.** Rejected: the
module runs the LoLa runtime inside a QM system process, has no E2E, cannot be
unloaded, and its benefit has been measured only against its own user-space
stand-in on QEMU. It remains an optional transport (D7).

**All bindings in `communication`.** This keeps the code close to the `mw::com`
core, but every protocol and every later addition enlarges the core repository,
its ownership and its release cycle, and the core team would become responsible
for protocols it does not own. Rejected; the binding interface stays in
`communication` and the bindings move to their protocol repositories (P1, P2).

**One repository per binding.** This keeps each binding small, but it multiplies
repositories without a matching change in ownership, and it does not reduce the
work on the shared interfaces. Rejected; one repository per protocol family is
used instead (P2).

**Runtime loading or registration of binding libraries.** This would allow new
bindings without a build change. It raises questions about dynamic loading in the
QNX safety concept, and registration after startup conflicts with the rule that
allocation happens only at startup and shutdown. Rejected for ASIL. Build-time
linking is chosen (P5, rule 4).

## Rationale

The target puts each concern in one place. The wire protocol and the network
stack are in the daemon, which is QM. The binding interface is in `communication`,
which is the `mw::com` repository and holds no network stack; the bindings sit in
their protocol repositories. The ASIL-B logic is in `gatewayd`. A QM stack and an
ASIL-B consumer therefore never share a process, which is the
freedom-from-interference boundary the feature requirements already require.

It removes the two duplicated mechanisms that the repositories currently
implement: forwarding and the service model. Each of these is already provided
by `mw::com`, so the target reuses it instead of re-implementing it.

It keeps the LoLa binding as the zero-copy path on one host, and does not claim
zero-copy across the network: the network path always copies, and the zero-copy
benefit is limited to the local `mw::com` path.

The choices that depend on data (the stack, the fast path, the serializer
location) are deferred to follow-up records, so this record does not depend on
numbers that have not yet been measured on target hardware.

## Consequences

Work products that change:

| Work product | Repository | Change |
|---|---|---|
| Build-time binding table | `communication` | Bindings are added without a change to the `mw::com` core; nothing is registered after startup |
| Generic methods | `communication` | Required before `socom` is removed (`communication#767`) |
| Forwarding | `communication` | One path, generalised from the LoLa gateway |
| Serializer plugin interface | `communication` | Shared by all bindings and `gatewayd` |
| Daemon service interface | `communication` | `mw::com` services, replacing the `socom` contract |
| SOME/IP binding | SOME/IP protocol repository (`inc_someip_gateway`) | Moved from `communication`; gets a transport through the daemon service interface |
| `someipd` | `inc_someip_gateway` | Offers the daemon service interface; uses the chosen stack |
| `gatewayd` | `inc_someip_gateway` | E2E protection implemented; no forwarding code of its own |
| `socom` | `inc_someip_gateway` | Retired |
| `gateway_ipc_binding` forwarding | `inc_someip_gateway` | Replaced by the shared forwarding path |
| DR-001 | `inc_someip_gateway` | Status changed to superseded by this record |
| Prototype | `communication` | Moved into the target components or removed |
| DDS daemon and DDS binding | DDS repository (to be decided) | `ddsd` and the DDS binding, against the binding interface in `communication` |

Follow-up records that are needed:

1. SOME/IP stack for `someipd`, and the location of the stack source.
2. io-sock fast path (after the measurements in Evidence Required).
3. Serializer implementation location, shared with DDS.
4. Repository for the DDS daemon, and the owner of the DDS protocol path.
5. Location of the SOME/IP binding, and of the SOME/IP protocol repository.
6. Owner and location of the binding conformance test suite.

Open work that must be re-scoped: `inc_someip_gateway#358` (the migration
sequence, which keeps a reduced `socom`) and the open `socom` PRs #322, #409,
#417 and #421. Their scope should follow this record once it is accepted.

Verification: tests T1 to T8 (defined in Evidence Required) apply, in particular
TC8 conformance (T1), the multi-application host test (T2) and fault injection on
the QM/ASIL boundary (T6).

## Rejected Ideas

- A kernel module in an ASIL data path. Rejected: it is not a safety mechanism
  and it places `mw::com` in a QM system process.
- A stack per application without a host daemon. Rejected for the reasons in
  Alternatives Considered.
- A new gateway repository for SOME/IP. Rejected: the gateway stays in
  `inc_someip_gateway` and the shared parts move to `communication`.

## References

- DR-009, DDS communication: `docs/design_decisions/architecture/DR-009-arch.md`
- DR-002-Proc, the FEP process: `docs/design_decisions/process/DR-002-proc.md`
- SOME/IP gateway feature page: https://eclipse-score.github.io/score/main/features/communication/some_ip_gateway/index.html
- DR-001 and DR-002 of the gateway: `inc_someip_gateway/docs/architecture/dec_someip_api_abstraction.rst` and `dec_ipc_implementation.rst`
- Gateway design discussion: https://github.com/orgs/eclipse-score/discussions/1984
- Communication FT discussion (stack comparison): https://github.com/orgs/eclipse-score/discussions/3365
- Stack contribution call: https://github.com/eclipse-score/score/issues/2787 (LG proposal `#2807`, LIBERSOM `#3456`, TC8 suite `#3464`)
- DDS gateway: https://github.com/eclipse-score/score/issues/2726, feature request PR https://github.com/eclipse-score/score/pull/2997
- lg-someip in `communication`: https://github.com/eclipse-score/communication/pull/1498
- Generic methods in `mw::com`: https://github.com/eclipse-score/communication/issues/767
- opensomeip in `inc_someip_gateway`: https://github.com/eclipse-score/inc_someip_gateway/pull/435
- Migration sequence: https://github.com/eclipse-score/inc_someip_gateway/pull/358
- LG measurement slides, attached to discussion `#3365`: `lg-someip-for-S-CORE_v0.3_26102026.pdf` (proponent's data, not reproduced here)
- Prototype and benchmark: `communication/experimental/someip_sd`
