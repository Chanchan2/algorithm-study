# https://www.acmicpc.net/problem/14889

import sys

input = sys.stdin.readline

def cal_status(members, graph) :
    l = len(members)
    status = 0
    for i in range(l) :
        mem1 = members[i]
        for j in range(i, l) :
            mem2 = members[j]
            status += graph[mem1][mem2] + graph[mem2][mem1]
    return status

def dfs(idx, cnt) :
    if cnt == n // 2 :
        global diff
        start_members = []
        link_members = []
        for i in range(n) :
            if visited[i] :
                start_members.append(i)
            else :
                link_members.append(i)
        start = cal_status(start_members,graph)
        link  = cal_status(link_members, graph)
        diff = min(diff, abs(start - link))
        return

    for i in range(idx,  n) :
        if not visited[i] :
            visited[i] = True
            dfs(idx + 1, cnt + 1)
            visited[i] = False
    
n = int(input())
visited = [False if i != 0 else True for i in range(n)]
print(visited)
graph = [list(map(int, input().split())) for _ in range(n)]
diff = int(1e9)

dfs(1, 1)
print(diff)
