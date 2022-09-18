# 2048 (Easy)

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))


def direction_pop(any_deque: deque, direction: int):
    if direction > 0:
        return any_deque.popleft()
    else:
        return any_deque.pop()


def get_next_board(board, direction):
    # direction 1 up 2 down 3 left 4 right
    def get_updown_board(board, direction):
        # direction == 1 up -1 down
        next_board = [[0 for i in range(n)] for j in range(n)]

        for j, col in enumerate(zip(*board)):
            new_col = deque(x for x in col if x != 0)

            if not new_col:
                continue

            i = 0 if direction == 1 else -1
            last_append = True
            first = first = direction_pop(new_col, direction)
            while new_col:
                second = direction_pop(new_col, direction)
                if first == second:
                    next_board[i][j] = first * 2
                    if new_col:
                        first = direction_pop(new_col, direction)
                    else:
                        last_append = False
                        break
                else:
                    next_board[i][j] = first
                    first = second
                i += direction

            if last_append:
                next_board[i][j] = first

        return next_board

    def get_leftright_board(board, direction):
        # direction == 1 left -1 right
        next_board = [[0 for i in range(n)] for j in range(n)]

        for i, row in enumerate(board):
            new_row = deque(x for x in row if x != 0)

            if not new_row:
                continue

            j = 0 if direction == 1 else -1
            last_append = True
            first = first = direction_pop(new_row, direction)
            while new_row:
                second = direction_pop(new_row, direction)
                if first == second:
                    next_board[i][j] = first * 2
                    if new_row:
                        first = direction_pop(new_row, direction)
                    else:
                        last_append = False
                        break
                else:
                    next_board[i][j] = first
                    first = second
                j += direction

            if last_append:
                next_board[i][j] = first

        return next_board

    # direction 1 up 2 down 3 left 4 right
    if direction == 1:
        return get_updown_board(board, 1)
    elif direction == 2:
        return get_updown_board(board, -1)
    elif direction == 3:
        return get_leftright_board(board, 1)
    else:
        return get_leftright_board(board, -1)


def get_max_value(board):
    max_value = -1
    for row in board:
        max_value = max(max_value, max(row))
    return max_value


stack = [[board, 0]]
answer = 0
while stack:
    cur_board, depth = stack.pop()
    if depth == 5:
        answer = max(answer, get_max_value(cur_board))
        continue

    for i in range(1, 5):
        stack.append([get_next_board(cur_board, i), depth + 1])

print(answer)
