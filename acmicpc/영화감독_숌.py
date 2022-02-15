# https://www.acmicpc.net/problem/1436

n = int(input())

numbers = [i for i in range(666, int(1e7)) if '666' in str(i)]

print(numbers[n - 1])