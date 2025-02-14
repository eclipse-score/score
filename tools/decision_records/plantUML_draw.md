# Use of PlantUML and Draw.IO in the Score Project

## Status

Accepted

## Context

The Score project requires a consistent and maintainable approach for creating and managing architectural and technical diagrams. The primary concerns driving this decision include:

- **Version Control:** The ability to store and manage diagrams as code to ensure traceability and history tracking.
- **Collaboration:** Allowing multiple contributors to edit and refine diagrams without requiring proprietary software.
- **Automation:** Supporting automated documentation generation.
- **Ease of Use:** Enabling contributors with varying levels of expertise to create and update diagrams efficiently.
- **Ease of Integration with Sphinx and Sphinx-Needs:** Ensuring diagrams can be seamlessly incorporated into documentation workflows using Sphinx and Sphinx-Needs.

The guidance document [docs-as-code](https://github.com/eclipse-score/score/blob/d96cd4ddf295fb949de5582519f7cc51fec8bf7b/docs/guidance/docs-as-code.rst) emphasizes the need for text-based documentation tools that integrate well with version control systems.

## Decision

We have chosen to use **PlantUML** and **Draw.IO** for diagramming in the Score project:

1. **PlantUML**: 
   - Supports "Diagrams as Code", allowing diagrams to be stored as text.
   - Easily integrates with documentation tools such as Sphinx and Markdown.
   - Can be version-controlled efficiently.
   - Enables automation for diagram generation in CI/CD pipelines.
   - Works well with **Sphinx and Sphinx-Needs**, allowing inline diagrams within documentation.

2. **Draw.IO**:
   - Provides an intuitive graphical interface for users who prefer WYSIWYG (What You See Is What You Get) editing.
   - Supports exporting diagrams in multiple formats, including SVG and PNG.
   - Can be stored in repositories as XML files, making version control feasible.
   - Can be used alongside Sphinx documentation by embedding exported diagrams.
   - Should only be chosen in cases where more complex diagrams cannot be rendered with PlantUML.
   
These tools complement each other, allowing users to choose between code-based and graphical approaches while ensuring compatibility with the documentation strategy.

## Consequences

- **Positive Impacts:**
  - Diagrams can be stored and managed within the Git repository alongside documentation.
  - Contributors can choose between textual and graphical diagram creation.
  - Enables automation in documentation pipelines.
  - Ensures long-term maintainability and accessibility of diagrams.
  - Seamless integration with **Sphinx and Sphinx-Needs**, improving documentation workflows.

- **Challenges:**
  - Requires contributors to be familiar with PlantUML syntax if they opt for code-based diagrams.

This decision aligns with the project's "Docs as Code" philosophy, ensuring maintainability, accessibility and effective collaboration.
