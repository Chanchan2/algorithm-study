# https://www.acmicpc.net/problem/5086

import sys

input = sys.stdin.readline

def check_numbers(a, b) :
    if b % a == 0 :
        return 'factor'
    elif a % b == 0 :
        return 'multiple'
    else :
        return 'neither'
a, b = map(int, input().split())
while a!=0 and b!=0 :
    print(check_numbers(a, b))
    a, b = map(int, input().split())
