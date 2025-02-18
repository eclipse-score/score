load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_test")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")

cc_binary(
    name = "example-app",
    srcs = ["main.cpp"],
    deps = ["//bazel/toolchains/samples/cpp/company"],
)

cc_test(
    name = "example-test",
    srcs = ["test.cpp"],
    deps = [
        "@googletest//:gtest",
        "@googletest//:gtest_main",
    ],
)

pkg_tar(
    name = "example-app-pkg",
    srcs = ["example-app"],
    visibility = ["//bazel/toolchains/samples/docker:__pkg__"],
)
