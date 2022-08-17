# 아기 상어

import sys
from collections import deque

input = sys.stdin.readline
# 위, 왼쪽 순으로 방문하도록 설정
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)


n = int(input())
space = []
for i in range(n):
    temp = list(map(int, input().split()))
    if 9 in temp:
        start_x = i
        start_y = temp.index(9)
    space.append(temp)
space[start_x][start_y] = 0
answer = 0
# 0 빈칸
# 1~6 물고기 크기
# 9 상어
def bfs(start_x, start_y, start_size, start_cnt_eat, start_timer):
    queue = deque()
    queue.append((start_x, start_y, start_size, start_cnt_eat, start_timer))
    visit = [[False for j in range(n)] for i in range(n)]
    visit[start_x][start_y] = True
    possible_fish = []
    temp_timer = 10**7

    while queue:
        x, y, size, cnt_eat, timer = queue.popleft()

        # 가능한 물고기 군이 존재하는데, 현재 칸 수가 더 많이 온 상황
        if possible_fish and temp_timer < timer:
            possible_fish.sort(key=lambda x: (x[4], x[0], x[1]))

            space[possible_fish[0][0]][possible_fish[0][1]] = 0
            return possible_fish[0]

        timer += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if visit[nx][ny]:
                continue

            if space[nx][ny] > size:
                continue
            elif space[nx][ny] == size or space[nx][ny] == 0:
                queue.append((nx, ny, size, cnt_eat, timer))
                visit[nx][ny] = True
            else:
                temp_timer = min(temp_timer, timer)
                if cnt_eat == size - 1:
                    possible_fish.append((nx, ny, size + 1, 0, timer))
                else:
                    possible_fish.append((nx, ny, size, cnt_eat + 1, timer))

                visit[nx][ny] = True

    if possible_fish:
        possible_fish.sort(key=lambda x: (x[4], x[0], x[1]))
        space[possible_fish[0][0]][possible_fish[0][1]] = 0
        return possible_fish[0]


f = bfs(start_x, start_y, 2, 0, 0)

while f:
    answer = f[4]
    f = bfs(f[0], f[1], f[2], f[3], f[4])

print(answer)
