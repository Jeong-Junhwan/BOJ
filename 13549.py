# 숨바꼭질 3

import heapq

n, k = map(int, input().split())
min_heap = []
visited = set()
heapq.heappush(min_heap, (0, n))

while min_heap:
    cnt, pos = heapq.heappop(min_heap)
    if pos in visited:
        continue

    if pos == k:
        print(cnt)
        break

    visited.add(pos)
    if pos > 0:
        heapq.heappush(min_heap, (cnt + 1, pos - 1))
    if pos < k:
        heapq.heappush(min_heap, (cnt + 1, pos + 1))
        heapq.heappush(min_heap, (cnt, pos * 2))
