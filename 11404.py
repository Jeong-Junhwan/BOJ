# 플로이드

import sys
import heapq

INF = 10000000
input = sys.stdin.readline

n = int(input())
m = int(input())
cost = [[INF for j in range(n + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    cost[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)


def astar(start):
    heap = []
    for i, x in enumerate(cost[start]):
        if i == start or x == INF:
            continue
        heapq.heappush(heap, (x, i))

    while heap:
        cur_cost, cur_pos = heapq.heappop(heap)

        for next_pos, next_cost in enumerate(cost[cur_pos]):
            if next_cost >= INF:
                continue
            elif cost[start][next_pos] <= cur_cost + next_cost:
                continue
            heapq.heappush(heap, (cur_cost + next_cost, next_pos))
            cost[start][next_pos] = cur_cost + next_cost


for i in range(1, n + 1):
    astar(i)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0, end=" ") if cost[i][j] == INF else print(cost[i][j], end=" ")
    print()
