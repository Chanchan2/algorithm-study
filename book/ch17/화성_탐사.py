import heapq

INF = int(1e9)
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

t = int(input())

for _ in range(t) :
    n = int(input())
    mars = []
    distance = [[INF] * n for k in range(n)]

    for i in range(n) :
        mars.append(list(map(int, input().split())))

    q = []
    heapq.heappush(q, (0, 0))
    distance[0][0] = mars[0][0]
    while q :
        r, c = heapq.heappop(q)
        for dr, dc in move :
            r_n = r + dr
            c_n = c + dc
            if 0 <= r_n < n and 0 <= c_n < n:
                if distance[r][c] + mars[r_n][c_n] < distance[r_n][c_n] :
                    distance[r_n][c_n] = distance[r][c] + mars[r_n][c_n]
                    heapq.heappush(q, (r_n, c_n))

    print(distance[-1][-1])