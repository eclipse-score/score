# VSO Assets

This folder contains visual assets for the Vehicle Service Orchestrator (VSO) feature documentation.


## Architecture Diagrams

### VSO_architecture.svg
**Used in:** [docs/features/vso/index.rst](../index.rst) - System Architecture section

Main architecture diagram showing the Multi-node Scenario Evidence Layer:
- **Data Inputs Layer:** Per-node signals from Runtime Plane, Diagnostics Module, and Platform Resources (purple boxes)
- **VSO Core Modules:** Scenario Management, State Manager, Evidence Aggregation, Scenario Evidence Violation, Response Management (orange/yellow boxes)
- **Output Layer:** OEM State Manager / Safety Manager integration and S-CORE Lifecycle handoff (green boxes)

Key principle: VSO observes and generates evidence but does NOT execute or decide.

### VSO_component_relationship.svg
**Used in:** [docs/features/vso/index.rst](../index.rst) - Integration with S-CORE Components section

Diagram showing the clear separation of concerns between:
- **S-CORE Diagnostics / OpenSOVD** (blue) - raw signals, fault lifecycle
- **VSO** (orange) - evidence generation, pipeline monitoring
- **OEM State Manager / Safety Manager** (green) - decision-making
- **S-CORE Lifecycle** (purple) - execution

### VSO_evidence_state_matrix.svg
**Used in:** [docs/features/vso/index.rst](../index.rst) - Evidence State Response Matrix section

Visual representation of the Evidence State Response Matrix showing six evidence states:
- **OK** (green): Normal execution, no action
- **WATCH** (yellow): Light monitoring, minor deviations
- **WARN** (orange): Focused debugging (30s), pre-snapshot, dashboard warning
- **VIOLATED** (red): Intensive diagnostics (60s), snapshot freeze, critical alert
- **INCOMPLETE** (purple): Missing signals, low confidence evidence
- **RECOVERED** (blue): Return to normal, recovery package archived
