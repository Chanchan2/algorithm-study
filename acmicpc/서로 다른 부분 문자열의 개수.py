# https://www.acmicpc.net/problem/11478

import sys

input = sys.stdin.readline

word = input().strip()
word_length = len(word)
word_set = set()
for i in range(1, word_length) :
    for j in range(word_length - i + 1) :
        word_set.add(word[j:j+i])

print(len(word_set) + 1)
