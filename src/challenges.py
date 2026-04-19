"""
Week 7: Moonlight Festival Control Booth

Use Python's heapq module to solve priority queue problems.
"""

from __future__ import annotations

import heapq
from typing import List, Tuple, Optional


def order_festival_alerts(alerts: List[Tuple[int, str]]) -> List[str]:
    """
    Return alert titles in the order they should be handled.

    Each alert is a tuple:
        (priority, title)

    Smaller priority numbers are handled first.
    """
    if not alerts:
        return []

    heap: list[tuple[int, str]] = []

    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result: list[str] = []

    while heap:
        _, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(alerts: List[Tuple[int, str]]) -> List[str]:
    """
    Return alert titles in priority order.

    If two alerts have the same priority, preserve input order.
    """
    if not alerts:
        return []

    heap: list[tuple[int, int, str]] = []

    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result: list[str] = []

    while heap:
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def top_k_festival_alerts(alerts: List[Tuple[int, str]], k: int) -> List[str]:
    """
    Return the titles of the k most urgent alerts.

    If k <= 0, return an empty list.
    If k is larger than the number of alerts, return as many as possible.

    Uses stable ordering for same-priority alerts.
    """
    if k <= 0 or not alerts:
        return []

    heap: list[tuple[int, int, str]] = []

    # 🔥 FIX: include index for stable ordering
    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result: list[str] = []

    for _ in range(min(k, len(heap))):
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def peek_next_festival_alert(alerts: List[Tuple[int, str]]) -> Optional[str]:
    """
    Return the title of the next alert without modifying the original list.

    If alerts is empty, return None.
    """
    if not alerts:
        return None

    heap = list(alerts)  # copy
    heapq.heapify(heap)

    return heap[0][1]