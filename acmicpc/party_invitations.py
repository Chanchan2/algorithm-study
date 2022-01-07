# https://www.acmicpc.net/problem/5856

import sys
import copy

input = sys.stdin.readline

n, g = map(int, input().split())

invited = [False] * (n + 1)
cows = [[] for _ in range(n + 1)]
groups_n = [0] * g
groups_c = []
length = []

for i in range(g) :
    temp = list(map(int, input().split()))
    length.append(temp[0])
    groups_c.append(temp[1 : ])
    for j in temp[1 : ] :
        cows[j].append(i)

invited[1] = True
for i in cows[1] :
    groups_n[i] += 1

while True :
    temp = copy.deepcopy(invited)
    for i in range(g) :
        if groups_n[i] == length[i] - 1 :
            for j in groups_c[i] :
                if not invited[j] :
                    invited[j] = True
                    for k in cows[j] :
                        groups_n[k] += 1
                        
    if temp == invited :
        break
print(sum(invited))