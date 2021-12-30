# https://www.acmicpc.net/problem/1439

s = list(input())
cnt = 1
temp = s[0]

for i in s[1:] :
    if temp != i :
        cnt +=1
        temp = i

cnt = cnt // 2
print(cnt)
