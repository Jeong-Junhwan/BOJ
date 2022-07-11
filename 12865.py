# 평범한 배낭

import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # 물건 수, 최대 무게
dp_table = [[0 for _ in range(k + 1)] for __ in range(n + 1)]
for i in range(1, n + 1):
    w, v = map(int, input().split())  # 무게, 가치
    for j in range(1, k + 1):
        if w > k:
            dp_table[i][j] = dp_table[i - 1][j]
        else:
            if j >= w:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - w] + v)
            else:
                dp_table[i][j] = dp_table[i - 1][j]

print(dp_table[n][k])
