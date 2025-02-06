Decision Record: Where to Document
Documentation Structure
Guidance and Usage Instructions  guidance/*.rst
This is where we document how to use our tools.

Tool Architecture, Concepts, and Decision Records  README.md (next to the source code)

This follows the convention of placing a README.md in each directory.
It ensures easy discoverability and avoids burying critical information deep within documentation.
Additional .md files can be used as needed. Potentially in sub directories. Potentially in docs subdirectory.
Rendering to the Final Website
Both categories will be rendered via Sphinx. While detailed technical documentation (e.g., "how the tools work") may not be directly relevant to the website users, we still want to use our own tooling to assess usability firsthand within our team.

As a small compromise, we will evaluate using Markdown within the /docs/_tooling and /tools/ directories. See #156 for further details.

Participants: @AlexanderLanin @MaximilianSoerenPollak
