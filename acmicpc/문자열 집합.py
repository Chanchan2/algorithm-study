# https://www.acmicpc.net/problem/14425
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
s = []
for i in range(n) :
    s.append(input())

cnt = 0
for i in range(m) :
    if input() in s :
        cnt += 1
        
print(cnt)