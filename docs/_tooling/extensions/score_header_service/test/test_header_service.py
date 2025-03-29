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
import os
from unittest.mock import ANY, MagicMock, patch
import score_header_service.header_service as hs
import pytest


@pytest.fixture(scope="session", autouse=True)
def add_metadata(record_testsuite_property):
    record_testsuite_property("Verifies", ["GD__automatic_document_header_generation"])
    record_testsuite_property(
        "Description", "It should check the generation of the header information."
    )
    record_testsuite_property("ASIL", "ASIL_D")
    record_testsuite_property("Priority", "1")
    record_testsuite_property("TestType", "Requirements-based test")
    record_testsuite_property("DerivationTechnique", "Analysis of requirements")


def test_register():
    mock_app = MagicMock()
    mock_env = MagicMock()
    mock_data = MagicMock()
    mock_service = MagicMock()
    mock_data.get_or_create_services.return_value = mock_service
    mock_env.app = mock_service
    mock_data.env = mock_env
    with patch(
        "score_header_service.header_service.SphinxNeedsData", return_value=mock_data
    ):
        hs.register(mock_app, mock_env, None)
        mock_service.register.assert_called_once_with("header-service", ANY)


@patch("random.randint")
def test_generate_hash(randint_mock):
    randint_mock.return_value = 42
    assert hs.generate_hash() == "73475cb4"


@patch("score_header_service.header_service.generate_hash")
@patch("score_header_service.header_service._extract_github_data")
@patch("sphinx.application.Sphinx")
def test_request_from_directive_github_data(
    mock_app, mock_extract_github_data, mock_generate_hash
):
    github_data = {
        "author": "John Doe",
        "approvers": "apover_1",
        "reviewers": "reviewer_1",
        "hash": "abcdef",
    }
    hash_value = "abcdef"
    need_data = {
        "type": "review_header",
        "title": "Service Title",
        "layout": "focus",
        "template": "header",
        "id": f"review__header__{hash_value}",
    }
    mock_extract_github_data.return_value = github_data
    mock_generate_hash.return_value = hash_value
    mock_directive = MagicMock()
    mock_directive.env.config.header_service_use_github_data = True
    header_service = hs.HeaderService(mock_app, "dummy-service", None)
    assert header_service.request_from_directive(mock_directive) == [
        need_data | github_data
    ]


@patch("score_header_service.header_service.generate_hash")
@patch("score_header_service.header_service._extract_merge_commit_data")
@patch("sphinx.application.Sphinx")
def test_request_from_directive_commit_data(
    mock_app, mock_extract_merge_commit_data, mock_generate_hash
):
    github_data = {
        "author": "John Doe",
        "approvers": "apover_1",
        "reviewers": "reviewer_1",
        "hash": "abcdef",
    }
    hash_value = "abcdef"
    need_data = {
        "type": "review_header",
        "title": "Service Title",
        "layout": "focus",
        "template": "header",
        "id": f"review__header__{hash_value}",
    }
    mock_directive = MagicMock()
    mock_directive.env.config.header_service_use_github_data = False
    mock_directive.env.docname = "file1.rst"
    mock_extract_merge_commit_data.return_value = github_data
    mock_generate_hash.return_value = hash_value
    header_service = hs.HeaderService(
        mock_app, "dummy-service", {"header_service_use_github_data": False}
    )
    assert header_service.request_from_directive(mock_directive) == [
        need_data | github_data
    ]
    mock_extract_merge_commit_data.assert_called_once_with("file1.rst")


@patch("score_header_service.header_service.HeaderService.request_from_directive")
@patch("sphinx.application.Sphinx")
def test_debug(mock_app, mock_request_from_directive):
    debug_data = [{"key": "value"}]
    mock_request_from_directive.return_value = debug_data
    header_service = hs.HeaderService(mock_app, "dummy-service", None)
    assert header_service.debug(None) == debug_data


@patch("score_header_service.header_service.subprocess.run")
def test_extract_merge_commit_data(run_mock):
    lines = """abcdef
John Doe
Approved: {approver1} ( {approver1@mail.com} ) on {2024-11-1}
Approved: {approver2} ( {approver2@mail.com} ) on {2024-11-2}
Reviewed: {reviewer1} ( {reviewer1@mail.com} ) on {2024-12-1}
Reviewed: {reviewer2} ( {reviewer2@mail.com} ) on {2024-12-2}
Reviewed: {reviewer3} ( {reviewer3@mail.com} ) on {2024-12-3}"""

    result_mock = MagicMock()
    result_mock.returncode = 0
    result_mock.stdout.decode.return_value = lines
    run_mock.return_value = result_mock

    assert hs._extract_merge_commit_data("/req/feature1") == {
        "author": "John Doe",
        "approver": ["approver1, approver1@mail.com", "approver2, approver2@mail.com"],
        "reviewer": [
            "reviewer1, reviewer1@mail.com",
            "reviewer2, reviewer2@mail.com",
            "reviewer3, reviewer3@mail.com",
        ],
        "hash": "abcdef",
    }
    run_mock.assert_called_once_with(
        [
            'git log --pretty="format:%H%n%an, %ae%n%b" --max-count=1 --merges --first-parent -p "/req/feature1'
        ],
        shell=True,
        capture_output=True,
    )


@patch("score_header_service.header_service.subprocess.run")
def test_extract_merge_commit_data_error(run_mock):
    result_mock = MagicMock()
    result_mock.returncode = 1
    run_mock.return_value = result_mock

    assert hs._extract_merge_commit_data("/req/feature1") == {
        "author": "N/A",
        "approver": "N/A",
        "reviewer": "N/A",
        "hash": "N/A",
    }


@patch("score_header_service.header_service._extract_approvers")
@patch("score_header_service.header_service._extract_reviewers")
@patch("score_header_service.header_service._extract_team_info")
@patch("score_header_service.header_service._extract_org")
@patch("score_header_service.header_service._extract_repo")
@patch("score_header_service.header_service._extract_pull_request")
@patch("score_header_service.header_service._extract_github_token")
@patch("score_header_service.header_service.Auth.Token")
@patch("score_header_service.header_service.Github")
def test_extract_github_data(
    mock_github,
    mock_auth_token,
    mock_extract_github_token,
    mock_extract_pull_request,
    mock_extract_repo,
    mock_extract_org,
    mock_extract_team_info,
    mock_extract_reviewers,
    mock_extract_approvers,
):
    mock_extract_github_token.return_value = "fake_token"
    mock_auth_token.return_value = "fake_token"
    mock_extract_org.return_value = "org"
    mock_extract_repo.return_value = "repo"
    mock_extract_pull_request.return_value = "123"
    mock_github_instance = MagicMock()
    mock_org = MagicMock()
    mock_repo = MagicMock()
    mock_pr = MagicMock()
    mock_repo.get_pull.return_value = mock_pr
    mock_pr.user.login = "author1"
    mock_pr.get_reviews.return_value = []
    mock_pr.merge_commit_sha = "abcdef"
    mock_github.return_value = mock_github_instance
    mock_github_instance.get_organization.return_value = mock_org
    mock_github_instance.get_repo.return_value = mock_repo
    mock_extract_approvers.return_value = "approver1"
    mock_extract_reviewers.return_value = "reviewer1; reviewer2"
    mock_extract_team_info.return_value = {"team1": "approver3"}

    data = hs._extract_github_data()
    assert data == {
        "author": "author1",
        "approvers": "approver1",
        "reviewers": "reviewer1; reviewer2",
        "hash": "abcdef",
    }


@patch("score_header_service.header_service.Auth.Token")
def test_extract_github_data_exception(mock_auth_token):
    mock_auth_token.side_effect = Exception("Error")
    assert hs._extract_github_data() == {
        "author": "N/A",
        "approvers": "N/A",
        "reviewers": "N/A",
        "hash": "N/A",
    }


def test_extract_org():
    with patch.dict(os.environ, {"GITHUB_REPOSITORY": "org/repo"}):
        assert hs._extract_org() == "org"


def test_extract_repo():
    with patch.dict(os.environ, {"GITHUB_REPOSITORY": "org/repo"}):
        assert hs._extract_repo() == "org/repo"


def test_extract_github_token():
    with patch.dict(os.environ, {"GH_TOKEN": "fake_token"}):
        assert hs._extract_github_token() == "fake_token"


def test_extract_pull_request():
    with patch.dict(os.environ, {"GITHUB_REF_NAME": "123/merge"}):
        assert hs._extract_pull_request() == "123"


def test_extract_team_info():
    mock_org = MagicMock()
    mock_team1 = MagicMock()
    mock_team2 = MagicMock()
    mock_member1 = MagicMock()
    mock_member2 = MagicMock()
    mock_member3 = MagicMock()
    mock_team1.name = "team1"
    mock_team1.id = 1
    mock_team2.name = "automotive-score-committers"
    mock_team2.id = 2
    mock_member1.login = "approver1"
    mock_member2.login = "approver2"
    mock_member3.login = "approver3"
    mock_team2.get_members.return_value = [mock_member1, mock_member3]
    mock_team1.get_members.return_value = [mock_member1, mock_member2]
    mock_org.get_teams.return_value = [mock_team1, mock_team2]
    mock_org.get_team.side_effect = lambda id: mock_team1 if id == 1 else mock_team2
    assert hs._extract_team_info(mock_org) == {
        "automotive-score-committers": ["approver1", "approver3"]
    }


@patch("score_header_service.header_service._append_approver_teams")
def test_extract_appprovers(mock_append_approver_teams):
    mock_review1 = MagicMock()
    mock_review2 = MagicMock()
    mock_review3 = MagicMock()
    mock_review1.state = "APPROVED"
    mock_review2.state = "APPROVED"
    mock_review3.state = "COMMENTED"
    mock_review1.user.login = "approver1"
    mock_review2.user.login = "approver2"
    mock_review3.user.login = "approver3"
    mock_append_approver_teams.return_value = ["approver1", "approver2"]
    assert (
        hs._extract_approvers(
            [mock_review1, mock_review2, mock_review3],
            {"team1": ["approver1", "approver2"]},
        )
        == "approver1; approver2"
    )


def test_append_approver_teams():
    approvers = ["approver1", "approver2"]
    team_info = {"team1": ["approver1"]}
    assert hs._append_approver_teams(approvers, team_info) == [
        "approver1 (team1)",
        "approver2",
    ]


def test_extract_reviewers():
    mock_review1 = MagicMock()
    mock_review2 = MagicMock()
    mock_review3 = MagicMock()
    mock_review1.state = "COMMENTED"
    mock_review2.state = "APPROVED"
    mock_review3.state = "CHANGES_REQUESTED"
    mock_review1.user.login = "reviewer1"
    mock_review2.user.login = "reviewer2"
    mock_review3.user.login = "reviewer3"
    assert (
        hs._extract_reviewers([mock_review1, mock_review2, mock_review3], "author1")
        == "reviewer1; reviewer3"
    )
