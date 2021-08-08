import sys
from collections import deque
m,n = map(int, sys.stdin.readline().split())

#1익음 0익지않음 -1빈칸
tomato1 = []
tomatoes = []
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    tomatoes.append(temp)
    #익은 토마토의 위치를 따로 저장
    for i in range(len(temp)):
        if temp[i] == 1:
            tomato1.append((i,_))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(tomato1):
    queue = deque(tomato1)
    while queue:
        node = queue.popleft()
        
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]

            #밖으로 벗어난 경우 제외
            if not (0 <= nx <= m-1 and 0 <= ny <= n-1):
                continue
            #해당 칸이 토마토이면 익은토마토로 변경 
            if tomatoes[ny][nx] == 0:
                tomatoes[ny][nx] = tomatoes[node[1]][node[0]] + 1
                queue.append((nx,ny))

def printing():
    days = 0
    for i in tomatoes:
        for j in i:
            if j == 0:
                return -1
            if j > days:
                days = j
    return days -1 
bfs(tomato1)
print(printing())
