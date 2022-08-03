# 1043 거짓말

import sys

input = sys.stdin.readline

# 사람 수, 파티 수
n, m = map(int, input().split())

# 같은 정보를 공유하는 집단
groups = []

# 진실을 아는 사람들 (과장을 하면 안됨)
know_true = set()
true_input = list(map(int, input().split()))
if true_input[0] != 0:
    for people in true_input[1:]:
        know_true.add(people)
groups.append(know_true)

# 파티에 오는 사람들
come_party = []
for i in range(m):
    come_party_input = list(map(int, input().split()))
    come_party.append(come_party_input)
    union_group = []
    for people in come_party_input[1:]:
        for idx, group in enumerate(groups):
            if people in group:
                if idx not in union_group:
                    union_group.append(idx)
                group.update(come_party_input[1:])

    if len(union_group) == 0:
        groups.append(set(come_party_input[1:]))
    elif len(union_group) >= 2:
        union_group.sort()
        for idx in union_group[1:]:
            groups[union_group[0]] = groups[union_group[0]].union(groups[idx])
        union_group.sort(reverse=True)
        for idx in union_group[:-1]:
            del groups[idx]

answer = 0
for party in come_party:
    if party[1] not in groups[0]:
        answer += 1
print(answer)
