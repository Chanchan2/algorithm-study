# https://www.acmicpc.net/problem/15651

from itertools import product

n, m = map(int, input().split())

result = product(range(1, n + 1), repeat=m)

for i in result :
    temp = list(map(str, i))
    print(' '.join(temp))