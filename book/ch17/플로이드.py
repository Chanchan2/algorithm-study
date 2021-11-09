# https://www.acmicpc.net/problem/11404
import sys

input = sys.stdin.readline

inf = int(1e9)
n = int(input())
m = int(input())
route = []
graph = [[inf] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1) :
    graph[a][a] = 0

for _ in range(m) : # a에서 b로가는 비용 c
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) #중복노선의 경우 최소 비용입력

for k in range(1, n + 1) :
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])  
# i에서 j로 가는 비용 vs i에서 k거쳐 j로 가는 비용

for i in range(1, n + 1) :
    print(*[0 if k == inf else k for k in graph[i][1:]])
