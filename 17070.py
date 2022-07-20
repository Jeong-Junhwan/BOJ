# 파이프 옮기기 1

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
house = []
house.append([0 for i in range(n + 1)])
for i in range(n):
    house.append([0] + list(map(int, input().split())))

dp_table = [[[0, 0, 0] for i in range(n + 1)] for j in range(n + 1)]
dp_table[1][2][0] = 1


for i in range(1, n + 1):
    for j in range(3, n + 1):
        if house[i][j] == 1:
            dp_table[i][j] = [0, 0, 0]
        else:
            # 수평으로 들어옴 = 바로 왼쪽이 수평이였거나 대각선
            dp_table[i][j][0] = dp_table[i][j - 1][0] + dp_table[i][j - 1][1]

            # 수직으로 들어옴 = 바로 위가 수직이였거나 대각선
            dp_table[i][j][2] = dp_table[i - 1][j][2] + dp_table[i - 1][j][1]

            # 대각선으로 들어옴 = 왼쪽 위에 경우 다 가능 (대신 벽이 없어야 함)
            if house[i - 1][j] == house[i][j - 1] == 0:
                dp_table[i][j][1] = sum(dp_table[i - 1][j - 1])
print(sum(dp_table[n][n]))
