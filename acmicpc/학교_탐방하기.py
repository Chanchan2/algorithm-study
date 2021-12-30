# https://www.acmicpc.net/problem/13418
# 크루즈칼 알고리즘

import sys

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

n, m = map(int, input().split())
parent = list(range(n + 1))
edges = []
min_result = 0
max_result = 0

for _ in range(m + 1) :
    a, b, c = map(int, input().split())
    if c == 0 :
        cost = 1
    else :
        cost = 0
    edges.append((cost, a, b))

edges.sort() # min

for edge in edges :
    cost, a, b = edge
    

    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        min_result += cost

minimum_cost = min_result**2

edges = sorted(edges, reverse = True) # max
parent = list(range(n + 1))

for edge in edges :
    cost, a, b = edge
    

    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        max_result += cost

maximum_cost = max_result**2

print(maximum_cost - minimum_cost)
