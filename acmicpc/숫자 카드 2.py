# https://www.acmicpc.net/problem/10816

import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_pos = [0 for _ in range(10000001)]
n_neg = [0 for _ in range(10000001)]
for i in n_list :
    if i >= 0 :
        n_pos[i] += 1
    else :
        n_neg[abs(i)] += 1
m = int(input())
m_list = list(map(int, input().split()))
for i in m_list :
    if i >= 0 :
        print(n_pos[i], end = ' ')
    else :
        print(n_neg[abs(i)], end = ' ')