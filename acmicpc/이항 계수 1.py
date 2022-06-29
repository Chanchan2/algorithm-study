# https://www.acmicpc.net/problem/11050

import sys

input = sys.stdin.readline

N, K = map(int ,input().split())
if K == 0 :
    print(1)
else :
    result = 1
    for i in range(N, N - K, -1) :
        result *= i
    for i in range(1, K + 1) :
        result //= i
    print(result)