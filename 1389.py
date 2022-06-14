# 케빈 베이컨의 6단계 법칙

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
g = dict()
k_distance = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)

    if b not in g:
        g[b] = [a]
    else:
        g[b].append(a)


def bfs(g, start):
    queue = deque()
    queue.append(((start, 0)))
    visited = set()
    pre_visited = set()
    for index in range(1, start):
        pre_visited.add(index)
    while queue:
        node, distance = queue.popleft()
        if node not in visited:
            if k_distance[start][node] == 0:
                k_distance[start][node] = distance
                k_distance[node][start] = distance
                k_distance[0][start] += distance
                k_distance[0][node] += distance
            visited.add(node)
            pre_visited.add(node)
            if len(pre_visited) == n:
                break

            for child_node in g[node]:
                queue.append((child_node, distance + 1))


for i in range(1, n + 1):
    bfs(g, i)

answer = 0
min_dist = 601
for i, x in enumerate(k_distance[0]):
    if i == 0:
        pass
    else:
        if x < min_dist:
            min_dist = x
            answer = i

print(answer)
