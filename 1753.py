import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().strip())
visited = {0}
Edges = dict()



for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if u not in Edges:
        Edges[u] = [(v, w)]
    else:
        Edges[u].append((v, w))

answer = [3000001 for i in range(V + 1)]

def astar(start):
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        value, pos = heapq.heappop(heap)

        if pos in visited:
            continue

        visited.add(pos)
        
        if pos not in Edges:
            continue

        for v, w in Edges[pos]: # 이부분에서 현재위치 pos에서 가능한 간선만 탐색하면 됨
            if answer[v] >= value + w:
                answer[v] = value + w
                heapq.heappush(heap, (answer[v], v))


astar(K)
for i in range(1, V + 1):
    if i == K:
        print(0)
    elif answer[i] == 3000001:
        print("INF")
    else:
        print(answer[i])
