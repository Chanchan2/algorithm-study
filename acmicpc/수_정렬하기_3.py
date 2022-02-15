# https://www.acmicpc.net/problem/10989

import sys

input = sys.stdin.readline

n = int(input())

numbers = [0] * 10001

for _ in range(n) :
    temp = int(input())
    numbers[temp] += 1

for i in range(10001) :
    for j in range(numbers[i]) :
        print(i)