# https://www.acmicpc.net/problem/1037

import sys

input = sys.stdin.readline

n = int(input())
factor_list = list(map(int, input().split()))
N = min(factor_list) * max(factor_list)
print(N)