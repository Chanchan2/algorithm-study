# https://www.acmicpc.net/problem/6051

import sys

input = sys.stdin.readline

n = int(input())

q_list = [[]]
def print_num(q_list) :
    if q_list :
        print(q_list[-1])
    else :
        print(-1)

for _ in range(n) :
    query = input().split()
    if query[0] == 'a' :
        q_list.append(q_list[-1] + [int(query[1])])

    elif query[0] == 's' :
        q_list.append(q_list[-1][:-1])

    else :
        q_list.append(q_list[int(query[1]) - 1])

    print_num(q_list[-1])
