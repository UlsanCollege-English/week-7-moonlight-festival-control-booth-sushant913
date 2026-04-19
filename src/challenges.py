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

    Uses a min-heap to process alerts efficiently.
    """
    if not alerts:
        return []

    heap: list[tuple[int, str]] = []

    # Build heap
    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    # Extract in priority order
    result: list[str] = []
    while heap:
        _, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(alerts: List[Tuple[int, str]]) -> List[str]:
    """
    Return alert titles in priority order.

    If two alerts share the same priority, the one that appeared
    earlier in the input list is handled first (stable behavior).

    Achieved by adding the index as a secondary sort key.
    """
    if not alerts:
        return []

    heap: list[tuple[int, int, str]] = []

    # Include index to preserve order for ties
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

    Rules:
    - k <= 0 → return []
    - k > len(alerts) → return all alerts in priority order
    """
    if k <= 0 or not alerts:
        return []

    heap: list[tuple[int, str]] = []

    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result: list[str] = []

    # Extract only k items (or fewer if not enough alerts)
    for _ in range(min(k, len(heap))):
        _, title = heapq.heappop(heap)
        result.append(title)

    return result


def peek_next_festival_alert(alerts: List[Tuple[int, str]]) -> Optional[str]:
    """
    Return the title of the next alert to handle without modifying
    the original alerts list.

    Uses heapify on a copy to avoid side effects.

    Returns:
        - title (str) if alerts exist
        - None if alerts is empty
    """
    if not alerts:
        return None

    # Create a copy so original list is unchanged
    heap = list(alerts)
    heapq.heapify(heap)

    # Peek (smallest priority element)
    return heap[0][1]