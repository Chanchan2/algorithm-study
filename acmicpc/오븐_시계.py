# https://www.acmicpc.net/problem/2525

a, b = map(int, input().split())
c = int(input())
b += c

while b >= 60 :
    b = b - 60
    a += 1

a = a % 24

print(a, b)