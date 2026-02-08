<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-001-Arch: Consistent Stack vs. Reference Integration

- **Date:** 2026-02-07

```{dec_rec} Consistent Stack vs. Reference Integration
:id: dec_rec__arch__consistent_stack_vs_reference
:status: accepted
:context: Architecture
:decision: S-CORE as consistent stack
```

---

# Consistent Stack vs. Reference Integration

## Context

The project was initiated with ambiguous architectural assumptions. In some project material, S-CORE is described as a reference integration of independently evolving projects/modules. In parallel, discussions and expectations emerged that treat S-CORE as a coherent, continuously working stack.

This ambiguity creates friction in technical discussions, feature planning, and change justification. Contributors and committers currently lack a clear architectural baseline to decide whether modules, processes and tools are expected to optimize for individual evolution of modules or for the behavior of the overall stack.

This decision record clarifies the intended architectural role of S-CORE and establishes a foundation for subsequent technical and procedural decisions.

The scope of this decision applies to the entire S-CORE project, including all existing and future modules.

Two categories of modules must be distinguished:

1. Existing open-source projects/modules originating from other contexts and managed independently. These modules may be integrated into S-CORE if they are a good technical fit and align with S-CORE's functional goals. Their independent planning cadence and processes are explicitly acknowledged.
2. Modules that do not yet exist and are created specifically to fulfill the purpose of S-CORE within the S-CORE GitHub organization. These modules are directly affected by this architectural decision.

## Decision

S-CORE is defined as a **continuously consistent stack**.

The primary architectural goal of the project is the consistency and correctness of the full stack. All modules within S-CORE are expected to align with the objectives of the stack.

Modules created in the context of S-CORE exist to serve the stack. Their evolution is guided by stack-level use cases, not by module-local objectives in isolation.

Existing independently managed open-source projects/modules may be integrated where appropriate. Their independence is accepted, but their integration into S-CORE is evaluated and justified exclusively in terms of stack-level goals.

This decision is binding for the project. Any deviation requires a new, explicitly agreed Architecture Decision Record.

## Options Considered

### Option 1: Reference Integration of Independent Modules

Modules evolve independently, with their own roadmaps and priorities. Integration occurs late and primarily before releases. Coordination effort is concentrated at integration time. Modules effectively behave as separate projects that are assembled into a reference configuration.

This option favors module autonomy and minimizes continuous coordination. It shifts complexity to late integration phases and accepts reduced guarantees about the state of the full stack during development.

### Option 2: Consistent Stack as Leading Use Case

The stack is the primary architectural artifact. Modules contribute to and are validated against the behavior of the full stack. Continuous integration is used to ensure the stack remains functional throughout development.

This option increases coordination and change management overhead during development. In return, it establishes a clear architectural contract. Changes are evaluated based on their impact on the stack, and the reference stack is expected to remain usable.

## Consequences

The consistent stack model constrains module-level autonomy. Not all module-local use cases are valid by default. Changes, especially breaking changes, must be justified in terms of stack-level requirements.

The cost is increased coordination effort and earlier discussion of cross-cutting impacts. The benefit is architectural clarity and a shared basis for decision-making across teams.

Late integration risk is reduced. Architectural inconsistencies surface earlier, during development rather than at release time.

## Impact on Development Workflow

For modules created within S-CORE, development is guided by stack objectives. Features and changes are expected to consider their impact on the overall stack from the start.

Breaking changes in any module integrated into the stack require justification based on stack use cases. Module-specific arguments that do not align with stack objectives are insufficient.

This decision does not define concrete workflows, tooling, or CI/CD mechanisms. It establishes the architectural expectation that such mechanisms must support continuous stack consistency.

## Impact on Governance and Planning

Planning and prioritization discussions must reference stack-level goals. Module roadmaps are not authoritative on their own when they affect the behavior of the stack.

This decision enables future decision records to define how architectural alignment is reviewed, how changes are discussed, and how conflicts between module and stack objectives are resolved.

No specific governance structure or role model is defined by this record.

## Explicit Non-Goals

This decision record does not:

- Define concrete development processes or workflows.
- Specify CI/CD implementations or quality gates.
- Define release cadences or versioning strategies.
- Provide a migration plan for existing modules.
- Specify how architectural discussions are conducted or moderated.

These topics are expected to be addressed in follow-up decision records, using this decision as a shared architectural foundation.
