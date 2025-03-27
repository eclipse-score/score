# Guide to Creating a Sphinx Extension

This document will help you with the most important building blocks and provide all information needed to start writing your own Sphinx extension in the S-CORE project.
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

```bash
_tooling/
├── extensions/
│   ├── README.md
│   ├── score_draw_uml_funcs/
│   ├── YOUR_EXTENSION/
│   │   ├── __init__.py  # your python code (setup needs to be in here)
│   │   ├── xyz.py       # your python code (if you need/want to split it across different files)
│   │   └── tests/
│   │       ├── test_xyz.py             # unit tests
│   │       └── test_YOUR_EXTENSION.py  # integration tests
├── score_metamodel/
├── score_plantuml.py
```



### Integration Tests

To enable integration tests, we make use of the Sphinx test app fixture provided in pytest by Sphinx itself.

#### What Do You Need?

To create a Sphinx testing app, you need the same components as a normal Sphinx app:
- RST file to build
- `conf.py` file
- Source, conf, and build directories
In addition, you can provide anything else that you might need to test your specific extension.


For examples on how to use and implement the sphinx testing app, you can check out the [source code linker](docs/_tooling/score_source_code_linker/tests)

Find everything related to testing within bazel and how to add your test suite to it, [see here](/tools/testing/pytest/README.md)

Also look at already built extensions inside S-CORE. They can be found in their respective folders:
- [score_metamodel](/docs/_tooling/extensions/score_metamodel/README.md)
- [score_draw_uml_funcs](/docs/_tooling/extensions/score_draw_uml_funcs/__init__.py)

## Further Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/en)
- [Sphinx Testing Fixture](https://www.sphinx-doc.org/en/master/extdev/testing.html#module-sphinx.testing)
- [Sphinx Needs Documentation](https://sphinx-needs.readthedocs.io/en/latest/)
- [Sphinx Tutorials](https://www.sphinx-doc.org/en/master/development/tutorials/index.html)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
