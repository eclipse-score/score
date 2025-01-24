# tools/feature_flags/feature_flags.bzl
load("@bazel_skylib//rules:common_settings.bzl", "bool_flag", "BuildSettingInfo")

OutputPathInfo = provider(fields = ["path"])

FEATURE_TAG_MAPPING = {
    "feature1": ["some-ip", "tag2"],
    "second-feature": ["test-feat", "tag6"],
}

def _feature_flag_translator_impl(ctx):
    output = ctx.actions.declare_file("feature_flags.txt")
    tags = []
    for flag, _ in ctx.attr.flags.items():
        if flag[BuildSettingInfo].value:
            flag_name = flag.label.name
            if flag_name in FEATURE_TAG_MAPPING:
                tags.extend(FEATURE_TAG_MAPPING[flag_name])
            else:
                tags.append(flag_name)
    
    content = ",".join(tags)
    ctx.actions.write(output = output, content = content)
    
    return [DefaultInfo(files = depset([output]))]

feature_flag_translator = rule(
    implementation = _feature_flag_translator_impl,
    attrs = {
        "flags": attr.label_keyed_string_dict(
            mandatory = True,
            providers = [BuildSettingInfo],
        ),
    },
)

def define_feature_flags(name):
    bool_flag(
        name = "feature1",
        build_setting_default = False,
    )
    bool_flag(
        name = "second-feature",
        build_setting_default = False,
    )
    
    feature_flag_translator(
        name = name,
        flags = {":feature1": "True", ":second-feature": "True"},
    )
