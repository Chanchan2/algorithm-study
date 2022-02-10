# https://www.acmicpc.net/problem/2798

import sys

input = sys.stdin.readline


def blackjack(target, numbers) :
    answer = 0
    for f in range(len(numbers)) :
        array = []
        if numbers[f] > target :
            continue

        for s in range(f + 1, len(numbers)) :
            if numbers[f] + numbers[s] > target :
                continue

            for t in range(s + 1, len(numbers)) :
                if numbers[f] + numbers[s] + numbers[t] > target :
                    continue
                temp = numbers[f] + numbers[s] + numbers[t]
                answer = max(answer, temp)
    return answer

n, m = map(int,input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

print(blackjack(m, numbers))