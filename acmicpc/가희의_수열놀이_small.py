# https://www.acmicpc.net/problem/17162

import sys

input = sys.stdin.readline


q, mod = map(int, input().split())

arr = []
count = [[] for _ in range(mod)]
order = 0
for _ in range(q) :
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        j = temp[1] % mod
        arr.append(j)
        count[j].append(order)
        order += 1

    elif temp[0] == 2 :
        if arr :
            del count[arr.pop()][-1]
            order -= 1
    
    else :
        if all(count) :
            result = [i[-1] for i in count]
            print(max(result) - min(result) + 1)
        else :
            print(-1)

          