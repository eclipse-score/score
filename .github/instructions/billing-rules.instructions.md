---
description: Billing domain rules for the S-CORE customer billing service
---

# Billing Rules

Behavior rules for agents working on the customer billing service.

## Domain

- The billing service owns customer invoices, payment terms, and rating.
- Never modify invoice amounts directly; always go through the rating pipeline.
- All monetary values are handled as integer minor units (cents) with an explicit currency code.

## Conventions

- Follow the S-CORE metamodel for all normative artifacts.
- Keep billing state transitions traceable: every mutation must record the triggering event.
- Do not introduce new external dependencies without a design decision document.
