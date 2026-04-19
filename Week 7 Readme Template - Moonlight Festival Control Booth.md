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

This guarantees that alerts are returned in correct priority order without sorting the entire list directly.

---

### `order_festival_alerts_stable`

To handle ties (same priority), I needed to preserve the original input order.

- I stored heap items as: `(priority, index, title)`
- The `index` comes from `enumerate(alerts)`
- If two alerts have the same priority, Python compares the index next

This ensures **stable ordering**, meaning earlier alerts are processed first when priorities match.

---

### `top_k_festival_alerts`

The goal here was to return only the `k` most urgent alerts.

- I pushed all alerts into a heap
- Then I popped only the first `k` elements
- I used `min(k, len(alerts))` to safely handle cases where `k` is larger than the input size

Edge cases handled:
- If `k <= 0`, return an empty list
- If alerts list is empty, return an empty list

---

### `peek_next_festival_alert`

This function returns the next alert without modifying the original input.

- I created a copy of the list and used `heapq.heapify()` to convert it into a heap
- Then I accessed the smallest element using `heap[0]` (constant time)
- This avoids permanently changing the original alerts list

---

## Complexity

### `order_festival_alerts`

- **Time:** O(n log n)  
- **Space:** O(n)  
- **Why:**  
  Each of the `n` alerts is pushed into the heap (O(log n)) and later popped (O(log n)), resulting in O(n log n) overall. The heap stores all elements, requiring O(n) space.

---

### `order_festival_alerts_stable`

- **Time:** O(n log n)  
- **Space:** O(n)  
- **Why:**  
  Same as above, but each heap element also stores an index. This does not change the overall complexity.

---

### `top_k_festival_alerts`

- **Time:** O(n log n)  
- **Space:** O(n)  
- **Why:**  
  Building the heap takes O(n log n), and extracting `k` elements takes O(k log n). In the worst case (k = n), it becomes O(n log n).

---

### `peek_next_festival_alert`

- **Time:** O(n)  
- **Space:** O(n)  
- **Why:**  
  Heapifying the copied list takes O(n), and accessing the smallest element is O(1). The copy requires additional space.

---

## Edge-case checklist

### `order_festival_alerts`

- [x] empty input  
- [x] one alert  
- [x] multiple different priorities  

---

### `order_festival_alerts_stable`

- [x] same-priority tie  
- [x] all same priority  
- [x] empty input  

---

### `top_k_festival_alerts`

- [x] `k = 0`  
- [x] `k > len(alerts)`  
- [x] duplicate priorities  
- [x] empty input  

---

### `peek_next_festival_alert`

- [x] empty input  
- [x] normal case  

---

## Test notes

- Tests were written using `pytest` and cover both normal and edge cases.
- Special attention was given to tie-handling and ensuring stable ordering.
- Additional tests verify that functions do not modify the original input (especially for `peek`).

---

## Assistance & Sources

### AI used?

- [x] Yes  

If yes, what did it help with?

- Reviewing and improving code structure  
- Clarifying heap usage and edge cases  
- Strengthening explanations for complexity and approach  

---

### Other sources

- Python official documentation (`heapq`)
- Lecture notes and class materials  

---

## Reflection

### What was hardest?

Understanding how to correctly handle tie cases while still using a heap was the most challenging part. Initially, it was not obvious how to preserve input order without breaking the priority logic.

---

### What do you understand better now?

I now clearly understand how priority queues work and why heaps are more efficient than sorting for this type of problem. I also learned how small design decisions (like adding an index) can significantly affect correctness.