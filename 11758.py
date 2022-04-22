import sys

INPUT = sys.stdin.readline

# ccw인지 확인
def check_ccw(a, b, c):
    # 벡터를 이용하여 a,b와 b,c를 비교하면 됨
    def vector(p1, p2):
        return (p2[0] - p1[0], p2[1] - p1[1])

    vector_1 = vector(a, b)  # a -> b 벡터
    vector_2 = vector(b, c)  # b -> c 벡터

    # 외적을 이용하여 cw 인지 ccw인지 확인
    cross_product_value = vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0]

    # 외적값이 0보다 크면 ccw
    if cross_product_value > 0:
        return 1
    elif cross_product_value == 0:
        return 0
    # 아니면 cw
    return -1


p1 = tuple(map(int, INPUT().split()))
p2 = tuple(map(int, INPUT().split()))
p3 = tuple(map(int, INPUT().split()))

print(check_ccw(p1, p2, p3))
