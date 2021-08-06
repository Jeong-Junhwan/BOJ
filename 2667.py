import sys

n = int(sys.stdin.readline().strip())
house = []
for _ in range(n):
    house.append(list(sys.stdin.readline().strip()))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    cnt = 1
    stack = []
    stack.append((x,y))
    house[x][y] = 2
    while stack:
        node = stack.pop()
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]

            #범위 벗어난 경우
            if not (0 <= nx <= n-1 and 0 <= ny <= n-1):
                continue
            #집이 있는 경우를 2로 바꾸기
            if house[nx][ny] == '1':
                house[nx][ny] = 2
                cnt += 1
                stack.append((nx,ny))
    return cnt    



#모든 집 돌면서 아직 방문 안한 '1' 이 있는 칸에서 dfs 실행
answer = []
for i in range(n):
    for j in range(n):
        if house[i][j] == '1':
            answer.append(dfs(i,j))

print(len(answer))
answer.sort()
for i in answer:
    print(i)
