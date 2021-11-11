from collections import deque
import copy

N = int(input())
times = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
q= deque()

for i in range(1, N + 1) :
    temp = list(map(int, input().split()))
    times[i] = temp[0]      #강의 시간 저장

    if len(temp) > 2 :
        for precourse in temp[1 : -1] :
            graph[precourse].append(i)      #선수과정에 상위과정 저장
            indegree[i] += 1
    else :
        q.append(i)   # 진입차수 0인 경우 저장

def topology_sort() :
    result = copy.deepcopy(times)

    while q :
        now = q.popleft()
        for i in graph[now] :
            result[i] = max(result[i], result[now] + times[i])
            indegree[i] -= 1
            if indegree[i] == 0 :
                q.append(i)
        # print(q)

    for i in range(1, N + 1) :
        print(result[i])

topology_sort()
