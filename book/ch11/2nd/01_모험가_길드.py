n = map(int, input())

warrior = list(map(int, input().split()))
warrior = sorted(warrior)

answer = 0
cnt = 0
fear = warrior[0]
for i in warrior :
    if fear != i :
        fear = i    
    cnt += 1
    if cnt == fear :
        cnt = 0
        answer += 1

print(answer)
