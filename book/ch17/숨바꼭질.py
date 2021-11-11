import heapq

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dist = 0
q = []
heapq.heappush(q, (dist, 1))
distance[1] = 0

while q :
    dist, now = heapq.heappop(q)
    dist += 1
    if visited[now] :
        continue
    visited[now] = True
    for i in graph[now] :
        distance[i] = min(distance[i], dist)
        heapq.heappush(q, (dist, i))

maximum = max(distance[1:])
num = distance.index(maximum)
cnt = distance.count(maximum)
print(num, maximum, cnt)