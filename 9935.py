# 문자열 폭발

s = input()
boom = input()

boom_len = len(boom)
answer = []

for x in s:
    answer.append(x)
    if x == boom[-1] and "".join(answer[-boom_len:]) == boom:
        for i in range(boom_len):
            answer.pop()

print("".join(answer)) if answer else print("FRULA")
