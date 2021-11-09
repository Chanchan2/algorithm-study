# # https://www.acmicpc.net/problem/18353
# import sys
# input = sys.stdin.readline

# n = int(input())
# soldiers = map(int, input().split())
# num_sols = list(enumerate(soldiers))
# num_sols.sort(key = lambda x : x[1], reverse = True)
# # print(num_sols)
# dp = [1] * n


# for i in range(1, n) :
#     for j in range(i) :
#         if num_sols[j][0] < num_sols[i][0] and num_sols[j][1] > num_sols[i][1]:
#             dp[i] = max(dp[i], dp[j] + 1)
    
# print(n - max(dp))

import sys
input = sys.stdin.readline

n = int(input())
soldiers = list(map(int, input().split()))
dp = [1] * n


for i in range(1, n) :
    for j in range(i) :
        if soldiers[j] > soldiers[i] :
            dp[i] = max(dp[i], dp[j] + 1)
    
print(n - max(dp))
