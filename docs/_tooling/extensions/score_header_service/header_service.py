# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************
import hashlib
import os
import random
import re
import subprocess
from collections import defaultdict
from typing import Any, ClassVar

from github import (
    Auth,
    Github,
    Organization,
    PaginatedList,
    PullRequestReview,
    Repository,
)
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util.docutils import SphinxDirective
from sphinx_needs.data import SphinxNeedsData
from sphinx_needs.services.base import BaseService

# req-traceability: GD__automatic_document_header_generation
APPROVER_TEAMS = ["automotive-score-committers"]


# def setup(app: Sphinx) -> dict[str, str | bool]:
#     """Register the header service with the Sphinx application.

#     :param app: The Sphinx application instance.
#     """
#     app.connect("env-before-read-docs", register)
#     return {
#         "version": "0.1",
#         "parallel_read_safe": True,
#         "parallel_write_safe": True,
#     }


def register(app: Sphinx, env: BuildEnvironment, _: str | None) -> None:
    """Register the HeaderService with the Sphinx application environment.

    :param app: The Sphinx application instance.
    :param env: The Sphinx build environment.
    :param _: Additional argument not used.
    """
    app.add_config_value("header_service_use_github_data", True, "env")
    data = SphinxNeedsData(env)
    services = data.get_or_create_services()
    services.register("header-service", HeaderService)


def generate_hash() -> str:
    """Generate a random SHA-256 hash.

    :return: A string representing the first 8 characters of the hash.
    """
    random_input = str(random.randint(0, 100000000000)).encode()
    return hashlib.sha256(random_input).hexdigest()[:8]


class HeaderService(BaseService):
    options = {}

    def __init__(
        self,
        app: Sphinx,
        name: str,
        config: dict[str, Any] | None,
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialize the HeaderService.

        :param app: The Sphinx application instance.
        :param name: The name of the service.
        :param config: The configuration dictionary.
        :param kwargs: Additional keyword arguments.
        """
        super(BaseService, self).__init__()

    def request_from_directive(
        self, directive: SphinxDirective
    ) -> list[dict[str, str | list[str]]]:
        """
        Processes a directive and returns the need data.

        :param directive: The directive instance.
        :return: A list containing the need data dictionary.
        """
        need_data: dict[str, str | list[str]] = {
            "type": "review_header",
            "title": "Service Title",
            "layout": "focus",
            "template": "header",
            "id": f"review__header__{generate_hash()}",
        }

        review_data: dict[str, str | list[str]] = (
            _extract_github_data()
            if directive.env.config.header_service_use_github_data
            else _extract_merge_commit_data(directive.env.docname)
        )
        need_data.update(review_data)
        return [need_data]

    def debug(self, directive: SphinxDirective) -> list[dict[str, str | list[str]]]:
        """
        Return debug data for the given options.

        :param options: The options dictionary.
        :return: A list containing the debug data dictionary.
        """
        debug_data: list[dict[str, str | list[str]]] = self.request_from_directive(
            directive
        )
        return debug_data


def _extract_merge_commit_data(location: str) -> dict[str, str | list[str]]:
    """Extract data from the merge commit log.

    :param location: The location of the merge commit.
    :return: A dictionary containing the extracted data.
    """
    default_data: dict[str, str | list[str]] = {
        "author": "N/A",
        "approver": "N/A",
        "reviewer": "N/A",
        "hash": "N/A",
    }

    git_cmd = f'git log --pretty="format:%H%n%an, %ae%n%b" --max-count=1 --merges --first-parent -p "{location}'

    result = subprocess.run([git_cmd], shell=True, capture_output=True)

    if result.returncode:
        print(f"Error during git call {git_cmd}\n{result.stderr.decode()}")
        return default_data

    out = result.stdout.decode()
    lines = out.split("\n")

    hash = lines[0]
    author = lines[1]

    data: defaultdict[str, list[str]] = defaultdict(list)

    pattern = r"(Approved|Reviewed): \{(.*)} \( \{(.*)\} \) on \{(.*)\}"

    for m in re.finditer(pattern, out, re.MULTILINE):
        data[m.group(1)].append(", ".join(m.group(2, 3)))

    commit_data: dict[str, str | list[str]] = {
        "author": author,
        "approver": data.get("Approved", "N/A"),
        "reviewer": data.get("Reviewed", "N/A"),
        "hash": hash,
    }
    return commit_data


def _extract_github_data() -> dict[str, str | list[str]]:
    """Retrieve data from GitHub and returns it as a dictionary.

    :return: A dictionary containing the GitHub data.
    """
    empty_data: dict[str, str | list[str]] = {
        "author": "N/A",
        "approvers": "N/A",
        "reviewers": "N/A",
        "hash": "N/A",
    }

    github: Github | None = None

    try:
        auth = Auth.Token(_extract_github_token())
        github = Github(auth=auth)
        org: Organization.Organization = github.get_organization(_extract_org())
        repo: Repository.Repository = github.get_repo(_extract_repo())
        pr = repo.get_pull(int(_extract_pull_request()))
        reviews = pr.get_reviews()
        author = pr.user.login
        data: dict[str, str | list[str]] = {
            "author": author,
            "approvers": _extract_approvers(reviews, _extract_team_info(org)),
            "reviewers": _extract_reviewers(reviews, author),
            "hash": pr.merge_commit_sha,
        }
    except Exception as ex:
        print(f"Unable to extract Github information\n{ex}")
        data = empty_data
    finally:
        if github:
            github.close()
    return data


def _extract_org() -> str:
    """Retrieve the organization from the GITHUB_REPOSITORY environment variable.

    :return: The organization name.
    """
    return os.environ["GITHUB_REPOSITORY"].split("/")[0]


def _extract_repo() -> str:
    """Retrieve the repository from the GITHUB_REPOSITORY environment variable.

    :return: The repository name.
    """
    return os.environ["GITHUB_REPOSITORY"]


def _extract_github_token() -> str:
    """Retrieve the GitHub token from the GH_TOKEN environment variable.

    :return: The GitHub token.
    """
    return os.environ["GH_TOKEN"]


def _extract_pull_request() -> str:
    """Retrieve the pull request number from the GITHUB_REF_NAME environment variable.

    :return: The pull request number.
    """
    return os.environ["GITHUB_REF_NAME"].split("/")[0]


def _extract_approvers(
    reviews: PaginatedList.PaginatedList[PullRequestReview.PullRequestReview],
    team_info: dict[str, list[str]],
) -> str:
    """Retrieve a list of all approvers of the pull request.

    :param reviews: The list of reviews.
    :param team_info: The team information dictionary.
    :return: A string containing the approvers.
    """
    approvers_set: set[str] = {
        review.user.login for review in reviews if review.state == "APPROVED"
    }
    approvers_list: list[str] = _append_approver_teams(list(approvers_set), team_info)
    return "; ".join(sorted(approvers_list))


def _extract_team_info(org: Organization.Organization) -> dict[str, list[str]]:
    """Retrieve all members of the approver teams and stores them in a dictionary.

    :param org: The GitHub organization instance.
    :return: A dictionary containing the team information.
    """
    team_info: dict[str, list[str]] = {
        t.name: [m.login for m in org.get_team(t.id).get_members()]
        for t in org.get_teams()
        if t.name in APPROVER_TEAMS
    }
    return team_info


def _append_approver_teams(
    approvers: list[str], team_info: dict[str, list[str]]
) -> list[str]:
    """Add approver teams to the user names.

    :param approvers: The list of approvers.
    :param team_info: The team information dictionary.
    :return: A list of approvers with their teams.
    """
    approvers_with_teams: list[str] = []

    for approver in approvers:
        teams = [name for name, members in team_info.items() if approver in members]
        approver_with_teams = (
            approver + " (" + ", ".join(teams) + ")" if teams else approver
        )
        approvers_with_teams.append(approver_with_teams)

    return approvers_with_teams


def _extract_reviewers(
    reviews: PaginatedList.PaginatedList[PullRequestReview.PullRequestReview],
    author: str,
) -> str:
    """Retrieve a list of all reviewers excluding the author of the pull request.

    :param reviews: The list of reviews.
    :param author: The author of the pull request.
    :return: A string containing the reviewers.
    """
    reviewer = {
        review.user.login
        for review in reviews
        if review.state in ["COMMENTED", "CHANGES_REQUESTED", "DISMISSED"]
        and review.user.login != author
    }
    return "; ".join(sorted(reviewer))
