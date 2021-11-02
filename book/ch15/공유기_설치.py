# https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline


n, c = map(int,input().split())
inf = int(1e9)

houses = []
for _ in range(n) :
    houses.append(int(input()))

houses.sort()

start = 1
end = houses[-1] - houses[0]

min_dist = inf
while start <= end :
    mid = (end + start) // 2

    cnt = 1 # 0번째 집 설치

    temp = houses[0]
    for dist in houses[1:] :
        if dist - temp >= mid : # 두집 사이 거리가 mid값보다 이상이면 설치
            cnt += 1
            temp = dist

    if cnt >= c : # 설치 대수가 많거나 같을 때
        start = mid + 1
        result = mid
    else : # 설치 대수가 적을 때
        end = mid - 1

print(result)
