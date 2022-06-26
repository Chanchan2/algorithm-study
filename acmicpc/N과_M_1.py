# https://www.acmicpc.net/problem/15649
from itertools import permutations

n, m = map(int, input().split())

numbers = list(range(1, n + 1))

for a in permutations(numbers, m) :
    print(' '.join(list(map(str, a))))