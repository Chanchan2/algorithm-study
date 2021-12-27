from copy import deepcopy
import heapq
INF = int(1e9)

def eat (array, baby, targets) :
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    distance = [[INF] * len(array) for _ in range(len(array))]
    visited = [[False] * len(array) for _ in range(len(array))]
    temp = deepcopy(array)
    r_s, c_s, s, e = baby
    q = []
    heapq.heappush(q, (0, r_s, c_s))
    distance[r_s][c_s] = 0

    while q :
        dist, r_n, c_n = heapq.heappop(q)
        visited[r_n][c_n] = True
        for dr, dc in move :
            r = r_n + dr
            c = c_n + dc
            if 0 <= r < len(temp) and 0 <= c < len(temp) :
                if temp[r][c] > s :
                    continue
                distance[r][c] = min(distance[r][c], dist + 1)
                if not visited[r][c] :
                    heapq.heappush(q, (distance[r][c], r, c))
            else :
                continue
    target_dist = []

    for r_t, c_t in targets :
        if distance[r_t][c_t] != INF :
            target_dist.append((distance[r_t][c_t], r_t, c_t))
    
    if target_dist :
        target_dist = sorted(target_dist, key = lambda x : (x[0], x[1], x[2]))
        time, r_t, c_t = target_dist[0]
        array[r_t][c_t] = 9
        array[r_s][c_s] = 0
        e += 1
        if e == s :
            s += 1
            e = 0
            baby = [r_t, c_t, s, e]
        return time
    else :
        return 0

n = int(input())
graph = []
fishes = {}

for i in range(n) :
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(n) :
        if line[j] == 9 :
            baby = [i, j, 2, 0]  # row, col, size, eat
        elif line[j] != 0 :
            k = line[j]
            if k not in fishes.keys() :
                fishes[k] = [(i, j)]
            else :
                fishes[k].append((i, j))

time = 0
while fishes.keys() :
    if min(fishes.keys()) >= baby[2] :
        break
    target_keys = [k for k in fishes.keys() if k < baby[2]]
    targets = []
    for k in target_keys :
        for v in fishes[k] :
            targets.append(v)
    feeding_time = eat(graph, baby, targets)
    print(graph)
    print(baby)
    if feeding_time == 0 :
        break
    time += feeding_time
    print(targets)




print(time)