# 곱셈

A, B, C = map(int, input().split())


def power(a, b):
    if b == 1:
        return a % C
    elif b == 2:
        return a * a % C

    else:
        if b % 2 == 0:
            temp = power(a, b // 2)
            return temp * temp % C

        else:
            temp = power(a, b // 2)
            return temp * temp * a % C


print(power(A, B))
