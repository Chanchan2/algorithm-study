# https://school.programmers.co.kr/learn/courses/30/lessons/12978?language=python3

def solution(N, road, K):
    graph = [[int(1e9)] * (N+1) for _ in range(N + 1)]
    for i in range(N + 1) :
        graph[i][i] = 0

    for a, b, c in road :
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[a][b], c)
    
    for i in range(1, N + 1) :
        for j in range(1, N + 1) :
            for k in range(1, N + 1) :
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
                # graph[k][j] = min(graph[j][k], graph[j][i] + graph[i][k])
    
    print(graph)
    
    answer = [i for i in graph[1][1:] if i <= K]
    print(answer)
    return len(answer)

if __name__ == '__main__' :
    N = 6
    road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
    K = 4
    print(solution(N, road, K))