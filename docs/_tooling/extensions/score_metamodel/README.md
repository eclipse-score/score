# score_metamodel

This extension provides the metamodel and corresponding checks of the SCORE
project as a Sphinx extension.

See [../README](../README.md) for more information on why we use extensions.

## Naming

* check: A check is a function that checks compliance to a specific rule.
  (Note: sphinx-needs calls this a 'warning')
* Need-Local checks: checks which can be checked file-local, without a graph of
  other needs.
* Graph-Based checks: These warnings require a graph of all other needs to be
  checked.

## Creating new checks

In order to create a new check, you need to create a file in the `checks`
directory. It will be picked up automatically.
Then you need to write a local or graph based check function.
You need to use @local_check or @graph_check decorators to mark your function
accordingly.
Have a look at a simple example like `id_contains_feature`.

## Usage

Add score_metamodel to your extensions in `conf.py`:

```python
extensions = [
    ...
    'score_metamodel',
    ...
]
```

Make sure score_metamodel is installed in your environment or added to your
sys.path.


## Decision Record: split of need-local and graph-based checks

While sphinx-needs' own check/warning mechanism is very powerful, it only works
for need-local checks. This means, that it is not possible to warn about
graph-based issues like wrong links etc.

There are multiple ways to solve this issue, for example via
https://github.com/useblocks/sphinx-needs/pull/1248

However we chose to implement a custom warning mechanism, as we needed a
more elaborate solution for our use case anyway. Calling the checks ourselfes
seems to be the most flexible solution.

Technically local checks will be called with a single need, while graph-based
checks will be called with all needs.
