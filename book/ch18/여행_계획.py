
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))

parent = list(range(n))
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            union_parent(parent, i, j)

temp = list(map(int, input().split()))
citys = [i - 1 for i in temp]

print(parent)
answer = 'YES'

for i in range(m - 1) :
    if parent[citys[i]] != parent[citys[i + 1]] :
        answer = 'NO'
        break

print(answer)

