# 스택 수열

import sys
from collections import deque

n = int(sys.stdin.readline())
input_num = deque()
output_stack = []
answer = []
for _ in range(n):
    input_num.append(int(sys.stdin.readline()))

current_n = 1
output_stack.append(current_n)
answer.append("+")


for desired in input_num:
    if not output_stack:
        current_n += 1
        output_stack.append(current_n)
        answer.append("+")

    if desired > output_stack[-1]:
        while desired > output_stack[-1]:
            current_n += 1
            output_stack.append(current_n)
            answer.append("+")

    if desired == output_stack[-1]:
        output_stack.pop()
        answer.append("-")

    elif desired < output_stack[-1]:
        answer = ["NO"]
        break


for pushpop in answer:
    print(pushpop)
