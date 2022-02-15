# https://www.acmicpc.net/problem/11650

import sys

input = sys.stdin.readline

n = int(input())
pairs = []

for _ in range(n) :
    pairs.append(tuple(map(int, input().split())))

pairs = sorted(pairs, key = lambda x : (x[0], x[1]))
for x, y in pairs :
    print(x, y)