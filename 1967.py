# 트리의 지름

import sys

input = sys.stdin.readline

n = int(input())

tree = dict()
for i in range(n - 1):
    parent, child, weight = map(int, input().split())
    if parent not in tree:
        tree[parent] = [(child, weight)]
    else:
        tree[parent].append((child, weight))

    if child not in tree:
        tree[child] = [(parent, weight)]
    else:
        tree[child].append((parent, weight))


def search(start):
    visit = [False for i in range(n + 1)]
    stack = [[start, 0]]
    max_len = 0
    end_pos = 0
    while stack:
        cur_node, cur_weight = stack.pop()
        if visit[cur_node] == True:
            continue

        visit[cur_node] = True
        if cur_weight > max_len:
            max_len = cur_weight
            end_pos = cur_node
        try:
            for next_node, next_weight in tree[cur_node]:
                stack.append([next_node, cur_weight + next_weight])
        except:
            continue
    return (end_pos, max_len)


print(search(search(1)[0])[1])
