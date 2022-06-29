# https://www.acmicpc.net/problem/11051

import sys

input = sys.stdin.readline

def factorial(N) :
    result = 1
    while N :
        result *= N
        N -= 1
    return result

def combination(N, K) :
    if K == 0 :
        return 1
    else :
        return factorial(N) // (factorial(K) * factorial(N - K))
N, K = map(int, input().split())
print(combination(N, K) % 10007)