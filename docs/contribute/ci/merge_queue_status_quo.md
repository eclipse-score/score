<!-- ----------------------------------------------------------------------------
  Copyright (c) 2026 Contributors to the Eclipse Foundation

  See the NOTICE file(s) distributed with this work for additional
  information regarding copyright ownership.

  This program and the accompanying materials are made available under the
  terms of the Apache License Version 2.0 which is available at
  https://www.apache.org/licenses/LICENSE-2.0

  SPDX-License-Identifier: Apache-2.0
----------------------------------------------------------------------------- -->

# Merge queue status quo

This snapshot covers **48 active repositories** as of **2026-11-15**.
It includes repositories with at least one non-bot commit on their default branch in the preceding 30 days.
Source: [organization configuration](https://github.com/eclipse-score/.eclipsefdn/blob/a7ed6c57933c53fecf3c944c5ebcba16fb142d6c/otterdog/eclipse-score.jsonnet).

For configuration instructions, use the [how-to](merge_queues.md).
For the meaning and trade-offs of each feature, [compare alternatives](merge_queue_alternatives.md).

## Reading the table

Each row is an observed combination of the same features used in the alternatives.
Repositories with matching features are grouped; long groups are split into shorter rows for readability.

* **Early expensive checks** describes the selected expensive jobs. Other jobs may use different policies; **Not assessed** does not mean that no early checks exist.
* **Collector** and **Individual checks** describe the required-check mechanism, not proof that every intended job is covered.
* **None** means that no validation checks are required, regardless of queue or up-to-date settings.

## Repository configurations

| Repositories | Merge queue | Up-to-date requirement | Early expensive checks | Required validation checks |
| --- | --- | --- | --- | --- |
| `devcontainer`, `inc_someip_gateway` | Enabled | No | PR labels | Collector |
| `communication` | Enabled | No | Automatic internally; PR labels for forks | Individual checks |
| `baselibs`, `inc_ecu_model`, `logging`, `time`, `tooling` | Enabled | No | Automatic on every PR | Individual checks |
| `itf`, `qnx_unit_tests` | Enabled | No | Automatic internally; skipped for forks | Individual checks |
| `lifecycle` | Enabled | Yes | Automatic on every PR | Collector |
| `persistency` | Enabled | No | Not assessed | None |
| `kyron`, `reference_integration` | Disabled | Yes | Not assessed | None |
| `.github`, `bazel_cpp_toolchains`, `bazel_platforms`, `bazel_registry`, `bazel_registry_ui` | Disabled | No | Not assessed | None |
| `cicd-actions`, `cicd-workflows`, `config_management`, `contributor_training`, `coverage_tool` | Disabled | No | Not assessed | None |
| `dash-license-scan`, `dev_playground`, `docs-as-code`, `eclipse-score-website`, `eclipse-score-website-preview` | Disabled | No | Not assessed | None |
| `inc_diagnostics`, `inc_security_crypto`, `infrastructure`, `mcp-servers`, `module_template` | Disabled | No | Not assessed | None |
| `openssl`, `os_autosd`, `os_images`, `process_description`, `qnx_sdp` | Disabled | No | Not assessed | None |
| `qnx_sdp_pkg`, `rules_imagefs`, `sbom-tool`, `score`, `score-crates` | Disabled | No | Not assessed | None |
| `score_cpp_policies`, `score_rust_policies`, `testing_tools`, `tools` | Disabled | No | Not assessed | None |

## Known gaps

* `lifecycle`'s required collector does not include its separate QNX jobs.
* `time` has a QNX queue collector in its workflow, but that collector is not listed as a required check.
