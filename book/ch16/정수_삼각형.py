# https://www.acmicpc.net/problem/1932
def dynamic(r, c) :
    if r == 0 :
        array[r][c] = triangle[r][c]
    else :
        if c == 0 :
            array[r][c] = array[r - 1][c] + triangle[r][c]
        elif c == r :
            array[r][c] = array[r - 1][r - 1] + triangle[r][c]
        else :
            array[r][c] = max(array[r - 1][c - 1], array[r - 1][c]) + triangle[r][c]

n = int(input())
triangle = []
array = [[0] * i for i in range(1, n + 1)]
for i in range(n) :
    triangle.append(list(map(int, input().split())))
    for j in range(i + 1) :
        dynamic(i, j)
# print(array)
print(max(array[-1]))

