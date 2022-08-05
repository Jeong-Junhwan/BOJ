# 벽 부수고 이동하기

import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(input().rstrip())

visit = [[[False, False] for i in range(m)] for j in range(n)]
visit[0][0] = [True, True]
queue = deque([(0, 0, 1, 0)])
answer = -1
while queue:
    # x, y, 지금까지 거리, 벽을 부술 수 있는가? (0 아직 안부숨 1 부숨)
    x, y, dist, break_wall = queue.popleft()

    if x == n - 1 and y == m - 1:
        answer = dist
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 바깥으로 나간 경우
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        # 이미 벽도 안뚫어보고 방문한경우
        if visit[nx][ny][0]:
            continue

        # 벽 뚫고 방문했지만 지금 아직 벽 안뚫은경우는 킵해야함
        # 따라서 벽 뚫은 경우만 continue
        elif visit[nx][ny][1] and break_wall == 1:
            continue

        # 벽이 아닌 경우
        if matrix[nx][ny] == "0":
            queue.append((nx, ny, dist + 1, break_wall))
            visit[nx][ny][break_wall] = True
        # 벽인경우
        else:
            # 이미 벽 부수고 왔으면 더 못부숨
            if break_wall == 1:
                continue
            queue.append((nx, ny, dist + 1, 1))
            visit[nx][ny][1] = True

print(answer)
