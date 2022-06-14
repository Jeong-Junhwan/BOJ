# AC

import sys
from collections import deque

t = int(sys.stdin.readline().strip())


def AC(Ps, n, xs):
    queue = deque(xs[1:-1].replace("RR", "").split(","))
    left_right = True
    for p in Ps:

        if p == "R":
            left_right = not left_right
        else:
            if n >= 1:
                if left_right:
                    queue.popleft()
                else:
                    queue.pop()
                n -= 1
            else:
                print("error")
                return

    if n == 0:
        print("[]")
    else:
        if not left_right:
            queue.reverse()

        new_xs = f"[{queue[0]}"
        for i in range(1, n):
            new_xs += f",{queue[i]}"
        new_xs += "]"
        print(new_xs)


for _ in range(t):
    Ps = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    xs = sys.stdin.readline().strip()
    AC(Ps, n, xs)
