# https://www.acmicpc.net/problem/10814

import sys

input = sys.stdin.readline

n = int(input())
order = 0
array = []

for _ in range(n) :
    age, name = input().split()
    array.append((int(age), order, name))
    order += 1


for a, o, n in array :
    print(a, n)
