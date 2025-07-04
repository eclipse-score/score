# TRLC Renderer

`TRLC Renderer` helps to view requirements written in TRLC as ReStructuredText.
This way, it is possible to generate and HTML or PDF version of them, using Sphinx.

The `TRLC Renderer` can be used as follows

```
load("//tools/trlc_renderer:trlc_renderer.bzl", "trlc_renderer")
load("@trlc//:trlc.bzl", "trlc_requirements")

trlc_requirements(
    name = "some_requriement",
    srcs = ["some_requirement.trlc"],
    spec = [...],
)

trlc_renderer(
    name = "requirements",
    reqs = [":some_requirement"],
)

```

## Design

In general the `TRLC Renderer` is right now quite simple. It parses the TRLC files, using the TRLC Python library, then
creates a tree of requirements including the sections and then writes their headlines into a file.

In the future, this rendering needs to be requirement type specific, depending on the Sphinx PlugIng of TRLC (which is
not yet developed). At that point, the logic needs to be made more variable, thus that it is easily possible to
introduce new requirements types.
