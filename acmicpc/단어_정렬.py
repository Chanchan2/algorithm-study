# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

n = int(input())

words = []

for _ in range(n) :
    words.append(input().strip())

words = list(set(words))
words = sorted(words, key = lambda x : (len(x), x))
for w in words :
    print(w)