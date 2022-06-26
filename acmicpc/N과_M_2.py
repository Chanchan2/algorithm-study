# https://www.acmicpc.net/problem/15650
from itertools import combinations
n, m = map(int, input().split())

numbers = list(range(1, n + 1))

result = list(combinations(numbers, m))

for i in result :
    temp = map(str, i)
    print(' '.join(temp))