# https://www.acmicpc.net/problem/1934

import sys

input = sys.stdin.readline

def get_gcd(p, q) :
    r = -1
    while True :
        r = p % q
        if r == 0 :
            break
        p, q = q, r
    return q

def get_lcm(p, q) :
    gcd = get_gcd(p, q)
    return p*q//gcd

n = int(input())

for i in range(n) :
    a, b = map(int, input().split())
    if b > a :
        a, b = b, a
    print(get_lcm(a, b))