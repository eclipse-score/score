# *******************************************************************************
# Copyright (c) 2026 Contributors to the Eclipse Foundation
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

"""Unit tests of the FEP FCP bot, run with: python -m pytest .github/fep_fcp"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import pytest

import fcp

T0 = datetime(2026, 10, 1, 6, 0, tzinfo=timezone.utc)
BOT = "github-actions[bot]"


# --------------------------------------------------------------------------- fakes


class FakeComment:
    def __init__(self, author: str, body: str, number: int):
        self.user = SimpleNamespace(login=author)
        self.body = body
        self.html_url = (
            f"https://github.com/eclipse-score/score/pull/1#issuecomment-{number}"
        )

    def edit(self, body: str) -> None:
        self.body = body


class FakeIssue:
    def __init__(self, number: int, labels: list[str], is_pr: bool = False):
        self.number = number
        self.labels = [SimpleNamespace(name=n) for n in labels]
        self.pull_request = object() if is_pr else None
        self.comments: list[str] = []

    def add_to_labels(self, name: str) -> None:
        self.labels.append(SimpleNamespace(name=name))

    def remove_from_labels(self, name: str) -> None:
        self.labels = [label for label in self.labels if label.name != name]

    def create_comment(self, body: str) -> None:
        self.comments.append(body)


class FakePR(FakeIssue):
    def __init__(self, labels: list[str], body: str = "Tracking: #42"):
        super().__init__(1, labels, is_pr=True)
        self.body = body
        self.state = "open"
        self.head = SimpleNamespace(sha="abc123")
        self.issue_comments: list[FakeComment] = []
        self.reviews: list[SimpleNamespace] = []

    def get_issue_comments(self) -> list[FakeComment]:
        return self.issue_comments

    def create_issue_comment(self, body: str, author: str = BOT) -> FakeComment:
        comment = FakeComment(author, body, len(self.issue_comments))
        self.issue_comments.append(comment)
        return comment

    def get_reviews(self) -> list[SimpleNamespace]:
        return self.reviews

    def review(self, login: str, state: str, at: datetime) -> None:
        self.reviews.append(
            SimpleNamespace(
                user=SimpleNamespace(login=login), state=state, submitted_at=at
            )
        )


class FakeRepo:
    def __init__(self, pr: FakePR, permissions: dict[str, str] | None = None):
        self.pr = pr
        self.issues = {42: FakeIssue(42, ["fep"])}
        self.statuses: list[dict] = []
        self.permissions = permissions or {}

    def get_issue(self, number: int) -> FakeIssue:
        return self.issues[number]

    def get_commit(self, sha: str) -> SimpleNamespace:
        return SimpleNamespace(
            create_status=lambda **kw: self.statuses.append({"sha": sha, **kw})
        )

    def get_collaborator_permission(self, login: str) -> str:
        return self.permissions.get(login, "read")


CFG = fcp.Config(
    fep_label="fep",
    fcp_label="fep:fcp",
    breaking_change_label="fep:breaking-change",
    fcp_days=14,
    max_resets=1,
    reminder_days_before=[7, 2],
    breaking_change_quorum=2,
    quorum_group="Architecture Community",
    bot_login=BOT,
    known_good_url="known_good",
    known_good_groups=["target_sw"],
    extra_registry_modules=[],
    registry_metadata_url="registry/{module}",
    extra_stakeholders={"Architecture Community": ["arch1", "arch2", "arch3"]},
)


def fake_fetch(url: str) -> dict:
    return {
        "known_good": {
            "modules": {"target_sw": {"score_baselibs": {}, "score_logging": {}}}
        },
        "registry/score_baselibs": {
            "maintainers": [{"github": "base1"}, {"github": "base2"}]
        },
        "registry/score_logging": {"maintainers": [{"github": "log1"}]},
    }[url]


def run(pr: FakePR, repo: FakeRepo, now: datetime) -> fcp.Ledger:
    fcp.Bot(repo, CFG, now, fake_fetch).process(pr)
    return fcp.Bot(repo, CFG, now, fake_fetch)._sticky(pr)[1]


@pytest.fixture
def pr() -> FakePR:
    return FakePR(["fep", "fep:fcp"])


@pytest.fixture
def repo(pr: FakePR) -> FakeRepo:
    return FakeRepo(pr, {"shepherd": "write"})


# --------------------------------------------------------------------------- pure logic


def test_config_file_loads() -> None:
    cfg = fcp.Config.load()
    assert cfg.fcp_days == 14
    assert cfg.quorum_group in cfg.extra_stakeholders


def test_resolve_stakeholders_keeps_modules_without_maintainers() -> None:
    def fetch(url: str) -> dict:
        if url == "registry/score_logging":
            raise ValueError("broken json")
        return fake_fetch(url)

    assert fcp.resolve_stakeholders(CFG, fetch) == {
        "score_baselibs": ["base1", "base2"],
        "score_logging": [],
        "Architecture Community": ["arch1", "arch2", "arch3"],
    }


def test_ledger_round_trip() -> None:
    ledger = fcp.Ledger(
        "open", T0, T0 + timedelta(days=14), {"g": ["a"]}, reminders_sent=[7]
    )
    assert fcp.Ledger.from_body(f"text\n{ledger.to_marker()}\n") == ledger


def test_comment_review_does_not_override_approval_and_late_reviews_are_ignored() -> (
    None
):
    deadline = T0 + timedelta(days=14)
    reviews = [
        fcp.Review("Alice", "APPROVED", T0 + timedelta(days=1)),
        fcp.Review("alice", "COMMENTED", T0 + timedelta(days=2)),
        fcp.Review("bob", "APPROVED", T0 + timedelta(days=1)),
        fcp.Review("bob", "CHANGES_REQUESTED", deadline + timedelta(seconds=1)),
    ]
    latest = fcp.latest_decisive_reviews(reviews, deadline)
    assert {login: r.state for login, r in latest.items()} == {
        "alice": "APPROVED",
        "bob": "APPROVED",
    }


def test_due_reminder_sends_each_reminder_once() -> None:
    ledger = fcp.Ledger("open", T0, T0 + timedelta(days=14), {})
    assert fcp.due_reminder(ledger, T0 + timedelta(days=6), [7, 2]) is None
    assert fcp.due_reminder(ledger, T0 + timedelta(days=7), [7, 2]) == 7
    assert fcp.due_reminder(ledger, T0 + timedelta(days=8), [7, 2]) is None
    # a missed run catches up with the most urgent reminder only
    ledger.reminders_sent = []
    assert fcp.due_reminder(ledger, T0 + timedelta(days=13), [7, 2]) == 2
    assert fcp.due_reminder(ledger, T0 + timedelta(days=13), [7, 2]) is None


# --------------------------------------------------------------------------- bot


def test_non_fep_pr_gets_success_status(repo: FakeRepo) -> None:
    pr = FakePR([])
    fcp.Bot(repo, CFG, T0, fake_fetch).process(pr)
    assert repo.statuses[-1]["state"] == "success"
    assert pr.issue_comments == []


def test_fep_without_fcp_label_is_pending(repo: FakeRepo) -> None:
    pr = FakePR(["fep"])
    fcp.Bot(repo, CFG, T0, fake_fetch).process(pr)
    assert repo.statuses[-1]["state"] == "pending"
    assert pr.issue_comments == []


def test_start_notifies_stakeholders_and_mirrors_tracking_issue(
    pr: FakePR, repo: FakeRepo
) -> None:
    ledger = run(pr, repo, T0)
    assert ledger.state == "open"
    assert ledger.deadline == T0 + timedelta(days=14)
    assert ledger.tracking_issues == [42]
    body = pr.issue_comments[0].body
    for login in ("@base1", "@base2", "@log1", "@arch1"):
        assert login in body
    assert "fep:fcp" in {label.name for label in repo.issues[42].labels}
    assert repo.statuses[-1]["state"] == "pending"


def test_silence_is_approval_after_deadline(pr: FakePR, repo: FakeRepo) -> None:
    run(pr, repo, T0)
    pr.review("base1", "APPROVED", T0 + timedelta(days=3))
    ledger = run(pr, repo, T0 + timedelta(days=14, minutes=1))
    assert ledger.state == "accepted"
    assert repo.statuses[-1]["state"] == "success"
    assert "fep:fcp" not in {label.name for label in pr.labels}
    assert "fep:fcp" not in {label.name for label in repo.issues[42].labels}
    final = pr.issue_comments[-1].body
    assert (
        "ACCEPTED" in final
        and "Approved by silence: score_logging, Architecture Community" in final
    )


def test_blocking_objection_rejects_until_dismissed(pr: FakePR, repo: FakeRepo) -> None:
    run(pr, repo, T0)
    pr.review("arch2", "CHANGES_REQUESTED", T0 + timedelta(days=3))
    assert run(pr, repo, T0 + timedelta(days=4)).state == "open"
    assert "1 blocking" in repo.statuses[-1]["description"]
    assert run(pr, repo, T0 + timedelta(days=15)).state == "rejected"
    assert repo.statuses[-1]["state"] == "failure"


def test_dismissed_objection_does_not_block(pr: FakePR, repo: FakeRepo) -> None:
    run(pr, repo, T0)
    pr.review("arch2", "DISMISSED", T0 + timedelta(days=3))
    assert run(pr, repo, T0 + timedelta(days=15)).state == "accepted"


def test_objection_after_deadline_is_ignored(pr: FakePR, repo: FakeRepo) -> None:
    run(pr, repo, T0)
    pr.review("log1", "CHANGES_REQUESTED", T0 + timedelta(days=20))
    assert run(pr, repo, T0 + timedelta(days=21)).state == "accepted"


def test_non_stakeholder_objection_is_informational(pr: FakePR, repo: FakeRepo) -> None:
    run(pr, repo, T0)
    pr.review("drive-by", "CHANGES_REQUESTED", T0 + timedelta(days=1))
    assert run(pr, repo, T0 + timedelta(days=15)).state == "accepted"
    assert "drive-by" in pr.issue_comments[0].body


def test_breaking_change_needs_explicit_quorum(repo: FakeRepo) -> None:
    pr = FakePR(["fep", "fep:fcp", "fep:breaking-change"])
    run(pr, repo, T0)
    pr.review("arch1", "APPROVED", T0 + timedelta(days=1))
    assert run(pr, repo, T0 + timedelta(days=15)).state == "rejected"

    pr = FakePR(["fep", "fep:fcp", "fep:breaking-change"])
    run(pr, repo, T0)
    pr.review("arch1", "APPROVED", T0 + timedelta(days=1))
    pr.review("arch3", "APPROVED", T0 + timedelta(days=1))
    assert run(pr, repo, T0 + timedelta(days=15)).state == "accepted"


def test_reminder_mentions_only_silent_groups(pr: FakePR, repo: FakeRepo) -> None:
    run(pr, repo, T0)
    pr.review("base2", "APPROVED", T0 + timedelta(days=1))
    run(pr, repo, T0 + timedelta(days=7, hours=1))
    reminder = pr.issue_comments[-1].body
    assert "7 day(s) left" in reminder
    assert "@log1" in reminder and "@base1" not in reminder
    comments = len(pr.issue_comments)
    run(pr, repo, T0 + timedelta(days=8))
    assert len(pr.issue_comments) == comments


def test_removing_label_cancels_and_readding_restarts(
    pr: FakePR, repo: FakeRepo
) -> None:
    run(pr, repo, T0)
    pr.remove_from_labels("fep:fcp")
    assert run(pr, repo, T0 + timedelta(days=1)).state == "cancelled"
    pr.add_to_labels("fep:fcp")
    ledger = run(pr, repo, T0 + timedelta(days=2))
    assert ledger.state == "open" and ledger.start == T0 + timedelta(days=2)
    assert "Superseded" in pr.issue_comments[0].body


def test_fake_ledger_from_other_users_is_ignored(pr: FakePR, repo: FakeRepo) -> None:
    fake = fcp.Ledger("accepted", T0, T0, {}, closed_at=T0)
    pr.create_issue_comment(fake.to_marker(), author="mallory")
    assert run(pr, repo, T0).state == "open"


def test_reset_once_by_committer(pr: FakePR, repo: FakeRepo) -> None:
    run(pr, repo, T0)
    bot = fcp.Bot(repo, CFG, T0 + timedelta(days=5), fake_fetch)

    bot.command(pr, "random", "/fcp reset")
    assert "only committers" in pr.issue_comments[-1].body

    bot.command(pr, "shepherd", "/fcp reset\nrevised section 3")
    ledger = bot._sticky(pr)[1]
    assert ledger.resets == 1 and ledger.deadline == T0 + timedelta(days=19)
    assert "@base1" in pr.issue_comments[-1].body

    bot.command(pr, "shepherd", "/fcp reset")
    assert "no further reset" in pr.issue_comments[-1].body
