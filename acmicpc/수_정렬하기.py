# https://www.acmicpc.net/problem/2750

import sys

input = sys.stdin.readline

n = int(input())

numbers = []
for _ in range(n) :
    numbers.append(int(input()))

numbers.sort()
for i in range(n) :
    print(numbers[i])