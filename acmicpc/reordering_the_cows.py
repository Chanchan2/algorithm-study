# https://www.acmicpc.net/problem/10024

import sys
from collections import Counter

input = sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input())

a = []
b = []
cows = list(range(n + 1))

for _ in range(n) :
    a.append(int(input()))

for _ in range(n) :
    b.append(int(input()))

for i in range(n) :
    if find_parent(cows, a[i]) != find_parent(cows, b[i]) :
        union_parent(cows, a[i], b[i])

for i in range(1, n + 1) :
    cows[i] = find_parent(cows, i)

cows = cows[1:]
cows_cnt = Counter(cows)

if len(cows_cnt) == n :
    print(0, -1)

else :
    print(len(cows_cnt), max(cows_cnt.values()))

