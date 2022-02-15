# https://www.acmicpc.net/problem/7568

import sys

input = sys.stdin.readline

n = int(input())
array = []
weights = []
heights = []
for i in range(n) :
    weight, height = map(int, input().split())
    array.append((weight, height))
    weights.append(weight)
    heights.append(height)

weights.sort(reverse=True)
heights.sort(reverse=True)

scores = [0] * n 

for i in range(n - 1) :
    w_i, h_i = array[i]
    for j in range(i + 1, n) :
        w_j, h_j = array[j]

        if w_i > w_j and h_i > h_j :
            scores[j] += 1
        elif w_i < w_j and h_i < h_j :
            scores[i] += 1
scores = [i + 1 for i in scores]
scores = list(map(str, scores))
print(' '.join(scores))
