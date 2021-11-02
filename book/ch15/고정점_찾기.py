n = int(input())
numbers = list(map(int, input().split()))
start = 0
end = n - 1

while True :
    mid = (start + end) // 2
    if numbers[mid] == mid :
        break
    elif end - start == 1 :
        mid = -1
        break
    elif numbers[mid] < mid :
        start = mid
    elif numbers[mid] > mid :
        end = mid

print(mid)

