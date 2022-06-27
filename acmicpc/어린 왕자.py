# https://www.acmicpc.net/problem/1004

import sys

input = sys.stdin.readline

T = int(input())

def is_in(p_1, p_2, r) :
    d = ((p_1[0] - p_2[0])**2 + (p_1[1] - p_2[1])**2)**0.5
    return d < r

def check_in_and_out() :
    x_1, y_1, x_2, y_2 = map(int,input().split())
    p_s = (x_1, y_1)
    p_a = (x_2, y_2)
    n = int(input())
    cnt = 0
    for _ in range(n) :
        c_x, c_y, r = map(int, input().split())
        p_p = (c_x, c_y)
        if is_in(p_s, p_p, r) and is_in(p_a, p_p, r) :
            continue
        elif is_in(p_s, p_p, r) or is_in(p_a, p_p, r) :
            cnt += 1
    print(cnt)

for i in range(T) :
    check_in_and_out()