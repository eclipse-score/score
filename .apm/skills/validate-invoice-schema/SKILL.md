---
name: validate-invoice-schema
description: Validate customer invoice documents against the S-CORE billing schema. Use when creating, editing, or reviewing invoice JSON/YAML artifacts.
---

# Validate Invoice Schema

Validate invoice documents against the S-CORE billing schema.

## When to use

- Creating a new invoice artifact
- Editing an existing invoice document
- Reviewing a pull request that touches invoice schemas

## Procedure

1. Load the invoice document under review.
2. Check required fields: `invoiceId`, `customerId`, `currency`, `lines`, `total`.
3. Verify every line item has `sku`, `quantity` (positive integer), and `unitPrice` (integer minor units).
4. Verify `total` equals the sum of `quantity * unitPrice` across all lines.
5. Report any violations with the offending field path.
