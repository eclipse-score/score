# Automatic Header Generation Service

## Purpose
The service *header-service* generates a table with review and approver informations.
It uses the template *header.need* to generate this table.

## Extraction Methods
This modules can use two different methods to extract the needed information.
* GitHub data
* Merge commit log

The used method can be configured as a configuration parameter in *conf.py*.

    header_service_use_github_data = True

GitHub data is used if parameter is not set.


## Environment variables
This module uses the following environment variables if the extraction method **Github data** is configured:

GH_TOKEN: Github access token
GITHUB_REF_NAME: Github reference name (<pull request no>/merge)
GITHUB_REPOSITORY: Github repository <org>/<repo>

## Excecution
The document generation has to be executed as follows:

    GH_TOKEN=$GH_TOKEN bazel run //docs:incremental

Sphinx cannot acess the environment variables when started via bazel build.

If extraction method **Merge commit info** is used the document generation can be executed as follows:

    bazel run //docs:incremental


## Usage
Add the descriptor *header_service* to a RST file to fill out review and approver informations.

.. needservice:: header-service

This generates the following Table:

| Document Identification |                               |
| ----------------------- | ----------------------------- |
| Document Type           | Checklist                     |
| Document ID             | DPX-CONTR-REVIEW-CHECKLIST    |
| Project Name            | dependix                      |
| ASIL                    | B                             |
| Security Classification | CONFIDENTIAL                  |
| Author                  | [Author of the PR]            |
| Reviewer                | [List of PR reviewers]        |
| Approver                | [List of PR approvers]        |
| Version                 | [Merge commit hash of the PR] |
| Status                  | RELEASED                      |
