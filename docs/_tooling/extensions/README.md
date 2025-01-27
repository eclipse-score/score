# Decision Record: Why extensions?

Instead of setting global variables in conf.py which may be incorrect,
misspelled, have the wrong type etc., we can use extensions to setup sphinx,
sphinx-needs and other extensions.
This way we interact through a typesafe API and can be sure that the
configuration is correct.
