load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "department",
    srcs = ["department.cpp"],
    hdrs = ["includes/department.h"],
    includes = ["includes/"],
    linkstatic = True,
    visibility = ["//bazel/toolchains/samples/cpp/company:__pkg__"],
)
