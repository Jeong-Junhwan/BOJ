# 최소비용 구하기

import sys
import heapq

input = sys.stdin.readline

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

bus = dict()  # bus[a] = [[b, cost], [c, cost2], ...]
for _ in range(m):
    a, b, cost = map(int, input().split())
    if a in bus:
        bus[a].append([cost, b])
    else:
        bus[a] = [[cost, b]]

start, end = map(int, input().split())

heap = []
visited = set()
heapq.heappush(heap, (0, start))  # (cost, city) 를 넣기

while heap:
    cur_cost, cur_city = heapq.heappop(heap)
    # heap 이니까 이미 방문했으면 무조건 같거나 작은 비용으로 방문함
    if cur_city in visited:
        continue

    # 도착 했으면 즉시 종료
    if cur_city == end:
        print(cur_cost)
        break

    # 이미 방문 안하고 종료 도시도 아닌 경우
    visited.add(cur_city)
    if cur_city not in bus:  # 근데 연결된 도시가 더 없으면 다음으로
        continue
    # 연결된 도시가 있으면 heap에 추가
    for next_cost, next_city in bus[cur_city]:
        if next_city in visited:
            continue
        heapq.heappush(heap, (cur_cost + next_cost, next_city))
