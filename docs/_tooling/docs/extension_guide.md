# Guide to Creating a Sphinx Extension

This document will help you with the most important building blocks and provide all information needed to start writing your own Sphinx extension in the Score project.   
**It is intended for developers, it will not show how to use extensions.**

## Getting Started

1. Create a new folder in `docs/_tooling/extensions` called `score_<name of your extension>`
2. Copy the template inside the `__init__.py`
3. Adapt to your needs

```python
from sphinx.application import Sphinx

def setup(app: Sphinx) -> dict:
    # attach to events, add config parameters, call functions etc.
    ...
    return {
        "version": "0.1",
        "parallel_read_safe": True,  # or False
        "parallel_write_safe": True,  # or False
    }
```

The `setup` function is vital as this is the one that Sphinx will call when loading your extension.   
From here you can attach to different events emitted by Sphinx or sphinx-needs, emit events yourself, 
or implement the logic needed for your extension to work.

## Attaching to an Event

Your extension might want to attach certain functions to events that Sphinx emits. This can be done like so:

```python
def setup(app: Sphinx) -> dict:
    app.connect("<event>", <function_to_execute>)
    ...
```

It's important to ensure that the function you are attaching to the event accepts the correct number of arguments in the right order.
Depending on the event you attach to, some information might not be available, or might be locked. 
Some events also expect a return value.

For more information, please see the related documentation:
- [Attaching function signature](https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.connect)
- [Build API events](https://www.sphinx-doc.org/en/master/extdev/event_callbacks.html#core-events-overview)  
- [sphinx-needs events](https://github.com/useblocks/sphinx-needs/blob/master/docs/contributing.rst#structure-of-the-extensions-logic)

## Adding a New Configuration Value

Adding new configuration values can be useful. This can be achieved with:

```python
def setup(app: Sphinx) -> dict:
    app.add_config_value("<config-name>", <default>, <rebuild>, <types>)
    ...
```

Each configuration value has an associated 'rebuild' value that determines what needs to be rebuilt if this value is changed.  
It must be one of these values:
- `'env'`: if a change in the setting only takes effect when a document is parsed - this means that the whole environment must be rebuilt.  
- `'html'`: if a change in the setting needs a full rebuild of HTML documents.  
- `''`: if a change in the setting will not need any special rebuild.  

More information is available in the [documentation here](https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_config_value).

## Adding Your Extension to Sphinx

Adding your extension to Sphinx is straightforward. Since all Python files are already 'discovered', you just need to add the extension inside `conf.py` to the extensions list:

```python
# conf.py
extensions = [
        #...
        "score_<name of your extension>",
]
```

> **Important:** There cannot be any BUILD file inside the entire 'extensions' folder, as that would break the Python imports.

## Testing

As we want to ensure code quality, testing is an integral part of the development process.
We perform testing with unit tests as well as integration tests that validate the full extension.

> Tests should cover both the happy path and edge cases.

### Where to Place Your Test Code

```
_tooling
ÃÄÄ extensions
³   ÃÄÄ README.md
³   ÃÄÄ score_draw_uml_funcs
³   ÃÄÄ YOUR_EXTENSION
³   ³   ÃÄÄ __init__.py  # your python code (setup needs to be in here)
³   ³   ÃÄÄ xyz.py       # your python code (if you need/want to split it across different files)
³   ³   ÀÄÄ tests
³   ³       ÃÄÄ test_xyz.py             # unit tests
³   ³       ÀÄÄ test_YOUR_EXTENSION.py  # integration tests
³   ÃÄÄ score_metamodel
³   ÀÄÄ score_plantuml.py
```

### Integration Tests

To enable integration tests, we make use of the Sphinx test app fixture provided in pytest by Sphinx itself.
The documentation for this is rather [sparse](https://www.sphinx-doc.org/en/master/extdev/testing.html#module-sphinx.testing),
so here are some starter code snippets and tips based on the integration testing of the source code linker.

#### What Do You Need?

To create a Sphinx testing app, you need the same components as a normal Sphinx app:
- RST file to build
- `conf.py` file
- Source, conf, and build directories

In addition, you can provide anything else that you might need to test your specific extension.

#### Building the Fixtures

Since we do not want to create permanent files, we will create a temporary directory via pytest fixtures.
This will give us the base temporary directory where we can then place all other files we may need to create.

```python
import pytest
from pathlib import Path
from sphinx_needs.data import SphinxNeedsData
from sphinx.testing.util import SphinxTestApp


@pytest.fixture(scope="session")  # the scope tells pytest to only execute this fixture once per test session
def sphinx_base_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("sphinx")  # you can name this whatever you want
```

Next, we need to set up the sphinx-test-app with all necessary arguments:

```python
@pytest.fixture(scope="session")
def sphinx_app_setup(sphinx_base_dir):
    def _create_app(conf_content, rst_content, requirements_text=None):
        src_dir = sphinx_base_dir / "src"
        src_dir.mkdir(exist_ok=True)
        
        # Here we write all the configuration, RST, and other files you may need.
        # These will be supplied via the fixture call later, so you can switch them out to test different scenarios.
        (src_dir / "conf.py").write_text(conf_content)
        (src_dir / "index.rst").write_text(rst_content)

        if requirements_text:
            (src_dir / "requirements.txt").write_text(json.dumps(requirements_text))

        app = SphinxTestApp(
            freshenv=True,
            srcdir=Path(src_dir),
            confdir=Path(src_dir),
            outdir=sphinx_base_dir / "out",
            buildername="html",
            warningiserror=True,
            # You can override configuration parameters as well.
            confoverrides={"requirement_links": str(src_dir / "requirements.txt")},

            # Other configuration params you may need
            # ...
        )

        return app

    return _create_app
```

Then we need the `conf.py`. Keep in mind that this `conf.py` knows nothing about the 'score' `conf.py`, and therefore you need to supply 
anything that you need in your test, like directives, extra options, and any other configuration that might not be standard.
*Remember to also add your extension into the extension list*

```python
@pytest.fixture(scope="session")
def basic_conf():
    return """
extensions = [
    "sphinx_needs",
    "score_source_code_linker",
]
needs_types = [
    dict(directive="test_req", title="Testing Requirement", prefix="TREQ_", color="#BFD8D2", style="node"),
]
needs_extra_options = ["source_code_link"]
needs_string_links = { 
    "source_code_linker": {
        "regex": r"(?P<value>[^,]+)",
        "link_url": "{{value}}",
        "link_name": "Source Code Link",
        "options": ["source_code_link"],
    },
}
"""
```

We are still missing an RST file we can render into the output HTML. This file can vary drastically depending on what you need to test.
It can be as simple as just having a title, or much more complex.
> Also pay attention that this is syntactically correct, as the test will fail if the RST can't be parsed by docutils.

```python
@pytest.fixture(scope="session")
def basic_needs():
    return """
TESTING SOURCE LINK 
===================
.. test_req:: TestReq1
   :id: TREQ_ID_1
   :status: valid
.. test_req:: TestReq2
   :id: TREQ_ID_2
   :status: open
"""
```

You can create many more fixtures if you need them. They are a great way to have something available for more than just one test,
or to organize your code better.

Now we need to bring it all together and build the test app:

```python
# Note: example_source_link_text_all_ok is left out to keep it a bit more brief, it's just a dict

# Defining our actual test here, with all arguments and fixtures
def test_source_link_integration_ok(
    sphinx_app_setup,
    basic_conf,
    basic_needs,
    example_source_link_text_all_ok,
    sphinx_base_dir,
):
    # Building the test app, supplying all needed arguments
    app = sphinx_app_setup(basic_conf, basic_needs, example_source_link_text_all_ok)
    try:
        app.build()
        # Now we have a fully functional sphinx-app, with built HTML documentation

        # Testing if the expectation equals reality
        Needs_Data = SphinxNeedsData(app.env)
        needs_data = {x["id"]: x for x in Needs_Data.get_needs_view().values()}
        assert "TREQ_ID_1" in needs_data
        assert "TREQ_ID_2" in needs_data
        assert (
            ",".join(example_source_link_text_all_ok["TREQ_ID_1"])
            == needs_data["TREQ_ID_1"]["source_code_link"]
        )
        assert (
            ",".join(example_source_link_text_all_ok["TREQ_ID_2"])
            == needs_data["TREQ_ID_2"]["source_code_link"]
        )
    finally:
        app.cleanup()  # Not strictly necessary as it's called internally, but it's cleaner to be explicit
```

You can also test the generated HTML content for correctness:

```python
    try:
        app.build()
        html_content = (app.outdir / "index.html").read_text() 
        assert "<td><p>John Doe</p></td>" in html_content
        assert '<div class="line">approver_1</div>' in html_content
        # ... other assertions 
```

### How to Add Tests to Bazel

Now that you have finished the tests, adding them to Bazel is straightforward. Inside `docs/BUILD`, add 
these two blocks (or more if necessary):

```starlark
py_library(
    name = "score_<YOUR_EXTENSION>",
    srcs = glob(["_tooling/extensions/<YOUR_EXTENSION>/**/*.py"]),
    imports = ["_tooling/extensions"],
    visibility = ["//visibility:public"],
)

score_py_pytest(
    name = "score_<YOUR_EXTENSION>_test",
    size = "small",  # small/medium/large
    srcs = glob(["_tooling/extensions/<YOUR_EXTENSION>/tests/**/*.py"]),
    visibility = ["//visibility:public"],
    deps = [":score_<YOUR_EXTENSION>", ":<OTHER_DEPENDENCIES>"],
)
```

If you want to exclude some files from being gathered, this is possible via the `exclude` keyword inside the glob:  
`srcs = glob(["ALL_FILES_TO_INCLUDE"], exclude = ["ALL_FILES_TO_EXCLUDE"]),`

You should now be able to run your tests: 
```
$ bazel test //docs:score_<YOUR_EXTENSION>_test
```

## Further Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/en)
- [Sphinx Needs Documentation](https://sphinx-needs.readthedocs.io/en/latest/)
- [Sphinx Tutorials](https://www.sphinx-doc.org/en/master/development/tutorials/index.html)  

Also look at already built extensions inside Score. They can be found in their respective folders:
- score_metamodel
- score_draw_uml_funcs
