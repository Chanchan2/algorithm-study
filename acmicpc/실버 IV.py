# https://www.acmicpc.net/problem/1358

import sys

input = sys.stdin.readline

def is_in(x1, y1, link) :
    W, H, X, Y = link
    radius =H/2
    if X <= x1 <= X+W and Y <= y1 <= Y+H :
        return True
    else :
        d_1 = ((x1 - X)**2 + (y1 - (Y + radius))**2)**0.5
        d_2 = ((x1 - (X + W))**2 + (y1 - (Y + radius))**2)**0.5
        if d_1 <= radius or d_2 <= radius :
            return True
    return False

W, H, X, Y, P = map(int, input().split())
link = (W, H, X, Y)

cnt = 0
for i in range(P) :
    x, y = map(int, input().split())
    if is_in(x, y, link) :
        cnt += 1
print(cnt)
