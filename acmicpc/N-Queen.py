# https://www.acmicpc.net/problem/9663

# from copy import deepcopy

# n = int(input())

# graph = [[1] * n for _ in range(n)]

# def draw(graph, pos, n) :
#     temp = deepcopy(graph)
#     r, c = pos
#     temp[r] = [0] * n
#     for i in range(n) :
#         temp[i][c] = 0
#         r_1 = r + i
#         r_2 = r - i
#         c_1 = c + i
#         c_2 = c - i
#         if r_1 in range(n) :
#             if c_1 in range(n) :
#                 temp[r_1][c_1] = 0
#             if c_2 in range(n) :
#                 temp[r_1][c_2] = 0
#         if r_2 in range(n) :
#             if c_1 in range(n) :
#                 temp[r_2][c_1] = 0
#             if c_2 in range(n) :
#                 temp[r_2][c_2] = 0
#     return temp

# cnt = 0
# def find_case(graph, row, n) :
#     global cnt

#     for c in range(n) :
#         temp = deepcopy(graph)
#         if temp[row][c] == 1 :
#             if row == n - 1 :
#                 cnt += 1
        
#             else :
#                 temp = draw(temp, (row, c), n)
#                 find_case(temp, row + 1, n)

# find_case(graph, 0, n)
# print(cnt)

n = int(input())

ver = [1]*n
diag_1, diag_2 = [1]*(2*n-1), [1]*(2*n-1)

cnt = 0

def find_case(i) :
    global cnt
    if i == n :
        cnt += 1
        return
    for j in range(n) :
        if all([ver[j], diag_1[i+j], diag_2[i-j+n-1]]) :
            ver[j] = diag_1[i+j] = diag_2[i-j+n-1] = 0
            find_case(i + 1)
            ver[j] = diag_1[i+j] = diag_2[i-j+n-1] = 1

find_case(0)
print(cnt)