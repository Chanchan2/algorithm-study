# https://www.acmicpc.net/problem/9375

import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T) :
    clothes_dict = {}
    n = int(input())
    for i in range(n) :
        item, part = input().split()
        if part not in clothes_dict.keys() :
            clothes_dict[part] = ['None']
        clothes_dict[part].append(item)

    result = 1
    for value in clothes_dict.values() :
        result *= len(value)

    print(result - 1)