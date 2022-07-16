# 연구소

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
pos_012 = [[] for _ in range(3)]
cnt_0 = 0
rnd_center = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j, x in enumerate(temp):
        pos_012[x].append((i, j))
        if x == 0:
            cnt_0 += 1
    rnd_center.append(temp)
# 0 빈칸
# 1 벽
# 2 바이러스


def next_four(cur_pos):
    cur_x = cur_pos[0]
    cur_y = cur_pos[1]
    return_set = set()
    return_set.add((max(cur_x - 1, 0), cur_y))  # 상
    return_set.add((min(cur_x + 1, n - 1), cur_y))  # 하
    return_set.add((cur_x, max(cur_y - 1, 0)))  # 좌
    return_set.add((cur_x, min(cur_y + 1, m - 1)))  # 우
    try:
        return_set.remove((cur_x, cur_y))
    except:
        pass
    return return_set


def bfs(starts, rnd_center, cnt):
    visited = set()
    queue = deque()
    queue.extend(starts)
    while queue:
        cur_node = queue.popleft()
        if cur_node in visited:
            continue
        next_nodes = next_four(cur_node)
        for next_node in next_nodes:
            if rnd_center[next_node[0]][next_node[1]] == 0:
                rnd_center[next_node[0]][next_node[1]] = 2
                cnt -= 1
                queue.append(next_node)
    return cnt


answer = 0
for combination in combinations(pos_012[0], 3):
    new_rnd_center = []
    for i in rnd_center:
        new_rnd_center.append(i.copy())
    for pos in combination:
        new_rnd_center[pos[0]][pos[1]] = 1
    answer = max(answer, bfs(pos_012[2], new_rnd_center, cnt_0 - 3))

print(answer)
