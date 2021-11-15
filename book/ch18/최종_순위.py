# https://www.acmicpc.net/problem/3665

import sys

input = sys.stdin.readline

test = int(input())
for t in range(test) :
    n = int(input())
    edges = [[] for _ in range(n + 1)]

    last_year = list(map(int, input().split()))

    for i in range(1, n) :
        edges[last_year[i]] =last_year[:i]
    
    m = int(input())
    for _ in range(m) :
        a, b = map(int, input().split())
        if b in edges[a] :
            edges[a].remove(b)
            edges[b].append(a)
        else :
            edges[b].remove(a)
            edges[a].append(b)
    
    rank = [(k, len(v)) for k, v in enumerate(edges)]
    rank_2 = sorted(rank[1:], key = lambda x : x[1])

    check = [v for k, v in rank_2]
    if check == list(range(n)) :
        print(*[k for k, v in rank_2])
    
    else :
        print('IMPOSSIBLE')