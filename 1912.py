# 연속합

import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
dp_list = []
max_answer = -1000

for i, x in enumerate(input_list):
    if i != 0:
        n1 = 0
        n2 = x + dp_list[i - 1]
        n3 = x

        max_answer = max(max_answer, n2, n3)
        dp_list.append(max(n1, n2, n3))

    else:
        max_answer = max(max_answer, input_list[0])
        dp_list.append(input_list[0])

print(max_answer)
