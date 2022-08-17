# 암호 만들기

from itertools import combinations

l, c = map(int, input().split())
s = input().split()
s.sort()

for x in combinations(s, l):
    temp = []
    cnt1 = 0
    cnt2 = 0
    for y in x:
        temp.append(y)
        if y in "aeiou":
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= 1 and cnt2 >= 2:
        print("".join(temp))
