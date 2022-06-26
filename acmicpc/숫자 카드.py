# https://www.acmicpc.net/problem/10815
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
        if n_pos[i] :
            print(1, end=' ')
        else :
            print(0, end=' ')
    else :
        if n_neg[abs(i)] :
            print(1, end=' ')
        else :
            print(0, end=' ')