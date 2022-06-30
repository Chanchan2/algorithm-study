# https://www.acmicpc.net/problem/1010

import sys

input = sys.stdin.readline

def factorial(num) :
    result = 1
    while num != 0 :
        result *= num
        num -= 1
    return result

def combination(a, b) :
    return factorial(a) // (factorial(b) * factorial(a - b))

T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    print(combination(M, N))
