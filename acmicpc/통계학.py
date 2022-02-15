# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

numbers = []

for _ in range(n) :
    numbers.append(int(input()))

if n == 1 :
    print(numbers[0])
    print(numbers[0])
    print(numbers[0])
    print(0)

else :
    numbers.sort()
    num_dict = Counter(numbers)
    a, b= num_dict.most_common(2)
    if a[1] == b[1] :
        c = b[0]
    else :
        c = a[0]


    print(round(sum(numbers) / n))
    print(numbers[n // 2])
    print(c)
    print(max(num_dict.keys()) - min(num_dict.keys()))