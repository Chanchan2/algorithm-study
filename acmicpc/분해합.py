# https://www.acmicpc.net/problem/2231
n = int(input())

for i in range(1, n) :
    temp = i + sum(map(int, list(str(i))))
    if temp == n :
        print(i)
        break
else :
    print(0)