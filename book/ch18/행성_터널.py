import sys

input = sys.stdin.readline

def find_parent(parent, x) :
    if x != parent[x] :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
planets = []
edges = []
parent = list(range(n))

for i in range(n) :
    x, y, z = map(int, input().split())
    planets.append([i, (x, y, z)])

for i in range(3) :
    planets = sorted(planets, key = lambda x: x[1][i])
    for j in range(n - 1) :
            if find_parent(parent,planets[j][0]) == find_parent(parent,planets[j + 1][0]) :
                continue
            if planets[j][1][i] == planets[j + 1][1][i]:
                union_parent(parent, planets[j][0], planets[j + 1][0])
            else :
                distance = abs(planets[j][1][i] - planets[j + 1][1][i])
                edges.append((distance, planets[j][0], planets[j + 1][0]))

edges.sort()

result = 0
for cost, x, y in edges :
    if find_parent(parent, x) != find_parent(parent, y) :
        union_parent(parent, x, y)
        result += cost

print(result)
