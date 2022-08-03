# 특정한 최단 경로

import sys
import heapq

input = sys.stdin.readline
INF = 100000000

# 정점, 간선
n, e = map(int, input().split())

# 그래프
g = [[INF for i in range(n + 1)] for j in range(n + 1)]

for i in range(e):
    # a <-> b 비용이 c
    a, b, c = map(int, input().split())
    g[a][b] = c
    g[b][a] = c

# 반드시 지나야 하는 두 점
v1, v2 = map(int, input().split())


def path_find(start, end):
    cost = [INF for i in range(n + 1)]
    cost[start] = 0
    heap = [[0, start]]
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)

        if cur_node == end:
            return cur_cost

        if cur_cost > INF:
            return INF

        for next_node, next_cost in enumerate(g[cur_node]):
            if next_node == 0 or next_node == cur_node:
                continue

            if cur_cost + next_cost < cost[next_node]:
                cost[next_node] = cur_cost + next_cost
                heapq.heappush(
                    heap,
                    [cur_cost + next_cost, next_node],
                )
    return INF


case_1 = path_find(1, v1) + path_find(v1, v2) + path_find(v2, n)
case_2 = path_find(1, v2) + path_find(v2, v1) + path_find(v1, n)
min_case = min(case_1, case_2)
if min_case >= INF:
    print(-1)
else:
    print(min_case)
