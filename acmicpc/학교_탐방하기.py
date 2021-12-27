# https://www.acmicpc.net/problem/13418
n, m = map(int, input())
graph = [[[], []] for _ in range(n)]

for _ in range(m) :
    a, b, c = map(int, input())
    graph[a][c].append(b)

visited = [False] * n
route = [0]
max_t = 0
# min_t = int(1e9)

while True :
    now = route.pop()
    visited[now] = True
    while graph[now][1] :
        route.append(graph[now][1].pop())
        max_t += 1

    if not route :
        route.append(graph[now][0].pop())

