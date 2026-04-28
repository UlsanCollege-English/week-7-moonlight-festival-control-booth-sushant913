# Week 7 Homework: Moonlight Festival Control Booth

## Summary

This project simulates a real-world control booth system that manages incoming festival alerts based on urgency. Instead of processing alerts in the order they arrive, the system prioritizes them using a min-heap (priority queue).

The goal was to use Python’s `heapq` module to efficiently organize, retrieve, and manage alerts, including handling edge cases like ties in priority and limiting results to the top `k` alerts.

---

## Approach

### `order_festival_alerts`

I used a min-heap to ensure that alerts with smaller priority values (higher urgency) are processed first.

- Each heap item was stored as a tuple: `(priority, title)`
- Python’s heap automatically orders by the first value (priority)
- I pushed all alerts into the heap, then repeatedly popped from it to build the result list

---

### `order_festival_alerts_stable`

To handle ties (same priority), I preserved original input order.

- Heap items stored as `(priority, index, title)`
- `index` comes from `enumerate(alerts)`
- If priorities tie, smaller index comes first

---

### `top_k_festival_alerts`

Returns only the `k` most urgent alerts.

- Push all alerts into heap
- Pop only first `k`
- Uses `min(k, len(alerts))`

Edge cases:
- `k <= 0` returns `[]`
- empty input returns `[]`

---

### `peek_next_festival_alert`

Returns next alert without changing original input.

- Copy list
- Use `heapify()`
- Return first heap item

---

## Complexity

### `order_festival_alerts`

- Time: O(n log n)
- Space: O(n)

### `order_festival_alerts_stable`

- Time: O(n log n)
- Space: O(n)

### `top_k_festival_alerts`

- Time: O(n log n)
- Space: O(n)

### `peek_next_festival_alert`

- Time: O(n)
- Space: O(n)

---

## Why Heap Is Good

A heap quickly returns the smallest priority item, making it ideal for urgent task systems.

---

## Run Tests

```bash
pytest -q