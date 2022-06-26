# https://www.acmicpc.net/problem/15652

from itertools import combinations_with_replacement as cwr

n, m = map(int, input().split())

result = cwr(range(1, n+1), m)

for i in result :
    for j in i :
        print(j, end=' ')
    else :
        print()