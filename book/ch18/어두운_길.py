def find_parent(parent, x ) :
    if parent[x] != x :
        parent[x]  = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())
edges = []
parent = list(range(n))
result = 0

for _ in range(m) :
    x, y, z = map(int, input().split())
    edges.append((z, x ,y))
edges.sort()

for cost, x, y in edges :
    if find_parent(parent, x) != find_parent(parent, y) :
        union_parent(parent, x, y)
    else :
        result += cost

print(result)