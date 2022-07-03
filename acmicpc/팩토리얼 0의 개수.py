# https://www.acmicpc.net/problem/1676

import sys

input = sys.stdin.readline

def factorial(num) :
    result = 1
    while num != 0 :
        result *= num
        num -= 1

    return result

N = int(input())
fact = str(factorial(N))
cnt = 0
for i in fact[::-1] :
    if i == '0' :
        cnt += 1
    else :
        break
    
print(cnt)