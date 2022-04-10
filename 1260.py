import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

graph = dict()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]


def dfs(x):
    dfs_result = []
    stack = [x]
    while stack:
        node = stack.pop()
        if visited_dfs[node] == False:
            visited_dfs[node] = True
            dfs_result.append(node)
            if node in graph:
                graph[node].sort(reverse=True)
                stack.extend(graph[node])
    return dfs_result


def bfs(x):
    bfs_result = []
    queue = deque()
    queue.append(x)
    while queue:
        node = queue.popleft()
        if visited_bfs[node] == False:
            visited_bfs[node] = True
            bfs_result.append(node)
            if node in graph:
                graph[node].sort()
                queue.extend(graph[node])
    return bfs_result


for i in dfs(v):
    print(i, end=" ")
print()
for i in bfs(v):
    print(i, end=" ")
