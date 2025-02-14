# One devcontainer?
In the main repository eclipse-score/score the focus is on documentation, therefore the devcontainer
is specifically tailored to that purpose. To simplify the setup, only one devcontainer is used,
for both documentation and development of documentation tooling.

In other eclipse-score repositories, the situation is different and either a combined devcontainer
or multiple devcontainers is more appropriate.

# Why is Python included?
Unfortunately multiple python related bazel targets rely on the system python installation.

`py_library` and `py_binary` targets are prominent examples, however they can trivially
be fixed by using `aspect_rules_py` instead of `rules_python`. Bug-report: https://github.com/bazelbuild/rules_python/issues/691


Others are not as easy to work around, e.g. `format.fix`.
