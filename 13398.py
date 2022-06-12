# 연속합 2

n = int(input())
input_list = list(map(int, input().split()))
dp_list = [[0] * n for _ in range(2)]

max_answer = -1000

for i, x in enumerate(input_list):
    if i != 0:

        dp_list[0][i] = max(x, dp_list[0][i - 1] + x)  # 제거 안됨
        dp_list[1][i] = max(dp_list[0][i - 1], dp_list[1][i - 1] + x)  # 제거 됨

        max_answer = max(max_answer, dp_list[0][i], dp_list[1][i])
    else:
        max_answer = max(max_answer, input_list[0])
        dp_list[0][i] = input_list[0]
        dp_list[1][i] = max(input_list[0], 0)


print(max_answer)
