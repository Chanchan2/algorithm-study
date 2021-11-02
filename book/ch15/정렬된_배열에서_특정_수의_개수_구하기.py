from bisect import bisect_left, bisect_right

def binary_search(numbers, x, start, end) :
    mid = (start + end) // 2
    if numbers[mid] == x :
        return mid
    elif numbers[mid] > x :
        return binary_search(numbers, x, start, mid)
    elif numbers[mid] < x :
        return binary_search(numbers, x, mid, end)

n, x =map(int, input().split())
numbers = list(map(int,input().split()))

# if x not in numbers :
#     print(-1)

# else :
#     cnt = 0
#     while x in numbers :
#         idx = binary_search(numbers, x, 0, len(numbers))
#         numbers.pop(idx)
#         cnt += 1
    
#     print(cnt)

start = bisect_left(numbers, x)
end = bisect_right(numbers, x)
result = end - start
if result == 0 :
    result = -1

print(result)