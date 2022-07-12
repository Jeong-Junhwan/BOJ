# 내려가기

import sys

INPUT = sys.stdin.readline

n = int(INPUT())
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]
for i in range(n):
    a, b, c = map(int, INPUT().split())
    if i != 0:
        temp_a = max(dp_max[:2]) + a
        temp_b = max(dp_max) + b
        temp_c = max(dp_max[1:]) + c

        temp_d = min(dp_min[:2]) + a
        temp_e = min(dp_min) + b
        temp_f = min(dp_min[1:]) + c

        dp_max = [temp_a, temp_b, temp_c]
        dp_min = [temp_d, temp_e, temp_f]
    else:
        dp_max = [a, b, c]
        dp_min = [a, b, c]

print(max(dp_max), min(dp_min))
