# https://www.acmicpc.net/problem/2477

import sys

input = sys.stdin.readline

k = int(input())

x = 500
y = 500

x_list = []
y_list = []
for i in range(6) :
    dir, dis = map(int, input().split())

    if dir == 1 :
        x += dis
    elif dir == 2 :
        x -= dis
    elif dir == 3 :
        y -= dis
    else :
        y += dis
    x_list.append(x)
    y_list.append(y)

x_max = max(x_list)
x_min = min(x_list)
y_max = max(y_list)
y_min = min(y_list)
points = [(x_list[i], y_list[i]) for i in range(6)]
rec = [(x_max, y_max), (x_max, y_min), (x_min, y_max), (x_min, y_min)]
for x, y in points :
    if x not in [x_min, x_max] and y not in [y_min, y_max] :
        center = (x, y)

for point in rec :
    if point not in points :
        out_p = point

result = (x_max - x_min) * (y_max - y_min) - (abs(center[0] - out_p[0]) * abs(center[1] - out_p[1]))
print(result * k)
   
    
