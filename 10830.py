# 행렬 제곱

import sys

input = sys.stdin.readline

n, b = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))


def matrix_mul(m1, m2):
    temp = [[0 for i in range(n)] for j in range(n)]
    for i, row in enumerate(m1):
        for j, col in enumerate(zip(*m2)):
            t = 0
            for a, b in zip(row, col):
                t += a * b
            temp[i][j] = t % 1000
    return temp


def matrix_pow(mat, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000
        return mat
    elif b == 2:
        return matrix_mul(mat, mat)
    if b % 2 == 0:
        return matrix_pow(matrix_mul(mat, mat), b // 2)
    return matrix_mul(mat, matrix_pow(matrix_mul(mat, mat), b // 2))


for row in matrix_pow(matrix, b):
    print(*row)
