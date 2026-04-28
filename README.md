# Week 7 Homework: Moonlight Festival Control Booth

## Summary

This project uses Python heapq to organize festival alerts by priority. Lower numbers are more urgent. The system processes alerts in correct priority order instead of arrival order.

---

## Functions

### order_festival_alerts

Returns all alert titles in priority order.

### order_festival_alerts_stable

Returns alerts in priority order. If priorities match, keeps original order.

### top_k_festival_alerts

Returns only the k most urgent alerts.

### peek_next_festival_alert

Returns next alert without changing original list.

---

## Complexity

### order_festival_alerts

- Time: O(n log n)
- Space: O(n)

### order_festival_alerts_stable

- Time: O(n log n)
- Space: O(n)

### top_k_festival_alerts

- Time: O(n log n)
- Space: O(n)

### peek_next_festival_alert

- Time: O(n)
- Space: O(n)

---

## Why Heap Is Good

A heap is useful because it quickly gives the smallest priority item. This makes it perfect for urgent task systems.

---

## Run Tests

```bash
pytest -q
