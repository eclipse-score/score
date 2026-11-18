# DR-010-Arch: Introduce System Monitoring (SMon) Middleware Feature

- **Date:**

```{dec_rec} Introduce System Monitoring (SMon) middleware
:id: dec_rec__arch__introduce_smon_middleware
:status: proposed
:context: Architecture
:decision: Introduces a portable SMon middleware feature with standardized CPU and memory monitoring, threshold alerting, and decoupled integration interfaces across Linux and QNX.
:version: 1
:tracking: https://github.com/eclipse-score/score/issues/3340
:affects: doc__smon
:consequences: S-CORE project will get a new feature team and extra code to maintain
```

---

## Context

This feature request proposes introducing **System Monitoring (SMon)** as a reusable
S-CORE middleware feature for monitoring CPU and volatile memory
resource utilization on automotive ECUs running Linux or QNX.

SMon provides periodic resource measurements, configurable threshold
evaluation, and standardized integration interfaces for error
reporting, diagnostic fault recording, and logging.

On a Domain Controller ECU, multiple applications share CPU and memory resources simultaneously.
There is currently no standardized S-CORE middleware feature that:

- Periodically measures CPU and memory load at the **system, core, process, and
  application-group** level
- Evaluates those metrics against **configurable thresholds** and triggers fault reporting
  (error aggregator + DTC) or warning logs accordingly
- Operates portably across **Linux and QNX** via a clean platform abstraction boundary
- Exposes **well-defined required interfaces** for error reporting, DTC recording, and logging —
  fully decoupled from any specific backend implementation

Without such a feature, each project team implements ad-hoc monitoring logic, leading to
fragmentation, inconsistency, and missed faults across vehicle programs.

### Detailed Feature Requirements

Detailed requirements are documented separately in the feature requirements tree:

- Feature entry point: [System Monitoring](../../features/smon/index.rst)
- Requirements specification: [System Monitoring Requirements](../../features/smon/requirements/index.rst)

### Requested Capabilities

### CPU Monitoring

- [ ] Overall system CPU load (as a percentage)
- [ ] CPU load per individual core
- [ ] CPU load per running application (process)
- [ ] CPU load per configured application group

### Memory

- [ ] Overall volatile memory load (as a percentage)
- [ ] Volatile memory load per running application (process)
- [ ] Volatile memory load per configured application group
- [ ] Total and available system memory
- [ ] Per-process memory as USS, RSS, PSS, and VM (where supported by the OS)

### Threshold & Alerting

- [ ] Configurable threshold rules per metric type
- [ ] Configurable comparison operator per rule (e.g., greater than)
- [ ] Configurable actions per rule: `ReportError`, `RecordDTC`, `LogWarning`
- [ ] Configurable trigger mode per action: `Always` or `OnChange`
- [ ] Threshold rules scopeable to a specific application or application group

### Integration Interfaces

- [ ] Required interface for error reporting to the central error aggregator
- [ ] Required interface for DTC recording in the fault memory
- [ ] Required interface for log message publication

### Configuration

- [ ] All parameters readable from an external file (e.g., JSON) at startup — no recompilation
- [ ] Named application groups definable in configuration
- [ ] Logging enable/disable configurable per metric category
- [ ] Metrics logging interval configurable
- [ ] One or more threshold rules definable in configuration

### General & Platform

- [ ] Structured log messages published at the configured interval
- [ ] Graceful shutdown on `SIGINT` / `SIGTERM`
- [ ] Concurrent metric collection to minimize per-cycle latency
- [ ] Portable between Linux and QNX via a platform abstraction boundary
- [ ] Robust against processes or threads appearing/disappearing during an active scan

### Integration Context

The SMon feature integrates with three **platform-provided services** via required interfaces:

| External Service             | Role                                                                 |
|------------------------------|----------------------------------------------------------------------|
| **Central Error Aggregator** | Receives fault notifications when configured thresholds are breached |
| **Fault Memory (DTC Store)** | Receives DTC records for persistent fault logging                    |
| **Logging Backend**          | Receives structured metric snapshots and threshold warning messages  |

> ⚠️ SMon does **not** mandate a specific implementation of any of these services.
> They are integration points to be fulfilled by the platform adopter.

![SMon Combined Diagram](../../features/smon/_assets/combined_view.png)

### Anticipated Future Extensions

The following items are **out of scope** for this initial request but identified as natural
future extensions:

| Future Need                       | Description                                                                                           |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| **Additional metric sources**     | Network I/O (SOME/IP, DDS), Disk I/O, GPU utilization                                                 |
| **Threshold hysteresis**          | Sustained-breach detection over N cycles + lower watermark for alert clearing                         |
| **Live telemetry streaming**      | Real-time metric streaming over a network transport to visualization tools or IDE dashboards          |
| **Cross-platform unit testing**   | Verifying platform-specific monitor logic on a Linux host via OS-call mocking (no QNX target needed)  |

---

## Decision

- **Standardized Monitoring:** Eliminates duplicated and ad-hoc watchdog code across application teams by providing a shared, consistent middleware solution.
- **Cross-Platform Portability:** Decouples platform-specific drivers (Linux/QNX) from sensors and monitoring business logic, enabling reuse across ECU variants.
- **Platform Decoupling:** S-CORE remains independent of specific diagnostic, error aggregation, or logging backends through defined required interfaces.
- **Host-Based Verification:** Hardware-independent driver abstraction enables unit testing on host machines without physical hardware or target OS installations.
- **Implementation Scope:** Requires maintaining OS drivers for both Linux and QNX, defining runtime configuration parsing, and maintaining integration test harnesses.

---

## Consequences

S-CORE gains another feature that must be developed, integrated, deployed, tested, and maintained, including platform-specific support for Linux and QNX. It will also require a new Feature team.

---

## Alternatives Considered

no alternatives were identified at this point in time.

---

## Justification for the Decision

Introducing SMon as a middleware feature addresses the growing complexity of multi-application
Domain Controller ECUs. It centralizes resource observation, prevents silent resource exhaustion,
and standardizes fault escalation across different vehicle programs and operating systems,
fulfilling requirements from platform adopters Valeo and BMW.

---

## Related Links

- Feature request document: `docs/features/system_monitoring/index.rst`
- Feature requirements: `docs/features/system_monitoring/requirements/index.rst`
- Combined diagram: `docs/features/system_monitoring/_assets/combined_view.png`
- Tracking issue: <https://github.com/eclipse-score/score/issues/3340>
- Requested by: Valeo, BMW
