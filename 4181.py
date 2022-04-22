import sys

INPUT = sys.stdin.readline

# 발사한 화살의 수
n = int(INPUT())

# 좌표 저장
xy = []
for _ in range(n):
    x, y, c = INPUT().split()
    if c == "Y":
        xy.append(tuple(map(int, (x, y))))


def check_ccw(a, b, c):
    # 벡터를 이용하여 a,b와 b,c를 비교하면 됨
    def vector(p1, p2):
        return (p2[0] - p1[0], p2[1] - p1[1])

    vector_1 = vector(a, b)  # a -> b 벡터
    vector_2 = vector(b, c)  # b -> c 벡터

    # 외적을 이용하여 cw 인지 ccw인지 확인
    cross_product_value = vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0]

    # 외적값이 0보다 크면 ccw
    if cross_product_value >= 0:
        return True
    return False


def convex_hull():
    # x, y값 기준으로 소팅
    xy.sort(key=lambda x: (x[0], x[1]))

    # 아래쪽 한번 슥 돌고
    convex_lower = []
    for c in xy:
        while len(convex_lower) >= 2:
            a, b = convex_lower[-2], convex_lower[-1]
            if check_ccw(a, b, c) == 1:
                break
            convex_lower.pop()
        convex_lower.append(c)

    # 위쪽 한번 슥 돌고
    convex_upper = []
    for c in reversed(xy):
        while len(convex_upper) >= 2:
            a, b = convex_upper[-2], convex_upper[-1]
            if check_ccw(a, b, c):
                break
            convex_upper.pop()
        convex_upper.append(c)

    # 합친다.
    convex = convex_lower[:-1] + convex_upper[:-1]
    return convex


convex = convex_hull()
print(len(convex))
for c in convex:
    print(f"{c[0]} {c[1]}")
