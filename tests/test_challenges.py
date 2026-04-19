"""Pytest tests for Week 7: Moonlight Festival Control Booth."""

import pytest

from src.challenges import (
    order_festival_alerts,
    order_festival_alerts_stable,
    peek_next_festival_alert,
    top_k_festival_alerts,
)


# -----------------------------
# order_festival_alerts
# -----------------------------

def test_order_festival_alerts_normal_case() -> None:
    alerts = [
        (2, "Food court power issue"),
        (1, "Main Stage microphone failed"),
        (3, "Lost umbrella report"),
    ]

    result = order_festival_alerts(alerts)

    assert result == [
        "Main Stage microphone failed",
        "Food court power issue",
        "Lost umbrella report",
    ]


def test_order_festival_alerts_empty_input() -> None:
    assert order_festival_alerts([]) == []


def test_order_festival_alerts_one_alert() -> None:
    alerts = [(1, "Storm warning")]
    assert order_festival_alerts(alerts) == ["Storm warning"]


def test_order_festival_alerts_duplicate_priorities() -> None:
    alerts = [
        (2, "Lighting check"),
        (2, "Backstage cleanup"),
        (1, "Security call"),
    ]

    result = order_festival_alerts(alerts)

    # First must be highest priority
    assert result[0] == "Security call"

    # Remaining can be in any order, but must match exactly
    assert sorted(result[1:]) == sorted(["Lighting check", "Backstage cleanup"])


def test_order_festival_alerts_large_input_consistency() -> None:
    alerts = [(i % 3 + 1, f"Alert {i}") for i in range(100)]

    result = order_festival_alerts(alerts)

    # Ensure result length matches input
    assert len(result) == len(alerts)

    # Ensure smallest priority appears first
    first_priority = min(p for p, _ in alerts)
    assert any(title for p, title in alerts if p == first_priority and title == result[0])


# -----------------------------
# order_festival_alerts_stable
# -----------------------------

def test_order_festival_alerts_stable_normal_case() -> None:
    alerts = [
        (2, "Food truck restock"),
        (1, "North Gate security call"),
        (3, "Lost hat report"),
    ]

    assert order_festival_alerts_stable(alerts) == [
        "North Gate security call",
        "Food truck restock",
        "Lost hat report",
    ]


def test_order_festival_alerts_stable_keeps_input_order_for_ties() -> None:
    alerts = [
        (1, "A"),
        (1, "B"),
        (1, "C"),
    ]

    assert order_festival_alerts_stable(alerts) == ["A", "B", "C"]


def test_order_festival_alerts_stable_mixed_ties() -> None:
    alerts = [
        (2, "X"),
        (1, "A"),
        (1, "B"),
        (2, "Y"),
    ]

    assert order_festival_alerts_stable(alerts) == ["A", "B", "X", "Y"]


def test_order_festival_alerts_stable_empty_input() -> None:
    assert order_festival_alerts_stable([]) == []


# -----------------------------
# top_k_festival_alerts
# -----------------------------

def test_top_k_festival_alerts_normal_case() -> None:
    alerts = [
        (3, "Merch tent low stock"),
        (1, "Storm warning"),
        (2, "Ticket scanner issue"),
        (1, "Stage power failure"),
    ]

    assert top_k_festival_alerts(alerts, 3) == [
        "Storm warning",
        "Stage power failure",
        "Ticket scanner issue",
    ]


def test_top_k_festival_alerts_k_zero() -> None:
    alerts = [(1, "A"), (2, "B")]
    assert top_k_festival_alerts(alerts, 0) == []


def test_top_k_festival_alerts_k_negative() -> None:
    alerts = [(1, "A"), (2, "B")]
    assert top_k_festival_alerts(alerts, -5) == []


def test_top_k_festival_alerts_k_larger_than_input() -> None:
    alerts = [
        (2, "Food court power issue"),
        (1, "Main Stage microphone failed"),
    ]

    result = top_k_festival_alerts(alerts, 10)

    assert result == [
        "Main Stage microphone failed",
        "Food court power issue",
    ]


def test_top_k_festival_alerts_empty_input() -> None:
    assert top_k_festival_alerts([], 3) == []


def test_top_k_festival_alerts_duplicate_priorities() -> None:
    alerts = [
        (1, "A"),
        (1, "B"),
        (2, "C"),
        (2, "D"),
    ]

    result = top_k_festival_alerts(alerts, 2)

    assert len(result) == 2
    assert set(result) == {"A", "B"}


# -----------------------------
# peek_next_festival_alert
# -----------------------------

def test_peek_next_festival_alert_normal_case() -> None:
    alerts = [
        (2, "Food court power issue"),
        (1, "Main Stage microphone failed"),
        (3, "Lost umbrella report"),
    ]

    assert peek_next_festival_alert(alerts) == "Main Stage microphone failed"


def test_peek_next_festival_alert_empty_input() -> None:
    assert peek_next_festival_alert([]) is None


def test_peek_next_festival_alert_does_not_modify_original_input() -> None:
    alerts = [
        (2, "Lighting check"),
        (1, "Security call"),
        (3, "Lost scarf report"),
    ]

    original = alerts.copy()

    result = peek_next_festival_alert(alerts)

    assert result == "Security call"
    assert alerts == original


def test_peek_next_festival_alert_with_same_priorities() -> None:
    alerts = [
        (1, "A"),
        (1, "B"),
    ]

    result = peek_next_festival_alert(alerts)

    assert result in {"A", "B"}