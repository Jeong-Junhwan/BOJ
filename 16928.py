# 뱀과 사다리 게임
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ladders_or_snakes = dict()
for _ in range(n + m):
    a, b = map(int, input().split())
    ladders_or_snakes[a] = b

queue = deque()
queue.append([1, 0])  # 현재 위치, 주사위 횟수
visited = set()

while queue:
    cur_pos, cur_cnt = queue.popleft()
    if cur_pos == 100:
        print(cur_cnt)
        break

    if cur_pos in visited:
        continue

    visited.add(cur_pos)
    for i in range(1, 7):
        next_pos = min(cur_pos + i, 100)
        if next_pos in ladders_or_snakes:
            next_pos = ladders_or_snakes[next_pos]
        queue.append([next_pos, cur_cnt + 1])
