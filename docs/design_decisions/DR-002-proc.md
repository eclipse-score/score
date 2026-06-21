# DR-002-Proc: Feature & Enhancement Proposal (FEP) Process

- **Date:** 2026-06-19
- **Audience:** S-CORE Architecture Community

```{dec_rec} Feature & Enhancement Proposal (FEP) Process
:id: dec_rec__proc__fep_process
:status: accepted
:context: Informal feature request handling no longer scales: proposals are not differentiated by importance, the Architecture Community has an unbounded review obligation, and cross-Feature-Team alignment has no defined governance path.
:decision: Adopt a FEP process requiring a mandatory Shepherd and a binding 10-day Final Comment Period for platform-level and cross-Feature-Team decisions, while Feature Teams retain full authority within their own domain.
```

---

## Context / Problem

S-CORE's feature request process was designed for a smaller, co-located community where architectural alignment happened naturally through face-to-face discussion. That model no longer holds. Three related problems have emerged as the project and contributor base grew:

**Scale and diversity of feature requests.** The broader scope of the project brings more feature requests from more contributors with more varied backgrounds. Some proposals are architecturally significant and urgent — they are not being handled in time. Others have no genuine community backing and consume the same process overhead as the important ones. The current process does not differentiate.

**An unsustainable obligation on the Architecture Community.** The implicit expectation is that the Architecture Community responds promptly to every feature request. At current scale this is physically impossible. Architecture Community members are spread thin across low-priority proposals while high-priority ones queue. There is also no mechanism to signal that a proposal simply does not have enough interest to proceed — every idea, however early-stage, enters the same process.

**No governance path for cross-Feature-Team alignment.** When a decision requires agreement across Feature Team boundaries — a shared interface, a protocol choice, a breaking change to a shared component — there is currently no defined process. These decisions either stall, get made unilaterally, or consume Architecture Community time informally without a structured outcome. Without a consistent governance path for cross-cutting decisions, a consistent and operationally coherent stack cannot be maintained.

---

## Decision

Adopt a **Feature & Enhancement Proposal (FEP) process** with the following principles:

**Maximize Feature Team autonomy.** Feature Teams have full authority over decisions within their own domain. No FEP is required for changes that a single Feature Team owns end-to-end with no cross-cutting impact. The FEP process is not a central approval gate for all changes — it is the governance mechanism for decisions that cannot or should not be made unilaterally.

**FEP required for platform-level changes and cross-Feature-Team alignment.** A FEP is required when a change introduces new platform-level functionality, modifies stable interfaces, has breaking impact on existing integrators, or requires agreement across Feature Team boundaries. The FEP process applies equally to externally visible features and to internal cross-cutting decisions.

**Two structural mechanisms not present in the current process:**

1. A **Shepherd** — an Architecture Community member (not the author) who agrees to guide the proposal to maturity and endorses its entry into formal review. The responsibility to find a Shepherd rests entirely with the author. If no Shepherd can be found, that is itself a signal: the proposal does not have sufficient community backing to proceed. The Architecture Community is not obligated to shepherd every idea.

2. A **Final Comment Period (FCP)** — a time-bounded (14 calendar days), binding review window. Architecture Community members are expected to engage during FCP. Silence at the end of FCP counts as approval. This gives the community a defined, bounded obligation and makes the default outcome "proceed" rather than "wait."

**Architecture Community membership includes Feature Team leads.** Feature Team leads participate in FCP for proposals that cross into or affect their domain, have standing to raise blocking objections, and — critically — their silence during an FCP that affects their Feature Team counts as approval. This is the mechanism by which cross-FT alignment is achieved: structured, time-bounded, with a clear default.

**FEPs are Decision Records.** The FEP template is a superset of the DR template. FEPs are DRs that arrive through a defined governance process rather than being recorded informally. When a FEP completes FCP, it is accepted in-place as a DR in the appropriate category (`Arch`, `Proc`, `Strat`, etc.) with a matching identifier. This DR is itself the first example: a Process FEP filed as `DR-002-Proc`.

The process specification follows in the next section.

---

## Process Specification

### What Requires a FEP?

A FEP is required when a change cannot be decided by a single Feature Team alone — because it has platform-level impact, modifies stable interfaces, introduces breaking changes, or requires alignment across Feature Team boundaries. Changes that a Feature Team owns end-to-end with no cross-cutting impact do not require a FEP. When in doubt, a short Phase 0 post to the architecture channel clarifies the path.

---

### FEP Types

| Type | Use when |
|---|---|
| **Feature** | Proposing new functionality not currently in S-CORE |
| **Enhancement** | Extending or improving existing functionality within established architecture |
| **Breaking Change** | Any change that breaks backwards compatibility for existing integrators — higher bar |
| **Process** | Proposing changes to S-CORE's development or governance process |
| **Informational** | Documenting design decisions, constraints, or rationale without proposing a change |

---

### Roles

**Author** — the person proposing the change. Responsible for writing and maintaining the FEP, integrating feedback, and driving consensus. The author is not the Shepherd.

**Shepherd** — an Architecture Community member (not the author) who guides the FEP through the process. The Shepherd's job:
- Helps the author understand what the proposal needs to cover
- Reviews drafts for completeness and soundness before formal review
- Decides when the proposal is mature enough to enter FCP — this is the key gatekeeping function
- Does **not** make the final accept/reject decision (to preserve objectivity)

Finding a Shepherd is the author's responsibility. If no Architecture Community member is willing to shepherd a proposal, the idea does not proceed.

**Architecture Community** — all architects and Feature Team leads with standing to review FEPs. Includes Feature Team leads, who participate in FCP for proposals affecting their domain. During FCP, every Architecture Community member is expected to either raise a substantive objection or approve (explicitly or by silence). Silence at end of FCP counts as approval.

---

### The Process: Five Phases

```
[0] Idea Exploration  →  [1] Draft + Shepherd  →  [2] FCP  →  [3] Decision  →  [4] Implementation Tracking
```

**Phase 0 — Idea Exploration** *(informal, no status)*

Post the idea informally in the S-CORE architecture channel before writing anything formal. The goal is to surface obvious problems early, find similar prior proposals, and identify whether a Shepherd might be willing to pick this up. A good Phase 0 post answers: what problem does this solve, why can't it be solved with what we have, and what is the rough shape of the solution. Move to Phase 1 when you have a willing Shepherd.

**Phase 1 — Draft + Shepherd Shaping** *(status: `Draft`)*

The author finds a Shepherd and files the FEP as a PR. A FEP in draft (no Shepherd confirmed yet) does not require a GitHub issue. Once a Shepherd is confirmed, a tracking issue is opened to follow the FEP through to implementation. The FEP references this issue via the `:tracking:` field; the issue links back to the FEP PR, giving bidirectional traceability. Author and Shepherd iterate until the proposal is complete and well-argued. When the Shepherd judges it ready, they signal readiness for FCP. The Architecture Community chair (or proxy) then announces the FCP to the full community. If a proposal is going nowhere, the Shepherd advises the author to withdraw rather than let it drag indefinitely.

**Phase 2 — Final Comment Period (FCP)** *(status: `Under Review`)*

Once announced, the Architecture Community has 10 calendar days to engage. Objections must be substantive and technical — the Shepherd distinguishes blocking from non-blocking feedback. The Shepherd can reset the FCP once if a significant new issue requires a revised proposal.

FCP closes with no unresolved blocking objections → accepted. FCP closes with unresolved blocking objections → rejected. Technical Lead escalation may intervene in exceptional cases, but this is not the default path.

Silence is approval. Architecture Community members who do not engage during FCP cannot subsequently block implementation.

**Phase 3 — Decision** *(status: `Accepted` | `Rejected` | `Withdrawn`)*

FCP closed cleanly → the FEP is accepted as a Decision Record. FCP closed with unresolved blocking objections → rejected. The author may withdraw at any point before acceptance.

Breaking Change FEPs additionally require explicit approval from a minimum quorum of Architecture Community members — they cannot pass by silence alone.

**Phase 4 — Implementation Tracking** *(status: `Implementing` → `Implemented`)*

When a FEP is accepted its PR is merged and the DR is recorded. The tracking issue remains open and becomes the implementation tracking artifact. It is closed only when the implementation — not the FEP — is merged. Implementing teams link their work items to the tracking issue. If implementation reveals the accepted design is materially wrong, a follow-up FEP must be filed rather than diverging silently.

---

### FEP Template

````markdown
# DR-NNN-<Category>: <Short imperative title>

- **Date:** YYYY-MM-DD

```{dec_rec} <Short imperative title>
:id: dec_rec__<arch|proc|strat|infra|int>__<slug>
:status: draft
:tracking: <GitHub issue URL — required once a Shepherd is confirmed>
:context: <One sentence: what situation or gap makes this proposal necessary?>
:decision: <One sentence: what is being proposed?>
```

---

## Context / Problem
<!-- What problem does this solve? Why is the current state insufficient?
     Include evidence: user requests, integration pain points, gaps vs. roadmap. -->

## Decision
<!-- What is being proposed, precisely? What changes, what is added, what is removed?
     For API changes: before/after interface definitions.
     For architectural changes: updated component model or sequence diagrams. -->

## Backwards Compatibility
<!-- Who is affected? What is the migration path? Is a deprecation period required?
     Remove this section if there is no breaking change. -->

## Alternatives Considered
<!-- What other approaches did you evaluate and why were they rejected? -->

## Rationale
<!-- Why this approach over the alternatives? What constraints or requirements drove the design? -->

## Consequences
<!-- What changes after acceptance? What must be implemented, updated, or tracked?
     Enumerate affected work products and downstream documents. -->

## Rejected Ideas
<!-- Ideas raised during FCP that were explicitly not adopted, with rationale.
     Remove if empty. -->
````

---

### Breaking Change FEPs — Additional Requirements

A proposal classified as **Breaking Change** must additionally include:

- **Impact Inventory**: explicit list of known integrators, configurations, or customer deliverables that will break
- **Migration Path**: concrete steps integrators must take, with estimated effort
- **Deprecation Timeline**: if a grace period is offered, how long and how the old behavior is signaled as deprecated
- **Sign-off from Affected Teams**: acknowledgment (not necessarily approval) from leads of teams known to be directly affected before FCP entry

---

## Rationale

**Why shift Shepherd responsibility to the author?** The Architecture Community's attention is the scarce resource. Making the author responsible for finding a Shepherd ensures a proposal only consumes Architecture Community capacity when at least one community member judges it worth their time. Ideas without community interest do not proceed.

**Why a binding FCP with silence-as-approval?** The current process has no forcing function and no defined default. A time-bounded FCP with silence-as-approval respects reviewer time, establishes a clear deadline, and removes indefinite passive blocking as a strategy. The 10-day FCP follows the Rust RFC process, which uses the same mechanism for the same reasons.

**Why include Feature Team leads in the Architecture Community?** Cross-FT alignment only works if the people accountable for each affected domain have standing in the decision process. Their silence during an FCP affecting their domain counts as approval — this is what makes the FCP binding for cross-cutting decisions.

**Why maximize Feature Team autonomy?** The FEP process should be the exception, not the rule. Feature Teams are closest to their domain and should make most decisions without Architecture Community involvement. Central governance that reaches too far creates bottlenecks and disempowers the teams doing the work.

**Why are FEPs DRs?** The DR format is already established and trusted in the community. FEPs are DRs that arrive through a defined governance process rather than informally. The FEP process gives DRs a defined front door: propose, shape, get community consensus, then record. Existing DRs reached informally remain valid.

**References and prior art:** This process definition was inspired by [Python PEP process](https://peps.python.org/pep-0001/), [Kubernetes KEP process](https://github.com/kubernetes/enhancements/tree/master/keps/sig-architecture/0000-kep-process) & [Rust RFC process](https://github.com/rust-lang/rfcs/blob/master/README.md).

---

## Consequences

### Effective on acceptance

- The Architecture Community formally owns the governance of platform-level FEPs and cross-Feature-Team alignment decisions.
- The Architecture Community is **not** obligated to engage with every feature request — only with those that have found a Shepherd and entered FCP.
- The Technical Lead circle's role in feature request handling changes to: triage incoming FRs (Platform/cross-FT → FEP process; single-FT → Feature Team). TLs are notified when a FEP enters FCP for roadmap awareness but do not gate the architectural decision.
- Accepted FEPs are Decision Records — filed in the appropriate DR category in the score repository.

### Implementation (tracked as issues after acceptance)

The following documents require update. None block acceptance of this DR — changes are tracked as GitHub issues linked to this DR after acceptance: [[DR-002-Proc] Implement FEP process](https://github.com/eclipse-score/score/issues/3061)

| Document | Change |
|---|---|
| [Feature Request Guideline](https://eclipse-score.github.io/score/main/contribute/contribution_request/feature_request.html) | Add routing decision at entry; platform/cross-FT FRs → FEP process, single-FT FRs → FT authority |
| [Project Management Plan](https://eclipse-score.github.io/score/main/platform_management_plan/project_management.html) | Correct formal error: PMP assigns FR review to TL circle; update to reflect Architecture Community ownership for platform/cross-FT FRs, TL role → triage |
| [Change Management Plan](https://eclipse-score.github.io/score/main/platform_management_plan/change_management.html) | Add two-tier taxonomy; map FEP acceptance to existing Change Request status flow |
| [Software Architecture Overview](https://eclipse-score.github.io/score/main/users_guide/project_basics/software_architecture_overview.html) | Update reference to FEP process for structural/platform-level changes |
| [Process Description — Change Management](https://eclipse-score.github.io/process_description/main/process_areas/change_management/index.html) | No change required; FEP Shepherd + FCP implements `wf__change_analyze_cr` for platform-level FRs |
