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

"""FEP Final Comment Period (FCP) bot.

Drives Phase 2 of the FEP process (docs/contribute/contribution_request/feature_request.rst):

* When the ``fep:fcp`` label is added to a FEP PR, the stakeholders (module maintainers from the
  bazel registry plus the Architecture Community) are resolved, frozen in a ledger and notified
  with an @-mention. They are not added as reviewers.
* While the FCP is open, a sticky PR comment and the ``fep/fcp`` commit status show who approved,
  who objected (``Request changes``) and who has not responded yet. Reminders ping silent groups.
* When the deadline passes, silence counts as approval. Reviews submitted after the deadline are
  ignored. Undismissed change requests from stakeholders reject the FEP; Breaking Change FEPs
  additionally need an explicit quorum.

The ledger is stored as JSON in a hidden marker in the sticky comment, so the bot is stateless.
The script is started by .github/workflows/fep-fcp.yml.
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections.abc import Callable
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.request import urlopen

CONFIG_PATH = Path(__file__).with_name("config.json")
STATUS_CONTEXT = "fep/fcp"
LEDGER_RE = re.compile(r"<!-- fep-fcp-ledger (\{.*?\}) -->", re.DOTALL)
ISSUE_REF_RE = re.compile(
    r"(?:(?<![\w/])#|github\.com/eclipse-score/score/issues/)(\d+)\b"
)
SHEPHERD_RE = re.compile(r"^\s*shepherd:\s*@([\w-]+)", re.IGNORECASE | re.MULTILINE)
DECISIVE_STATES = ("APPROVED", "CHANGES_REQUESTED", "DISMISSED")


# --------------------------------------------------------------------------- configuration


@dataclass
class Config:
    fep_label: str
    fcp_label: str
    breaking_change_label: str
    fcp_days: int
    max_resets: int
    reminder_days_before: list[int]
    breaking_change_quorum: int
    quorum_group: str
    bot_login: str
    known_good_url: str
    known_good_groups: list[str]
    extra_registry_modules: list[str]
    registry_metadata_url: str
    # Groups and chair/proxy are either listed here directly, or taken from the
    # owners of a CODEOWNERS pattern (resolved by load()).
    extra_stakeholders: dict[str, list[str]] = field(default_factory=dict)
    chair_and_proxy: list[str] = field(default_factory=list)
    codeowners_file: str = ".github/CODEOWNERS"
    codeowners_stakeholders: dict[str, str] = field(default_factory=dict)
    chair_and_proxy_codeowners: str = ""

    @classmethod
    def load(cls, path: Path = CONFIG_PATH, repo_root: Path | None = None) -> Config:
        data = json.loads(path.read_text())
        data.pop("_comment", None)
        cfg = cls(**data)
        if cfg.codeowners_stakeholders or cfg.chair_and_proxy_codeowners:
            root = repo_root or path.resolve().parents[2]
            text = (root / cfg.codeowners_file).read_text()
            for group, pattern in cfg.codeowners_stakeholders.items():
                cfg.extra_stakeholders[group] = codeowners(text, pattern)
            if cfg.chair_and_proxy_codeowners:
                cfg.chair_and_proxy = codeowners(text, cfg.chair_and_proxy_codeowners)
        return cfg


def codeowners(text: str, pattern: str) -> list[str]:
    """Individual owners of ``pattern`` in a CODEOWNERS file (the last matching line wins).

    Teams (``@org/team``) are skipped: reviews are given by users, not by teams.
    """
    owners: list[str] | None = None
    for line in text.splitlines():
        tokens = line.split("#", 1)[0].split()
        if tokens and tokens[0] == pattern:
            owners = []
            for token in tokens[1:]:
                if token.startswith("@") and "/" not in token:
                    owners.append(token[1:])
                else:
                    print(
                        f"Warning: skipping CODEOWNERS entry {token} of {pattern}",
                        file=sys.stderr,
                    )
    if owners is None:
        raise ValueError(f"CODEOWNERS has no entry for {pattern}")
    return owners


# --------------------------------------------------------------------------- stakeholders


def fetch_json(url: str) -> Any:
    with urlopen(url, timeout=30) as response:
        return json.loads(response.read())


def resolve_stakeholders(
    cfg: Config, fetch: Callable[[str], Any] = fetch_json
) -> dict[str, list[str]]:
    """Map stakeholder group name -> GitHub logins, same sources as reference_integration."""
    known_good = fetch(cfg.known_good_url)
    modules: list[str] = []
    for group in cfg.known_good_groups:
        modules += list(known_good.get("modules", {}).get(group, {}))
    modules += cfg.extra_registry_modules

    stakeholders: dict[str, list[str]] = {}
    for module in dict.fromkeys(modules):
        try:
            metadata = fetch(cfg.registry_metadata_url.format(module=module))
        except (URLError, ValueError) as error:
            print(
                f"Warning: cannot read registry metadata of {module}: {error}",
                file=sys.stderr,
            )
            metadata = {}
        stakeholders[module] = [
            m["github"] for m in metadata.get("maintainers", []) if m.get("github")
        ]
    stakeholders.update(cfg.extra_stakeholders)
    return stakeholders


# --------------------------------------------------------------------------- ledger


def _fmt(moment: datetime) -> str:
    return moment.strftime("%Y-%m-%d %H:%M UTC")


def _duration(delta: timedelta) -> str:
    """Human readable duration: days and hours, or minutes below one hour."""

    def unit(count: int, name: str) -> str:
        return f"{count} {name}{'' if count == 1 else 's'}"

    seconds = max(int(delta.total_seconds()), 0)
    days, hours, minutes = (
        seconds // 86400,
        seconds % 86400 // 3600,
        seconds % 3600 // 60,
    )
    if days:
        return unit(days, "day") + (f" {unit(hours, 'hour')}" if hours else "")
    if hours:
        return unit(hours, "hour")
    return unit(minutes, "minute")


def _utc(moment: datetime) -> datetime:
    return moment if moment.tzinfo else moment.replace(tzinfo=timezone.utc)


@dataclass
class Ledger:
    state: str  # open | accepted | rejected | cancelled
    start: datetime
    deadline: datetime
    stakeholders: dict[str, list[str]]
    breaking: bool = False
    resets: int = 0
    reminders_sent: list[int] = field(default_factory=list)
    closed_at: datetime | None = None
    tracking_issues: list[int] = field(default_factory=list)
    shepherds: list[str] = field(default_factory=list)

    def to_marker(self) -> str:
        data = asdict(self)
        for key in ("start", "deadline", "closed_at"):
            data[key] = data[key].isoformat() if data[key] else None
        return f"<!-- fep-fcp-ledger {json.dumps(data, separators=(',', ':'))} -->"

    @classmethod
    def from_body(cls, body: str) -> Ledger | None:
        match = LEDGER_RE.search(body or "")
        if not match:
            return None
        data = json.loads(match.group(1))
        for key in ("start", "deadline", "closed_at"):
            data[key] = datetime.fromisoformat(data[key]) if data.get(key) else None
        return cls(**data)


# --------------------------------------------------------------------------- evaluation


@dataclass
class Review:
    login: str
    state: str
    submitted_at: datetime
    id: int = 0


@dataclass
class Dismissal:
    """A dismissed change request, as recorded in the PR timeline."""

    reviewer: str
    by: str
    at: datetime
    message: str
    honored: bool = False  # dismissed in time by the Shepherd, chair or proxy


def apply_dismissals(
    reviews: list[Review],
    events: list[tuple[int, str, datetime, str]],
    trusted: set[str],
    deadline: datetime,
) -> tuple[list[Review], list[Dismissal]]:
    """Only the Shepherd, chair or proxy may dismiss an objection, before the deadline.

    ``events`` are (review id, dismissed by, dismissed at, message) of dismissed change
    requests. Any other dismissal is not honored: the review counts as a change request again.
    """
    by_id = {e[0]: e for e in events}
    result: list[Review] = []
    dismissals: list[Dismissal] = []
    for review in reviews:
        event = by_id.get(review.id) if review.state == "DISMISSED" else None
        if event is None:
            result.append(review)
            continue
        _, by, at, message = event
        honored = by.lower() in trusted and at <= deadline
        dismissals.append(Dismissal(review.login, by, at, message, honored))
        result.append(
            review
            if honored
            else Review(
                review.login, "CHANGES_REQUESTED", review.submitted_at, review.id
            )
        )
    return result, dismissals


@dataclass
class GroupResult:
    name: str
    members: list[str]
    approved_by: list[str]
    blocked_by: list[str]

    @property
    def status(self) -> str:
        if self.blocked_by:
            return "blocking"
        if self.approved_by:
            return "approved"
        return "silent"


@dataclass
class Evaluation:
    groups: list[GroupResult]
    explicit_approvers: list[str]
    other_objections: list[str]  # change requests by people who are not stakeholders
    dismissals: list[Dismissal] = field(default_factory=list)

    @property
    def blocking(self) -> list[GroupResult]:
        return [g for g in self.groups if g.status == "blocking"]

    @property
    def silent(self) -> list[GroupResult]:
        return [g for g in self.groups if g.status == "silent"]

    @property
    def approved(self) -> list[GroupResult]:
        return [g for g in self.groups if g.status == "approved"]


def latest_decisive_reviews(
    reviews: list[Review], deadline: datetime
) -> dict[str, Review]:
    """Latest approval / change request / dismissal per user, submitted before the deadline.

    Plain comments do not change a user's decision, just as on GitHub.
    """
    latest: dict[str, Review] = {}
    for review in sorted(reviews, key=lambda r: r.submitted_at):
        if review.submitted_at > deadline or review.state not in DECISIVE_STATES:
            continue
        latest[review.login.lower()] = review
    return latest


def evaluate(
    ledger: Ledger,
    reviews: list[Review],
    quorum_group: str,
    dismissals: list[Dismissal] | None = None,
) -> Evaluation:
    latest = latest_decisive_reviews(reviews, ledger.deadline)
    groups = []
    stakeholder_logins: set[str] = set()
    for name, members in ledger.stakeholders.items():
        stakeholder_logins.update(m.lower() for m in members)
        decided = [(m, latest.get(m.lower())) for m in members]
        groups.append(
            GroupResult(
                name=name,
                members=members,
                approved_by=[m for m, r in decided if r and r.state == "APPROVED"],
                blocked_by=[
                    m for m, r in decided if r and r.state == "CHANGES_REQUESTED"
                ],
            )
        )
    quorum_members = {m.lower() for m in ledger.stakeholders.get(quorum_group, [])}
    return Evaluation(
        groups=groups,
        explicit_approvers=sorted(
            r.login
            for login, r in latest.items()
            if r.state == "APPROVED" and login in quorum_members
        ),
        other_objections=sorted(
            r.login
            for login, r in latest.items()
            if r.state == "CHANGES_REQUESTED" and login not in stakeholder_logins
        ),
        dismissals=dismissals or [],
    )


def closing_state(
    evaluation: Evaluation, ledger: Ledger, cfg: Config
) -> tuple[str, str]:
    """State and reason the FCP closes with once the deadline has passed."""
    if evaluation.blocking:
        names = ", ".join(g.name for g in evaluation.blocking)
        return "rejected", f"unresolved blocking objections ({names})"
    if (
        ledger.breaking
        and len(evaluation.explicit_approvers) < cfg.breaking_change_quorum
    ):
        return "rejected", (
            f"Breaking Change quorum not reached ({len(evaluation.explicit_approvers)}"
            f"/{cfg.breaking_change_quorum} explicit approvals from the {cfg.quorum_group})"
        )
    return "accepted", "no unresolved blocking objections"


def due_reminder(ledger: Ledger, now: datetime, days_before: list[int]) -> int | None:
    """Smallest reminder that is due and not sent yet; all due reminders are marked as sent."""
    if now >= ledger.deadline:
        return None
    due = [
        d
        for d in days_before
        if d not in ledger.reminders_sent and now >= ledger.deadline - timedelta(days=d)
    ]
    if not due:
        return None
    ledger.reminders_sent.extend(due)
    return min(due)


# --------------------------------------------------------------------------- rendering


def _mentions(logins: list[str]) -> str:
    return ", ".join(f"@{login}" for login in logins) or "_no maintainers registered_"


def _group_status(group: GroupResult, closed: bool) -> str:
    if group.status == "blocking":
        return f"🚫 changes requested by {', '.join(group.blocked_by)}"
    if group.status == "approved":
        return f"✅ approved by {', '.join(group.approved_by)}"
    return "☑️ approved by silence" if closed else "⏳ no response yet"


def _dismissal_lines(evaluation: Evaluation) -> list[str]:
    lines = []
    for d in evaluation.dismissals:
        text = f'{d.reviewer}\'s objection dismissed by {d.by} at {_fmt(d.at)}: "{d.message}"'
        if not d.honored:
            text = (
                f"⚠️ {text}. Not by the Shepherd, chair or proxy before the deadline, "
                "so it **still counts as blocking**."
            )
        lines.append(f"* {text}")
    return lines


def _roles_line(ledger: Ledger, cfg: Config) -> str:
    chair = ", ".join(cfg.chair_and_proxy) or "none configured"
    if ledger.shepherds:
        return f"Shepherd: {', '.join(ledger.shepherds)} · chair / proxy: {chair}"
    return (
        f"⚠️ No Shepherd found in the tracking issue (expected a line `shepherd: @login`); "
        f"only the chair / proxy ({chair}) can dismiss objections or reset the FCP."
    )


def render_sticky(
    ledger: Ledger, evaluation: Evaluation, cfg: Config, now: datetime, reason: str = ""
) -> str:
    closed = ledger.state != "open"
    headline = {
        "open": f"🟡 **Open**: closes **{_fmt(ledger.deadline)}** "
        f"({_duration(ledger.deadline - now)} left)",
        "accepted": f"✅ **Accepted**: FCP closed {_fmt(ledger.closed_at or now)}, {reason}",
        "rejected": f"🚫 **Rejected**: FCP closed {_fmt(ledger.closed_at or now)}, {reason}",
        "cancelled": f"⏹️ **Cancelled**: the `{cfg.fcp_label}` label was removed before the FCP closed",
    }[ledger.state]
    lines = [
        "## FEP Final Comment Period",
        "",
        headline,
        "",
        (
            f"The stakeholders below were notified on {_fmt(ledger.start)}. They have "
            f"{_duration(ledger.deadline - ledger.start)}, until **{_fmt(ledger.deadline)}**, "
            "to review this FEP:"
        ),
        "",
        "* **Approve** the PR if you agree, or leave it: **silence counts as approval** once the period ends.",
        (
            "* Submit a **Request changes** review for a substantive, technical objection. The Shepherd decides "
            "whether it is blocking and dismisses non-blocking ones; only dismissals by the Shepherd, "
            "chair or proxy count."
        ),
        "* Reviews submitted after the deadline are not taken into account.",
        "",
    ]
    if ledger.breaking:
        lines += [
            (
                f"⚠️ **Breaking Change FEP**: silence alone is not enough, {cfg.breaking_change_quorum} explicit "
                f"approvals from the {cfg.quorum_group} are required "
                f"(currently {len(evaluation.explicit_approvers)})."
            ),
            "",
        ]
    lines += ["| Stakeholder group | Members | Status |", "|---|---|---|"]
    lines += [
        f"| {g.name} | {_mentions(g.members)} | {_group_status(g, closed)} |"
        for g in evaluation.groups
    ]
    lines.append("")
    if evaluation.dismissals:
        lines += ["**Dismissed objections:**", "", *_dismissal_lines(evaluation), ""]
    if evaluation.other_objections:
        lines += [
            (
                f"ℹ️ Change requests from non-stakeholders (for the Shepherd to assess): "
                f"{', '.join(evaluation.other_objections)}"
            ),
            "",
        ]
    lines += [_roles_line(ledger, cfg), ""]
    if ledger.tracking_issues:
        lines.append(
            f"Tracking issue: {', '.join(f'#{n}' for n in ledger.tracking_issues)}"
        )
    else:
        lines.append(
            f"⚠️ No tracking issue labeled `{cfg.fep_label}` is referenced in the PR description."
        )
    if ledger.resets:
        lines.append(f"The FCP was reset {ledger.resets} time(s).")
    lines += ["", ledger.to_marker()]
    return "\n".join(lines)


def render_reminder(ledger: Ledger, evaluation: Evaluation, now: datetime) -> str:
    silent = [
        f"* {g.name}: {_mentions(g.members)}" for g in evaluation.silent if g.members
    ]
    return "\n".join(
        [
            (
                f"⏰ **FEP Final Comment Period: {_duration(ledger.deadline - now)} left** "
                f"(closes {_fmt(ledger.deadline)})."
            ),
            "",
            "No response yet from:",
            "",
            *silent,
            "",
            (
                "Silence counts as approval once the period ends. Objections raised after the deadline "
                "are not taken into account."
            ),
        ]
    )


def render_reset(ledger: Ledger, author: str) -> str:
    everyone = sorted(
        {m for members in ledger.stakeholders.values() for m in members}, key=str.lower
    )
    return "\n".join(
        [
            (
                f"🔁 **FEP Final Comment Period reset** by @{author}. The proposal was revised; "
                f"the new deadline is **{_fmt(ledger.deadline)}**."
            ),
            "",
            "Please review the updated proposal: " + _mentions(everyone),
        ]
    )


def render_final(ledger: Ledger, evaluation: Evaluation, reason: str) -> str:
    def names(groups: list[GroupResult]) -> str:
        return ", ".join(g.name for g in groups) or "none"

    return "\n".join(
        [
            f"🏁 **FEP Final Comment Period closed: {ledger.state.upper()}** ({reason}).",
            "",
            f"* Period: {_fmt(ledger.start)} to {_fmt(ledger.deadline)}",
            f"* Approved explicitly: {names(evaluation.approved)}",
            f"* Approved by silence: {names(evaluation.silent)}",
            f"* Blocking objections: {names(evaluation.blocking)}",
            *(
                [
                    "* Dismissed objections:",
                    *[f"  {x}" for x in _dismissal_lines(evaluation)],
                ]
                if evaluation.dismissals
                else []
            ),
            "",
            "All stakeholders listed in the FCP comment above were notified when the period started.",
        ]
    )


def _truncate(text: str, limit: int = 140) -> str:
    return text if len(text) <= limit else text[: limit - 1] + "…"


# --------------------------------------------------------------------------- GitHub


class Bot:
    def __init__(
        self,
        repo: Any,
        cfg: Config,
        now: datetime,
        fetch: Callable[[str], Any] = fetch_json,
    ):
        self.repo = repo
        self.cfg = cfg
        self.now = now
        self.fetch = fetch

    # -- helpers

    def _sticky(self, pr: Any) -> tuple[Any, Ledger | None]:
        # Only trust comments written by the bot itself, anybody could post a fake ledger.
        for comment in pr.get_issue_comments():
            if comment.user.login == self.cfg.bot_login:
                ledger = Ledger.from_body(comment.body)
                if ledger:
                    return comment, ledger
        return None, None

    def _reviews(self, pr: Any, ledger: Ledger) -> tuple[list[Review], list[Dismissal]]:
        reviews = [
            Review(r.user.login, r.state, _utc(r.submitted_at), r.id)
            for r in pr.get_reviews()
            if r.user is not None and r.submitted_at is not None
        ]
        events = []
        for event in pr.get_issue_events():
            dismissed = event.raw_data.get("dismissed_review") or {}
            if (
                event.event == "review_dismissed"
                and dismissed.get("state") == "changes_requested"
            ):
                events.append(
                    (
                        dismissed.get("review_id"),
                        event.actor.login if event.actor else "ghost",
                        _utc(event.created_at),
                        dismissed.get("dismissal_message") or "",
                    )
                )
        return apply_dismissals(reviews, events, self._trusted(ledger), ledger.deadline)

    def _evaluate(self, pr: Any, ledger: Ledger) -> Evaluation:
        reviews, dismissals = self._reviews(pr, ledger)
        return evaluate(ledger, reviews, self.cfg.quorum_group, dismissals)

    def _trusted(self, ledger: Ledger) -> set[str]:
        return {
            login.lower() for login in [*ledger.shepherds, *self.cfg.chair_and_proxy]
        }

    def _shepherds(self, issue_numbers: list[int]) -> list[str]:
        shepherds: list[str] = []
        for number in issue_numbers:
            body = self.repo.get_issue(number).body or ""
            shepherds += [s for s in SHEPHERD_RE.findall(body) if s not in shepherds]
        return shepherds

    def _status(
        self, sha: str, state: str, description: str, url: str | None = None
    ) -> None:
        kwargs = {"target_url": url} if url else {}
        self.repo.get_commit(sha).create_status(
            state=state,
            description=_truncate(description),
            context=STATUS_CONTEXT,
            **kwargs,
        )

    def _tracking_issues(self, pr: Any) -> list[Any]:
        issues = []
        for number in dict.fromkeys(
            int(n) for n in ISSUE_REF_RE.findall(pr.body or "")
        ):
            if number == pr.number or len(issues) >= 5:
                continue
            try:
                issue = self.repo.get_issue(number)
            except Exception as error:  # noqa: BLE001 - a dangling reference must not break the bot
                print(f"Warning: cannot read #{number}: {error}", file=sys.stderr)
                continue
            if issue.pull_request is None and self.cfg.fep_label in {
                label.name for label in issue.labels
            }:
                issues.append(issue)
        return issues

    def _publish(
        self,
        pr: Any,
        comment: Any,
        ledger: Ledger,
        evaluation: Evaluation,
        reason: str = "",
    ) -> Any:
        body = render_sticky(ledger, evaluation, self.cfg, self.now, reason)
        if comment is None:
            return pr.create_issue_comment(body)
        comment.edit(body)
        return comment

    def _remove_label(self, issue: Any) -> None:
        try:
            issue.remove_from_labels(self.cfg.fcp_label)
        except Exception as error:  # noqa: BLE001 - label may already be gone
            print(
                f"Info: could not remove {self.cfg.fcp_label} from #{issue.number}: {error}",
                file=sys.stderr,
            )

    # -- state machine

    def process(self, pr: Any) -> None:
        labels = {label.name for label in pr.labels}
        comment, ledger = self._sticky(pr)
        sha = pr.head.sha

        if self.cfg.fep_label not in labels and ledger is None:
            self._status(sha, "success", "Not an FEP")
            return
        if pr.state != "open":
            return

        in_fcp = self.cfg.fcp_label in labels
        if in_fcp and (ledger is None or ledger.state in ("cancelled", "rejected")):
            comment, ledger = self._start(pr, comment, labels)
        if ledger is None:
            self._status(
                sha,
                "pending",
                f"Final Comment Period not started (add the {self.cfg.fcp_label} label)",
            )
            return

        # The Shepherd may change during the FCP, read it from the tracking issue every time.
        if ledger.state == "open":
            ledger.shepherds = self._shepherds(ledger.tracking_issues)
        evaluation = self._evaluate(pr, ledger)
        reason = ""

        if ledger.state == "open" and not in_fcp:
            ledger.state = "cancelled"
            ledger.closed_at = self.now
        elif ledger.state == "open" and self.now >= ledger.deadline:
            ledger.state, reason = closing_state(evaluation, ledger, self.cfg)
            ledger.closed_at = self.now
            self._close(pr, ledger, evaluation, reason)
        elif ledger.state == "open":
            due = due_reminder(ledger, self.now, self.cfg.reminder_days_before)
            if due is not None and evaluation.silent:
                pr.create_issue_comment(render_reminder(ledger, evaluation, self.now))
        elif ledger.state in ("accepted", "rejected"):
            reason = closing_state(evaluation, ledger, self.cfg)[1]

        comment = self._publish(pr, comment, ledger, evaluation, reason)
        self._status(sha, *self._status_for(ledger, evaluation), comment.html_url)

    def _status_for(self, ledger: Ledger, evaluation: Evaluation) -> tuple[str, str]:
        if ledger.state == "accepted":
            return (
                "success",
                f"FEP accepted, FCP closed {_fmt(ledger.closed_at or ledger.deadline)}",
            )
        if ledger.state == "rejected":
            return "failure", "FEP rejected in the Final Comment Period"
        if ledger.state == "cancelled":
            return "pending", "Final Comment Period cancelled"
        return "pending", (
            f"FCP open until {_fmt(ledger.deadline)}: {len(evaluation.approved)}/{len(evaluation.groups)} approved, "
            f"{len(evaluation.blocking)} blocking, {len(evaluation.silent)} silent"
        )

    def _start(self, pr: Any, comment: Any, labels: set[str]) -> tuple[Any, Ledger]:
        tracking = self._tracking_issues(pr)
        ledger = Ledger(
            state="open",
            start=self.now,
            deadline=self.now + timedelta(days=self.cfg.fcp_days),
            stakeholders=resolve_stakeholders(self.cfg, self.fetch),
            breaking=self.cfg.breaking_change_label in labels,
            tracking_issues=[issue.number for issue in tracking],
            shepherds=self._shepherds([issue.number for issue in tracking]),
        )
        evaluation = self._evaluate(pr, ledger)
        # A new comment (not an edit) so that every stakeholder gets an @-mention notification.
        if comment is not None:
            comment.edit(
                comment.body.replace(
                    LEDGER_RE.search(comment.body).group(0), "_Superseded, see below._"
                )
            )
        comment = pr.create_issue_comment(
            render_sticky(ledger, evaluation, self.cfg, self.now)
        )
        for issue in tracking:
            issue.add_to_labels(self.cfg.fcp_label)
            issue.create_comment(
                f"FEP Final Comment Period started in #{pr.number}, closes **{_fmt(ledger.deadline)}**: "
                f"{comment.html_url}"
            )
        return comment, ledger

    def _close(
        self, pr: Any, ledger: Ledger, evaluation: Evaluation, reason: str
    ) -> None:
        pr.create_issue_comment(render_final(ledger, evaluation, reason))
        self._remove_label(pr)
        for number in ledger.tracking_issues:
            issue = self.repo.get_issue(number)
            self._remove_label(issue)
            issue.create_comment(
                f"FEP Final Comment Period in #{pr.number} closed: **{ledger.state}** ({reason}). "
                "Please update the status of this issue accordingly."
            )

    def command(self, pr: Any, author: str, body: str) -> None:
        if (body or "").strip().splitlines()[:1] != ["/fcp reset"]:
            return
        comment, ledger = self._sticky(pr)
        if ledger is None or ledger.state != "open":
            pr.create_issue_comment(
                f"@{author} there is no open Final Comment Period to reset."
            )
            return
        ledger.shepherds = self._shepherds(ledger.tracking_issues)
        if author.lower() not in self._trusted(ledger):
            pr.create_issue_comment(
                f"@{author} only the Shepherd, chair or proxy can reset the FCP."
            )
            return
        if ledger.resets >= self.cfg.max_resets:
            pr.create_issue_comment(
                f"@{author} the FCP was already reset {ledger.resets} time(s), no further reset."
            )
            return
        ledger.resets += 1
        ledger.start = self.now
        ledger.deadline = self.now + timedelta(days=self.cfg.fcp_days)
        ledger.reminders_sent = []
        pr.create_issue_comment(render_reset(ledger, author))
        evaluation = self._evaluate(pr, ledger)
        comment = self._publish(pr, comment, ledger, evaluation)
        self._status(
            pr.head.sha, *self._status_for(ledger, evaluation), comment.html_url
        )


# --------------------------------------------------------------------------- entry point


def _pull_request(repo: Any, env: dict[str, str]) -> Any | None:
    if env.get("PR_NUMBER"):
        return repo.get_pull(int(env["PR_NUMBER"]))
    # workflow_run payloads of fork PRs have no pull_requests[]. For pull_request_review
    # events head_repository is even the base repository, so owner:branch is not reliable
    # either: match the head commit first, the branch name only as a fallback.
    sha, branch = env.get("HEAD_SHA"), env.get("HEAD_BRANCH")
    open_prs = list(repo.get_pulls(state="open"))
    for pr in open_prs:
        if sha and pr.head.sha == sha:
            return pr
    for pr in open_prs:
        if branch and pr.head.ref == branch:
            return pr
    return None


def main() -> int:
    from github import (
        Auth,
        Github,
    )  # imported here so that the unit tests do not need PyGithub

    env = dict(os.environ)
    cfg = Config.load()
    repo = Github(auth=Auth.Token(env["GITHUB_TOKEN"])).get_repo(
        env["GITHUB_REPOSITORY"]
    )
    bot = Bot(repo, cfg, datetime.now(timezone.utc))
    event = env.get("EVENT_NAME", "")

    if event == "workflow_run" and env.get("RUN_EVENT") == "merge_group":
        # The FCP gate was already enforced on the PR before it entered the merge queue.
        bot._status(env["HEAD_SHA"], "success", "Checked on the pull request")
        return 0

    if event == "issue_comment":
        bot.command(
            repo.get_pull(int(env["PR_NUMBER"])),
            env["COMMENT_AUTHOR"],
            env.get("COMMENT_BODY", ""),
        )
        return 0

    if event == "workflow_run" or env.get("PR_NUMBER"):
        pr = _pull_request(repo, env)
        if pr is None:
            print("No pull request found for this event, nothing to do.")
            return 0
        bot.process(pr)
        return 0

    # schedule / workflow_dispatch without PR: close expired FCPs and send reminders
    for issue in repo.get_issues(state="open", labels=[cfg.fcp_label]):
        if issue.pull_request is not None:
            bot.process(repo.get_pull(issue.number))
    return 0


if __name__ == "__main__":
    sys.exit(main())
