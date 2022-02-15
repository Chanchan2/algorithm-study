# https://www.acmicpc.net/problem/1018

import sys
from pprint import pprint

input = sys.stdin.readline

n, m = map(int, input().split())

chess_borad_1 = [
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
]

chess_board_2 = [
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
]

def cal(board) :
    global chess_borad_1
    global chess_board_2

    diff_1 = 0
    diff_2 = 0

    for r in range(8) :
        for c in range(8) :
            diff_1 += abs(board[r][c] - chess_borad_1[r][c])
            diff_2 += abs(board[r][c] - chess_board_2[r][c])

    return min(diff_1, diff_2)

board = []
for _ in range(n) :
    board.append([1 if i == 'B' else 0 for i in list(input())])


answer = 100
for i in range(n - 7) :
    for j in range(m - 7) :
        answer = min(answer, cal([x[j:j+8] for x in board[i:i+8]]))

print(answer)