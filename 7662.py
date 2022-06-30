import sys
import heapq


# 테스트 케이스 개수
T = int(sys.stdin.readline().strip())
for t in range(T):
    # Q에 적용할 연산의 개수
    k = int(sys.stdin.readline().strip())

    Q1 = []  # 최소
    Q2 = []  # 최대
    cnt_dict = dict()
    for _ in range(k):
        DI, n = sys.stdin.readline().split()

        if DI == "I":
            heapq.heappush(Q1, int(n))
            heapq.heappush(Q2, -int(n))
            try:
                cnt_dict[int(n)] += 1
            except:
                cnt_dict[int(n)] = 1
        else:
            try:
                if n == "-1":
                    # 최솟값 삭제
                    while True:
                        temp = Q1[0]
                        if cnt_dict[temp] >= 1:
                            cnt_dict[temp] -= 1
                            heapq.heappop(Q1)
                            break
                        else:
                            heapq.heappop(Q1)
                else:
                    # 최댓값 삭제
                    while True:
                        temp = -Q2[0]
                        if cnt_dict[temp] >= 1:
                            cnt_dict[temp] -= 1
                            heapq.heappop(Q2)
                            break
                        else:
                            heapq.heappop(Q2)

                # 그 뭐냐 최소나 최대가 삭제 되어야 하면 삭제
                while True:
                    try:
                        if cnt_dict[Q1[0]] < 1:
                            heapq.heappop(Q1)
                        else:
                            break
                    except:
                        break

                while True:
                    try:
                        if cnt_dict[-Q2[0]] < 1:
                            heapq.heappop(Q2)
                        else:
                            break
                    except:
                        break

            except:
                Q1.clear()
                Q2.clear()
                cnt_dict.clear()

    if not Q1 or not Q2:
        print("EMPTY")
    else:
        print(-Q2[0], Q1[0])
