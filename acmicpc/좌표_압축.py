# https://www.acmicpc.net/problem/18870

n = int(input())
numbers = list(map(int, input().split()))
num_set = sorted(set(numbers))
numbers2 = {num_set[i] : i for i in range(len(num_set))}

print(' '.join([str(numbers2[number]) for number in numbers]))
