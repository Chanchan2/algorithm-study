# https://www.acmicpc.net/problem/14501

n = int(input())
schedule = []
dp = [0] * (n + 1)

for i in range(n) :
    t, p = map(int, input().split())
    schedule.append((t, p))
    

for i in range(n) : # 0 ~ (n - 1) 총 n일
    t, p = schedule[i]
    if t + i <= n :
        for j in range(t + i, n + 1) :
            dp[j] = max(dp[j], dp[i] + p)
print(max(dp))
