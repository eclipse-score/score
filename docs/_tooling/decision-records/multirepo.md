# Decision Record: Multi-Repository Documentation Setup in SCORE

## Problem Statement

The SCORE project manages stakeholder and feature requirements in the `/score`
repository (referred to as _platform_ hereafter). However, implementations and
implementation-specific requirements reside in separate repositories
(`/module-<xyz>`). These modules must link to the feature requirements they
implement. However, currently linking is only possible within a single
repository.

## Decision

**Status**: Open
**Solution**: 3. Uni-directional linking + Multiple platform websites

## Context: Repository Dependencies and Setup

SCORE is structured as a multi-repository project.

![Repo Setup](_assets/multirepo_setup.drawio.svg)

### **score (_platform_)**

- The `score` repository hosts process requirements, process tooling
  (docs-as-code), and feature requirements.
- It is unaware of individual modules, as they are implemented in separate
  repositories, potentially outside of SCORE.

### **module-\<xyz\>**

- Each `module-<xyz>` repository contains module-level requirements derived
  from feature requirements, along with the module implementation.
- Modules must link to feature requirements in the _platform_ repository.

### **reference_integration**

- The `reference_integration` repository integrates a specific version of the
  platform and all required modules.
- Other integrations may exist, using different versions of the platform and
  modules.

## Requirements

- Links must remain correct and functional over time, at least for all released
  versions.
- Dependencies between repositories should work with any version, not just
  released versions, ensuring quick iterations and feedback loops.

## Use Cases

1. **Building platform documentation**
   - Includes process requirements, feature requirements, and guidance.
2. **Building documentation for a single module**
   - Includes module requirements, implementation, test results, and platform
     coverage metrics.
3. **Building documentation for an integration**
   - Includes platform requirements, all module documents, integration test
     results, and coverage metrics.

## Constraints

- All repositories follow the same process (version) and tooling (version).
- Custom Sphinx templates are only considered if provided centrally.
- Data protection is not a concern as all content is open source under the same
  license.
- Requirements originating from integrations are out of scope.

## Previous Decisions

_Unfortunately those are not documented, therefore we cannot provide links to
any decision records._

- SCORE handles multiple repositories via Bazel.
- Requirements and links are implemented using `sphinx-needs`.
- Requirement-link versioning is managed through hashes.
- We have two different mechanisms for versioning. Current assumption is that
  we'll use bazel to pull other repositories in a specific version, while we
  never pull different versions of the same repository. So basically, we have
  the "classic multi repo setup" situation, as it's well known from e.g. git
  submodules.

## Bidirectional Linking Without Side Effects

"Bidirectional linking without side effects" means that the _platform_-website
remains unaffected by the modules while still linking to them. This
necessitates multiple versions of the platform-website.

This can be avoided by having a single platform-website that is either aware of
all module-websites with bi-directional links or by no modules at all
(uni-directional links from module-websites to platform-website).

### **Problems with multiple platform-websites**

- Maintaining multiple platform-websites results in different websites with
  identical content but different module links.
- Users must be cautious about which variant of the platform-website they view.

### **Benefits of multiple platform-websites**

- We don't need to have a platform-website hosted in hundreds of different
  versions, or artificially restrict ourselves to fewer versions when linking
  (e.g. only tagged versions). Each module can host any version of the
  platform-website.

#### **multiple platform-websites Model**

![Multiple Websites](_assets/multirepo_bidirectional.drawio.svg)

#### **single platform-website Model**

![Websites with Unidirectional
Links](_assets/multirepo_unidirectional.drawio.svg)

## Solutions

### **1. Bidirectional Linking Without Side Effects = Multiple platform websites**

Bazel imports other repositories. When building module or integration
documentation, everything is built in a single pass.

#### **Pros:**

- Versioning is fully managed by Bazel with minimal overhead, since it happens
  anyway for the source code.
- Supports untagged versions (any commit ID).

#### **Cons:**

- Heavy reliance on Bazel, potentially problematic for Esbonio and related
  tools.
- Performance issues, especially with Doxygen and test results, as everything
  is rebuilt each time.

#### **Approach 1: Single Website**

- Uses Bazel to import dependencies.
- By producing a unified website is achieved by generating the root `index`
  file dynamically.
- **Pro:** Shared navigation menu and search functionality.
- **Con:** No customization via `conf.py`, limiting module-specific templates.

#### **Approach 2: Separate Websites**

- Uses Bazel to import dependencies.
- Generates individual websites for each repository using the
  `sphinx-external-needs` three-step process (build, exchange JSON, rebuild).
- Generates a landing page linking to each website.
- **Con:** No shared navigation menu or search functionality.

### **2. Uni-directional Linking + Single platform website**

If we were to drop the bi-directional linking requirement, we could simplify
the setup significantly. The platform-website would not link to the modules,
but modules would link to the platform-website.

Bazel imports only `needs.json` from other repositories, or alternatively
fetches `needs.json` from published websites.

#### **Pros:**

- Fast and efficient documentation builds.

#### **Cons:**

- Versioning is managed at the website level, not by Bazel.
- Linking is limited to versioned tags of repositories.
- Requires keeping multiple website versions.

#### **Optimization:**

- Changes to the platform could trigger module builds which will validate
  whether the link hashes are still correct. This could be done by a CI job.



### **3. Uni-directional linking + Multiple platform websites**

Again we import the needs.json from the other repositories. But this time we
don't link to the original repository, but copy the pre-rendered website from
the gh-pages branch of that other repository. This way we can link to the
original website, but we don't have to build it ourselves. Versioning is now
fully handled by bazel, and not by providing multiple versions of the website.

In the far far future we could extend this solution with back-links. See
'further thoughts' at the end.

## Considered Alternatives

### **1. Needservice (Manual Approach)**

This is basically a manual approach to the problem. As long as any other
solution works, that would be preferrable.

### **2. Weblinks (Full URLs)**

We can simply link pages / needs in the other repositories by their full url.
While we can ensure that those links work, everything beyond that will become
problematic. Versioning might be solvable, but checking correct hashes
(versioning) is challenging. Other approaches are better suited for that.

Bidirectional links are not possible. As we'd like the same approach
everywhere, this is a **no-go**.


### **3. Needimport (Sphinx-Needs Extension)**

This is a sphinx-needs extension that allows to link to needs in other
repositories. The other repositories do NOT need to be available at build time.
Only their build output is required (needs.json).

Needs from the other repositories are imported, as if they were local. However
all structure is lost! All surrounding text, images etc are lost. Only the
needs themselfes are imported. This is a **no-go**.


### **4. Monorepo - No-Go**

- Violates SCORE’s fundamental design, which allows independent module
  development without modifying SCORE.

## Further Thoughts

If the platform dynamically generated back-links via JavaScript, a single
website could serve all modules using query parameters (e.g.,
`platform.html?module=module-xyz`). This approach could resolve usability
issues caused by having a single platform website and is a potential future
enhancement.

In case of multiple platform websites, we could use a different language like
Python to achieve the same result, without re-triggering Sphinx.
