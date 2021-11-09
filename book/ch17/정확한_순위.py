import pprint

INF = int(1e9)

n, m = map(int, input().split())
upper = [[INF] * (n + 1) for _ in range(n + 1)]
lower = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m) :
    a, b = map(int, input().split())
    upper[a][b] = 1
    lower[b][a] = 1

for k in range(n + 1) :
    for i in range(n + 1) :
        for j in range(n + 1) :
            upper[i][j] = 1 if upper[i][k] + upper[k][j] < INF else upper[i][j]
            lower[i][j] = 1 if lower[i][k] + lower[k][j] < INF else lower[i][j]

for i in range(n + 1):
    upper[i] = [0 if j == INF else j for j in upper[i] ]
    lower[i] = [0 if j == INF else j for j in lower[i] ]

pprint.pprint(upper, width=30)
pprint.pprint(lower, width=30)
cnt = 0
for i in range(1, n + 1) :
    if sum(upper[i]) + sum(lower[i]) == n - 1 :
        print(i)
        cnt += 1

print(cnt)
    