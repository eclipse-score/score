# Decision Record: How to disabale requirements

## Context
[Feature Flags](https://eclipse-score.github.io/score/process/guidance/feature_flags/index.html#feature-flags) require the functionality
of disable or enabeling requirements based on which feature flags were provided, in order to build relevant documentation only.
This decision record will contain what implementation was choosen to enable this feature.

## Decision
Use the 'hide' option from sphinx-needs objects to remove/disable requirements.

## Chosen Solution: 'hide' Option
The 'hide' option was selected as the primary implementation method.

### Advantages
- Can be set programmatically with minimal complexity
- Maintains document structure integrity
- Provides clear control over element visibility
- Predictable behavior in programmatic contexts

### Negatives
- Requirements still appear in the rst via 'view source code' 
- Information only saved inside the `NeedsInfoType` objects

## Alternatives Considered

### Alternative 1: `:delete:` Option
**Why Not Chosen:**
- Lacks programmatic control capabilities. Can only be set hardcoded inside rst files  

More info: [Delete option docs](https://sphinx-needs.readthedocs.io/en/latest/directives/need.html#delete)

### Alternative 2: `del_need`  Method
**Why Not Chosen:**
- Introduces complexity in document node management
- Creates challenges in locating correct manipulation points
- Risk of document structure corruption during build
- Increases maintenance overhead due to complex node relationships  

More info: [del_need docs](https://sphinx-needs.readthedocs.io/en/latest/api.html#sphinx_needs.api.need.del_need)

### Alternative 3: `variations` Approach
**Why Not Chosen:**
- Filtering behavior appears inconsistent or non functional when used programmatically
- Requires hardcoding in configuration files for reliable operation  

More info: [variations docs](https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-variants)

