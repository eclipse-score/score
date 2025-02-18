load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "company",
    srcs = ["company.cpp"],
    hdrs = ["includes/company.h"],
    includes = ["includes/"],
    linkstatic = True,
    visibility = ["//bazel/toolchains/samples/cpp:__subpackages__"],
    deps = ["//bazel/toolchains/samples/cpp/department"],
)
