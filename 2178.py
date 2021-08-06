import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().strip()))

#4개 방향 찾기
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        nodes = queue.popleft()
        for node in nodes:
            #현재 위치 기준으로 네 방향 검사하기
            temp = []
            for i in range(4):
                nx = node[0] + dx[i]
                ny = node[1] + dy[i]

                #범위를 벗어났으면 스킵
                if not (0 <= nx <= m-1 and 0 <= ny <= n-1):
                    continue
                #벽 혹은 첫칸으로 돌아온경우 스킵
                if graph[ny][nx] == '0' or (nx == 0 and ny == 0):
                    continue

                #아직 가지 않은 '1' 칸이면, 현재 칸에서 +1 해주기
                if graph[ny][nx] == '1':
                    graph[ny][nx] = int(graph[node[1]][node[0]]) + 1
                    temp.append((nx,ny))
            queue.append(temp)
    return graph[n-1][m-1]

print(bfs([(0,0)]))
