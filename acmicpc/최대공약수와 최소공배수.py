# https://www.acmicpc.net/problem/2609

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

a, b = map(int, input().split())
if b > a :
    a, b = b, a
gcd = get_gcd(a, b)
print(gcd)
print(int(a * b / gcd))