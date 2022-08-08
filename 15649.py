# N과 M (1)

import itertools

n, m = map(int, input().split())

for i in itertools.permutations(range(1, n + 1), m):
    for j in i:
        print(j, end=" ")
    print()
