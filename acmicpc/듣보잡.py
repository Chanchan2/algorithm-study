# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cant_hear = []
cant_see = []
for i in range(n) :
    cant_hear.append(input().strip())
for i in range(m) :
    cant_see.append(input().strip())

result = set(cant_hear) & set(cant_see)
result = sorted(list(result))
print(len(result))
print('\n'.join(result))