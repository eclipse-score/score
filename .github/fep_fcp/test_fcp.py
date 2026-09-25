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
    def __init__(
        self, number: int, labels: list[str], is_pr: bool = False, body: str = ""
    ):
        self.number = number
        self.body = body
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
        self.issue_events: list[SimpleNamespace] = []

    def get_issue_comments(self) -> list[FakeComment]:
        return self.issue_comments

    def create_issue_comment(self, body: str, author: str = BOT) -> FakeComment:
        comment = FakeComment(author, body, len(self.issue_comments))
        self.issue_comments.append(comment)
        return comment

    def get_reviews(self) -> list[SimpleNamespace]:
        return self.reviews

    def get_issue_events(self) -> list[SimpleNamespace]:
        return self.issue_events

    def review(self, login: str, state: str, at: datetime) -> int:
        review_id = 100 + len(self.reviews)
        self.reviews.append(
            SimpleNamespace(
                id=review_id,
                user=SimpleNamespace(login=login),
                state=state,
                submitted_at=at,
            )
        )
        return review_id

    def dismiss(self, review_id: int, by: str, at: datetime, message: str) -> None:
        next(r for r in self.reviews if r.id == review_id).state = "DISMISSED"
        self.issue_events.append(
            SimpleNamespace(
                event="review_dismissed",
                actor=SimpleNamespace(login=by),
                created_at=at,
                raw_data={
                    "dismissed_review": {
                        "state": "changes_requested",
                        "review_id": review_id,
                        "dismissal_message": message,
                    }
                },
            )
        )


class FakeRepo:
    def __init__(self, pr: FakePR):
        self.pr = pr
        self.issues = {
            42: FakeIssue(42, ["fep"], body="author: @someone\nshepherd: @Shepherd")
        }
        self.statuses: list[dict] = []

    def get_issue(self, number: int) -> FakeIssue:
        return self.issues[number]

    def get_commit(self, sha: str) -> SimpleNamespace:
        return SimpleNamespace(
            create_status=lambda **kw: self.statuses.append({"sha": sha, **kw})
        )


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
    chair_and_proxy=["chair"],
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
    return FakeRepo(pr)


# --------------------------------------------------------------------------- pure logic


def test_config_file_loads_groups_from_codeowners() -> None:
    cfg = fcp.Config.load()
    assert cfg.fcp_days == 14
    assert "qor-lb" in cfg.extra_stakeholders[cfg.quorum_group]
    assert cfg.chair_and_proxy == ["qor-lb", "arsibo"]


def test_codeowners_last_match_wins_and_teams_are_skipped() -> None:
    text = """
# /docs/features/  @commented-out
/docs/features/    @old
/docs/features/    @a @b  @org/team  # inline comment
/docs/features/x/  @other
"""
    assert fcp.codeowners(text, "/docs/features/") == ["a", "b"]
    with pytest.raises(ValueError, match="no entry for /missing/"):
        fcp.codeowners(text, "/missing/")


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


@pytest.mark.parametrize(
    ("delta", "text"),
    [
        (timedelta(days=14), "14 days"),
        (timedelta(days=1, hours=5), "1 day 5 hours"),
        (timedelta(hours=5, minutes=59), "5 hours"),
        (timedelta(minutes=61), "1 hour"),
        (timedelta(minutes=25), "25 minutes"),
        (timedelta(seconds=-5), "0 minutes"),
    ],
)
def test_duration(delta: timedelta, text: str) -> None:
    assert fcp._duration(delta) == text


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


def test_objection_dismissed_by_shepherd_does_not_block_and_is_recorded(
    pr: FakePR, repo: FakeRepo
) -> None:
    run(pr, repo, T0)
    review = pr.review("arch2", "CHANGES_REQUESTED", T0 + timedelta(days=3))
    pr.dismiss(review, "shepherd", T0 + timedelta(days=4), "not blocking")
    ledger = run(pr, repo, T0 + timedelta(days=15))
    assert ledger.state == "accepted"
    assert ledger.shepherds == ["Shepherd"]
    record = "arch2's objection dismissed by shepherd at 2026-10-05 06:00 UTC"
    assert record in pr.issue_comments[0].body
    assert record in pr.issue_comments[-1].body  # final record
    assert "still counts" not in pr.issue_comments[-1].body


def test_objection_dismissed_by_chair_does_not_block(
    pr: FakePR, repo: FakeRepo
) -> None:
    run(pr, repo, T0)
    review = pr.review("arch2", "CHANGES_REQUESTED", T0 + timedelta(days=3))
    pr.dismiss(review, "chair", T0 + timedelta(days=4), "ok")
    assert run(pr, repo, T0 + timedelta(days=15)).state == "accepted"


def test_objection_dismissed_by_other_committer_still_blocks(
    pr: FakePR, repo: FakeRepo
) -> None:
    run(pr, repo, T0)
    review = pr.review("arch2", "CHANGES_REQUESTED", T0 + timedelta(days=3))
    pr.dismiss(review, "committer", T0 + timedelta(days=4), "meh")
    assert run(pr, repo, T0 + timedelta(days=5)).state == "open"
    assert "1 blocking" in repo.statuses[-1]["description"]
    assert "still counts as blocking" in pr.issue_comments[0].body
    assert run(pr, repo, T0 + timedelta(days=15)).state == "rejected"


def test_dismissal_after_deadline_does_not_count(pr: FakePR, repo: FakeRepo) -> None:
    run(pr, repo, T0)
    review = pr.review("arch2", "CHANGES_REQUESTED", T0 + timedelta(days=3))
    # the closing run is late and the Shepherd dismisses after the deadline
    pr.dismiss(review, "shepherd", T0 + timedelta(days=14, hours=1), "too late")
    assert run(pr, repo, T0 + timedelta(days=14, hours=2)).state == "rejected"


def test_missing_shepherd_is_flagged(repo: FakeRepo) -> None:
    repo.issues[42].body = "author: @someone"
    pr = FakePR(["fep", "fep:fcp"])
    run(pr, repo, T0)
    assert "No Shepherd found in the tracking issue" in pr.issue_comments[0].body


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
    assert "6 days 23 hours left" in reminder
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


def test_reset_once_by_shepherd(pr: FakePR, repo: FakeRepo) -> None:
    run(pr, repo, T0)
    bot = fcp.Bot(repo, CFG, T0 + timedelta(days=5), fake_fetch)

    bot.command(pr, "committer", "/fcp reset")
    assert "only the Shepherd, chair or proxy" in pr.issue_comments[-1].body

    bot.command(pr, "shepherd", "/fcp reset\nrevised section 3")
    ledger = bot._sticky(pr)[1]
    assert ledger.resets == 1 and ledger.deadline == T0 + timedelta(days=19)
    assert "@base1" in pr.issue_comments[-1].body

    bot.command(pr, "shepherd", "/fcp reset")
    assert "no further reset" in pr.issue_comments[-1].body


def test_pull_request_lookup_for_fork_review_event() -> None:
    # pull_request_review from a fork: no PR number, head_repository is the base repo
    fork_pr = SimpleNamespace(number=3, head=SimpleNamespace(sha="abc", ref="proposal"))
    other = SimpleNamespace(number=2, head=SimpleNamespace(sha="def", ref="proposal"))
    repo = SimpleNamespace(get_pulls=lambda state: [other, fork_pr])
    env = {"HEAD_SHA": "abc", "HEAD_OWNER": "eclipse-score", "HEAD_BRANCH": "proposal"}
    assert fcp._pull_request(repo, env) is fork_pr
    assert (
        fcp._pull_request(repo, {"HEAD_SHA": "zzz", "HEAD_BRANCH": "proposal"}) is other
    )
    assert fcp._pull_request(repo, {"HEAD_SHA": "zzz", "HEAD_BRANCH": "nope"}) is None
