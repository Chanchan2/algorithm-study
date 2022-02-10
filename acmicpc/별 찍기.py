# https://www.acmicpc.net/problem/2447

import sys

input = sys.stdin.readline

def make_pattern(num) :
    if num == 3 :
        return [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
    else :
        t = num // 3
        pat, t_star = [[' ' for i in range(num)] for j in range(num)], make_pattern(t)

        for k in range(t) :
            pat[k] = pat[num - t + k] = t_star[k]*3
        for l in range(t) :
            pat[k+1+l][:t] = pat[k+1+l][num-t:] = t_star[l]
        return pat

a = int(input())
b = make_pattern(a)
for i in range(a) :
    for j in range(a) :
        print(b[i][j], end='')
    print()