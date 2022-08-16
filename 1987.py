# 알파벳

import sys

input = sys.stdin.readline
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

r, c = map(int, input().split())
board = []
for i in range(r):
    board.append(input().rstrip())

visit = [False] * 26
visit[ord(board[0][0]) - 65] = True
ans = 1


def back_tracking(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    if ans >= 26:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if visit[ord(board[nx][ny]) - 65]:
            continue

        visit[ord(board[nx][ny]) - 65] = True
        back_tracking(nx, ny, cnt + 1)
        visit[ord(board[nx][ny]) - 65] = False


back_tracking(0, 0, 1)
print(ans)
