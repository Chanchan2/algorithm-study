# https://www.acmicpc.net/problem/17178
# Stack

import sys
import copy

input = sys.stdin.readline

n = int(input())

lines = []

for _ in range(n) :
    line = list(input().split())
    for i in line :
        letter, num = i.split('-')
        lines.append((letter, int(num)))

temp = copy.deepcopy(lines)
temp = sorted(temp, key = lambda x : (x[0], x[1]))

order = 0
waiting = []
result = 'GOOD'
while lines or waiting :
    if lines and temp.index(lines[0]) == order :
        lines.pop(0)
        order += 1
    elif waiting and temp.index(waiting[-1]) == order:
        waiting.pop()
        order += 1
    elif temp[order] in waiting :
        result = 'BAD'
        break
    else :
        waiting.append(lines.pop(0))

print(result)

