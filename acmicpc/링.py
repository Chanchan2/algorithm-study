# https://www.acmicpc.net/problem/3036

import sys

input = sys.stdin.readline

def get_gcd(a, b) :
    if a < b :
        a, b = b, a
    r = a % b
    if r != 0 :
        return get_gcd(b, r)
    else :
        return b

n = int(input())
wheel_list = list(map(int, input().split()))
first = wheel_list[0]
for i in wheel_list[1:] :
    gcd = get_gcd(first, i)
    print(f'{first//gcd}/{i//gcd}')