<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright (c) 2026 Contributors to the Eclipse Foundation -->

# Write Stage Artifact

## Workflow

1. Call `check_stage_completeness` for the stage about to begin.
2. Call `write_stage_artifact` with the issue ID, artifact type, title, content, and traceability links.
3. Use the returned path as the durable review target.
4. Keep implementation evidence under the same issue's `harness/` directory.

The writer chooses the required numbered filename and adds the SPDX and traceability metadata.