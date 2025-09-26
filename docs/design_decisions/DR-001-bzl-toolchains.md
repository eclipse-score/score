# WIP: Draft for bazel_toolchains repository
```bash
bazel-toolchains/
├─ MODULE.bazel
├─ README.md
├─ extentions/
│  ├─ register.bzl              # module extension + public macros
│  └─ ...                       # whatever we need to set additionally to extensions.
├─ rules/
│  ├─ cc_config.bzl             # cc_common.create_cc_toolchain_config_info helpers
│  ├─ gcc_config.bzl            # GCC feature sets/action_configs by major
│  └─ llvm_config.bzl           # Clang/LLVM feature sets/action_configs by major
├─ overlays/
│  ├─ linux/
│  │  ├─ common.bzl             # linker, rpath, default sysroot resolution for Linux
│  │  ├─ aarch64.bzl            # linux aarch64 specific bits
│  │  └─ x86_64.bzl             # linux x86_64 specific bits
│  └─ qnx/
│     ├─ common.bzl             # QNX RTP specifics: qcc/q++, -V*, crt runtime, lib search
│     ├─ aarch64.bzl            # linux aarch64 specific bits
│     └─ x86_64.bzl             # linux x86_64 specific bits
├─ families/
│  ├─ gcc/
│  │  ├─ 12/
│  │  │  ├─ features.bzl
│  │  │  └─ toolchain.bzl       # produces cc_toolchain + config_info
│  │  ├─ 13/
│  │  │  ├─ features.bzl
│  │  │  └─ toolchain.bzl
│  │  └─ 14/
│  │     ├─ features.bzl
│  │     └─ toolchain.bzl
│  └─ llvm/
│     ├─ 17/
│     │  ├─ features.bzl
│     │  └─ toolchain.bzl
│     └─ 18/
│        ├─ features.bzl
│        └─ toolchain.bzl
├─ toolchains/                  # actual instances users reference
│  └─ cc/
│     ├─ gcc/
│     │  ├─ linux_x86_64/
│     │  │  ├─ 12/BUILD.bazel
│     │  │  ├─ 13/BUILD.bazel
│     │  │  └─ 14/BUILD.bazel
│     │  ├─ linux_aarch64/
│     │  │  ├─ 12/BUILD.bazel
│     │  │  ├─ 13/BUILD.bazel
│     │  │  └─ 14/BUILD.bazel
│     │  └─ qnx_aarch64/
│     │     └─ 12/BUILD.bazel
│     └─ llvm/
│        └─ linux_x86_64/
│           ├─ 17/BUILD.bazel
│           └─ 18/BUILD.bazel
├─ examples/
│  ├─ hello_cc/
│  └─ howto_register/
└─ tests/
   ├─ smoke/                    # compile/link hello, pthread, pic, shared
   ├─ headers/                  # builtin include dirs resolution checks
   └─ qnx/                      # qcc driver & -V profile sanity
```
